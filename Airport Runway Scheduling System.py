# ------------------------------------------------------
# AIRPORT RUNWAY SCHEDULING SYSTEM - STREAMLIT VERSION
# Algorithms: Backtracking, Dynamic Programming, Priority Queue
# ------------------------------------------------------

import pandas as pd
import streamlit as st

class Flight:
    def init(self, fid, arrival, duration, priority):
        self.id = fid
        self.arrival = arrival
        self.duration = duration
        self.priority = priority


# ---------------- BACKTRACKING ----------------

def backtracking_schedule():
    flights = [
        Flight("AI101", 1, 3, 0),
        Flight("UK202", 2, 2, 0),
        Flight("EK303", 3, 4, 0)
    ]
    runways = [0, 0]
    data = []

    for f in flights:
        for r in range(2):
            start = max(f.arrival, runways[r])
            end = start + f.duration
            data.append({
                "Flight": f.id,
                "Runway": r,
                "Start": start,
                "End": end
            })
            runways[r] = end

    df = pd.DataFrame(data)
    return df

# ---------------- DYNAMIC PROGRAMMING ----------------
def dynamic_programming_schedule():
    arrival = [1, 2, 3]
    duration = [3, 2, 4]
    n = len(arrival)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        arr = arrival[i - 1]
        dur = duration[i - 1]
        dp[i] = min(dp[i - 1] + dur, arr + dur)

    df = pd.DataFrame({
        "Flight": [f"F{i}" for i in range(1, n + 1)],
        "Arrival": arrival,
        "Duration": duration,
        "Completion_Time": [dp[i] for i in range(1, n + 1)]
    })
    total = dp[n]
    return df, total

# ---------------- PRIORITY QUEUE ----------------
def priority_queue_schedule():
    flights = [
        Flight("AI101", 1, 3, 2),
        Flight("UK202", 2, 2, 1),
        Flight("EK303", 3, 4, 3),
        Flight("QR404", 1, 2, 2)
    ]
    flights.sort(key=lambda x: x.priority)

    runways = [0, 0]
    data = []

    for f in flights:
        r = 0 if runways[0] <= runways[1] else 1
        start = max(f.arrival, runways[r])
        end = start + f.duration
        runways[r] = end
        data.append({
            "Flight": f.id,
            "Runway": r,
            "Start": start,
            "End": end,
            "Priority": f.priority
        })

    df = pd.DataFrame(data)
    return df

# ---------------- STREAMLIT UI ----------------
st.set_page_config(page_title="Airport Runway Scheduler", layout="wide")

st.title("✈ Airport Runway Scheduling System")
st.markdown("### Compare Backtracking, Dynamic Programming, and Priority Queue Approaches")

algo = st.sidebar.radio(
    "Select an Algorithm:",
    ["Backtracking", "Dynamic Programming", "Priority Queue"]
)

st.sidebar.markdown("---")
st.sidebar.info("This system schedules flights on runways using different algorithmic techniques.")

if algo == "Backtracking":
    st.subheader("🧩 Backtracking Algorithm")
    st.write("Explores all possible valid schedules to ensure no runway conflict.")
    df = backtracking_schedule()
    st.dataframe(df, use_container_width=True)
    st.bar_chart(df.set_index("Flight")[["Start", "End"]])

elif algo == "Dynamic Programming":
    st.subheader("🧮 Dynamic Programming Algorithm")
    st.write("Optimizes total completion time (minimizes delay).")
    df, total = dynamic_programming_schedule()
    st.dataframe(df, use_container_width=True)
    st.metric("Minimum Total Completion Time", f"{total}")
    st.line_chart(df.set_index("Flight")[["Completion_Time"]])

elif algo == "Priority Queue":
    st.subheader("🏆 Priority Queue Algorithm")
    st.write("Schedules flights efficiently by giving priority to emergency or high-priority flights.")
    df = priority_queue_schedule()
    st.dataframe(df, use_container_width=True)
    st.bar_chart(df.set_index("Flight")[["Start", "End"]])

st.markdown("---")
st.caption("Developed for DAA Mini Project — Demonstrating Scheduling Algorithms in Real-World Scenarios")

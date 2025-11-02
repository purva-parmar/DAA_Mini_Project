# ------------------------------------------------------
# AIRPORT RUNWAY SCHEDULING SYSTEM - STREAMLIT VERSION
# Algorithms: Backtracking, Dynamic Programming, Priority Queue
# ------------------------------------------------------

import pandas as pd

# ---------------- FLIGHT CLASS ----------------
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

import numpy as np
import pandas as pd

data = pd.read_csv("data.csv")

def sorting(dat):

    sort_data = data[data["time"] == dat]

    chay = sort_data[["tip", "total_bill"]].sort_values(["tip", "total_bill"])

    print(chay)

    tip, cost = list(chay["tip"]), list(chay["total_bill"])

    procent = []

    for i in range(len(cost)):
        proc = round((tip[i] / cost[i]) * 100)
        procent.append(proc)

    print(round(sum(procent)/len(procent)))

sorting("Lunch")
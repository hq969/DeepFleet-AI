import pandas as pd
from model import FleetModel

data = pd.read_csv("data/delivery_logs.csv")
X = data[["distance"]]
y = data["time"]

model = FleetModel()
model.train(X, y)

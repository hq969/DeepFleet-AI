import pandas as pd
from model import FleetModel

model = FleetModel()
model.train([[10], [20]], [15, 30])
print(model.predict([[25]]))

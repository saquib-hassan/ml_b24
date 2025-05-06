
2 + 2
!pip install pandas
import pandas as pd
import numpy as np

!pip install matplotlib
import matplotlib.pyplot as plt
!pip install scikit-learn
from sklearn.linear_model import LinearRegression

demo_data = {"candy": [1, 2, 3, 4, 5],
    "price": [2, 4, 6, 8, 10.5]}

df = pd.DataFrame(demo_data)
df.head()

df.shape
df.tail

model = LinearRegression()
model.fit(df[["candy"]], df[["price"]])

model.predict([[12]])

model.coef_
model

from sklearn.metrics import r2_score
predicted_price = model.predict(df[["candy"]])
predicted_price
r2_score(df[["price"]], predicted_price)

df["predicted_price"] = predicted_price
df.head()
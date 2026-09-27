import numpy as np
import pandas as pd

marks=np.array([72,85,91,68,77])
print("Marks:",marks)
print("Mean:",np.mean(marks))
print("Maximum:",np.max(marks))
print("Minimum:",np.min(marks))

data={
    "Name":["Amit","Riya","Sourav","Neha","Rahul"],
    "Attendance":[88,92,76,95,81],
    "Marks":[72,85,68,91,77]
}
df=pd.DataFrame(data)
print("\n__First Five Reord__")
print(df.head())

print("\n__Data Information__")
print(df.info())
print("\n__Statistical Summary__")
print(df.describe())

print("\nAverage Marks:",df["Marks"].mean())


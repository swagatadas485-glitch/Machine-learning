import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# 1. Load dataset
iris = load_iris()

df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["target"] = iris.target

# 2. Basic Exploration
print("---- First Five Rows ----")
print(df.head())

print("\n---- Dataset Information ----")
df.info()

print("\n---- Statistical Summary ----")
print(df.describe())

print("\n---- Missing Values ----")
print(df.isnull().sum())

# 3. Correlation Heatmap
print("\n---- Correlation Matrix ----")

corr = df.corr(numeric_only=True)
print(corr)

plt.figure(figsize=(8, 6))

sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")
plt.show()

# Find strongest positive correlation
corr_matrix = df.drop("target", axis=1).corr()

upper = corr_matrix.where(
    np.triu(np.ones(corr_matrix.shape), k=1).astype(bool)
)

strongest = upper.stack().idxmax()
value = upper.stack().max()

print("\nStrongest Positive Correlation:")
print(strongest)
print("Correlation:", value)
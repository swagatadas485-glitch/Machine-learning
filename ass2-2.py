import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# 1. Load dataset
iris = load_iris()

df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["target"] = iris.target

# 2. Basic EDA
print("---- First Five Rows ----")
print(df.head())

print("\n---- Dataset Information ----")
df.info()

print("\n---- Statistical Summary ----")
print(df.describe())

print("\n---- Missing Values ----")
print(df.isnull().sum())

# 3. Correlation matrix
print("\n---- Correlation Matrix ----")
print(df.corr(numeric_only=True))

# 4. Scatter plot
plt.figure(figsize=(7, 5))

sns.scatterplot(
    data=df,
    x="sepal length (cm)",
    y="petal length (cm)",
    hue="target"
)

plt.title("Sepal Length vs Petal Length")
plt.show()

# 5. Histogram
plt.figure(figsize=(7, 5))

sns.histplot(df["sepal length (cm)"], kde=True)

plt.title("Distribution of Sepal Length")
plt.show()

# 6. Boxplots for all numerical attributes
plt.figure(figsize=(10, 6))

sns.boxplot(data=df.drop("target", axis=1))

plt.title("Boxplots of All Numerical Attributes")
plt.xticks(rotation=45)

plt.show()
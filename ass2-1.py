import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# 1. Load dataset
iris = load_iris()

# Create DataFrame
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df["target"] = iris.target

# 2. Basic EDA
print("First 5 rows:")
print(df.head())

print("\nDataset Information:")
df.info()

print("\nStatistical Summary:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

# 3. Correlation
print("\nCorrelation Matrix:")
print(df.corr(numeric_only=True))

# 4. Scatter Plot
sns.scatterplot(
    data=df,
    x="sepal length (cm)",
    y="petal length (cm)",
    hue="target"
)

plt.title("Sepal Length vs Petal Length")
plt.show()

# 5. Histogram
sns.histplot(df["sepal length (cm)"], kde=True)

plt.title("Distribution of Sepal Length")
plt.show()
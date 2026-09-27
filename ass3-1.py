import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder, StandardScaler

# Set seed for reproducibility
np.random.seed(42)
n_samples = 10

# 1. Create the synthetic dataset
data = {
    "Age": np.random.randint(22, 60, size=n_samples).astype(float),
    "Salary": np.random.randint(40000, 120000, size=n_samples).astype(float),
    "Department": np.random.choice(
        ["HR", "IT", "Sales", "Finance"], size=n_samples
    ),
    "Years_of_Experience": np.random.randint(1, 35, size=n_samples).astype(
        float
    ),
}
df = pd.DataFrame(data)

# 2. Inject missing values deliberately
df.loc[2, "Age"] = np.nan
df.loc[5, "Salary"] = np.nan
df.loc[7, "Years_of_Experience"] = np.nan

print("--- Step 1: Dataset with Missing Values ---")
print(df)

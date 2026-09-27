import pandas as pd

# Create DataFrame
data = {
    "Student_Name": ["Swagata", "sonia", "amit", "rakesh", "Riya"],
        "Roll_Number": [102, 132, 143, 104, 105],
        "Marks": [85, 76, 92, 68, 88],
        "Attendance": [90, 85, 95, 80, 92]
}

df = pd.DataFrame(data)

print("Complete DataFrame:")
print(df)

# Filter students with marks above 80
result = df[df["Marks"] > 80]

print("\nStudents who scored above 80:")
print(result)
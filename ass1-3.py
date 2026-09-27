import pandas as pd

# Create DataFrame
data = {
    "Student_Name": ["Swagata", "sonia", "amit", "rakesh", "Riya"],
    "Roll_Number": [102, 132, 143, 104, 105],
    "Marks": [85, 76, 92, 68, 88],
    "Attendance": [90, 85, 95, 80, 92]
}

df = pd.DataFrame(data)

# Function to calculate grade
def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"

# Add Grade column dynamically
df["Grade"] = df["Marks"].apply(calculate_grade)

print(df)
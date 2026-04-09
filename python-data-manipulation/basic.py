import pandas as pd

data_csv = pd.read_csv("data.csv")
data_json = pd.read_json("data.json")

# From a dictionary (most common way)
employees = pd.DataFrame({
    "name":       ["Alice", "Bob", "Charlie", "Diana", "Eve"],
    "department": ["Engineering", "Sales", "Engineering", "HR", "Sales"],
    "salary":     [75000, 52000, 82000, 61000, 54000],
    "years_exp":  [5, 2, 8, 3, 1],
    "remote":     [True, False, True, False, True],
})

# Quick ways to inspect data
#print("All info: ", employees.info()) # indexes, non-null, num. of rows, num. of columns, types, memory usage
#print("====")
#print("Shape (rows, columns):", employees.shape)
#print("====")
#print("Column names:", list(employees.columns))
#print("====")
#print("Data types:\n", employees.dtypes)
#print("====")


#print(data_csv.to_string()) #all

#print(data_json.head(10))

#print(data_json.tail()) #5 last rows

# Save to CSV
employees.to_csv("employees.csv", index=False)


# ---------------------- #
#       SELECTING        #
# ---------------------- #

#print(employees[["name", "salary"]])


# Select rows by position with .iloc[row, col] NUMERIC POSITION
print("First row:", employees.iloc[0].to_dict())
print("Rows 1-3, columns 0-2:")
print(employees.iloc[0:3, 0:3])
print()

# Select rows by label with .loc[row, col] LABEL POSITION
print("Column 'name' for rows 0-2:")
print(employees.loc[0:2, "name"])
print()

# ---------------------- #
#       FILTERING        #
# ---------------------- #

# Filter with a condition
high_earners = employees[employees["salary"] > 60000]
print("Salary > 60,000:")
print(high_earners)
print()

# Multiple conditions: & (and), | (or), ~ (not)
# IMPORTANT: wrap each condition in parentheses!
senior_engineers = employees[(employees["department"] == "Engineering") & (employees["years_exp"] >= 5)]
print("Senior Engineers (5+ years):")
print(senior_engineers)
print()

# Filter with .isin() for multiple values
sales_or_hr = employees[employees["department"].isin(["Sales", "HR"])]
print("Sales or HR:")
print(sales_or_hr)
print()

# Filter strings with .str methods (str - converts EACH value, to_string() - would convert Series to looong string)
names_with_a = employees[employees["name"].str.startswith("A")]
print("Names starting with 'A':")
print(names_with_a)
print()

# ---------------------- #
#    ADDING & MODIFYING  #
# ---------------------- #

# New column from calculation
employees["monthly_salary"] = employees["salary"] / 12

# New column from condition
employees["senior"] = employees["years_exp"] >= 5

# Modify existing column
employees["salary"] = employees["salary"] * 1.05  # 5% raise for everyone!



# ---------------------- #
#         SORTING        #
# ---------------------- #
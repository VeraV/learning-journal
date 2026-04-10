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
#print("First row:", employees.iloc[0].to_dict())
#print("Rows 1-3, columns 0-2:")
#print(employees.iloc[0:3, 0:3])
#print()

# Select rows by label with .loc[row, col] LABEL POSITION
#print("Column 'name' for rows 0-2:")
#print(employees.loc[0:2, "name"])
#print()

# ---------------------- #
#       FILTERING        #
# ---------------------- #

# Filter with a condition
high_earners = employees[employees["salary"] > 60000]
#print("Salary > 60,000:")
#print(high_earners)
#print()

# Multiple conditions: & (and), | (or), ~ (not)
# IMPORTANT: wrap each condition in parentheses!
senior_engineers = employees[(employees["department"] == "Engineering") & (employees["years_exp"] >= 5)]
#print("Senior Engineers (5+ years):")
#print(senior_engineers)
#print()

# Filter with .isin() for multiple values
sales_or_hr = employees[employees["department"].isin(["Sales", "HR"])]
#print("Sales or HR:")
#print(sales_or_hr)
#print()

# Filter strings with .str methods (str - converts EACH value, to_string() - would convert Series to looong string)
names_with_a = employees[employees["name"].str.startswith("A")]
#print("Names starting with 'A':")
#print(names_with_a)
#print()

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

# Sort by one column
by_salary = employees.sort_values("salary", ascending=False)
#print(by_salary[["name", "salary"]])

# Sort by multiple columns
by_dept_exp = employees.sort_values(["department", "years_exp"], ascending=[True, False])
#print("Sorted by department, then experience:")
#print(by_dept_exp[["name", "department", "years_exp"]])


# -------------------------- #
#   Grouping & Aggregation   #
# -------------------------- #


# Average salary per department
avg_by_dept = employees.groupby("department")["salary"].mean()
#print("Average salary by department:")
#print(avg_by_dept)

# Multiple aggregations at once
dept_stats = employees.groupby("department").agg( #agg - alias for aggregate (USE AGG!)
    avg_salary=("salary", "mean"), #The pattern is always res_col_name=("source_column", "operation").
    total_employees=("name", "count"),
    max_experience=("years_exp", "max"),
)
#print("Department statistics:")
#print(dept_stats)

# Quick summary statistics
#print("Overall summary:")
#print(employees.describe())
#print()

employees["senior"].nunique() # Number of UNIQUE values

###### Standard Deviation - .std() #####

# Tells how spread out the values are from the mean
#   - a small std means values are clustered together,
#   - a large std means they're all over the place

stable = pd.Series([100, 102, 98, 101, 99])
wild   = pd.Series([50, 200, 10, 180, 60])

stable.mean()  # 100.0
stable.std()   # ~1.6  — very tight, values barely move

wild.mean()    # 100.0
wild.std()     # ~82.8 — huge spread, values jump everywhere



# Both teams have the same total sales (200).
# Which team is more consistent?
# (comparing with each team's avg)

teams = pd.DataFrame({
    "team":   ["Alpha", "Alpha", "Alpha", "Alpha",
               "Beta",  "Beta",  "Beta",  "Beta"],
    "month":  ["Jan", "Feb", "Mar", "Apr",
               "Jan", "Feb", "Mar", "Apr"],
    "sales":  [50, 48, 52, 50,
               20, 80, 30, 70],
})

teams.groupby("team").agg(consistency=("sales", "std"))



###### Percentile - .quantile(0.75) ######

# What value sits at the X% mark if I sort all the data?
# Think of it as dividing your data into 100 equal slices.

salaries = pd.Series([30000, 40000, 50000, 70000, 120000])

salaries.quantile(0.25)  # 40000 — 25% of people earn less than this
salaries.quantile(0.50)  # 50000 — the median, exactly the middle
salaries.quantile(0.75)  # 70000 — 75% earn less, only 25% earn more
salaries.quantile(0.90)  # 100000 — top 10% threshold
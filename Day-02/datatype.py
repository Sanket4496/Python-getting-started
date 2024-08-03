Employee_name = "Ram"
Age=55
Height=150.6

type(Employee_name)
type(Age)
type(Height)

type(Height) is int
type(Age) is float
type(Employee_name) is str

# Converting one data type to another
# Before converting
type(Height)
# Converting Height to int and store it in another variable
ht=int(Height)
type(ht)
# Converting Height to int and store it in the same variable
Height=int(Height)
type(Height)

# Accepted Coercing 
# An integer is enclosed inside a quotes
Salary_tier='1'
type(Salary_tier)

Salary_tier=int(Salary_tier)
type(Salary_tier)

# Rejected Coercing
Employee_name="Ram"
Employee_name=float(Employee_name)

def calculate_gross_salary(basic, allowance):
    return basic + allowance


def calculate_tax(gross, rate):
    return gross * rate / 100


def calculate_net_salary(gross, tax):
    return gross - tax


name = input("Enter employee name: ")

basic = float(input("Enter basic salary: "))
allowance = float(input("Enter allowance: "))
rate = float(input("Enter tax rate: "))

gross = calculate_gross_salary(basic, allowance)
tax = calculate_tax(gross, rate)
net = calculate_net_salary(gross, tax)

print("\nEmployee Name:", name)
print("Gross Salary:", gross)
print("Tax:", tax)
print("Net Salary:", net)
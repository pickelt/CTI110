# Tyler Pickel
# Date: 10/26/2025
# P3HW2_Salary_PickelTyler.py
# This program calculates an employee’s gross pay, accounting for overtime,
# and displays all pay details formatted in aligned columns.

# Pseudocode:
# 1. Ask for employee name, hours worked, and pay rate.
# 2. If hours worked > 40, calculate overtime hours and overtime pay.
# 3. Calculate regular pay and total gross pay.
# 4. Display results with formatted alignment.

# Get employee details
name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))

print('-----------------------------------------')

# Check for overtime
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    reg_pay = 40 * pay_rate
else:
    overtime_hours = 0
    overtime_pay = 0
    reg_pay = hours_worked * pay_rate

# Calculate gross pay
gross_pay = reg_pay + overtime_pay

# Display results
print(f'Employee name:  {name}')
print()
print('Hours Worked   Pay Rate   OverTime   OverTime Pay   RegHour Pay   Gross Pay')
print('----------------------------------------------------------------------------')
print(f'{hours_worked:<13.1f}{pay_rate:<11.1f}{overtime_hours:<10.1f}'
      f'{overtime_pay:<15.2f}${reg_pay:<13.2f}${gross_pay:<.2f}')

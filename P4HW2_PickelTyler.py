# Tyler Pickel
# Date: 11/9/2025
# P4HW2 - Payroll Calculator with Overtime
# This program calculates pay for multiple employees until user enters "Done".

"""
Pseudocode
- Start totals at 0
- Ask for employee name or Done
- While name is not Done:
    - Ask for hours and rate
    - If hours > 40, find overtime hours and pay
    - Find regular pay and gross pay
    - Add each amount to totals
    - Show employee’s pay info
    - Ask for next name
- When Done, print total counts and pay amounts
"""

# totals for all employees
total_employees = 0
total_overtime_pay = 0.0
total_regular_pay = 0.0
total_gross_pay = 0.0

# get first name
name = input("Enter employee's name or \"Done\" to terminate: ")

# loop until user types Done
while name != "Done":
    hours = float(input("How many hours did " + name + " work? "))
    rate = float(input("What is " + name + "'s pay rate? "))

    # check for overtime
    if hours > 40:
        overtime_hours = hours - 40
        overtime_pay = overtime_hours * rate * 1.5
        regular_pay = 40 * rate
    else:
        overtime_hours = 0
        overtime_pay = 0
        regular_pay = hours * rate

    gross_pay = regular_pay + overtime_pay

    # display one employee's results
    print("\nEmployee name:  " + name + "\n")
    print("Hours Worked\tPay Rate\tOverTime\tOverTime Pay\tRegHour Pay\tGross Pay")
    print("--------------------------------------------------------------------------")
    print(format(hours, ".1f"), "\t\t",
          format(rate, ".2f"), "\t\t",
          format(overtime_hours, ".1f"), "\t\t",
          "$" + format(overtime_pay, ".2f"), "\t\t",
          "$" + format(regular_pay, ".2f"), "\t\t",
          "$" + format(gross_pay, ".2f"))
    print()

    # update totals
    total_employees += 1
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay

    # ask for next employee
    name = input("Enter employee's name or \"Done\" to terminate: ")

# show totals when user types Done
print("\nTotal number of employees entered: ", total_employees)
print("Total amount paid for overtime: $" + format(total_overtime_pay, ".2f"))
print("Total amount paid for regular hours: $" + format(total_regular_pay, ".2f"))
print("Total amount paid in gross: $" + format(total_gross_pay, ".2f"))

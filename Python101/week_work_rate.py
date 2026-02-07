# Get the number of hours worked.
hours_worked = input('How many hours you work this week: ')

week_hours = float(hours_worked)

# Get the hourly pay rate.
base_hour = 40.00
pay_rate = 17.00
normal_week = week_hours * pay_rate
extra_payrate = pay_rate * 2.0

extra_pay = (week_hours - base_hour) * extra_payrate

extra_week = normal_week + extra_pay


# If the employee worked more than 40 hours: Calculate and display the gross pay with overtime.
if week_hours <= 40 or week_hours ==40:
    print('Your week payment is:', f'{normal_week:.2f}')
else:
    # Else: Calculate and display the gross pay as usual.
    print(f'Your work more than 40h this week, your week payment is: {extra_week:.2f}')

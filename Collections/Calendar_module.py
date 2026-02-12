import calendar
date_input=input()
m, d, y=map(int,date_input.split())
day_number=calendar.weekday(y, m, d)
day_name=calendar.day_name[day_number]
print(day_name.upper())

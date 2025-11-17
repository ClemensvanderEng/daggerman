import datetime

print("Enter your year of birth.")
year = input(int)
print("Enter your month of birth.")
month = input(int)
print("Enter your day of birth.")
day = input(int)

now = datetime.datetime.now()

age = now.year-year

if now.month < month:
    age -= 1
elif now.month == month:
    if now.day < day:
        age -= 1
    elif now.day == day:
        print ("happy birthday")

print ("You are",age)

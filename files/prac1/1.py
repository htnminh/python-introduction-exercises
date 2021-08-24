# Exercise 1
# Write a program to display the number of days in a month, given the month and the year

month = int(input())
year = int(input())

def div(a, b):
    if a % b == 0: return True
    return False

def leap(year):
    if (div(year, 4) and (not div(year, 100))) or (div(year, 400)):
        return True
    return False

#                    1   2   3   4   5   6   7   8   9  10  11  12
days_in_month = [-1, 31, -1, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if month == 2:
    if leap(year):
        print(29)
    else:
        print(28)
else:
    print(days_in_month[month])
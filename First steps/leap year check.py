# checking a range of years
def check_leap_years(start, end):
    for year in range(start, end):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            # you're only checking if the year is divisible by 4 to determine if it's a leap year.
            # While this is partially correct, the actual rule is a bit more complex:
            # a year is a leap year if it is divisible by 4, but not by 100, unless it is also divisible by 400.
            print(str(year) + ' is a leap year')
        else:
            print(str(year) + ' is not a leap year')

check_leap_years(2034, 2050)

# checking a specific year
def check_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(str(year) + ' is a leap year')
    else:
        print(str(year) + ' is not a leap year')

check_leap_year(4)






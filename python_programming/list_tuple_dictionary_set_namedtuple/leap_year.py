month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def if_leap_year(year):
    return year % 4 == 0 or (year % 400 == 0 and year % 100 != 0)


def num_of_days_month(year, month):
    if 0 >= month or month >= 13:
        return 'invalid month'
    elif month == 2 and if_leap_year(year):
        return 29
    else:
        return month_days[month]


print(num_of_days_month(1948, 14))

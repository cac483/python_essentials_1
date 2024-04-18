import datetime

def is_year_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    thirty_days = [4, 6, 9, 11]
    thirty_one_days = [1, 3, 5, 7, 8, 10, 12]
    
    if month in thirty_days:
        return 30
    else:
        if month in thirty_one_days:
            return 31
        else:
            if month == 2:
                if is_year_leap(year):
                    return 29
                else:
                    return 28
            else:
                return None


def day_of_year(year, month, day):
    if day > 0 and day <= days_in_month(year, month):
        dow = datetime.datetime(year, month, day)
        return dow.weekday()
    else:
        return None

print(day_of_year(2000, 12, 32))

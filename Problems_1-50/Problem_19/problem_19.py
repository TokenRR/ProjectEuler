import time
from datetime import date


def check_weekday(y, m, d, sundays):
    'The function of finding the day of the week'
    if date(y, m, d).isoweekday() == 7 and d == 1: sundays += 1
    return sundays

def main():
    'Program`s logic'
    sundays = 0                                        # variable for counting how many Sundays fell on the first of the month
    SAJN = [4, 6, 9, 11]                               # 30 days has September, April, June and November
    FEB = 2                                            # February has 28/29 days
    OF = 1901                                          # Year from task
    TO = 2001                                          # Year from task

    for year in range(OF, TO):
        for month in range(1, 13):

            if month in SAJN:                          # block for September, April, June and November
                for day in range(1, 31):
                    sundays = check_weekday(year, month, day, sundays)

            elif month == FEB:                         # Block for February
                if year % 4 == 0 and year % 400 != 0:  # if this year are a leap
                    for day in range(1, 30):
                        sundays = check_weekday(year, month, day, sundays)
                else:                                  # if this year are not a leap
                    for day in range(1, 29):
                        sundays = check_weekday(year, month, day, sundays)

            else:                                      # Block for rest of the months
                for day in range(1, 32):
                    sundays = check_weekday(year, month, day, sundays)
    return sundays
    

if __name__ == "__main__":
    '''
    You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
    How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
    '''
    timer_start = time.time()

    print(f'\nResult = {main()}')

    timer_stop = time.time()
    print(f'\nSpend time: {round(timer_stop-timer_start, 5)} seconds')
"""
Inputs:
  how my goodness

Returns:
  Pizza with mushrooms
"""

import datetime


def days_in_month(year, month, day=1):
    """
    Inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month

    Returns:
      The number of days in the input month.
    """
    date_1 = datetime.datetime(year, month % 12 + 1, day)
    date_2 = datetime.datetime(year, month, day)
    days = (date_1 - date_2).days
    return days if days > 0 else 31


def is_valid_date(year, month, day):
    """
     Inputs:
       year  - an integer representing the year
       month - an integer representing the month
       day   - an integer representing the day

     Returns:
       True if year-month-day is a valid date and
       False otherwise
     """
    try:
        datetime.datetime(year, month, day)
        return True
    except ValueError:
        return False


def days_between(year1, month1, day1, year2, month2, day2):
    """
      Inputs:
        year1  - an integer representing the year of the first date
        month1 - an integer representing the month of the first date
        day1   - an integer representing the day of the first date
        year2  - an integer representing the year of the second date
        month2 - an integer representing the month of the second date
        day2   - an integer representing the day of the second date

      Returns:
        The number of days from the first date to the second date.
        Returns 0 if either date is invalid or the second date is
        before the first date.
      """
    if not is_valid_date(year1, month1, day1) \
            or not is_valid_date(year2, month2, day2):
        return 0
    date_1 = datetime.datetime(year1, month1, day1)
    date_2 = datetime.datetime(year2, month2, day2)
    delta = (date_2 - date_1).days
    return 0 if delta <= 0 else delta


def age_in_days(year, month, day):
    """
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day

    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid of if the input
      date is in the future.
    """
    today = datetime.datetime.now()
    return days_between(year, month, day, today.year, today.month, today.day)

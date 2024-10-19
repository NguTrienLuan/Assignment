def is_valid_time_format(input_time_value):
    """
    This function checks whether the string value input by the user is
    a valid time *AND* presented in HH:mm format

    Parameters:
    - input_time_value: str, the value provided by the user

    Returns:
    bool - True if input value is a valid time in HH:mm format, 
           False otherwise
    """
    if len(input_time_value) == 5 and input_time_value[2] == ":":
        hour, minute = input_time_value.split(":")
        if hour.isdigit() and minute.isdigit():
            hour = int(hour)
            minute = int(minute)

            return hour in range(24) and minute in range(60)

    return False    


def is_valid_date_format(input_date_value):
    """
    This function checks whether the string value input by the user is 
    a valid date (on or before 2024) *AND* presented in DD/MM/YYYY format

    Parameters:
    - input_date_value: str; the value provided by the user

    Returns:
    bool - True if input value is a valid date in DD/MM/YYYY format (on or before 2024), 
           False otherwise
    """

    numeric_chars = "0123456789"

    if len(input_date_value) == 10 and input_date_value[2] == "/" and input_date_value[5] == "/":
        day, month, year = input_date_value.split("/")

        if (all([char in numeric_chars for char in day]) 
            and all([char in numeric_chars for char in month]) 
            and all([char in numeric_chars for char in year])):

            day = int(day)
            month = int(month)
            year = int(year)
            return is_date_valid(day, month, year)

    return False

def is_date_valid(day, month, year):
    """
    This function checks whether the given date exists in the Gregorian calendar.

    Parameters:
    - day: int, (converted) integer value of the day
    - month: int, (converted) integer value of the month
    - year: int, (converted) integer value of the year in the Gregorian calendar

    Returns:
    bool - True if the given date exists in the Gregorian calendar, False otherwise
    """
    valid_days = None
    valid_months = range(1, 13)

    if month in [1, 3, 5, 7, 8, 10, 12]:
        valid_days = range(1, 32)
    elif month in [4, 6, 9, 11]:
        valid_days = range(1, 31)
    elif month == 2 and is_leap_year(year):
        valid_days = range(1, 30)
    elif month == 2 and not is_leap_year(year):
        valid_days = range(1, 29)
    else:
        return False

    return day in valid_days and month in valid_months and 0 <= year <= 2024


def is_leap_year(year):
    """
    This function checks if the year is a leap year.

    Parameters:
    - year: int

    Returns:
    bool - True if given year is a leap year, False otherwise
    """
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def is_valid_course(course: str):
    valid_courses = {"Python", "Information Security", "Artificial Intelligence"}
    course_lst = course.split(',')
    for item in course_lst:
        if item.lower().title() not in valid_courses:
            return False
    
    return True


# DO NOT MODIFY BEYOND THIS LINE
if __name__ == "__main__":
    pass
import datetime
import calendar
from dateutil.relativedelta import relativedelta

import ics
import pytz

py_days = list(calendar.Calendar().iterweekdays())
fmt_days = list(calendar.day_name)
day_dict = dict(zip(py_days, fmt_days))
weeks_suffix = {1:'st', 2:'nd', 3:'rd', 4:'th'}

def floor_month(date):
    date -= datetime.timedelta(days=date.day-1)
    return date

def create_parking_event(date, week_num, day_of_week):
    global day_dict, weeks_suffix
    e = ics.Event()
    day_fmt = day_dict[day_of_week]
    suff = weeks_suffix[week_num]
    week_fmt = f'{week_num}{suff}'
    e.name = f'Parking Alert: {week_fmt} {day_fmt} of month.'
    e.begin = date.strftime('%Y-%m-%d %I:%M%:%S')
    return e

def get_events(week_num, day_of_week, date=datetime.date.today(), yearsout=10):
    assert isinstance(week_num, int) and week_num>=1 and week_num<=4, "week number out of range"
    assert isinstance(day_of_week, int) and day_of_week>=0 and day_of_week<=6, "day number ranges in python from 0-6"
    initdate = date
    #date = pytz.timezone('US/Mountain').localize(date)
    cal = ics.Calendar()
    date = floor_month(date)
    while date.year < 2029:
        while date.weekday() != day_of_week:
            date += datetime.timedelta(days=1)
        date += datetime.timedelta(weeks=week_num-1)
        cal.events.add(create_parking_event(date, week_num, day_of_week))
        date = floor_month(date)
        date += relativedelta(months=1)
    return cal

with open('parking_alerts.ics', 'w') as f:
    f.writelines(get_events(1, 3))
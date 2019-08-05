import calendar
import datetime

def create_cal():
    cal = ''
    cal += "BEGIN:VCALENDAR\nVERSION:2.0\n"
    return cal

def finish_cal(cal):
    cal += 'END:VCALENDAR'
    return cal

def make_event(cal, week_num, day_of_week, date=datetime.date.today()):
    #assert isinstance(week_num, int) and week_num>=1 and week_num<=4, "week number out of range"
    #assert isinstance(day_of_week, int) and day_of_week>=0 and day_of_week<=6, "day number ranges in python from 0-6"
    week_of_month = str(week_num)[0]
    #date = floor_month(date)
    #make event
    event = 'BEGIN:VEVENT\nDTSTART;TZID=America/Denver:'
    starttime = datetime.date.today().strftime('%Y%m%d') + 'T120000Z\n'
    event += starttime
    rrule = 'RRULE:FREQ=MONTHLY;BYDAY='
    #determine day
    days = list(calendar.day_name)
    days_abr = [str.upper(abr[:2]) for abr in list(calendar.day_abbr)]
    days_of_week = dict(zip(days, days_abr))
    days_of_week = {'Monday': 'MO', 'Tuesday': 'TU', 'Wednesday': 'WE', 'Thursday': 'TH', 'Friday': 'FR', 'Saturday': 'SA', 'Sunday': 'SU'}
    form_day_abr = days_of_week[day_of_week]
    day_of_month = week_of_month + form_day_abr
    rrule += day_of_month + '\n'
    event += rrule
    summary = f'SUMMARY:Parking Alert: {week_num} {day_of_week} of month.\n'
    event += summary
    event += 'END:VEVENT\n'
    return event
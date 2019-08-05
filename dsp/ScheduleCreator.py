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
    import calendar
    import datetime
    #assert isinstance(week_num, int) and week_num>=1 and week_num<=4, "week number out of range"
    #assert isinstance(day_of_week, int) and day_of_week>=0 and day_of_week<=6, "day number ranges in python from 0-6"
    weeknum = str(week_num)[0]
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
    form_day_abr = days_of_week[day_of_week]
    day_of_month = str(week_num) + form_day_abr
    rrule += day_of_month + '\n'
    event += rrule
    weeks_suffix = {1:'st', 2:'nd', 3:'rd', 4:'th'}
    suffix = weeks_suffix[week_num]
    summary = f'SUMMARY:Parking Alert: {week_num}{suffix} {day_of_week} of month.\n'
    event += summary
    event += 'END:VEVENT\n'
    return event
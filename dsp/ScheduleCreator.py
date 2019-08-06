import calendar
import datetime

def create_cal():
    cal = ''
    cal += "BEGIN:VCALENDAR\nVERSION:2.0\n"
    return cal

def finish_cal(cal):
    cal += 'END:VCALENDAR'
    return cal

def make_event(week_num, day_of_week, date=datetime.date.today()):
    week_of_month = str(week_num)[0]
    event = 'BEGIN:VEVENT\nDTSTART;TZID=America/Denver:'
    starttime = datetime.date.today().strftime('%Y%m%d') + '\n' #all day
    event += starttime
    rrule = 'RRULE:FREQ=MONTHLY;BYDAY='
    days = list(calendar.day_name)
    days_abr = [str.upper(abr[:2]) for abr in list(calendar.day_abbr)]
    days_of_week = dict(zip(days, days_abr))
    form_day_abr = days_of_week[day_of_week]
    day_of_month = week_of_month + form_day_abr
    rrule += day_of_month + '\n'
    event += rrule
    summary = f'SUMMARY:Parking Alert: {week_num} {day_of_week} of month.\n'
    event += summary
    event += 'END:VEVENT\n'
    return event
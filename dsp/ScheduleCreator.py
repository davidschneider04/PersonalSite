import calendar
import datetime

def create_cal():
    cal = ''
    cal += "BEGIN:VCALENDAR\nVERSION:2.0\nPRODID:davidschneiderprojects.com\nNAME:Parking Reminders\nX-WR-CALNAME:Parking Reminders\n"
    return cal

def finish_cal(cal):
    cal += 'END:VCALENDAR'
    return cal

def floor_month(date):
    date -= datetime.timedelta(days=date.day-1)
    return date

def make_event(week_num, day_of_week, date=datetime.date.today()):
    week_of_month = str(week_num)[0]
    event = 'BEGIN:VEVENT\n'
    starttime = 'DTSTART;TZID=America/Denver:'
    starttime += date.strftime('%Y%m%d') + 'T080000Z\n'
    event += starttime
    endtime = 'DTEND;TZID=America/Denver:'
    endtime += date.strftime('%Y%m%d') + 'T170000Z\n'
    event += endtime
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
    #alarm at 9PM and 7AM
    alarm = 'BEGIN:VALARM\n' + 'TRIGGER:-PT11H\n' + 'REPEAT:1\n' + 'DURATION:PT10H\n' + 'ACTION:DISPLAY\n' + f'{summary}' + 'END:VALARM\n'
    event += alarm
    event += 'END:VEVENT\n'
    return event
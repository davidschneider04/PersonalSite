import calendar
import datetime
import dateutil

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

def add_rrule(event, byday):
    rrule = 'RRULE:FREQ=MONTHLY;BYDAY='
    rrule += byday
    rrule += '\n'
    event += rrule
    return event

def except_holidays(event):
    #source: denvergov.org/content/denvergov/en/office-of-human-resources/employee-resources/holiday-schedule.html
    #new years - not needed yet
    #mlk - not needed yet
    #presidents - not needed yet
    #cesar chavez (?) - not needed yet
    #memorial
    event += 'EXRULE:FREQ=YEARLY;BYDAY=MO;BYSETPOS=-1;BYMONTH=5\n'
    #independence
    event += 'EXRULE:FREQ=YEARLY;BYMONTH=7;BYMONTHDAY=4\n'
    #labor
    event += 'EXRULE:FREQ=YEARLY;BYDAY=MO;BYSETPOS=1;BYMONTH=9\n'
    #veterans
    event += 'EXRULE:FREQ=YEARLY;BYMONTH=11;BYMONTHDAY=11\n'
    #thanksgiving
    event += 'EXRULE:FREQ=YEARLY;BYDAY=TH;BYSETPOS=4;BYMONTH=11\n'
    #xmas - not needed yet
    return event

def make_event(week_num, day_of_week, date=datetime.date.today()):
    week_of_month = week_num[0]
    event = 'BEGIN:VEVENT\n'
    loop_date = floor_month(date)
    loop_weeks = 1 if loop_date.strftime('%A') == day_of_week else 0
    while loop_weeks != int(week_of_month) or loop_date.strftime('%A') != day_of_week:
        loop_date += datetime.timedelta(days=1)
        if loop_date.strftime('%A') == day_of_week:
            loop_weeks += 1
    if loop_date < date:
        loop_date += dateutil.relativedelta(months=1)
    starttime = 'DTSTART;TZID=America/Denver:'
    starttime += loop_date.strftime('%Y%m%d') + 'T080000Z\n'
    event += starttime
    endtime = 'DTEND;TZID=America/Denver:'
    endtime += loop_date.strftime('%Y%m%d') + 'T170000Z\n'
    event += endtime
    days = list(calendar.day_name)
    days_abr = [str.upper(abr[:2]) for abr in list(calendar.day_abbr)]
    days_of_week = dict(zip(days, days_abr))
    form_day_abr = days_of_week[day_of_week]
    rrule_freq = week_of_month + form_day_abr
    event = add_rrule(event, rrule_freq)
    event = except_holidays(event)
    #exclude all instances before today
    today_frmt = date.strftime('%Y%m%d')
    event += f'EXRULE:FREQ=DAILY;INTERVAL=1;UNTIL={today_frmt}\n'
    summary = f'SUMMARY:Parking Alert: {week_num} {day_of_week} of month.\n'
    event += summary
    #alarm at 9PM and 7AM
    alarm = 'BEGIN:VALARM\n' + 'TRIGGER:-PT11H\n' + 'REPEAT:1\n' + 'DURATION:PT10H\n' + 'ACTION:DISPLAY\n' + f'{summary}' + 'END:VALARM\n'
    event += alarm
    event += 'END:VEVENT\n'
    return event
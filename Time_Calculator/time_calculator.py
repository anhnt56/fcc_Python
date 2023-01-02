def add_time(start, duration, week=None):
    # weekday in ascending order
    weekdays = {'monday': 0, 'tuesday': 1, 'wednesday': 2, 'thursday': 3, 'friday': 4, 'saturday': 5, 'sunday': 6}

    # trunk & sort data
    startArr = start.split(' ')
    startTime = startArr[0].split(':')
    meridiem = 'AM'
    durationTime = duration.split(':')

    # calculate hour
    tmpHour = (int(startTime[0]) + int(durationTime[0]))
    if startArr[1] == 'PM':
        tmpHour += 12

    # calculate minute
    tmpMinute = (int(startTime[1]) + int(durationTime[1]))
    if (tmpMinute > 59):
        tmpHour += 1

    # generate to number of days
    days = int(tmpHour // 24)  # Flooring the division, since rounding will give a wrong value.

    # hour that surplus
    surHour = tmpHour % 24

    # convert 'AM' to 'PM' if the 12th hours is passed.
    if surHour > 11:
        meridiem = 'PM'

    # convert back to 12h format
    if surHour > 12:
        surHour -= 12
    elif surHour == 0:
        surHour = 12

    # calculate surplus minute.
    endMinute = tmpMinute % 60

    # Concatonate the first part of the string.
    totalTime = str(surHour) + ':' + str(endMinute).zfill(2) + ' ' + meridiem

    # if the weekday option was given, add that weekday to the string.
    if week is not None:
        week = week.lower()
        weekdayNumb = weekdays[week]
        surWeekdayNumb = (days + weekdayNumb) % 7
        # https://stackoverflow.com/questions/8023306/get-key-by-value-in-dictionary
        actualWeek = list(weekdays.keys())[list(weekdays.values()).index(surWeekdayNumb)]
        totalTime += ', ' + actualWeek.capitalize()

    # if the day has changed, add the correct string value
    if days > 1:
        totalTime += ' (' + str(days) + ' days later)'
    elif days > 0:
        totalTime += ' (next day)'

    return totalTime
import datetime

year = 2017


def dayOfProgrammer(year):
    #Julian calender

    if year <= 1917 and year % 4:    #regular year
        res = "13.09."+str(year)

    elif year <= 1917 and not year % 4:
        #leap year
        res = "12.09." + str(year)

    elif year == 1918:
        res = "26.09.1918"

    #Gregorian calender
    else:
        start_date = datetime.datetime(year, 1, 1)
        delta = datetime.timedelta(days=255)
        result = start_date + delta
        res = result.strftime('%d.%m.%Y')
    return res





print(dayOfProgrammer(year))
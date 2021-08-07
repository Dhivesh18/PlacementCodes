def dayOfProgrammer(year):
    if year < 1918:
        l = ['12.09.'] if year % 4 == 0 else ['13.09.']
        l.append(year)
    elif year >= 1919:
        l = ['12.09.'] if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0) else ['13.09.']
        l.append(year)
    elif year == 1918:
        l = ['26.09.', year]
    return "".join(str(i) for i in l)

year=int(input())
print(dayOfProgrammer(year))

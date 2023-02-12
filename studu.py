import calendar
a = calendar.LocaleHTMLCalendar(locale='Russian_Russia')
with open('calendar.html', 'w') as g:
    print(a.formatyear(20023, width=4), file=g)
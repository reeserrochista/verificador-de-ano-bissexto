from datetime import date
year = int(input('Que ano você quer analisar?. Digite 0 para ver o ano atual.'))
if year == 0:
    year = date.today().year
if year % 4 == 0 and year % 100 !=0 or year % 400 == 0:
    print('{} é um ano bissexto'.format(year))
else:
    print('{} não é um ano bissexto'.format(year))

def leap_year(year):
    """É bissexto se for divisível por 4 e (não for divisível por 100 ou for divisível por 400)"""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 ==0)
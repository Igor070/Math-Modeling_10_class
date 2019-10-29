def visocos(a):
    """ 
        Функция определяет високосный || не високосный год
    """
    if a%4==0 and a%100!=0 or a%400==0:
        return('високосный')
    else:
        return('не високосный')

print(visocos(2000))
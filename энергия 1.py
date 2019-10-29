from constant import G

def energi(m,v,h):
    """ 
    Функция определяет полную механическую энергию
    """
    e = (m*v**2)/2+m*G*h

    return e


print(energi(5, 100, 4))
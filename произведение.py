def pro(N):
    """
       Функция перемножает все часла массива
    """
    s = 1
    for i in range(0, len(N), 1):
        s = s*N[i]
        print(s)
    return s

N = range(1, 10, 1)
print(pro(N))
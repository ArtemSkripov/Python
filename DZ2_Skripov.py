a = float(input('Введи первую сторону '))
b = float(input('Введи вторую сторону '))
c = float(input('Введи третью сторону '))
if a and b and c:
    if a+b > c and a+c > b and b+c > a:
        print('Это треугольник')
        p=(a+b+c)/2
        s=(p*(p-a)*(p-b)*(p-c)) ** 0.5
        print('Его площадь равна ', s)
    else:
        print('Это не треугольник')
else:
    print('Сторона не может быть 0')
    
    
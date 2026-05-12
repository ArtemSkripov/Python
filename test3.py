""" a=[12,23,3,45,5,6,7]
sum = 0
i=0
while i < len(a):
    if a[i] > 10:
        sum = sum+a[i]
    i=i+1
print(sum) """


""" a = int(input('Введите число'))
n = 1
sum = 0
while n <= a:
    sum = sum + n ** 3
    n=n+1
print(sum) """

""" import random
i = 0
while i != 7:
    i = random.randint(1,10)
    print(i)
print('Выпало 7') """

""" n = int(input("Введите первое число"))
m = int(input("Введите второе число"))
s=0
for i in range(n,m+1):
    s=s+i**3
print(s) 
  """
""" n = int(input("Введите первое число"))
m = int(input("Введите второе число"))
s = m-n+1
for i in range(n,m+1):
    print(i)
print(s)   """

""" from random import randint
n=int(input('Введите число'))
m=int(input('Введите число'))
matrix = []
for i in range(n):
    row = []
    for j in range(m):
        row.append(randint(1,9))
    matrix.append(row)
    print(row, end='\n')
sum = 0
kol = 0
for row in matrix:
    for element in row:
            sum = sum+element
            kol += 1 
print(sum)
print(kol) """


""" x = [2,4,55,6,73,5]
count = 0
while count < len(x):
    x[count] = x[count]*(-2)
    count+=1
print(x)

x = [2,4,55,6,73,5]
elem = 0
for i in x:
    x[elem] = i * (-2)
    elem+=1
print(x) """

x = [2,5,67,88,2,3]
count = 0
even_count = 0
while count < len(x):
    if x[count]%2 == 0:
        even_count +=1
    count+=1
print(even_count)

x = [2,4,55,6,73,5]
even_count = 0
for i in x:
    if i%2 == 0:
        even_count +=1
print(even_count)


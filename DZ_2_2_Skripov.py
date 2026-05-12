x=input('Введите строку')
x=x.replace(' ','')
print(x)
result=''
for y in x:
    if y not in result:
        result=result+y
print(result)
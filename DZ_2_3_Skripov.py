x=input('Введите строку: ')
small=0
big=0
for i in x:
    if i>='a' and i<='z':
        small=small+1
    elif i>='A' and i<='Z':
        big=big+1
print(small)
print(big)
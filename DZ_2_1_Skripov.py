x=input('Напишите любое предложение')
x=x.replace(' ',' ')
x=x.replace('.',' ')
x=x.replace(',',' ')
x=x.replace('?',' ')
x=x.replace('-',' ')
x=x.replace(';',' ')
x=x.replace(':',' ')
x=x.replace('!',' ')
x=x.split(' ')
print(x)
longest = ''
for i in x:
    if len(i) > len(longest):
        longest = i
print(f'Самое длинное слово в предложении: {longest}')
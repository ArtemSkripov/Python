firstname = 'Artem '
lastname = 'Skripov '
age = '36'
print('Привет, меня зовут ',firstname+lastname,'Мне ', age)

list_b=[3,2,'ff']
list_b.append('gggggg')
print(list_b)
list_b.remove(2)
print(list_b)
print(list_b[1])
print(list_b.remove('ff'))
del list_b[0]
print(list_b)
list_b[0] = 77
print (list_b)
list_b.append('fffffff')
print(list_b)
print(len(list_b))
a = list_b.pop(1)
print(list_b)
print(a)

a = [1, 2, 3]
b = [4, 5, 6]
a.append('oooo')
a.insert(0,'gggg')
b.insert(0,'hhhh')
b.insert(0,'bts')
print(a)
print(b)
a.extend(b)
print(a)

s={1,2,3,3,3,3,4}
print(s)
s.add(7)
print(s)

d1={'a':3,'b':'cool'}
print(d1)
d1['new'] = 66
print(d1)
print(d1['new'])
del d1['b']
print

a = [1,2]
b = (1,2)
c = {(1,2):[2,3,4]}
print(a,b,c,)

a=[1,2,3,4]
b=[]
b=a
print(id(a))
print(id(b))
b.append(23)
print(a)
print(b)
b.append([5,4,5])
print(a)
print(b)
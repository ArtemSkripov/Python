#Задание 1
x = [2,4,55,6,73,5]
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
print(x)

#Задание 2
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

#Задание 3
a = {'test':'test_value','europe':'eur','dollar':'usd','ruble':'rub'}
key_list = list(a.keys())
count = 0
new_dict = {}
while count < len(key_list):
    key = key_list[count]
    value = a[key]
    new_key = key + str(len(key))
    new_dict[new_key] = value
    count+=1
a = new_dict
print(a)

a = {'test':'test_value','europe':'eur','dollar':'usd','ruble':'rub'}
key_list = list(a.keys())
count = 0
new_dict = {}
for i in key_list:
    new_key = key_list[count] + str(len(i))
    value = a[i]
    new_dict[new_key] = value
    count+=1
a = new_dict
print(a)

#Задание 4
a = [1, 2, 3, 4, 5]
new_list = []
for i in range(1, len(a)):
    new_list.append(a[i])
new_list.append(a[0])
print(new_list)


a = [1, 2, 3, 4, 5]
new_list = []
i = 1
while i < len(a):
    new_list.append(a[i])
    i += 1
new_list.append(a[0])
print(new_list)

#Задание 5
a = [1,1]
count = 1
while count < 14:
    a.append(a[-1]+a[-2])
    count+=1
print(a)

a = [1,1]
for i in range(13):
    a.append(a[-1]+a[-2])
print(a)
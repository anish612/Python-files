fruits = ['orange','apple','pear','banana','kiwi','apple','banana']
cnt=fruits.count('apple')
print(cnt)

indx=fruits.index('banana')
print(indx)

rev=fruits.reverse()
print(rev)

fruits.append('grapes')
print(fruits)

fruits.sort()
print(fruits)




L1 = [0,1,2,3,4,5,6]
L2 = [9,8,7,6,5,4,3]
print(L1)

print(L2[3])

print(L1[-3])

print(L2[1:3])

L1.append(5)
print(L1)

L1.extend(L2)
print(L1)



dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict3 = {**dict1, **dict2}
print(dict3)



employees = ['Kelly', 'Emma', 'John']
defaults = {"designation": 'Application Developer', "salary": 8000}
result = dict.fromkeys(employees, defaults)
print(result)


Dict1 = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}
Dict1["Location"]=Dict1.pop("city")
print(Dict1)



Dict2 = {
     'emp1': {'name': 'Jhon', 'salary': 7500},
     'emp2': {'name': 'Emma', 'salary': 8000},
     'emp3': {'name': 'Brad', 'salary': 6500}
}
Dict2['emp3']['salary']=8500
print(Dict2)




Dict3 = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
  
}
keys=['name','salary']


dic={k:Dict3[k] for k in keys}
print(dic)


number = [1,5]
number.insert(1,3)
print(number)
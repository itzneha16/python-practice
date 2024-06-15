dict1={'name':'Neha','surname':'shinde','no':78 }
print(dict1)
dict2={'surname':'shinde','no':78,'name':'Neha'}
print(dict1==dict2)
print(id(dict1))
print(id(dict2))
print(id(dict1)==id(dict2))

print(dict1['surname'])
dict2['name']='swaraj'
print(dict2)

info={'name':'Riya','surname':'Shinde','age':22}
print(info)
info ['gender']='female'
print(info)
del info ['surname']
print(info)
key_name='phone'
info [key_name]=9356512809
print(info)

bikes={'brand':'custom', 'price':2000}
keys=bikes.keys()
print(keys)
print(type(keys))
print(bikes.items())

#use of variables in dictionary
name='neha'
surname='shinde'
phone=9356512809

my_info={'name':name, 'phone':phone, 'surname':surname}
print(my_info)
print(my_info.get('name'))
print(my_info.get('phone' ,0))
print(my_info.get('rollno' ,0))

my_list=[[1,4],[5,9]]
print(dict(my_list)) 

 
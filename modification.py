'''list1=[1,2,3]
list3=[1,2,3]
list2=list1
print(id(list3)) #elements in list1 and list 3 are same but memory location / id are differnt 
print(id(list1))
print(id(list2))# if we copy element then id of both object are same

print(id([1,2,3]))

dict1={'name':'neha','marks':100}
dict2={'name':'neha','marks':100}
print(id(dict1))
print(id(dict2))'''


#deepcopy function
dict_1={'name':'neha','marks':100 , 'rollno':[]}
dict_copy=deepcopy(dict_1)
print(dict_1)
print(dict_copy)

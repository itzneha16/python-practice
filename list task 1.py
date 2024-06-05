#task no 1
list=[True , 'hi', 102 ,10.5 , 66]
print(list)
list.pop(2)
print(list)
print(len(list))
#list.sort(reverse=True)
print(list)
list.extend([102,67])
print(list)

#task no 2

L1=[20,78,97,99]
L2=[54,87,65]
list3= L1 + L2
print(list3)
list3=L1.__add__ (L2) 
print(list3)

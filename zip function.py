fruit=['apple','mango','papaya','banana']
rate=[120,600,50,60]
f_r=zip(fruit,rate)
print(f_r)
list=list(f_r)
print(list)

f_r=zip(fruit,rate)
dict1=dict(f_r)
print(dict1)
print(type(dict1))

fruit=['apple','mango','papaya','banana']
rate=[120,600,50,60] 
name='abcde'
zip_code=zip(fruit,rate,name)
# print(list(zip_code))
for fruits in zip_code:
    print(fruits)
    print(fruits[1])
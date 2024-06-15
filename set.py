numbers={105,87,105,76,105,283}
print(numbers) #python delete duplicate values in set 
print(type(numbers))

fruit={'apple','banana','lime','mango'}
new_fruits={'lime','mango','banana','apple'}
print(fruit == new_fruits)

set={}
print(set)
print(type(set)) # we can not create empty set

#empty set
my_set= set()
print(my_set)
print(type(my_set))

#issubset method
num1={10,20}
num2={30,20,40,10,50}
subset=num1.issubset(num2)
print(subset)   

#adding new element in set
my_set={2,4,5,6,9}
print(my_set)
my_set.add(8)
print(my_set)
my_set.remove(5)
print(my_set)
my_set.discard(5)
print(my_set)
print(my_set.intersection((9,7,10,6)))

set_1={10,8,9,5 }
set_2={2,8,3,1,9}
print(set_1.intersection(set_2))
print(set_1.union(set_2))
print(set_2.union(set_1))
print((set_1.union(set_2)) == (set_2.union(set_1)))

#we can used | this symbol for union method
num1={1,2,3}
num2={7,9,1,2}
print(num1 | num2)

#creat copy of set
num1={1,2,3}
other=num1.copy()
print(other)

#symmetric differnce
a={'a','b','c'}
b={'l','c','m'}
print(a)
print(b)
print(a.symmetric_difference(b))
print((a|b) - (a&b))


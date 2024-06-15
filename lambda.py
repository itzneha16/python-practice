def greeting(greet):
    return lambda name : f"{greet} , {name}"

moring=greeting("good morning")
print(moring('neha'))

evening=greeting('good evening')
print(evening('swaraj'))

def multiplying(multipler):
    return lambda x:x**multipler

number1=multiplying(5)
print(number1(2))
print(number1(5))

# sort the list using lambda function
students=[{'neha':'neha','score':90},
          {'name':'swaraj','score':20},
          {'name':'nikita','score':60}]

students.sort(key=lambda student:student['score'])
print(students)

numbers=[3,4,5,8,10,15,20,21]

Evan=list(filter(lambda num:num % 2 == 0 , numbers))
print("Evan numbers : ",Evan)

Odd=list(filter(lambda num:num % 2 == 1, numbers))
print("Odd numbers : ",Odd)
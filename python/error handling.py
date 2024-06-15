# try:
#     print(10/0)
# except ZeroDivisionError as e:
#     print(type(e))
#     print(e)
#     # print('Error - zero division error')

# print('contion.....')

# #multiple Errors
# try:
#     print(10/0)
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e:
#     print(e)
    
# print("continue......")

# #multiple error handling with one except block
# try:
#     print('10'/0)
# except (ZeroDivisionError,TypeError) as e:
#     print(e)
#  print('contionue...')


# # ELSE block
# try:
#     print(10/2)
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e:
#     print(e)
# else:
#     print("there was no error...")

# #finally block
# try:
#     print(10/2)
# except ZeroDivisionError as r:
#     print(e)
# except TypeError as e:
#     print(e)
# else:
#     print("there was no error")
# finally:
#     print('continue........')
    
    
# #Error generation with raise
# def mult(a,b):
#     if b == 0:
#         raise TypeError("second argument can't be 0")
#     return a/b
# try:
#     mult(10,0)
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e:
#     print(e)
    
# print("continue...")    

# # Example
# try:
#     salary=int(input("Enter your salary : "))
#     days=int(input("Enetr your working days : "))
#     salary_per_day=salary/days
#     print(salary_per_day)
# except ValueError :
#     print("can't accept input string ")
# except ZeroDivisionError :
#     print("can't acccept input zero ")


# try:
#     salary=int(input("Enter your salary : "))
#     days=int(input("Enetr your working days : "))
#     salary_per_day=salary/days
#     print(salary_per_day)
# except (ValueError, ZeroDivisionError) as e :
#     if type(e)==ValueError:
#         print(e)
#         print("can't accept input string")
#     if type(e)==ZeroDivisionError:
#         print(e)
#         print("can't accept input string")

# # complete example
# try:
#     salary=int(input("Enter your salary : "))
#     days=int(input("Enetr your working days : "))
#     salary_per_day=round(salary/days)
# except ZeroDivisionError as e:
#     print(e)
#     print("can't accept input zero ")
# except ValueError as e:
#     print(e)
#     print("can't accept input string ")
# else:
#     print("salary per day : ", salary_per_day)
# finally:
#     print("Salary operation calculation complete")

 # # regester user example

def symbol(email):
    return '@' in email

def user_register(email,age):
    if not isinstance(email,str):
        raise TypeError("Email must be a string")
    if not isinstance(age,int):
        raise TypeError("Age must be integer")
    if not symbol(email):
        raise ValueError("Invaild Email: email must comtain @ sysmbol")
    
    print("user registration succefull")
    return {'Email':email,'Age':age}

try:
    user=user_register('neha@gmail.com','22')
    print(user)
except (TypeError,ValueError) as e :
    print(e)
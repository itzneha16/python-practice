#keyargumenta and arguments
# def my_function(*args,**kwargs):
#     print(args)
#     print(kwargs)
    
# my_function(10,True,'abc',key=20,name='neha',)

def send_email(to,subject,*args):
    print(f"sending email to :{to}")
    print(f"Email subject : {subject}")
    
    if args:
        print("aditional arguments :")
        for additional in args:
            print(additional)

send_email('nehashinde@gmail' ,'helloooo','other@email','im there')
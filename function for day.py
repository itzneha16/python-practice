from datetime import date

def get_weekday():
    return date.today().strftime('%A')
    
print(get_weekday()) 

def get_weekday():
    return date.today().strftime('%a')
    
print(get_weekday()) 

def get_weekday():
    return date.today().strftime('%D')
    
print(get_weekday()) 

def get_weekday():
    return date.today().strftime('%d')
    
print(get_weekday()) 

def get_weekday():
    return date.today().strftime('%a,%d/%m/%y')
    
print(get_weekday()) 
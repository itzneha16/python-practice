def num_info(num):
    """
    print wether number is evan or odd
    Args:
        num (int): Enter number
    return: 
        str:it tells it is evan or odd number
    """
    if (num%2)==0:
        print(f"{num} is evan number...")
    else:
        print(f"{num} is odd numner...")
        
num_info(28)
num_info(55)
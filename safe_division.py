def get_numbers(): 
    try: 
        a = int(input("enter a number: "))
        b = int(input("enter a number: "))
        return a, b
    except ValueError: 
        return "invalid numbers"


def division(a, b): 
    try: 
        return a / b
    except ZeroDivisionError: 
        return "undefined division"

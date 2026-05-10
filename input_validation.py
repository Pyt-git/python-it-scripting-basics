def get_number():
    user_input = input("enter a number: ")

    try: 
        return int(user_input)
    except ValueError: 
        return "invalid number"

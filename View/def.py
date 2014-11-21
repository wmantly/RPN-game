def welcome():
    print('''
        Welcome to the RPN game!

        Go bears!
        ''')
    return input( "Please enter you name:\n")

def getPin():
    pin = input( "Please enter your pin:\n")
    if type( pin ) != int: return getPin()
    return pin

def game():
    pass
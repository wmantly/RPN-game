def welcome():
    print('''
        Welcome to the RPN game!

        Go bears

        l (enter) login
        n (enter) new user
        ''')

    temp = input( "Choice:\n" )

    if temp == 'l': return True;
    else: return False

def sign_up():
    name = input( "Please enter a user Name:\n" )
    password = input( "Please enter a pin:\n" )
    return( { 'name':name, 'password':password } )

def login():
    name = input( "Please enter a user Name:\n" )
    password = input( "Please enter a pin:\n" )
    return( { 'name':name, 'password':password } )

def show_rpn( obj ):
    if len(a) > 2:
        if obj.right_or_wrong:
            print( "Right!" )
        else:
            print( "Wrong!, the correct answer is " + obj.answer )
        print( "time taken: " + obj.time_taken )

    print( "Please solve!\n") 
    print( solve + "\n" )
    return input('?')

##testing

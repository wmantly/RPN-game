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
    print( "Pick a new user name and pin:" )
    name = input( "Please enter a user Name:\n" )
    password = input( "Please enter a pin:\n" )
    return( { 'name':name, 'password':password } )

def name_exists():
    print( "Sorry, that name is all ready registered!" )
    return sign_up()

def login():
    print( "Please log in with your user name and pin:" )
    name = input( "Please enter a user Name:\n" )
    password = input( "Please enter a pin:\n" )
    return( { 'name':name, 'password':password } )

def show_rpn( obj ):
    if len(obj) > 2:
        
        if obj["right_or_wrong"]:
            print( "Right!" )
        else:
            print( "Wrong!, the correct answer is " + obj["answer"] )
        print( "time taken: " + obj["time_taken"] )

    print( "Please solve!\n") 
    print( obj["rpn"] + "\n" )
    return input('?')

##testing

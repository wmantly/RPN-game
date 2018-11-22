## to use dev console:
will allow dev outpt
and view.devConsole( [ message] )
will print dev message, one line per item in passed array
instead of print 

that way it print on a box on the screen
but it will only show a few lines
like, dont do a dir(), youll only see the first few lines
and view.devConsole() ONLY takes lists or object's
so if you want to console a sting do this
view.devConsole( [string] )
and it only works in controller.py and view.py, there would need to be a abstraction function some where in model.py or controller.py to make it work with in model.py

on the devconsole takes a second argument that will sleep the function
Its an int in seconds 

## To Do:

### nice-to-have
user can review profile, see bar graph of solved problems by difficulty

high scores of different users

after each solution, user sees the message along with former problem AND solution

have some kind of race against something so the user has to figure out the rpn before some visual thing happens(hammer drops)

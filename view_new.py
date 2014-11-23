#!/usr/bin/env python3

import curses
import time

screen = curses.initscr()

screen.border(0)
# curses.noecho() 
curses.curs_set(1) 
screen.keypad(1)
       

def welcome():

    screen.addstr(2, 2, "Welcome to the RPN game!" )
    screen.addstr(3, 2, "Go bears!" )
    screen.refresh()
    time.sleep(.5)

    screen.addstr(5, 3, "l login" )
    screen.addstr(6, 3, "n new user" )
    screen.addstr(7, 3, "Q Quit" )
    screen.refresh()


    while True:
        event = screen.getch()
        if event == ord("Q"): exit();
        if event == ord("n"): return False
        if event == ord("l"): return True

    # temp = input( "Choice:\n" )

    # if temp == 'l': return True;
    # else: return False

def sign_up():

    screen.clear()
    screen.border(0)

    screen.addstr(2, 2, "Pick a new user name and pin:" )
    screen.refresh()
    screen.addstr(3, 2, "user Name:" )
    name = screen.getstr(4, 2, 60)
    screen.addstr(5, 2, "Pin:" )
    screen.refresh()
    password = screen.getstr(6, 2, 60)

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

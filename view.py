#!/usr/bin/env python3

import curses
import time

class View:
    def __init__( self ):

        # start the courses instance
        self.screen = curses.initscr()

        # configure the whole screen

        # set border for main screen
        self.screen.border(0)
        # hide KB input
        curses.noecho()

        curses.curs_set(0)

        # idk, i have to look it up
        self.screen.keypad(1)

        # draw the main screen
        self.screen.refresh()

        # setup the header window
        self.header = curses.newwin( 4, 35, 2, 3 )
        self.header.border(0)

        # setup the right header window
        self.header_right = curses.newwin( 4, 35, 2, 38 )
        self.header_right.border(0)
        self.header_right.refresh()

        # setup the body window
        self.body = curses.newwin( 11, 50, 6 , 3)
        # self.body.border(0)

        # side bar
        self.side_bar = curses.newwin( 11, 20, 6 , 53)
        self.side_bar.border(0)


        #############################################

        self.header_right.addstr( 1, 20, "Not logged in")
        self.header_right.refresh()

    def welcome( self ):
        
        # write the header up
        self.header.addstr( 1, 2, "Welcome to the RPN game!" )
        self.header.addstr( 2, 2, "Go bears!" )

        #draw the header
        self.header.refresh()

        # short pause
        time.sleep(.5)

        # write the body
        self.body.addstr( 1, 3, "l login" )
        self.body.addstr( 2, 3, "n new user" )
        self.body.addstr( 3, 3, "Q Quit" )

        # draw the body
        self.body.refresh()

        #listen for keyboard input
        while True:
            event = self.screen.getch()
            if event == ord( "q" ) or event == ord( "Q" ):
                # needs work...
                curses.endwin()
                exit()
            if event == ord( "n" ) or event == ord( "N" ):
                return False
            if event == ord( "l" ) or event == ord( "L" ):
                return True
            else:
                self.body.addstr( 5, 3, "Please make a valid selection." )
                # draw the body
                self.body.refresh()

    def sign_up( self, message=False ):

        # remove old body content
        self.body.clear()

        # allow user to see KB input
        curses.echo()

        # write to body
        self.body.addstr(2, 2, "Pick a new user name and pin:" )
        # draw body
        self.body.refresh()

        # ask for user name
        self.body.addstr(3, 2, "user Name:" )
        name = self.body.getstr(4, 2, 60)

        self.body.addstr(5, 2, "Pin:" )
        #self.body.refresh()
        password = self.body.getstr(6, 2, 60)

        # if error message
        if message:
            self.body.addstr( 7,2, message )
            self.body.refresh()

        return( { 'name':name, 'password':password } )

    def name_exists( self ):
        # remove old body content
        self.body.clear()

        self.body.addstr(2, 2, "Sorry, that name is all ready registered!" )
        return self.sign_up( True )

    def login( self ):
        # remove old body content
        self.body.clear()
        # allow user to see KB input
        curses.echo()

        self.body.addstr(2, 2, "Please log in with your user name and pin:" )

        self.body.addstr(3, 2, "user Name:" )
        name = self.body.getstr(4, 2, 60)
        self.body.addstr(5, 2, "Pin:" )

        self.body.refresh()
        password = self.body.getstr(6, 2, 60)

        return( { 'name':name, 'password':password } )

    def update_side_bar( self, array ):

        # remove old content
        self.side_bar.clear()
        self.side_bar.border(0)
        left = 3
        count = 1
        for i in array:
            self.side_bar.addstr( count, left, i )
            count += 1
        # draw new content
        self.side_bar.refresh()

    def update_user( self, array ):

        # remove old content
        self.header_right.clear()
        self.header_right.border(0)

        left = 10
        count = 1
        for i in array:
            self.header_right.addstr( count, left, i )
            count += 1
        # draw new content
        self.header_right.refresh()

    def show_rpn( self, obj ):
        # remove old body content
        self.body.clear()

        if len(obj) > 2:

            if obj['right_or_wrong']:
                self.body.addstr(2, 2, "Right!" )
            else:
                self.body.addstr(2, 2, "Wrong!, the correct answer is " + obj['answer'] )
            self.body.addstr(3, 2, "time taken: " + obj['time_taken'] )

        self.body.addstr(4, 2, "Please solve!") 
        self.body.addstr(5, 2, obj["rpn"] + "\n" )
        self.body.addstr(6, 2, "?")
        self.body.refresh()
        answer = self.body.getstr(6, 3, 60)
        return answer

    def dev(self, mess ):
        # side bar
        self.dev = curses.newwin( 11, 20, 17 , 53)
        self.dev.border(0)
        pass
##testing

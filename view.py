#!/usr/bin/env python3

import time
import random

class View:
    def __init__( self, screen, curses ):

        self.showDev = False
        self.userName = None

        self.curses = curses
        # start the curses instance
        self.screen = screen

        # configure the whole screen

        # set border for main screen
        self.screen.border(0)
        # hide KB input
        self.curses.noecho()

        self.curses.curs_set(0)

        # idk, i have to look it up
        self.screen.keypad(1)

        # draw the main screen
        self.screen.refresh()

        # setup the header window
        self.header = self.curses.newwin( 4, 35, 2, 3 )
        self.header.border(0)

        # setup the right header window
        self.header_right = self.curses.newwin( 4, 35, 2, 38 )
        self.header_right.border(0)
        self.header_right.refresh()

        # setup the body window
        self.body = self.curses.newwin( 15, 50, 6 , 3)
        # self.body.border(0)

        # side bar
        self.side_bar = self.curses.newwin( 15, 20, 6 , 53)
        self.side_bar.border(0)

        # dev console
        self.dev = self.curses.newwin( 50, 70, 17 , 3)
        self.dev.border(0)

        #############################################

        self.header_right.addstr( 1, 20, "Not logged in")
        self.header_right.refresh()

    def menu( self, sidebar=True ):
        #listen for keyboard input

        # hide KB input
        self.curses.noecho()

        if sidebar:
            array = []

            # check if there is a logged in user
            if self.userName:
                array.extend( [ "l log out", "p play" ] )
            else:
                array.extend( [ "l login", "n new user" ] )

            #append things that are all ways in menu 
            array.extend( [ "", "c cedits", "Q Quit" ] )

            # trigger side bar update
            self.update_side_bar( array )

        # loop to listen for user input
        while True:

            event = self.screen.getch()

            # check if user is logged in
            if self.userName:
                if event == ord( "p" ) or event == ord( "P" ):
                    return { '_return_to': 'new_round' }

                if event == ord( "h" ) or event == ord( "H" ):
                    return { '_return_to': 'home' }

                if event == ord( "l" ) or event == ord( "L" ):
                    return { '_return_to': 'logOut' }
            else:
                if event == ord( "n" ) or event == ord( "N" ):
                    return { '_next': 'sign_up' }

                if event == ord( "l" ) or event == ord( "L" ):
                    return { '_next': 'login' }

            
            # all ways
            if event == ord( "c" ) or event == ord( "C" ):
                return { '_next': 'about' }

            if event == ord( "q" ) or event == ord( "Q" ):
                # needs work...
                self.curses.endwin()
                exit()
            else:
                self.side_bar.addstr( 12, 2, "invalid choice." )
                # draw the body
                self.curses.flash()
                self.side_bar.refresh()

    def welcome( self, message=False ):

        # write the header up
        self.header.addstr( 1, 2, "Welcome to the RPN game!" )
        #draw the header
        self.header.addstr( 2, 2, "Go bears!" )
        if self.showDev:
            self.header.addstr( 2, 12, "-dev" )

        self.header.refresh()

        # short pause
        time.sleep(.5)

        self.body.clear()
        self.body.refresh()

        # write the body
        self.body.addstr( 1, 3, "c cedits" )
        self.body.addstr( 3, 3, "l login" )
        self.body.addstr( 4, 3, "n new user" )
        self.body.addstr( 6, 3, "Q Quit" )

        # draw the body
        self.body.refresh()

        #listen for keyboard input
        return self.menu()

    def sign_up( self, message=False ):

        # remove old body content
        self.body.clear()

        # allow user to see KB input
        self.curses.echo()

        # remove old content
        self.side_bar.clear()
        self.side_bar.refresh()

        # write to body
        self.body.addstr(2, 2, "Pick a new user name and pin:" )
        # draw body
        self.body.refresh()

        # show error message
        if message:
            self.body.addstr( 7, 2, message )
            self.body.refresh()

        # ask for user name
        self.body.addstr(3, 2, "user Name:" )
        name = self.body.getstr(4, 2, 60)

        self.body.addstr(5, 2, "Pin:" )
        #self.body.refresh()
        password = self.body.getstr(6, 2, 60)

        return( { 'name':name, 'password':password, '_return_to': 'sign_up' } )

    def login( self, message=False ):
    
        # remove old body content
        self.body.clear()

        # remove old content
        self.side_bar.clear()
        self.side_bar.refresh()

        # allow user to see KB input
        self.curses.echo()

        if message:
            self.curses.flash()
            self.body.addstr( 7, 2, message )
            self.body.refresh()

        self.body.addstr(2, 2, "Please log in with your user name and pin:" )

        self.body.addstr(3, 2, "user Name:" )
        name = self.body.getstr(4, 2, 60)
        self.body.addstr(5, 2, "Pin:" )

        self.body.refresh()
        password = self.body.getstr(6, 2, 60)

        # if error message

        return( { 'name':name, 'password':password, '_return_to': 'login' } )

    def home( self, array ):
        # remove old content
        self.body.clear()
        self.body.border(0)
        left = 2
        count = 1
        for i in array:
            self.body.addstr( count, left, str( i ) )
            count += 1
            if count > 12: break
        # draw new content
        self.body.refresh()

        return self.menu()

    def update_side_bar( self, array ):

        # remove old content
        self.side_bar.clear()
        self.side_bar.border(0)
        left = 3
        count = 1
        for i in array:
            self.side_bar.addstr( count, left, str(i) )
            count += 1
        # draw new content
        self.side_bar.refresh()

    def update_user( self, array ):
        self.userName = array[0]
        if not self.userName:
            display = "Please log in"
        else:
            display = array[0]
        # remove old content
        self.header_right.clear()
        self.header_right.border(0)

        left = 33 - len( display )

        self.header_right.addstr( 1, left, display )
        # draw new content
        self.header_right.refresh()

    def show_rpn( self, obj ):
        # remove old body content
        self.body.clear()
        
        self.side_bar.clear()
        self.side_bar.refresh()

                # allow user to see KB input
        self.curses.echo()

        if len(obj) > 2:

            if obj['right_or_wrong']:
                self.body.addstr(2, 2, "Right!" )
            else:
                self.body.addstr(2, 2, "Wrong!, the correct answer is " + obj['answer'] )
            self.body.addstr(3, 2, "time taken: " + str(obj['time_taken']) )

        self.body.addstr( 4, 2, "Please solve!") 
        self.body.addstr( 5, 2, obj["rpn"] )
        self.body.addstr( 6, 2, "?")
        self.body.refresh()
        answer = self.body.getstr( 6, 3, 60 )
        return answer

    def about( self, message=False ):
        # remove old body content
        self.body.clear()
        self.body.border(0)

        self.side_bar.clear()
        self.side_bar.refresh()

        array = [
            {
                'name': "William Mantly", 
                'email': "wmantly@gmail.com", 
                'desc': "Designed and implemented the UI."
            },{
                'name': "Benjamin Himley", 
                'email': "benjaminhimley85@gmail.com", 
                'desc': "wrote rpn generator and controller,",
                'desc2': "bugfix assit"
            },{
                'name': "Adolfo Reyes", 
                'email': "adolfo0620@gmail.com", 
                'desc': "bug hunter"
            },{
                'name': "Brendan Gilroy", 
                'email': "BDGilroy@gmail.com"
            }
        ]

        random.shuffle(array)

        line = 2
        for i in array:
            self.body.addstr( line, 2, i['name'] + ' - ' + i['email'] )
            if 'desc' in i:
                line += 1
                self.body.addstr( line, 2, i['desc'] )
            if 'desc2' in i:
                line += 1
                self.body.addstr( line, 2, i['desc2'] )
            line += 2
            self.body.refresh()
            time.sleep(1)

        return self.menu()

    def devConsole( self, message, sleep=2 ):
        # side bar
        if not self.showDev: return False

        self.dev.clear()
        self.dev.border(0)
        
        count = 0
        for i in message:
            count += 1
            self.dev.addstr( count, 2, i )
            print( i )

        self.dev.refresh()
        time.sleep( sleep )

##testing

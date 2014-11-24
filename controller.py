from view import View
import model
import sys
from datetime import datetime
import curses

db = model.DB()

class Game:
    def __init__ (self, screen):

        # initialize the View class
        self.view = View( screen, curses )
        self.sesh_totals = {}  
        self.sesh_totals['time'] = 0
        self.sesh_totals['correct'] = 0
        self.sesh_totals['wrong'] = 0
        self.sesh_totals['difficulty'] = 1   

        if 'dev' in sys.argv:
            self.view.showDev = True

        self.view_loader( "welcome" )

    def view_loader( self, view_name, passing=None ):
        re = getattr( self.view , view_name )( passing )

        if type( re ) == dict:
            if '_return_to' in re:
                return getattr( self, re['_return_to'] )( re )

            if '_next' in re:
                self.view_loader( re['_next'] )
        return re

    def sign_up(self, obj):
        this_user = db.create_user(obj['name'], obj['password'])
        if this_user:
            self.view.update_user( [ obj['name'] ] )
            db.save_sesh(this_user.user_id)
            self.new_round()
        else:
            message = "User name taken"
            self.view_loader( "sign_up", message )

    def login(self, obj):
        this_user = db.fetch_user(obj['name'], obj['password'])
        if this_user:
            db.save_sesh(this_user.user_id)             
            self.view.update_user( [ obj['name'] ] )
            self.new_round()
        else:
            message = "Invalid login"
            self.login( self.view.login( message ) )

    def home( self, obj=[] ):
        self.view_loader( 'home', obj )

    def logOut( self, message=False ):
        self.view.update_user( [ None ] )
        self.view_loader( "welcome" )

    def new_round(self, last_turn = None, difficulty=1):
        if last_turn: last_turn = self.last_turn
        new_turn = model.Turns(difficulty)
        new_turn.start_time = datetime.now()
        rpn_as_string = ' '.join(new_turn.rpn.expression)
        info_obj = {}
        info_obj["rpn"] = rpn_as_string
        self.change_sesh_totals(last_turn)
        if last_turn:
            last_turn.time_taken = last_turn.end_time - last_turn.start_time
            info_obj["time_taken"] = (last_turn.time_taken)
            info_obj["last_rpn"] = last_turn.rpn.expression
            info_obj["answer"] = last_turn.rpn.solution
            info_obj["right_or_wrong"] = last_turn.correct_incorrect

        answer = self.view_loader( 'show_rpn', info_obj )
        self.view.devConsole( [ str(type(answer)), str( len( info_obj ) ) ] )
        ## if answer != int: return False 
        self.view.devConsole( (str(self.sesh_totals['difficulty']), str(self.sesh_totals['correct']), str(self.sesh_totals['wrong']) ))
        new_turn.correct_incorrect = (int(new_turn.rpn.solution) == int(answer))
        new_turn.end_time = datetime.now()
        new_turn.time_taken = str(new_turn.end_time - new_turn.start_time)
        db.save_turn(new_turn)
        self.last_turn = new_turn
        self.last_info_obj = info_obj
        # self.new_round(new_turn, self.sesh_totals['difficulty'])
        return self.home( self.sesh_totals.items() )

    def change_sesh_totals(self, last_turn=None):
        if last_turn:
            self.sesh_totals['time'] = last_turn.time_taken
            self.sesh_totals['correct'] += 1 if last_turn.correct_incorrect else 0
            self.sesh_totals['wrong'] += 0 if last_turn.correct_incorrect else 1
            self.sesh_totals['difficulty'] = 1

        if self.sesh_totals['correct'] + 3 <= self.sesh_totals['wrong']:
            self.sesh_totals['difficulty'] -= 1 if self.sesh_totals['difficulty'] > 1 else 0
        if self.sesh_totals['correct'] - 3 >= self.sesh_totals['wrong']:
            self.sesh_totals['difficulty'] += 1           
        #self.view.update_side_bar( ['last time', self.sesh_totals['time'],'correct', str(self.sesh_totals['correct']), 'wrong', str(self.sesh_totals['wrong']),'difficulty', str(self.sesh_totals['difficulty']) ] )

    def calculate_next_rpn_diff(self):
        #run some queries in the db to see if we should up the difficulty or drop it
        pass        

    def check_high_scores(self):
        #get high scores from model/db
        #pass scores to view
        pass

    def check_personal_stats(self):
        #get personal stats from model/db
        #pass scores to view
        pass

    def end_game(self):
        model.close_db()
        sys.exit()

# start the main process in a curses wrapper
# this MUST be done for a clean exit!!!
# https://docs.python.org/3/library/curses.html#curses.wrapper

try: 
     curses.wrapper( Game ) 
except KeyboardInterrupt: 
     print( "Got KeyboardInterrupt exception. Exiting..." )
     exit() 

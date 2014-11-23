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

        if 'dev' in sys.argv:
            self.view.showDev = True

        if self.view.welcome():
            self.login(self.view.login())
        else:
            self.sign_up(self.view.sign_up())

    def sign_up(self, obj):
        this_user = db.create_user(obj['name'], obj['password'])
        if this_user:
            self.view.update_user( obj['name'] )
            db.save_sesh(this_user.user_id)
            self.new_round()
        else:
            message = "User name taken"
            self.sign_up( self.view.sign_up( message ) )

    def login(self, obj):
        this_user = db.fetch_user(obj['name'], obj['password'])
        if this_user:
            self.view.devConsole( [obj['name'], obj['password']] )
            db.save_sesh(this_user.user_id)             
            self.view.update_user( obj['name'] )
            self.new_round()
        else:
            message = "Invalid login"
            self.login( self.view.login( message ) )

    def new_round(self, last_turn = None):
        # please find a way to get the user name into the call below
        self.view.update_user( [ 'user name variable here' ] )

        new_turn = model.Turns()
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

        answer = self.view.show_rpn(info_obj)
        new_turn.correct_incorrect = (new_turn.rpn.solution == answer)
        new_turn.end_time = datetime.now()
        new_turn.time_taken = new_turn.end_time - new_turn.start_time
        db = model.DB()
        db.save_turn(new_turn)
        self.new_round(new_turn)

    def change_sesh_totals(self, last_turn=None):
        self.sesh_totals['time'] = 0
        self.sesh_totals['correct'] = 0
        self.sesh_totals['wrong'] = 0
        self.sesh_totals['difficulty'] = 1   

        if last_turn:
            self.sesh_totals['time'] += last_turn.time_taken
            self.sesh_totals['correct'] += 1 if last_turn.correct_incorrect else 0
            self.sesh_totals['correct'] += 0 if last_turn.correct_incorrect else 1
            self.sesh_totals['difficulty'] = 1
        # each value of the list is line of output on the sidebar
        self.view.update_side_bar( ['time', str(self.sesh_totals['time']),'correct', str(self.sesh_totals['correct']), 'wrong', str(self.sesh_totals['wrong']),'difficulty', str(self.sesh_totals['difficulty']) ] )

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
# curses.wrapper(Game) 

try: 
     curses.wrapper( Game ) 
except KeyboardInterrupt: 
     print( "Got KeyboardInterrupt exception. Exiting..." )
     exit() 

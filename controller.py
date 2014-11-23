import model
from view import View
import sys
from datetime import datetime

view = View()

class Game:
    def __init__ (self):
        if view.welcome():
            self.login(view.login())
        else:
            self.sign_up(view.sign_up())

    def sign_up(self, obj):
        db = model.DB()
        this_user = db.create_user(obj['name'], obj['password'])
        print(this_user)
        input()
        if this_user:
            self.new_round()
        else:
            self.sign_up( view.name_exists() )

    def login(self, obj):
        db = model.DB()
        verify = db.fetch_user(obj['name'], obj['password'])
        if verify:
            self.new_round()
        else:
            view.incorrect_password()

    def new_round(self, last_turn = None):
        new_turn = model.Turns()
        new_turn.start_time = datetime.now()
        rpn_as_string = ''.join(new_turn.rpn.expression)
        info_obj = {}
        info_obj["rpn"] = rpn_as_string
        if last_turn:
            info_obj["time_taken"] = (last_turn.end_time - last_turn.start_time)
            info_obj["last_rpn"] = last_turn.rpn.expression
            info_obj["answer"] = last_turn.rpn.solution
            info_obj["right_or_wrong"] = last_turn.correct_incorrect
        answer = view.show_rpn(info_obj)
        new_turn.correct_incorrect = (new_turn.rpn.solution == answer)
        new_turn.end_time = datetime.now()
        new_turn.time_taken = new_turn.end_time - new_turn.start_time
        db.save_turn(new_turn)
        self.new_round(new_turn)

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

this_game = Game()

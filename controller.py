import model
import view
import sys
from datetime import datetime


class Game:
    def __init__ (self):
        if view.welcome():
            self.login(view.login())
        else:
            self.sign_up(view.sign_up())

    def sign_up(self, obj):
        verify = model.sign_up(obj)
        if verify:
            self.next_round(verify)
        else:
            view.name_exists()

    def login(self, obj):
        verify = model.login(obj)
        if verify:
            self.next_round(verify)
        else:
            view.incorrect_password()

    def end_round(self, real_answer, their_answer):
        model.save_turn((real_answer == their_answer), datetime.now(), diff)
        self.next_round()

    def next_round(self):
        rpn = model.new_rpn()
        start_time = datetime.now()
        view.show_rpn(rpn, start_time, rpn.diff)


    # def check_high_scores(self):
        #get high scores from model/db
        # pass

    # def check_personal_stats(self):
        #get personal stats from model/db
        # pass

    def end_game(self):
        model.close_db()
        sys.exit()

this_game = Game()
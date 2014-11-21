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
        this_user = model.User.create_new_user(obj)
        if this_user:
            self.next_round(this_user)
        else:
            view.name_exists()

    def login(self, obj):
        verify = model.User(obj)
        if verify:
            self.next_round(verify)
        else:
            view.incorrect_password()

    def new_round(self, last_turn = None):
        new_turn = Turn.create_turn()
        now_turn.start_time = datetime.now()
        rpn_as_string = ''.join(new_turn.rpn.equation)
        show_info_and_rpn = []
        show_info_and_rpn.append(rpn_as_string)
        if last_turn:
            show_info_and_rpn.append(last_turn.end_time - last_turn.start_time)
            show_info_and_rpn.append(last_turn.rpn.equation)
            show_info_and_rpn.append(last_turn.rpn.answer_equation)
        answer = view.show_rpn(show_info_and_rpn)
        new_turn.correct_incorrect = (new_turn.rpn.answer_equation == answer)
        new_turn.end_time = datetime.now()
        db.save_turn(new_turn)
        self.new_round(new_turn)

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
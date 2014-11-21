import model
import view
import sys

class Game:
    def __init__ (self):
        self.start_game(view.welcome())
        # get name and pass to model
        pass

    def start_game(self, name):
        # give name to model/db
        #get rpm from model/db
        #give rpm to view
        #save start time
        pass

    def end_round(self, real_answer, their_answer):
        pass
        #store stats in db
        self.next_round()

    def next_round(self):
        pass
        #save last round stats (time, )
        #get next rpm from model/db


    # def check_high_scores(self):
        #get high scores from model/db
        # pass

    # def check_personal_stats(self):
        #get personal stats from model/db
        # pass

    def end_game(self):
        #close db
        sys.exit()

this_game = Game()
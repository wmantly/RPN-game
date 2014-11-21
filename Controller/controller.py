import model
import view

class Game:
    def __init__ (self):
        # display initial view
        pass

    def create_account(self, name):
        model.create_account(name)
        pass

    def start_game(self):
        #get rpm from model/db
        #give rpm to view
        #save start time
        pass

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
        pass
        #close db
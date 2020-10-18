import random



class Player:
    def __init__(self):
        self.total_score = 0
        self.this_round_score = 0
        self.on_turn = False
    def get_total_score(self):
        return self.total_score
    def get_this_round_score(self):
        return self.this_round_score
    def set_on_turn(self,on_turn):
        self.on_turn = on_turn
    def add_score(self,added_score):
        self.this_round_score = self.this_round_score + added_score
        if self.this_round_score + self.total_score >=100:
            self.total_score=self.this_round_score + self.total_score
            #self.this_round_score = 0
    def hold(self):
        self.total_score = self.this_round_score + self.total_score
        self.this_round_score = 0
        self.on_turn = False
    def lost_score(self):
        self.this_round_score = 0
        self.on_turn = False

class Die:
    def __init__(self):
        self.die_number = 0
    def roll(self):
        self.die_number = random.randint(1,6)
    def get_die_number(self):
        return self.die_number

def main():
    game_start = 1
    number_of_players = input("Please input how many players: ")
    players =[]
    for i in range(int(number_of_players)):
        player = Player()
        players.append(player)
    on_turn_index = 0
    die = Die()
    while game_start==1:
        change_turn=0
        while change_turn==0:
            decision = input("Player"+str(on_turn_index+1)+", do you want to roll or hold (r:roll / h:hold): ")
            if decision=="r":
                die.roll()
                if die.get_die_number()==1:
                    players[on_turn_index].lost_score()
                    change_turn =1
                else:
                    players[on_turn_index].add_score(die.get_die_number())
                print("Player" + str(on_turn_index+1) + " rolled " + str(die.get_die_number())
                      +", total score is "+str(players[on_turn_index].get_total_score())
                      +", score in this round is "+str(players[on_turn_index].get_this_round_score()))
                if players[on_turn_index].get_total_score()>=100:
                    game_start = 0
                    change_turn =1
                    print("Player" + str(on_turn_index + 1) + " win the game with a total of " + str(
                        players[on_turn_index].get_total_score()) + "!")
            else:
                players[on_turn_index].hold()
                change_turn=1
        if on_turn_index != int(number_of_players) - 1:
            on_turn_index = on_turn_index + 1
        else:
            on_turn_index = 0


if __name__ == "__main__":
    main()
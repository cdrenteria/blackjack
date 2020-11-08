from random import shuffle
import time
import ast


class Card:
    """ Builds a single card"""
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def display_card(self):
        """This displays the value and suit of card, if the card is a face card it assigns a value of 10"""
        print(f"{self.value} of {self.suit}")
        if self.value == "Jack":
            self.value = 10
        if self.value == "Queen":
            self.value = 10
        if self.value == "Ace":
            self.value = 10
        if self.value == "King":
            self.value = 10


class Deck:
    """Builds, shuffles, and displays a deck of cards using the Card class"""
    def __init__(self, amount=1):
        self.amount = amount
        self.cards = []

    def build_deck(self):
        """Builds a new deck of 52 cards using the Card Class"""

        for d in range(self.amount):
            for s in ["Hearts" , "Spades" , "Diamonds" , "Clubs"]:
                for v in range(1, 11):
                    self.cards.append(Card(v, s))
            for s in ["Hearts" , "Spades" , "Diamonds" , "Clubs"]:
                for v in ["Jack" , "Queen" , "King", "Ace"]:
                    self.cards.append(Card(v, s))


    def display_deck(self):
        """For every card contained in the deck it prints the suit and value"""
        for c in self.cards:
            c.display_card()

    def shuffle_deck(self):
        """ Randomly rearranges the cards"""
        shuffle(self.cards)


class Player:
    def __init__(self):
        self.hand = []
        self.amount = 0
        self.play = True
        self.score = 0

    def draw_card(self):
        """ Draws a card and adds it the players hand and check the player total value of cards to see if is lower, equal
        to or higher than 21"""
        self.hand.append(d1.cards.pop())
        self.hand[-1].display_card()
        inc_amount = self.hand[-1].value
        self.amount += inc_amount
        if self.amount > 21:
            print("Bust!")
        elif self.amount == 21:
            print("You win!")
            p1.score += 200
            print(p1.score)
        elif self.amount < 21:
            p1.player_input()

    def player_input(self):
        """Allow a player to hit or pass"""
        if self.play == True:
            p1_input = input(f"You have {self.amount} would you like to hit or pass? [1 - hit / 0 - pass]: ")

        if p1_input == "1" or p1_input.lower() == "hit":
            p1.draw_card()
        elif p1_input == "0" or p1_input.lower() == "pass":  # Problem! When I enter "0" it repeats p1_input once.
            print("Alright, my turn!")
        else:
            print("Please hit or pass")


class Dealer(Player):
    """
    This is a subclass of Player and inherits it's attributes. This class plays 21 against the Player using 'if' logic
    """
    def __init__(self):
        super().__init__()
        self.hand = []
        self.amount = 0

    def dealer_draw_car(self):
        """
        The dealer draws a card, check's the value of the cards in his and and will either hit if he has less then the player
        and stay if he has more while being under 21 total. The dealer looses if his is lower so he will hit
        even if he is very close to 21 since it is his only option to win. The dealer will 'push' if he is equal to
        the player.
        """
        self.hand.append(d1.cards.pop())
        self.hand[-1].display_card()
        time.sleep(1)
        inc_amount = self.hand[-1].value
        self.amount += inc_amount
        if self.amount > 21: #If the dealer goes over 21 they lose
            print("I went over! You win!")
            p1.score += 100
            print(p1.score)
            time.sleep(1)
        elif self.amount == 21: #If the dealer hits 21 they lose
            print(f" You had {p1.amount} and I have {self.amount} I win!")
            time.sleep(1)
        elif abs(21-self.amount) < abs(21-p1.amount): #if the dealer gets closer to 21 then the palyer they win
            print(f" You had {p1.amount} and I have {self.amount} I win!")
            time.sleep(1)
        elif self.amount > 18 and (abs(21 - self.amount) == abs(21 - p1.amount)): # if the dealer is over 18 and equal to the player they push
            print("Push")
            time.sleep(1)
        else:
            p2.dealer_draw_car()

def play_game():
    """"Runs a continous loop that plays blackjack"""

    p1.draw_card()
    if p1.amount < 21:
        p2.dealer_draw_car()
    p2.amount = 0
    p1.amount = 0


def setup_game():
    """
    Creates the new deck and shuffles it
    :return:
    """
    d1.build_deck()
    d1.shuffle_deck()


def end_game():
    """Ends the game, resets the cards, and checks for a high score. If Player has new high score it will allow them to
    save their score and name"""

    with open("high_score.txt", "r") as high_scores:
        high_score_dict = ast.literal_eval(high_scores.read())
        print(p1.score)
        for k in high_score_dict:
            if p1.score > high_score_dict[k]:
                print("New High Score!")
                high_score_name = input("What is your name? ")
                new_high_score = {high_score_name: p1.score}
                with open("high_score.txt", "w") as high_scores:
                    high_scores.truncate(0)
                    high_scores.write(str(new_high_score))
    p1.score = 0
    d1.cards = []
    setup_game()
    print("Shuffling the deck!")
    time.sleep(1)

d1 = Deck()
setup_game()
p2 = Dealer()
p1 = Player()
while True:
    play_game()
    if len(d1.cards) <= (d1.amount * 13):
        end_game()
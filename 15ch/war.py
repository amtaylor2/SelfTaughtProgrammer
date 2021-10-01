#Two class variables suits and values
#Cards
class Card:
    suits = ("spades", 
    "hearts",
    "diamonds",
    "clubs")
#add 2 None so values correspond with index value
    values = (None, None, 
    "2", "3", "4","5", "6", "7","8","9","10",
    "Jack","Queen","King", "Ace")

    def __init__(self,v,s):
        """suit + value are ints"""
        self.value = v
        self.suit = s
#checks if card less than
    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
            return False
#checks if card is greater than
    def __gt__(self,c2):
        if self.value > c2.value:
            return True
        if self.value == c2.suit:
            if self.suit > c2.suit:
                return True
            else:
                return False
            return False
#returns the card value and suit
    def __repr__(self):
        v = self.value[self.value] + \
            " of " + self.suits[self.suit]
        return v
#Deck
class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2,15):
            for j in range(4):
                self.cards.append(Card(i,j))
#nested for loop creates cards for each suit
    def rm_card(self):
        if len(self.cards) == 0:
            return
        return self.cards.pop()

deck = Deck()
for card in deck.cards:
    print(card)

#Player

class Player:
    def __init__(self,name):
        self.wins = 0
        self.card = None
        self.name = name

#Game

class Game:
    def __init__(self):
        name1 = input("player one")
        name2 = input("player two")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins(self,winner):
        w = "{} wins this round"
        w = w.format(winner)
        print(w)

    def draw(self,p1n, p1c,p2n,p2c):
        d = "{} drew {} {} drew {}"
        d = d.format(p1n,p1c,p2n,p2c)
        print(d)
    
    def play_game(self):
        cards = self.deck.cards
        print("beginning War!")
        while len(cards) >= 2:
            m = "q to quit. Any" + \
                "key to play:"
            response = input(m)
            if response == 'q':
                break
            p1c = self.deck.rm_card()
            p2c = self.deck.rm_card()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n,p1c,p2n,p2c)

            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)

        win = self.winner(self.p1, self.p2)
        print("War is over.{} wins".format(win))

    def winner(self,p1,p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        return "It was a tie!"
game = Game()
game.play_game()
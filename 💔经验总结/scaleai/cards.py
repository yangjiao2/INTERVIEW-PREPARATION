from random import shuffle
from enum import Enum
from collections import defaultdict

class GameState(Enum):
    READY = 'READY'
    STARTED = 'STARTED'
    END = 'END'

# class CardSuit(Enum):
#     1 = 'Club'
#     2 = 'Heart'
#     3 = 'Diamond'
#     4 = 'Spade'
#     # Heart = 2
#     # Diamond = 3
#     # Spade = 4

# class CardRank(Enum):
#     11 = "J"
#     12 = "Q"
#     13 = "K"
#     1 = "A"

class CardSuit(Enum):
    CLUB, HEART, DIAMOND, SPADE = range(1, 5)

class CardRank(Enum):
    TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN = range(2, 11)
    JACK, QUEEN, KING, ACE = range(11, 15)


class Card():
    # suits = ["spades",
    #          "hearts",
    #          "diamonds",
    #          "clubs"]

    # values = [None, None,"2", "3",
    #           "4", "5", "6", "7",
    #           "8", "9", "10",
    #           "Jack", "Queen",
    #           "King", "Ace"]

    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    # @property
    def value(self):
        return self.value

    # @property
    def suit(self):
        return self.suit


    def __lt__(self, c2):
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        return False

    def __gt__(self, c2):
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        return False

    def __eq__(self, c2):
        return (not self.__lt__(c2)) and (not self.__gt__(c2))


    def __repr__(self):
        rank_key = str(CardRank(self.value).name)
        v = rank_key +\
            " of " + \
            (CardSuit(self.suit).name)
        return v


class Deck:
    def __init__(self, cards = []):
        self.cards = cards
        self.shuffle()

    def shuffle(self):
        shuffle(self.cards)

    def draw(self, draw_card_rule = None, args = {}):
        # prev = args.get("history", None)
        draw_cards = args.get("draw_cards", [])

        if len(self.cards) == 0:
            return (None, None)
        card = None
        if draw_card_rule != None:
            draw_cards, remaining_cards = draw_card_rule.execute_rule("default", self.cards, args)
            # self.cards = remaining_cards
            # print ("remaining_cards", remaining_cards)
            return (draw_cards, remaining_cards)

        elif draw_cards == None:
            return (self.cards.pop(), self.cards)
        else:
            cards_existed = all([card in self.cards for card in draw_cards])
            if not cards_existed:
                raise Exception("cards can not be draw, not existed")
            remaining_cards = list(filter( lambda x: x != card, self.cards))
            self.cards = remaining_cards

        return (draw_cards, remaining_cards)

    def add(self, cards):
        if isinstance(cards, list):
            self.cards += cards
        else:
            self.cards.append(cards)

    def sort(self):
        return sorted(self.cards)

    def __repr__(self):
        for card in self.cards:
            cards = ", ".join(str(card))
        return cards


class Hand(Deck):
    def __init__(self):
        super().__init__()


class Player():
    def __init__(self, name):
        self.wins = 0
        self.name = name
        self.hand = Hand()

    def draw_card_from_hand(self, rule, args = {}):
        cards, remain_cards = self.hand.draw(rule, args)
        return cards

    def draw_card_from_deck(self, rule, args = {}):
        deck = args.get("deck")
        cards, remain_cards = deck.draw(rule, args)
        self.hand.add(cards)
        # print (self.hand)

        deck.cards = remain_cards
        return cards


class RuleEngine():
    def __init__(self, name):
        self.name = name
        self.conditions = {}

    def add_condition(self, fact, condition):
        self.conditions[fact]=condition

    def execute_rule(self, fact= "default", cards = [],  args = {}):
        # print ("execute", fact, self.conditions[fact])
        return self.conditions[fact](cards, args)
    
    # def evaluate(self, facts, args):
    #     return list([fact(args) for fact in facts])


class DrawTopRule(RuleEngine):
    def __init__(self, name = "draw_first_one"):
        super().__init__(name)
        def execute(cards, args):
            if len(cards) != 0:
                return (cards[0], cards[1:])
            return (None, None)

        self.add_condition("default", execute)
    
class SingleCardRule(RuleEngine):
    def __init__(self, name = "single_card"):
        super().__init__(name)
        # self.history = history

        # def compare(obj1, obj2):
        #     return obj1 < obj2
        def execute( cards,  args = {}):
            history = args.get("history", None)
            # print ("history", history, cards)
            for card in sorted(cards):
                # print ("sorted(cards)", card)
                if (history and history < card) or (not history):
                    return (card, [rest for rest in cards if rest != card])

        self.add_condition("default", execute)



class MultiCardRule(RuleEngine):
    def __init__(self, name, history = []):
        super().__init__("multi_card")

        def compare(list1, list2):
            if len(list1) == len(list2):
                value1 = [card.value for card in list1]
                value2 = [card.value for card in list2]

                if len(set(value1)) == len(set(value2)) and len(set(value2))  == 1:
                    return list(set(value1))[0] < list(set(value2))[0]

        self.add_condition("same_value", compare)

class Game():
    def __init__(self, draw_card_rule = None):

        self.deck = Deck([])
        self._addAllCards()

        self.players = []
        self.status = GameState.READY
        self.player_index = 0
    
        self.scores = defaultdict(int)

    def startGame(self, player_count = 2):
        for i in range(1, player_count + 1):
            # name = input("player name: ")
            self._addPlayer(str(i))
        self.status = GameState.STARTED
        self.play()

    def play(self):
        player = self.players[self.player_index]
        print ('deck: remain {}'.format( len(self.deck.cards)))
        command = input('Player{}: draw card? (y/n)'.format(player.name))
        prev = None
        while len(self.deck.cards) != 0 and command == 'y':
            player = self.players[self.player_index]
            # card = player.hand.draw()
            # card = self.draw_card_rule.execute_rule()(self.deck.cards)
            if len(player.hand.cards) > 5:
                curr_cards = player.draw_card_from_hand(SingleCardRule(), {"history": prev})
                print ('{} card draw from player {}'.format(curr_cards, player.name))
                prev = curr_cards
                command = input('Player{}: continue to draw card? (y/n)'.format(self.players[self.player_index].name))


            curr_cards = player.draw_card_from_deck(DrawTopRule(), {"deck": self.deck})
            print ('deck: remain {}'.format( len(self.deck.cards)))
            self.switchPlayer()ç


    # def addScore(self, player_index, score):
    #     self.scores[player_index] += score

    def endGame(self):
        self.status = GameState.END

    def _addAllCards(self):
        for rank in CardRank:
            for suit in CardSuit:
        # for i in range(1, 14):
        #     for j in range(4):
                self.deck.add(Card(rank.value,
                                 suit.value))

                        
    def _addPlayer(self, name = ""):
        if self.status == GameState.READY:
            player_name = name if name != "" else "Player" + len(self.players) + 1
            self.players.append(Player(player_name))
        else:
            raise Exception('not allow to add player when game in state' + game.status)

    def switchPlayer(self, index=None):
        if index != None:
            self.player_index = index % len(self.players)
        else:
            self.player_index = (self.player_index + 1) % len(self.players)


    def wins(self, winner):
        w = "{} wins this round".format(winner)
        # print(w)
        self.endGame()

game = Game()
game.startGame(player_count=2)

    # def draw(self, p1n, p1c, p2n, p2c):
    #     d = "{} drew {} {} drew {}"
    #     d = d.format(p1n,
    #                  p1c,
    #                  p2n,
    #                  p2c)
    #     print(d)

#     def play_game(self):
#         cards = self.deck.cards
#         print("beginning War!")
#         while len(cards) >= 2:
#             m = "q to quit. Any " + \
#                 "key to play:"
#             response = input(m)
#             if response == 'q':
#                 break
#             p1c = self.deck.rm_card()
#             p2c = self.deck.rm_card()
#             p1n = self.p1.name
#             p2n = self.p2.name
#             self.draw(p1n,
#                       p1c,
#                       p2n,
#                       p2c)
#             if p1c > p2c:
#                 self.p1.wins += 1
#                 self.wins(self.p1.name)
#             else:
#                 self.p2.wins += 1
#                 self.wins(self.p2.name)

#         win = self.winner(self.p1,
#                          self.p2)
#         print("War is over.{} wins"
#               .format(win))

#     def winner(self, p1, p2):
#         if p1.wins > p2.wins:
#             return p1.name
#         if p1.wins < p2.wins:
#             return p2.name
#         return "It was a tie!"

# game = Game()
# game.play_game()
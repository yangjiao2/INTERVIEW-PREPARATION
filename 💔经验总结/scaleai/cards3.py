from enum import Enum
import random

class Suit(Enum):
    HEARTS = 'Hearts'
    DIAMONDS = 'Diamonds'
    CLUBS = 'Clubs'
    SPADES = 'Spades'

class Rank(Enum):
    TWO = '2'
    THREE = '3'
    FOUR = '4'
    FIVE = '5'
    SIX = '6'
    SEVEN = '7'
    EIGHT = '8'
    NINE = '9'
    TEN = '10'
    JACK = 'Jack'
    QUEEN = 'Queen'
    KING = 'King'
    ACE = 'Ace'

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __repr__(self):
        return f"{self.rank.value} of {self.suit.value}"

class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in Suit for rank in Rank]

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()

    def deal_holdem(self):
        private_cards = [self.draw() for _ in range(2)]
        community_cards = [self.draw() for _ in range(5)]
        return private_cards, community_cards

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, cards):
        self.hand.extend(cards)

    def show_hand(self):
        for card in self.hand:
            print(card)


class TwentyOnePointGame(Game):
    def deal_initial_cards(self):
        for _ in range(2):
            self.player1.draw(self.deck.draw())
            self.player2.draw(self.deck.draw())

    def get_hand_value(self, player):
        value = 0
        num_aces = 0

        for card in player.hand:
            if card.rank in [Rank.TEN, Rank.JACK, Rank.QUEEN, Rank.KING]:
                value += 10
            elif card.rank == Rank.ACE:
                num_aces += 1
                value += 11
            else:
                value += int(card.rank.value)

        while value > 21 and num_aces > 0:
            value -= 10
            num_aces -= 1

        return value

    def check_winner(self):
        player1_value = self.get_hand_value(self.player1)
        player2_value = self.get_hand_value(self.player2)

        if player1_value > 21 and player2_value > 21:
            return "No one wins, both players busted!"
        elif player1_value > 21:
            return f"{self.player2.name} wins with {player2_value} points!"
        elif player2_value > 21:
            return f"{self.player1.name} wins with {player1_value} points!"
        elif player1_value == player2_value:
            return "It's a tie!"
        elif player1_value == 21:
            return f"{self.player1.name} wins with 21 points!"
        elif player2_value == 21:
            return f"{self.player2.name} wins with 21 points!"
        elif player1_value > player2_value:
            return f"{self.player1.name} wins with {player1_value} points!"
        else:
            return f"{self.player2.name} wins with {player2_value} points!"


class TexasHoldemGame:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.community_cards = []
        self.deck = Deck()

    def deal_initial_cards(self):
        private_cards1, private_cards2 = self.deck.deal_holdem()
        self.player1.draw(private_cards1)
        self.player2.draw(private_cards2)
        self.community_cards = self.deck.deal_holdem()[1]

    def show_community_cards(self):
        print("\nCommunity Cards:")
        for card in self.community_cards:
            print(card)

    def get_hand_value(self, player):
        # Add hand value calculation logic here
        pass

    def check_winner(self):
        # Add winner checking logic here
        pass


class Console:
    def __init__(self, game):
        self.game = game

    def start_game(self):
        # Deal initial cards and set the current player to player 1
        self.game.deal_initial_cards()
        current_player = self.game.player1

        while True:
            self.display_game_state()
            self.handle_player_turn(current_player)
            if self.check_game_over():
                break

            current_player = self.switch_player(current_player)

        self.display_game_result()

    def display_game_state(self):
        print("\nCurrent Game State:")
        # Display player hands and community cards
        self.game.player1.show_hand()
        self.game.player2.show_hand()
        if isinstance(self.game, TexasHoldemGame):
            self.game.show_community_cards()

    def handle_player_turn(self, player):
        print(f"\n{player.name}'s turn:")
        while True:
            action = input("Enter 'h' to hit or 's' to stand: ").lower()
            if action == 'h':
                player.draw(self.game.deck.draw())
                break
            elif action == 's':
                break
            else:
                print("Invalid input. Please enter 'h' or 's'.")

    def check_game_over(self):
        player1_value = self.game.player1.get_hand_value()
        player2_value = self.game.player2.get_hand_value()

        if player1_value >= 21 or player2_value >= 21:
            return True
        return False

    def switch_player(self, current_player):
        if current_player == self.game.player1:
            return self.game.player2
        else:
            return self.game.player1

    def display_game_result(self):
        print("\nGame Over")
        print(self.game.check_winner())


# Test the game
player1 = Player("Player 1")
player2 = Player("Player 2")

game = TexasHoldemGame(player1, player2)
console = Console(game)
console.start_game()

from abc import ABC, abstractmethod
from enum import Enum
from collections import defaultdict

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
    JACK = '11'
    QUEEN = '12'
    KING = '13'
    ACE = '14'

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.deck = Deck()

    def __repr__(self):
        return f"{self.rank.value} of {self.suit.value}"

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, card):
        self.hand.append(card)

    def show_hand(self):
        for card in self.hand:
            print(card)


class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in Suit for rank in Rank]

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop()


class Game(ABC):
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    @abstractmethod
    def deal_initial_cards(self):
        pass

    @abstractmethod
    def check_winner(self):
        pass

class TwentyOnePointGame(Game):

    def deal_initial_cards(self):
        for _ in range(2):
            self.player1.draw(self.deck.draw())
            self.player2.draw(self.deck.draw())

    def check_winner(self):
        player1_value = self.player1.get_hand_value()
        player2_value = self.player2.get_hand_value()

        if player1_value > 21 and player2_value > 21:
            return "No one wins, both players busted!"
        elif player1_value > 21:
            return f"{self.player2.name} wins!"
        elif player2_value > 21:
            return f"{self.player1.name} wins!"
        elif player1_value == player2_value:
            return "It's a tie!"
        elif player1_value == 21:
            return f"{self.player1.name} wins with 21 points!"
        elif player2_value == 21:
            return f"{self.player2.name} wins with 21 points!"
        elif player1_value > player2_value:
            return f"{self.player1.name} wins!"
        else:
            return f"{self.player2.name} wins!"


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

class TexasHoldemGame(Game):

    def __init__(self, player1, player2):
        super().__init__(player1, player2)
        self.community_cards = []
        self.deck = Deck()

    def deal_initial_cards(self):
        private_cards1, private_cards2 = self.deck.deal_holdem()
        self.player1.draw(private_cards1)
        self.player2.draw(private_cards2)
        self.community_cards = self.deck.deal_holdem()[1]

    def _deal_helper(self):
        private_cards = [self.deck.draw() for _ in range(2)]
        community_cards = [self.deck.draw() for _ in range(5)]
        return private_cards, community_cards

    def deal_initial_cards(self):
        private_cards1, private_cards2 = self._deal_helper()
        self.player1.draw(private_cards1)
        self.player2.draw(private_cards2)
        self.community_cards = self.deck._deal_helper()[1]

    def get_hand_value(self, player):
        def is_straight(hand):
            sorted_hand = sorted(hand, key=lambda card: Rank.index(card.rank))
            for i in range(len(sorted_hand) - 4):
                if all(Rank.index(sorted_hand[i + j].rank) == Rank.index(sorted_hand[i].rank) + j for j in range(1, 5)):
                    return True
            return False

        def is_flush(hand):
            suit_count = {suit: 0 for suit in Suit}
            for card in hand:
                suit_count[card.suit] += 1
            return any(count >= 5 for count in suit_count.values())

        def count_ranks(hand):
            rank_count = {rank: 0 for rank in Rank}
            for card in hand:
                rank_count[card.rank] += 1
            return rank_count

        def is_four_of_a_kind(rank_count):
            return any(count == 4 for count in rank_count.values())

        def is_full_house(rank_count):
            return any(count == 3 for count in rank_count.values()) and any(count == 2 for count in rank_count.values())

        def is_three_of_a_kind(rank_count):
            return any(count == 3 for count in rank_count.values())

        def is_two_pair(rank_count):
            return sum(1 for count in rank_count.values() if count == 2) == 2

        def is_one_pair(rank_count):
            return any(count == 2 for count in rank_count.values())

        hand = player.hand + self.community_cards

        if is_straight(hand) and is_flush(hand):
            return 9  # Straight flush
        if is_four_of_a_kind(count_ranks(hand)):
            return 8  # Four of a kind
        if is_full_house(count_ranks(hand)):
            return 7  # Full house
        if is_flush(hand):
            return 6  # Flush
        if is_straight(hand):
            return 5  # Straight
        if is_three_of_a_kind(count_ranks(hand)):
            return 4  # Three of a kind
        if is_two_pair(count_ranks(hand)):
            return 3  # Two pair
        if is_one_pair(count_ranks(hand)):
            return 2  # One pair

        return 1  # High card


    def check_winner(self):
        player1_value = self.get_hand_value(self.player1)
        player2_value = self.get_hand_value(self.player2)

        if player1_value > player2_value:
            return f"{self.player1.name} wins with {self.get_hand_name(player1_value)}!"
        elif player2_value > player1_value:
            return f"{self.player2.name} wins with {self.get_hand_name(player2_value)}!"
        else:
            return "It's a tie!"

    def get_hand_name(self, value):
        hand_names = {
            9: "Straight flush",
            8: "Four of a kind",
            7: "Full house",
            6: "Flush",
            5: "Straight",
            4: "Three of a kind",
            3: "Two pair",
            2: "One pair",
            1: "High card"
        }
        return hand_names.get(value, "Unknown")


class Console:
    def __init__(self, game):
        self.game = game



    def start_game(self):
        self.game.deal_initial_cards()
        current_player = self.game.player1

        while True:
            self.display_game_state()
            self.handle_player_turn(current_player)
            if self.check_game_over():
                break

            current_player = self.switch_player(current_player)

        self.display_game_result()

    def switch_player(self, current_player):
        if current_player == self.game.player1:
            return self.game.player2
        else:
            return self.game.player1


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
        return self.game.player1.get_hand_value() >= 21 or self.game.player2.get_hand_value() >= 21

    def display_game_result(self):
        print("\nGame Over")
        print(self.game.check_winner())

player1 = Player("Player 1")
player2 = Player("Player 2")

game = TexasHoldemGame(player1, player2)
console = Console(game)
console.start_game()

from typing import Optional
from game_info import CARD_RANKS
from player import Player


class CLI():

    def input_length_error(self, *, length: int) -> None:
        print(
            f"Sorry! {length} is not a valid number of cards, you need 5 cards to play this game")
        print("Please Try Again!")

    def input_card_error(self, *, card: str) -> None:
        print(
            f"Sorry! {card} is not a valid card, please choose from one of the cards shown above")
        print("Please Try Again!")

    def input_wildcard_error(self) -> None:
        print("Sorry! Can't use '*' with four Aces!")
        self.input_same_card()

    def input_same_card(self) -> None:
        print(
            "Sorry! You need atleast one card of different kind, no five-of-a-kind allowed!")

    def welcome_text(self) -> None:
        print('\n', '\t', "======",
              "Hi! Welcome to Poker Game", "======", '\t', '\n')

    def get_player_name(self) -> str:

        player_name = input(
            "\n Hi there! Please input your name (default:Player):")

        if player_name.strip() == "":
            return "Player"

        return player_name.strip()

    def get_player_hand(self, *, player_name: str) -> str:

        print('\n', "Please choose from one of the values below", "\n",
              list(CARD_RANKS.keys()), '\n')
        user_cards = input(f"\n {player_name}'s hand:")

        return user_cards.strip()

    def print_draw(self, *, hand_type: str) -> None:
        print('\n', f"Looks like you both got {hand_type}s")
        print('\n', "Let's Call it a draw! You both are winners in our eyes :)")

    def print_winner(self, *, winner: Player) -> None:
        print(
            '\n', f"It was a close game, but '{winner.name}' wins this game with his '{winner.hand_type}' ")
        print('\n', "Let's give him a big hand ;)")

    def farewell_text(self) -> None:
        print('\n', '\t', "======",
                    "Bye! See you next time", "======", '\t', '\n')

from cli import CLI
from hand import Hand
from player import Player
from rules import Rules


class Poker:

    def __init__(self) -> None:
        self.cli = CLI()
        self.cli.welcome_text()

    def __get_player(self) -> Player:
        name = self.cli.get_player_name()

        while True:
            hand = self.cli.get_player_hand(
                player_name=name)
            player_hand = Hand(hand=hand)
            if player_hand.is_valid():
                break

        hand_type = player_hand.classify()
        player = Player(name=name, hand=hand, hand_type=hand_type)
        return player

    def play(self):
        player1 = self.__get_player()
        player2 = self.__get_player()
        rules = Rules(player1=player1, player2=player2)
        winner = rules.decide()
        if winner:
            self.cli.print_winner(winner=winner)
        else:
            self.cli.print_draw(hand_type=player1.hand_type)

        self.cli.farewell_text()

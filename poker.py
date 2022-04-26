from cli import CLI
from hand import Hand
from player import Player
from rules import Rules


class Poker:

    def __init__(self) -> None:
        self.cli = CLI()

    def __get_player(self) -> Player:
        name = self.cli.get_player_name()
        hand = self.cli.get_player_hand(
            player_name=name)
        player_hand = Hand(hand=hand)
        hand_type = player_hand.classify()
        player = Player(name=name, hand=hand, hand_type=hand_type)
        return player

    def play(self):
        player1 = self.__get_player()
        player2 = self.__get_player()
        rules = Rules(player1=player1, player2=player2)
        winner = rules.decide()
        self.cli.print_result(winner=winner)

from dataclasses import dataclass
from typing import List, Optional
from collections import Counter
from game_info import CARD_RANKS, HAND_RANKS
from player import Player


@dataclass
class Rules():

    player1: Player
    player2: Player

    """
        Helper Sorting Methods
    """

    def __sort_by_value(self, *, hand: str) -> List[int]:

        unique_cards = set(hand)

        for i in range(len(unique_cards)):
            unique_cards[i] = CARD_RANKS[unique_cards[i]]

        return sorted(unique_cards)

    def __sort_by_frequency(self, *, hand: str) -> List[int]:
        unique_cards = Counter(hand)
        sorted_unique_cards = unique_cards.most_common()
        ranks = []

        for card, _ in sorted_unique_cards:
            ranks.append(CARD_RANKS[card])

        return ranks

    def __sort_straight_ranks(self, *, hand: str) -> List[int]:
        if hand == "A2345":
            return [5, 4, 3, 2, 1]

        return self.__sort_by_value(hand=hand)

    """
        Helper Comparison Methods
    """

    def __compare_ranks(self, *, list1: List[int], list2: List[int]) -> Optional[Player]:
        if list1 > list2:
            return self.player1
        elif list2 < list1:
            return self.player2
        else:
            return None

    def __compare_by_priority(self) -> Optional[Player]:
        sorted_ranks1 = self.__sort_by_frequency(hand=self.player1.hand)
        sorted_ranks2 = self.__sort_by_frequency(hand=self.player2.hand)

        return self.__compare_ranks(list1=sorted_ranks1, list2=sorted_ranks2)

    def __compare_by_highest(self) -> Optional[Player]:
        sorted_ranks1 = self.__sort_by_value(hand=self.player1.hand)
        sorted_ranks2 = self.__sort_by_value(hand=self.player2.hand)

        return self.__compare_ranks(list1=sorted_ranks1, list2=sorted_ranks2)

    def __compare_straight(self) -> Optional[Player]:
        sorted_ranks1 = self.__sort_straight_ranks(hand=self.player1.hand)
        sorted_ranks2 = self.__sort_straight_ranks(hand=self.player2.hand)

        return self.__compare_ranks(list1=sorted_ranks1, list2=sorted_ranks2)

    """
        Hand Type Comparison Methods
    """

    def __compare_diff_types(self) -> Player:
        if HAND_RANKS[self.player1.hand_type] > HAND_RANKS[self.player2.hand_type]:
            return self.player1
        else:
            return self.player2

    def __compare_same_types(self, *, hand_type: str) -> Optional[Player]:
        if hand_type == "TWO_PAIR" or hand_type == "FULL_HOUSE":
            return self.__compare_by_priority()

        elif hand_type == "STRAIGHT":
            return self.__compare_straight()

        else:
            return self.__compare_by_highest()

    """
       Parent Public Method Enforcing Rules
    """

    def decide(self) -> Optional[Player]:
        if self.player1.hand_type != self.player2.hand_type:
            return self.__compare_diff_types()

        return self.__compare_same_types(hand_type=self.player1.hand_type)

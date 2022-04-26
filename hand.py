from dataclasses import dataclass, field
from collections import Counter
from operator import le
from typing import List, Optional
from cli import CLI
from game_info import CARD_RANKS


@dataclass
class Hand():

    hand: str
    max_hand_length: int = field(init=False, default=5)
    printer: CLI = field(init=False, repr=False, default_factory=CLI)

    def is_valid(self) -> bool:
        hand_length = len(self.hand)
        if hand_length != self.max_hand_length:
            self.printer.input_length_error(length=hand_length)
            return False

        for card in self.hand:
            if card not in CARD_RANKS:
                self.printer.input_card_error(card=card)
                return False

        return True

# Check Wildcard
    def __check_wildcard(self):

        if '*' not in self.hand:
            return False

        unique_cards = set(self.hand)
        if len(unique_cards) == 2 and unique_cards == {"A"}:
            return False

        if len(unique_cards) == self.max_hand_length:

    def __check_two_unique(self, *, freq: int) -> str:
        if freq == 4:
            return "FOUR_OF_KIND"
        elif freq == 3:
            return "FULL_HOUSE"

    def __check_three_unique(self, *, freq: int) -> str:
        if freq == 3:
            return "THREE_OF_KIND"
        elif freq == 2:
            return "TWO_PAIR"

    def __check_four_unique(self, *, freq: int) -> str:
        if freq == 2:
            return "PAIR"

    def __check_all_unique(self, *, card_frequency_list: List[tuple]) -> str:
        ranks = []
        for card, _ in card_frequency_list:
            ranks.append(CARD_RANKS[card])

        if max(ranks) - min(ranks) == 4:
            return "STRAIGHT"
        else:
            return "HIGH_CARD"

    def __detect_hand(self) -> str:
        card_counter = Counter(self.hand)
        unique_cards = len(card_counter)
        unique_card_frequency = card_counter.most_common()
        _, highest_freq = unique_card_frequency[0]

        hand_type = ""

        if unique_cards == 2:
            hand_type = self.__check_two_unique(freq=highest_freq)

        elif unique_cards == 3:
            hand_type = self.__check_three_unique(freq=highest_freq)

        elif unique_cards == 4:
            hand_type = self.__check_four_unique(freq=highest_freq)

        elif unique_cards == self.max_hand_length:
            hand_type = self.__check_all_unique(
                card_frequency_list=unique_card_frequency)

        return hand_type

    def classify(self) -> Optional[str]:
        hand_type = self.__detect_hand()
        return hand_type

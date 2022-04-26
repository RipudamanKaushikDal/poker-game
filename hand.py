from dataclasses import dataclass, field
from collections import Counter
from typing import List, Optional
from cli import CLI
from game_info import CARD_RANKS


@dataclass
class Hand():

    hand: str
    max_hand_length: int = field(init=False, default=5)
    printer: CLI = field(init=False, repr=False, default_factory=CLI)

    """
        Private Helper Mehods
    """

# Check Wildcard
    def __tackle_wildcard(self) -> None:
        if '*' not in self.hand:
            return

        hand_list = self.hand.split()
        wild_card_index = hand_list.index('*')
        unique_ranks = {CARD_RANKS[card] for card in self.hand}

        if len(unique_ranks) != self.max_hand_length:
            hand_list[wild_card_index] = 'A'
        else:
            unique_ranks.remove(1)
            wild_card_value = self.__get_wildcard_for_straights(unique_ranks=unique_ranks)
            wild_card = self.__card_reverse_lookup(card_rank=wild_card_value)
            hand_list[wild_card_index] = wild_card

        self.hand = "".join(hand_list)



    def __card_reverse_lookup(self,*,card_rank:int) -> str:
        for card, rank in CARD_RANKS.items():
            if card_rank == rank:
                return card

            

    def __get_wildcard_for_straights(self,*,unique_ranks:set) -> int:
        max_rank = max(unique_ranks)  
        min_rank = min(unique_ranks)

        if max_rank - min_rank == 4:
            range_set = {rank for rank in range(min_rank,max_rank+1)}
            wild_value = list(range_set.difference(unique_ranks))[0]
            return wild_value
    
        
        elif max_rank - min_rank == 3 and max_rank == CARD_RANKS['A']:
            return min_rank - 1
    

        elif max_rank - min_rank == 3:
            return max_rank + 1

        else:
            return CARD_RANKS['A']



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


    """
        Public Main Methods
    """

    def is_valid(self) -> bool:
        hand_length = len(self.hand)
        if hand_length != self.max_hand_length:
            self.printer.input_length_error(length=hand_length)
            return False

        card_count = Counter(self.hand)

        for card in self.hand:

            if card == '*' and card_count['A'] == 4:
                self.printer.input_wildcard_error()
                return False

            elif card not in CARD_RANKS:
                self.printer.input_card_error(card=card)
                return False

        return True

    def classify(self) -> Optional[str]:
        self.__tackle_wildcard()
        hand_type = self.__detect_hand()
        return hand_type

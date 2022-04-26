from typing import Dict

CARD_RANKS: Dict[str, int] = {'*':1,'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
                              '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

HAND_RANKS: Dict[str, int] = {
    "HIGH_CARD": 1,
    "PAIR": 2,
    "TWO_PAIR": 3,
    "THREE_OF_KIND": 4,
    "STRAIGHT": 5,
    "FULL_HOUSE": 6,
    "FOUR_OF_KIND": 7,
}

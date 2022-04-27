import unittest
from hand import Hand
from player import Player
from rules import Rules


class TestHandInput(unittest.TestCase):

    def setUp(self) -> None:
        self.valid_hands = ["AAAKT", "2345*", "KK*KK", "A267J", "44KQA"]
        self.invalid_hands = ["AA*AA", "ATHFG", "KKQQTT", "      ", "KKKKK"]

    def test_invalid_hands(self) -> None:
        for hand_input in self.invalid_hands:
            with self.subTest(hand_input):
                player_hand = Hand(hand=hand_input)
                self.assertFalse(player_hand.is_valid())

    def test_valid_hands(self) -> None:
        for hand_input in self.valid_hands:
            with self.subTest(hand_input):
                player_hand = Hand(hand=hand_input)
                self.assertTrue(player_hand.is_valid())


class ClassifyWildCards(unittest.TestCase):

    def test_classify_as_ace(self) -> None:
        player_hand = Hand(hand='KKKK*')
        self.assertEqual(player_hand.classify_wildcard(), 'KKKKA')

    def test_classify_as_straight_max(self) -> None:
        player_hand = Hand(hand='3456*')
        self.assertEqual(player_hand.classify_wildcard(), '34567')

    def test_classify_as_straight_min(self) -> None:
        player_hand = Hand(hand='*JQKA')
        self.assertEqual(player_hand.classify_wildcard(), 'TJQKA')

    def test_classify_as_straight_between(self) -> None:
        player_hand = Hand(hand='5*789')
        self.assertEqual(player_hand.classify_wildcard(), '56789')

    def test_classify_as_none(self) -> None:
        player_hand = Hand(hand='KKQQ4')
        self.assertIsNone(player_hand.classify_wildcard())


class CompareHands(unittest.TestCase):

    def setUp(self) -> None:
        self.player1 = "tester1"
        self.player2 = "tester2"


if __name__ == '__main__':
    unittest.main(verbosity=2)

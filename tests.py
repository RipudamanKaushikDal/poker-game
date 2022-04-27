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
        self.player1_name = "tester1"
        self.player2_name = "tester2"

    def test_toak_vs_fh(self) -> None:
        hand1, hand2 = "AAAKT", "22233"
        hand1_type, hand2_type = "THREE_OF_KIND", "FULL_HOUSE"
        player1 = Player(name=self.player1_name,
                         hand=hand1, hand_type=hand1_type)
        player2 = Player(name=self.player2_name,
                         hand=hand2, hand_type=hand2_type)
        rules = Rules(player1=player1, player2=player2)
        winner = rules.decide()
        self.assertEqual(winner, player2)

    def test_straights(self) -> None:
        hand1, hand2 = "23456", "A2345"
        hand1_type = hand2_type = "STRAIGHT"
        player1 = Player(name=self.player1_name,
                         hand=hand1, hand_type=hand1_type)
        player2 = Player(name=self.player2_name,
                         hand=hand2, hand_type=hand2_type)
        rules = Rules(player1=player1, player2=player2)
        winner = rules.decide()
        self.assertEqual(winner, player1)

    def test_two_pairs(self) -> None:
        hand1, hand2 = "AA993", "AA88K"
        hand1_type = hand2_type = "TWO_PAIR"
        player1 = Player(name=self.player1_name,
                         hand=hand1, hand_type=hand1_type)
        player2 = Player(name=self.player2_name,
                         hand=hand2, hand_type=hand2_type)
        rules = Rules(player1=player1, player2=player2)
        winner = rules.decide()
        self.assertEqual(winner, player1)

    def test_full_houses(self) -> None:
        hand1, hand2 = "AAA22", "KKKQQ"
        hand1_type = hand2_type = "FULL_HOUSE"
        player1 = Player(name=self.player1_name,
                         hand=hand1, hand_type=hand1_type)
        player2 = Player(name=self.player2_name,
                         hand=hand2, hand_type=hand2_type)
        rules = Rules(player1=player1, player2=player2)
        winner = rules.decide()
        self.assertEqual(winner, player1)

    def test_value_comparison(self) -> None:
        hand1, hand2 = "AA234", "AA235"
        hand1_type = hand2_type = "PAIR"
        player1 = Player(name=self.player1_name,
                         hand=hand1, hand_type=hand1_type)
        player2 = Player(name=self.player2_name,
                         hand=hand2, hand_type=hand2_type)
        rules = Rules(player1=player1, player2=player2)
        winner = rules.decide()
        self.assertEqual(winner, player2)

    def test_draw(self) -> None:
        hand1, hand2 = "KKKKA", "KKKKA"
        hand1_type = hand2_type = "FOUR_OF_KIND"
        player1 = Player(name=self.player1_name,
                         hand=hand1, hand_type=hand1_type)
        player2 = Player(name=self.player2_name,
                         hand=hand2, hand_type=hand2_type)
        rules = Rules(player1=player1, player2=player2)
        winner = rules.decide()
        self.assertIsNone(winner)


if __name__ == '__main__':
    unittest.main(verbosity=1)

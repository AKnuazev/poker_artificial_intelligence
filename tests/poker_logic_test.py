import unittest
from source.poker_items import Card, Deck, Hand, values, suits


# values = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# suits = ["♠", "♣", "♥", "♦"]  # "spades", " clubs", "hearts", "diamonds"

class TestItems(unittest.TestCase):
    def test_card(self):
        card1 = Card(values[0], suits[0])
        self.assertEqual(card1.value, values[0])
        self.assertEqual(card1.suit, suits[0])
        self.assertEqual(str(card1), "2♠")

        card2 = Card(values[12], suits[1])
        self.assertEqual(card1 == card2, False)
        self.assertEqual(card1 != card2, True)
        self.assertEqual(card1 < card2, True)
        self.assertEqual(card1 <= card2, True)
        self.assertEqual(card1 > card2, False)
        self.assertEqual(card1 >= card2, False)

    def test_deck(self):
        deck = Deck()
        last_card = deck.deck[len(deck.deck) - 1]
        self.assertEqual(deck.get_card(), last_card)

        last_card = deck.deck[len(deck.deck) - 1]
        deck.shuffle()
        last_card_after_shuffle = deck.deck[len(deck.deck) - 1]
        self.assertNotEqual(last_card, last_card_after_shuffle)

    def test_hand(self):
        hand = Hand()
        board = Hand()
        # board.add_card(Card(0, '0'))
        deck = Deck()

        # for _ in range(5):
        #     board.add_card(deck.get_card())
        # for _ in range(2):
        #     hand.add_card(deck.get_card())
        #
        # summ_hand = hand + board
        # self.assertEqual(len(summ_hand.cards), len(hand.cards) + len(board.cards))

        ace_hearts = Card(14, '♥')
        two_spades = Card(2, '♠')

        pair_comb = Hand()
        for _ in range(2):
            pair_comb.add_card(two_spades)

        two_pairs_comb = Hand()
        for _ in range(2):
            two_pairs_comb.add_card(two_spades)
            two_pairs_comb.add_card(ace_hearts)

        three_comb = Hand()
        for _ in range(3):
            three_comb.add_card(two_spades)

        straight_comb = Hand()
        for i in range(5):
            straight_comb.add_card(Card(i + 1, suits[i % 4]))

        flash_comb = Hand()
        for i in range(5):
            flash_comb.add_card(Card(i * 2 + 2, suits[0]))

        full_house_comb = Hand()
        for _ in range(3):
            full_house_comb.add_card(ace_hearts)
        for _ in range(2):
            full_house_comb.add_card(two_spades)

        four_comb = Hand()
        for _ in range(4):
            four_comb.add_card(two_spades)

        straight_flash_comb = Hand()
        for i in range(5):
            straight_flash_comb.add_card(Card(i + 2, suits[0]))

        royal_flash_comb = Hand()
        for i in range(5):
            royal_flash_comb.add_card(Card(14 - i, suits[0]))

        self.assertEqual(pair_comb.check_combination(board), 14 + 1, "Expected pair")
        self.assertEqual(two_pairs_comb.check_combination(board), 14 + 2, "Expected two pairs")
        self.assertEqual(three_comb.check_combination(board), 14 + 3, "Expected three of a kind")
        self.assertEqual(straight_comb.check_combination(board), 14 + 4, "Expected straight")
        self.assertEqual(flash_comb.check_combination(board), 14 + 5, "Expected flash")
        self.assertEqual(full_house_comb.check_combination(board), 14 + 6, "Expected full house")
        self.assertEqual(four_comb.check_combination(board), 14 + 7, "Expected four of a kind")
        self.assertEqual(straight_flash_comb.check_combination(board), 14 + 8, "Expected straight flash")
        self.assertEqual(royal_flash_comb.check_combination(board), 14 + 9, "Expected royal flash")

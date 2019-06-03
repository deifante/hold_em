import pytest
from typing import List, Dict

from hold_em.card import Card
from hold_em.player import Player
from hold_em.hand import Hand, make_histogram


@pytest.fixture()
def test_hands() -> Dict[str, List[Card]]:
    return {
        'straight flush': [Card('A', 'D'), Card('K', 'D'), Card('Q', 'D'), Card('J', 'D'), Card('T', 'D')],
        'four of a kind': [Card('7', 'D'), Card('7', 'H'), Card('7', 'C'), Card('7', 'S'), Card('T', 'D')],
        'full house': [Card('5', 'D'), Card('5', 'H'), Card('5', 'C'), Card('2', 'S'), Card('2', 'D')],
        'flush': [Card('2', 'D'), Card('4', 'D'), Card('6', 'D'), Card('8', 'D'), Card('J', 'D')],
        'straight': [Card('9', 'C'), Card('K', 'H'), Card('Q', 'D'), Card('J', 'S'), Card('T', 'D')],
        'wheel': [Card('A', 'C'), Card('2', 'H'), Card('3', 'D'), Card('4', 'S'), Card('5', 'D')],
        'three of a kind': [Card('6', 'D'), Card('6', 'H'), Card('6', 'C'), Card('J', 'S'), Card('T', 'D')],
        'two pair': [Card('T', 'D'), Card('T', 'H'), Card('3', 'C'), Card('3', 'S'), Card('Q', 'D')],
        'pair': [Card('7', 'D'), Card('2', 'H'), Card('3', 'C'), Card('3', 'S'), Card('4', 'D')],
        'high card': [Card('7', 'D'), Card('Q', 'H'), Card('4', 'C'), Card('3', 'S'), Card('T', 'D')]
    }

class TestHand:
    """Tests the Hand class"""

    def test_constructor(self):
        """Tests that we can construct a Hand object."""
        hand = Hand([Card('A', 'D')])
        assert isinstance(hand, Hand)

    def test_str(self, test_hands: Dict[str, List[Card]]):
        """Tests that we can make a human friendly representation of the hand.
        """
        hand = Hand(test_hands['straight flush'])
        expected = 'Straight flush. Kicker: Ace. High Card in Hand: Ace. (Ace of Diamonds, King of Diamonds, Queen of Diamonds, Jack of Diamonds, Ten of Diamonds).'
        assert expected == str(hand)

    def test_card_ranking(self, test_hands: Dict[str, List[Card]]):
        hand = Hand(test_hands['straight flush'])
        assert Hand.hand_ranks['straight flush'] == hand.get_rank()
        assert 14 == hand.get_high_card_in_hand_rank()
        assert 14 == hand.get_high_kicker_card_rank()
        
        hand = Hand(test_hands['four of a kind'])
        assert Hand.hand_ranks['four of a kind'] == hand.get_rank()
        assert 7 == hand.get_high_card_in_hand_rank()
        assert 10 == hand.get_high_kicker_card_rank()

        hand = Hand(test_hands['full house'])
        assert Hand.hand_ranks['full house'] == hand.get_rank()
        assert 5 == hand.get_high_card_in_hand_rank()
        assert 5 == hand.get_high_kicker_card_rank()

        hand = Hand(test_hands['flush'])
        assert Hand.hand_ranks['flush'] == hand.get_rank()
        assert 11 == hand.get_high_card_in_hand_rank()
        assert 11 == hand.get_high_kicker_card_rank()

        hand = Hand(test_hands['straight'])
        assert Hand.hand_ranks['straight'] == hand.get_rank()
        assert 13 == hand.get_high_card_in_hand_rank()
        assert 13 == hand.get_high_kicker_card_rank()

        hand = Hand(test_hands['wheel'])
        assert Hand.hand_ranks['straight'] == hand.get_rank()
        assert 14 == hand.get_high_card_in_hand_rank()
        assert 14 == hand.get_high_kicker_card_rank()

        hand = Hand(test_hands['three of a kind'])
        assert Hand.hand_ranks['three of a kind'] == hand.get_rank()
        assert 6 == hand.get_high_card_in_hand_rank()
        assert 11 == hand.get_high_kicker_card_rank()

        hand = Hand(test_hands['two pair'])
        assert Hand.hand_ranks['two pair'] == hand.get_rank()
        assert 10 == hand.get_high_card_in_hand_rank()
        assert 12 == hand.get_high_kicker_card_rank()

        hand = Hand(test_hands['pair'])
        assert Hand.hand_ranks['pair'] == hand.get_rank()
        assert 3 == hand.get_high_card_in_hand_rank()
        assert 7 == hand.get_high_kicker_card_rank()
        
        hand = Hand(test_hands['high card'])
        assert Hand.hand_ranks['high card'] == hand.get_rank()
        assert 12 == hand.get_high_card_in_hand_rank()
        assert 12 == hand.get_high_kicker_card_rank()
        
def test_make_histogram():
    """Test creating a Card rank based histogram from a list of Cards"""
    hand = [
        Card('Q', 'D'),
        Card('2', 'C'),
        Card('T', 'D'),
        Card('Q', 'S'),
        Card('A', 'S'),
        Card('Q', 'H'),
        Card('3', 'D'),
        Card('Q', 'C'),
        Card('2', 'H')
    ]
    expected_histogram = {
        14:1,
        12:4,
        10:1,
        3:1,
        2:2,
    }
    assert expected_histogram == make_histogram(hand)

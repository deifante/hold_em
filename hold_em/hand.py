from typing import List
from operator import methodcaller

from hold_em.card import Card, FriendlyCard

def make_histogram(hand: List[Card]) -> List[int]:
    """Create a histogram based on card rank
    :param hand: The list of cards that we will create the histogram from.
    :type hand: List[Card]
    :returns: A histogram of the cards based on their rank. Sorted with the
        highest rank first.
    :rtype: List[int]
    """
    histogram = {}
    for card in hand:
        if card.get_rank() in histogram:
            histogram[card.get_rank()] += 1
        else:
            histogram[card.get_rank()] = 1

    sorted_histogram = {k: histogram[k] for k in sorted(histogram, reverse = True)}
    return sorted_histogram


class Hand:
    """A hand of cards belonging to a Player"""

    hand_ranks = {
        'high card': 1,
        'pair': 2,
        'two pair': 3,
        'three of a kind': 4,
        'straight': 5,
        'flush': 6,
        'full house': 7,
        'four of a kind': 8,
        'straight flush': 9
    }

    card_rank_names = {
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'jack',
        12: 'queen',
        13: 'king',
        14: 'ace'
    }

    def __init__(self, cards: List[Card]):
        """Creates a hand of cards.
        :param cards: The cards that go into this hand.
        :type cards: List[Card]
        """
        self.cards = cards
        self.hand_type_rank = None
        self.high_card_in_hand_rank = None
        self.high_card_in_kicker_rank = None

    def __eq__(self, other) -> bool:
        """Equals operator overload"""
        if isinstance(other, Hand):
            return self.cards == other.cards
        return NotImplemented

    def __str__(self) -> str:
        """Create a string representation of this hand."""
        card_string = ''
        if self.hand_type_rank is None:
            self.make_rank()
        sorted_cards = sorted(self.cards, key=methodcaller('get_rank'), reverse=True)
        for card in sorted_cards[:-1]:
            card_string += f'{str(card)}, '
        card_string += f'{str(sorted_cards[-1])}'
        if not hasattr(Hand, 'reverse_ranks'):
            Hand.reverse_ranks = {y:x for x,y in Hand.hand_ranks.items()}
        return f"{Hand.reverse_ranks[self.hand_type_rank].capitalize()}. Kicker: {Hand.card_rank_names[self.high_card_in_kicker_rank].capitalize()}. High Card in Hand: {Hand.card_rank_names[self.high_card_in_hand_rank].capitalize()}. ({card_string})."
    
    def get_rank(self) -> int:
        """Gets the hand rank of the hand."""
        if self.hand_type_rank is None:
            self.make_rank()
        return self.hand_type_rank
    
    def get_high_card_in_hand_rank(self) -> int:
        """Gets the rank of the highest in hand card."""
        if self.hand_type_rank is None:
            self.make_rank()
        return self.high_card_in_hand_rank

    def get_high_kicker_card_rank(self) -> int:
        """Gets the rank of the highest card the player holds, including kickers.
        """
        if self.hand_type_rank is None:
            self.make_rank()
        return self.high_card_in_kicker_rank

    def make_rank(self):
        """Determine the rank of the hand"""
        is_flush = False
        is_straight = False
        rank_sorted_hand = sorted(self.cards, key=methodcaller('get_rank'))
        self.high_card_in_kicker_rank = rank_sorted_hand[-1].get_rank()
        card_hist = make_histogram(self.cards)
        histogram_values = card_hist.values()
        histogram_items = card_hist.items()

        # determine if we have a flush
        if len(set([card.suit for card in self.cards])) == 1:
            is_flush = True
        
        # determine if we have a straight
        max_count = sorted(histogram_values)[-1]
        if rank_sorted_hand[-1].get_rank() - rank_sorted_hand[0].get_rank() == 4 and max_count == 1:
            is_straight = True

        # check for a straight with the ace as 1
        if rank_sorted_hand[-1].get_rank() == 14 and rank_sorted_hand[-2].get_rank() == 5 and max_count == 1:
            is_straight = True

        if is_flush and is_straight:
            self.hand_type_rank = Hand.hand_ranks['straight flush']
            self.high_card_in_hand_rank = self.high_card_in_kicker_rank
            return
        
        if 4 in histogram_values:
            self.hand_type_rank = Hand.hand_ranks['four of a kind']
            for rank, rank_count in histogram_items:
                if rank_count == 4:
                    self.high_card_in_hand_rank = rank
                    break
            return
        
        if 3 in histogram_values and 2 in histogram_values:
            self.hand_type_rank = Hand.hand_ranks['full house']
            self.high_card_in_hand_rank = self.high_card_in_kicker_rank
            return

        if is_flush:
            self.hand_type_rank = Hand.hand_ranks['flush']
            self.high_card_in_hand_rank = self.high_card_in_kicker_rank
            return
        
        if is_straight:
            self.hand_type_rank = Hand.hand_ranks['straight']
            self.high_card_in_hand_rank = self.high_card_in_kicker_rank
            return

        if 3 in histogram_values:
            self.hand_type_rank = self.hand_ranks['three of a kind']
            for rank, rank_count in histogram_items:
                if rank_count == 3:
                    self.high_card_in_hand_rank = rank
                    break
            return
            
        if 2 == list(histogram_values).count(2):
            self.hand_type_rank = Hand.hand_ranks['two pair']
            self.high_card_in_hand_rank = 0
            for rank, rank_count in histogram_items:
                if rank_count == 2 and rank > self.high_card_in_hand_rank:
                    self.high_card_in_hand_rank = rank
            return

        if 2 in histogram_values:
            self.hand_type_rank = Hand.hand_ranks['pair']
            for rank, rank_count in histogram_items:
                if rank_count == 2:
                    self.high_card_in_hand_rank = rank
                    break
            return

        self.hand_type_rank = Hand.hand_ranks['high card']
        self.high_card_in_hand_rank = self.high_card_in_kicker_rank
        return
from hold_em.card import Card, CardParser
from hold_em.player import Player, PlayerRank, make_histogram

import pytest

@pytest.fixture()
def karen_player() -> Player:
    hole_cards = [
            Card('A', 'D'),
            Card('Q', 'C')
        ]
    community_cards = [
        Card('2', 'S'),
        Card('4', 'D'),
        Card('5', 'H'),
        Card('T', 'C'),
        Card('8', 'D')
    ]
    player = Player('Karen', hole_cards, community_cards)
    return player

class TestPlayer:
    """Tests the Player class"""

    def test_constructor(self, karen_player: Player):
        """Test the creation of a player"""
        assert isinstance(karen_player, Player)

    def test_get_hole_cards(self, karen_player: Player):
        """Test getting hole cards from a player"""
        hole_cards = [
            Card('A', 'D'),
            Card('Q', 'C')
        ]
        assert hole_cards == karen_player.get_hole_cards()

    def test_get_community_cards(self, karen_player: Player):
        """Tests getting the community cards from a player"""
        community_cards = [
            Card('2', 'S'),
            Card('4', 'D'),
            Card('5', 'H'),
            Card('T', 'C'),
            Card('8', 'D')
        ]
        assert community_cards == karen_player.get_community_cards()

class TestPlayerRank:
    """Tests the ranking of a player"""

    def test_constructor(self, karen_player: Player):
        """Test the creation of a PlayerRank object"""
        karen_rank = PlayerRank(karen_player)
        assert isinstance(karen_rank, PlayerRank)

    def test_make_five(self, karen_player: Player):
        """Test creating all the combinations of hands a player can have"""
        karen_rank = PlayerRank(karen_player)
        karen_hands = karen_rank.make_five()
        # Hole Cards
        ad = Card('A', 'D')
        qc = Card('Q', 'C')
        # Community Cards
        ts = Card('2', 'S')
        fd = Card('4', 'D')
        fh = Card('5', 'H')
        tc = Card('T', 'C')
        ed = Card('8', 'D')

        expected_hands = [
            [ad, qc, ts, fd, fh],
            [ad, qc, ts, fd, tc],
            [ad, qc, ts, fd, ed],
            [ad, qc, ts, fh, tc],
            [ad, qc, ts, fh, ed],
            [ad, qc, ts, tc, ed],
            [ad, qc, fd, fh, tc],
            [ad, qc, fd, fh, ed],
            [ad, qc, fd, tc, ed],
            [ad, qc, fh, tc, ed],
        ]
        assert expected_hands == karen_hands

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

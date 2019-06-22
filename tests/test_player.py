import pytest

from hold_em.card import Card, CardParser
from hold_em.hand import Hand
from hold_em.player import Player


@pytest.fixture()
def karen_player() -> Player:
    hole_cards = [Card("A", "D"), Card("Q", "C")]
    community_cards = [
        Card("2", "S"),
        Card("4", "D"),
        Card("5", "H"),
        Card("T", "C"),
        Card("8", "D"),
    ]
    player = Player("Karen", hole_cards, community_cards)
    return player


@pytest.fixture()
def tracey_player() -> Player:
    hole_cards = [Card("A", "D"), Card("K", "C")]
    community_cards = [
        Card("Q", "S"),
        Card("J", "D"),
        Card("5", "H"),
        Card("T", "C"),
        Card("8", "D"),
    ]
    player = Player("Tracey", hole_cards, community_cards)
    return player


@pytest.fixture()
def community_player() -> Player:
    hole_cards = [Card("2", "D"), Card("3", "H")]
    community_cards = [
        Card("A", "H"),
        Card("A", "D"),
        Card("K", "H"),
        Card("K", "S"),
        Card("K", "C"),
    ]
    player = Player("Community", hole_cards, community_cards)
    return player


class TestPlayer:
    """Tests the Player class"""

    def test_constructor(self, karen_player: Player):
        """Test the creation of a player"""
        assert isinstance(karen_player, Player)

    def test_constructor_too_many_community_cards(self):
        """Tests that an exception is thrown when an incorrect number of
        community cards are passed to the constructor.
        """
        hole_cards = [Card("7", "D"), Card("3", "C")]
        community_cards = [
            Card("Q", "S"),
            Card("J", "D"),
            Card("5", "H"),
            Card("T", "C"),
            Card("8", "D"),
            Card("2", "D"),
            Card("4", "D"),
        ]
        with pytest.raises(ValueError):
            Player("Becky", hole_cards, community_cards)

    def test_get_hole_cards(self, karen_player: Player):
        """Test getting hole cards from a player"""
        hole_cards = [Card("A", "D"), Card("Q", "C")]
        assert hole_cards == karen_player.get_hole_cards()

    def test_get_community_cards(self, karen_player: Player):
        """Tests getting the community cards from a player"""
        community_cards = [
            Card("2", "S"),
            Card("4", "D"),
            Card("5", "H"),
            Card("T", "C"),
            Card("8", "D"),
        ]
        assert community_cards == karen_player.get_community_cards()

    def test_make_five(self, karen_player: Player):
        """Test creating all the combinations of hands a player can have"""
        karen_hands = karen_player.make_five()

        # Hole Cards
        ad = Card("A", "D")
        qc = Card("Q", "C")
        # Community Cards
        ts = Card("2", "S")
        fd = Card("4", "D")
        fh = Card("5", "H")
        tc = Card("T", "C")
        ed = Card("8", "D")

        expected_hands = [
            [ts, fd, fh, tc, ed],
            [ts, fd, fh, tc, ad],
            [ts, fd, fh, tc, qc],
            [ts, fd, fh, ed, ad],
            [ts, fd, fh, ed, qc],
            [ts, fd, fh, ad, qc],
            [ts, fd, tc, ed, ad],
            [ts, fd, tc, ed, qc],
            [ts, fd, tc, ad, qc],
            [ts, fd, ed, ad, qc],
            [ts, fh, tc, ed, ad],
            [ts, fh, tc, ed, qc],
            [ts, fh, tc, ad, qc],
            [ts, fh, ed, ad, qc],
            [ts, tc, ed, ad, qc],
            [fd, fh, tc, ed, ad],
            [fd, fh, tc, ed, qc],
            [fd, fh, tc, ad, qc],
            [fd, fh, ed, ad, qc],
            [fd, tc, ed, ad, qc],
            [fh, tc, ed, ad, qc],
        ]

        assert expected_hands == karen_hands

    def test_get_best_hand(self, tracey_player: Player):
        """Test getting the best hand a player can play"""
        expected_hand = Hand(
            [
                Card("Q", "S"),
                Card("J", "D"),
                Card("T", "C"),
                Card("A", "D"),
                Card("K", "C"),
            ]
        )
        tracey_best_hand = tracey_player.get_best_hand()
        assert expected_hand == tracey_best_hand

    def test_get_best_hand_community_cards(self, community_player: Player):
        """Test getting the best hand when the best hand is already in the
        community cards.
        """
        expected_hand = Hand(
            [
                Card("A", "H"),
                Card("A", "D"),
                Card("K", "H"),
                Card("K", "S"),
                Card("K", "C"),
            ]
        )
        community_player_best_hand = community_player.get_best_hand()
        assert expected_hand == community_player_best_hand

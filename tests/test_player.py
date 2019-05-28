from hold_em.card import Card, CardParser
from hold_em.player import Player

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
        




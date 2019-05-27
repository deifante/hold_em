from hold_em.card import Card, CardParser
from hold_em.player import Player

class TestPlayer:
    """Tests the Player class"""

    def test_constructor(self):
        """Test the creation of a player"""
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
        assert isinstance(player, Player)
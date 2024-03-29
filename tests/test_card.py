import pytest

from hold_em.card import Card, CardParser
from hold_em.player import Player


class TestCardParser:
    """Tests the ability to parse cards"""

    def test_parse(self):
        """Card parsing unit test"""
        card_parser = CardParser()
        card = Card("A", "D")
        parsed_card = card_parser.parse("AD")
        assert card == parsed_card

    def test_card_parsing(self):
        """Card parsing integration test"""
        expected_output = "Jack of Spades"
        card_parser = CardParser()
        parsed_card = card_parser.parse("JS")
        assert expected_output == str(parsed_card)

    def test_get_rank(self):
        """Test getting the card rank"""
        card = Card("Q", "C")
        assert 12 == card.get_rank()

    def test_parse_invalid_card(self):
        """Test parsing an invalid card"""
        card_parser = CardParser()
        with pytest.raises(KeyError):
            card_parser.parse("SH")

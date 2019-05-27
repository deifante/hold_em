from dataclasses import dataclass, field

class FriendlyCard:
    """Assists in creating human friendly output for Card objects"""
    faces = {
        '2': 'Two',
        '3': 'Three',
        '4': 'Four',
        '5': 'Five',
        '6': 'Six',
        '7': 'Seven',
        '8': 'Eight',
        '9': 'Nine',
        'T': 'Ten',
        'J': 'Jack',
        'Q': 'Queen',
        'K': 'King',
        'A': 'Ace',
    }
    suits = {
        'H': 'Hearts',
        'S': 'Spades',
        'D': 'Diamonds',
        'C': 'Clubs'
    }

@dataclass(order=True)
class Card:
    """A class representing a playing card"""
    face: chr
    suit: chr

    def __repr__(self):
        """Produce debug output for a card"""
        return f"{self.face}, {self.suit}"

    def __str__(self):
        """Produce human friendly output for a card"""
        return f"{FriendlyCard.faces[self.face]} of {FriendlyCard.suits[self.suit]}"

class CardParser:
    """Creates cards from text input"""

    def parse(self, card: str) -> Card:
        """Parse a 2 letter raw card into a Card object
        :param card:  A 2 letter string representing a playing card.
        :type card: str
        :returns: Card
        """
        return Card(card[0], card[1])

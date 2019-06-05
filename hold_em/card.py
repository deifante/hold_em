from dataclasses import dataclass, field


class FriendlyCard:
    """Assists in creating human friendly output for Card objects"""

    faces = {
        "2": "Two",
        "3": "Three",
        "4": "Four",
        "5": "Five",
        "6": "Six",
        "7": "Seven",
        "8": "Eight",
        "9": "Nine",
        "T": "Ten",
        "J": "Jack",
        "Q": "Queen",
        "K": "King",
        "A": "Ace",
    }
    suits = {"H": "Hearts", "S": "Spades", "D": "Diamonds", "C": "Clubs"}


@dataclass(order=True)
class Card:
    """A class representing a playing card"""

    face: chr
    suit: chr

    ranks = {
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "T": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
        "A": 14,
    }

    def __repr__(self) -> str:
        """Produce debug output for a card.
        :returns: Debug output for a card.
        :rtype: str
        """
        return f"{self.face}, {self.suit}"

    def __str__(self) -> str:
        """Produce human friendly output for a card.
        :returns: Human friendly output for a card. Describes the face and
            suit. eg. Ace of Spades.
        :rtype: str
        """
        return f"{FriendlyCard.faces[self.face]} of {FriendlyCard.suits[self.suit]}"

    def get_rank(self) -> int:
        """Get the card rank.
        :returns: The rank of the card J == 11, Q == 12 ... up to A == 14.
        :rtype: int
        """
        return Card.ranks[self.face]


class CardParser:
    """Creates cards from text input."""

    def parse(self, card: str) -> Card:
        """Parse a 2 letter raw card into a Card object
        :param card:  A 2 letter string representing a playing card.
        :type card: str
        :returns: A single Card object.
        :rtype: Card
        """
        if card[0] not in FriendlyCard.faces:
            raise KeyError(card[0])
        if card[1] not in FriendlyCard.suits:
            raise KeyError(card[1])
        return Card(card[0], card[1])

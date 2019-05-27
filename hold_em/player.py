from typing import List

from . import card

class Player:
    """Represents a player of texas hold em"""

    def __init__(self, name: str, hole_cards: List[card.Card], community_cards: List[card.Card]):
        """Creates a new Player with 2 hole cards
        :param name: The name of the player
        :type name: str
        :param hole_cards: The 2 cards dealt to only this player
        :type hole_cards: List[Card]
        :raises: ValueError
        """
        if len(hole_cards) != 2:
            raise ValueError(f'Must have 2 and only 2 hole cards when creating a Player. {len(hole_cards)} hole cards passed.')
        self.hole_cards = hole_cards

        if len(community_cards) != 5:
            raise ValueError(f'Must have 5 and only 5 community cards when creating a Player. {len(community_cards)} community cards passed.')
        self.community_cards = community_cards            
        self.name = name

    def __str__(self):
        """Produces human friendly output for a player"""
        community_cards = ''
        for card in self.community_cards[:-1]:
            community_cards += f" the {str(card)},"
        community_cards = f"{community_cards[:-2]} and the {str(self.community_cards[-1])}"
        community_cards = community_cards.strip()
        return f"{self.name} holds the {self.hole_cards[0]} and the {self.hole_cards[1]} hole cards and holds {community_cards} as community cards."

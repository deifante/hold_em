from typing import List
from itertools import combinations

from hold_em.card import Card

class Player:
    """Represents a player of texas hold em"""

    def __init__(self, name: str, hole_cards: List[Card], community_cards: List[Card]):
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

    def get_hole_cards(self) -> List[Card]:
        """Get the 2 hole cards for this player"""
        return self.hole_cards

    def get_community_cards(self) -> List[Card]:
        """Get the community cards for this player"""
        return self.community_cards


class PlayerRank:
    """Gets the rank of a player's hand"""

    def __init__(self, player: Player):
        """Creates a PlayerRank object for ranking the player hand
        :param player: Player the player whos hand will be ranked
        :type player: Player
        """
        self.player = player

    def make_five(self) -> List[List[Card]]:
        """Makes all the 5 card hands this player can have
        :returns: List[List[card.Card]] A list of possible hands."""
        five_card_combinations = []
        hole_cards = self.player.get_hole_cards()
        community_cards = self.player.get_community_cards()
        for comb in combinations(community_cards, 3):
            five_card_combinations.append(hole_cards + list(comb))
        return five_card_combinations

    def rank(self):
        hands = self.make_five()
        for hand in hands:
            card_hist = {}
            for card in hand:
                if card.get_rank() in card_hist:
                    card_hist[card.get_rank()] += 1
                else:
                    card_hist[card.get_rank()] = 1



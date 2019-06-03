from typing import List
from itertools import combinations
from operator import methodcaller

from hold_em.card import Card
from hold_em.hand import Hand


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
            raise ValueError(
                f"Must have 2 and only 2 hole cards when creating a Player. {len(hole_cards)} hole cards passed."
            )
        self.hole_cards = hole_cards

        if len(community_cards) != 5:
            raise ValueError(
                f"Must have 5 and only 5 community cards when creating a Player. {len(community_cards)} community cards passed."
            )
        self.community_cards = community_cards
        self.name = name

    def __str__(self) -> str:
        """Produces human friendly output for a player.
        :returns: A human friendly string representation of the player.
            Describes the hole cards and the community cards.
        :rtype: str
        """
        community_cards = ""
        for card in self.community_cards[:-1]:
            community_cards += f" the {str(card)},"
        community_cards = (
            f"{community_cards[:-2]} and the {str(self.community_cards[-1])}"
        )
        community_cards = community_cards.strip()
        return f"{self.name} holds the {self.hole_cards[0]} and the {self.hole_cards[1]} hole cards and holds {community_cards} as community cards."

    def get_hole_cards(self) -> List[Card]:
        """Get the 2 hole cards for this player.
        :returns: The 2 hole cards for this player.
        :rtype: List[Card]
        """
        return self.hole_cards

    def get_community_cards(self) -> List[Card]:
        """Get the community cards for this player.
        :returns: The community cards for this player.
        :rtype: List[Card]
        """
        return self.community_cards

    def make_five(self) -> List[List[Card]]:
        """Makes all the 5 card hands this player can have.
        :returns: A list of possible hands.
        :rtype: List[List[card.Card]]
        """
        five_card_combinations = []
        for comb in combinations(self.community_cards, 3):
            five_card_combinations.append(self.hole_cards + list(comb))
        return five_card_combinations

    def get_best_hand(self) -> Hand:
        """Gets the best hand this player can play.
        :returns: A hand representing the best cards this player has.
        :rtype: Hand
        """
        hands = [Hand(hand) for hand in self.make_five()]
        sorted_hands = sorted(hands, key=methodcaller("get_rank"), reverse=True)
        return sorted_hands[0]

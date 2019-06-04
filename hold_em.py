from operator import itemgetter

from hold_em.card import Card, CardParser
from hold_em.player import Player

if __name__ == "__main__":
    card_parser = CardParser()
    community_cards = []
    raw_community_cards = input("Please input community the cards:")

    try:
        for card in raw_community_cards.split():
            community_cards.append(card_parser.parse(card))
            print(f"{str(community_cards[-1])}")
    except KeyError as err:
        help_text = (
            "Community cards are 2 letters. The first is the rank. This must be"
            " one of A, Q, K, J, T, 9, 8, 7, 6, 5, 4, 3 or 2. The second letter"
            " is the suit. It must be one of D, C, H, S. There must be five and"
            " only five community cards."
        )
        print(f"Invalid character, {err} entered for card, {card}.\n{help_text}")
        exit()

    # A somewhat arbritrary maximum number of players.
    max_players = 20
    players = []
    i = 0
    try:
        while i < max_players:
            raw_player = input(f"Please input the cards for player # {i}:")
            if len(raw_player.strip()) == 0:
                print("End of player input.")
                break
            player_name, *player_cards = raw_player.strip().split()
            print(f"player name:{player_name}, player cards:{player_cards}")
            player_cards = [card_parser.parse(c) for c in player_cards[:2]]
            players.append(Player(player_name, player_cards, community_cards))
            print(f"Player {i+1}: {players[-1]}")
            i += 1
    except EOFError:
        print("End of player input.")

    best_hands = []
    for player in players:
        # todo: multiple players with the same name.
        print(f"Getting best hand for {player.name}")
        best_hand = player.get_best_hand()
        print(f"Best hand:{best_hand}")
        best_hands.append(
            (
                player.name,
                best_hand,
                best_hand.get_rank(),
                best_hand.get_high_card_in_hand_rank(),
                best_hand.get_high_kicker_card_rank(),
            )
        )
    print(f"best hand tuples: {best_hands}")
    sorted_players = sorted(best_hands, key=itemgetter(2, 3, 4), reverse=True)
    i = 1
    for player in sorted_players:
        print(f"{i} {player[0]} {str(player[1])}")
        i += 1
    print("done")

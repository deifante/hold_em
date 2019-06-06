from operator import itemgetter

from hold_em.card import Card, CardParser
from hold_em.player import Player

if __name__ == "__main__":
    card_parser = CardParser()
    community_cards = []
    card_help_text = (
        "Cards are 2 letters. The first is the rank. This must be one of A, Q,"
        " K, J, T, 9, 8, 7, 6, 5, 4, 3 or 2. The second letter is the suit. It"
        " must be one of D, C, H, S."
    )
    community_card_help = (
        "There must be five and only five community cards. Example:\nKS AD 3H 7C TD"
    )
    player_card_help = (
        "A player must have a unique name and two cards. Example:\nBecky JD QC"
    )
    raw_community_cards = input("Please input community the cards:")

    try:
        for card in raw_community_cards.split():
            community_cards.append(card_parser.parse(card))
    except KeyError as err:
        print(
            f"Invalid character, {err} entered for card, {card}."
            f"\n{card_help_text}\n{community_card_help}"
        )
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
            player_cards = [card_parser.parse(c) for c in player_cards[:2]]
            players.append(Player(player_name, player_cards, community_cards))
            i += 1
    except EOFError:
        print("End of player input.")
    except KeyError as err:
        print(
            f"Invalid character, {err} entered for player, ({raw_player})."
            f"\n{card_help_text}\n{player_card_help}"
        )
        exit()
    except ValueError as err:
        print(err)
        exit()

    best_hands = []
    for player in players:
        best_hand = player.get_best_hand()
        best_hands.append(
            (
                player.name,
                best_hand,
                best_hand.get_rank(),
                best_hand.get_high_card_in_hand_rank(),
                best_hand.get_high_kicker_card_rank(),
            )
        )
    sorted_players = sorted(best_hands, key=itemgetter(2, 3, 4), reverse=True)
    i = 1
    for player in sorted_players:
        print(f"{i} {player[0]} {str(player[1])}")
        i += 1
    print("done")

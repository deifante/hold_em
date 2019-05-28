from hold_em.card import Card, CardParser
from hold_em.player import Player, PlayerRank

if __name__ == '__main__':
    card_parser = CardParser()
    community_cards = []
    i = 0
    raw_community_cards = input('Please input community the cards:')

    i = 0
    for card in raw_community_cards.split():
        community_cards.append(card_parser.parse(card))
        print (f"{str(community_cards[-1])}")
        i += 1

    # A somewhat arbritrary maximum number of players.
    max_players = 20
    players = []
    i = 0
    try:
        while i < max_players:
            raw_player = input(f"Please input the cards for player # {i}:")
            if len(raw_player.strip()) == 0:
                print ('End of player input.')
                break
            player_name, *player_cards = raw_player.strip().split()
            print (f"player name:{player_name}, player cards:{player_cards}")
            player_cards = [card_parser.parse(c) for c in player_cards[:2]]
            players.append(Player(player_name, player_cards, community_cards))
            print(f'Player {i+1}: {players[-1]}')
            i += 1
    except EOFError:
        print (f'End of player input.')

    print ("Ranking a player's hand")
    rank = PlayerRank(players[0])
    rank.rank()
    print ('done')
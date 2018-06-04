def TexasHoldEm(num_of_players, ante, num_of_decks):
    from DeckGenerator import DeckGenerator
    from NumberConvertor import NumberConvertor
    # creates the players
    if num_of_players > 10:
        return 'That\'s too many people'
    players = [[] for i in range(num_of_players)]
    community_cards = []
    deck = []
    burn_cards = []
    rounds = 0
    # Generate hands
    while rounds < 2:
        for i in range(len(players)):
            new_card = DeckGenerator(num_of_decks)
            if new_card not in deck:
                deck.append(new_card)
                players[i].append(new_card)
            else:
                while new_card in deck:
                    new_card = DeckGenerator(num_of_decks)
                deck.append(new_card)
                players[i].append(new_card)
        rounds = rounds + 1
    # Generate first 3 community cards
    while rounds < 3:
        new_card = DeckGenerator(num_of_decks)
        if new_card not in deck:
            deck.append(new_card)
            burn_cards.append(new_card)
        else:
            while new_card in deck:
                new_card = DeckGenerator(num_of_decks)
            deck.append(new_card)
            burn_cards.append(new_card)
        while len(community_cards) < 3:
            new_card = DeckGenerator(num_of_decks)
            if new_card not in deck:
                deck.append(new_card)
                community_cards.append(new_card)
            else:
                while new_card in deck:
                    new_card = DeckGenerator(num_of_decks)
                deck.append(new_card)
                community_cards.append(new_card)
        rounds = rounds + 1

    # Generate last 2 community cards
    while rounds < 5:
        new_card = DeckGenerator(num_of_decks)
        if new_card not in deck:
            deck.append(new_card)
            burn_cards.append(new_card)
        else:
            while new_card in deck:
                new_card = DeckGenerator(num_of_decks)
            deck.append(new_card)
            burn_cards.append(new_card)
        while len(community_cards) == rounds:
            new_card = DeckGenerator(num_of_decks)
            if new_card not in deck:
                deck.append(new_card)
                community_cards.append(new_card)
            else:
                while new_card in deck:
                    new_card = DeckGenerator(num_of_decks)
                deck.append(new_card)
                community_cards.append(new_card)
        rounds = rounds + 1
    # Convert cards into something useful

    player_hands = NumberConvertor(players, num_of_decks)
    # For more than one deck, the number has to be divided by the number of decks used,
    # so the number can be converted to one of 52 cards in a playin deck.

    community_cards_suits = NumberConvertor(community_cards, num_of_decks)

    print(end='\n')

    if len(deck) < (num_of_players * 2 + 5 + 3):
        print("Something went wrong in card generation.")
        print(len(deck))
        if len(community_cards) < 5:
            print("The error is community cards")
            print(len(community_cards))
        elif len(burn_cards) < 3:
            print("The error is burn cards")
            print(len(burn_cards))
        else:
            print("The error is player cards")

    print(community_cards_suits)
    for i in range(len(player_hands)):
        print('Player', str(i + 1) + '\'s Hand:', player_hands[i])
    return
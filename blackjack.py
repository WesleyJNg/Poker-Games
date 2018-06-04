def blackjack(num_of_human_players, num_of_computer_players, ante, num_of_decks):
    '''
    It might be easier to use num_of_players = num_of_human_players + num_of_computer_players + 1
    '''
    num_of_players = num_of_human_players + num_of_computer_players
    # num_of_players + 1 because the dealer doesn't count as a player
    players = [[] for i in range(num_of_players + 1)]
    # every player and the dealer will be a list within players
    # the dealer is the last list since the dealer is the last to go during gameplay

    # visible_cards is for the AI to use to make decisions
    visible_cards = []

    # to keep track of the cards that have been generated
    deck = []

    # to keep track of players who have last
    busted_index = []
    # Dealing

    from DeckGenerator import DeckGenerator

    # This is only to create face down cards
    # num_of_players + 1 to include the dealer
    while len(deck) < (num_of_players + 1):

        # for loop so that each player and the dealer gets one face down card
        for i in range(len(players)):
            new_card = DeckGenerator(num_of_decks)
            # if the new card does not exist, gets added to deck and dealt to player
            if new_card not in deck:
                deck.append(new_card)
                players[i].append(new_card)
            # if the new card does exist, a new card is generated until a card that does not exist is generated
            else:
                while new_card in deck:
                    new_card = DeckGenerator(num_of_decks)

            # the generated card is then added to the deck and dealt to the player
                deck.append(new_card)
                players[i].append(new_card)

    # Create visible cards
    # num_of_players + 1 to include dealer
    while len(visible_cards) < (num_of_players + 1):

        # for loop so that each player and the dealer gets one face up card
        for i in range(len(players)):
            new_card = DeckGenerator(num_of_decks)

            # if the new card does not exist, gets added to deck, dealt to the player, and added to visible_cards
            if new_card not in deck:
                deck.append(new_card)
                visible_cards.append(new_card)
                players[i].append(new_card)

            # if the new card does exist, a new card is generated until a card that does not exist is generated
            else:
                while new_card in deck:
                    new_card = DeckGenerator(num_of_decks)

                # the generated card is then added to deck, dealt to the player, and added to visible_cards
                deck.append(new_card)
                players[i].append(new_card)
                visible_cards.append(new_card)

    # The start of check for blackjack

    # Convert the numbers to actual playing cards
    from NumberConvertor import NumberConvertor
    player_hands = NumberConvertor(players, num_of_decks)
    # player_hands now contains every hand as a list of string values with the names of playing cards

    # Convert the string values into the integer values that the playing cards represent
    from cardconvertor import handconvertor
    from cardconvertor import cardconvertor
    hand_value = handconvertor(player_hands)
    # hand_value now contains a list with the numeric value of each player's hand

    # list to know which player, if any, has a blackjack
    index_blackjack = []

    # for loop to check each player's hand or blackjack
    for i in range(len(hand_value)):
        if hand_value[i][0] == 21:

            # when i == len(hand_value), the dealer's hand is being checked for blackjack
            if i == len(hand_value):
                # if the dealer has blackjack, the game has ended with the house winning
                return 'Dealer says, "Blackjack." All players lost.'
            # report who has a blackjack
            else:
                print('Player ' + str(i + 1) + ' has a blackjack.')

                # save which players got a blackjack
                index_blackjack.append(i)

    # Player input?
    # the initial players are all human players so num_of_human_players
    for i in range(num_of_human_players):

        # skip human players who have blackjack
        if i in index_blackjack:
            continue

        # the actual player input part
        else:
            answer = ''

            # Turns the numbers in the player's hand into the actual cards
            hand = NumberConvertor(players[i], num_of_decks)

            # Whose turn it is
            print('Player', str(i + 1) + "'s turn")

            # Player's hand
            print('Hand:', hand, '\n')

            # Repeats question until player chooses to stay
            while answer != ('2' or 'stay'):

                # Asks for player's decision
                answer = input("Would you like to:"
                               "\n" "1. Hit, or"
                               "\n" "2. Stay?"
                               "\n")

                # Ensures the input is all lowercase
                if type(answer) == str:
                    answer = answer.lower()
                else:
                    continue

                # For Hit
                if answer == '1' or answer == 'hit':
                    # hand_value will be used to check for if the player's new card causes a bust
                    hand_value = 0

                    # generate the new card
                    new_card = DeckGenerator(num_of_decks)

                    # add new card to player's hand, deck, and visible card
                    if new_card not in deck:
                        players[i].append(new_card)
                        deck.append(new_card)
                        visible_cards.append(new_card)
                        hand = NumberConvertor(players[i], num_of_decks)

                        # prints player's hand so they can decide whether or not to take another card
                        print(hand)

                    else:
                        # generate new card until a card that is not in the deck is created
                        while new_card in deck:
                            new_card = DeckGenerator(num_of_decks)

                        # add new card to player's hand, deck, and visible card
                        players[i].append(new_card)
                        deck.append(new_card)
                        visible_cards.append(new_card)
                        hand = NumberConvertor(players[i], num_of_decks)

                        # print player's hand so they can decide whether or not to take another card
                        print(hand)

                    # Check for bust
                    # Ace conversion from 11 to 1 is not working as intended
                    # (Doesn't convert once, can't handle two aces)

                    # j because i is currently in use to ask each human player whether or not they want a new card
                    for j in range(len(hand)):

                        # take only the face value of the card
                        # 'Ace of Spades' becomes 'Ace'
                        card = hand[j].split(' ', )[0]

                        # 'Ace' becomes its numeric value (11)
                        card = cardconvertor(card)

                        # Calculate the new hand value once another card is converted
                        hand_value = hand_value + card

                        # Check for bust
                        if hand_value > 21:
                            card_sans_suit = []

                            # k because j is in use
                            for k in range(len(hand)):
                                card_sans_suit.append(hand[k].split(' ',)[0])

                            get_around_cant_assign_to_literal = 'Ace'
                            for get_around_cant_assign_to_literal in card_sans_suit:
                                hand_value = hand_value + (1 - 11)
                                # The below might not be usable with a while statement
                                # Need to reset it but only when there is a new ace?
                                ace_conversion = True
                            else:
                                continue
                        else:
                            continue
                    if hand_value > 21:
                        print('Player', str(i + 1), 'has busted.', '\n')
                        busted_index.append(i)
                        break
                    else:
                        continue
                # For Stay
                elif answer == '2' or answer == 'stay':
                    print('\n')
                    break

                # For if the human player does not give a proper response
                else:
                    print('\n', 'That was not a valid response.', '\n')

    # Computer player deciding whether or not to hit or stay


    # Final conversion from numbers to playing cards to reveal all hands
    player_hands = NumberConvertor(players, num_of_decks)
    for i in range(len(player_hands)):
        if i in busted_index:
            continue
        elif i == num_of_players:
            print('Dealer\'s hand: ', str(player_hands[i]))
        else:
            print('Player', str(i + 1) + '\'s', 'hand: ', str(player_hands[i]))
    # IDEA; use list.pop() to generate dealer hand then not_dealer will be the remaining list

    not_dealer = player_hands[:(len(player_hands) - 1)]
    dealer = player_hands[:num_of_players]
    if all(dealer > i for i in not_dealer):
        return 'Dealer won.'
    return 'Game ended'

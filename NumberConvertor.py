def NumberConvertor(cards, number_of_decks):
    suits = {0: 'Hearts',
             1: 'Spades',
             2: 'Diamonds',
             3: 'Clubs'}

    value = {0: 'Ace',
             1: '2',
             2: '3',
             3: '4',
             4: '5',
             5: '6',
             6: '7',
             7: '8',
             8: '9',
             9: '10',
             10: 'Jack',
             11: 'Queen',
             12: 'King'}

    if type(cards) == list:
        if type(cards[0]) == list:
            value3 = [[] for i in range(len(cards))]
            for i in range(len(cards)):
                for j in range(len(cards[i])):
                    number = value[(cards[i][j] // number_of_decks) % 13]
                    suit = suits[(cards[i][j] // number_of_decks) // 13]
                    card_name = str(number) + ' of ' + str(suit)
                    value3[i].append(card_name)
        else:
            value3 = []
            for i in range(len(cards)):
                number = value[(cards[i] // number_of_decks) % 13]
                suit = suits[(cards[i] // number_of_decks) // 13]
                card_name = str(number) + ' of ' + str(suit)
                value3.append(card_name)
    else:
        return
    return value3

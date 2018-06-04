def handconvertor(player_hands):
    face_to_number = {'10': 10,
                      'King': 10,
                      'Queen': 10,
                      'Jack': 10,
                      'Ace': 11,
                      '9': 9,
                      '8': 8,
                      '7': 7,
                      '6': 6,
                      '5': 5,
                      '4': 4,
                      '3': 3,
                      '2': 2}
    hand_value = [[] for i in range(len(player_hands))]
    for i in range(len(player_hands)):
        value = 0
        for j in range(len(player_hands[i])):
            card = player_hands[i][j].split(' ', )[0]
            value = value + face_to_number[card]
        hand_value[i].append(value)

    return hand_value


def cardconvertor(card):
    face_to_number = {'10': 10,
                      'King': 10,
                      'Queen': 10,
                      'Jack': 10,
                      'Ace': 11,
                      '9': 9,
                      '8': 8,
                      '7': 7,
                      '6': 6,
                      '5': 5,
                      '4': 4,
                      '3': 3,
                      '2': 2}
    card_value = face_to_number[card]
    return card_value

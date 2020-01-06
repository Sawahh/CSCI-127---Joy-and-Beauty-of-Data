# -----------------------------------------+
# Sierra Stephens                          |
# CSCI 127, Program 2                      |
# Last Updated: Feb 6, 2019                |
# -----------------------------------------|
# A simplified Cribbage scoring system.    |
# -----------------------------------------+

def pair(hand):
    points = 0
    for i in range(len(hand)):
        for n in range(i+1, len(hand)):
            if hand[i][0] == hand[n][0]:
                points += 2
    return points

def point_value(string):
    if string == "Two":
        return 2
    if string == "Three":
        return 3
    if string == "Four":
        return 4
    if string == "Five":
        return 5
    if string == "Six":
        return 6
    if string == "Seven":
        return 7
    if string == "Eight":
        return 8
    if string == "Nine":
        return 9
    if string == "Ten":
        return 10
    if string == "Jack":
        return 10
    if string == "Queen":
        return 10
    if string == "King":
        return 10
    if string == "Ace":
        return 11
def fifteens(hand):
    points = 0
    for i in range(len(hand)):
        for n in range(i+1, len(hand)):
            if (point_value(hand[i][0]) + point_value(hand[n][0])) == 15:
                points += 2
    return points

def flush(hand):
    if hand[0][1] == hand[1][1] == hand[2][1] == hand[3][1] == hand[4][1]:     #### weak
        return 5
    else:
        return 0

def evaluate_hand(hand):
    points = flush(hand) + fifteens(hand) + pair(hand)
    print("Points scored:", points, "\n")

def print_hand(cards_in_hand, number):
    print("Hand", str(number) + ": ", end = "")
    for i in cards_in_hand:
        if i != cards_in_hand[(len(cards_in_hand) - 1)]:       ##### strong
            print(i[0], i[1], end = ", ")
        else:
            print(i[0], i[1])

# -----------------------------------------+
# Do not change anything below this line.  |
# -----------------------------------------+

def process_hands(cribbage_input, cards_in_hand):
    number = 1
    for hand in cribbage_input:
        hand = hand.split()
        hand_as_list = []
        for i in range(cards_in_hand):
            hand_as_list.append([hand[0].capitalize(), hand[1].capitalize()])
            hand = hand[2:]
        print_hand(hand_as_list, number)
        evaluate_hand(hand_as_list)
        number += 1

# -----------------------------------------+

def main():
    cribbage_file= open("cribbage.txt", "r")
    process_hands(cribbage_file, 5)
    cribbage_file.close()

# -----------------------------------------+

main()

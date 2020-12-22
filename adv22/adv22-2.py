from collections import deque
import copy
from aocd import get_data

my_list = get_data(day=22).split("\n\n")
p1_string = list(map(int, my_list[0].strip("\n").split("\n")[1:]))
p2_string = list(map(int, my_list[1].strip("\n").split("\n")[1:]))

def queue_to_list(queue):
    queue_copy = copy.deepcopy(queue)
    l = []

    while(not len(queue_copy) == 0):
        card = queue_copy.popleft()
        l.append(card)

    return l

def game(p1_deck_list, p2_deck_list):
    past_configs_list = []
    p1_deck = deque()
    p2_deck = deque()

    for i in range(0, len(p1_deck_list)):
        p1_deck.append(p1_deck_list[i])

    for i in range(0, len(p2_deck_list)):
        p2_deck.append(p2_deck_list[i])

    while(not len(p1_deck) == 0 and not len(p2_deck) == 0):

        if([queue_to_list(p1_deck), queue_to_list(p2_deck)] in past_configs_list):
            return (0, 1)

        past_configs_list.append([queue_to_list(p1_deck), queue_to_list(p2_deck)])
        p1_card = p1_deck.popleft()
        p2_card = p2_deck.popleft()

        if(len(p1_deck) >= p1_card and len(p2_deck) >= p2_card):
            winner = game(queue_to_list(p1_deck)[:p1_card], queue_to_list(p2_deck)[:p2_card])[1]

            if(winner == 1):
                p1_deck.append(p1_card)
                p1_deck.append(p2_card)

            elif(winner == 2):
                p2_deck.append(p2_card)
                p2_deck.append(p1_card)

        else:

            if(p1_card > p2_card):
                p1_deck.append(p1_card)
                p1_deck.append(p2_card)

            elif(p2_card > p1_card):
                p2_deck.append(p2_card)
                p2_deck.append(p1_card)

    winning_cards = []

    if(not len(p1_deck) == 0):

        winning_cards = queue_to_list(p1_deck)
        winning_score = 0

        for i in range(0,len(winning_cards[::-1])):
            winning_score += (i + 1) * winning_cards[::-1][i]

        return (winning_score, 1)

    elif(not len(p2_deck) == 0):

        winning_cards = queue_to_list(p2_deck)
        winning_score = 0

        for i in range(0,len(winning_cards[::-1])):
            winning_score += (i + 1) * winning_cards[::-1][i]

        return (winning_score, 2)

print(game(p1_string, p2_string)[0])

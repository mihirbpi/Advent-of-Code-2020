from collections import deque
from aocd import get_data

my_list = get_data(day=22).split("\n\n")
p1_string = list(map(int, my_list[0].strip("\n").split("\n")[1:]))
p2_string = list(map(int, my_list[1].strip("\n").split("\n")[1:]))

def game(p1_deck_list, p2_deck_list):
    past_configs_list = []
    p1_deck = deque(p1_deck_list)
    p2_deck = deque(p2_deck_list)

    while(len(p1_deck) > 0 and len(p2_deck) > 0):

        if([list(p1_deck), list(p2_deck)] in past_configs_list):
            return (p1_deck, 1)

        past_configs_list.append([list(p1_deck), list(p2_deck)])
        p1_card = p1_deck.popleft()
        p2_card = p2_deck.popleft()

        if(len(p1_deck) >= p1_card and len(p2_deck) >= p2_card):
            winner = game(list(p1_deck)[:p1_card], list(p2_deck)[:p2_card])[1]

            if(winner == 1):
                p1_deck.append(p1_card)
                p1_deck.append(p2_card)

            else:
                p2_deck.append(p2_card)
                p2_deck.append(p1_card)

        else:

            if(p1_card > p2_card):
                p1_deck.append(p1_card)
                p1_deck.append(p2_card)

            else:
                p2_deck.append(p2_card)
                p2_deck.append(p1_card)

    if(len(p1_deck) > 0):
        return (p1_deck, 1)

    else:
        return (p2_deck, 2)

winning_deck = list(game(p1_string, p2_string)[0])[::-1]
winning_score = 0

for i in range(0, len(winning_deck)):
    winning_score += (i + 1) * winning_deck[i]

print(winning_score)

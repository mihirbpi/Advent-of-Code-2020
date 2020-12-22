import asyncio
from aocd import get_data

my_list = get_data(day=22).split("\n\n")
p1_string = list(map(int, my_list[0].strip("\n").split("\n")[1:]))
p2_string = list(map(int, my_list[1].strip("\n").split("\n")[1:]))

p1_deck = asyncio.Queue()
p2_deck = asyncio.Queue()

for i in range(0, len(p1_string)):
    p1_deck.put_nowait(p1_string[i])

for i in range(0, len(p2_string)):
    p2_deck.put_nowait(p2_string[i])

while(not p1_deck.empty() and not p2_deck.empty()):
    p1_card = p1_deck.get_nowait()
    p2_card = p2_deck.get_nowait()

    if(p1_card > p2_card):
        p1_deck.put_nowait(p1_card)
        p1_deck.put_nowait(p2_card)

    elif(p2_card > p1_card):
        p2_deck.put_nowait(p2_card)
        p2_deck.put_nowait(p1_card)

winning_cards = []

if(not p1_deck.empty()):

    while(not p1_deck.empty()):
        card = p1_deck.get_nowait()
        winning_cards.append(card)


elif(not p2_deck.empty()):

    while(not p2_deck.empty()):
        card = p2_deck.get_nowait()
        winning_cards.append(card)

winning_score = 0

for i in range(0,len(winning_cards[::-1])):
    winning_score += (i + 1) * winning_cards[::-1][i]

print(winning_score)

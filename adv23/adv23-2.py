from aocd import get_data

cups_list = list(map(int, list(get_data(day=23))))
cups_list.extend(range(max(cups_list) + 1, 1000000 + 1))
size = len(cups_list)

class Node(object):

    def __init__(self, parent, value, prev, next_):
        assert isinstance(parent, LinkedList)
        self.parent = parent
        self.value = value
        self.prev = prev
        self.next = next_

    def insert(self, x):
        node = Node(self.parent, x, self, self.next)
        self.parent.D[x] = node
        self.next = node
        node.next.prev = node
        return node

    def erase(self):
        self.next.prev = self.prev
        self.prev.next = self.next
        del self.parent.D[self.value]
        del self

class LinkedList(object):

    def __init__(self):
        self.D = {}

    def append(self, prev, x):

        if(prev is None):
            node = Node(self, x, None, None)
            node.next = node
            node.next.prev = node
            self.D[x] = node
            return node

        else:
            node = Node(self, x, prev, prev.next)
            prev.next = node
            node.next.prev = node
            self.D[x] = node
            return node

    def find(self, x):
        return self.D[x]

    def to_list(self, start):
        node = self.D[start]
        result = [node.value]
        node = node.next

        while (node.value != start):
            result.append(node.value)
            node = node.next

        return result

cups_linked_list = LinkedList()
prev = None

for num in cups_list:
    prev = cups_linked_list.append(prev, num)

current_cup_node = cups_linked_list.find(cups_list[0])

del cups_list

for i in range(0, 10000000):

    current_cup = current_cup_node.value
    pick_up = []
    pick_up_node = current_cup_node.next

    for j in range(0, 3):
        pick_up.append(pick_up_node.value)
        tmp = pick_up_node.next
        pick_up_node.erase()
        pick_up_node = tmp

    if(current_cup == 1):
        dest_cup = size

    else:
        dest_cup = current_cup - 1

    while (dest_cup in pick_up):

        if(dest_cup == 1):
            dest_cup = size

        else:
            dest_cup -= 1

    dest_node = cups_linked_list.find(dest_cup)

    for cup in pick_up:
        dest_node = dest_node.insert(cup)

    del dest_node

    current_cup_node = cups_linked_list.find(current_cup)
    current_cup_node = current_cup_node.next

print(cups_linked_list.to_list(1)[1] * cups_linked_list.to_list(1)[2])

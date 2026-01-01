import random

#1
class Contestant:
    def __init__(self, name, chest_number, country, time = 0):
        self.name = name
        self.chest_number = chest_number
        self.time = time
        self.country = country

    def __str__(self):
        return f"{self.name} {self.chest_number} {self.time} {self.country}"

#2
class Node:
    def __init__(self , contestant):
        self.contestant = contestant
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self .head=None
        self.tail =None
    def append(self , contestant):
        new_node = Node(contestant)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def sort_by_time(self):
        """Sort the linked list of contestants by their time in ascending order."""
        if self.head is None:
            return
        current = self.head
        while current is not None:
            key_contestant = current.contestant
            prev_node = current.prev
            while prev_node is not None and prev_node.contestant.time > key_contestant.time:
                prev_node.next.contestant = prev_node.contestant
                prev_node = prev_node.prev
            if prev_node is None:
                self.head.contestant = key_contestant
            else:
                prev_node.next.contestant = key_contestant
            current = current.next

    def get_top_performers(self, M):
        """Get the top M performers from the linked list."""
        performers = []
        current = self.head
        while current is not None and len(performers) < M:
            performers.append(current.contestant)
            current = current.next
        return performers

#3
def simulate_heats(contestants , N, M):
    if len(contestants) <= N:
        final_heat = LinkedList()
        for contestant in contestants:
            contestant.time = random.randint(1, 100)  # Assign a random time for each contestant
            final_heat.append(contestant)
        final_heat.sort_by_time()
        return final_heat.get_top_performers(M)
    while len(contestants) > N:
        heats = []
        for i in range(0, len(contestants), N):
            heat_contestants = contestants[i:i + N]
            heat = LinkedList()
            for contestant in heat_contestants:
                contestant.time = random.randint(1, 100)
                heat.append(contestant)
            heat.sort_by_time()
            heats.append(heat.get_top_performers(M))
        next_round_contestants = []
        for heat_tops in heats:
            next_round_contestants.extend(heat_tops)
        contestants = next_round_contestants
    final_heat = LinkedList()
    for contestant in contestants:
        contestant.time = random.randint(1, 100)
        final_heat.append(contestant)
    final_heat.sort_by_time()
    return final_heat.get_top_performers(3)

#4
def test():
    """Create a list of contestants."""
    contestants = [
    Contestant("Contestant A", 1, "Country A"),
    Contestant("Contestant B", 2, "Country B"),
    Contestant("Contestant C", 3, "Country C"),
    Contestant("Contestant D", 4, "Country D"),
    Contestant("Contestant E", 5, "Country E"),
    Contestant("Contestant F", 6, "Country F"),
    Contestant("Contestant G", 7, "Country G"),
    Contestant("Contestant H", 8, "Country H")
    ]

    N = 4 #Number of contestants per heat
    M = 2 #Number of top performers to select from each heat

    #Run the final selection process
    winners = simulate_heats(contestants, N, M)
    print("Final Selection:")
    medals = ["Gold", "Silver", "Bronze"]
    for i , winner in enumerate(winners):
        print(f"{medals[ i ]}: {winner}")

test()

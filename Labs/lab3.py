from colorama import Fore, Style, init
init(autoreset=True)

class Node:
    def __init__(self, id, name):
        self.next = None
        self.id = id
        self.name = name
    
class TicketQueue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.total_customers = 0
    
    def enqueue(self, id, name):
        node = Node(id, name)
        if self.front is None:
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node
        self.total_customers += 1
        return name
    
    def dequeue(self):
        if self.front is None:
            return None
        name = self.front.name
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        self.total_customers -= 1
        return name
    
    def peek_next_customer(self):
        if self.front is None or self.front.next is None:
            return None
        return self.front.next.name
    
    def cancel_booking(self, id):
        if self.front is None:
            return None
        if id == self.front.id:
            name = self.front.name
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            self.total_customers -= 1
            return name
        prev = self.front
        curr = self.front.next
        while curr:
            if curr.id == id:
                name = curr.name
                prev.next = curr.next
                if curr == self.rear:
                    self.rear = prev
                self.total_customers -= 1
                return name
            prev = curr
            curr = curr.next
        return None
    
    def move_to_end(self, id):
        if self.front is None or self.rear.id == id:
            return None
        prev = None
        curr = self.front
        while curr:
            if curr.id == id:
                break
            prev = curr
            curr = curr.next
        if curr is None:
            return None
        if prev:
            prev.next = curr.next
        if curr == self.front:
            self.front = curr.next
        if curr == self.rear:
            return None
        self.rear.next = curr
        self.rear = curr
        curr.next = None
        return curr.name
    
    def find_position(self, id):
        if self.front is None:
            return None
        pos = 1
        temp = self.front
        while temp:
            if temp.id == id:
                return (pos, temp.name)
            pos += 1
            temp = temp.next
        return None
    
    def total_customers_count(self):
        return self.total_customers


def test():
    YELLOW = "\033[93m"
    RESET = "\033[0m"

    queue = TicketQueue()

    # Add initial customers
    customers = [(101, "Raj"), (102, "Maya"), (103, "Liam"), (104, "Sara")]
    print(f"{YELLOW}Adding customers to the queue:{RESET}")
    for cust_id, cust_name in customers:
        added_name = queue.enqueue(cust_id, cust_name)
        print(f"{added_name} (ID: {cust_id}) joined the queue.")

    print(f"\n{YELLOW}Peek at the next customer:{RESET}")
    next_customer = queue.peek_next_customer()
    print(f"Next customer to be served: {next_customer}" if next_customer else "Queue is empty.")

    print(f"\n{YELLOW}Find positions by ID:{RESET}")
    for cust_id in [102, 104]:
        result = queue.find_position(cust_id)
        if result:
            pos, name = result
            print(f"{name} (ID {cust_id}) is at position {pos} in the queue.")
        else:
            print(f"Customer ID {cust_id} not found.")

    print(f"\n{YELLOW}Move a customer to the end:{RESET}")
    moved_name = queue.move_to_end(102)
    print(f"{moved_name} has been moved to the end of the queue." if moved_name else "Customer not found or already at the end.")

    print(f"\n{YELLOW}Cancel a booking:{RESET}")
    cancelled_name = queue.cancel_booking(103)
    print(f"{cancelled_name}'s booking has been cancelled." if cancelled_name else "Customer not found.")

    print(f"\n{YELLOW}Serve the next customer:{RESET}")
    served_name = queue.dequeue()
    print(f"{served_name} has been served." if served_name else "Queue is empty.")

    print(f"\n{YELLOW}Peek at the next customer after serving one:{RESET}")
    next_customer = queue.peek_next_customer()
    print(f"Next customer to be served: {next_customer}" if next_customer else "Queue is empty.")

    print(f"\n{YELLOW}Total customers remaining:{RESET} {queue.total_customers_count()}")

    # Add a new customer
    print(f"\n{YELLOW}Adding a new customer:{RESET}")
    added_name = queue.enqueue(105, "Rajat")
    print(f"{added_name} (ID: 105) joined the queue.")

    # Serve next customer
    print(f"\n{YELLOW}Serve the next customer:{RESET}")
    served_name = queue.dequeue()
    print(f"{served_name} has been served." if served_name else "Queue is empty.")

    # Move last customer to end
    print(f"\n{YELLOW}Move last customer to end:{RESET}")
    moved_name = queue.move_to_end(105)
    print(f"{moved_name} has been moved to the end." if moved_name else "Customer already at the end or not found.")

    # Peek at next customer
    print(f"\n{YELLOW}Peek at next customer:{RESET}")
    next_customer = queue.peek_next_customer()
    print(f"Next customer to be served: {next_customer}" if next_customer else "Queue is empty.")

    print(f"\n{YELLOW}Total customers remaining in the queue:{RESET} {queue.total_customers_count()}")


test()

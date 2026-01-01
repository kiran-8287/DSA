# ---------------------------
# Queue class
# ---------------------------

class Queue:
    def __init__(self):
        # Initialize an empty queue using a list
        self.items = []

    def is_empty(self):
        """Check if the queue is empty. Returns True if empty, False otherwise."""
        return len(self.items) == 0

    def enqueue(self, task):
        """
        Add a task at the rear of the queue.
        :param task: tuple (task_name, priority, department)
        """
        self.items.append(task)

    def dequeue(self):
        """
        Remove and return the front task of the queue.
        If the queue is empty, returns None.
        """
        if not self.is_empty():
            return self.items.pop(0)

    def peek(self):
        """Return the front task without removing it. Returns None if empty."""
        if not self.is_empty():
            return self.items[0]

    def size(self):
        """Return the number of tasks currently in the queue."""
        return len(self.items)


# ---------------------------
# Print tasks in reverse order
# ---------------------------
def print_reverse(queue):
    """
    Recursively print all tasks from latest to earliest (reverse order).
    
    :param queue: Queue object
    """
    def helper():
        if(queue.is_empty() == False):
            item = queue.dequeue()
            helper()
            print(f"{item[0]} ({item[1]}, {item[2]})")
            queue.enqueue(item)
        else:
            return
    helper()

# ---------------------------
# Find highest priority task in a department
# ---------------------------
def find_highest_priority(queue, department, current_min=None, result=None):
    """
    Recursively find the task with the lowest priority within a specific department.
    
    :param queue: Queue object
    :param department: String, department to filter tasks
    :param current_min: Current minimum priority (used in recursion)
    :param result: Current task with minimum priority (used in recursion)
    :return: tuple (task_name, priority, department) or None if not found
    """
    def helper(current_min=None, result=None):
        if queue.is_empty():
            return result, current_min
        item = queue.dequeue()
        if item[2] == department:
            if current_min is None or item[1] < current_min:
                current_min = item[1]
                result = item
        result, current_min = helper(current_min, result)
        queue.enqueue(item)
        return result, current_min
    result, current_min = helper(current_min,result)
    return result

# ---------------------------
# Reorder queue by department
# ---------------------------
def move_department_to_front(queue, department):
    """
    Recursively move all tasks of a given department to the front of the queue.
    Preserves the relative order of both the department tasks and other tasks.
    
    :param queue: Queue object
    :param department: String, department whose tasks should be moved to front
    """
    q = Queue()
    def helper(q):
        if(queue.is_empty()==False):
            item = queue.dequeue()
            if(item[2] == department):
                q.enqueue(item)
                helper(q)
            else:
                helper(q)
                queue.enqueue(item)
        else:
            return
        
    helper(q)
    def sender(q):
        if(queue.is_empty()):
            return
        q.enqueue(queue.dequeue())
        sender(q)
    def receiver(q):
        if(q.is_empty()):
            return
        queue.enqueue(q.dequeue())
        receiver(q)
    sender(q)
    receiver(q)
    
def test():
    task_queue = Queue()
    task_queue.enqueue(("Task1", 5, "Cardiology"))
    task_queue.enqueue(("Task2", 2, "Neurology"))
    task_queue.enqueue(("Task3", 1, "Cardiology"))
    task_queue.enqueue(("Task4", 4, "Orthopedics"))
    task_queue.enqueue(("Task5", 3, "Neurology"))

    print("Tasks in reverse order:")
    print_reverse(task_queue)

    print("\nHighest priority task in Cardiology:")
    highest = find_highest_priority(task_queue, "Cardiology")
    if highest:
        print(f"{highest[0]} ({highest[1]}, {highest[2]})")
    else:
        print("None")

    print("\nQueue after moving Cardiology tasks to front:")
    move_department_to_front(task_queue, "Cardiology")
    for t in task_queue.items:
        print(f"{t[0]} ({t[1]}, {t[2]})")
test()

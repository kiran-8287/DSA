
import time

# Employee Node Class
class Employee:
    def __init__(self, emp_id, name):
        """
        Initialize an Employee node.

        Parameters:
        - emp_id: Unique identifier for the employee (int or str)
        - name: Name of the employee (str)

        Attributes to initialize:
        - id: Employee ID
        - name: Employee name
        - check_in_time: Time the employee checked in (str or empty)
        - check_out_time: Time the employee checked out (str or empty)
        - is_present: Boolean flag, True if present, else False
        - next: Pointer to next employee in the list
        - prev: Pointer to previous employee in the list
        """
        # TODO: Initialize all attributes required for the Employee node
        self.id = emp_id
        self.name = name
        self.check_in_time = ""
        self.check_out_time = ""
        self.is_present = False
        self.next = None
        self.prev = None

# Attendance System using a Doubly Circular Linked List
class AttendanceSystem:
    def __init__(self):
        """
        Initialize the attendance system.

        Attributes to initialize:
        - head: Points to the first employee (None if list is empty)
        - total_employees: Keeps count of total employees
        """
        # TODO: Initialize required system attributes
        self.head = None
        self.total_employees = 0

    def get_current_time(self):
        """
        Returns the current system time as a formatted string.
        Example format: "YYYY-MM-DD HH:MM:SS"
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())


        """
        # TODO: get current system time as formatted string
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

    def add_employee(self, emp_id, name):
        """
        Adds a new employee to the system.

        Steps:
        - Create a new Employee object
        - If the list is empty, insert as head and update next/prev as required
        - Else, add at the end of the circular doubly linked list (before head)
        - Increment total_employees
        - Print a success message after successful addition
        """
        # TODO: Implement adding a new employee
        node = Employee(emp_id,name)
        if(self.head == None):
            self.head = node
            node.next = node
            node.prev = node
        else:
            temp = self.head
            while(temp.next != self.head):
                temp = temp.next
            temp.next = node
            node.prev = temp
            node.next = self.head
            self.head.prev = node
        self.total_employees += 1

    def search_employee(self, emp_id):
        """
        Search for an employee 

        Returns:
        - Employee instance if found
        - None if not found
        """
        # TODO: Traverse the list to find and return the employee
        if(self.head == None):
            return None
        temp = self.head
        while(temp.next != self.head):
            if(temp.id == emp_id):
                return temp
            temp = temp.next
        if(temp.id == emp_id):
            return temp
        return None

    def check_in(self, emp_id):
        """
        Mark an employee as present and record check-in time.

        Steps:
        - Search for employee 
        - If not found, print message and return
        - If already checked in, inform user and return
        - Otherwise, set is_present = True and record check-in time
        - Reset check-out time to empty
        - Print confirmation message
        """
        # TODO: Implement check-in logic
        node = self.search_employee(emp_id)
        if(node == None):
            print("Employee not found!")
            return
        if(node.check_in_time == ""):
            node.is_present = True
            node.check_in_time = self.get_current_time()
            node.check_out_time = ""
        else:
            return

    def check_out(self, emp_id):
        """
        Mark an employee as absent and record check-out time.

        Steps:
        - Search for employee 
        - If not found, print message and return
        - If not checked in, inform user and return
        - Otherwise, set is_present = False and record check-out time
        - Print confirmation message
        """
        # TODO: Implement check-out logic
        node = self.search_employee(emp_id)
        if(node == None):
            print("Employee not found!")
            return
        if(node.check_in_time != ""):
            node.is_present = False
            node.check_out_time = self.get_current_time()
        else:
            return

    def display_all(self):
        """
        Display all employees and their attendance status.

        Details to print:
        - Employee ID, name, status (Present/Absent), check-in, and check-out times

        Steps:
        - If no employees exist, inform the user
        - Else, traverse the list and print all employee details
        """
        # TODO: Traverse and display data for all employees
        if(self.head == None):
            print("List is empty!")
            return
        temp = self.head
        while(temp.next != self.head):
            print(f"Employee ID-{temp.id}, Name -{temp.name}")
            temp = temp.next
        print(f"Employee ID-{temp.id}, Name -{temp.name}")
        return

    def update_employee(self, emp_id, new_name):
        """
        Update the name of an employee.

        Steps:
        - Search for employee 
        - If not found, print message and return
        - Else, update name and print confirmation
        """
        # TODO: Implement update logic
        node = self.search_employee(emp_id)
        if(node == None):
            print("Employee not found!")
            return
        node.name = new_name
        print(f"Updated name")

    def delete_employee(self, emp_id):
        """
        Delete an employee from the system.

        Steps:
        - Search for employee 
        - If not found, print message and return
        - Else, update pointers to remove the employee from the circular doubly linked list
        - If list becomes empty, update head accordingly
        - Decrement total_employees
        - Print confirmation message
        """
        # TODO: Implement deletion logic
        node = self.search_employee(emp_id)
        if(node == None):
            print("Employee not found!")
            return
        if(node == self.head):
            if(node.next == node):
                self.head = None
                return
            node.next.prev = node.prev
            node.prev.next = node.next
            self.head = node.next
            del(node)
        elif(node.next == self.head):
            node.prev.next = self.head
            self.head.prev = node.prev
            del(node)
        else:
            node.next.prev = node.prev
            node.prev.next = node.next
            del(node)
        self.total_employees -= 1
    def sort_by_id(self):
        """
        Sort all employees by their IDs.

        Steps:
        - reorder nodes by emp_id
        - Update the list structure as needed 
        - Print a message after sorting is complete
        """
        if(self.head == None or self.head.next == self.head):
            return

        swapped = True
        while swapped:
            swapped = False
            temp = self.head

            while(temp.next != self.head):
                if(temp.id > temp.next.id):
                    temp.id, temp.next.id = temp.next.id, temp.id
                    temp.name, temp.next.name = temp.next.name, temp.name
                    temp.check_in_time, temp.next.check_in_time = temp.next.check_in_time, temp.check_in_time
                    temp.check_out_time, temp.next.check_out_time = temp.next.check_out_time, temp.check_out_time
                    temp.is_present, temp.next.is_present = temp.next.is_present, temp.is_present
                    swapped = True
                temp = temp.next
        print("Employees sorted by ID.")
            



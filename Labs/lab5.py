class Patient:
    def __init__(self,priority,name):
        self.priority = priority
        self.name = name

class PatientQueue:
    def __init__(self):
        self.heap = []

    def upheap(self,i):
        while(i > 0):
            parent = (i-1)//2
            if(self.heap[parent].priority > self.heap[i].priority):
                self.heap[parent],self.heap[i] = self.heap[i],self.heap[parent]
                i = parent
            else:
                break

    def downheap(self,i):
        n = len(self.heap)
        smallest = i

        while(True):
            l = 2*i + 1
            r = 2*i + 2
            if(l < n and self.heap[smallest].priority > self.heap[l].priority):
                smallest = l
            if(r < n and self.heap[smallest].priority > self.heap[r].priority):
                smallest = r
            if(smallest != i):
                self.heap[smallest],self.heap[i] = self.heap[i],self.heap[smallest]
                i = smallest
            else:
                break

    def add_patient(self,patient):
        self.heap.append(patient)
        self.upheap(len(self.heap)-1)
    
    def get_next_patient(self):
        out = self.heap[0]
        self.heap[0],self.heap[-1] = self.heap[-1],self.heap[0]
        self.heap.pop()
        self.downheap(0)
        return out
    
    def update_priority(self,name,new_priority):
        node = None
        idx = 0
        for i in range(len(self.heap)):
            if(name == self.heap[i].name):
                node = self.heap[i]
                idx = i
                break
        old_priority = node.priority
        node.priority = new_priority
        if(old_priority < new_priority):
            self.downheap(idx)
        else:
            self.upheap(idx)
    
    def show_all_patients(self):
        for i in range(len(self.heap)):
            print(f"Name {self.heap[i].name}, Priority: {self.heap[i].priority}")


def test_patient_queue():
    pq = PatientQueue()

    # Adding the new patients
    patients = [
        (4, "Monica"), (5, "Amit"), (6, "Ivan"), (15, "Mary"), (9, "John"),
        (7, "Abram"), (20, "Vihan"), (16, "Kevin"), (25, "Nancy"), (14, "Harshitha"),
        (12, "Ravi"), (11, "Varun"), (13, "Karan"), (2, "David")
    ]

    for priority, name in patients:
        patient = Patient(priority, name)
        pq.add_patient(patient)

    print("All Patients in heap order:")
    pq.show_all_patients()

    print("\nTreated Patient:")
    treated = pq.get_next_patient()
    print(f"Name: {treated.name}, Priority: {treated.priority}\n")

    print("\nRemaining Patients in heap order:")
    pq.show_all_patients()

    # Increase priority of Amit from 5 to 1 (higher priority)
    print("\nUpdating priority of Amit from 5 to 1...")
    pq.update_priority("Amit", 1)
    pq.show_all_patients()

    # Decrease priority of Abram from 7 to 17 (lower priority)
    print("\nUpdating priority of Abram from 7 to 17...")
    pq.update_priority("Abram", 17)
    pq.show_all_patients()

    print("\nTreated Patient:")
    treated = pq.get_next_patient()
    print(f"Name: {treated.name}, Priority: {treated.priority}")

    print("\nRemaining Patients in heap order:")
    pq.show_all_patients()


# Run the updated test
test_patient_queue()

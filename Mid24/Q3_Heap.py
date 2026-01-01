class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, value):
        """Insert value into the heap"""
        pass

    def extract_max(self):
        """Remove and return the maximum element"""
        pass

    def get_heap(self):
        """Return heap as level-order list"""
        pass

    # ---------------- Heapify Helpers ----------------
    def _heapify_up(self, index):
        """Move the element at index up to maintain heap property"""
        pass


    def _heapify_down(self, index):
        """Move the element at index down to maintain heap property"""
        pass

def test():
    values = [10, 30, 20, 5, 40, 15]
    heap = MaxHeap()

    for v in values:
        heap.insert(v)

    print("Heap after insertions (level order):", heap.get_heap())

    max_val = heap.extract_max()
    print("Extracted Maximum:", max_val)
    
    print("Heap after one extraction (level order):", heap.get_heap())


# Run test
if __name__ == "__main__":
    test()


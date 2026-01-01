# class MinHeap:
#     def __init__(self):
#         self.heap = []
    
#     def insert(self, key):
#         self.heap.append(key)
#         self.upheap(len(self.heap)-1)
    
#     def removeMin(self):
#         self.heap[0] , self.heap[len(self.heap)-1] = self.heap[len(self.heap)-1] , self.heap[0]
#         out = self.heap.pop()
#         self.downheap(0)
#         return out
        
#     def upheap(self, i):
#         while(i > 0):
#             parent = (i - 1) // 2
#             if(self.heap[parent] > self.heap[i]):
#                 self.heap[parent] , self.heap[i] = self.heap[i] , self.heap[parent]
#                 i = parent
#             else:
#                 break
    
#     def downheap(self, i):
#         n = len(self.heap)
#         while True:
#             smallest = i
#             l = 2*i + 1
#             r = 2*i + 2
#             if(l < n and self.heap[l] < self.heap[smallest]):
#                 smallest = 1
#             if(r < n and self.heap[r] < self.heap[smallest]):
#                 smallest = r
#             if(smallest != i):
#                 self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
#                 i = smallest
#             else:
#                 break
    
#     def heapify(self, arr):
#         self.heap = arr[:]
#         n = len(self.heap)
#         for i in range((n // 2) - 1, -1, -1):
#             self.downheap(i)
    
#     def show(self):
#         print("Heap: ", self.heap)

# mh=MinHeap()
# mh. insert(5); mh. insert(3); mh. insert(8)
# mh.show()
# print("Removed:", mh.removeMin()); mh.show()

# class MaxHeap:
#     def __init__(self):
#         self.heap= []

#     def insert(self , key):
#         self.heap.append(key)
#         self.upheap(len(self.heap)-1)
    
#     def removeMax(self):
#         maximum = self.heap[0]
#         self.heap[0] , self.heap[len(self.heap)-1] = self.heap[len(self.heap)-1], self.heap[0]
#         self.heap.pop()
#         self.downheap(0)
#         return maximum

#     def upheap(self, i):
#         parent = (i - 1) // 2
#         while(i > 0):
#             if(self.heap[i] > self.heap[parent]):
#                 self.heap[parent] , self.heap[i] =  self.heap[i] ,self.heap[parent]
#                 i = parent
#             else:
#                 break
    
#     def downheap(self, i):
#         n = len(self.heap)
#         while True:
#             largest = i
#             l = 2*i + 1
#             r = 2*i + 2
#             if(l < n and self.heap[l] > self.heap[largest]):
#                 largest = l
#             if(r < n and self.heap[r] > self.heap[largest]):
#                 largest = r
#             if(largest != i):
#                 self.heap[i], self.heap[largest] = self.heap[largest],self.heap[i]
#                 i = largest
#             else:
#                 break
#     def show(self):
#         print("MaxHeap: ", self.heap)

# mx=MaxHeap()
# mx. insert(10); mx. insert(4); mx. insert(7)
# mx.show()
# print("Removed: ", mx.removeMax()); mx.show()

class Heap:
    def __init__(self):
        self.heap = []
    
    def upheap(self,i):
        child = i
        parent = (i-1)//2
        while(i > 0):
            if(self.heap[child] < self.heap[parent]):
                self.heap[child] , self.heap[parent] = self.heap[parent],self.heap[child]
                i = parent
            else:
                break
    
    def downheap(self,i):
        n = len(self.heap)
        while(True):
            smallest = i
            l = 2*i + 1
            r = 2*i + 2
            if(l < n and self.heap[smallest] > self.heap[l]):
                smallest = l
            if(r < n and self.heap[smallest] > self.heap[r]):
                smallest = r
            if(smallest != i):
                self.heap[smallest] , self.heap[i] = self.heap[i] ,self.heap[smallest]
                i = smallest
            else:
                break

    def insert(self,val):
        self.heap.append(val)
        self.upheap(len(self.heap)-1)
    
    def minVal(self):
        out = self.heap[0]
        self.heap[0],self.heap[-1] = self.heap[-1],self.heap[0]
        self.heap.pop()
        self.downheap(0)
    

    def heapify(self, arr):
        self.heap = arr[:]
        n = len(self.heap)
        for i in range((n // 2) - 1, -1, -1):
            self.downheap(i)
    
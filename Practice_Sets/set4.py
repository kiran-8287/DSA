# class TaskManager:
#     def __init__(self):
#         self.heap = []

#     def upheap(self, i):
#         while i > 0:
#             parent = (i - 1) // 2
#             if self.heap[i][0] < self.heap[parent][0]:
#                 self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
#                 i = parent
#             else:
#                 break

#     def downheap(self, i):
#         n = len(self.heap)
#         while True:
#             smallest = i
#             l = 2 * i + 1
#             r = 2 * i + 2
#             if l < n and self.heap[l][0] < self.heap[smallest][0]:
#                 smallest = l
#             if r < n and self.heap[r][0] < self.heap[smallest][0]:
#                 smallest = r
#             if smallest != i:
#                 self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
#                 i = smallest
#             else:
#                 break

#     def add_task(self, priority, description):
#         node = (priority, description)
#         self.heap.append(node)
#         self.upheap(len(self.heap) - 1)

#     def execute_task(self):
#         if self.heap == []:
#             return None
#         root = self.heap[0]
#         last = self.heap.pop()
#         if self.heap != []:
#             self.heap[0] = last
#             self.downheap(0)
#         return root

#     def peek_next_task(self):
#         return self.heap[0] if self.heap else None

#     def show_tasks(self):
#         for task in self.heap:
#             print(task)
#         print()

#     def change_priority(self, description, new_priority):
#         found = False
#         for i in range(len(self.heap)):
#             if self.heap[i][1] == description:
#                 self.heap[i] = (new_priority, description)
#                 self.upheap(i)
#                 self.downheap(i)
#                 found = True
#                 break
#         if not found:
#             print("Not Found")

#     def get_task_count(self):
#         return len(self.heap)


# def test_taskmanager():
#     tm = TaskManager()
#     tm.add_task(3, "Complete assignment")
#     tm.add_task(1, "Fix server bug")
#     tm.add_task(2, "Prepare presentation")

#     print("All Tasks:")
#     tm.show_tasks()

#     print("\nNext Task:")
#     print(tm.peek_next_task())

#     print("\nExecuting Task:")
#     print(tm.execute_task())
#     tm.show_tasks()

#     print("\nChanging priority of 'Complete assignment' to 0...")
#     tm.change_priority("Complete assignment", 0)
#     tm.show_tasks()

#     print("\nTotal tasks in system:", tm.get_task_count())


# test_taskmanager()


# l = ["apple", "banana", "mango"]
# for i,fruit in enumerate(l):
#     print(f"{i}, {fruit}")
#     print()
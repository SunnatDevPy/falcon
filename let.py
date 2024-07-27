# from collections import deque
#
# # class Stack:
# #     def __init__(self):
# #         self.stack = deque
# #         self.stack_size = 0
# #
# #     def empty(self) -> bool:
# #         return not self.stack_size
# #
# #     def size(self):
# #         return self.stack_size
# #
# #     def peek(self):
# #         return self.stack[-1]
# #
# #     def pop(self):
# #         if not self.empty():
# #
# #             return self.stack.pop()
# #
# #     def push(self, value):
# #         self.stack_size += 1
# #         self.stack.append(value)
#
# # s = Stack()
# # s.push(1)
# # print(s.empty())
#
# # from queue import Queue
# #
# # s = Queue()
# #
# # class MyQueue:
# #     def __init__(self, maxsize=None):
# #         self.maxsize = maxsize
# #         self.queue = []
# #         self.q_size = 0
# #
# #     def empty(self):
# #         return not self.q_size == 0
# #
# #     def size(self):
# #         return self.q_size
# #
# #     def bottom(self):
# #         if self.q_size:
# #             return self.queue[0]
# #         raise Exception('Queue is empty')
# #
# #     def get_(self):
# #         if not self.empty():
# #             self.q_size -= 1
# #             return self.queue.pop(0)
# #         else:
# #             return 'List bosh'
# #
# #     def put(self, value):
# #         if self.size() != self.maxsize:
# #             self.q_size += 1
# #             self.queue.append(value)
# #         else:
# #             print('Queue is full')
# #
# #
# # q = MyQueue(5)
# # q.put(1)
# # q.put(1)
# # q.put(1)
# # q.put(1)
# # q.put(1)
#
#
# # q.get_()
# # q.get_()
#
# # print(q.size())
# # print(q.empty())
#
#
# '==================== LinkedList ==========================='
#
#
# # class Node:
# #     def __init__(self, data, next=None):
# #         self.data = data
# #         self.next = next
# #
# # numbers = range(1, 100)
# #
# # head = Node(numbers[0], None)
# # tmp = head
# # for number in numbers[1:]:
# #     tmp.next = Node(number)
# #     tmp = tmp.next
# ## a = [1, 2, 2, 2, 3, 4, 5, 5, 6, 7]
# # b = [2, 3, 3, 4, 5, 6]
# # l = []
# #
# # i = 0
# from typing import Optional
#
#
# # while i < len(a):
# #     if a[i] < b[i] and len(b) <= i:
# #         l.append(a[i])
# #     else:
# #         if len(b) >= i:
# #             continue
# #         l.append(b[i])
# #     i += 1
#
# # for i in range(len(b)):
# #     for j in range(len(a)):
# #         if j > i:
# #             l.append(j)
# #             continue
# #
# #
# #
# #
# # print(l)
#
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
#
# class Solution:
#     def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         new_list = ListNode()
#         tmp = head
#         while tmp.next:
#             sum_ = 0
#             if tmp.val == 0:
#                 new_list.next = sum_
#                 sum_ = 0
#             sum_ += tmp.val
#             tmp.next
#         return new_list
#
# # tmp = head
# # while tmp:
# #     print(tmp.data)
# #     tmp = tmp.next
#
# # n1 = Node(1)
# # n2 = Node(2)
# # n3 = Node(3)
# # n4 = Node(4)
# #
# # n1.next = n2
# # n2.next = n3
# # n3.next = n4
# # head = n1
# #
# #
# # while n1:
# #     print(n1.data)
# #     n1 = n1.next
# #
# # n1 = head
# # while n1:
# #     print(n1.data)
# #     n1 = n1.next
#
# class Node:
#     def __init__(self, data=None, next=None):
#         self.data = data
#         self.next = next
#
#
# class LinkedList:
#     def __init__(self):
#         self.head = Node()
#
#     def append(self, data):
#         new_node = Node(data)
#         tmp = self.head
#         while tmp.next is not None:
#             tmp = tmp.next
#         tmp.next = new_node
#
#     def pop(self):
#         tmp = self.head
#
#     def size(self):
#         return self.head.next.data
#
#     def insert(self, data):
#         pass
#
#     def show(self):
#         tmp = self.head.next
#         while tmp:
#             print(tmp.data)
#             tmp = tmp.next
#
#     def remowe_(self, value):
#         tmp = self.head.next
#         while tmp.next:
#             if tmp.data == value:
#                 tmp.next = tmp.next.next
#             tmp = tmp.next
#
#
# l = LinkedList()
#
# l.append(1)
# l.append(2)
# l.append(3)
# l.append(4)
# l.append(5)
# l.append(6)
# l.remowe_(3)
# l.show()


# l = [1,2,3,4]
# l[1:3] = [
# 0,0,0]
# print(l)

# listma = list(map(lambda x:x**2, l))
# print(listma)





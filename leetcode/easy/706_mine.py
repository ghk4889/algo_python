# 706. Design HashMap
# Design a HashMap without using any built-in hash table libraries.

# Implement the MyHashMap class:
#
# MyHashMap() initializes the object with an empty map.
# void put(int key, int value) inserts a (key, value) pair into the HashMap.
# If the key already exists in the map, update the corresponding value.
# int get(int key) returns the value to which the specified key is mapped,
#   or -1 if this map contains no mapping for the key.
# void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.
import collections


class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(ListNode)

    def put(self, key: int, value: int) -> None:
        index = key % self.size
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
            return

        p = self.table[index]

        while p:
            if p.key == key:
                p.value = value
                return
            if not p.next:
                p.next = ListNode(key, value)
                return
            p = p.next

    def get(self, key: int) -> int:
        idx = key % self.size
        node = self.table[idx]

        while node and node.key != key:
            node = node.next

        if not node:
            return -1

        return node.value

    def remove(self, key: int) -> None:
        idx = key % self.size
        node = prev = self.table[idx]

        # 첫 번째 노드를 삭제할 경우
        if node.key == key:
            self.table[idx] = ListNode() if node.next is None else node.next

        while node and node.key != key:
            prev = node
            node = node.next

        if not node:
            return

        prev.next = node.next
        node = None

        return

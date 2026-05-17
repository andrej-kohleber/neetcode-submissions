"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
            if not head:
                return None
        
            nodes = {}
            node = head
            while node:
                nodes[node] = Node(node.val, None, None)
                node = node.next

            node = head
            while node:
                if node.next:
                    nodes[node].next = nodes[node.next]
                if node.random:
                    nodes[node].random = nodes[node.random]
                node = node.next

            return nodes[head]
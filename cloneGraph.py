"""
BFS Approach
TC - O(V + E)
SC - O(V)
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None: return None

        q = deque([])
        hMap = {}

        def clone(node, hMap):
            if node in hMap:
                return hMap[node]
            clonednode = Node(node.val)
            # add too hMap
            hMap[node] = clonednode
            return clonednode

        # create copy node
        # clone(Node(1), hMap)
        copyNode = clone(node, hMap)
        # q = [[1]]
        q.append(node)

        while q:
            # currNode = 1
            # currNode = 2
            currNode = q.popleft()
            # clonedNode =  1'
            # clonedNode =  2'
            clonedNode = clone(currNode, hMap)

            # neighbor = [2, 4]
            # neighbor = [1, 3]
            for neighbor in currNode.neighbors:
                if neighbor not in hMap:
                    # q = [[Node(2), Node(4)]]
                    # Node(1) already in hMap, therefore --> # q = [[Node(4), Node(3)]]
                    q.append(neighbor)

                # create clone of the neighbor
                # 2', 4'
                # 3'
                clonedNeighbor = clone(neighbor, hMap)
                # 1'.append(2', 4')
                # 2'.append(1', 3')
                clonedNode.neighbors.append(clonedNeighbor)
        # 1' is the head of the copyNode
        return copyNode
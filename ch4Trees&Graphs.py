# cracking the coding interview
# chapter 4 trees and graphs

# interview questions
import collections


class bst_node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, data):
        # return False because you don't want duplicates
        if self.data == data:
            return False
        elif self.data > data:
            if self.left:
                return self.left.insert(data)
            else:
                self.left = bst_node(data)
                return True
        else:
            if self.right:
                return self.right.insert(data)
            else:
                self.right = bst_node(data)
                return True

    def find(self, data):
        if self.data == data:
            return True
        elif self.data > data:
            if self.left:
                return self.left.find(data)
            else:
                return False
        else:
            if self.right:
                return self.right.find(data)
            else:
                return False

    def preorder(self):
        if self:
            print(str(self.data))
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()

    def postorder(self):
        if self:
            if self.left:
                self.left.postorder()
            if self.right:
                self.right.postorder()
            print(str(self.data))

    def inorder(self):
        if self:
            if self.left:
                self.left.inorder()
            print(str(self.data))
            if self.right:
                self.right.inorder()
        
        
class Tree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = bst_node(data)
            return True
    
    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def preorder(self):
        print("Preorder")
        self.root.preorder()

    def postorder(self):
        print("Postorder")
        self.root.postorder()

    def inorder(self):
        print("Inorder")
        self.root.inorder()

# 4.1 route between nodes
# given a directed graph and 2 nodes S and E, write an algorithm that will find out if there is a path between the two nodes

    def findRoute(self, s, e):
        if s == e: return True
        
        # instantiate q and add the starting node s
        q = collections.deque()
        q.append(s)

        # indicate the state of the starting node (its in the q so it is visiting)
        s.state = visiting

        # while loop to run until the path is found or all nodes are checked (resulting in empty q)
        while q:
            # get the node at the front of the q
            c = q.popleft()
            if c != None:
                # loop through the neighbors of current node c (the nodes at the same level as c)
                for n in c.adjacent:
                    if n.state == unvisited:
                        if n == e:
                            return True
                        else:
                            # add node n to q so its neighbors will be checked
                            n.state = visiting
                            q.add(n)
                # once all of c's neighbors have been checked it has been visited (popped from q and all adjacent checked)
                c.state = visited

        return False

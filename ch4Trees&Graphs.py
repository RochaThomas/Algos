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

# 4.2 minimal tree
# given a sorted array with unique integer elements, write an algo to create a BST with minimal height
    def minimal_tree(self, array):
        """
        midpoint of the array is inserted as root
        midpoint from start to midpoint of array is root.left
        midpoint from midpoint to end of array is root.right
        """
        if array.isEmpty(): return None

        root = Node(array[len(array) / 2])
        root.left = self.minimal_tree(array[0 : (len(array) / 2) - 1])
        root.left = self.minimal_tree(array[(len(array) / 2) + 1 : len(array)])
        return root
            

# 4.3 list of depths
# given a binary tree, design an algorithm which creates a linked list of every node at each depth
    def list_of_depths(self):
        res = []

        # create a linkedlist
        curr = LinkedList(Node())
        
        if self.root != None:
            # add root to LL
            curr.add(self.root)
        
        # run while loop until there are no more children nodes
        while curr.size() > 0:
            # add prev level of tree to LL
            res.append(curr)
            # save prev level as 'parents' so you can iterate through them to get left and right (the next level)
            parents = curr
            # create new LL for the new level
            curr = LinkedList(Node())
            # iterate through parents adding left and right as the next level to the new LL
            for parent in parents:
                if parent.left != None:
                    curr.add(parent.left)
                if parent.right != None:
                    curr.add(parent.right)
        
        return res
        

# 4.4 check balanced
# implement a function to check if a binary tree is balanced (|node.left.height - node.right.height| <= 1)
    
    def check_balanced(self, root):
        def check_height(root):
            # if None return -1 (2 None nodes -> -1 - -1 = 0 as height diff)
            if root == None:
                return -1
            
            # get left height using check height
            left_height = self.check_height(root.left)
            if left_height == float("-inf"): return float("-inf")

            # get right height using check height
            right_height = self.check_height(root.right)
            if right_height == float("-inf"): return float("-inf")

            # get difference between heights
            height_diff = abs(left_height - right_height)
            # if greater than 1 return neg inf -> runs up the stack and into check_balanced function to return False
            if height_diff > 1:
                return float("-inf")
            else:
                # returning anything other than neg inf to check_balanced results in true
                return max(left_height, right_height) + 1
        return check_height(root) != float("-inf")

# 4.5 validate bst
# implement a function to check if a binary tree is a binary search tree

    def validate_bst(self):
        pass
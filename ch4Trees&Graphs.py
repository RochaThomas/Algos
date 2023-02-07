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
        def valid_bst_node(root, min, max):
            # if None return true
            if root == None:
                return True
            
            # if min is not None this means the node is on the right, right nodes must be larger than the min
            # if max is not None this means the node is on the left, left nodes must be less than the max
            # return false otherwise
            if (min != None and root.data <= min) or (max != None and root.data > max):
                return False

            # run valid bst node on both right and left of node
            if (not valid_bst_node(root.right, root.data, max) or not valid_bst_node(root.left, min, root.data)):
                return False

        return valid_bst_node(self.root, None, None)

# 4.6 successor
# write an algo to find the next node of a given node in a bst, assume each node has a link to its parent node
    def successor(self, n):
        def leftMostChild(n):
            if n == None:
                return None
            while(n.left != None):
                n = n.left
            return n

        if n == None:
            return None
        
        # if there is a right branch, return the left most child of the right branch
        if n.right != None:
            return leftMostChild(n.right)
        else:
            temp = n
            parent = temp.parent

            # work you way back up the tree, until you hit the val that comes after n
            # when the conditions are met to break the while loop you will have hit the right value
            while parent != None and parent.left != temp:
                temp = parent
                parent = parent.parent

            return parent

# 4.7 build order
# given a list of project with and a list of dependencies (which are lists of pairs of projects where the second project in the list
# is dependent on the first proj in the list), write function that will find a build order that will allow all projs to be built 
# with all their dependencies being build first. if there is no such order return None
    def build_order(self):
        """
        code here is super duper long so here's the general idea...
        get the list of dependencies and list of projects
        whatever project has 0 dependencies gets appended to the order
            then get rid of any outgoing edges from those in the order
        now any projects that were dependent on those in the order, have no dependencies and you can repreat the process
        if there aren't anymore projects with 0 dependencies but there are still more projects to be done return False

        you can also use DFS
        choose a node and run until the children nodes are None. this means you are at the end and nothing depends on these
        to be built so these can be built last. append to the end of the order
        the parent of these children must come before the children so add those before the children in the order
        if you detect a cylce return False
        """
        
        pass

# 4.8 First Common Ancestor
# make an algo that finds the first common ancestor of two nodes in a binary tree

    def first_common_ancestor(self, n1, n2):
        """
        solution if the nodes have links to their parents
            one way is to traverse up the tree from the two nodes and see where they meet
                this is implemented like the algo find_intersection of two linked lists
            another way is to traverse up the tree for on node and at each parent node, check if the parent node has
            the second node in its tree

        solution if the nodes do not have link to their parents
            one solution
                see where the nodes are as you traverse down the tree, 
                if they are on same branch then shift to that branch and search again
                if they are on opposite branches then you have found the first common ancestor
            another solution
                in the above solution, multiple subtree are searched over and over
                we can use a recursive function that bubbles up whether or not n1 and n2 exist in a branch
                return n1 if roots subtree includes n1 but not n2
                return n2 if roots subtree includes n2 but not n1
                return null if neither are there
                else return the lowest common ancestor

                running the recursive function on the left and right will return the lca when the two calls return non null values
        """
        pass

# 4.9 bst sequences
# given a bst, print all possible arrays that could have led to this bst given that the bst was implemented 
# by traversing through an array from left to right

    def bst_sequences(self):
        """
        maybe look for a video for the python code for this
        a little hard to follow
        but the basic idea is by implementing 2 recursive functions
        we know that after the root node is inserted, root.left and root.right can be inserted in any order
        thus it follows that the sequences can be generated by weaving the left and right arrays as long as the
        root nodes are inserted before root.left and root.right
        add the next node up in the tree to the sequence by prepending the sequences that were generated by weaving

        one function weaves the left and right array sequences such that the parent nodes are always added before the child nodes
            give [1, 2, 3] and [4, 5, 6], 1 will always be added before 2 and 3. in the same way, 4 will alwasy be added before 5 and 6
            4 and all of the nodes after 4 maybe added before 1 because 4+ would all be larger than 4's parent
            and 1-3 would all be smaller than 1 and 4's parent so the two branches would not interfere with each other as they are added
            from left to right

            likewise 1-3 can all be added before 4+
            
            essentially the new generated weaved array will still have 1 appear before 2 and 2 before 3
                4 before 5 and 5 before 6
        another function prepends the sequences with the next node up the tree
        """
        pass

# 4.10 check subtree
# t1 and t2 are large binary trees with t1 >>>> t2. create an algo to determine if t2 is a subtree of t1
    def check_subtree(self, t1, t2):
        pass
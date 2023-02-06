# cracking the coding interview
# chapter 4 trees and graphs

# interview questions
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
# 
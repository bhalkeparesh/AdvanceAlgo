from Crypto.Hash import SHA256
from collections import namedtuple


"""Rules: 
1. Every black node must have red node children. 
2. The distance from a node to its descendents has a uniform number of black nodes
3. All leaves are black
4. The root of the tree is black
5. If it's your first time at Fight Club you have to fight
"""

def preorder_traversal(node, func=None):
    if func:
        func(node.value)
    preorder_traversal(node.left)
    preorder_traversal(node.right)

def check_if_red(node):
    return node != None and node.color == "R"

class RedBlackNode:
    def __init__(self, value, color="B"):
        self.parent = None
        self.color = None
        self.right = None
        self.left = None
        self.value = value
        self.digest = None

class NilNode(RedBlackNode):
  __instance__ = None

  @classmethod
  def instance(self):
    if self.__instance__ is None:
      self.__instance__ = NilNode()
    return self.__instance__

  def __init__(self):
    self.color = 'B'
    self.value = None
    self.left = self.right = self.parent = None

  def __nonzero__(self):
    return False

  def __bool__(self):
    return False



class RedBlackTree:
    def __init__(self):
        self.root = NilNode.instance()

    def insert_helper(self, z):
        y = NilNode.instance()
        x = self.root
        while x:
            y = x
            if z.value < x.value:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if not y:
            self.root = z
        else:
            if z.value < y.value:
                y.left = z
            else:
                y.right = z
        
    def check_violations(self):
        """Goes through tree and checks that all of the rules for RB are followed"""
        pass
    
    def recolor(self, node, color):
        pass

    def rotateLeft(self, root):
        newRoot = root.right
        #Root takes its right childs left node
        root.right = newRoot.left
        #Set parent as root
        if newRoot.left != None:
            newRoot.left.parent = root
        #new root sets parent as root
        newRoot.parent = root.parent
        if newRoot.parent == None:
            pass
        elif root.parent.left == root:
            newRoot.parent.left = newRoot
        else:
            newRoot.parent.right = newRoot
        # Set new roots left child as root
        newRoot.left = root
        # Set old roots parent as newRoot
        root.parent = newRoot

    def rotateRight(self, root):
        newRoot = root.left
        root.left = newRoot.right
        if newRoot.right != None:
            newRoot.right.parent = root
        newRoot.parent = root.parent
        if newRoot.parent == None:
            pass
        elif root.parent.right == root:
            newRoot.parent.right = newRoot
        else:
            newRoot.parent.left = newRoot
        newRoot.right = root
        root.parent = newRoot

    def insert(self, node):
        self.insert_helper(node)
        if self.root == None:
            node.color = 'B'
            self.root = node
            return
        node.color = 'R'
        while node != self.root and node.parent.color == 'R':
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle and uncle.color == 'R':
                    node.parent.color = 'B'
                    uncle.color = 'B'
                    node.parent.parent.color = 'R'
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.rotateLeft(node)
                    node.parent.color = 'B'
                    node.parent.parent.color = 'R'
                    self.rotateRight(node.parent.parent)
            else:
                u = node.parent.parent.left
                if node and node.color == 'R':
                    node.parent.color = 'B'
                    u.color = 'B'
                    node.parent.parent.color = 'R'
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.rotateRight(node)
                    node.parent.color = 'B'
                    node.parent.parent.color = 'R'
                    self.rotateLeft(node.parent.parent)
        self.root.color = 'B'


if __name__ == "__main__":
    rb = RedBlackTree()
    rb.insert(RedBlackNode(5))
    print(rb.root.value)
    rb.insert(RedBlackNode(10))
    print(rb.root.right.value)

# Author: Troy Schotter
# Date: Jan 23rd, 2026
# starting point of the file
# Assignment name: in class code

from BinaryTree import Node, BinaryTree

# create a new class that inherits from Node
# don't do this for the hw, just create a Node class
# that already has left and right
class BNode(Node):
    # override Node __init__
    def __init__(self, data):
        super(data)
        self.left = None
        self.right = None

def main():
    print("Hello World")

    BTree = BinaryTree()
    # create a Node
    x = Node(10)
    # create another Node
    y = Node(30)
    print(x) #prints "data" of x

    # kick off the recursion for the print
    BTree.inorder_print(BTree.head)

if __name__ == "__main__":
    main()
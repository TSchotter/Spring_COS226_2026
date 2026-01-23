class Node:
    # init function (the contructor)
    # all methods in a class need to have
    # "self" as a parameter
    # self is used to refer to the obj
    # you are creating
    def __init__(self, data):
        # internal variable "data" is
        # set to the parameter "data"
        self.data = data
    #override the how the obj is treated as a string
    def __str__(self):
        # return our data, as a string
        # return str(self.data)
        return f"[{self.data}]"
    
class BinaryTree:
    #initialize Tree
    def __init__(self):
        # we have no nodes yet in the tree
        self.head = None

    def add(self, data):
        
        pass # used as a placehold so you can have blank function

    def inorder_print(self, node):
        if node == None: # stops the recursion
            return
        # prints all nodes, in order
        pass
    def preorder_print(self, node):
        # prints all nodes, pre order
        pass
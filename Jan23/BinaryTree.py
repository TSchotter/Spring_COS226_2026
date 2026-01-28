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
        # if it's not in the tree, we will add.

        newNode = Node(data)
        if (self.head == None):
            # tree doesn't have a head node
            self.head = newNode
            return # done, time to leave

        # traverse the tree until we find the correct spot
        curNode = self.head # set pointer to look at start
    

        # loop until we find spot. 
        # we will want the loop to end when we insert the new node
        # or, when we run into the same data that we want to add

        # if newNode data is the same as the data of curNode
        #  leave loop
        # curNode.data == newNode.data <- condition

        # do I want to look left, or right.
        # thing to add < what we're looking at
        #  newNode.data < curNode.data

        # is there something there in that direction?
        #   left side ver.
        #  curNode.left is None, or !None

        # if there is nothing there, place the node
        # curNode.left = newNode
        # we're done, leave the loop

        # if there IS something there,
        # traverse left.
        # move the pointer to the left
        # curNode = curNode.left
        # start the loop again

        pass # used as a placehold so you can have blank function

    def inorder_print(self, node):
        if node == None: # stops the recursion
            return
        # prints all nodes, in order
        pass
    def preorder_print(self, node):
        # prints all nodes, pre order
        pass
from binaryTree import BinaryTree, Node, TreeVisualizer

# create AVL tree class inheriting 
# BinaryTree
class AVLTree(BinaryTree):

    # overwrite the add
    def add(self, curNode, data):
        if self.head == None:
            self.head = Node(data)
            return
        
        # curNode is our current spot
        # recursive termination
        if curNode == None:
            # create Node, height of new nodes is 1 already
            return Node(data)
        
        # curNode is a Node if we get here

        # check if curNode is same data
        if curNode.data == data:
            # make no change, iterate back up
            return curNode
        
        if data < curNode.data:
            # set the left to the result of add
            curNode.left = self.add(curNode.left, data)
        else:
            curNode.right = self.add(curNode.right, data)
        # check balance
        

        # left and/or height might not exists
        if curNode.left == None:
            leftHeight = 0
        else:
            leftHeight = curNode.left.height
        if curNode.right == None:
            rightHeight = 0
        else:
            rightHeight = curNode.right.height

        # a new Node was added, we need to update height
        curNode.height = max(leftHeight, 
                             rightHeight)+1
        # past recursion calls are expecting this
        return curNode

visualizer = TreeVisualizer()

tree = AVLTree()
tree.add(tree.head, 10)
tree.add(tree.head,20)
tree.add(tree.head,70)
tree.add(tree.head,30)
tree.add(tree.head,40)
tree.add(tree.head,1)
# add tree to visualizer snapshot
visualizer.add_to_stack(tree)
#show the visualizer
visualizer.visualize()
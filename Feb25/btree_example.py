from btree_visualizer import Tree, TreeVisualizer, Bucket, DataItem


treevisualizer = TreeVisualizer()

class BucketNode(Bucket):

 
    def add(self, item, leftLink = None):
        
        pass

    def remove(self, key):
        pass

class BTree(Tree):
    def add(self, key, value):
        pass

    def remove(self, key):
        pass

    def search(self, key):
        pass

    def split_leaf_node(self, node):
        pass

    def split_internal_node(self, node):
        pass

    def steal(self, node, direction):
        pass

    def merge(self, leftNode, rightNode):
        pass

def main():
    print("B+ Tree Example")

    maxdegree = 5

    # create a tree with a max degree of 5
    tree = BTree(maxdegree)

    treevisualizer.add_to_stack(tree)


    tree.root = BucketNode(maxdegree)

    # Not an accurate B or B+ tree, just a visual example. Also not the way you should add the nodes
    tree.root.keys = [50, 100]
    tree.root.is_leaf = False
    tree.root.links = [None, None, None]
    tree.root.links[0] = BucketNode(maxdegree)
    tree.root.links[0].keys = [25, 45]
    tree.root.links[1] = BucketNode(maxdegree)
    tree.root.links[1].keys = [55, 95]
    tree.root.links[2] = BucketNode(maxdegree)
    tree.root.links[2].keys = [120, 140]
    treevisualizer.add_to_stack(tree) # Data doesn't exist in this tree, only the keys.

    # manually setting these internal nodes to not be considered leaf nodes.
    tree.root.links[0].links = [None, None, None]
    tree.root.links[0].is_leaf = False
    tree.root.links[1].links = [None, None, None]
    tree.root.links[1].is_leaf = False
    tree.root.links[2].links = [None, None, None]
    tree.root.links[2].is_leaf = False

    # manually filling the leaf nodes with data.
    tree.root.links[0].links[0] = BucketNode(maxdegree)
    tree.root.links[0].links[0].keys = [DataItem(0, "Alice"), DataItem(10, "Bob"), DataItem(15, "Charlie")]
    tree.root.links[0].links[1] = BucketNode(maxdegree)
    tree.root.links[0].links[1].keys = [DataItem(30, "Diana"), DataItem(35, "Eve"), DataItem(38, "Frank")]
    tree.root.links[0].links[2] = BucketNode(maxdegree)
    tree.root.links[0].links[2].keys = [DataItem(46, "Grace"), DataItem(48, "Henry")]

    tree.root.links[1].links[0] = BucketNode(maxdegree)
    tree.root.links[1].links[0].keys = [DataItem(52, "Ivy"), DataItem(54, "Jack")]
    tree.root.links[1].links[1] = BucketNode(maxdegree)
    tree.root.links[1].links[1].keys = [DataItem(56, "Kate"), DataItem(58, "Liam")]
    tree.root.links[1].links[2] = BucketNode(maxdegree)
    tree.root.links[1].links[2].keys = [DataItem(97, "Maya"), DataItem(99, "Noah")]

    tree.root.links[2].links[0] = BucketNode(maxdegree)
    tree.root.links[2].links[0].keys = [DataItem(112, "Olivia"), DataItem(114, "Paul")]
    tree.root.links[2].links[1] = BucketNode(maxdegree)
    tree.root.links[2].links[1].keys = [DataItem(126, "Quinn"), DataItem(128, "Ruby")]
    tree.root.links[2].links[2] = BucketNode(maxdegree)
    tree.root.links[2].links[2].keys = [DataItem(142, "Sam"), DataItem(144, "Tina")]


    # manually setting the next pointers for the leaf nodes.
    tree.root.links[0].links[0].next = tree.root.links[0].links[1]
    tree.root.links[0].links[1].next = tree.root.links[0].links[2]
    tree.root.links[0].links[2].next = tree.root.links[1].links[0]
    tree.root.links[1].links[0].next = tree.root.links[1].links[1]
    tree.root.links[1].links[1].next = tree.root.links[1].links[2]
    tree.root.links[1].links[2].next = tree.root.links[2].links[0]
    tree.root.links[2].links[0].next = tree.root.links[2].links[1]
    tree.root.links[2].links[1].next = tree.root.links[2].links[2]
    
    treevisualizer.add_to_stack(tree) # now data exists in the tree.

    treevisualizer.visualize()


if __name__ == "__main__":
    main()
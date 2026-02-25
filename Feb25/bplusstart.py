#import the visualizer
from btree_visualizer import *

class BBucket(Bucket):
    pass

# inherit from Tree in visualizer
class BTree(Tree):
    # when adding to the tree,
    # send an entire DataItem
    def add(self, newDataItem):

        # find right bucket for newDataItem

        if self.root == None:
            # very first piece of data, create new root
            self.root = BBucket(self.maxdegree)
            self.root.keys.append(newDataItem)
            # leaf buckets don't have lists
            return # done
        
        # goal = reach the bottom
        curBucket = self.root
        # if we're at an internal node, keep going down
        while(curBucket.is_leaf == False):
            # find correct index for links, 
            # by looking at the keys
            targetIndex = 0
            for i in curBucket.keys:
                if i > newDataItem.key:
                    # we found the path to travel,
                    # stop looking
                    break
                targetIndex += 1
            # now targetIndex is the correct index
            curBucket = curBucket.links[targetIndex]

        # We're now at the correct leaf bucket
        curBucket.add(DataItem) # let bucket handle it's own add
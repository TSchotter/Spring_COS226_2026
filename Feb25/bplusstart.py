#import the visualizer
from btree_visualizer import *

class BBucket(Bucket):
    # add function will work for internal and leaf buckets
    def add(self, item, leftLink = None):
        if (self.is_leaf):
            # "item" is a DataItem
            self.leaf_add(item)
        else:
            # this will only be called as a result of a split,
            # "item" is an integer, not an entire DataItem
            # leftLink is the link to the new bucket created from split
            self.internal_add(item, leftLink)
    def leaf_add(self, newItem):
        # find right spot in self.keys, and insert newItem to that spot

        # [You do this]

        # return size of the keys, so that the tree can decide if it
        # needs to split
        return len(self.keys)
        
    def internal_add(self, key, leftLink):
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
        size = curBucket.add(newDataItem) # let bucket handle it's own add
        
        # check if bucket is too big
        if size >= self.maxdegree:
            # a leaf bucket (curBucket) is too big
            #  and we need to... split

            self.leaf_split(curBucket)
    
    # called when we need to split a leaf bucket
    def leaf_split(self, curBucket):

        # create new left bucket
        leftBucket = BBucket(self.maxdegree)
        # fix all prev and next's
        leftBucket.next = curBucket
        leftBucket.prev = curBucket.prev
        curBucket.prev = leftBucket
        if leftBucket.prev:
            leftBucket.prev.next = leftBucket
        
        middle = self.maxdegree//2 # middle floored
        leftBucket.keys = curBucket.keys[:middle] # pulls index 0,1
        curBucket.keys = curBucket.keys[middle:] # pulls index 2,3,4

        if curBucket.parent == None:
            # if the bucket has no parent, it's the root

            # create new internal bucket
            self.root = BBucket(self.maxdegree)
            self.root.is_leaf = False
            # place 0 index of right bucket into new internal bucket
            self.root.keys = [curBucket.keys[0]]
            # set up links
            self.root.links = [leftBucket, curBucket]
            # set leaf bucket parent properties
            curBucket.parent = self.root
            leftBucket.parent = self.root
        else:
            # we have a parent (we're not the root)
            leftBucket.parent = curBucket.parent

            # hand the parent the new key, and the link to the new bucket
            size = curBucket.parent.add(curBucket.keys[0].key, leftBucket)
            if size >= self.maxdegree:
                self.internal_split(curBucket.parent)

    # called when we need to split an internal bucket
    def internal_split(self, curBucket):
        pass
        
import time
import random

def bubbleSort(x):
    for i in range(len(x)):
        didSwap = False
        for j in range(len(x)-1-i): # run one and i less time
            if x[j] > x[j+1]: # left bigger than right
                # swap
                x[j], x[j+1] = x[j+1], x[j]
                didSwap = True
        if not didSwap: # did not swap, leave early
            return

def selectionSort(x):
    for i in range(len(x)-1):

        smallest = i # smallest number at index we've seen
        for j in range(i+1, len(x)): # start j at i+1
            if x[smallest] > x[j]:
                # found a smaller number
                smallest = j
        # swap i and smallest
        x[i], x[smallest] = x[smallest], x[i]

def mergeSort(x):
    # kick off the recursion
    split(x, 0, len(x)-1) # give it the full bounds of the list

def split(x, start, end):
    if (end-start) <= 0: # changed to <= 0, since <= 1 allows size 2 arrays to return early
        return

    middleIndex = (end-start)//2 + start
    split(x, start, middleIndex) # left side
    split(x, middleIndex+1, end) # right

    merge(x, start, middleIndex, end)

def merge(x, start, middle, end):
    left = x[start:middle+1]  # makes memory complexity O(n)

    i = start # the next spot we fill
    l = 0  # looking at start of left array
    r = middle+1 # looking at start of right array

    while(i <= end): # continue as long as we have spots to fill
        # which value, x[l] or x[r] goes into x[i]
        if (l < len(left) and r <= end): # both l and r in in bounds
            if (x[r] < left[l]):
                x[i] = x[r] # number at "r" was the smaller
                r+=1 # look at next spot
            else:
                x[i] = left[l] # number at "l" was the smaller
                l+=1
        elif(l < len(left)): # r is out of bounds, only grab l
            x[i] = left[l]
            l+=1
        else:
            x[i] = x[r]
            r+=1 # look at next spot
        i += 1 # set target location to next spot


def quickSort(x):
    # kicks off recursion process
    quickSortRecursive(x, 0, len(x)-1)

def quickSortRecursive(x, start, end):
    if (end <= start): 
        # list is small enough that we know it's in order
        return

    p = lomutoPartition(x, start, end)

    # left half
    quickSortRecursive(x, start, p-1)

    # right half
    quickSortRecursive(x, p+1, end)


def lomutoPartition(x, start, end):
    pivot = x[end]
    i = start # i at the start
    for j in range(i, end): # j at start, to end-1
        if x[j] <= pivot: # check if we need to swap
            x[i], x[j] = x[j], x[i]
            i += 1 # increase i if we swap
    # swap i and pivot
    x[i], x[end] = x[end], x[i]

    return i # return where pivot is


def naivePartition(x, start, end):
    pivot = x[end]
    # create empty list that we fill.
    copy = []
    # find things less than pivot
    for i in range(start, end):
        # anything less than pivot, add it to "copy"
        if x[i] <= pivot:
            copy.append(x[i])

    partitionIndex = start + len(copy)        
    copy.append(pivot) # add the pivot

    # find things greater than pivot
    for i in range(start, end):
        # anything greater than pivot, add it to "copy"
        if x[i] > pivot:
            copy.append(x[i])
    
    # place all things in copy into same spot on x
    for i in range(len(copy)):
        x[start+i] = copy[i]

    # hand relevant info back up
    return partitionIndex

    # naivePartition(x, start, partitionIndex-1)
    # naivePartition(x, partitionIndex+1, end)


random.seed(0)
n = 200000

x = []

for i in range(n):
    x.append(random.randint(0,20000))


start = time.time()
quickSort(x)
print(x[100:200])
end = time.time()
print(end-start) # number of seconds difference between two
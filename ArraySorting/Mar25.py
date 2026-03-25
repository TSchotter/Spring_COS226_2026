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
    

def split(x, start, end):
    if end-start <= 1:
        return
    
    middleIndex = (end-start)//2
    split(x, start, middleIndex) # left side
    split(x, middleIndex+1, end) # right

    merge(x, start, middleIndex, end)

def merge(x, start, middle, end):
    left = x[start:middle+1]

    i = start # the next spot we fill
    l = 0  # looking at start of left array
    r = middle+1. # looking at start of right array


random.seed(0)
n = 20000

x = []

for i in range(n):
    x.append(random.randint(0,20000))


start = time.time()
selectionSort(x)
print(x[100:120])
end = time.time()
print(end-start) # number of seconds difference between two
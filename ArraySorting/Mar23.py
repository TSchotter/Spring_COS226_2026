import time
import random

random.seed(0)
n = 10000000

x = []

start = time.time()
for i in range(n):
    x.append(random.randint(0,20000))
end = time.time()

print(x[:10])
print(end-start) # number of seconds difference between two
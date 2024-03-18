import numpy as np
import sys
import time

l1 = range(1000)
print(sys.getsizeof(5) * len(l1))

array = np.arange(1000)
print(array.size * array.itemsize)


SIZE = 10000

l1 = range(SIZE)
l2 = range(SIZE)

a1 = np.arange(SIZE)
a2 = np.arange(SIZE)

print(a1)
# Python list
start = time.time()
result = [(x + y) for x, y in zip(l1, l2)]
print("Python list took", (time.time() - start) * 1000)

start = time.time()
result2 = a1 + a2
print("numpy list took", (time.time() - start) * 1000)

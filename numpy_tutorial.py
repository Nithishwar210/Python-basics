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

a = [6, 7, 8]
print("numpy ", a[1:])

a = np.array([[6, 7, 8], [1, 2, 3], [4, 5, 6]])
print("numpy ", a[1:])
print("numpy ", a[1:, 0:2])

range1 = np.arange(10000).reshape(10000, 1)
# start = time.time()
# for cell in range1.flat:
#     print("flat", cell)
# print("numpy list flat took", (time.time() - start) * 1000)
a = [6, 7, 8]
start = time.time()
for x, y in np.nditer([range1, a]):
    print('nditer', x, y)
print("numpy list flat took", (time.time() - start) * 1000)

#
# a = np.zeros(100)
# print(a)
# print(np.split(a, 4))
# a = np.array([[6, 7, 8], [1, 2, 3], [4, 5, 6]], dtype=int)
# print(np.vsplit(a, 1))
#
# arr = np.array([1, 2, 3, 4, 5])
# x = arr.view()
# y = arr.copy()
#
# arr[0] = 42
# print(x.base)
# print(y.base)
#
# np.savetxt('test.txt', a, fmt='%.0g', header='Learn mandaya')
# loaded = np.loadtxt('test.txt', dtype=int)
# print(loaded)

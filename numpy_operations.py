import numpy as np

l1 = np.array([1, 2, 3], dtype=float)
# print(l1)
# print(l1.size)
# print(l1.itemsize)

zeros = np.zeros((3, 4))
# print(zeros)
# print(np.arange(6, 10, 2))
# print(np.linspace(1, 5, 5))

twoDArr = np.array([[1, 2], [3, 4], [5, 6]])
# print(twoDArr.shape)
# print(twoDArr.reshape(3, 2))
# print(twoDArr.ravel())
# print(twoDArr.min())
# print(twoDArr.max())
# print(twoDArr.sum())
# print(twoDArr.sum(axis=0))
# print(twoDArr.sum(axis=1))
# print(np.sqrt(twoDArr))
# print(np.std(twoDArr))

# Creating a np array
npArr = np.array([1, 3, 5])
npArr2 = np.array([[1, 2], [3, 4], [5, 6]])

# Array Attributes
print(npArr2.shape)
print(npArr.size)
print(npArr2.itemsize)
print(npArr2.dtype)


# Array operation
arr3 = npArr * 5
arr4 = npArr + 2
arr5 = npArr + np.array([1, 3, 5])
arr6 = np.sin(npArr)

print("arr3", arr3)
print("arr4", arr4)
print("arr5", arr5)
print("arr6", arr6)

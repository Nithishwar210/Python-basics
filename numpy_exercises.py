import numpy
import numpy as np


# Write a Numpy program to get the Numpy version and show the Numpy build configuration.
def exercise1():
    print(np.__version__)
    # print(np.show_config())
    print(np.info(np.all))  # very useful
    arr = [1, 2, 3, 4]
    print(numpy.all(arr))


def exercise2():
    arr = np.array([[True, True], [False, True]])
    print(np.all(arr, where=[True, False], axis=1))
    array = np.array([[True, True, 0],
                      [True, True, True],
                      [True, None, True]])

    # Along axis 0 (rows)
    result_axis_0 = np.all(array, axis=0)
    print("Result along axis 0 (rows):", result_axis_0)

    # Along axis 1 (rows)
    result_axis_1 = np.all(array, axis=1)
    print("Result along axis 1 (rows):", result_axis_1)

    arr = np.array([1, 2, 0, 0])
    print('non zeros', arr != 0)
    print('non zeros any', np.any(arr))

    # isfinite & isInf
    arrInf = np.array([1, 2, np.nan, np.inf, 2.1, 1+1j])
    print("arrInf", np.isfinite(arrInf))
    print("arrInf", np.isinf(arrInf))
    print("arrInf", np.isnan(arrInf))
    print("arrInf", np.iscomplex(arrInf))
    print("arrInf", np.isreal(arrInf))
    print("arrInf", np.isscalar(arrInf))

    tolerance1 = np.array([3.0, 2.00001, 1.1], dtype=float)
    tolerance2 = np.array([3.0, 2.0, 1.1])

    print("tolerance", np.allclose(tolerance1, tolerance2, rtol=1e-04, atol=1e-08))
    print("array size", tolerance1.size * tolerance1.itemsize, tolerance1.itemsize)
    zeros = np.zeros(10, dtype=int)
    ones = np.ones(10, dtype=int)
    fives = np.ones(10, dtype=int) * 5
    print("zeros", zeros)
    print("ones", ones)
    print("fives", fives)
    print("range 30 to 70", np.arange(30, 71))
    print("range 30 to 70", np.arange(30, 71, 2))
    print("3 x 3 matrix", np.arange(9).reshape(3, 3))
    array_2D = np.identity(5) * 4
    print("array_2d", array_2D)
    print("random", np.random.normal(0, 1, 15))
    arr34 = np.arange(12).reshape(3, 4)
    print('first last others',arr34, arr34[0][1:-1])
    # for x in arr34.flat:
    #     print('x', x)

    lin = np.linspace(5, 50, 10, dtype=int)
    arrArg = np.arange(5, 51, 5)
    print("linspace", lin, arrArg)
    print("Join", np.concatenate([arr34, arr34]))


if __name__ == '__main__':
    # exercise1()
    exercise2()

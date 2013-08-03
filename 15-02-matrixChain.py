import numpy
import numpy.random
import exceptions


def matrixMultiply(x, y):
    if x.shape[1] != y.shape[0]:
        raise exceptions.ValueError("Matrices are not compatible")

    c = numpy.zeros((x.shape[0], y.shape[1]))
    for i in range(x.shape[0]):
        for j in range(y.shape[1]):
            for k in range(x.shape[1]):
                c[i, j] += x[i, k] * y[k, j]
    return c

if __name__ == "__main__":
    x = numpy.random.uniform(0, 1, (100, 30))
    y = numpy.random.uniform(0, 1, (30, 200))
    print matrixMultiply(x, y)

    x = numpy.eye(100)
    y = numpy.eye(100)
    print matrixMultiply(x, y)

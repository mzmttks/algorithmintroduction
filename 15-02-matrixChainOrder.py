import numpy


def matrixChainOrder(p):
    n = len(p) - 1
    cost = numpy.zeros((n + 1, n + 1))
    reco = numpy.zeros((n + 1, n + 1))

    for l in range(2, n + 1):  # l is a chain length
        for i in range(1, n - l + 2):
            j = i + l - 1
            cost[i, j] = numpy.infty
            for k in range(i, j):
                q = cost[i, k] + cost[k+1, j] + p[i-1] * p[k] * p[j]
                if q < cost[i, j]:
                    cost[i, j] = q
                    reco[i, j] = k

    return cost[1:, 1:], reco[1:, 1:]


def printOptimalParents(s, i, j):
    if i == j:
        print "A_%d" % (i),
    else:
        print "(",
        printOptimalParents(s, i, s[i-1, j-1])
        printOptimalParents(s, s[i-1, j-1] + 1, j)
        print ")",


if __name__ == "__main__":
    p = [30, 35, 15, 5, 10, 20, 25]
    # matrix chain of 30x35 35x15 15x5 5x10 10x20 20x25

    cost, reconst = matrixChainOrder(p)
    print cost
    print reconst
    printOptimalParents(reconst, 1, len(p)-1)

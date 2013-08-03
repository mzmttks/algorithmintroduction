import numpy


def lcsLength(x, y):
    m = len(x)
    n = len(y)

    b = [["" for i in range(n+1)] for j in range(m+1)]
    c = numpy.zeros((m+1, n+1))

    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]:
                c[i, j] = c[i-1, j-1] + 1
                b[i][j] = "lu"
            elif c[i-1, j] >= c[i, j-1]:
                c[i, j] = c[i-1, j]
                b[i][j] = "u"
            else:
                c[i, j] = c[i, j-1]
                b[i][j] = "l"
    return c, b


def printLcs(b, x, i, j):
    print "-" + x[i-1]
    if i == -1 or j == -1:
        return

    if b[i-1][j-1] == "lu":
        printLcs(b, x, i-1, j-1)
        print x[i], x, i-1
    elif b[i-1][j-1] == "u":
        printLcs(b, x, i-1, j)
    else:
        printLcs(b, x, i, j-1)

if __name__ == "__main__":
    x = "abcbdab"
    y = "bdcaba"
    c, b = lcsLength(x, y)
    printLcs(b, x, len(x), len(y))

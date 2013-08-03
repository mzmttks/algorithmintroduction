import numpy
import numpy.random


def cutrod(table, n):
    if n == 0:
        return 0
    q = -numpy.infty
    for i in range(1, n+1):
        q = max(q, table[i] + cutrod(table, n-i))
    return q

if __name__ == "__main__":
    table = {1:  1, 2:  5, 3:  8, 4:  9,  5: 10,
             6: 17, 7: 17, 8: 20, 9: 24, 10: 30}
    print cutrod(table, 10)

    for sticklen in [3, 10, 100, 1000]:
        table = zip(range(1, sticklen+1),
                    [numpy.random.randint(100) for i in range(sticklen)])
        table = dict(table)
        print table
        print cutrod(table, sticklen)

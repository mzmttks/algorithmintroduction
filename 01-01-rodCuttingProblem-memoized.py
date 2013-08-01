import numpy
import numpy.random


def memoizedCutrod(table, n):
    memo = {}
    for i in range(0, n+1):
        memo[i] = -numpy.infty
    return memoizedCutrodAux(table, n, memo)


def memoizedCutrodAux(table, n, memo):
    if memo[n] >= 0:
        return memo[n]
    if n == 0:
        q = 0
    else:
        q = -numpy.infty
        for i in range(1, n+1):
            q = max(q, table[i] + memoizedCutrodAux(table, n-i, memo))
    memo[n] = q
    return q

if __name__ == "__main__":
    table = {1:  1, 2:  5, 3:  8, 4:  9,  5: 10,
             6: 17, 7: 17, 8: 20, 9: 24, 10: 30}
    print memoizedCutrod(table, 10)

    for sticklen in [3, 10, 100, 300]:
        table = zip(range(1, sticklen+1),
                    [numpy.random.randint(100) for i in range(sticklen)])
        table = dict(table)
        print table
        print memoizedCutrod(table, sticklen)

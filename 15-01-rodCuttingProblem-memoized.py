import numpy
import numpy.random


def memoizedCutrod(table, n):
    memo = {}
    for i in range(0, n+1):
        memo[i] = -numpy.infty

    s = {}
    for i in range(1, n+1):
        s[i] = -numpy.infty
    s[0] = 0

    best = memoizedCutrodAux(table, n, memo, s)
    return best, s


def memoizedCutrodAux(table, n, memo, s):
    if memo[n] >= 0:
        return memo[n]
    if n == 0:
        q = 0
    else:
        q = -numpy.infty
        for i in range(1, n+1):
            if q < table[i] + memoizedCutrodAux(table, n-i, memo, s):
                q = table[i] + memoizedCutrodAux(table, n-i, memo, s)
                s[n] = i
    memo[n] = q
    return q

if __name__ == "__main__":
    table = {1:  1, 2:  5, 3:  8, 4:  9,  5: 10,
             6: 17, 7: 17, 8: 20, 9: 24, 10: 30}
    best, reconst = memoizedCutrod(table, 10)
    for key in sorted(table.keys()):
        print "%3d %3d %3d" % (key, table[key], reconst[key])

    for sticklen in [3, 10, 100, 300]:
        table = zip(range(1, sticklen+1),
                    [numpy.random.randint(100) for i in range(sticklen)])
        table = dict(table)
        memoizedCutrod(table, sticklen)

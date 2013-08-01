import numpy
import numpy.random


def bottomupCutrod(table, n):
    memo = {}
    for i in range(1, n+1):
        memo[i] = -numpy.infty
    memo[0] = 0

    for j in range(1, n+1):
        q = -numpy.infty
        for i in range(1, j+1):
            q = max(q, table[i] + memo[j-i])
        memo[j] = q
    return memo[n]


def bottomupCutrodReconstruction(table, n):
    memo = {}
    for i in range(1, n+1):
        memo[i] = -numpy.infty
    memo[0] = 0

    s = {}
    for i in range(1, n+1):
        s[i] = -numpy.infty
    s[0] = 0

    for j in range(1, n+1):
        q = -numpy.infty
        for i in range(1, j+1):
            if q < table[i] + memo[j-i]:
                q = table[i] + memo[j-i]
                s[j] = i
        memo[j] = q
    return memo[n], s


if __name__ == "__main__":
    table = {1:  1, 2:  5, 3:  8, 4:  9,  5: 10,
             6: 17, 7: 17, 8: 20, 9: 24, 10: 30}
    print bottomupCutrod(table, 10)
    result, reconst = bottomupCutrodReconstruction(table, 10)

    for key in sorted(table.keys()):
        print "%3d %3d %3d" % (key, table[key], reconst[key])

    # for sticklen in [3, 10]:
    #     table = zip(range(1, sticklen+1),
    #                 [numpy.random.randint(100) for i in range(sticklen)])
    #     table = dict(table)
    #     print table
    #     print bottomupCutrod(table, sticklen)
    #     print bottomupCutrodReconstruction(table, sticklen)

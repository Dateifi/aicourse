def printPat(n):
    res = ''
    for i in range(n, 0, -1):
        _n = n
        while _n > 0:
            for j in range(i):
                res += str(_n) + ' '
            _n -= 1
        res += '$'
    print(res)


n = int(input())
printPat(n)

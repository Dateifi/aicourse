from collections import deque


def solution(M, F):
    M, F = int(M), int(F)
    moves = 0
    if M == 1:
        return str(moves + F - 1)
    elif F == 1:
        return str(moves + M - 1)
    elif M % 2 == 0 and F % 2 == 0:
        return "impossible"
    elif M % F == 0 or F % M == 0:
        return "impossible"
    while M != 1 and F != 1:
        if M > F:
            moves += M // F
            M = M % F
        else:
            moves += F // M
            F = F % M
    return str(moves + M + F - 2)


print(solution("15", "3"))

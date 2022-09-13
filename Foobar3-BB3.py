def solution(M, F):
    M, F = int(M), int(F)
    moves = 0
    while M > 1 and F > 1:
        if M > F:
            moves += M // F
            M = M % F
        else:
            moves += F // M
            F = F % M
    if M < 1 or F < 1:
        return "impossible"

    return str(moves + M + F - 2)


print(solution("2", "1"))

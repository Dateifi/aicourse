from collections import deque


def solution(M, F):
    M, F = int(M), int(F)
    queue = deque([(1, 1)])
    visited = set()
    moves = 0
    if M == 1:
        return str(moves + F - 1)
    elif F == 1:
        return str(moves + M - 1)
    elif M % 2 == 0 and F % 2 == 0:
        return "impossible"
    elif M % F == 0 or F % M == 0:
        return "impossible"

    while queue:
        for _ in range(len(queue)):
            current = queue.popleft()
            if current == (M, F) or current == (F, M):
                return str(moves)
            elif current[0] > M or current[1] > F:
                return "impossible"
            for num in operations(current):
                if num not in visited and (num[0] % 2 != 0 or num[1] % 2 != 0):
                    visited.add(num)
                    queue.append(num)
        moves += 1
    return "impossible"


def operations(current):
    m, f = current
    new = []
    new.append((m + f, f))
    new.append((m, f + m))
    return new


print(solution("7", "4"))

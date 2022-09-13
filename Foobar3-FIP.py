from collections import deque

def solution(n):
    n = int(n)
    queue = deque([n])
    visited = set()
    moves = 0

    while queue:
        for _ in range(len(queue)):
            current = queue.popleft()
            if current == 1:
                return moves
            for num in operations(current):
                if num not in visited:
                    visited.add(num)
                    queue.append(num)
        moves += 1
    return moves


def operations(current):
    new = [current + 1, current - 1]
    if current % 2 == 0:
        new.append(current // 2)
    return new

print(solution("15"))

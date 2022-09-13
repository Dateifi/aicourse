

[ 0 , 0 , 0 , 0 , 0 , 0 , 0 ,0 ]
[ 0 , 0 , 0 , 0 , 0 , 0 , 0 ,0 ]
[ 0 , 0 , 0 , 0 , 0 , 0 , 0 ,0 ]
[ 0 , 0 , 0 , 0 , 0 , 0 , 0 ,0 ]
[ 0 , 0 , 0 , 0 , 0 , 0 , 0 ,0 ]
[ 0 , 0 , 0 , 0 , 0 , 0 , 0 ,0 ]
[ 0 , 0 , 0 , 0 , 0 , 0 , 0 ,0 ]
[ 0 , 0 , 0 , 0 , 0 , 0 , 0 ,0 ]
[ 0 , 0 , 0 , 0 , 0 , 0 , 0 ,0 ]





def solution(src, dest):

    DIRECTIONS = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

    chessboard = [[] for _ in range(8)]
    for i in range(0, 64):
        chessboard[i // 8].append(i)

    src_index = (src // 8, src % 8)
    dest_index = (dest // 8, dest % 8)

    move_queue = [src_index]
    visited = set()
    visited.add(src_index)
    moves = 0

    while move_queue:
        for _ in range(len(move_queue)):
            current = move_queue.pop(0)
            if current == dest_index:
                return moves
            for direction in DIRECTIONS:
                new = (current[0] + direction[0], current[1] + direction[1])
                if 0 <= new[0] < 8 and 0 <= new[1] < 8 and new not in visited:
                    move_queue.append(new)
                    visited.add(new)
        moves += 1

    return moves






print(solution(56, 28))
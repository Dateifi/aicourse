data = [ 4, 1,1,2,2,5,3,8,5,1]


def solution(data, n):

    unique_ids = set(data)
    for minion_id in unique_ids:
        k = data.count(minion_id)
        if k > n:
            data = [x for x in data if x != minion_id]
    return data




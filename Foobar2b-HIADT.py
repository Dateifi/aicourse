def solution(n, b):
    result_set = set()
    result_list = []
    while True:
        k = len(str(n))
        x = int("".join(reversed("".join(sorted(str(n))))), b)
        y = int("".join(sorted(str(n))), b)
        z = x - y
        digits = []
        while z:
            digits.append(str(z % b))
            z //= b
        n = "".join(reversed(digits)).zfill(k)
        result_list.append(n)
        if n in result_set:
            return len(result_list) - result_list.index(n) - 1
        else:
            result_set.add(n)











z = 124
b = 5
digits = []
while z:
    digits.append(str(z % b))
    z //= b
print("".join(reversed(digits)))
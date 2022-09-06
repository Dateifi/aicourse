def to_digit(input):
    digit = []
    for char in input:
        digit.append(list_for_conv.index(char))
    return digit

list_for_conv = ("0123456789ABCDEF")

def switch_base(base, numbr, out_base):
    number = 0
    for index in range(len(numbr)):
        number += base ** index * numbr[-index - 1]
    output = []
    while number != 0:
        output.append(number % out_base)
        number = number // out_base
    return output[::-1]


def switch_two(numbr):
    out = ""
    for digit in numbr:
        out += list_for_conv[digit]
    return out


number = input("number: ")
base = int(input("base: "))
number = to_digit(number)
out_base = int(
    input("conv_base:")
)
result = switch_base(base, number, out_base)

print(switch_two(result))
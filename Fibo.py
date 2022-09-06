class NewInt(int):
    def __new__(cls, value):
        created_object = super().__new__(cls, value)
        return created_object

    def __init__(self, value):
        self.value = value

    def is_fibonacci(self):
        a, b = 0, 1
        while a < self.value:
            a, b = b, a + b
        return a == self.value

def main():
    n = NewInt(1000)
    new_int_list = [NewInt(i) for i in range(0, n.value + 1)]
    new_int_fib_list = [i for i in new_int_list if i.is_fibonacci()]
    print(new_int_fib_list)


if __name__ == '__main__':
    main()

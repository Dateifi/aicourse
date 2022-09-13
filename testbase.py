personer = []
with open('Personer.dta', encoding="ISO-8859-1") as f:
    for line in f:
        line = line.rstrip().split(";")
        personer.append(line)

class MinHeap:
    def __init__(self):
        self.heap = []
        self.size = 0
        self.heap.append("dummy")

    def insert(self, a_list):
        self.heap.append(a_list)
        self.size += 1
        self.perc_up(self.size)

    def perc_up(self, i):
        while i // 2 > 0:
            if self.heap[i][0] + self.heap[i][1] < self.heap[i // 2][0] + self.heap[i // 2][1]:
                self.heap[i], self.heap[i // 2] = self.heap[i // 2], self.heap[i]
            i = i // 2

    def perc_down(self, i):
        while (i * 2) <= self.size:
            mc = self.min_child(i)
            if self.heap[i][0] + self.heap[i][1] > self.heap[mc][0] + self.heap[mc][1]:
                self.heap[i], self.heap[mc] = self.heap[mc], self.heap[i]
            i = mc

    def min_child(self, i):
        if i * 2 + 1 > self.size:
            return i * 2
        else:
            if self.heap[i*2][0] + self.heap[i*2][1] < self.heap[i*2+1][0] + self.heap[i*2+1][1]:
                return i * 2
            else:
                return i * 2 + 1

    def del_min(self):
        ret_val = self.heap[1]
        self.heap[1] = self.heap[self.size]
        self.size -= 1
        self.heap.pop()
        self.perc_down(1)
        return ret_val

    def build_heap(self, a_list):
        i = len(a_list) // 2
        self.size = len(a_list)
        self.heap = ["dummy"] + a_list[:]
        while (i > 0):
            self.perc_down(i)
            i = i - 1

    def heap_sort(self):
        sort_list = []
        while self.size > 0:
            sort_list.append(self.del_min())
        return sort_list

    def __str__(self):
        return str(self.heap)

    def __len__(self):
        return self.size

    def __getitem__(self, i):
        return self.heap[i]

    def __setitem__(self, i, val):
        self.heap[i] = val


heap = MinHeap()
heap.build_heap(personer)
sorted_list = heap.heap_sort()
for i in range(0, 100000, 20000):
    print(
        f"{sorted_list[i][0] + ' ' + sorted_list[i][1].lower().title():<30}  {sorted_list[i][2].lower().title():<30} {sorted_list[i][3]} - {sorted_list[i][4].lower().title()}")


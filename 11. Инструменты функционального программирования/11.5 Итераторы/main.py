

class StepValueError(Exception):
    pass

class Iterator:

    def __init__(self, start, stop, step=1):
        if step == 0: raise StepValueError
        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        if (self.start > self.stop and self.step > 0) or (self.start < self.stop and self.step < 0):
            raise StepValueError

        self.pointer += self.step
        if (self.step < 0 and self.pointer-self.step < self.stop) or (self.step > 0 and self.pointer-self.step > self.stop):
            raise StopIteration()
        else: return self.pointer-self.step



try:
    print("\nIter1:")
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

print("\nIter2:")
for i in iter2:
    print(i, end=" ")
    print()
print("\nIter3:")
for i in iter3:
    print(i, end=" ")
    print()
print("\nIter4:")
for i in iter4:
    print(i, end=" ")
    print()

print("\nIter5(Have an error: start = 10, stop = 1 when step = 1 by default):")
try:
    for i in iter5:
        print(i, end=" ")
        print()
except StepValueError:
    print('Шаг указан неверно')

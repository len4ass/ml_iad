class SelfCount:
    _count = 0

    def __init__(self):
        type(self)._count += 1

    def __del__(self):
        type(self)._count -= 1

    @property
    def count(self):
        return type(self)._count

    @count.setter
    def count(self, value):
        pass

    @count.deleter
    def count(self):
        pass


a = SelfCount()
print(a.count)
b, c = SelfCount(), SelfCount(),
a.count = 100500
print(a.count, b.count, c.count)
del b.count
del b
print(a.count)


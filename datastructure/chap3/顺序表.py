class ListUnderflow(ValueError):
    pass


class List():
    def __init__(self):
        self._list = []

    def is_empty(self):
        if self.len() == 0:
            return True

    def add(self, elem):
        '''按照从小到大的顺序加入到list内'''
        if self.is_empty():
            self._list.append(elem)
            return
        length = self.len()
        if length == 1 and elem < self._list[0]:
            self._list.insert(0, elem)
            return
        elif length == 1 and elem >= self._list[0]:
            self._list.append(elem)
            return
        for i in range(length - 1):
            if elem < self._list[0]:
                self._list.insert(0, elem)
                return
            elif elem >= self._list[i] and elem <= self._list[i + 1]:
                self._list.insert(i, elem)
                return
            i += 1
        self._list.append(elem)
        return

    def len(self):
        return self._list.__len__()

    def __str__(self):
        for i in self._list:
            print(i, end=' ')
        return ''

    def merge(self, other):
        '''合并两个排好序的顺序表'''
        if not isinstance(other, type(self)):
            raise ListUnderflow("类型不正确")
        for i in other._list:  # 既然是顺序链表，加入元素的时候就已经排序好了，在另一个顺序表中取出元素的时候在以add形式加入，不就是排好序的吗
            self.add(i)


ls1 = List()
for i in range(10, 0, -1):
    ls1.add(i)
print(ls1)
ls2 = List()
for i in range(1, 19, 2):
    ls2.add(i)
ls1.merge(ls2)
print(ls1)

# 实现了队列以及双端队列
from chap3.DLList import *


class QueueUnderflow(ValueError):
    pass


class SQueue(object):
    def __init__(self, init_len=8):
        self._len = init_len  # 储存区长度
        self._elems = [0] * init_len  # 元素存储
        self._head = 0  # 表头元素下表
        self._num = 0  # 已存入的元素个数
        self.__extendlen = init_len  # 留作增长之用

    def is_empty(self):
        return self._num == 0

    def peek(self):
        '''返回队头元素'''
        if self.is_empty():
            raise QueueUnderflow("队列为空")
        return self._elems[self._head]

    def dequeue(self):
        '''队头元素取出'''
        if self.is_empty():
            raise QueueUnderflow("还是不知道该写什么错误")
        e = self._elems[self._head]
        self._head = (self._head + 1) % self._len
        self._num -= 1

    def enqueue(self, e):
        '''在队尾入队'''
        if self._num == self._len:
            self.__extend()
        self._elems[(self._head + self._num) % self._len] = e
        self._num += 1

    def __extend(self):
        '''在队满的情况下扩充队列，私有方法哟'''
        old_len = self._len
        self._len += self.__extendlen  # 原本这句写作self._len*=2
        new_elems = [0] * self._len
        for i in range(old_len):
            new_elems[i] = self._elems[(self._head + i) % old_len]
        self._elems, self._head = new_elems, 0

    def get_extend(self):
        return self.__extend()

    def __str__(self):
        '''打印队列中的元素'''
        for i in self._elems:
            print(i, end=' ')
        return ''


class CycQueue(SQueue):
    def __init__(self, init_len=8):
        super().__init__()
        self._rear = 0

    def enqueue(self, e):
        if (self._rear + 1) % self._len == self._head:
            self.get_extend()
        self._elems[self._rear] = e
        self._num += 1
        self._rear = (self._rear + 1) % self._len

    def __str__(self):
        for i in self._elems[self._head:self._rear]:
            print(i, end=' ')
        return ''


class Double_End_Queue1():
    '''双端队列（deque，全名double-ended queue）是一个限定插入和删除操作的数据结构，具有队列和栈的性质。
    双端队列中的元素可以从两端弹出，其限定插入和删除操作在表的两端进行。基于python list实现'''

    def __init__(self):
        self.elems = []

    def is_empty(self):
        '''判断双端队列是否为空'''
        return self.elems == []

    def addFront(self, elem):
        '''在队首添加元素elem'''
        self.elems.append(elem)

    def addRear(self, elem):
        '''在队尾添加元素elem'''
        self.elems.insert(0, elem)

    def removeFront(self):
        '''删除队首元素'''
        return self.elems.pop()

    def removeRear(self):
        '''删除队尾元素'''
        return self.elems.pop(0)

    def getFront(self):
        '''访问队首元素'''
        return self.elems[-1]

    def getRear(self):
        '''访问队尾元素'''
        return self.elems[0]

    def size(self):
        '''返回双端队列的长度'''
        return len(self.elems)

    def __str__(self):
        '''打印双端队列的内容'''
        for i in self.elems:
            print(i, end=' ')
        return ''


class Double_End_Queue2(DLList):
    '''基于双链表实现的双端队列'''

    def __init__(self):
        super().__init__(head=None, rear=None)

    def is_empty(self):
        '''判断双端队列是否为空,其实没有必要重写的'''
        return super().is_empty()

    def addFront(self, elem):
        '''在队首添加元素elem，在这里重写就改了个名字'''
        return super().append(elem)

    def addRear(self, elem):
        '''在队尾添加元素elem'''
        return super().prepend(elem)

    def removeFront(self):
        '''删除队首元素,即原来双链表的尾部'''
        return super().pop_rear()

    def removeRear(self):
        '''删除队尾元素，即原来双链表的头部'''
        return super().pop_head()

    def getFront(self):
        '''访问队首元素'''
        return self._rear.elem

    def getRear(self):
        '''访问队尾元素'''
        return self._head.elem

    def size(self):
        '''返回双端队列的长度'''
        return super().len()

    def __str__(self):
        '''打印双端队列的内容从队尾打印到队首'''
        return super().__str__()


queue = CycQueue()
for i in range(5):
    queue.enqueue(i)
print(queue.peek(), queue._len, queue._num, queue._head, queue._rear)
queue.dequeue()
print(queue.peek(), queue._len, queue._num, queue._head, queue._rear)
print(queue)
print('_' * 50)

d = Double_End_Queue1()
print(d.is_empty())
d.addRear(4)
d.addRear('dog')
d.addFront('cat')
d.addFront(True)
print(d.size())
print(d.is_empty())
d.addRear(8.4)
print(d.removeRear())
print(d.removeFront())
print(d)
print(d.getRear())
print('-' * 50)

d1 = Double_End_Queue2()
print(d1.is_empty())
d1.addRear(4)
d1.addRear('dog')
d1.addFront('cat')
d1.addFront(True)
print(d1.size())
print(d1.is_empty())
d1.addRear(8.4)
print(d1.removeRear())
print(d1.removeFront())
print(d1)
print(d1.getRear())
print('-' * 50)

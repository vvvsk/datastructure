class DLNode():
    def __init__(self, elem, prev=None, next_=None):
        self.elem = elem
        self.prev = prev
        self._next = next_


class DLListUnderflow(ValueError):
    pass


class DLList():
    def __init__(self, head=None, rear=None):
        self._head = head
        self._rear = rear

    def is_empty(self):
        return self._rear == self._head

    def prepend(self, elem):
        '''头部增加一个元素'''
        p = DLNode(elem, prev=None, next_=self._head)
        if self._head is None:
            self._rear = p
        else:
            p._next.prev = p
        self._head = p

    def append(self, elem):
        '''尾部增加一个元素'''
        p = DLNode(elem, prev=self._rear, next_=None)
        if self._head is None:
            self._head = p
        else:
            p.prev._next = p
        self._rear = p

    def pop_head(self):
        '''删除头元素'''
        if self._head is None:
            raise DLListUnderflow("空双链表，干嘛还要删除呢？")
        e = self._head.elem
        self._head = self._head._next
        if self._head is not None:
            self._head.prev = None
        return e

    def pop_rear(self):
        '''删除尾元素'''
        if self._rear is None:
            raise DLListUnderflow("空双链表，干嘛还要删除呢？")
        e = self._rear.elem
        self._rear = self._rear.prev
        if self._rear is None:
            self._head = None
        else:
            self._rear._next= None
        return e

    def len(self):
        '''返回双链表的长度'''
        p, length = self._head, 0
        if p is None:
            return length
        while p is not None:
            length += 1
            p = p._next
        return length

    def reverse(self):
        '''通过移动链表中数据实现双链表反转'''
        length = self.len()
        if length == 0 or length == 1:
            return
        if length % 2 == 0:
            condition = 'p_head._next is  p_rear and p_rear.prev is p_head'
        else:
            condition = 'p_head._next is p_rear.prev'
        p_head, p_rear = self._head, self._rear
        while True:
            if eval(condition):  # 当条件满足的时候，还要进行再交换一次
                temp = p_head.elem
                p_head.elem = p_rear.elem
                p_rear.elem = temp
                break
            temp = p_head.elem
            p_head.elem = p_rear.elem
            p_rear.elem = temp
            p_head = p_head._next
            p_rear = p_rear.prev

    def reverse1(self):
        '''不移动结点中的数组实现双链表反转'''
        p = None  # 从前往后改变链接方向
        while self._head:
            temp = self._head
            self._head = temp._next
            temp._next = p
            p = temp
        self._head = p

        q = None  # 从后往前改变链接方向，这样就实现了两个方向的链接
        while self._rear:
            temp = self._rear
            self._rear = temp.prev
            temp.prev = q
            q = temp
        self._rear = q

    def sort(self):
        '''为什么不把每个数据拿出来放入列表，在列表里面排序好在一个个加入呢？
        我这里采用冒泡排序'''
        p = self._head
        if p is None or p._next is None:
            return
        q = self._rear
        while self._head is not q:
            p = self._head
            while q is not p:
                if p.elem > p._next.elem:
                    temp = p.elem
                    p.elem = p._next.elem
                    p._next.elem = temp
                p = p._next
            q = q.prev

    def sort1(self):  # 换一种思路,过段时间把它实现了
        q = self._rear
        while self._head is not q:
            p = self._head
            while q is not p:
                if p.elem > p._next.elem:
                    temp = p.elem
                    p.elem = p._next.elem
                    p._next.elem = temp
                p = p._next
            q = q.prev

    def sort2(self):
        p = self._head
        if p is None or p._next is None:
            return
        rem = p._next
        p._next = None
        while rem is not None:
            p = self._head
            q = None
            while p is not None and p.elem <= rem.elem:
                q = p
                p = p._next
            if q is None:
                self._head = rem
            else:
                q._next = rem
            q = rem
            rem = rem._next
            q._next = p
        '''重新建立prev的链接'''
        p = None
        q = self._head
        while q._next is not None:
            q.prev = p
            p = q
            q = p._next
        q.prev = p
        self._rear = q

    def __str__(self):
        p = self._head
        if p is None:
            raise DLListUnderflow("都是空链表了，你还想打印什么出来")
        while p is not None:
            print(p.elem, end=' ')
            p = p._next
        return ''


dllist = DLList()
for i in range(10):
    dllist.append(i)
print(dllist)
dllist.pop_head()
dllist.pop_rear()
print(dllist)
dllist.reverse1()
print(dllist)
dllist.sort2()

print(dllist)
print(dllist.len())

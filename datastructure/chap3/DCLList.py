class DLNode():
    '''带有前指针和后指针的结点'''

    def __init__(self, elem, prev=None, next_=None):
        self.elem = elem
        self.prev = prev
        self._next = next_


class DCLListUnderflow(ValueError):
    '''自定义的循环双链表的异常'''
    pass


class DCLList():
    '''循环双链表类'''

    def __init__(self):  # 初始化的时候是空的，我干嘛还要考虑尾节点的next是不是指向head，多次一举，在添加元素里面讨论不行吗？
        self._head = None

    def is_empty(self):
        '''判断循环双链表是否为空'''
        if self._head is None:
            return True

    def prepend(self, elem):
        '''在头部添加一个元素'''
        p = DLNode(elem)
        if self._head is None:
            p._next = p
            p.prev = p
        else:
            self._head.prev._next = p  # 先将p与尾节点的互联关系建立
            p.prev = self._head.prev
            p._next = self._head  # 再将p与首结点的互联关系建立
            p._next.prev = p

        self._head = p

    def append(self, elem):
        '''在尾部添加一个元素'''
        self.prepend(elem)
        self._head = self._head._next

    def len(self):
        '''返回循环双链表的长度'''
        if self.is_empty():
            raise DCLListUnderflow("我这个小循环双链表都为空了，哪里还有长度")
        p, length = self._head, 0
        while True:
            length += 1
            p = p._next
            if p is self._head:
                break
        return length

    def pop_head(self):
        '''删除头部一个元素'''
        p = self._head
        if p is None:
            raise DCLListUnderflow("你到底要对我这个小小空链表要干嘛")
        elif p._next is p:
            return None
        else:
            self._head.prev._next = self._head._next
            self._head._next.prev = self._head.prev
            self._head = self._head._next

    def pop_rear(self):
        '''删除尾部一个元素'''
        p = self._head
        if p is None:
            raise DCLListUnderflow("你到底要对我这个小小空链表要干嘛")
        elif p._next is p:
            return None
        else:
            self._head.prev.prev._next = self._head
            self._head.prev = self._head.prev.prev

    def __str__(self):
        p = self._head
        if p is None:
            raise DCLListUnderflow("都是空循环双链表，你还想打印出什么结果出来，不可能的啊，兄嘚")
        while True:
            print(p.elem, end=' ')
            p = p._next
            if p is self._head:
                break
        return ''


# 其他操作我不实现了
dcllist = DCLList()
for i in range(10):
    dcllist.append(i)
dcllist.pop_head()
print(dcllist)
print(dcllist._head.prev.elem)
print(dcllist.len())



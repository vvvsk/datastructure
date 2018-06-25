class LNode():
    '''带有后指针的结点'''

    def __init__(self, elem, next_=None):
        '''创建结点类'''
        self.elem = elem
        self._next = next_


class CLinkedListUnderflow(ValueError):
    '''自定义的循环单链表异常'''
    pass


class LCList():
    '''循环单链表'''

    def __init__(self):
        self._rear = None

    def is_empty(self):
        return self._rear is None

    def prepend(self, elem):
        p = LNode(elem)
        if self._rear is None:
            p._next = p
            self._rear = p
        else:
            p._next = self._rear._next
            self._rear._next = p

    def append(self, elem):
        self.prepend(elem)
        self._rear = self._rear._next

    def pop_head(self):
        '''弹出前端元素，并返回其值'''
        if self._rear is None:
            raise CLinkedListUnderflow("空双链表无法进行删除")
        p = self._rear
        if p._next is self._rear:
            self._rear = None
            return p.elem
        else:
            self._rear._next = p._next._next
        return p.elem

    def pop_rear(self):
        '''弹出尾部元素，并返回其值'''
        if self._rear is None:
            raise CLinkedListUnderflow("空双链表无法进行删除")
        p = self._rear
        if p._next is self._rear:
            self._rear = None
            return p.elem
        while p._next is not self._rear:
            p = p._next
        print(p.elem)
        self._rear = p
        p._next = p._next._next  # 跳过下一个元素，等于删除了它，优秀
        return p.elem

    def __str__(self):
        if self._rear is None:
            return
        p = self._rear._next
        while True:
            print(p.elem, end=' ')
            if p is self._rear:
                break
            p = p._next
        return ''

    def insert(self, elem, i):
        '''insert(self,elem,i)将元素elem插入，作为第i个元素，其他元素不变'''
        if i > self.len() or i < 0:
            raise CLinkedListUnderflow("指定位置难以插入", i)
        elif i == 0:
            self.prepend(elem)
            return
        elif i == self.len():
            self.append(elem)
            return
        p, n = self._rear._next, 0
        while p is not self._rear:
            n += 1
            if n == i:
                break
            p = p._next
        q = LNode(elem, p._next)
        p._next = q
        return

    def len(self):
        '''返回循环链表的长度'''
        if self._rear is None:
            return 0
        p, length = self._rear, 1
        if p is None:
            return 0
        while p._next is not self._rear:
            length += 1
            p = p._next
        return length

    def pop_any(self, i):
        '''pop_any(self,i)删除表中的i个元素'''
        if i > self.len() or i <= 0:
            raise CLinkedListUnderflow("指定位置无法进行删除操作", i)
        elif i == 1:
            self.pop_head()
            return
        elif i == self.len():
            self.pop_rear()
            return
        p, n = self._rear._next, 1
        while p is not self._rear:
            n += 1
            if n == i:
                break
            p = p._next
        p._next = p._next._next
        return

    def search(self, elem):
        '''search(self,elem)查找elem在表中的位置，不存在时返回-1'''
        if self._rear is None:
            raise CLinkedListUnderflow("循环链表为空")
        p, n = self._rear._next, 1
        while p is not self._rear:
            if p.elem == elem:
                return n
            n += 1
            p = p._next
        if p.elem == elem:  # 尾节点我不知道怎么写到上面while里面
            return n
        return -1

    def forall(self):
        '''foral1(self,option)对表中所有元素进行option操作'''
        p = self._rear
        while p._next is not self._rear:
            self.option(p)
            p = p._next

    def option(self, p=None):
        '''对结点进行option操作，该例未定义'''
        if not isinstance(p, type(LNode)):
            # print('success')
            return
        return False

    def __len__(self):
        return self.len()

    def from_list_to_LList(self, list=[]):
        '''传入一个list，将它变成LList'''
        if list is None:
            self._rear = None
            return self
        for i in list:
            self.append(i)
        return self

    def from_CList_to_list(self):
        clist = []
        if self._rear is None:
            return clist
        p = self._rear._next
        while p is not self._rear:
            clist.append(p.elem)
            p = p._next
        clist.append(p.elem)
        return clist

    def rev(self):
        ''' 将链表倒置
            算法从一个表的首端不断取出结点，加入到另一个表的首段，完成操作'''
        if self._rear is None:
            return self

        if self._rear._next is self._rear:
            return self
        temp = self._rear
        p = temp
        self._rear = None
        while p._next is not temp:
            self.prepend(p._next.elem)
            p = p._next
        self.prepend(p._next.elem)

    def rev_visit(self, option):
        '''反向遍历链表，并对其中每一个元素进行option操作'''
        self.rev()
        p = self._rear
        while True:
            option(p)
            if p is self._rear:
                break
            p = p._next
        self.rev()

    def find_minial(self):
        '''查找链表中最小元素，返回最小元素以及所在位置'''
        if self._rear is None:
            raise CLinkedListUnderflow("链表 为空，无法进行查找操作")
        p, minial, n, min_cont = self._rear._next, self._rear.elem, 1, 1
        while True:
            if p.elem < minial:
                minial = p.elem
                min_cont += 1
            n += 1
            if p is self._rear:
                break
            p = p._next
        return (minial, min_cont)

    def del_if(self, pred):
        '''删除当前链表中所有满足谓词函数pre元素'''
        if self._rear is None:
            raise CLinkedListUnderflow("链表为空，无法进行删除操作")
        p, n = self._rear._next, 1
        while True:
            if pred(p):
                self.del_any(n)
            if p is self._rear:
                break
            n += 1
            p = p._next

    def del_duplicate(self):
        '''删除表中所有重复的元素'''
        if self._rear is None:
            raise CLinkedListUnderflow("链表为空，无法进行删除操作")
        p = self._rear._next
        elems = [p.elem]  # 辅助变量，进行删除

        while p._next is not self._rear:  # 最后一个结点访问不到
            if p._next.elem in elems:
                p._next = p._next._next
            else:
                elems.append(p._next.elem)
                p = p._next
        if p._next.elem in elems:
            self.pop_rear()

    def interleaving(self, other):
        '''将另一个单链表中的元素交错的加入到本链表中，返回本链表'''
        if not isinstance(other, type(self)):
            raise CLinkedListUnderflow("Type Error")
        if other.is_empty():
            return
        p = self._rear._next
        q = other._rear._next
        while True:
            if p is self._rear:
                r = p._next
                p._next = q
                self._rear = other._rear
                self._rear._next = r
                break
            if p is other._rear:
                p._next = q
                break
            temp = p._next
            p._next = q
            q = temp
            p = p._next

    def partition(self, pred):
        '''循环单链表剖分函数，满足pred()加入到true_pred链表中，不满足则加入到false_pred中'''
        p = self._rear._next
        true_pred = LCList()
        false_pred = LCList()
        while True:
            if pred(p.elem):
                true_pred.append(p.elem)
            false_pred.append(p.elem)
            if p is self._rear:
                break
        return (true_pred, false_pred)


CL1 = LCList()
for i in range(10):
    CL1.append(i)
print(CL1)
CL1.prepend(10)
print(CL1)
CL1.pop_head()
print(CL1)
CL1.pop_rear()
print(CL1)
print(CL1.len())
CL1.insert(100, 9)
print(CL1)
CL1.pop_any(9)
print(CL1)
print(CL1.search(100))
print(CL1.from_CList_to_list())
CL1.rev()
print(CL1)
print(CL1.find_minial())
CL1.append(100)
CL1.del_duplicate()
print(CL1)
CL2 = LCList()
for i in range(5):
    CL2.append(i)

CL1.interleaving(CL2)
print(CL1)

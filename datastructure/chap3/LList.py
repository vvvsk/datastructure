class LNode():
    def __init__(self, elem, next_=None):
        '''创建结点类'''
        self.elem = elem
        self._next = next_


class LinkedListUnderflow(ValueError):
    pass


class LList():
    '''创建链表'''

    def __init__(self, head=None):
        self._head = head

    def is_empty(self):
        '''is_empty(self)判断self是否为一个空表'''
        return self._head is None

    def len(self):
        '''len(self)获得self的长度'''
        p,length = self._head, 0
        while p is not None:
            length += 1
            p = p._next
        return length

    def prepend(self, elem):
        '''=prepend(self,elem)将元素elem加入到表中作为第一个元素'''
        self._head = LNode(elem, self._head)

    def append(self, elem):
        '''append(self,elem)将元素elem加入表中作为最后一个元素'''
        if self._head is None:
            self._head = LNode(elem)
            return
        p = self._head
        while p._next is not None:
            p = p._next
        p._next = LNode(elem)

    def insert(self, elem, i):
        '''insert(self,elem,i)将元素elem插入，作为第i个元素，其他元素不变'''
        if i > self.len() or i < 0:
            raise LinkedListUnderflow("指定位置难以插入", i)
        elif i == 0:
            self.prepend(elem)
            return
        elif i == self.len():
            self.append(elem)
            return
        p, n = self._head, 0
        while p._next is not None:
            n += 1
            if n == i:
                break
            p = p._next
        q = LNode(elem, p._next)
        p._next = q
        return

    def del_first(self):
        '''del_first(self)删除表中的首元素'''
        if self.is_empty():
            raise LinkedListUnderflow("链表为空，操作无法进行")
        self._head = self._head._next

    def del_last(self):
        '''del_last(self)删除表中的尾元素'''
        if self.is_empty():
            raise LinkedListUnderflow("链表为空，操作无法进行")
        if self._head._next is None:
            self._head = None
        p = self._head
        while p._next._next is not None:
            p = p._next
        p._next = None

    def del_any(self, i):
        '''del_any(self,i)删除表中的i个元素'''
        if i > self.len() or i <= 0:
            raise LinkedListUnderflow("指定位置无法进行删除操作", i)
        elif i == 1:
            self.del_first()
            return
        elif i == self.len():
            self.del_last()
            return
        p, n = self._head, 1
        while p._next._next is not None:
            n += 1
            if n == i:
                break
            p = p._next
        p._next = p._next._next
        return

    def __str__(self):
        '''返回链表值集合'''
        p = self._head
        if p == None:
            return "链表为空"
        while p is not None:
            print(p.elem, end=' ')
            p = p._next
        return ''

    def search(self, elem):
        '''search(self,elem)查找elem在表中的位置，不存在时返回-1'''
        if self._head is None:
            raise LinkedListUnderflow("链表为空")
        p, n = self._head, 1
        while p is not None:
            if p.elem == elem:
                return n
            n += 1
            p = p._next
        return -1

    def forall(self):
        '''foral1(self,option)对表中所有元素进行option操作'''
        p = self._head
        while p is not None:
            self.option(p)
            p = p._next

    def option(self, p=None):
        '''对结点进行option操作，该例未定义'''
        if not isinstance(p, type(LNode)):
            # print('success')
            return
        return False

    def __len__(self):
        p = self._head
        length = 0
        while p:
            length += 1
            p = p.next
        return length

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            raise LinkedListUnderflow("类型错误")
        p = self._head
        q = other._head
        if self.len() != other.len():
            return False
        while p is not None and q is not None:
            if p.elem != q.elem:
                return False
            p = p._next
            q = q._next
        return True

    def __lt__(self, other):
        '''小于'''
        p, q = self._head, other._head
        if p is None and q is None:
            return False
        while p and q:
            if p.elem == q.elem:
                p, q = p._next, q._next
            elif p.elem > q.elem:
                return False
            else:
                return True
            if p is None:
                return True
            else:
                return False

    def __gt__(self, other):
        '''大于'''
        if self == other or self < other:
            return False
        else:
            return True

    def __ge__(self, other):
        '''大于等于'''
        p, q = self._head, other._head
        if p is None and q is None:
            return False
        while p and q:
            if p.elem == q.elem:
                p, q = p._next, q._next
            elif p.elem <= q.elem:
                return False
            else:
                return True
            if p is None:
                return True
            else:
                return False

    def __le__(self, other):
        '''小于等于'''
        if self > other:
            return False
        else:
            return True

    def from_list_to_LList(self, list=[]):
        '''传入一个list，将它变成LList'''
        if list is None:
            self._head = None
            return self
        for i in list:
            self.append(i)
        return self

    def from_LList_to_list(self):
        '''将自身LList 变成list'''
        list = []
        if self._head is None:
            return list
        p = self._head
        while p is not None:
            list.append(p.elem)
            p = p._next
        return list

    def rev(self):
        ''' 将链表倒置
        算法，改变相邻两个结点元素的互相指向方向，并保存后一个结点信息，用来与
        下一个相邻的结点元素指向，以此类推'''
        p = None
        while self._head:
            temp = self._head
            self._head = temp._next
            temp._next = p
            p = temp
        self._head = p

    def rev_visit(self, option):
        '''反向遍历链表，并对其中每一个元素进行option操作'''
        self.rev()
        p = self._head
        while p is not None:
            print('correct')
            option(p)
            p = p._next
        self.rev()

    def find_minial(self):
        '''查找链表中最小元素，返回最小元素以及所在位置'''
        if self._head is None:
            raise LinkedListUnderflow("链表 为空，无法进行查找操作")
        p, minial, n, min_cont = self._head, self._head.elem, 1, 1
        while p is not None:
            if p.elem < minial:
                minial = p.elem
                min_cont += 1
            n += 1
            p = p._next
        return (minial, min_cont)

    def del_minimal(self):
        '''删除链表中最小的元素'''
        result = self.find_minial()
        self.del_any(result[1])

    def pred(self, elem):
        if elem:
            return True

    def del_if(self, pred):
        '''删除当前链表中所有满足谓词函数pre元素'''
        if self._head is None:
            raise LinkedListUnderflow("链表为空，无法进行删除操作")
        p, n = self._head, 1
        while p is not None:
            if pred(p):
                self.del_any(n)
            n += 1
            p = p._next

    def del_duplicate(self):
        '''删除表中所有重复的元素'''
        if self._head is None:
            raise LinkedListUnderflow("链表为空，无法进行删除操作")
        p = self._head
        elems = [self._head.elem]  # 辅助变量，进行删除
        while p._next is not None:
            if p._next.elem in elems:
                p._next = p._next._next
            else:
                elems.append(p._next.elem)
                p = p._next

    def interleaving(self, other):
        '''将另一个单链表中的元素交错的加入到本链表中，返回本链表'''
        if not isinstance(other, type(self)):
            raise LinkedListUnderflow("Type Error")
        if other.is_empty():
            return
        p = self._head
        q = other._head
        while q is not None:
            temp = p._next
            p._next = q
            q = temp
            p = p._next

    def partition(self, pred):
        '''单链表剖分函数，满足pred()加入到true_pred链表中，不满足则加入到false_pred中'''
        p = self._head
        true_pred = LList()
        false_pred = LList()
        while p is not None:
            if pred(p.elem):
                true_pred.append(p.elem)
            false_pred.append(p.elem)
        return (true_pred, false_pred)

    def sort(self):
        '''链表排序'''
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

    def insert_sort(self, list=None):
        '''未排序列表，通过插入排序，从空链表开始，实现一个排好序的链表'''
        if list is None:
            raise LinkedListUnderflow("Error")
        self.from_list_to_LList(list)
        self.sort()





# l1 = LList()
# print(l1)
# # l1.del_first()
# for i in range(1, 11):
#     l1.append(i)
# l1.del_first()
# l1.del_last()
# print(l1)
# l1.insert(12, 7)
# print(l1)
# l1.del_any(2)
# print("l1:", l1)
# l1.forall()
# print(l1.search(2))
#
# l2 = LList()
# print(l2)
# for i in range(1, 12):
#     l2.append(i)
# print("l2:", l2)
# print(l1 == l2)
# print(l1 > l2)
# print(l1 >= l2)
# print(l1 < l2)
# print(l1 <= l2)
#
# l3 = LList()
# l3.from_list_to_LList([1, 2, 3, 4, 5])
# print("l3:", l3)
# print(l2.from_LList_to_list())
# print(l3.rev_visit(l3.option))
# print(l3)
# l3.del_minimal()
# l3.append(5)
# l3.append(4)
# l3.append(3)
# print(l3)
# l3.del_duplicate()
# print(l3)
#
# l4 = LList()
# for i in range(1, 10, 2):
#     l4.append(i)
# print(l4)
# l5 = LList()
# for i in range(2, 11, 2):
#     l5.append(i)
# print(l5)
# l4.interleaving(l5)
# print("交错后", l4)
#
# l6 = LList()
# l6.insert_sort([4, 3, 5, 9, 6, 8, 7])
# print(l6)

class Node():
    def __init__(self, elem, list_point=None, next_=None):
        self.elem = elem
        self._next = next_
        self.list_point = list_point  # 表指针，指向该结点在那个表中


class List_Point_LListUnderflow(ValueError):
    pass


class List_Point_LList():
    def __init__(self, head=None):
        self._head = head

    def append(self, elem):
        if self._head is None:
            self._head = Node(elem, self)
            return
        p = self._head
        while p._next is not None:
            p = p._next
        p._next = Node(elem, self)

    def __str__(self):
        p = self._head
        if p is None:
            raise List_Point_LListUnderflow("我还只是个空链表啊")
        while p is not None:
            print(p.elem, end='  ')
            p = p._next
        return ''


list_point_list = List_Point_LList()
list_point_list.append(10)
print(list_point_list)

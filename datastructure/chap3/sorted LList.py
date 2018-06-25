from chap3.LList import LList,LNode,LinkedListUnderflow

class Sort_LList(LList):
    def __init__(self,head = None):
        super().__init__(head)

    def add(self, elem):
        '''为什么不直接调用父类方法，再sort一下呢？
        加入一个元素，不过依然是排序好的
        '''
        p = self._head
        if p is None:
            self.append(elem)
            return
        if p._next is None:
            if p.elem>elem:
                self.prepend(elem)
                return
            else:
                self.append(elem)
                return
        while p and p._next:
            if p.elem>elem:
                self.prepend(elem)
                return
            elif p.elem<=elem and p._next.elem>elem:
                temp = p._next
                p._next = LNode(elem)
                p._next._next =temp
                return
            p = p._next
        self.append(elem)
        return

    def merge(self,other):
        if not isinstance(other,type(self)):
            raise LinkedListUnderflow("类型不正确")
        q = other._head
        if q is None:
            return
        while q is not None:
            self.add(q.elem)
            q = q._next


sorted_LList1 = Sort_LList()
for i in range(10,0,-1):
    sorted_LList1.add(i)
print(sorted_LList1)

sorted_LList2 = Sort_LList()
for i in range(0,20,2):
    sorted_LList2.add(i)
sorted_LList1.merge(sorted_LList2)
print(sorted_LList1)


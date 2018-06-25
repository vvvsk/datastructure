from chap3.LList import *


class Stackunderflow(ValueError):
    pass


class SStack():
    '''基于顺序表实现的栈，用list对象的_elems储存对象'''

    def __init__(self):
        self._elems = []

    def is_empty(self):
        '''判断栈是否为空栈'''
        return self._elems == []

    def top(self):
        '''get栈顶元素'''
        if self.is_empty():
            raise Stackunderflow("我都是空栈了，哪里有什么栈顶")
        return self._elems[-1]

    def push(self, *elem):
        '''压入一个元素到栈内'''
        self._elems.append(elem)

    def pop(self):
        '''移出栈顶元素,返回栈顶元素'''
        if self.is_empty():
            raise Stackunderflow("我都是空栈了，哪里有什么栈顶")
        return self._elems.pop()

    def depth(self):
        '''返回栈的深度'''
        if self.is_empty():
            raise Stackunderflow("空栈")
        return len(self._elems)

class LStack():
    '''基于链接表实现的栈，用LNode作为结点'''

    def __init__(self):
        self._top = None

    def is_empty(self):
        return self._top is None

    def top(self):
        '''get栈顶元素'''
        if self.is_empty():
            raise Stackunderflow("我都是空栈了，哪里有什么栈顶")
        return self._top.elem

    def push(self, elem):
        '''压入一个元素到栈内'''
        self._top = LNode(elem, self._top)

    def pop(self):
        '''移出栈顶元素,返回栈顶元素'''
        if self.is_empty():
            raise Stackunderflow("我都是空栈了，哪里有什么栈顶")
        p = self._top
        self._top = p._next
        return p.elem

# 测试语句
# st1 = SStack()
# st1.push(3)
# st1.push(5)
# while not st1.is_empty():
#     print(st1.pop())
#
# ls = LStack()
# ls.push(3)
# ls.push(5)
# while not ls.is_empty():
#     print(ls.pop())

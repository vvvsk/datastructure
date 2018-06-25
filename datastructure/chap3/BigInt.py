from chap3.LList import *


class BigInt(LList):
    '''用链表表示一个大整数'''

    def __init__(self, head=None):
        super().__init__(head)

    def from_str_to_BigInt(self, str):  # 假设输入的是一个规范的大整数
        len_str = len(str)
        if str[0] == '-':
            self.prepend('-')
            flag = 1
        else:
            self.prepend('+')
            flag = 0
        for i in range(flag, len_str):
            if 0 <= int(str[i]) <= 9:
                self.prepend(int(str[i]))
            else:
                raise LinkedListUnderflow('兄弟你传入字符串不正确')

    def __str__(self):
        self.rev()
        p = self._head
        if p is None:
            raise LinkedListUnderflow("空大整数链表，别再想着输出了")
        elif p.elem =='-':
            print(p.elem,end='')
            p = p._next
        elif p.elem =='+':
            p = p._next

        while p is not None:
            print(p.elem, end='')
            p = p._next
        self.rev()
        return ''

    def __add__(self, other):
        '''未实现非整数的加法'''
        p, q, result = self._head, other._head, BigInt()
        result.prepend(0)
        r = result._head
        while p and q:
            r.elem += (p.elem + q.elem)
            result.append(r.elem // 10)
            r.elem = r.elem % 10
            r = r._next
            p, q = p._next, q._next
            if p.elem:
                pass

        if p is None:
            while q is not None:
                r.elem += q.elem
                result.append(r.elem // 10)
                r.elem %= 10
                q, r = q._next, r._next
        if q is None:
            while p is not None:
                r.elem += p.elem
                result.append(r.elem // 10)
                r.elem %= 10
                p, r = p._next, r._next
        return result

    # 卧槽，还有这么多没做

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __floordiv__(self, other):
        pass

    def __eq__(self, other):
        if not isinstance(other, BigInt):
            raise LinkedListUnderflow("别拿怪物跟我比较")
        if self.len() != other.len():
            return False
        p, q = self._head, other._head
        if p or q is None:
            raise LinkedListUnderflow("你想拿我这个空空如也的大链表干嘛")
        while p and q:
            if p.elem != q.elem:
                return False
        return True


bitint1 = BigInt()
bitint1.from_str_to_BigInt('-12378')
bitint2 = BigInt()
bitint2.from_str_to_BigInt('125679')
print(bitint1, bitint2)
# print(bitint1 + bitint2)

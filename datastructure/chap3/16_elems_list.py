import random
from chap3.LList import LList


class ElemsUnderflow(ValueError):
    pass


class Elems():
    def __init__(self):
        self.elems = []

    def len(self):
        return self.elems.__len__()

    def add(self, elem):
        if self.len() < 16:
            self.elems.append(elem)
        else:
            raise ElemsUnderflow("elems已满，你加入不进去了")

    def clear(self):
        '''清楚里面的元素'''
        self.elems = []

    def __str__(self):
        for elem in self.elems:
            print(elem, end=' ')
        return ''


class Elems_16_List(LList):
    '''那么多方法我好像都不用重写，甚至初始化我好像都不用修改'''


elems_16_list = Elems_16_List()  # 用于暂存16个元素的链表
for j in range(3):
    elems = Elems()  # 含有16个元素的结点
    for i in range(13):
        elems.add(random.randint(1, 100))
    print(elems)
    elems_16_list.append(elems)
print(elems_16_list._head.elem)

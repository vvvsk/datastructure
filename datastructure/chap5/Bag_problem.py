# 背包求解函数

def knap_rec(weight, wlist, n):
    '''背包求解算法递归实现'''
    if weight == 0:
        return True
    if weight < 0 or (weight > 0 and n < 1):
        return False
    if knap_rec(weight - wlist[n - 1], wlist, n - 1):
        print('ITEM' + str(n) + ':', wlist[n - 1])
        return True
    if knap_rec(weight, wlist, n - 1):
        return True
    else:
        return False


def knap_stack(weight, wlist, n):
    '''背包问题的栈实现，非递归'''
    pass


knap_rec(10, [1, 2, 3, 4, 5, 6, 7, 8, 9], 9)

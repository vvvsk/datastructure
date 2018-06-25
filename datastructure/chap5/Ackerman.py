def ackerman_rev(m, n):
    '''ackerman函数的递归实现'''
    if m == 0:
        return n+1
    if m != 0 and n == 0:
        return ackerman_rev(m - 1, 1)
    if m != 0 and n != 0:
       return ackerman_rev(m - 1, ackerman_rev(m, n - 1))

def ackerman_no_rev(m,n):
    '''ackerman函数的非递归形式'''
    pass
print(ackerman_rev(2,30))

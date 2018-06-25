# 完成二元表达式求值
from chap6.BitTree import BitTree


def make_Sum(a, b):
    '''构造一个小树完成a+b操作'''
    return BitTree('+', a, b)


def make_Prod(a, b):
    '''构造一个小树完成a*b操作'''
    return BitTree('*', a, b)


def make_Diff(a, b):
    '''构造一个小树完成a+b操作'''
    return BitTree('-', a, b)


def make_div(a, b):
    '''构造一个小树完成a/b操作'''
    return BitTree('/', a, b)


def is_Basic_Exp(e):
    '''判断e是否为基础表达式,这里传入的参数为bittree，判断左右两边是不是树'''
    return not isinstance(e, BitTree)


def is_number(x):
    '''检查x是否为数字'''
    return (isinstance(x, int) or (isinstance(x, float) or
                                   isinstance(x, complex)))


def eval_Sum(a, b):
    '''加法求值'''
    if is_number(a) and is_number(b):
        return a + b
    return make_Sum(a, b)


def eval_Sum(a, b):
    '''加法求值'''
    if is_number(a) and is_number(b):
        return a + b
    return make_Sum(a, b)


def eval_Prod(a, b):
    '''乘法求值'''
    if is_number(a) and is_number(b):
        return a * b
    return make_Prod(a, b)


def eval_Diff(a, b):
    '''减法求值'''
    if is_number(a) and is_number(b):
        return a - b
    return make_Diff(a, b)


def eval_Div(a, b):
    '''除法求值'''
    if b == 0:
        raise ZeroDivisionError
    if is_number(a) and is_number(b):
        return a / b
    return make_div(a, b)


def eval_Exp(e, values={'s': 50}):
    '''对表达式e求值'''
    if is_Basic_Exp(e):  # 在这里检查e是不是values里面的bian'liang
        if e in values.keys():
            e = values[e]
        return e
    if e in values.items():
        e = values[e]
        print(e)
    option, a, b, = e.root(), eval_Exp(e.left()), eval_Exp(e.right())

    if option == '+':
        return eval_Sum(a, b)
    if option == '-':
        return eval_Diff(a, b)
    if option == '*':
        return eval_Prod(a, b)
    if option == '/':
        return eval_Div(a, b)


def variables(exp, li):  # 递归里面用不了生成器？？？
    '''先序遍历二叉树'''
    if exp.root() is None:
        return
    if is_Variable(exp.root()) is not None:
        li.append(is_Variable(exp.root()))
    if not is_Basic_Exp(exp.left()):  # 检查左边是不是树
        variables(exp.left(), li)
    else:
        if is_Variable(exp.left()) is not None:
            li.append(is_Variable(exp.left()))
    if not is_Basic_Exp(exp.right()):  # 检查左边是不是树
        variables(exp.right(), li)
    else:
        if is_Variable(exp.right()) is not None:
            li.append(is_Variable(exp.right()))


def is_Variable(x):
    # '''求出exp里出现的所有变量的集合，这个集合包不包括数字呢？
    # 我这里不包括数字，不包括运算符号'''
    operators = ('+', '-', '*', '/')
    if not is_number(x) and x not in operators:
        return x
    return


def derive(exp, var):  # 这里的exp只有加法和乘法运算
    '''表达式对变量var的导函数表达式'''
    if exp.root() is None:
        return

def interact_Eval_Exp():
    '''交互式二元表达式计算器'''
    while True:
        pass


e1 = make_Prod(3, make_Sum('s', make_div(5, 1)))
print(e1)  # 我是不是该定义一个函数，输出正常点
print(eval_Exp(e1))
li = []
'''将数组作为一个遍历函数的一个参数，遍历到一个节点，
    就将该节点数值保存到数组中，由于数组的传递是地址传递，
    所以函数中的改变会反应到外部，所以遍历结束，
    数组中就是遍历的数据'''
variables(e1, li)
print(li)

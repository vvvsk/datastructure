from chap5.Stack import SStack

# 完成后缀表达式与中缀表达式一些操作
priority = {'(': 1, '+': 3, '-': 3, '*': 5, '/': 5, '%': 5, '^': 7}
infix_operators = ('+', '-', '*', '/', '^', '%', '(', ')')


def suf_exp_evaluator(exp):
    '''后缀表达式计算'''
    operators = ['+', '-', '*', '/', '^', '%', '//']
    st = SStack()
    for x in exp:
        if x not in operators:
            st.push(x)
            continue
        if st.depth() < 2:
            raise SyntaxError('缺少运算对象')
        a = float(st.pop()[0])
        b = float(st.pop()[0])

        if x == '+':
            c = b + a
        elif x == '-':
            c = b - a
        elif x == '*':
            c = b * a
        elif x == '/':
            c = b / a
        elif x == '^':
            c = pow(b, a)
        elif x == '%':
            c = b % a
        elif x == '//':
            c = b // a
        else:
            break
        st.push(c)
    if st.depth() == 1:
        return st.pop()[0]
    raise SystemError("后缀表达式有问题")


def token_for_suffix(lines):
    '''生成器函数,用于后缀表达式，逐一生成lines中的每一项,每一项都存到列表里面不是最简单的吗'''
    lines = lines.split()
    return lines


def token_for_infix(lines):
    '''生成器函数，用于中缀表达式，逐一生成lines中的每一项，均不支持负数处理'''
    i, lines_len = 0, len(lines)
    while i < lines_len:
        while lines[i].isspace():
            i += 1
        if i >= lines_len:
            break
        if lines[i] in infix_operators:
            yield lines[i]
            i += 1
            continue
        j = i + 1
        while (j < lines_len and not lines[j].isspace() and lines[j] not in infix_operators):
            if (lines[j] == 'e' or lines[j] == 'E') and lines[j + 1] == '-':
                j += 1
            j += 1
        yield lines[i:j]
        i = j


def tran_infix_suffix(line):
    '''中缀表达式到后缀表达式'''
    st = SStack()
    exp = []  # 返回的后缀表达式
    for x in token_for_infix(line):
        if x not in infix_operators:
            exp.append(x)
        elif st.is_empty() or x == '(':  # 左括号进栈
            st.push(x)
        elif x == ')':
            while not st.is_empty() and st.top()[0] != '(':
                exp.append(st.pop()[0])
            if st.is_empty():
                raise SyntaxError('没有找到左括号，就是不匹配')
            st.pop()[0]
        else:
            while (not st.is_empty() and priority[st.top()[0]] >= priority[x]):
                exp.append(st.pop([0]))
            st.push(x)

    while not st.is_empty():
        if st.top()[0] == '(':
            raise SyntaxError("多余的(")
        exp.append(st.pop()[0])
    return exp


def tran_suffix_infix(line):
    suffix_operator = ('+', '-', '*', '/', '%', '^', '//')
    st = SStack()# 用于保存一小部分后缀表达式结果
    for x in token_for_suffix(line):
        if x not in suffix_operator:
            st.push(x)
        else:
            if st.depth()>=2:
                a = st.pop()[0]
                b = st.pop()[0]
                st.push('('+a+x+b+')')
            else:
                raise SyntaxError('后缀表达式错误')
    return st.top()[0]


def test_trans_infix_suffix(string):
    '''测试中缀表达式到后缀表达式'''
    print(string)
    print(tran_infix_suffix(string))
    print('value:', suf_exp_evaluator(tran_infix_suffix(string)))


def suffix_exp_calculator():
    '''后缀表达式计算器，记得在输入的时候每一个字符中间隔一个空格'''
    while True:
        lines = input("请输入后缀表达式")
        if lines == 'end':
            return
        res = suf_exp_evaluator(token_for_suffix(lines))
        return res


def infix_exp_calculator():
    '''中缀表达式计算器，正常输入'''
    while True:
        lines = input("请输入中缀表达式")
        if lines == 'end':
            return
        exp = tran_infix_suffix(lines)
        res = suf_exp_evaluator(exp)
        return res


def infix_exp_evaluator(exp):
    '''直接对中缀表达式进行计算
    举个例子(1*4-3)*(4*1/2-6)
    首先从开始(左括号扫描，保存到储存符号对象的栈内，下面用的栈叫st2，保存好以后，再处理下一个字符
    下一个字符是1，保存到储存运算对象的栈内，下面用的叫st1，保存好以后，处理下一个运算符
    再下一个字符是*，如果st2为空直接存入，但目前不是空的。那么就判断st2栈顶元素优先级与*的大小关系，*优先级大于（，
        那么就不进行运算，如果st2栈顶元素优先级大于*，取出st1两个元素以及st2栈顶元素，完成运算，存入st1中。再将*存入st2中
    下一个是4，保存到st1
    下一个是-，判断st2栈顶元素优先级与*的大小关系，st2栈顶元素*优先级大于-，取出st1两个元素以及st2栈顶元素，完成运算，存入st1中，再将-存入st2中
    下一个是3，保存到st1
    下一个是)，当遇到)右括号，看看st2中还有没有运算符。没有那就可惜了。还有的话，取出st2中运算对象，st1中两个对象完成运算，结果存入st1，
        这个过程是循环的，一直到取到的st2是(左括号，就停止，将st2中的左括号(弹出
    下一个是*，此时st2内为空，直接保存到st2没
    剩余(4*1/2-6)和上面一样
    此时st2内还有*，st1内还有两个元素，对st2循环处理，这已经比上面简单多了
    '''
    st1 = SStack()  # 保存运算对象以及计算的中间结果
    st2 = SStack()  # 存储尚未处理的运算符

    def compute_two_numbers(st, x):
        '''在st栈内取出两个数a，b，完成 a x b操作'''
        if st.depth() >= 2:
            a = float(st.pop()[0])
            b = float(st.pop()[0])
        else:
            raise SyntaxError("表达式error")
        if x == '+':
            c = b + a
        elif x == '-':
            c = b - a
        elif x == '*':
            c = b * a
        elif x == '/':
            c = b / a
        elif x == '^':
            c = pow(b, a)
        elif x == '%':
            c = b % a
        elif x == '//':
            c = b // a
        return c

    for x in token_for_infix(exp):
        if x not in infix_operators:
            st1.push(x)
        elif st2.is_empty() or x == '(':
            st2.push(x)
        elif x == ')':
            while not st2.is_empty() and st2.top()[0] != '(':
                st1.push(compute_two_numbers(st1, st2.pop()[0]))
            if st2.is_empty():
                raise SyntaxError("缺少(")
            st2.pop()
        else:
            print(x, st2.top())
            # 算术的计算方式，优先级高的优先计算
            while not st2.is_empty() and priority[st2.top()[0]] >= priority[x]:
                st1.push(compute_two_numbers(st1, st2.pop()[0]))
            st2.push(x)
    while not st2.is_empty():
        if st2.top()[0] == '(':
            raise SyntaxError("多余的(")
        st1.push(compute_two_numbers(st1, st2.pop()[0]))
    return st1.top()[0]  # 这还有很多毛病,有待发现


if __name__ == '__main__':
    # suffix_exp_calculator()
    # 测试语句较少，可能存在一些bug
    # test_trans_infix_suffix('(3-5)^(4-5)')
    #print(infix_exp_evaluator('(1*4-3)-(4*1/2-6)*(1-4)'))
    print(tran_suffix_infix('3 5 - 4 3 - *'))

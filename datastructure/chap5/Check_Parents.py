from chap5.Stack import SStack


def check_parens(text):
    '''括号配对检查函数，text为被检查文本路径'''
    parens = "()[]{}"
    open_parens = "([{"
    opposite = {')': '(', ']': '[', '}': '{'}

    def openfile(text):
        f = open(text, 'r')
        rowline = 0
        for eachline in f.readlines():
            rowline += 1
            yield eachline, rowline

    def parentheses(strings):
        '''括号生成器，每次调用返回text里下一个括号及其位置'''
        i, strings_len = 0, len(strings)
        while True:
            while i < strings_len and strings[i] not in parens:
                i += 1
            if i >= strings_len:
                return
            yield strings[i], i
            i += 1

    st = SStack()
    for line, rowline in openfile(text):
        for pr, i in parentheses(line):
            if pr in open_parens:  # 我 应该在压栈的时候把行号，字符位置均压入
                st.push(pr, rowline, i)  # rowline行号，i字符位置
            elif not st.is_empty() and st.pop()[0] == opposite[pr]:
                pass
            else:
                print("查到不匹配的括号了，行号 %d，位置%d, 括号 %s" % (rowline, i+1, pr))
                return False

    if st.is_empty():
        print("所有括号匹配正确")
        return True
    print("查到不匹配的括号了，行号 %s，位置%s, 括号 %s" % (st.top()[1], st.top()[2] + 1, st.top()[0]))
    return False


check_parens('check_parentheses.txt')

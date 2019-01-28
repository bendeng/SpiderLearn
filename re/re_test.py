import re

def lazy():
    str = 'abcbcbcb'
    pattern = re.compile('a.*b')  # 结果是['abcbcbcb']
    # pattern = re.compile('a.*?b')#结果是['ab']
    result = pattern.findall(str)
    print(result)



def dot():

    # . 是除了 换行符号\n 之外的 匹配
    one = """
        msfdsdffdsdfsn
        1234567778888N
    """

    #pattern = re.compile('m(.*)n')  #结果是['sfdsdffdsdfs']
    pattern = re.compile('m(.*)n', re.S | re.I)  #结果是['sfdsdffdsdfsn\n        1234567778888']
    result = pattern.findall(one)
    print(result)


def match():

    # 纯数字的正则 \d 0-9之间的一个数
    pattern = re.compile('^\d+$')
    one = '234'

    # 匹配判断的方法
    # match 方法 是否匹配成功 从头开始 匹配一次
    result = pattern.match(one)
    # 如果匹配不到，result则为None
    # 如果匹配到了，result.group()返回匹配到的字符
    print(result.group())


def summary():
    import re

    one = 'abc 123'
    patter = re.compile('\d+')

    # match 从头匹配 匹配一次
    result = patter.match(one)

    # search 从任意位置 , 匹配一次
    #result = patter.search(one)

    # findall  查找符合正则的 内容 -- list
    #result = patter.findall(one)

    # sub  替换字符串
    #result = patter.sub('#', one)

    # split  拆分
    #patter = re.compile(' ')
    #result = patter.split(one)

    print(result)

summary()
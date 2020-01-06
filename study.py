print('hello python')
word = 'word'
sentence = "这是一个句子。"
paragraph = """这是一个段落。
包含了多个语句"""

'''字符串'''
print(word[1::2])
print(sentence)
print(paragraph)

'''列表'''
list2 = ['runoob', 786, 2.23, 'john', 70.2]
list2.append('11')
print(list2[1:3])
print(list2)

'''元组'''
tuple = ('runoob', 786, 2.23, 'john', 70.2)
print(tuple)
print(tuple[1:2])

'''set() 集合'''
student = {'rose', 'jack', 'tom'}
if 'rose' in student:
    print("rose in student")
else:
    print("rose not in student")

a = set('abcabc')
b = set('bcdbcd')
print(a)
print(a - b)
print(a | b)
print(a & b)
print(a ^ b)

'''字典'''
dict = {}
dict['one'] = 1
dict[2] = '你是狗'
print(dict)
print(dict[2])

print('%s 今年%d' % ('晓明', 10))

a, b = 0, 1
while b < 10:
    print(b, end=' ')
    a, b = b, a + b

l = list(range(5))
it = iter(l)
print(next(it))


def method_1(name, age=10):
    print('name=', name)
    print('age=', age)


method_1(age=20, name='kang')
method_1('kang')


def method_2(*tup):
    print(tup)
    for x in tup:
        print(x)


method_2(2, 3, 4)


def method_3(**dicta):
    print(dicta)


method_3(a=3, b=4)

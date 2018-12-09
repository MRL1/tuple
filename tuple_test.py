# 01.计算元组长度并输出
tu=('alex','eric','rain')
print(len(tu))

#02.获取元组的第 2 个元素，并输出
print(tu[1])

#03. 获取元组的第 1-2 个元素，并输出
print(tu[0:2])

#04.请使用for输出元组的元素
for t in tu:
    print(t,end=' ')
    print()
#05.请使用for、len、range输出元组的索引
tu=('alex','eric','rain')
for t in range(len(tu)):
    print(t,tu[t])

#06.请问tu变量中的"k2"对应的值是什么类型？是否可以被修改？如果可以，请在其中添加一个元素 “Seven”
tu = ("alex", [11, 22, {"k1": 'v1', "k2": ["age", "name"], "k3": (11,22,33)}, 44])
tu[1][2]["k2"].append('Senven')
print(tu)
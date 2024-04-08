y = ('周杰伦', 11, ['football', 'music'])
num = y.index(11)
print(num)
num = y.index('周杰伦')
print(num)
del y[2][0]
y[2].append('coding')
print(y)


str = "itheima itcast boxuegu"
num = str.count("it")
print(num)
str2 = str.replace(" ", "|")
print(str2)
list = str2.split("|")
print(list)

my_list = ["黑马程序员", "传智播客", "黑马程序员", "传智播客", "itheima", "itcast", "itheima", "itcast"]
set = set()
for i in my_list:
    set.add(i)

#set = set(my_list)
print(f"集合为:{set}")
print(f"集合为:{set}")
print(f"集合为:{set}")
print(f"集合为:{set}")
print(f"集合为:{set}")

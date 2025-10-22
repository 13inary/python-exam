
# 单分支
if 2>1:
    print("单分支:","2 > 1", "\n")

# 双分支
if 2>1:
    print("双分支:","2 > 1", "\n")
else:
    print("双分支:","2 <= 1", "\n")

# 多分支
if 2>1:
    print("多分支:","2 > 1", "\n")
elif 2>0:
    print("多分支:","2 > 0", "\n")
else:
    print("多分支:","2 <= 0", "\n")

# 三元运算符，性能比标准方式快，但可读性差
value = 1 if 2>1 else 0
print("三元运算符:",value, "\n")


# 三元运算符-嵌套，性能比标准方式快，但可读性差
status = 'error' if False else \
          'warning' if True else \
          'normal'
print("三元运算符-嵌套:",status, "\n")
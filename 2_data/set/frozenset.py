
# 冻结集合

# 不可以改变
fs = frozenset([1,2,3])
# fs.add(4)        # AttributeError

# 可以作为map的键
index = {fs: 'data'}

# 可以嵌套集合
# 普通集合不能嵌套
# invalid = {{1,2}, {3,4}}  # TypeError
# 使用frozenset实现嵌套
valid = {frozenset({1,2}), frozenset({3,4})}
print("type()", valid, "\n") # {frozenset({3, 4}), frozenset({1, 2})}


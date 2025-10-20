# 集合

# 特性：
# 1. 不能包含list/dict等可变类型
# 2. 基于哈希表实现，元素必须可哈希
# 3. 无序
# 4. 元素去重唯一
# 5. 具备集合运算能力

# 初始化-标准
sets = {"element1", "element2"}
print("type:", type(sets)) # <class 'set'>
print("{}:", sets, "\n") # {'element1', 'element2'}

# 初始化-集合推导式
sets3 = {i for i in "element1"}
print("type:", type(sets3)) # <class 'set'>
print("{ for }:", sets3, "\n") # {'e', 'l', 'm', 'n', 't', 'u'} 无序

# 初始化-集合推导式2
sets4 = {i for i in range(10) if i % 2 == 0}
print("type:", type(sets4)) # <class 'set'>
print("{ for if }:", sets4, "\n") # {0, 2, 4, 6, 8} 无序

# 转化成集合
sets2 = set("element1")
print("type:", type(sets2)) # <class 'set'>
print("set():", sets2, "\n") # {'e', 'l', 'm', 'n', 't', 'u'} 无序

# 初始化-空集合
empty_sets = set()
print("type:", type(empty_sets)) # <class 'set'>
print("empty_sets:", empty_sets, "\n") # set()

# 初始化-空字典（注意！！！不是空集合）
empty_dict = {}
print("type:", type(empty_dict)) # <class 'dict'>
print("empty_dict:", empty_dict, "\n") # {}

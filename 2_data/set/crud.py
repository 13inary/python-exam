
# 添加元素
add_sets = {"element1", "element2"}
add_sets.add("element3")
print("add:", add_sets, "\n") # {'element1', 'element2', 'element3'}

# 删除元素-不存在则报错
remove_sets = {"element1", "element2", "element3"}
remove_sets.remove("element1")
print("remove:", remove_sets, "\n") # {'element2', 'element3'}

# 删除元素-不存在则不报错
remove_sets.discard("element4")
print("discard:", remove_sets, "\n") # {'element2', 'element3'}

# 删除元素-随机删除并返回
pop_element = remove_sets.pop()
print("pop:", remove_sets, "\n") # {'element2'}
print("pop_element:", pop_element, "\n") # {'element3'}

# 清空集合
clear_sets = {"element1", "element2", "element3"}
clear_sets.clear()
print("clear:", clear_sets, "\n") # set()

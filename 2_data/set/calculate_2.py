
# 集合运算
cal_sets1 = {"element1", "element2", "element3"}
cal_sets2 = {"element2", "element3", "element4"}

# 交集
print("cal_sets1 & cal_sets2:", cal_sets1 & cal_sets2, "\n") # {'element2', 'element3'}
print("cal_sets1.intersection(cal_sets2):", cal_sets1.intersection(cal_sets2), "\n") # {'element2', 'element3'}

# 并集
print("cal_sets1 | cal_sets2:", cal_sets1 | cal_sets2, "\n") # {'element1', 'element2', 'element3', 'element4'}
print("cal_sets1.union(cal_sets2):", cal_sets1.union(cal_sets2), "\n") # {'element1', 'element2', 'element3', 'element4'}

# 差集
print("cal_sets1 - cal_sets2:", cal_sets1 - cal_sets2, "\n") # {'element1'}
print("cal_sets1.difference(cal_sets2):", cal_sets1.difference(cal_sets2), "\n") # {'element1'}

# 对称差集
print("cal_sets1 ^ cal_sets2:", cal_sets1 ^ cal_sets2, "\n") # {'element1', 'element4'}
print("cal_sets1.symmetric_difference(cal_sets2):", cal_sets1.symmetric_difference(cal_sets2), "\n") # {'element1', 'element4'}


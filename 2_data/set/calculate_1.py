
# 集合运算
cal_sets1 = {"element1", "element2", "element3"}
cal_sets2 = {"element2", "element3", "element4"}

# 子集
print("cal_sets1.issubset(cal_sets2):", cal_sets1.issubset(cal_sets2), "\n") # False
print("cal_sets1.issubset(cal_sets1):", cal_sets1.issubset(cal_sets1), "\n") # True

# 超集
print("cal_sets1.issuperset(cal_sets2):", cal_sets1.issuperset(cal_sets2), "\n") # False
print("cal_sets1.issuperset(cal_sets1):", cal_sets1.issuperset(cal_sets1), "\n") # True

# 是否有交集
print("cal_sets1.isdisjoint(cal_sets2):", cal_sets1.isdisjoint(cal_sets2), "\n") # False

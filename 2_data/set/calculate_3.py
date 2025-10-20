
# 赋予集合运算结果
cal_sets1 = {"element1", "element2", "element3"}
cal_sets2 = {"element2", "element3", "element4"}

# 赋予并集
cal_sets1.update(cal_sets2)               # a |= b
print("update:", cal_sets1, "\n")

# 赋予交集
cal_sets1.intersection_update(cal_sets2)  # a &= b
print("intersection_update:", cal_sets1, "\n")

# 赋予差集
cal_sets1.difference_update(cal_sets2)    # a -= b
print("difference_update:", cal_sets1, "\n")

# 赋予对称差集
cal_sets1.symmetric_difference_update(cal_sets2)    # a ^= b
print("symmetric_difference_update:", cal_sets1, "\n")


# 多集合运算

# 三个集合的交集
s1 = {1,2,3}
s2 = {2,3,4}
s3 = {3,4,5}
newSets1 = set.intersection(s1, s2, s3)
print("set.intersection:", newSets1, "\n")  # {3}

# 动态集合合并
sets = [s1, s2, s3]
combined = set.union(*sets)
print("set.union:", combined, "\n") # {1,2,3,4,5}

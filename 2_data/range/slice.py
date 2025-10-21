r = range(10)

# 索引x下标的元素
print("r[5]:", r[5]) # 5

# 从后面开始索引
print("r[-1]:", r[-1]) # 9

# 大整数支持
big_range = range(10**18, 10**18 + 1000)
print("type:", type(big_range)) # <class 'range'>
print("big_range[500]:", big_range[500])  # 1000000000000000500

# 切片
print("r[2:5]:", r[2:5]) # [2, 3, 4]
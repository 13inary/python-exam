
r = range(10)
# 是否存在
print("5 in r:", 5 in r)        # True

# 索引
print("r.index(7):", r.index(7))    # 7

# 计数
print("r.count(3):", r.count(3))    # 1

# 预计算长度
r = range(10**8)
length = len(r)  # 提前计算避免重复计算
print("length:", length)




# 底层计算原理
def range_get_item(r, index):
    if index < 0:
        index += r.len
    if index < 0 or index >= r.len:
        raise IndexError
    return r.start + index * r.step

# 定义自定义的range-类似实现range的浮点数版本
def frange(start, stop, step):
    while start < stop:
        yield round(start, 10)
        start += step
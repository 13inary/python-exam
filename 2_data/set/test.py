
# 性能测试

# list VS set 查找元素
# 列表查找 O(n)
lst = list(range(10**6))
print("list:", 999999 in lst , "\n")        # 平均耗时 50ms
# 集合查找 O(1)
s = set(range(10**6))
print("set:", 999999 in s  , "\n")         # 平均耗时 0.0001ms

# list VS set 去重
import timeit
# 列表去重方法
def list_dedup(lst):
    return list({x: None for x in lst}.keys())
# 测试数据
data = [i%1000 for i in range(10**6)]
print(timeit.timeit(lambda: list(set(data)), number=10))        # 0.8s
print(timeit.timeit(lambda: list_dedup(data), number=10))      # 1.2s
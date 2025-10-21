
# 避免类型转换
list(range(10**7)) # 错误做法（内存爆炸）
sum(range(10**7)) # 正确做法（保持range对象）


# 步长优化
[i for i in range(0, 10**6, 2)] # 慢速步长
(i*2 for i in range(5*10**5)) # 等效快速实现

def sums(a, b):
    return a+b


result = sums(2, 4)
print(result)

# 函数作为参数
def do(func): # func为函数本身；func()为函数结果
    result = func(4, 5)
    return result
result = do(sums)
print(result)

# 匿名函数
result = do(lambda a,b: a+b)
print(result)

result = (lambda a,b: a+b)(2,3)
print(result)

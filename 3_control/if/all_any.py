
# all 所有元素为真时返回True（空迭代对象返回True），性能比if好
condition = [True, True, True]
if all(condition):
    print("all:",all(condition), "\n")
# 动态条件
if all(i >= 0 for i in range(10)):
    print("all动态条件:",all(i >= 0 for i in range(10)), "\n")
# 处理空列表的问题
security_checks = []
# 修正方案
allow_access = all(security_checks) if security_checks else False
if not allow_access:
    print("处理空列表的问题:",not allow_access, "\n")
# 自动类型转换规则 !!!
mixed_conditions = [1, 'hello', [], 0, {'a':1}]
print(all(mixed_conditions))  # False (因为空列表[]为False)




# any 至少一个元素为真时返回True（空迭代对象返回False），性能比if好
condition = [True, False, True]
if any(condition):
    print("any:",any(condition), "\n")
# ... 这里同all

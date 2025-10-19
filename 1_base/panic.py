# 断言，若为假则抛出异常
# 错误类型固定为AssertionError，常用于调试开发环境
# python -O 运行程序时,解释器会 忽略所有 assert 语句，__debug__ 全局变量变为 False
# golang中相当于：if !condition { panic(error) }
# 等价：
# if __debug__:
#    if not condition:
#        raise AssertionError("错误信息")
assert 2 < 1 # 断言失败，抛出AssertionError
assert 2 < 1, "断言失败" # 断言失败，自定义具体信息，抛出AssertionError

# 直接抛出异常
# 错误类型自定义，常用于生产环境
# golang中相当于：panic(fmt.Errorf("自定义错误"))
raise ValueError("自定义错误")


# 目的：在可能出现错误的代码周围编写，来捕抓错误，从而出现错误后根据错误类型进行处理

# 常见用法：
try: # 业务代码
    height = float("tall")
except ValueError: # 业务代码出现错误后，执行的分支1
    print("invalid data")
except ZeroDivisionError: # 业务代码出现错误后，执行的分支2
    print("zero")
except : # 业务代码出现错误后，执行的分支3，兜底的default操作：最后一个触发，如果前面没有触发，才触发
    print("error")
else: # 业务代码无异常，执行的分支4
    print("success")
finally: # 业务代码不管有没有错，一定会执行的分支5，常用于资源释放
    print("exit")


# 偷懒用法：
try:
    height = float("tall")
except Exception as e:  # 不管什么异常都走这里（不推荐用法）
    print(f"错误: {e}")


# 自定义错误：
class MyError(Exception):
    pass

raise MyError("自定义错误")




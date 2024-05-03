try:
    height = float("tall")
except ValueError:
    print("invalid data")
except ZeroDivisionError:
    print("zero")
except : # 最后一个触发
    print("error")
else:
    print("success")
finally: # 一定会执行
    print("exit")

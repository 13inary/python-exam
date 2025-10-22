
# 缓存判断结果
is_admin = "aaa" == 'admin'
if is_admin:
    print("缓存判断结果:","is_admin", "\n")


# 提前终止
def process(input):
    if not (1 > 2):
        print("提前终止:","process", input, "\n")
        return
    print("不提前终止:","process", input, "\n")
process(1)

# 概率高的在前面
if 100 > 1 or 100 > 99:
    print("概率高的在前面:","100 > 1 or 100 > 99", "\n")

# 空值处理，is None 比 if not x 好
age = None
if age is None:
    print("空值处理:","age is None", "\n")
if not age:
    print("空值处理:","not age", "\n")

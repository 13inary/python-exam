
# 格式化-可复用模板、支持复杂格式
messages = "新年快乐！祝你{}年身体健康".format("龙") # 按属虚
messages = "新年快乐！祝你{0}年身体健康".format("龙") # 按下标
messages = "新年快乐！祝你{name}年身体健康".format(name="龙") # 按名称
messages = "你的成绩是：{0:.2f}".format(6.666) # foat：2位小数
print("float:", messages, "\n")
messages = "你的余额是：{0:,}".format(6666666) # int: 添加千位分隔符
print("int:", messages, "\n")
messages = "你的进度是：{0:.2%}".format(0.666) # 百分比：保留2位小数
print("percent:", messages, "\n")
messages = "你的十六进制是：{0:x}".format(255) # 十六进制：byte => 16进制
print("hex:", messages, "\n")
# 第一个表示填充字符，第二个左对齐（<）、右对齐（>）、居中对齐（^）后面加数字表示宽度
# |     Right|Left******|  Center  |
print("|{:>10}|{:*<10}|{:^10}|\n".format("Right", "Left", "Center"))
# 访问对象属性
class User:
    def __init__(self, name):
        self.name = name
user = User("Diana")
print("user.Name: {u.name}\n".format(u=user)) # Name: Diana
# 访问数组元素
data_list = ["Python", "Java"]
print("list: {0[0]}, {0[1]}\n".format(data_list))
# 访问字典值
data_dict = {"name": "Diana", "age": 28}
print("dict: {0[name]}, {0[age]}\n".format(data_dict))
print("dict2: {name}, {age}\n".format(**data_dict))
# 转义花括号
print("{{}}\n".format()) # }}表示}、{{表示{
# 类型转换符
# !s 强制转字符串、!r 显示 repr() 形式、!a ASCII 转义
print("{!s} {!r} {!a}\n".format("测试", "测试", "测试")) # 测试 '测试' '\u6d4b\u8bd5'





# 格式化-最高效、可嵌入表达式、无法存储模板
name = "龙"
messages = f"新年快乐！祝你{name}年身体健康"
# 转义花括号
messages = f"}}{name}{{，转义花括号" # }}表示}、{{表示{
print("messages:", messages, "\n")




# 格式化-简洁语法




# 格式化-安全防注入
# 定义一个字符串共用模板，里面有变化的数据使用 {xxx} 占位，使用 format 方法传入数据

# map数据填充模板中的空位，这里map需要具备模板需要的所有数据，否则会报错
template = "Name: {name}, Age: {age}"
src_map = {"name": "Alice", "age": 30}
new_str = template.format_map(src_map)
print("template str:", new_str, "\n") # Name: Alice, Age: 30

# 处理map没有模板需要的数据的报错问题
# from collections import defaultdict
class SafeDict(dict):
    def __missing__(self, key):
        return f"<{key} missing>"

data = SafeDict({"city": "Paris"})
print("type of data:", type(data))
print("data:", data)
print("{city}, {country}".format_map(data))  # 输出：Paris, <country missing>




# 格式化 方式1
messages = "新年快乐！祝你{0}年身体健康".format("龙")
messages = "新年快乐！祝你{name}年身体健康".format(name="龙")
messages = "你的成绩是：{0:.2f}".format(6.666)

# 格式化 方式2
name = "龙"
messages = f"新年快乐！祝你{name}年身体健康"
messages = f"{name}，转义花括号}}{{" # }}表示}、{{表示{
print("messages:", messages, "\n")
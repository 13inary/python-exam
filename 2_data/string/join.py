

str_repeat = "喂～" * 3 # 重复
print("str_repeat", str_repeat, "\n")


# 拼接1
strs = "string" + "string" 

# 拼接2，性能通常比拼接1好
str_list = ["string", "string"]
str_join = ','.join(str_list) # string,string
print("str_join:", str_join, "\n")


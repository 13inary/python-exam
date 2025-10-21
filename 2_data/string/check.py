
# 判断是否为数字
fater_digit = "123456"
new_str8 = fater_digit.isdigit() # True
print("isdigit str:", new_str8, "\n")

# 判断是否为字母,有空格就不算字母
fater_alpha = "abcdef"
new_str9 = fater_alpha.isalpha() # True
print("isalpha str:", new_str9, "\n")

# 判断是否为字母和数字
fater_alnum = "123456abcdef"
new_str10 = fater_alnum.isalnum() # True
print("isalnum str:", new_str10, "\n")

# 判断是否以指定字符串开头
fater_startswith = "python"
new_str11 = fater_startswith.startswith("py") # True
print("startswith str:", new_str11, "\n")

# 判断是否以指定字符串结尾
fater_endswith = "python"
new_str12 = fater_endswith.endswith("on") # True
print("endswith str:", new_str12, "\n")




# 判断字面值是否相等
a = "python!"
b = "python!"
print("a is b", a is b, "\n")  # True (Python 3.8+)


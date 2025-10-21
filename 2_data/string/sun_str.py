# 是否包含子字符串
fater_str = "strings"
hav_str = "str" in fater_str
print("hav_str:", hav_str, "\n")

# 查找子字符串位置
index = fater_str.find("tr") # 可选参数是start和end，返回索引，找不到返回-1
print("find:", index, "\n")

# 查找子字符串位置-从右往左查找
index2 = fater_str.rfind("s") # 可选参数是start和end，返回索引，找不到返回-1
print("rfind:", index2, "\n")

index3 = fater_str.index("tr") # 可选参数是start和end，返回索引，找不到报ValueError
print("index:", index3, "\n")

index4 = fater_str.rindex("s") # 可选参数是start和end，返回索引，找不到报ValueError
print("rindex:", index4, "\n")



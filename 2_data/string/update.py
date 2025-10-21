fater_str3 = "  string  "

# 去除左右空格
new_str5 = fater_str3.strip() # string
print("strip str:", "'"+new_str5+"'", "\n")

# 去除左空格
new_str6 = fater_str3.lstrip() # string
print("lstrip str:", "'"+new_str6+"'", "\n")

# 去除右空格
new_str7 = fater_str3.rstrip() # string
print("rstrip str:", "'"+new_str7+"'", "\n")




# 替换子字符串
fater_str2 = "string!?"
new_str = fater_str2.replace("str", "str2")
print("replace str:", new_str, "\n")


# 替换字符，删除字符，注意是字符不是字符串，性能比replace好
trans_table = str.maketrans("str", "STR", "!?")
new_str2 = fater_str2.translate(trans_table)
print("translate str:", "'"+new_str2+"'", "\n")
# 同上，只是参数写法不一样，value为None时删除字符
trans_table2 = str.maketrans({"s": "S", "!": None})
new_str3 = fater_str2.translate(trans_table2)
print("translate str2:", "'"+new_str3+"'", "\n")
# 同上，只是字符串改为字节类型
trans_table3 = bytes.maketrans(b'h', b'H')
new_bytes_text = b'hello'.translate(trans_table3)  # 正确用法 (字节类型)
print("translate bytes:", new_bytes_text, "\n")




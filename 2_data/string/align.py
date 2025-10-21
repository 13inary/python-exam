
fater_str3 = " string "

# 左对齐
new_str2 = fater_str3.ljust(10, "*") # string **
print("ljust str:", new_str2, "\n")

# 右对齐
new_str3 = fater_str3.rjust(10, "*") # ** string
print("rjust str:", new_str3, "\n")

# 居中对齐
new_str4 = fater_str3.center(10, "*") # * string *
print("center str:", new_str4, "\n")





fill_str = "123456"
fill_str2 = "-12345"

# 左边填充0，让字符串长度达到10
str_zfill = fill_str.zfill(10) # 0000012345
print("zfill str:", str_zfill, "\n")
# 符号位保持在最前面
str_zfill2 = fill_str2.zfill(10) # -000012345
print("zfill str2:", str_zfill2, "\n")







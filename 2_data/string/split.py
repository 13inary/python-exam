
# 分割字符串-从左往右分割字符串
fater_str3 = "string,string\n,string"
str_list = fater_str3.split(",", -1) # ['string', 'string\n', 'string'] -1可以不写
print("split:", str_list, "\n")

# 分割字符串-从右往左分割字符串
str_list2 = fater_str3.rsplit(",", 1) # ['string,string\n', 'string']
print("rsplit:", str_list2, "\n")

# 统一处理 \n、\r、\r\n 等换行符，不保留行尾空字符串，按行分割，并去掉换行
str_list3 = fater_str3.splitlines() # ['string,string', ',string']
print("splitlines:", str_list3, "\n")

# 统一处理 \n、\r、\r\n 等换行符，不保留行尾空字符串，按行分割，并保留换行
str_list4 = fater_str3.splitlines(True) # ['string,string\n', ',string']
print("splitlines True:", str_list4, "\n")



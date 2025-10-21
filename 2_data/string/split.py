
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



# 使用正则表达式实现多个分割符分割字符串
import re
text = "apple,banana;cherry  date,fig"
separators = r'[,;\s]+'  # 匹配逗号、分号、空格（一个或多个）
result = re.split(separators, text)
print("re.split:", result, "\n") # ['apple', 'banana', 'cherry', 'date', 'fig']
# 处理中文
text2 = "苹果,香蕉;樱桃 日期,李子"
result2 = re.split(separators, text2, flags=re.UNICODE)
print("re.split with unicode:", result2, "\n")

# 正则表达式分割，保留分割符
text = "a,b;c d"
result = re.split(r'([,; ])', text)
print("re.split with separators:", result, "\n")  # 输出 ['a', ',', 'b', ';', 'c', ' ', 'd']
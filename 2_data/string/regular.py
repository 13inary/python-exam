
# 例子：查找子字符串
import re
pattern = re.compile(r'\d+')  # 预编译
find_result = pattern.findall("a1b23c")    # ['1', '23']
print("find_result:", find_result, "\n")


# 赋值
g = 1
g += 1
g -= 1

# 算术
a = 1 + 2
b = 1 - 2
c = 1 * 2
d = 1 / 2
e = 1 % 2

e = 1 ** 2 # 1^2

# 口诀：结果是变小的整数
# 用途
# 1. 如分页计算，pages = (total_items // items_per_page) + 1
# 2. 快速获取十进制的某一位，number = 345 tens_digit = (number // 10) % 10 结果是4
f = -5 // 2 # -5/2=-2.5 && 负数向下取整 => -3 
f = 5 // 2 # 5/2=2.5 && 正数取整 => 2 

# 比较
g == 1
g != 1
g > 1
g < 1
g >= 1
g <= 1

# 逻辑
h = True and False
i = True or False
j = not True

# 位运算
k = 1 << 1
l = 1 >> 1
m = 1 & 1
n = 1 | 1
o = 1 ^ 1

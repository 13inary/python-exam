# 理解步长的使用
# step 不可以为0
ra = range(5, 7)
print("type:", type(ra)) # <class 'range'>
for i in ra: # [5, 7) 步长默认为1
    print("range(5, 7):", i)
for i in range(1, 6, 2): # 1 3 5
    print("range(1, 6, 2):", i)

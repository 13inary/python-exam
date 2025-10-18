f = open("./b.txt", "w") # w为覆盖，a为追加，r+为读和追加
#f = open("./a.txt", "w", encoding="utf-8")

f.write("0\n")
f.write("1")

f.close()


# 避免忘记close()
with open("./b.txt", "w") as f :
    f.write("new")

f = open("./a.txt") # r
#f = open("./a.txt", "r")
#f = open("./a.txt", "w")
#f = open("./a.txt", "r", encoding="utf-8")

content = f.read(1) # 1byte
print("content: "+content)

line = f.readline()
print("line: "+line)

lines = f.readlines()
print(lines)

content = f.read() # all
print("content: "+content)

f.close()


# 避免忘记close()
with open("./a.txt") as f :
    print("content: " + f.read())

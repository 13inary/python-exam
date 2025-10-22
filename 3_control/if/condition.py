# 结合逻辑运算符
if 2 > 0 and 2 > 1 :
    print("结合逻辑运算符and:","2>0 && 2>1", "\n")

if 2 > 1 or 2 < 0 :
    print("结合逻辑运算符or:","2>1 or 2<0", "\n")

if not 2>1 :
    print("结合逻辑运算符not:","not 2>1", "\n")

# 链式比较
age = 20
if 18 <= age < 65: # 等同于 18 <= age and age < 65
    print("链式比较:","18 <= age < 65", "\n")


# 集合是否包含
key = 'name'
if key in {'name', 'age', 'gender'}:
    print("集合是否包含:","key in {'name', 'age', 'gender'}", "\n")
# 字符串是否包含
if 'na' in 'name':
    print("字符串是否包含:","'name' in 'name'", "\n")


# 类型安全检查
obj = 1
if isinstance(obj, (int, float)):
    print("类型安全检查:","isinstance(obj, (int, float))", "\n")

# 避免错误1
class User:
    def __init__(self, is_admin=False):
        self.is_admin = is_admin
users = [User(True), User(False)]
if users and users[0].is_admin:
    print("避免错误:","users and users[0].is_admin", "\n")

# 避免错误2
mylist = []
if not mylist:  # 比 len(mylist)==0 更高效
    print("避免错误:","not mylist", "\n")


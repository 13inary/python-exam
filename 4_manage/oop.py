# 定义
class Human:
    def __init__(self, name, age): # 构造函数
        self.name = name
        self.age = age
    def run(self):
        print(f"{self.name} is running")

# 使用
people = Human("Mr", 18) # 调用__init__()方法
people.run()

# 定义子类
class Man(Human):
    def __init__(self, name, age)
        super().__init__(name, age) # 调用父类的构造
        self.phone = 130
    def work(self):
        print(f"{self.name} is working")

son = Man("Mr", 30)
son.run()

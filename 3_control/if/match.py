# match
# _ 表示随意值
# 性能比if-elif好

# 基本用法
src = 100
match src:
    case 100 if src > 10: # 条件判断
        print("match", "100", "\n")
    case 200:
        print("match", "200", "\n")
    case 404 | 403: # 或操作
        print("match", "404 or 403", "\n")
    case (500 | 501) as code: # 或操作，并赋值给code
        print("match", "500 or 501", code, "\n")
    case _ if src < 0:
        print("match", "src < 0", "\n")
    case _: # 通配符表示随意值，必须放在最后
        print("match", "unknown", "\n")

# 约束类型
# 使用变量来匹配和获取输入的值
def type_safe_process(value):
    match value:
        case int(n): # 固定类型
            print(f"正整数: {n}")
        case list([int(first), *_]):
            print(f"以整数开头的列表，首元素 {first}")
        case _:
            print("未知")
type_safe_process([5, 'a', 3])  # 以整数开头的列表，首元素 5

# 匹配数组元素数量
def process_coordinates(points):
    match points:
        case []:
            print("无坐标")
        case [2, y]:  # 固定长度。长度必须是2
            print(f"二维点 (2, {y})")
        case [x, y]:  # 长度必须是2
            print(f"二维点 ({x}, {y})")
        case [first, *rest]:  # 长度必须是 2及以上，*rest 表示捕获剩余元素
            print(f"首点 {first}，剩余 {len(rest)} 个点")
process_coordinates([1,2])    # 二维点 (1, 2)
process_coordinates([1,2,3,4]) # 首点 1，剩余 3 个点


# 匹配字典
def process_user(user):
    match user:
        case {"age": age, "name": name}: # 顺序不重要
            print(f"用户 {name}，年龄 {age}")
        case {"name": "jane"}:
            print(f"用户 jane, 年龄未知")
        case {"name": "Jane"}: # 通配符必须放在最后，也就是不能作为key
            print(f"用户 Jane, 年龄未知")
process_user({"name": "John", "age": 30}) # 用户 John，年龄 30
process_user({"name": "Jane"}) # 用户 Jane, 年龄未知


# 匹配类
# 写法1 使用__match_args__来定义匹配顺序
class Point:
    __match_args__ = ('x', 'y')  # x和y是字段名(大小写也要一样)，顺序和调用的入参顺序一致
    def __init__(self, x, y):
        self.x = x
        self.y = y
def handle_shape(shape):
    match shape:
        case Point(x, y) if x == y: # 不会调用__init__，直接访问shape.x和shape.y
            print(f"对角线点 ({x}, {y})")
        case [Point(x1,y1), Point(x2,y2)]:
            print(f"线段: ({x1},{y1})→({x2},{y2})")
        case _:
            print("未知")
handle_shape(Point(3,3))  # 对角线点 (3, 3)
handle_shape([Point(1,2), Point(3,4)])  # 线段: (1,2)→(3,4)
# 写法2 调用的入参指定字段
class Point2:
    def __init__(self, x, y):
        self.x = x
        self.y = y
def handle_shape2(shape):
    match shape:
        case Point2(x=x1, y=y1) if x1 == y1:
            print(f"对角线点 ({x1}, {y1})")
        case [Point2(y=y1, x=x1), Point2(x=x2, y=y2)]: # 既然指定了，顺序就不重要了
            print(f"线段: ({x1},{y1})→({x2},{y2})")
        case _:
            print("未知")
handle_shape2(Point2(3,3))  # 对角线点 (3, 3)
handle_shape2([Point2(1,2), Point2(3,4)])  # 线段: (1,2)→(3,4)
# 写法3 Python 3.10+ 的dataclasses自动处理
from dataclasses import dataclass
@dataclass
class Point3:
    x: int
    y: int
point3_item = Point3(3,3)
print("point3_item.__match_args__", point3_item.__match_args__)
print("point3_item.__init__", point3_item.__init__)
def handle_shape3(shape):
    match shape:
        case Point3(x, y) if x == y:
            print(f"对角线点 ({x}, {y})")
        case [Point3(x, y), Point3(x2, y2)]: # 既然指定了，顺序就不重要了
            print(f"线段: ({x},{y})→({x2},{y2})")
        case _:
            print("未知")
handle_shape3(Point3(3,3))  # 对角线点 (3, 3)
handle_shape3([Point3(1,2), Point3(3,4)])  # 线段: (1,2)→(3,4)

# 匹配嵌套结构体
def parse_nested(data):
    match data:
        case {'user': {'name': str(name), 'age': int(age)}, 'items': [*products]}:
            print(f"{name}({age}) 购买了 {len(products)} 件商品")
        case {'error': {'code': int(code), 'message': msg}}:
            print(f"错误 {code}: {msg}")
        case _:
            print("未知数据结构")

parse_nested({
    'user': {'name': 'Alice', 'age': 30},
    'items': ['书', '咖啡']
})  # Alice(30) 购买了 2 件商品

# 捕获子模式
# 示例1
def analyze_command(cmd):
    match cmd.split():
        case ['login', username, password]:
            print("login", username, password)
        case ['download', *filenames] if len(filenames) > 0:
            print("download", filenames)
        case ['search', query, ('--limit', limit)]:  # 第三个参与要求是一个二元元组
            print("search", query, limit)
        case _:
            print("无效命令")
analyze_command("search python --limit 10") # 无效命令
# 示例2
def analyze_command2(cmd):
    match cmd:
        case ['search', query, ('--limit', limit)]:
            print(f"特殊模式：搜索 {query}，限制 {limit}")
analyze_command2(['search', 'python', ('--limit', '10')])



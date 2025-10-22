
# 作用：
# 自动生成__init__构造函数
# 自动生成__repr__可读的字符串表示
# 自动生成__eq__值相等比较
# 自动生成__match_args__ （Python 3.10+）
# 不生成__getitem__等序列操作支持

# 注意：
# 避免在子类中改变字段顺序
# 动态添加的字段不会自动添加到__match_args__

# 用法
from dataclasses import dataclass
@dataclass
class DataPoint:
    x: float
    y: float

# 生成def __lt__(self, other):
@dataclass(order=True)
class TimeSeries:
    timestamp: int
    value: float
a = TimeSeries(1, 2)
b = TimeSeries(1, 2)
print("__lt__", a.__lt__(b))
print("a == b", a == b)  # 输出: True
print("a < b", a < b)  # 输出: False

# 冻结，不可修改字段值
@dataclass(frozen=True)
class ImmutableConfig:
    api_key: str = "默认值" # 可以指定默认值
cfg = ImmutableConfig("SECRET_KEY")
try:
    cfg.api_key = "NEW_KEY"
except Exception as e:
    print(f"错误类型: {type(e).__name__}")

# 继承层级不影响匹配顺序
@dataclass
class Base:
    base_field: int
@dataclass
class Derived(Base):
    derived_field: str
d = Derived(10, "data")
print(Derived.__match_args__)  # 输出: ('base_field', 'derived_field')
match d:
    case Derived(bf, df):  # 继承层级不影响匹配顺序
        print(f"基字段: {bf}, 派生字段: {df}")

# 调试
@dataclass
class DebugPoint:
    x: int
    y: int

    def __getattribute__(self, name): # 访问属性: x 访问属性: y
        print(f"访问属性: {name}")
        return super().__getattribute__(name)

p = DebugPoint(3,4)
match p:
    case DebugPoint(a, b):  # 观察属性访问顺序
        print(f"匹配值: {a}, {b}") # 匹配值: 3, 4

# 优化匹配
@dataclass
class NetworkPacket:
    src_ip: str
    dst_ip: str
    payload: bytes
    __match_args__ = ("dst_ip", "src_ip") # 优化匹配性能
packet = NetworkPacket("192.168.1.1", "10.0.0.1", b"data")
match packet:
    case NetworkPacket("10.0.0.1", src):  # 优先匹配高频目标地址
        print(f"目标地址: {src}")



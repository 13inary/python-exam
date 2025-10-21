# 定义一个字符串共用模板，里面有变化的数据使用 {xxx} 占位，使用 format 方法传入数据

# map数据填充模板中的空位，这里map需要具备模板需要的所有数据，否则会报错
template = "Name: {name}, Age: {age}"
src_map = {"name": "Alice", "age": 30}
new_str = template.format_map(src_map)
print("template str:", new_str, "\n") # Name: Alice, Age: 30


# 处理map没有模板需要的数据的报错问题
# from collections import defaultdict
class SafeDict(dict):
    def __missing__(self, key):
        return f"<{key} missing>"

data = SafeDict({"city": "Paris"})
print("type of data:", type(data))
print("data:", data)
print("{city}, {country}".format_map(data))  # 输出：Paris, <country missing>




# 定义一个字符串共用模板，里面有变化的数据使用 {xxx} 占位，使用 format 方法传入数据

template = "Name: {name}, Age: {age}"
src_map = {"name": "Alice", "age": 30}
new_str = template.format_map(src_map)
print("template str:", new_str, "\n") # Name: Alice, Age: 30




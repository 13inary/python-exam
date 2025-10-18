# 基本命令使用

* 运行
```shell
# 当前目录优先
python script.py

# 按sys.path标准路径搜索
python3.11 -m module_name [args]
```
```shell
# 指定代码
python3.11 -c "print(2**8)"

# 交互式
python3.11 -i script.py
```

```shell
# 基本优化（移除assert等）
python3.11 -O
# 激进优化（移除文档字符串）
python3.11 -OO
# 触发字节码混合警告
python3.11 -b
```

```shell
# 不自动导入site模块
python3.11 -S
# 忽略所有环境变量
python3.11 -E
# 隔离模式（忽略用户环境）
python3.11 -I
```

```shell
# 基础详细模式
python3.11 -v
# 更详细输出
python3.11 -vv
```

```shell
# 指定源文件编码（替代文件头声明）
python3.11 -X utf8
# 带时间统计的运行
python3.11 -X importtime
```


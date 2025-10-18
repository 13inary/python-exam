# 配置

## 虚拟环境

* 创建虚拟环境
python -m venv .venv --prompt "my_project"

* 激活环境
Windows
.venv\Scripts\activate
Unix/macOS
source .venv/bin/activate


## 镜像
```shell
# vim ~/.pip/pip.conf
[global]
index-url = https://mirrors.aliyun.com/pypi/simple/
extra-index-url =
    https://pypi.tuna.tsinghua.edu.cn/simple/
    https://mirrors.tencent.com/pypi/simple/
```

## 性能优化
```
# 启用Python JIT编译器（Python 3.12+）
export PYTHON_JIT=1

# 设置内存分配器
export PYTHONMALLOC=malloc
```

## 多版本管理
```
# 使用pyenv管理版本
curl https://pyenv.run | bash
pyenv install 3.11.5
pyenv global 3.11.5
```

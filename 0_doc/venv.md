# 虚拟环境


## 虚拟环境隔离
实现工具：venv, virtualenv, conda
作用：在相同Python版本下隔离第三方包依赖


* 不同项目使用不同版本
* 不同项目使用不同依赖
* 不同项目使用不同配置


## 创建虚拟环境

```shell
python3.11 -m venv .venv --prompt "my_project"
# or
python3.11 -m venv myproject-env
# 环境目录结构
#my_project/
#├── bin/        # python/pip可执行文件（软链接），优先级比系统PATH高
#├── lib/        # 独立安装的包（site-packages）,每个环境的第三方包独立安装，互不影响
#└── pyvenv.cfg  # 环境配置（指向基础解释器）
```


## 激活虚拟环境

```shell
source .venv/bin/activate
```


## 区分版本和虚拟环境

系统python：python3.10、python3.11
python3.11：venvA、venvB、venvC

例子：
```shell
# 使用pyenv+venv组合
pyenv install 3.10.12
pyenv install 3.11.4

mkdir legacy-project && cd legacy-project
pyenv local 3.10.12
python -m venv .venv && source .venv/bin/activate

mkdir modern-project && cd modern-project
pyenv local 3.11.4
python -m venv .venv && source .venv/bin/activate
```


# 版本


## 版本区别

Python 2.x系列 在2020年已停止维护

3.9+版本需掌握walrus运算符（:=）

3.10+版本的结构模式匹配（match case）

3.11（性能优化）快25%-60%,错误增强上下文显示，类型系统支持Self类型和异常类型，异步中的Task取消改进


## 系统安装多个版本解释器
实现工具：update-alternatives, pyenv, deadsnakes PPA
作用：在同一系统共存不同大版本的Python解释器

* update-alternatives
update-alternatives配置多版本共存，使用python3.11作为默认解释器。若需要运行旧版本项目，建议使用venv创建隔离环境。

* pyenv
pyenv管理多个Python版本，支持切换和自动选择。

* deadsnakes PPA
Ubuntu/Debian安装3.10+版本，使用deadsnakes PPA。

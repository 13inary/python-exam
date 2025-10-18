# 安装

## 步骤

* Debian/Ubuntu
sudo apt update && sudo apt install python3.11-full

* RHEL/CentOS
sudo dnf install python311

* *编译安装（最新特性）
wget https://www.python.org/ftp/python/3.11.5/Python-3.11.5.tar.xz
tar xJf Python-3.11.5.tar.xz
cd Python-3.11.5
./configure --enable-optimizations
make -j$(nproc)
sudo make altinstall


## 组合推荐

* 最小生产环境
```shell
sudo apt install python3.11-minimal
```

* 标准开发环境
```shell
sudo apt install \
python3.11-full \
python3.11-dev \
python3.11-venv \
python3.11-doc
```

* 完整研究环境
```shell
sudo apt install \
python3.11-dbg \
python3.11-examples \
python3.11-full \
python3.11-dev
```
# BRISQUE for python

[项目原地址](https://github.com/bukalapak/pybrisque)

其中`test`下为示例代码

## 1. pip安装

- 安装模块

```bash
# 安装 brisque 模块
python3 -m pip install pybrisque
# 安装 libsvm
python3 -m pip install libsvm-official
```

- 修改`brisque.py`的模块导入部分

```python
from libsvm import svmutil
from libsvm.svmutil import *
```

## 2. 直接使用代码

- 安装模块

```bash
# 安装 libsvm
python3 -m pip install libsvm-official
```

- 导入路径: 文件夹名必须为`brisque`, 导入的路径为`brisque`文件夹所在目录

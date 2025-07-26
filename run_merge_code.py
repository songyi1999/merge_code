#!/usr/bin/env python3
"""
直接运行 merge_code 的便捷脚本
不需要 pip 安装，可以直接从源码运行
"""

import os
import sys

# 将 src 目录添加到 Python 路径
current_dir = os.path.dirname(os.path.abspath(__file__))
src_dir = os.path.join(current_dir, 'src')
sys.path.insert(0, src_dir)

# 导入并运行主函数
from merge_code.main import main

if __name__ == "__main__":
    main()
# 使用说明

## 直接从源码运行（无需 pip 安装）

### 方法一：使用 Python 脚本
```bash
python run_merge_code.py [参数]
```

### 方法二：使用批处理文件（Windows）
```cmd
run_merge_code.bat [参数]
```

### 方法三：直接运行模块
```bash
python -m src.merge_code.main [参数]
```

## 常用命令示例

### 基本使用
```bash
# 在当前目录合并代码
python run_merge_code.py

# 指定目录
python run_merge_code.py -d /path/to/your/project

# 指定输出文件
python run_merge_code.py -o merged_code.txt

# 指定页数限制
python run_merge_code.py -p 100
```

### 高级使用
```bash
# 只包含特定文件类型
python run_merge_code.py -i .py,.js,.vue

# 排除特定目录
python run_merge_code.py -x node_modules,dist,build

# 指定开始文件
python run_merge_code.py -s main.py

# 使用配置文件
python run_merge_code.py -c my_config.json
```

## 配置文件示例

创建 `.merge_code.json` 文件：
```json
{
  "directory": ".",
  "start_files": ["main.py", "app.py", "index.js"],
  "pages": 60,
  "include": ".py,.js,.vue,.html,.css",
  "exclude_dirs": "node_modules,dist,build,__pycache__",
  "exclude_files": "*.min.js,*.min.css,package-lock.json",
  "output": "merged_code.txt"
}
```

## 测试

运行测试：
```bash
python -m pytest test/
```

或者：
```bash
python test/test_main.py
```
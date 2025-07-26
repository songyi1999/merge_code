# 安装和使用指南

## 方法一：从源码打包安装（推荐）

### 1. 安装构建工具
```bash
python -m pip install --upgrade pip build wheel hatchling
```

### 2. 构建包
```bash
python -m build
```

### 3. 安装包
```bash
python -m pip install dist/merge_code-0.2.4-py3-none-any.whl
```

### 4. 使用方式

#### 方式一：作为模块运行
```bash
python -m merge_code --help
python -m merge_code -d /path/to/project
python -m merge_code -i py,js,vue -o output.txt
```

#### 方式二：直接导入使用
```python
import merge_code
merge_code.main()
```

#### 方式三：命令行工具（需要配置PATH）
```bash
merge_code --help
merge_code -d /path/to/project
```

## 方法二：开发模式安装

如果你想在开发过程中安装，可以使用可编辑安装：

```bash
python -m pip install -e .
```

这样修改源码后不需要重新安装。

## 方法三：直接从源码运行（无需安装）

如果不想安装，可以直接运行：

```bash
python run_merge_code.py [参数]
```

## 卸载

```bash
python -m pip uninstall merge-code
```

## 常用命令示例

```bash
# 查看版本
python -m merge_code --version

# 基本使用
python -m merge_code

# 指定目录
python -m merge_code -d /path/to/project

# 指定文件类型
python -m merge_code -i py,js,vue

# 指定输出文件
python -m merge_code -o merged_code.txt

# 指定页数限制
python -m merge_code -p 100

# 使用配置文件
python -m merge_code -c my_config.json

# 组合使用
python -m merge_code -d /path/to/project -i py,js -o output.txt -p 80
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

## 验证安装

运行以下命令验证安装是否成功：

```bash
python -c "import merge_code; print('安装成功！')"
python -m merge_code --version
```
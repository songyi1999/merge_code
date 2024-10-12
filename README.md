# 代码合并工具

## 简介

该工具用于合并源代码文件，主要用于软件著作权申请。它支持多种编程语言，包括 JavaScript、Python、PHP 等，并且可以根据指定的文件扩展名进行过滤。

## 功能

- **合并源代码**：支持多种文件格式的代码合并。
- **过滤文件**：可以根据文件扩展名、目录和文件名进行过滤。
- **处理注释**：自动删除源代码中的注释。
- **配置灵活**：支持通过配置文件或命令行参数进行灵活设置。

## 使用说明

### 命令行参数

* `-d` 或 `--directory`: 工作目录（默认为当前目录）
* `-s` 或 `--start-file`: 指定开始文件名（会在目录树中递归搜索）
* `-p` 或 `--pages`: 指定要提取的页面数（默认为 60）
* `-i` 或 `--include`: 指定要包含的文件扩展名（逗号分隔）
* `-o` 或 `--output`: 指定输出文件名（默认为 `out.txt`）
* `-x` 或 `--exclude-dirs`: 指定要排除的目录（逗号分隔）
* `-e` 或 `--exclude-files`: 指定要排除的文件模式（逗号分隔）
* `-c` 或 `--config`: 指定配置文件路径（默认为 `.merge_code.json`）
* `-v` 或 `--version`: 显示版本信息

### 默认行为

* 如果不指定开始文件名，工具会在目录树中递归搜索以下文件名：`login.vue`、`app.py`、`index.js`、`index.php`、`index.html`
* 如果不指定要包含的文件扩展名，工具会包含默认扩展名的所有文件
* 如果不指定要排除的文件扩展名，工具会排除常见的不必要文件

### 工作流程

1. 根据指定的目录和开始文件名，工具会在目录树中递归搜索开始文件。
2. 根据指定的文件扩展名，工具会过滤出要包含的文件。
3. 工具会合并过滤出的文件，并根据指定的页面数进行截取。
4. 工具会将合并后的代码保存到指定的输出文件中。

### 注意事项

* 请确保指定的目录和开始文件名正确。
* 请确保指定的文件扩展名正确。
* 请确保指定的页面数合理。
* 请确保输出文件名正确。

## 安装方法

### 使用 pip 安装

```bash
python -m pip install merge_code
```

源码安装
```
git clone https://github.com/songyi1999/merge_code.git
cd merge_code
python -m pip install -e .
```
使用示例
```
merge_code -d /path/to/directory
```
或 
```
cd /path/to/directory
merge_code
```
## 可选配置文件：
配置文件示例:
以下是配置文件 .merge_code.json 的模板：
```
{
  "directory": ".",
  "start_files": ["login.vue", "app.py", "index.js", "index.php", "index.html"],
  "pages": 60,
  "include": ".py,.js,.jsx,.ts,.tsx,.vue,.html,.css,.scss,.sass,.less,.php,.java,.c,.cpp,.h,.hpp",
  "exclude_dirs": "node_modules,dist,build,vendor,.git,.idea,.vscode,__pycache__,temp,tmp",
  "exclude_files": "*.min.js,*.min.css,package-lock.json,yarn.lock,pnpm-lock.yaml,postcss.config.js,vue.config.js,babel.config.js,.eslintrc.js,.merge_code.json",
  "output": "out.txt"
}
```
您可以根据需要修改此文件，并在运行工具时指定该配置文件。

## 许可证
本项目遵循 MIT 许可证。详细信息请参见 LICENSE 文件。
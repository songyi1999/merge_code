# 代码合并工具

## 简介

该工具用于合并源代码文件，主要用于软件著作权申请。它支持多种编程语言，包括 JavaScript、Python、PHP 等，并且可以根据指定的文件扩展名进行过滤。

## 使用说明

### 命令行参数

* `-d` 或 `--directory`: 工作目录（默认为当前目录）
* `-s` 或 `--start-file`: 指定开始文件名（会在目录树中递归搜索）
* `-p` 或 `--pages`: 指定要提取的页面数（默认为 60）
* `-i` 或 `--include`: 指定要包含的文件扩展名（逗号分隔）
* `-e` 或 `--exclude`: 指定要排除的文件扩展名（逗号分隔）
* `-o` 或 `--output`: 指定输出文件名（默认为 `out.txt`）
* 通过 -x 或 --exclude-dirs 参数指定要排除的目录，多个目录用逗号分隔。


### 默认行为

* 如果不指定开始文件名，工具会在目录树中递归搜索以下文件名：`login.vue`、`app.py`、`index.js`、`index.php`、`index.html`
* 如果不指定要包含的文件扩展名，工具会包含所有文件
* 如果不指定要排除的文件扩展名，工具会排除以下文件扩展名：`.lock`、`.out`、`.yaml`、`.txt`、`.md`、`.csv`、`.gitignore`、`.sh`、`.bat`、`.xml`、`.yml`、`.json`、`.png`、`.jpg`、`.jpeg`、`.gif`、`.bmp`、`.ico`、`.db`、`.sqlite`、`.bin`、`.exe`、`.dll`、`.so`、`.dylib`

## 工作流程

1. 根据指定的目录和开始文件名，工具会在目录树中递归搜索开始文件
2. 根据指定的文件扩展名，工具会过滤出要包含的文件
3. 工具会合并过滤出的文件，并根据指定的页面数进行截取
4. 工具会将合并后的代码保存到指定的输出文件中

## 注意事项

* 请确保指定的目录和开始文件名正确
* 请确保指定的文件扩展名正确
* 请确保指定的页面数合理
* 请确保输出文件名正确

## 安装方法

#### 用pip 安装
```
python -m pip install merge_code
```

#### 源码安装

```
git clone https://github.com/songyi1999/merge_code.git
cd merge_code
python -m pip install -e .
```

### 使用示例

```bash
merge_code -d /path/to/directory 
```
或
```
cd /path/to/directory
merge_code
```
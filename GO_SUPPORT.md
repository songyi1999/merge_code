# Go 语言支持说明

## 新增功能

merge_code v0.2.5 现在完全支持 Go 语言源代码合并！

### 支持的 Go 语言特性

1. **文件扩展名识别**：自动识别 `.go` 文件
2. **注释删除**：
   - 单行注释：`// 注释内容`
   - 多行注释：`/* 注释内容 */`
3. **开始文件识别**：自动查找 `main.go` 作为项目入口文件
4. **Go 项目文件排除**：自动排除 `go.sum`、`go.mod` 等文件

### 使用示例

#### 1. 合并 Go 项目
```bash
# 只合并 Go 文件
python -m merge_code -d /path/to/go/project -i go

# 指定 main.go 作为开始文件
python -m merge_code -d /path/to/go/project -i go -s main.go

# 合并到指定输出文件
python -m merge_code -d /path/to/go/project -i go -o merged_go_code.txt
```

#### 2. 混合语言项目
```bash
# 同时合并 Go、Python、JavaScript 文件
python -m merge_code -d /path/to/project -i go,py,js

# 包含更多语言
python -m merge_code -d /path/to/project -i go,py,js,java,cpp
```

#### 3. 使用配置文件
创建 `.merge_code.json`：
```json
{
  "directory": ".",
  "start_files": ["main.go", "main.py", "app.py", "index.js"],
  "pages": 60,
  "include": ".go,.py,.js,.jsx,.ts,.tsx,.vue,.html,.css",
  "exclude_dirs": "node_modules,dist,build,vendor,.git,target",
  "exclude_files": "*.min.js,*.min.css,go.sum,go.mod",
  "output": "merged_code.txt"
}
```

然后运行：
```bash
python -m merge_code -c .merge_code.json
```

### Go 项目结构示例

对于典型的 Go 项目结构：
```
my-go-project/
├── main.go
├── go.mod
├── go.sum
├── pkg/
│   ├── utils/
│   │   └── helper.go
│   └── models/
│       └── user.go
└── cmd/
    └── server/
        └── server.go
```

工具会：
1. 自动找到 `main.go` 作为开始文件
2. 递归扫描所有 `.go` 文件
3. 排除 `go.mod` 和 `go.sum` 文件
4. 删除所有注释并合并代码

### 注释删除示例

**原始 Go 代码：**
```go
package main

import "fmt"

// 这是一个单行注释
func main() {
    /* 
    这是一个多行注释
    用于说明函数功能
    */
    fmt.Println("Hello, World!")
}
```

**处理后的代码：**
```go
package main
import "fmt"
func main() {
    fmt.Println("Hello, World!")
}
```

### 支持的所有语言

现在 merge_code 支持以下编程语言：

- **Go** (.go) - 新增！
- Python (.py)
- JavaScript (.js, .jsx)
- TypeScript (.ts, .tsx)
- Vue (.vue)
- HTML (.html)
- CSS (.css, .scss, .sass, .less)
- PHP (.php)
- Java (.java)
- C/C++ (.c, .cpp, .h, .hpp)

### 版本信息

- 当前版本：v0.2.5
- 新增：Go 语言完整支持
- 改进：更好的注释删除算法
- 优化：更智能的文件类型识别
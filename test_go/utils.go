package main

import "strings"

// StringUtils 提供字符串工具函数
type StringUtils struct{}

/*
多行注释示例
这个函数用于处理字符串
*/
func (s *StringUtils) ToUpper(input string) string {
	// 转换为大写
	return strings.ToUpper(input)
}

// 检查字符串是否为空
func IsEmpty(str string) bool {
	return len(strings.TrimSpace(str)) == 0
}
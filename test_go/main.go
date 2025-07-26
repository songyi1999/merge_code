package main

import (
	"fmt"
	"log"
)

// 这是一个单行注释
func main() {
	/* 
	这是一个多行注释
	用于测试注释删除功能
	*/
	fmt.Println("Hello, World!")
	log.Println("这是一个Go程序示例")
}

// 另一个函数
func greet(name string) string {
	// 返回问候语
	return fmt.Sprintf("Hello, %s!", name)
}
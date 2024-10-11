import unittest
import os
import tempfile
from main import merge_code, find_files, find_start_file, process_file

class TestMain(unittest.TestCase):

    def test_merge_code(self):
        # 创建临时文件
        with tempfile.TemporaryDirectory() as tmp_dir:
            # 创建测试文件
            file1 = os.path.join(tmp_dir, 'file1.py')
            file2 = os.path.join(tmp_dir, 'file2.py')
            with open(file1, 'w') as f:
                f.write('print("Hello World!")')
            with open(file2, 'w') as f:
                f.write('print("Hello Again!")')

            # 测试 merge_code 函数
            merged_code, _ = merge_code([file1, file2], None, 100)
            self.assertEqual(merged_code.strip(), 'print("Hello World!")\nprint("Hello Again!")')

    def test_find_files(self):
        # 创建临时文件
        with tempfile.TemporaryDirectory() as tmp_dir:
            # 创建测试文件
            file1 = os.path.join(tmp_dir, 'file1.py')
            file2 = os.path.join(tmp_dir, 'file2.py')
            file3 = os.path.join(tmp_dir, 'file3.txt')
            with open(file1, 'w') as f:
                f.write('print("Hello World!")')
            with open(file2, 'w') as f:
                f.write('print("Hello Again!")')
            with open(file3, 'w') as f:
                f.write('Hello World!')

            # 测试 find_files 函数
            files = find_files(tmp_dir, ['.py'], [])
            self.assertEqual(files, [file1, file2])

    def test_find_start_file(self):
        # 创建临时文件
        with tempfile.TemporaryDirectory() as tmp_dir:
            # 创建测试文件
            file1 = os.path.join(tmp_dir, 'file1.py')
            file2 = os.path.join(tmp_dir, 'file2.py')
            with open(file1, 'w') as f:
                f.write('print("Hello World!")')
            with open(file2, 'w') as f:
                f.write('print("Hello Again!")')

            # 测试 find_start_file 函数
            start_file = find_start_file(tmp_dir, ['file1.py'])
            self.assertEqual(start_file, file1)

    def test_process_file(self):
        # 创建临时文件
        with tempfile.TemporaryDirectory() as tmp_dir:
            # 创建测试文件
            file1 = os.path.join(tmp_dir, 'file1.py')
            with open(file1, 'w') as f:
                f.write('print("Hello World!")')

            # 测试 process_file 函数
            content = process_file(file1)
            self.assertEqual(content.strip(), 'print("Hello World!")')

if __name__ == '__main__':
    unittest.main()

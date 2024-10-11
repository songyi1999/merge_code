import os
import re
import argparse
from typing import List, Tuple

VERSION = "0.1.3" 

def get_file_extension(file_path: str) -> str:
    file_name = os.path.basename(file_path)
    if file_name.startswith('.') and '.' not in file_name[1:]:
        return file_name  # Return the whole filename for hidden files without extensions
    return os.path.splitext(file_name)[1].lower()
def remove_comments(code: str, file_ext: str) -> str:
    if file_ext in ['.js', '.vue']:
        code = re.sub(r'//.*', '', code)
        code = re.sub(r'/\*[\s\S]*?\*/', '', code)
    elif file_ext == '.py':
        code = re.sub(r'#.*', '', code)
        code = re.sub(r"'''[\s\S]*?'''", '', code)
        code = re.sub(r'"""[\s\S]*?"""', '', code)
    return code

def remove_empty_lines(code: str) -> str:
    return '\n'.join(line for line in code.split('\n') if line.strip())

def process_file(file_path: str) -> str:
    encodings = ['utf-8', 'gbk', 'iso-8859-1', 'utf-16']
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as file:
                content = file.read()
            print(f"Successfully read file {file_path} with encoding {encoding}")
            file_ext = get_file_extension(file_path)
            content = remove_comments(content, file_ext)
            content = remove_empty_lines(content)
            return content
        except UnicodeDecodeError:
            continue
    print(f"Error: Unable to read file {file_path} with any of the attempted encodings.")
    return ""

def find_files(directory: str, include_exts: List[str], exclude_exts: List[str], exclude_dirs: List[str]) -> List[str]:
    file_list = []
    for root, dirs, files in os.walk(directory):
        # Remove excluded directories
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        for file in files:
            file_path = os.path.join(root, file)
            file_ext = get_file_extension(file_path)
            if (not include_exts or file_ext in include_exts) and file_ext not in exclude_exts:
                file_list.append(file_path)
    return file_list

def find_start_file(directory: str, start_files: List[str]) -> str:
    print("Searching for start files in directory:", directory)
    for root, _, files in os.walk(directory):
        print(f"Checking directory: {root}")
        print(f"Files in this directory: {files}")
        for start_file in start_files:
            if start_file in files:
                full_path = os.path.join(root, start_file)
                print(f"Found start file: {full_path}")
                return full_path
    print("No start file found.")
    return None

def merge_code(file_list: List[str], start_file: str, max_pages: int) -> Tuple[str, int]:
    if start_file:
        file_list = [f for f in file_list if f != start_file]
        file_list.insert(0, start_file)

    merged_code = ""
    total_lines = 0
    files_processed = 0

    for file_path in file_list:
        content = process_file(file_path)
        if not content:
            print(f"Skipping file {file_path} due to reading error")
            continue
        lines = content.split('\n')
        
        if total_lines + len(lines) > max_pages * 50:
            remaining_lines = max_pages * 50 - total_lines
            merged_code += '\n'.join(lines[:remaining_lines])
            total_lines += remaining_lines
            files_processed += 1
            break
        
        merged_code += content + '\n'  
        total_lines += len(lines)
        files_processed += 1

    return merged_code.strip(), files_processed

def main():
    parser = argparse.ArgumentParser(description="Merge source code files for software copyright application.")
    parser.add_argument("-d", "--directory", default=".", help="Working directory (default: current directory)")
    parser.add_argument("-s", "--start-file", help="Start file name (will be searched recursively)")
    parser.add_argument("-p", "--pages", type=int, default=60, help="Number of pages to extract (default: 60)")
    parser.add_argument("-i", "--include", help="Comma-separated list of file extensions to include")
    parser.add_argument("-e", "--exclude", help="Comma-separated list of file extensions to exclude")
    parser.add_argument("-o", "--output", default="out.txt", help="Output file name (default: out.txt)")
    parser.add_argument("-x", "--exclude-dirs", help="Comma-separated list of directory names to exclude")
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {VERSION}")
    
    args = parser.parse_args()

    directory = os.path.normpath(os.path.abspath(args.directory))
    start_files = ['login.vue', 'app.py', 'index.js','index.php','index.html']
    max_pages = args.pages
    include_exts = [f".{ext.strip().lower()}" for ext in args.include.split(',')] if args.include else []
    exclude_exts = [f".{ext.strip().lower()}" for ext in args.exclude.split(',')] if args.exclude else []
    exclude_dirs = [dir.strip() for dir in args.exclude_dirs.split(',')] if args.exclude_dirs else []
    
    default_exclude = ['.git','.lock','.out','.yaml','.txt','.md', '.csv','.gitignore',  '.sh','.bat','.xml', '.yml',  '.json','.png', '.jpg', '.jpeg', '.gif', '.bmp', '.ico', '.db', '.sqlite', '.bin', '.exe', '.dll', '.so', '.dylib']
    exclude_exts.extend([ext for ext in default_exclude if ext not in exclude_exts])
    
    output_file = args.output

    print("Working directory:", directory)
    print("Start files to search for:", start_files)
    print("Excluded file extensions:", exclude_exts)
    print("Excluded directories:", exclude_dirs)

    if args.start_file:
        start_file = find_start_file(directory, [args.start_file])
        if not start_file:
            print("Error: Start file '{}' not found in the directory tree.".format(args.start_file))
            return
    else:
        start_file = find_start_file(directory, start_files)
        if not start_file:
            print("Error: None of the default start files {} found in the directory tree.".format(start_files))
            return

    file_list = find_files(directory, include_exts, exclude_exts, exclude_dirs)
    merged_code, files_processed = merge_code(file_list, start_file, max_pages)

    with open(output_file, 'w', encoding='utf-8') as out_file:
        out_file.write(merged_code)

    print("Processed {} files.".format(files_processed))
    print("Merged code saved to {}".format(output_file))
    print("Total lines: {}".format(len(merged_code.split('\n'))))

if __name__ == "__main__":
    main()
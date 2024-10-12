import os
import re
import json
import argparse
from typing import List, Tuple
from fnmatch import fnmatch

VERSION = "0.2.3"

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

def find_files(directory: str, include_exts: List[str], exclude_dirs: List[str], exclude_files: List[str]) -> List[str]:
    file_list = []
    for root, dirs, files in os.walk(directory):
        # Remove excluded directories
        dirs[:] = [d for d in dirs if not any(fnmatch(d, pattern) for pattern in exclude_dirs)]
        for file in files:
            file_path = os.path.join(root, file)
            file_ext = get_file_extension(file_path)
            if file_ext in include_exts and not any(fnmatch(file, pattern) for pattern in exclude_files):
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
    print("Warning: No start file found.")
    return None

def merge_code(file_list: List[str], start_file: str, max_pages: int) -> Tuple[str, int]:
    if start_file and start_file in file_list:
        file_list.remove(start_file)
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

def load_config(config_file: str) -> dict:
    try:
        with open(config_file, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Config file {config_file} not found. Using default settings.")
        return {}
    except json.JSONDecodeError:
        print(f"Error parsing {config_file}. Using default settings.")
        return {}

def main():
    print("\nConfiguration file template (.merge_code.json):")
    config_template = {
        "directory": ".",
        "start_files": ["login.vue", "app.py", "index.js", "index.php", "index.html"],
        "pages": 60,
        "include": ".py,.js,.jsx,.ts,.tsx,.vue,.html,.css,.scss,.sass,.less,.php,.java,.c,.cpp,.h,.hpp",
        "exclude_dirs": "node_modules,dist,build,vendor,.git,.idea,.vscode,__pycache__,temp,tmp",
        "exclude_files": "*.min.js,*.min.css,package-lock.json,yarn.lock,pnpm-lock.yaml,postcss.config.js,vue.config.js,babel.config.js,.eslintrc.js,.merge_code.json",
        "output": "out.txt"
    }
    print(json.dumps(config_template, indent=2))
    parser = argparse.ArgumentParser(description="Merge source code files for software copyright application.")
    parser.add_argument("-d", "--directory", default=".", help="Working directory (default: current directory)")
    parser.add_argument("-s", "--start-file", help="Start file name (will be searched recursively)")
    parser.add_argument("-p", "--pages", type=int, default=100, help="Number of pages to extract (default: 100)")
    parser.add_argument("-i", "--include", help="Comma-separated list of file extensions to include (overrides default)")
    parser.add_argument("-o", "--output", default="out.txt", help="Output file name (default: out.txt)")
    parser.add_argument("-x", "--exclude-dirs", help="Comma-separated list of directory patterns to exclude (appends to default)")
    parser.add_argument("-e", "--exclude-files", help="Comma-separated list of file patterns to exclude (appends to default)")
    parser.add_argument("-c", "--config", default=".merge_code.json", help="Path to configuration file (default: .merge_code.json)")
    parser.add_argument("-v", "--version", action="version", version=f"%(prog)s {VERSION}")
    
    args = parser.parse_args()

    config = load_config(args.config)

    directory = os.path.normpath(os.path.abspath(args.directory or config.get('directory', '.')))
    start_files = config.get('start_files', ['login.vue', 'app.py', 'index.js', 'index.php', 'index.html'])
    max_pages = args.pages or config.get('pages', 60)
    default_include = ['.py', '.js', '.jsx', '.ts', '.tsx', '.vue', '.html', '.css', '.scss', '.sass', '.less', '.php', '.java', '.c', '.cpp', '.h', '.hpp']
    include_exts = [f".{ext.strip().lower()}" for ext in (args.include or config.get('include', '')).split(',')] if args.include or 'include' in config else default_include
    
    default_exclude_dirs = ['node_modules', 'dist', 'build', 'vendor', '.git', '.idea', '.vscode', '__pycache__', 'temp', 'tmp']
    user_exclude_dirs = [dir.strip() for dir in (args.exclude_dirs or config.get('exclude_dirs', '')).split(',')] if args.exclude_dirs or 'exclude_dirs' in config else []
    exclude_dirs = list(set(default_exclude_dirs + user_exclude_dirs))

    default_exclude_files = [ 'index.css' ,'*.min.js', '*.min.css', 'package-lock.json', 'yarn.lock', 'pnpm-lock.yaml', '*.config.js', 'vue.config.js', 'babel.config.js', '.eslintrc.js', '.merge_code.json']
    user_exclude_files = [file.strip() for file in (args.exclude_files or config.get('exclude_files', '')).split(',')] if args.exclude_files or 'exclude_files' in config else []
    exclude_files = list(set(default_exclude_files + user_exclude_files))
    
    output_file = args.output or config.get('output', 'out.txt')

    print("Working directory:", directory)
    print("Start files to search for:", start_files)
    print("Included file extensions:", include_exts)
    print("Excluded directories:", exclude_dirs)
    print("Excluded files:", exclude_files)

    if args.start_file:
        start_file = find_start_file(directory, [args.start_file])
    else:
        start_file = find_start_file(directory, start_files)

    file_list = find_files(directory, include_exts, exclude_dirs, exclude_files)
    
    if not file_list:
        print("Error: No files found matching the specified criteria.")
        return

    merged_code, files_processed = merge_code(file_list, start_file, max_pages)

    with open(output_file, 'w', encoding='utf-8') as out_file:
        out_file.write(merged_code)

    print("Processed {} files.".format(files_processed))
    print("Merged code saved to {}".format(output_file))
    print("Total lines: {}".format(len(merged_code.split('\n'))))

   

if __name__ == "__main__":
    main()
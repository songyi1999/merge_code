import os
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

def read_requirements():
    if os.path.exists("requirements.txt"):
        with open("requirements.txt", "r", encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip() and not line.startswith("#")]
    return []

setup(
    name="merge_code",
    version="0.1.0",
    author="sy",
    author_email="songyi1999@gmail.com",
    description="A tool to merge source code files for software copyright application",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/songyi1999/merge_code",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=read_requirements(),
    entry_points={
        "console_scripts": [
            "merge_code=merge_code.main:main",
        ],
    },
    include_package_data=True,
    package_data={
        "merge_code": ["*.txt", "*.md"],
    },
    extras_require={
        "dev": ["pytest", "flake8", "mypy"],
    },
    project_urls={
        "Bug Reports": "https://github.com/songyi1999/merge_code/issues",
        "Source": "https://github.com/songyi1999/merge_code",
    },
)
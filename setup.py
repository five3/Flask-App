#!/usr/bin/env python
# coding=utf-8
import os
from setuptools import setup, find_packages
from flask_app import __version__
# python setup.py sdist
# python setup.py bdist
# python setup.py bdist_egg
# python setup.py bdist_wheel
# twine upload dist/*0.1.4*


def get_desc():
    with open('README.md', 'r', encoding="utf-8") as f:
        return f.read()


def find_data_files(root):
    data_files = []
    data_files_root = f'{root}/templates'
    for fl in os.walk(data_files_root):
        dir, sub_dir, files = fl
        if dir.endswith('__pycache__'):
            continue
        for file in files:
            data_files.append(f'{dir}/{file}')

    return data_files


setup( 
    name="Flask-Application",
    version=__version__,
    keywords=["Flask", "Flask App", "Flask Project"],
    description="create application template for flask.",
    long_description="create application template for flask.",
    license="GUN V3",

    url="https://github.com/five3/Flask-App",
    author="five3",
    author_email="five3@163.com",

    package_dir={'flask_app': 'flask_app'},         # 指定哪些包的文件被映射到哪个源码包
    packages=find_packages(),       # 需要打包的目录。如果多个的话，可以使用find_packages()自动发现
    include_package_data=True,
    package_data={'flask_app': ['templates/*']},
    py_modules=[],          # 需要打包的python文件列表
    data_files=find_data_files('flask_app'),          # 打包时需要打包的数据文件
    platforms="any",
    install_requires=[      # 需要安装的依赖包
        'flask>=1.0.2'
    ],
    scripts=[],             # 安装时需要执行的脚本列表
    entry_points={
        'console_scripts': [    # 配置生成命令行工具及入口
            'flask-app = flask_app:main'
        ]
    },
    classifiers=[           # 程序的所属分类列表
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU General Public License (GPL)",
    ],
    zip_safe=False
)

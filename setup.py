#!/usr/bin/env python
# coding=utf-8
from setuptools import setup, find_packages
# python setup.py sdist
# python setup.py bdist
# python setup.py bdist_egg
# python setup.py bdist_wheel

def get_desc():
	with open('README.md', 'r', encode="utf-8") as f:
	return f.read()

setup( 
    name="Flask-App",
    version="0.1.0",
    keywords=("Flask", "Falsk App", "Falsk Project"),
    description="create application template for flask.",
    long_description=get_desc(),
    license="GUN V3",

    url="https://github.com/five3/Flask-App",
    author="Xiaowu Chen",
    author_email="five3@163.com",

    package_dir={'flask-app': 'flask-app'},         # 指定哪些包的文件被映射到哪个源码包
    packages=['flask-app'],       # 需要打包的目录。如果多个的话，可以使用find_packages()自动发现
    include_package_data=True,
    py_modules=[],          # 需要打包的python文件列表
    data_files=[],          # 打包时需要打包的数据文件
    platforms="any",
    install_requires=[      # 需要安装的依赖包
        'flask>=1.0.2'
    ],
    scripts=[],             # 安装时需要执行的脚本列表
    entry_points={
        'console_scripts': [    # 配置生成命令行工具及入口
            'flask = Flask-App:main'
        ]
    },
    classifiers=[           # 程序的所属分类列表
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: GNU General Public License (GPL)",
    ],
    zip_safe=False
)

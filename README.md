# 介绍
Flask-App是专门给Flask提供应用初始化创建的工具，通过该工具可以快速地创建一个Flask的初始项目/应用。
新创建的项目/应用会包含良好的目录结构和基础的项目配置信息，无需再通过手工的方式创建这些基础目录和文件。
如果你是`django`用户，那么你一定熟悉`django-admin`。没错！`Flask-App`就是`Flask`版本的`django-admin`。

# 安装
```bash
pip install Falsk-App
```

# 使用
## 创建多应用的项目
Flask的多应用项目模板具有以下特点：
- 基于`blueprint`进行`app`的路由和管理
- 每个`app`都会有自己的`mvc`结构和`templates`目录
- 集成了`gunicorn`作为正式环境的启动方式
- 集成了日志配置，通过`current_app.logger`对象直接使用
- 支持新增`app`

```bash
flask startproject pj01
```
该命令执行完成之后就会在当前目录创建`pj01`的项目目录，其具体结构如下：
```bash
|-- pj01
    |-- apps
          |-- pj01
                |-- controller
                    |-- __init__.py
                |-- model
                    |-- __init__.py
                |-- view
                    |-- __init__.py
                    |-- app.py
                    |-- index.py
                |-- templates
                    |-- home.html
                |-- __init__.py
          |-- logs
          |-- static
                |-- favicon.ico
          |-- utils
                |-- __init__.py
                |-- constants.py
          |-- __init__.py
    |-- __init__.py
    |-- config.py
    |-- gconfig.py
    |-- manage.py
    |-- wsgi.py
    |-- requirements.txt
    |-- startserver.sh
```
创建完Flask项目之后，在命令行直接进入到应用的主目录，然后执行启动命令：
```bash
python manage.py 8000
python manage.py runserver 8000
```
启动完成之后可以执行访问`http://localhost:8000/pj01/`来访问项目的主目录。

在开发完项目之后，上线时可通过执行`startserver.sh`脚本来启动`gunicorn`服务。默认启动的端口号为`8000`，如果需要修改端口号，可在`gconfig.py`文件里修改`bind`字段。

## 创建单应用的工程
```bash
flask createapp app01
```
暂未实现

# TODO
- 支持为多应用项目新增app
- 支持创建单应用项目
- 添加SQLAlchemy模型模板

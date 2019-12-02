![关注二维码](https://www.testqa.cn/static/banner.png)

> 如果你是`django`用户，那么你一定熟悉`django-admin`。没错！`Flask-App`就是`Flask`版本的`django-admin`。

# 介绍
`Flask-Application`是专门给`Flask`提供项目初始化的工具，通过该工具可以快速地创建一个`Flask`的初始项目/应用。新创建的项目/应用会包含良好的目录结构和基础的项目配置信息，无需再通过手工的方式创建这些基础目录和文件。

# 安装
```bash
pip install Falsk-Application 
```

# 快速开始
```bash
flask-app startproject demo_pj
cd demo_pj
python manage.py 8000
```
使用你喜欢的浏览器访问`http://localhost:8000/demo_pj/`，你就可以看到启动好首页。
![hello_flask](https://www.testqa.cn/static/hello_flask.png)

# 使用说明
## 多应用项目
Flask的多应用项目模板具有以下特点：
- 基于`blueprint`进行`app`的路由和管理
- 每个`app`都会有自己的`mvc`结构和`templates`目录
- 集成了`gunicorn`作为正式环境的启动方式
- 集成了日志配置，通过`current_app.logger`对象直接使用
- 支持新增`app`

### 创建方式
```bash
flask startproject demo_pj
```
该命令执行完成之后就会在当前目录创建`demo_pj`的项目目录，其具体结构如下：
```bash
|-- demo_pj
    |-- apps
          |-- demo_pj
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
                |-- decorators.py
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
cd demo_pj
python manage.py 8000
# or
python manage.py runserver 8000
```
启动完成之后可以执行访问`http://localhost:8000/demo_pj/`来访问项目的主目录。

### 线上部署
Flask-App集成了`gunicorn`来作为生成环境的部署方式，后台以`多进程+gevent`的方式提供并发支持,线上部署时使用如下命令：
```bash
sh startserver.sh
```
默认启动的端口号为`8000`，如果需要修改端口号，可在`gconfig.py`文件里修改`bind`字段。

> 通常在`gunicorn`服务之前还需要添加`nginx`代理服务，除了直接处理静态文件，还同时转发请求给后台的`gunicorn`服务。

## 单应用工程
```bash
flask createapp app01
```
暂未实现

# TODO
- 支持为多应用项目新增app
- 支持创建单应用项目
- 集成RESTfulAPI
- 集成flask-sqlarchemy
- sqlarchemy模型自动生成

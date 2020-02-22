# 存包处

### 项目包含以下几个模块

* web (官网页面、小程序API接口、数据管理后台)
* crawler (数据采集)

### 部署方式

* 构建虚拟环境

    `virtualenv env`

    `source env/bin/activate`

* 安装依赖

    `pip install -r requirements.txt`

* 运行服务

    `python manage.py runserver --settings=cunbaochu.settings.dev`

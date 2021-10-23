# 存包处

存包处是一个微信小程序，用于查找附近的行李寄存点

![二维码](./static/img/qr.png)

**此仓库为其对应后端代码**

系统搭建采用了 AWS 的 EC2，Elasticsearch Service 以及阿里云的 OSS

数据主要采集自网络，部分由店家贡献

### 项目包含以下几个模块

* web
    * 官网页面 www.cunbaochu.com
    * 小程序API接口 cbc.wanggezhi.com
    * 数据管理后台 /admin
* crawler 数据采集

### 部署方式

* 构建虚拟环境

    `virtualenv env`

    `source env/bin/activate`

* 安装依赖

    `pip install -r requirements.txt`

* 运行服务

    `python manage.py runserver --settings=cunbaochu.settings.dev`

### Refs

* 小程序代码 https://github.com/iamsk/cunbaochu-mini-program

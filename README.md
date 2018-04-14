# overview

##     本项目用于爬取wannimal网站的相册

>     老司机开车了 备好营养快线 以防翻车


#### 人员编制：

> ##### Py老司机：

名字 | 职位
---|---

江南皮革厂厂长

####   使用帮助:

###### 注:

- 本项目使用的python版本是:   Python 3.6.1 请自行安装 3.6.1版本
  - mac端使用: brew install python3
  - centos系列使用: yum install epel-release && yum install -y python3
  - ubuntu系列使用: apt install python3
- 本项目建议使用Pycharm进行开发
  - pycharm下载地址: https://www.jetbrains.com/pycharm/download/
  
  
**文件介绍:**

##### wanima.py:

    入口
    执行方法: python3  wanima.py

downfiles.py
    
    从网页中分析出图片地址，并下载图片文件
mongodbconn.py

    mongo的配置文件
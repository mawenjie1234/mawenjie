## ANR python 脚本

1. [看各个版本有哪些类型的anr](./resource/anr_statistics_by_version.py) 
2. [查看详细堆栈anr脚本](./resource/anr_statistics_by_version.py)



## 使用前准备

1. selenium  下载，命令行 pip install selenium
2. chromedriver 安装， [根据自己chrom浏览器版本下载](http://chromedriver.chromium.org/downloads)
3. 修改脚本中CHROME_DRIVER_PATH， 改成自己下载好的路径
4. 修改 GOOGLEPLAY_URL 。打开google 网站上anr详细列表，复制url，并且删除其中version
5. 修改GOOGLEPLAY_ACCOUNT_NAME。 就是登录邮箱
6. 修改GOOGLEPLAY_ACCOUNT_PWD，登录密码
7. APP_VERSION 需要查询的版本，这就是为啥要删除 GOOGLEPLAY_URL 的原因，这个地方自己给加了

## 运行

* 使用python 2.7跑
* python anr_statistics_by_version.py

## 结果

会在当前文件夹下生成csv 表



感谢 hongming.zhang


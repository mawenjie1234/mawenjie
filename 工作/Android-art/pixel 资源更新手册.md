# 资源更新

## resource/Pictures 更新注意事项

* 新加的图经过 [tingpng](https://tinypng.com/) 压缩
* 不要删除Fantasy_25.png 这张图。
* 一个版本新加的图最好打成一个zip包

## resource/Config 更新注意事项

### 资源表 picture_auto_refresh.csv 

1. 在magic 2.3.11 版本之前，资源表中请添加 Fantasy_25.png， 并且不要删除。
2.  任何展示表都要在在资源表中存在，如果不存在，无论如何都不会展示出来。
3. 资源表新加一列的时候看看文件会变大多少， 变大很多需要通知 dev leader，确认能不能不加这一列。


## 多语言 更新注意事项
文件 ： resource/ContentLocalized/ContentLocalized.csv

第一列为ID 第二列到第八列依次为 简体中文、英语、俄语、葡萄牙语、西班牙语、土耳其语、越南语

1. 语言顺序不可改动，否则显示语言会错乱
2. 对应的翻译不可以为空，否则会显示代码里的默认值



# 资源上传Git
---

1. 只要修改资源后，都需要使用建明工具打包，更新 resource/index.json 文件，可以在sourcetree 上看到变更，
如果没有变更，应该意识到打包错误，并且不能上传git，找相关dev 查看问题

2. [打包工具地址](https://files.ihandysoft.com/index.php/apps/files/?dir=/045/045_%20tools/folder_synch%20%E7%94%9F%E6%88%90json%E6%96%87%E4%BB%B6%2B%E6%A3%80%E6%9F%A5%E5%9B%BE%E7%89%87error/%E6%89%93%E5%8C%85%E5%B7%A5%E5%85%B7-json%E5%8F%98%E5%8C%96&fileid=13686988)


# 资源上传远端服务器
---

1. 更新线上某个版本的资源文件后，用户冷启动会下载远端文件， 第二次冷启动才能使用最新的配置文件，
2. 上传远端后测试远程更新，确保用户能更新到文件。有可能某一个文件没有访问权限导致整个无法更新。 
3. 资源上传请找 hongyuan.jia


# 上线

## 修改config 中的配置

上线确保config 中 CGFolder_UER 跟随版本更新

例如 ： https://s3.amazonaws.com/dev-config-appcloudbox/045games/Magic/Magic_A/picture/X/resource/

X请跟随 build.gradle 中的 versionCode

## resource/index.json
如果 index.json 文件对比上一个版本发生变化，请修改 文件中 Data -> version， 确保统计正确。
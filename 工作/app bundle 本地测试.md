aab包不能直接安装运行，需要使用[bundletool](https://drive.google.com/file/d/1E61hDrxmKKQ6Uk5dIgrJx4OvuT681Km_/view?usp=sharing)工具

使用下面命令将aab转化为apks

java -jar bundletool-all-0.10.0.jar build-apks --bundle=app.aab --output=app.apks

再使用下面命令安装apks

java -jar bundletool-all-0.10.0.jar install-apks --apks=app.apks


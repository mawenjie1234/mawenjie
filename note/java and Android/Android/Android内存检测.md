# 例子
连接手机运行app

打开终端输入 adb shell dumpsys meminfo com.bongolight.pixelcoloring  然后回车


# PM如何判断有问题

开启app 的进入主页 和 进行一些操作后回到主页后，都输入上面指令， 获取类似上面图中的信息。

关注App Summary 下的TOTAL/1024。如果差别很大，就发生了内存泄漏。

例如上图中TOTAL是 188375， 除以1024后是 183.9M，  经过一段时间测试后，回到界面发现变化为 258375， 那么就是内存泄漏

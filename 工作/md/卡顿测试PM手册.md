# 卡顿检查方法
## GT
## SM

# SM 介绍

## SM 工作原理

    主线程每隔16.6毫秒会加一个数a，SM会启动一个子线程。子线程也会每隔16.6ms加一个数b，并且去检查主线程数字a是否和子线程b一样，如果不一样，那么就表示主线程一直忙于处理别的事情，就表明发生了卡顿。

## SM 输出
    卡顿发生的时候，子线程会把主线程的堆栈获取并输出到手机里面
    
*  目前所有产品都会在手机的 sdcard/pixel/ 下， 按照打开app 时间来命名文件名
    * 精简版 日期+Simplify_SM.txt
    * 全部日志  日期+SM.text

## SM 限制

* 因为要把卡顿日志输出到sd卡下面，所以需要给app 读写sd卡权限，app 打开的时候会索取权限，所以在获取权限之前，sm 都无法记录卡顿点。可以给app 读取sd卡权限后，再次冷启动，就会有SM日志输出

# SM release版本

默认情况下，SM在release 下不会初始化，也不会有config 配置(防止配错)，因此如果需要在release 下使用SM，请按照下面步骤操作

* 在ApplicationBase.java 文件中找到以下代码

```
private void initSMUtils() {
        if (!HSApplication.isDebugging) {
            return;
        }
        SMUtils.init();
        SMUtils.setNeedMonitorActivityChange(true);
        SMUtils.start();
    }
```

* 删除掉 以下代码

```
  if (!HSApplication.isDebugging) {
            return;
        }
```
* 打release包
# Service

## 生命周期以及使用
![694018-99da2307c5d69134]($resource/694018-99da2307c5d69134.jpg)

### onCreate

* service 创建的时候调用，service 在系统中只有一个实例。
* service 默认是在主线程执行，因此最好是在onCreate 里面创建一个线程，并且之后的操作都在这个线程内执行
```
@Override
public void onCreate() {
    // TODO: It would be nice to have an option to hold a partial wakelock
    // during processing, and to have a static startService(Context, Intent)
    // method that would launch the service & hand off a wakelock.

    super.onCreate();
    HandlerThread thread = new HandlerThread("IntentService[" + mName + "]");
    thread.start();

    mServiceLooper = thread.getLooper();
    mServiceHandler = new ServiceHandler(mServiceLooper);
}

```

### onStart

* 这个方法是调用StartService 的时候调用的， 可以拿到intent在已经初始化好的子线程做事情。

### onBind

* 是启动模式bindService 的生命周期回调。

* [ ] bindservice 的时候，同一个Application 和不同的Application 在onServiceConnected 的写法会不会有不同。


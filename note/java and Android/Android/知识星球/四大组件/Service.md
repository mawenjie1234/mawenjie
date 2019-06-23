**Service**

## 使用场景
* Service是四大组件，可以很好的创建进程
* Service主要做一些耗时操作，不过一般应用的耗时操作也不会用到Service，大多数用于多进程，sdk等。
* 耗时操作，可以自己封装一个线程池，因为Service的使用没有线程池使用的方便。

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

* [x] bindservice 的时候，同一个Application 和不同的Application 在onServiceConnected 的写法会不会有不同。

下面是aidl的写法
```
public class MyService extends Service {
    Binder mService = new IMyAidlInterface.Stub() {

        @Override
        public void basicTypes(int anInt, long aLong, boolean aBoolean, float aFloat, double aDouble, String aString) throws RemoteException {

        }
    };

    public MyService() {
    }

    @Override
    public IBinder onBind(Intent intent) {
        // TODO: Return the communication channel to the service.
        return mService;
    }
}
// call in activity
bindService(new Intent(this, MyService.class), new ServiceConnection() {
    @Override
    public void onServiceConnected(ComponentName name, IBinder service) {
        mServiceProxy = IMyAidlInterface.Stub.asInterface(service);
    }

    @Override
    public void onServiceDisconnected(ComponentName name) {

    }
}, 0);
```


### onRebind
多次调用bindService 的时候，和unBindService 的时候会调用，一般做数据统计。

### onUnbind
调用onBindService的时候调用
* [x] 已经onBind的情况下，再次unBind会不会发生
 onUnBInd只会调用一次，就是和他绑定的最后一个context 销毁的时候。

### onDestroy

* 调用stopService 或者unBindService 后，Service 会销毁，但是根据情况而定。
* unBind和bind要一起用。

### onStartCommand

service的启动方式，
* START_NOT_STICKY service被回收不会自动启动。
* 

## Service 在复杂场景下的生命周期回调
[学习地址](https://blog.csdn.net/qq_22804827/article/details/78609636)

* 当startService单独使用时，即使对应的`startService`时传入的Context被销毁，Service也还是会处于运行状态。
* 无论多少个Activity绑定了Service，但是onBind()只会执行一次，也就是Service首次被绑定时会执行，onUnbind()也是如此，即最后一个Context失效后，才会执行onUnbind()（Activity主动调用unbindService或者被onDestory）。
而如果由于Activity没有主动调用unbindService与Serivice解绑，这样会造成内存泄漏

* 当只有一个Activity与Service进行bindService而没有startService，则Activity在onDestory前如果没有主动调用unbindService与Service解除绑定，或者只是直接调用stopService，则需要等到Activity被销毁，也就是与Service绑定的Context失效时，Service才会执行onUnbind()，之后会自动调用onDestory()进行销毁。

* 如果是多个Activity都绑定了同一个Service绑定，且没有执行过startService，当其中一个Activity onDestory或者进行unbindService之后，其与Service进行bindService时的Context就会失效，而当最后与Service绑定的Contxet失效后，Service才会执行onUnbind()，之后会自动调用onDestory()进行销毁。

* 如果是同时有多个Activity对Service进行了startService和bindService，如果没有显示调用过stopService，则当所有与Service绑定的Context失效后，Service不会被销毁，会一直在后台运行，因为有主动调用了startService，此时必须主动调用stopService或者在Service中调用stopSelf才能将其销毁；而如果在一个或者多个Context失效前主动调用了stopService或者在Service中调用stopSelf，则需要等到最后一个Context主动与Service进行unbindService或者失效后，才会能使Service执行onDestory。

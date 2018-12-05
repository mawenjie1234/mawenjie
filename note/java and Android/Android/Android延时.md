# Android延时操作
## Handler PostDelay
* 注册
```
  Handler handler = new Handler()
   Runable runable = new Runable(){
      public void run(){

      }
    }
   handler.postDelay(runable, delayTime)   
```

* 取消
   
    handler.removeCallBack(runable)
   
* 如果频繁的延时，可以随时remove 随时重新postDelay
---

## new Thread

```
new Thread(new Runnable(){   
public void run(){   
    Thread.sleep(delaytime);   
    handler.sendMessage(); //execute the task
    }   
}).start
  ```

## Timer And TimerTask
  * 注册
    ```
    Timer timer = new Timer()；
    TimerTask task = new TimerTask(){
      public void run(){}
    }
    timer.schedule(task, delayTime);
    ```
  * 取消
    ```
    timer.cancle();
    timer.purge();
    ```


 * 注意 ：如果同一个timer 已经cancle 了，那么就不能重新schedule，需要重新搞 timer 和 timerTask
 

# 那这些有什么不同呢

    
  
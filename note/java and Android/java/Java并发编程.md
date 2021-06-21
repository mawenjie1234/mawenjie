## 09 Java线程生命周期

## 通用线程生命周期

​	1初始 - 2可运行 - 3运行  - 5终止

​					- 4休眠 - 

<img src="Java%E5%B9%B6%E5%8F%91%E7%BC%96%E7%A8%8B.assets/9bbc6fa7fb4d631484aa953626cf6ae5.png" alt="img" style="zoom: 33%;" />

* 初始状态：在编程语言层创建，真正的线程还没有创建
* 可运行状态：操作系统线程已经创建，可以分配CPU
* 运行状态：被分配到CPU
* 休眠状态：调用了阻塞API（IO）/ 条件变量（等待某个事件），释放CPU使用权，切不会被分配CPU
* 终止状态：不会切换到其他状态，

## Java线程生命周期

<img src="Java%E5%B9%B6%E5%8F%91%E7%BC%96%E7%A8%8B.assets/3f6c6bf95a6e8627bdf3cb621bbb7f8c.png" alt="img" style="zoom:48%;" />

​	java中的blocked、waiting、timed_waiting 都是休眠状态，进入这个状态，不会分配CPU



#### Runnable状态：

	 * 系统调用阻塞API时候，例如IO，**java线程状态还是runnable，操作系统线程变为休眠状态**。java不考虑操作系统的调度
	 * 

#### 各个状态转换：

* Runnable和blocked转换
  * 等待synchronize的隐式锁，等待线程就从runnable变到blocked，获取到锁后，又恢复到runnable
* Runnable <--> Waiting
  * 获得锁的线程，调用wait
  * 调用Thread.join: Thread a, a.join 表示当前线程会等待线程a执行完，此时变为waiting, 等待结束变成runnable
  * LockSupport.park() ：java并发包中的锁，都是由他实现的，调用LockSupport.unPack(thread), 又变成runnable
* Runnable <-->  TimedWaiting
  * 带有超时的thread.sleed(n)、wait(n)、join(n)、LockSupport.packNanos(block, long deadline)、LockSupport.packUntil(deadline)
* New <--> Runnable：只要调用线程对象的start
* Runnable <--> Terminated:当run方法执行完、抛出异常、调用stop、调用interrupt

#### interrupt 和 stop

​	Stop：stop会让线程终止，如果自己写的ReentrantLock锁，没有调用unlock，就会死锁，比较危险

​	interrupt：通知线程，线程也可以无视

  * 通过异常：

      * 线程处于wait状态时候，调用interrupt会让线程转为Runnable，并且触发InterruptedException
      * 当线程处于Runnable，阻塞在 java.nio.channels.InterruptibleChannel 上时，调用线程 A 的 interrupt() 方法，A 会触发 java.nio.channels.ClosedByInterruptException 这个异常；
      * 阻塞在 java.nio.channels.Selector 上时，调用线程 A 的 interrupt() 方法，线程 A 的 java.nio.channels.Selector 会立即返回。

    ```java
    while(true) {
      if(th.isInterrupted()) {
        break;
      }
      // 省略
      try {
        Thread.sleep(100);
      }catch (InterruptedException e)｛
        // 如果catch住了，需要重新设置interrupt，
        // 抛出异常后，中断标志会自动清除
        Thread.currentThread().interrupt(); 
        e.printStackTrace();
      }
    }
    ```

    

		* 通过主动检测：线程在Runnable中，检查isisInterrupted
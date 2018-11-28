## 需要测试的点
### 性能测试的点
* getResource 获得所有picture 的列表
* getCategoryDisplay 获得一个category下所有的id，需要测试多大的文件有多少时间。
* updatePictureMeta， 更新DB中picture表中一个行的数据。


### 存储测试 
* 存储都要看下次启动后是否和上次set保持一致


#### PictureMeta
* PictureMeta setFinished 并且Picture 中的数据也应该所有改变
* setLocked  测试解锁信息，// todo 询问是否需要和myArt 结合一起。
* setMyArt  添加到myArt表中。
*  PaintStatus picture 状态是互斥的，是否设置后一定是这样的。

#### Picture 本地存储测试
* 画点测试
    1. 每次可能随机若干个点，并且调用画点函数，之后查看这些点是否已经被画上
    2. 随机几个透明点画，看是否有问题
    3. 画错几个点，看是否画上了，没有画上是对的。
* save() 保存用户的画点的顺序测试， 用户画完的图测试


### callback 测试

* PictureMeta 的call back 设置之后在call back的时候删除 检查call back的个数
* set 进去的call back 设置为null后，查看call back 里面是否还持有这个对象，不持有才对
* Picture 类和Picturemeta 中都得有


### 多线程测试

* 先想一想多线程操作同一个meta是否有问题。

----

基于以上的需要测试的点，需要做以下测试

* 全路径覆盖的方法
    * if else
    * 接口
    
* 冷启动和热启动场景
* 线程
* 性能
    * 流畅度
    * 耗电
    * 内存
        * 有没有泄漏
        * 峰值多少
  * 临界值测试
    
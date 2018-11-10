# 说明
  20版本是18的版本上升级了 framework ,  golden eye , 添加隐私。

# app : build.gradle
  1. constraint-layout 1.0.2 -> 1.1.3
  2. golden eye 9.27.004 -> 10.0.001
# assets :
  1. hotImage.plist localImage.plish  被修改
 
1 bind view hold
2 pictureLoader 对比一下。
3 画笔相关的数据结构变化。


# 1.0.18  -> 1.1.19  测试说明 ： 都使用release 版本跑分， 都使用最新的golden eye， 10.09.001， 注释掉 Drawing activity initBannerAd
 1. 1.0.18 680f8f1c058f7cbd620d9ffdea35cd8525331d2c
 
 501270216d7764c1e238be1bd2fce25770768a41






1. 打一个和15版本一样的golden eye， 坚决不能带启动游戏在主线程init的广告。
2. 加上旭哥的启动延时操作，并且数据再子线程做，等数据好了之后， 再出介绍界面，或者关闭新手引导。
3. 加上ImageLoad 的新代码，让界面滑动更加流畅。
4.  解决一波GT上检测出来的卡顿。
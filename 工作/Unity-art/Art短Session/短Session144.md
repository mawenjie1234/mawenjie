## 短Session 对用户是否有影响

# ![image](%E7%9F%ADSession144.assets/image.png)

结论： 

1. 短Session占比用户多的人均时长（13）是平均（47min）的27%，对数据有极大的影响
2. 短Session 用户的冷启动占比（45%）更高，推测可能是程序异常导致用户频繁冷启动。
3. 短Session占比50% 以上占总人数比例的15%，说明短Session用户其实不少，应该是必须要优化。

## todo

* 看数据
  * ES上短session 看看Android 4.4的。因为看Unity上的crash 4.4的用户特别多。
  * es上看短session用户picture click 和picture enter 的比例。以确定是否在这段时间内退出的比较多。
  * 关注0~3s、 3~10s，在哪个界面,  加上获取当前页面出错的数，因为获取页面出错的就是在启动。
  * 尝试关闭线上一个很少用户的广告，看看短 session的数据变化，用于定位是否是因为广告跳转出去后，回到app后马上crash

* 代码修改
  * 1.5.0  icon 下载队列变成1个，进入主玩暂停icon下载队列。
  * 区分不了session 是在后台发的。
  * session start 都使用unity 的onFocus
  * 启动end，看看页面到底有没有展示。

### 存疑

* 有些用户当日绘画时间0， 但是banner 展示了50多次。
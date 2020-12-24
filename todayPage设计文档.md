### PRD文档链接 

​    [PRD链接](https://wiki.atcloudbox.com/pages/viewpage.action?pageId=29164872)

### 影响范围

* 首页新数据层
* banner 获取推荐的一张图
* TodayUI 修改，pad适配，刘海屏适配
* 没有二级页面，新页面埋点

### 输入参数

1. 推荐的图片，推荐的分类，以及分配下的图
2. *这些数据已有的写出 类-方法*
3. *没有的写出新增的 类-方法，实现逻辑写在下部分*

### 开关：

1. today_new_tag_switch 新老页面开关
2. 运行时图片资源走之前的pictureItem

### 埋点：

1. 查看PRD文档

### 逻辑处理

1. 流程图

   1. <img src="todayPage%E8%AE%BE%E8%AE%A1%E6%96%87%E6%A1%A3.assets/image-20201223200417830.png" alt="image-20201223200417830" style="zoom:67%;" />

2. *页面更新逻辑*

   1. <img src="todayPage%E8%AE%BE%E8%AE%A1%E6%96%87%E6%A1%A3.assets/image-20201223200030762.png" alt="image-20201223200030762" style="zoom:70%;" />

3. 新页面UI实现

   <img src="todayPage%E8%AE%BE%E8%AE%A1%E6%96%87%E6%A1%A3.assets/image-20201223201443613.png" alt="三个页面节点排列" style="zoom:50%;" />

   ##### 新页面两层ScrollView 以及节点信息

   * 第一层ScrollView负责三个page左右滑动，第二层负责页面内部上下滑动
   * TodayItem84表示是和banner+tag相同高度空节点，用于列表页占位

   

   ##### 三个页面更新和top初始化

   <img src="todayPage%E8%AE%BE%E8%AE%A1%E6%96%87%E6%A1%A3.assets/image-20201223204930391.png" alt="image-20201223204930391" style="zoom:67%;" />

   * TodayPageScrollView 是第一层滑动列表，负责三个页面左右滑动
   * TodayTop 封装了banner和 tag，负责接收当前上下滑动列表位置更新
   * PageTodayNewCategory 是一个个页面，负责页面中显示pictureMeta

   ##### 页面上下滑动，左右页面跟随滑动流程

   <img src="todayPage%E8%AE%BE%E8%AE%A1%E6%96%87%E6%A1%A3.assets/image-20201224110741964.png" alt="image-20201224110741964" style="zoom:67%;" />

   1. TodayPageScrollView 接收到move操作的时候，更新内部三个页面内存位置信息，并触发TodayPageSelected
   2. PageToday 收到选中后，触发TodayTop注册新页面上下滑动通知
   3. TodayTop收到上下滑动通知更新follow page的位置，以确保其他页面跟随top移动

4. 新老页面适配新数据

   1. <img src="todayPage%E8%AE%BE%E8%AE%A1%E6%96%87%E6%A1%A3.assets/image-20201223200518121.png" alt="image-20201223200518121" style="zoom:60%;" />

### 测试用例

1. *开关：新老页面配置正确，tag读取个数正确
2. *适配 :
   1.  新页面pad页面一行三个，phone一行两个
   2. 刘海屏适配正常
   3. 一键回到顶部直接回到banner位置，
3. tag 可以显示多语言
4. 快速滑动页面，快速点击上方tag，动画正常，列表页显示正常
5. today页面内存和上版本基本持平，卡顿和上版本正常，页面切换无卡顿
6. 数据上报正常
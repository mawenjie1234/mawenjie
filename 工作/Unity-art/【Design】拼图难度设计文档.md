### PRD文档链接 

​    https://wiki.atcloudbox.com/pages/viewpage.action?pageId=25895680

### 影响范围

  拼图玩法本身

### 输入参数

1. 描述画笔使用哪个模板切图 新增64 100，之前重命名为36， 目录 Shader&Material/Jigsaw/data
2. 远端画笔顺序新增64、100， 之前重命名为36 目录 {pictureMeta.GetResourceBaseUrl()}_pdata36.json

### 开关：

1. jigsaw_difficulty 未开始的图进入时拼图块个数

### 埋点：

1. 参考PRD文档

### 逻辑处理

#### 需求拆解

1. 块的基础逻辑需要支持更多块，不限于36块
2. 64和36块画笔下，就是拖拽到panel区域后，画笔的大小不同
3. 画笔栏筛选：将当前画笔全部移出屏幕外，更新新的画笔，然后做回到位置动画
4. 筛选能在100块情况下筛选出左边和右边的画笔
5. panel区域可以支持区分左右两边，panel区域完成后需要滑动到右边，有动画
6. panel 在100块的情况下变大，并且只展示一半
7. 左右边切换只能在一边完成的时候切换
8. 100完成的时候中心有一个例子动画，并且panel大小变为正常大小
9. 数据存储在文件名上标识多少块，如果有进度，就加载之前有进度的块，如果没有，根据jigsaw_difficulty进入不同的块玩法
10. 100块下，每次移动会将进度全部存储，可能会有性能问题
11. 工具端需要支持64块和100块，画笔顺序，需要我这边定义文件名
12. 埋点

#### 资源类

![image-20210106115213712](%E6%8B%BC%E5%9B%BE%E9%9A%BE%E5%BA%A6%E8%AE%BE%E8%AE%A1%E6%96%87%E6%A1%A3.assets/image-20210106115213712.png)



#### 画笔类

![image-20210106115520297](%E6%8B%BC%E5%9B%BE%E9%9A%BE%E5%BA%A6%E8%AE%BE%E8%AE%A1%E6%96%87%E6%A1%A3.assets/image-20210106115520297.png)

#### 画笔栏和panel

![image-20210106115730965](%E6%8B%BC%E5%9B%BE%E9%9A%BE%E5%BA%A6%E8%AE%BE%E8%AE%A1%E6%96%87%E6%A1%A3.assets/image-20210106115730965.png)

#### 支持不同玩法加载资源逻辑

<img src="%E6%8B%BC%E5%9B%BE%E9%9A%BE%E5%BA%A6%E8%AE%BE%E8%AE%A1%E6%96%87%E6%A1%A3.assets/image-20210106140953994.png" alt="image-20210106140953994" style="zoom:50%;" />

#### 100块下特殊流程

<img src="%E6%8B%BC%E5%9B%BE%E9%9A%BE%E5%BA%A6%E8%AE%BE%E8%AE%A1%E6%96%87%E6%A1%A3.assets/image-20210106145633005.png" alt="image-20210106145633005" style="zoom:50%;" />

* 初始化100个JigsawItemMeta
* panel 初始化后，调用JigsawItemMgr设置所有画笔的AimLocalPos（目标位置）
* 删除AimPos，全部使用AimLocalPos

### 测试用例

1. jigsaw_difficulty 修改后，已经玩过的图块数应该不变
2. 点击重玩后也算新图，受jigsaw_difficulty控制
3. 重点测试100块下性能影响
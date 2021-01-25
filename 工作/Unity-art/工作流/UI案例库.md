### 字体以及多语言

#### 多语言

##### 组件 ：LocalizationText 

* LocalizationText替换Text组件，适合刚写UI时候

  <img src="UI%E6%A1%88%E4%BE%8B%E5%BA%93.assets/Localization 使用.png" alt="image-20210125164244455" style="zoom:50%;" />

* TextLanguage组件修改Text组件的多语言，适合给之前UI添加组件

##### 直接获取多语言

```c#
MFLanguage.singleton.GetTextWithId(Text TextId, String defaultString)
```



#### 字体动画使用缩放

<img src="UI%E6%A1%88%E4%BE%8B%E5%BA%93.assets/image-20210125171754508.png" alt="image-20210125171754508" style="zoom:50%;" />

​	首页tag选中情况下字体会变大，如果使用的用一个字体，使用缩放可以减少多种不同大小字体加入的draw call



### 滑动列表案例

* RecycleView 使用案例

  * 目前主页面遇到大部分滑动列表都使用RecycleView，比如GalleryPage， TodayPage，MyArt等

    <img src="UI%E6%A1%88%E4%BE%8B%E5%BA%93.assets/image-20210125175915751.png" alt="image-20210125175915751" style="zoom:70%;" />

    Recycle View 会自动复用之前类型的节点，节省了自己写复用逻辑。

* 什么情况下不合适RecycleView

  * 有限个节点的情况下，使用系统自带的ScrollVIew就可以
  * 每个节点的交互和动画复杂，需要牵扯到其他滑动列表中的节点，可以自己写复用机制。

### 图片使用案例

* 网图打本地

### 资源引用

* 在Prefab的Inspector中拖拽Resource中的资源，在Prefab加载的时候，资源也会被加载到
* 错误例子1 ：用户不需要图片资源结果被加载到了
  * <img src="UI%E6%A1%88%E4%BE%8B%E5%BA%93.assets/资源多引用1.png" alt="image-20210125194552198" style="zoom:60%;" />
  * <img src="UI%E6%A1%88%E4%BE%8B%E5%BA%93.assets/资源多引用2.png" alt="image-20210125201622692" style="zoom:60%;" />
  * 图中 LoadingImage 和 ChrismasLoadingImage下都拖拽了一系列资源图，但用户只会显示一个节点
  * 这样用于不论用不用资源，普通资源和Chrismas资源都被加载了
* 错误例子2：用户生命周期只会用一次的资源，却拖累了整个App加载
  * <img src="UI%E6%A1%88%E4%BE%8B%E5%BA%93.assets/给经常使用的图集中添加了不用的图.png" alt="image-20210125195026704" style="zoom:50%;" />
  * 这是一张common的资源，结果一个在测试版本的拼图资源放入common，结果拖累了整体App加载
  * 注意，这个是演示。

### 滑动列表优化

#### 列表滑动大量节点Active发生改变，导致卡顿

<img src="UI%E6%A1%88%E4%BE%8B%E5%BA%93.assets/滑动列表角标.png" alt="image-20210125202849134" style="zoom:50%;" />

![image-20210125202712624](UI%E6%A1%88%E4%BE%8B%E5%BA%93.assets/滑动列表-复用大量节点Active.png)

* PictureItem 复用格子的时候，角标不同使用的是Activity不同节点，导致卡顿
* 通过设置文字和图片透明度避免卡顿

#### 滑动列表节点层次导致不能合批

![image-20210125203214003](UI%E6%A1%88%E4%BE%8B%E5%BA%93.assets/滑动列表合批.png)

![image-20210125203631217](UI%E6%A1%88%E4%BE%8B%E5%BA%93.assets/滑动列表合批优化后.png)

将Text 单独放到一起，知道一下就可以，可能是Unity算法导致。

#### 滑动列表修改位置导致不能合批

![image-20210125205234751](UI%E6%A1%88%E4%BE%8B%E5%BA%93.assets/错误使用position.png)

使用setPosition后，由于3D转2D导致Z值不同，导致Image图不能合批

#### Mask 导致卡顿

![image-20210125205546113](UI%E6%A1%88%E4%BE%8B%E5%BA%93.assets/使用mask.png)

默认创建的ScrolViewl会自带一个Mask，请删除

### 布局规范

#### 冗余节点案例

#### 

### Component相关

1. 不需要接收点击事件的图/文字，去除Raycast Target
2. setting下有很多选择项，需要依次排列。可以使用Content Size Fitter + Vertical Layout Group
3. 多语言使用LocalizationText，文字加阴影不属于LocalizationText，新写一个脚本，使用组合的方式扩展。
4. 网图使用CacheImage，不满足需求情况下提出新需求而不是使用RawImage，这样会导致不在图片内存管理框架中


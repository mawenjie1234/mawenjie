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

---

### 图片使用案例

#### 网图 CacheImage

* 目前Art中网图全部使用CacheImage，使用CacheImage有利于维护网图内存

* CacheImage 使用

  * 将需要使用的地方直接加载Resource/Prefab/uGUI/ImageCell/CacheImage 的prefab
  * 加载图CacheImage.SetNewInfo(string url, string des) 提供远端URL和本地存储路径
  * 本地存储路径最好使用缓存目录，请使用MFUtils.GetCacheFilePath 拼接

* CacheImage 自定义loading动画

  * ```
    CacheImageLoading loadingUI = null, CacheImageLoadingArgs loadingArgs = null
    ```

  * CacheImageLoading 定义了显示和隐藏loading，需要自己实现

  * CacheImageLoadingArgs 是提供的一些show 的参数，比如不同的加载图、位置等信息

* CacheImage 自定义展示样式

  * ```
    CacheImageDisplay display = null, CacheImageDisplayArgs cacheImageDisplayArgs = null
    ```

  * CacheImageDisplay 定义了展示一张图的接口，需要自己实现具体细节

  * CacheImageDisplayArgs 包含了显示图的参数，比如不同的外边框

* 获取CacheImage加载状态

  * ```
    public enum LoadingStatus
            {
                NotStart,
                Loading, // 下载和解析过程
                FinishWithSuccess,
                FinishWithFail
            }
    CacheImage.GetLoadingStatus()
    ```

  * 通过callback形式 成功和失败回调

    ```
    TextureSucc 成功回调
    TextureFail 失败回调
    SetNewInfo（url,des,Action TextureSucc = null, Action TextureFail = null）
    ```

#### 网图打包内

* 网图打包内，需要将图片资源放入 StreamingAssets/content 下
* 网图打包内需PM找DEV更新，目前找 成才更新
* 网图打包内会增大包体积，请找 feng.lu商议放多少，放那些

#### 本地 icon

* 直接使用Image组件，打好图集即可

#### 本地大图

* 如果不打图集情况下，直接将图放入 Resource/Image/Other 下

---

### 资源引用

#### 加载方式

##### 使用拖拽加载

* 将Resource中的资源拖拽到 Prefab的Inspector中，在Prefab加载的时候，资源也会被加载到

##### 使用代码加载

使用Resource.Load 加载资源

##### 优劣

* 通常使用拖拽一张图比较方便，更换资源时候不用修改代码，不会出错
* 资源多选一：使用代码加载更好，可以只加载一部分，避免加载不必要资源

#### 示例

* 错误例子1 ：用户不需要图片资源结果被加载到了
  * <img src="UI%E6%A1%88%E4%BE%8B%E5%BA%93.assets/资源多引用1.png" alt="image-20210125194552198" style="zoom:60%;" />
  * <img src="UI%E6%A1%88%E4%BE%8B%E5%BA%93.assets/资源多引用2.png" alt="image-20210125201622692" style="zoom:60%;" />
  * 图中 LoadingImage 和 ChrismasLoadingImage下都拖拽了一系列资源图，但用户只会显示一个节点
  * 这样用于不论用不用资源，普通资源和Chrismas资源都被加载了
* 错误例子2：用户生命周期只会用一次的资源，却拖累了整个App加载
  * <img src="UI%E6%A1%88%E4%BE%8B%E5%BA%93.assets/给经常使用的图集中添加了不用的图.png" alt="image-20210125195026704" style="zoom:50%;" />
  * 这是一张common的资源，结果一个在测试版本的拼图资源放入common，结果拖累了整体App加载
  * 注意，这个是演示。

---

### 滑动列表案例

* RecycleView 使用案例

  * 目前主页面遇到大部分滑动列表都使用RecycleView，比如GalleryPage， TodayPage，MyArt等

    <img src="UI%E6%A1%88%E4%BE%8B%E5%BA%93.assets/image-20210125175915751.png" alt="image-20210125175915751" style="zoom:70%;" />

    Recycle View 会自动复用之前类型的节点，节省了自己写复用逻辑。

* 什么情况下不合适RecycleView

  * 只有几个节点的情况下，使用系统自带的ScrollVIew就可以。比如首页的tag
  * 每个节点的交互和动画复杂，需要牵扯到其他滑动列表中的节点

---

### 

### 滑动列表优化

#### 列表滑动大量节点Active发生改变，导致卡顿

<img src="UI%E6%A1%88%E4%BE%8B%E5%BA%93.assets/滑动列表角标.png" alt="image-20210125202849134" style="zoom:50%;" />

![image-20210125202712624](UI%E6%A1%88%E4%BE%8B%E5%BA%93.assets/滑动列表-复用大量节点Active.png)

* PictureItem 复用格子的时候，角标不同使用的是Active不同节点，导致卡顿
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

---

### 布局规范

#### tips

* 需要响应点击事件的节点使用 Empty4Raycast, image 和text下的Raycast Target 不勾选

  ![image-20210125210147549](UI%E6%A1%88%E4%BE%8B%E5%BA%93.assets/Recycast Target.png)

#### 冗余节点案例

#### Settings 上的开关

效果图

<img src="UI%E6%A1%88%E4%BE%8B%E5%BA%93.assets/image-20210127142644105.png" alt="image-20210127142644105" style="zoom:50%;" />

节点图

####![image-20210127134707730](UI%E6%A1%88%E4%BE%8B%E5%BA%93.assets/冗余节点案例.png) 

<img src="UI%E6%A1%88%E4%BE%8B%E5%BA%93.assets/Settings Recycast Target.png" alt="image-20210127142721436" style="zoom:50%;" />

* 效果图上根本没有文字，因此两个Text节点是多余的
* 加了一个ToggleButtom专门处理点击事件，可以删除。直接在父节点Toggle上添加
* 小手没有点击事件，应该去掉Raycast Target

---

### 使用Layout简化代码复杂性

#### 使用Layout 解决Setting页面复杂UI

Setting页面需求

<center class="half"><img src="UI%E6%A1%88%E4%BE%8B%E5%BA%93.assets/Settings UI.png" alt="image-20210127143722355" style="zoom:100%;" />    <img src="UI%E6%A1%88%E4%BE%8B%E5%BA%93.assets/Settings UI2.png" alt="image-20210127143813206" style="zoom:100%;" /></center>

节点

![image-20210127145510825](UI%E6%A1%88%E4%BE%8B%E5%BA%93.assets/Seting 节点.png)

#### 什么情况下限制使用Layout

* 页面性能要求高：滑动列表下尽量不使用Layout，这样可能会带来滑动卡顿。或者必须实测才能使用


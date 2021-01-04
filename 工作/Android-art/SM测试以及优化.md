# 如何分析卡顿点的堆栈范例

直接运行app， 将会在sdcard/pixel 下生成两个文件

* 精简版 日期Simplify_SM.txt
* 全部日志  日期SM.text
 
# 案例分析

在精简版中针对如下一段卡顿进行分析
```
-android.os.Handler.handleCallback(Handler.java:742)    60
 |-android.view.ViewRootImpl.performTraversals(ViewRootImpl.java:1489)    54
 | |-android.support.v4.app.Fragment.performCreateView(Fragment.java:2439)    29
 | | |-com.pixel.game.colorfy.activities.categoryFragement.CategoriesFragment.onCreateView(CategoriesFragment.java:54)    20
 | | | |-android.view.LayoutInflater.inflate(LayoutInflater.java:427)    3
 | | | |-com.pixel.game.colorfy.activities.categoryFragement.CategoriesFragment.initRecycleView(CategoriesFragment.java:92)    17
 | | | | |-com.pixel.game.colorfy.activities.categoryFragement.CategoriesFragment.initCarouselView(CategoriesFragment.java:61)    3
 | | | | | |-com.pixel.game.colorfy.activities.categoryFragement.HomeCarouselView.<init>(HomeCarouselView.java:37)    2
 | | | | | | |-com.pixel.game.colorfy.activities.categoryFragement.HomeCarouselView.initView(HomeCarouselView.java:41)    2
 | | | | |-com.pixel.game.colorfy.activities.categoryFragement.CategoriesFragment.initLinkFooterLayout(CategoriesFragment.java:65)    12
 | | | | | |-com.pixel.game.colorfy.Layout.UnderlineTextView.<init>(UnderlineTextView.java:26)    11
 | | |-com.pixel.game.colorfy.activities.MyArtsFragment.onCreateView(MyArtsFragment.java:60)    9
 | |-android.support.v7.widget.LinearLayoutManager.layoutChunk(LinearLayoutManager.java:1583)    22
 | | |-android.view.View.measure(View.java:18830)    20
 | | | |-com.pixel.game.colorfy.Layout.carouselView.CarouselViewLayout$PageViewAdapter.instantiateItem(CarouselViewLayout.java:222)    13
 | | | | |-com.pixel.game.colorfy.activities.categoryFragement.HomeCarouselView$1.setViewForPosition(HomeCarouselView.java:65)    13
 | | | | | |-com.pixel.game.colorfy.activities.carousels.FreePictures.initRootView(FreePictures.java:123)    12
 | | | | | | |-com.pixel.game.colorfy.activities.carousels.FreePictures.initDisplayPictureMeta(FreePictures.java:116)    10
 | | | | | | | |-com.pixel.game.colorfy.activities.carousels.FreePictures.updateDisplay(FreePictures.java:322)    10
 | | | | | | | | |-com.pixel.game.colorfy.framework.utils.ImageLoader.loadImageToImageView(ImageLoader.java:38)    10
 | | | | | | | | | |-com.pixel.game.colorfy.framework.utils.GlideApp.with(GlideApp.java)    8
 | | | | | | | | | | |-com.bumptech.glide.Glide.with(Glide.java:698)    7
 | | | | | | | | | | | |-com.bumptech.glide.Glide.getRetriever(Glide.java:671)    5
 | | | | | | | | | | | |-com.bumptech.glide.manager.RequestManagerRetriever.supportFragmentGet(RequestManagerRetriever.java:435)    2
 | | | |-android.support.v7.widget.RecyclerView$Recycler.tryGetViewHolderForPositionByDeadline(RecyclerView.java:5975)    5
 | | | | |-com.pixel.game.colorfy.activities.categoryFragement.PictureAdapter.onCreateViewHolder(PictureAdapter.java:21)    3
 | | | | | |-com.pixel.game.colorfy.activities.categoryFragement.PictureAdapter.onCreateViewHolder(PictureAdapter.java:42)    3
 | | | | |-com.pixel.game.colorfy.activities.categoryFragement.PictureAdapter.onBindViewHolder(PictureAdapter.java:21)    2
 | | | | | |-com.pixel.game.colorfy.activities.categoryFragement.PictureAdapter.onBindViewHolder(PictureAdapter.java:51)    2
 | | | | | | |-com.pixel.game.colorfy.activities.itembase.ItemBase.updatePictureMeta(ItemBase.java:189)    2
 | | | | | | | |-com.pixel.game.colorfy.activities.itembase.ItemBase.updateView(ItemBase.java:208)    2
 | | | | | | | | |-com.pixel.game.colorfy.activities.itembase.ItemBase.updateItemPicture(ItemBase.java:292)    2
 | | | | | | | | | |-com.pixel.game.colorfy.activities.itembase.ItemBase.loadOriginPicture(ItemBase.java:306)    2
 | | |-android.support.v7.widget.RecyclerView$Recycler.tryGetViewHolderForPositionByDeadline(RecyclerView.java:6019)    2
 |-net.appcloudbox.ads.adadapter.DfpInterstitialAdapter.DfpInterstitialAdapter$2.run(Unknown Source)    5
```


## 1.找到有多少个卡顿点

* 检查UnderlineTextView
* MyArtsFragment.onCreateView
* LinearLayoutManager.java 
  * 有两次 调用 Recycler.tryGetViewHolderForPositionByDeadline，是否可以算成一次，并且每一次都太长了，第二次都6帧
  *  glideApp.with 这个操作是不是可以移动到数据初始化
  
  
## 2.在详细日志中找到当前卡顿点堆栈的详细信息


```
-android.os.Handler.handleCallback(Handler.java:742)    60
 |-android.view.ViewRootImpl.performTraversals(ViewRootImpl.java:1489)    54
 | |-android.support.constraint.ConstraintLayout.onMeasure(ConstraintLayout.java:1572)    30
 | | |-android.support.v4.app.Fragment.performCreateView(Fragment.java:2439)    29
 | | | |-com.pixel.game.colorfy.activities.categoryFragement.CategoriesFragment.onCreateView(CategoriesFragment.java:54)    20
 | | | | |-android.support.v7.widget.RecyclerView.<init>(RecyclerView.java:497)    1
 | | | | |-com.pixel.game.colorfy.activities.categoryFragement.CategoriesFragment.initRecycleView(CategoriesFragment.java:92)    17
 | | | | | |-com.pixel.game.colorfy.activities.categoryFragement.CategoriesFragment.initCarouselView(CategoriesFragment.java:61)    3
 | | | | | | |-com.pixel.game.colorfy.activities.categoryFragement.HomeCarouselView.<init>(HomeCarouselView.java:37)    2
 | | | | | | | |-com.pixel.game.colorfy.activities.categoryFragement.HomeCarouselView.initView(HomeCarouselView.java:41)    2
 | | | | | | | | |-java.lang.reflect.Constructor.newInstance(Native Method)    1
 | | | | | | | | |-com.pixel.game.colorfy.Layout.carouselView.CarouselViewLayout.initIndicator(CarouselViewLayout.java:71)    1
 | | | | | | | | | |-com.pixel.game.colorfy.Layout.carouselView.CarouseViewIndicator.<init>(CarouseViewIndicator.java:21)    1
 | | | | | | | | | | |-java.util.AbstractList.<init>(AbstractList.java:377)    1
 | | | | | |-com.pixel.game.colorfy.activities.categoryFragement.CategoriesFragment.initLinkFooterLayout(CategoriesFragment.java:65)    12
 | | | | | | |-com.pixel.game.colorfy.Layout.UnderlineTextView.<init>(UnderlineTextView.java:26)    11
 | | | | | | | |-android.support.v4.graphics.TypefaceCompatUtil.copyToFile(TypefaceCompatUtil.java:144)    11
 | | | | | | | | |-libcore.io.BlockGuardOs.write(BlockGuardOs.java:313)    5
 | | | | | | | | | |-libcore.io.Posix.writeBytes(Native Method)    4
 | | | | | | | | | |-java.lang.ThreadLocal.get(ThreadLocal.java:65)    1
 | | | | | | | | |-android.content.res.AssetManager.readAsset(Native Method)    6
 | | | | | |-android.support.v7.widget.ViewBoundsCheck.<init>(ViewBoundsCheck.java:133)    1
 | | | |-com.pixel.game.colorfy.activities.MyArtsFragment.onCreateView(MyArtsFragment.java:60)    9
 | | | | |-android.view.LayoutInflater.rInflate(LayoutInflater.java:839)    8
 | | | | | |-android.content.res.AssetManager.applyStyle(Native Method)    1
 | | | | | |-android.support.v4.graphics.TypefaceCompatUtil.copyToFile(TypefaceCompatUtil.java:144)    7
 | | | | | | |-libcore.io.IoBridge.write(IoBridge.java:487)    3
 | | | | | | | |-java.util.Arrays.checkOffsetAndCount(Arrays.java:1722)    1
 | | | | | | | |-libcore.io.Posix.writeBytes(Native Method)    2
 | | | | | | |-android.content.res.AssetManager.readAsset(Native Method)    3
 | | |-android.support.constraint.solver.widgets.Chain.applyChainConstraints(Chain.java:46)    1
 | |-android.view.Surface.nativeAllocateBuffers(Native Method)    1
 | |-android.support.v7.widget.LinearLayoutManager.layoutChunk(LinearLayoutManager.java:1583)    22
 | | |-android.view.View.measure(View.java:18830)    20
 | | | |-android.support.v4.view.ViewPager.onMeasure(ViewPager.java:1622)    14
 | | | | |-com.pixel.game.colorfy.Layout.carouselView.CarouselViewLayout$PageViewAdapter.instantiateItem(CarouselViewLayout.java:222)    13
 | | | | | |-com.pixel.game.colorfy.activities.categoryFragement.HomeCarouselView$1.setViewForPosition(HomeCarouselView.java:65)    13
 | | | | | | |-com.pixel.game.colorfy.activities.carousels.FreePictures.<init>(FreePictures.java:72)    1
 | | | | | | |-com.pixel.game.colorfy.activities.carousels.FreePictures.initRootView(FreePictures.java:123)    12
 | | | | | | | |-java.lang.reflect.Constructor.newInstance(Native Method)    1
 | | | | | | | |-com.pixel.game.colorfy.activities.carousels.FreePictures.initAndPlayPictureItemAnimation(FreePictures.java:163)    1
 | | | | | | | |-com.pixel.game.colorfy.activities.carousels.FreePictures.initDisplayPictureMeta(FreePictures.java:116)    10
 | | | | | | | | |-com.pixel.game.colorfy.activities.carousels.FreePictures.updateDisplay(FreePictures.java:322)    10
 | | | | | | | | | |-com.pixel.game.colorfy.framework.utils.ImageLoader.loadImageToImageView(ImageLoader.java:38)    10
 | | | | | | | | | | |-com.pixel.game.colorfy.framework.utils.GlideApp.with(GlideApp.java)    8
 | | | | | | | | | | | |-com.bumptech.glide.Glide.with(Glide.java:698)    7
 | | | | | | | | | | | | |-com.bumptech.glide.GlideBuilder.build(GlideBuilder.java:388)    4
 | | | | | | | | | | | | | |-com.bumptech.glide.load.engine.executor.GlideExecutor.newSourceExecutor(GlideExecutor.java:187)    1
 | | | | | | | | | | | | | |-com.bumptech.glide.Glide.<init>(Glide.java:328)    2
 | | | | | | | | | | | | | | |-com.bumptech.glide.load.resource.bitmap.Downsampler.<clinit>(Downsampler.java:57)    1
 | | | | | | | | | | | | | | |-com.bumptech.glide.Registry.getImageHeaderParsers(Registry.java:595)    1
 | | | | | | | | | | | | |-com.bumptech.glide.manager.RequestManagerRetriever.supportFragmentGet(RequestManagerRetriever.java:435)    2
 | | | | | | | | | | | | | |-com.bumptech.glide.manager.RequestManagerRetriever.getSupportRequestManagerFragment(RequestManagerRetriever.java:415)    1
 | | | | | | | | | | | | | |-com.pixel.game.colorfy.framework.utils.GlideRequests.<init>(GlideRequests.java:38)    1
 | | | | | | | | | | | | | | |-com.pixel.game.colorfy.framework.utils.GlideRequests.setRequestOptions(GlideRequests.java:170)    1
 | | | | | | | | | | |-com.bumptech.glide.request.SingleRequest.obtain(SingleRequest.java:134)    1
 | | | | |-android.graphics.Paint.native_getRunAdvance(Native Method)    1
 | | | |-android.view.View.measure(View.java:18830)    6
 | | | | |-android.support.v7.widget.RecyclerView$Recycler.tryGetViewHolderForPositionByDeadline(RecyclerView.java:5975)    5
 | | | | | |-com.pixel.game.colorfy.activities.categoryFragement.PictureAdapter.onCreateViewHolder(PictureAdapter.java:21)    3
 | | | | | | |-com.pixel.game.colorfy.activities.categoryFragement.PictureAdapter.onCreateViewHolder(PictureAdapter.java:42)    3
 | | | | | | | |-android.view.LayoutInflater.inflate(LayoutInflater.java:427)    2
 | | | | | | | | |-java.lang.reflect.Constructor.newInstance(Native Method)    1
 | | | | | | | | |-android.support.v7.widget.VectorEnabledTintResources.isCompatVectorFromResourcesEnabled(VectorEnabledTintResources.java:93)    1
 | | | | | |-com.pixel.game.colorfy.activities.categoryFragement.PictureAdapter.onBindViewHolder(PictureAdapter.java:21)    2
 | | | | | | |-com.pixel.game.colorfy.activities.categoryFragement.PictureAdapter.onBindViewHolder(PictureAdapter.java:51)    2
 | | | | | | | |-com.pixel.game.colorfy.activities.itembase.ItemBase.updatePictureMeta(ItemBase.java:189)    2
 | | | | | | | | |-com.pixel.game.colorfy.activities.itembase.ItemBase.updateView(ItemBase.java:208)    2
 | | | | | | | | | |-com.pixel.game.colorfy.activities.itembase.ItemBase.updateItemPicture(ItemBase.java:292)    2
 | | | | | | | | | | |-com.pixel.game.colorfy.activities.itembase.ItemBase.loadOriginPicture(ItemBase.java:306)    2
 | | | | | | | | | | | |-com.pixel.game.colorfy.framework.utils.ImageLoader.loadGifToImageView(ImageLoader.java:69)    1
 | | | | | | | | | | | |-com.pixel.game.colorfy.model.picturedata.data.PictureMetaImpl.getOriginalImagePath(PictureMetaImpl.java:259)    1
 | | | | | | | | | | | | |-com.pixel.game.colorfy.model.picturedata.data.PictureFilePath.getOriginalImagePath(PictureFilePath.java:51)    1
 | | | | | | | | | | | | | |-com.pixel.game.colorfy.model.picturedata.data.PictureFilePath.getPicturePath(PictureFilePath.java:27)    1
 | | | | | | | | | | | | | | |-com.pixel.game.colorfy.model.picturedata.data.PictureFilePath.getResourcePath(PictureFilePath.java:15)    1
 | | | | | | | | | | | | | | | |-libcore.io.Posix.access(Native Method)    1
 | | | | |-android.graphics.Paint.native_getRunAdvance(Native Method)    1
 | | |-android.support.v7.widget.RecyclerView$Recycler.tryGetViewHolderForPositionByDeadline(RecyclerView.java:6019)    2
 | | | |-com.pixel.game.colorfy.activities.categoryFragement.CategoryAdapter.onBindViewHolder(CategoryAdapter.java:16)    1
 | | | | |-com.pixel.game.colorfy.activities.categoryFragement.CategoryAdapter.onBindViewHolder(CategoryAdapter.java:51)    1
 | | | | | |-com.pixel.game.colorfy.activities.categoryFragement.CategoryAdapter.convert(CategoryAdapter.java:43)    1
 | | | | | | |-com.pixel.game.colorfy.activities.categoryFragement.CategoryItemViewHolder.update(CategoryItemViewHolder.java:106)    1
 | | | | | | | |-com.pixel.game.colorfy.activities.categoryFragement.CategoryItemViewHolder.setAdapter(CategoryItemViewHolder.java:118)    1
 | | | |-com.pixel.game.colorfy.activities.categoryFragement.CategoryAdapter.onCreateViewHolder(CategoryAdapter.java:16)    1
 | | | | |-com.pixel.game.colorfy.activities.categoryFragement.CategoryAdapter.onCreateViewHolder(CategoryAdapter.java:34)    1
 | | | | | |-java.lang.reflect.Constructor.newInstance(Native Method)    1
 | |-android.os.Parcel.nativeWriteInterfaceToken(Native Method)    1
 |-java.lang.StringFactory.newStringFromChars(Native Method)    1
 |-com.google.android.gms.internal.ads.zzma.zza(Unknown Source)    5
 | |-com.google.android.gms.internal.ads.zzjr.zza(Unknown Source)    3
 | | |-android.os.BinderProxy.transactNative(Native Method)    1
 | | |-com.google.android.gms.ads.AdManagerCreatorImpl.newAdManagerByType(:com.google.android.gms@14799021@14.7.99 (040408-223214910):7)    2
 | | | |-dalvik.system.DexFile.defineClassNative(Native Method)    1
 | | | |-com.google.android.gms.ads.ChimeraAdManagerCreatorImpl.newAdManagerByType(:com.google.android.gms.dynamite_adsdynamite@14799051@14.7.99 (040408-223214910):34)    1
 | |-com.google.android.gms.ads.internal.a.b(:com.google.android.gms.dynamite_adsdynamite@14799051@14.7.99 (040408-223214910):85)    2
 | | |-android.os.BinderProxy.transactNative(Native Method)    1
 | | |-java.lang.Object.wait(Native Method)    1
==================Sat Feb 02 13:49:43 GMT+08:00 2019==================
```

如上就是全部日志。

## 3逐条分析

### 检查UnderlineTextView

```
 | | | | | |-com.pixel.game.colorfy.Layout.UnderlineTextView.<init>(UnderlineTextView.java:26)    9
 | | | | | | |-android.support.v4.graphics.TypefaceCompatUtil.copyToFile(TypefaceCompatUtil.java:144)    9
 | | | | | | | |-libcore.io.IoBridge.write(IoBridge.java:493)    7
 | | | | | | | | |-libcore.io.Posix.writeBytes(Native Method)    5
 | | | | | | | | |-java.util.Arrays.checkOffsetAndCount(Arrays.java:1722)    2
 | | | | | | | |-android.content.res.AssetManager.readAsset(Native Method)    2
```

从日志中看到，underlineTextView 中有一个copyToFile,加一个下划线为啥需要这个？

分析UnderlineTextView的init

```
    private void init() {
        mLinePaint = new Paint();
        mLinePaint.setStrokeWidth(Utils.dp2px(2f));
        mLinePaint.setColor(getCurrentTextColor());
    }

```

发现这些都不需要load 字体，判断有可能是使用下划线的view上使用了字体，把主界面下隐私政策的字体改为默认再进行测试

[x] 测试主界面隐私政策上字体

就是字体文字，字体文件太大了，5.2M


### MyArtsFragment.onCreateView
```
 | | | |-com.pixel.game.colorfy.activities.MyArtsFragment.onCreateView(MyArtsFragment.java:60)    9
 | | | | |-android.view.LayoutInflater.rInflate(LayoutInflater.java:839)    8
 | | | | | |-android.content.res.AssetManager.applyStyle(Native Method)    1
 | | | | | |-android.support.v4.graphics.TypefaceCompatUtil.copyToFile(TypefaceCompatUtil.java:144)    7
 | | | | | | |-libcore.io.IoBridge.write(IoBridge.java:487)    3
 | | | | | | | |-java.util.Arrays.checkOffsetAndCount(Arrays.java:1722)    1
 | | | | | | | |-libcore.io.Posix.writeBytes(Native Method)    2
 | | | | | | |-android.content.res.AssetManager.readAsset(Native Method)    3
```

又是字体，因此需要查看是两种字体还是一种字体。字体还有没有优化的可能。列出todo
[x] 看看是不是使用了两种不同的字体，还是一种字体

结果 ：
是一种字体,都使用了font/AvenirNext.ttc，但是style不一样，上面一个是normal 现在这个是bold。 字体文件有5.2M大小。应该使用更小的字体。



### LinearLayoutManager.java 
#### 有两次 调用 Recycler.tryGetViewHolderForPositionByDeadline，是否可以算成一次，并且每一次都太长了，第二次都6帧

从日志中分析发现进行了两次测量，分别测量了主界面上面的banner 和 下面的recycle view，因此两个是不同的。 不能合并，需要对每一个进行详细的分析
* 分析上面banner 中卡顿的原因是 flideApp的第一次init耗时。测试把glide耗时操作放到pictureData init 的那段时间。
* 分析 底部测量

```
 | | | | |-android.support.v7.widget.RecyclerView$Recycler.tryGetViewHolderForPositionByDeadline(RecyclerView.java:5975)    5
 | | | | | |-com.pixel.game.colorfy.activities.categoryFragement.PictureAdapter.onCreateViewHolder(PictureAdapter.java:21)    3
 | | | | | | |-com.pixel.game.colorfy.activities.categoryFragement.PictureAdapter.onCreateViewHolder(PictureAdapter.java:42)    3
 | | | | | | | |-android.view.LayoutInflater.inflate(LayoutInflater.java:427)    2
 | | | | | | | | |-java.lang.reflect.Constructor.newInstance(Native Method)    1
 | | | | | | | | |-android.support.v7.widget.VectorEnabledTintResources.isCompatVectorFromResourcesEnabled(VectorEnabledTintResources.java:93)    1
 | | | | | |-com.pixel.game.colorfy.activities.categoryFragement.PictureAdapter.onBindViewHolder(PictureAdapter.java:21)    2
 | | | | | | |-com.pixel.game.colorfy.activities.categoryFragement.PictureAdapter.onBindViewHolder(PictureAdapter.java:51)    2
 | | | | | | | |-com.pixel.game.colorfy.activities.itembase.ItemBase.updatePictureMeta(ItemBase.java:189)    2
 | | | | | | | | |-com.pixel.game.colorfy.activities.itembase.ItemBase.updateView(ItemBase.java:208)    2
 | | | | | | | | | |-com.pixel.game.colorfy.activities.itembase.ItemBase.updateItemPicture(ItemBase.java:292)    2
 | | | | | | | | | | |-com.pixel.game.colorfy.activities.itembase.ItemBase.loadOriginPicture(ItemBase.java:306)    2
 | | | | | | | | | | | |-com.pixel.game.colorfy.framework.utils.ImageLoader.loadGifToImageView(ImageLoader.java:69)    1
 | | | | | | | | | | | |-com.pixel.game.colorfy.model.picturedata.data.PictureMetaImpl.getOriginalImagePath(PictureMetaImpl.java:259)    1
 | | | | | | | | | | | | |-com.pixel.game.colorfy.model.picturedata.data.PictureFilePath.getOriginalImagePath(PictureFilePath.java:51)    1
 | | | | | | | | | | | | | |-com.pixel.game.colorfy.model.picturedata.data.PictureFilePath.getPicturePath(PictureFilePath.java:27)    1
 | | | | | | | | | | | | | | |-com.pixel.game.colorfy.model.picturedata.data.PictureFilePath.getResourcePath(PictureFilePath.java:15)    1
 | | | | | | | | | | | | | | | |-libcore.io.Posix.access(Native Method)    1
```

这一段发现是PictureAdapter.onCreateViewHolder 和 PictureAdapter.onBindViewHolder 耗时。但是已经无法具体分析出到底是那个函数更多，需要使用其他工具进行分析。


####  glideApp.with 这个操作是不是可以移动到数据初始化。

[x] 移动glide 到picture data在子线程操作的时候进行init，看是否有用。


```
    public static void initGlide(Context context){
        RequestOptions requestOptions = new RequestOptions().diskCacheStrategy(DiskCacheStrategy.AUTOMATIC);
        GlideApp.with(context).load("").apply(requestOptions);
    }
```

这个函数在数据初始化的时候调用将会优化glide的with的时间
```
 PictureManager.getInstance().startInit();
 ImageLoader.initGlide(HSApplication.getContext());
```

## 4总计
* CategoriesFragment.initCarouselView 3
* CategoriesFragment.initLinkFooterLayout 12
* MyArtsFragment.onCreateView ->  9 
  * 字体 8
* HomeCarouselView$1.setViewForPosition 13
  * freePictures.init() 1
  * ImageLoader.loadImageToImageView 10
* Recycler.tryGetViewHolderForPositionByDeadline 6
* Recycler.tryGetViewHolderForPositionByDeadline 2
* com.google.android.gms.internal.ads.zzma.zza 5
* other

优化 ： 

*  MyArtsFragment.onCreateView 9 -> 1   8
*  initLinkFooterLayout 12 -> 2   10
* ImageLoader.loadImageToImageView 10 -> 2  8

总计优化 26帧 43.3% 

## 5 小卡顿的优化怎么办

优化后的堆栈

```
-android.view.ViewRootImpl.performTraversals(ViewRootImpl.java:1489)    38
 |-android.support.v4.view.ViewPager.populate(ViewPager.java:1158)    22
 | |-com.pixel.game.colorfy.activities.main.MainViewPagerAdapter.getItem(MainViewPagerAdapter.java:45)    2
 | |-android.support.v4.app.Fragment.performCreateView(Fragment.java:2439)    19
 | | |-com.pixel.game.colorfy.activities.categoryFragement.CategoriesFragment.onCreateView(CategoriesFragment.java:54)    17
 | | | |-android.view.LayoutInflater.inflate(LayoutInflater.java:427)    7
 | | | |-com.pixel.game.colorfy.activities.categoryFragement.CategoriesFragment.initRecycleView(CategoriesFragment.java:92)    10
 | | | | |-com.pixel.game.colorfy.activities.categoryFragement.CategoriesFragment.initCarouselView(CategoriesFragment.java:61)    2
 | | | | | |-com.pixel.game.colorfy.activities.categoryFragement.HomeCarouselView.<init>(HomeCarouselView.java:37)    2
 | | | | | | |-com.pixel.game.colorfy.activities.categoryFragement.HomeCarouselView.initView(HomeCarouselView.java:41)    2
 | | | | |-com.pixel.game.colorfy.activities.categoryFragement.CategoriesFragment.initLinkFooterLayout(CategoriesFragment.java:65)    4
 | | | | | |-com.pixel.game.colorfy.Layout.UnderlineTextView.<init>(UnderlineTextView.java:26)    2
 | | |-com.pixel.game.colorfy.activities.MyArtsFragment.onCreateView(MyArtsFragment.java:60)    2
 |-android.support.v7.widget.LinearLayoutManager.layoutChunk(LinearLayoutManager.java:1583)    13
 | |-android.view.View.measure(View.java:18830)    10
 | | |-com.pixel.game.colorfy.Layout.carouselView.CarouselViewLayout$PageViewAdapter.instantiateItem(CarouselViewLayout.java:222)    4
 | | | |-com.pixel.game.colorfy.activities.categoryFragement.HomeCarouselView$1.setViewForPosition(HomeCarouselView.java:73)    4
 | | | | |-com.pixel.game.colorfy.activities.carousels.FreePictures.initRootView(FreePictures.java:123)    4
 | | | | | |-android.view.LayoutInflater.inflate(LayoutInflater.java:374)    2
 | | | | | |-com.pixel.game.colorfy.activities.carousels.FreePictures.initDisplayPictureMeta(FreePictures.java:116)    2
 | | | | | | |-com.pixel.game.colorfy.activities.carousels.FreePictures.updateDisplay(FreePictures.java:322)    2
 | | | | | | | |-com.pixel.game.colorfy.framework.utils.ImageLoader.loadImageToImageView(ImageLoader.java:41)    2
 | | |-android.support.v7.widget.RecyclerView$Recycler.tryGetViewHolderForPositionByDeadline(RecyclerView.java:5975)    6
 | | | |-com.pixel.game.colorfy.activities.categoryFragement.PictureAdapter.onCreateViewHolder(PictureAdapter.java:21)    4
 | | | | |-com.pixel.game.colorfy.activities.categoryFragement.PictureAdapter.onCreateViewHolder(PictureAdapter.java:42)    4
 | | | | | |-android.view.LayoutInflater.createViewFromTag(LayoutInflater.java:768)    2
 | | | |-com.pixel.game.colorfy.activities.categoryFragement.PictureAdapter.onBindViewHolder(PictureAdapter.java:21)    2
 | | | | |-com.pixel.game.colorfy.activities.categoryFragement.PictureAdapter.onBindViewHolder(PictureAdapter.java:51)    2
 | | | | | |-com.pixel.game.colorfy.activities.itembase.ItemBase.updatePictureMeta(ItemBase.java:189)    2
 | | | | | | |-com.pixel.game.colorfy.activities.itembase.ItemBase.updateView(ItemBase.java:208)    2
 | | | | | | | |-com.pixel.game.colorfy.activities.itembase.ItemBase.updateItemPicture(ItemBase.java:287)    2
 | |-android.support.v7.widget.RecyclerView$Recycler.tryGetViewHolderForPositionByDeadline(RecyclerView.java:5975)    2
```


* 从精简版中可以看出 CategoriesFragment inflate 还消耗较多，可以修改布局
* FreePictures 应该是一个简单的布局，inflate 太多，需要修改布局
* CategoriesFragment.initLinkFooterLayout 还是4帧，需要使用其他工具查看
* PictureAdapter.onCreateViewHolder 耗时4帧太久了
* ItemBase.updateItemPicture 2帧

之后通过Systrace 在已经知道代码的范围内添加Trace.beginSection() 和 Tracer.endSection()来看详细哪些需要优化。








# Android结构与技术选型

标签（空格分隔）： Android 选型 库

---

## 基本理念
1. Kotlin可选，[**Rxjava主项目中禁用**][1] 
2. 空格空行，命名表意 
3. 包名采用 PBF（按功能分包 Package By Feature）[参考][2]
4. 最小化职责（方法，commit)

## 开发规范
- 使用Gradle插件约束
[《阿里Java开发规范》](https://github.com/alibaba/p3c)

- [《Android开发规范》](https://github.com/Blankj/AndroidStandardDevelop/blob/master/README.md)

- View/Data分层
MVC MVP MVVM 不做强制

- 结构化
能用List动态管理的，绝对不要平铺
高内聚，单一职责

## 基础组件
### 基础库

``` 
    // android base lib
    implementation 'androidx.appcompat:appcompat:1.1.0'
    implementation 'androidx.multidex:multidex:2.0.1'
    implementation 'androidx.legacy:legacy-support-v4:1.0.0'
    implementation 'androidx.appcompat:appcompat:1.1.0'
    implementation 'androidx.recyclerview:recyclerview:1.0.0'
    implementation 'androidx.constraintlayout:constraintlayout:1.1.3'

    // LiveData
    implementation "androidx.lifecycle:lifecycle-livedata:2.1.0"

    // db lib
    implementation "androidx.room:room-runtime:2.2.0"
    annotationProcessor "androidx.room:room-compiler:2.2.0"

    // json lib
    implementation 'com.google.code.gson:gson:2.8.5'

    // Glide
    implementation 'com.github.bumptech.glide:glide:4.7.1'
    annotationProcessor 'com.github.bumptech.glide:compiler:4.7.1'
```

**需要学习的**

[Room](https://developer.android.google.cn/training/data-storage/room/index.html)
[Lifecycle](https://developer.android.google.cn/topic/libraries/architecture/lifecycle)

### 项目共有库
**共同维护，逐步迭代**
    
	Log --本地日志
	crashhandler/ crashReport --异常管理
	EventReport --事件统计
	Utils --工具类
	Network --网络
	BaseViews --基础View
	Permissions --权限
	Compats -机型适配(状态栏，刘海屏）
	BaseFramework --原来HSFramework实现


### UI参考
微信UI开源方案参考，与PM协定
[QMUI Android](https://qmuiteam.com/android)

### 开源库搜索
https://www.ctolib.com/android/#

## 风险规避
 - 个性化Mapping文件
 - AndResGuard
 - 字符串加密（待）
 - 数据库加密（待）

## 效率工具 (待)

- 提高打包速度 freeline
		https://github.com/alibaba/freeline

- 服务端打包


[1]:https://zhuanlan.zhihu.com/p/64869089
[2]:https://medium.com/hackernoon/package-by-features-not-layers-2d076df1964d#.mp782izhh
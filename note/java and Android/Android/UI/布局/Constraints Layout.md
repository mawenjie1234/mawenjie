# ConstraintLayout 

## [android 介绍](https://developer.android.com/training/constraint-layout/)

##[简书参考文档](https://www.jianshu.com/p/768b9e47a77b)

##  1 [负间距](https://juejin.im/entry/5b73d1b96fb9a009ba3fed79)

  利用android.widget.SpaceSpace控件

```xml
<ImageView
        android:id="@+id/iv"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_marginTop="100dp"
        android:contentDescription="@null"
        android:src="@mipmap/ic_launcher"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toTopOf="parent" />

    <android.widget.Space
        android:id="@+id/space"
        android:layout_width="0dp"
        android:layout_height="0dp"
        android:layout_marginBottom="20dp"
        android:layout_marginEnd="20dp"
        android:background="@android:color/holo_blue_bright"
        app:layout_constraintBottom_toBottomOf="@+id/iv"
        app:layout_constraintEnd_toEndOf="@+id/iv" />

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="48dp"
        android:background="@android:color/holo_blue_bright"
        android:gravity="center"
        android:text="Hello World!"
        android:textColor="@android:color/white"
        app:layout_constraintStart_toEndOf="@+id/space"
        app:layout_constraintTop_toBottomOf="@+id/space" />
```



## 链条布局 chains

Chains 以实现想LinearLayout效果，在一个方向上类似群组，其他方向可以单独控制。

* Chains 的属性在第一个view 属性控制。

Chains 有以下几种属性

*  layout_constraintHorizontal_chainStyle
*  layout_constraintHorizontal_weight
*  layout_constraintVertical_chainStyle
*  layout_constraintVertical_weight


## Guidelines




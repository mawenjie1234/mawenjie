# 现阶段遇到的问题

* pad 和 phone 布局大致相同，仅有一些参数不同，但是不知道怎么怎么写到dimen下，导致有两个layout，非常不好维护，一旦新添加一个元素，pad上也得接入。
* 多个flavor 下，布局上回出现不同的按钮，这些按钮有了新的点击事件需要id，如果代码引用id 后，另外一个flavor 就无法打包了。
* 


## 第一个问题，能不能做到只有一个layout

准则：以后开必须只有一个layout

要达到上面的标准，目前我们有什么问题

* constraint layout或者我们自定义的一些属性，不知道怎么添加到values 下

举例：

```
 <android.support.constraint.ConstraintLayout
        android:layout_width="0dp"
        android:layout_height="0dp"
        app:layout_constraintHeight_percent="0.5"
        app:layout_constraintDimensionRatio="194.7:273.7"
        android:background="@drawable/bg_art_dialog"
        >
```


* layout_constraintHeight_percent 实际上是一个float类型，

```
    <item name="dialog_preview_height_percent" type="dimen" format="float">0.61547</item>

```

可以在dimens 下这么写，就可以引用了



* layout_constraintDimensionRatio 实际上是一个string，因此，直接写到string 里面就可以了。

所以完全体应该是

```
<android.support.constraint.ConstraintLayout
        app:layout_constraintHeight_percent="@dimen/dialog_preview_height_percent"
        app:layout_constraintDimensionRatio="@strings/dialog_preview_dimension_ratio"
        android:background="@drawable/bg_art_dialog"
        >
```


接着在不同的values下的dimens或者string 中写不同的机型，不同flavor的值。


## 第二个问题，不同包下的id不一样怎么办

准则： id应该尽量一致，如果不一致，暂时可以在ids下声明，这样别的flavor也可以编译没有问题。

* 在main/values/ids.xml 下描述好id
```
<item name="preview_continue_btn" type="id"/>
```


## 最后一个问题，bug 修改了，art和paint不能同步怎么办？




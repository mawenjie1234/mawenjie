  # UI适配，density适配方式

## 集成

1. app下的build.gradle implementation 'me.jessyan:autosize:1.1.2'
2. AndroidManifest.xml 添加默认设计尺寸

```
<application>
        <meta-data
            android:name="design_width_in_dp"
            android:value="250"/>
        <meta-data
            android:name="design_height_in_dp"
            android:value="444"/>
    </application>
```

## 举个例子

```
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    >
    <ImageView
        android:id="@+id/top_banner_bg"
        android:layout_width="0dp"
        android:layout_height="0dp"
        app:layout_constraintTop_toTopOf="@+id/top_banner_pic"
        app:layout_constraintBottom_toBottomOf="@+id/top_banner_pic"
        app:layout_constraintLeft_toLeftOf="@+id/top_banner_pic"
        app:layout_constraintRight_toRightOf="parent"
        android:layout_marginEnd="10dp"
        android:background="@drawable/white_rectangle"
        android:layout_marginTop="7.3dp"
        android:layout_marginBottom="7.3dp"
        android:layout_marginStart="20dp"
        />
    <ImageView
        android:id="@+id/top_banner_pic"
        android:layout_width="132.3dp"
        android:layout_height="132.3dp"
        app:layout_constraintTop_toTopOf="parent"
        app:layout_constraintLeft_toLeftOf="parent"
        android:layout_marginTop="13.3dp"
        android:layout_marginStart="6.7dp"
        android:src="@drawable/invalid_name"
        android:scaleType="fitXY"
        />
    <TextView
        android:id="@+id/top_banner_title"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        app:layout_constraintLeft_toRightOf="@+id/top_banner_pic"
        app:layout_constraintTop_toTopOf="@+id/top_banner_bg"
        app:layout_constraintRight_toRightOf="@+id/top_banner_bg"
        android:text="Editor’s Choice"
        android:textSize="12dp"
        android:textColor="#000000"
        android:layout_marginTop="17.7dp"
        android:fontFamily="@font/avenirnext_bold"
        />

    <TextView
        android:layout_width="0dp"
        android:layout_height="wrap_content"
        app:layout_constraintTop_toBottomOf="@+id/top_banner_title"
        app:layout_constraintRight_toRightOf="@+id/top_banner_bg"
        app:layout_constraintLeft_toRightOf="@+id/top_banner_pic"
        android:textColor="#000000"
        android:text="Explore the image recommended by editors"
        android:layout_marginStart="6dp"
        android:layout_marginEnd="13dp"
        android:textSize="9.3dp"
        android:layout_marginTop="6.7dp"
        android:fontFamily="@font/avenirnextltproregular"
        android:lineSpacingExtra="1dp"
        android:letterSpacing="0"
        android:alpha="0.8"
        android:gravity="top"
        />

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="OPEN"
        android:textSize="9.3dp"
        app:layout_constraintBottom_toBottomOf="@+id/top_banner_bg"
        app:layout_constraintRight_toRightOf="@+id/top_banner_bg"
        android:background="@drawable/red_rectangle"
        android:layout_marginRight="9.3dp"
        android:layout_marginBottom="9.3dp"
        android:textColor="#ffffff"
        android:paddingTop="4.3dp"
        android:paddingBottom="4.3dp"
        android:paddingLeft="12.3dp"
        android:paddingRight="12.3dp"
        android:fontFamily="@font/avenirnext_bold"
        />
</androidx.constraintlayout.widget.ConstraintLayout>
```

各个手机上的效果

* 小米mix3， 超级长的手机1080 * 2340
 <img src="$resource/Screenshot_2019-09-29-14-26-03-066_com.example.myapplication.png" width = "300" height = "650" alt="图片名称" align=center />

* 红米note3， 前几年普通5.5寸1920*1080手机
 <img src="$resource/Screenshot_2019-10-03-02-32-22-055_com.example.myapplication.png" width = "300" height = "533.33" alt="图片名称" align=center />

* 小米5s，5寸 1920*1080
 <img src="$resource/Screenshot_2019-10-02-14-43-09-593_com.example.myapplication.png" width = "300" height = "533.33" alt="图片名称" align=center />
* 4.3寸 800x480
![image]($resource/image.png) 

## 有些页面不想用怎么办

老ui可以无论是activity还是Fragment，都可以可以继承CancelAdapt 这个接口
```
public class MainActivity extends AppCompatActivity implements CancelAdapt {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.main_activity);
    }
}

```

```
public class MainFragment extends Fragment implements CancelAdapt {

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container,
                             @Nullable Bundle savedInstanceState) {
        return inflater.inflate(R.layout.main_fragment, container, false);
    }
}
```


## 有个界面设计尺寸不一样怎么办

可以继承CustomAdapt，并且自己实现两个函数
```
  public class MainFragment extends Fragment implements CustomAdapt {

    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container,
                             @Nullable Bundle savedInstanceState) {
        return inflater.inflate(R.layout.main_fragment, container, false);
    }
    
    @Override
    public boolean isBaseOnWidth() {
        return false;
    }

    @Override
    public float getSizeInDp() {
        return 0;
    }
}
```

## pixel 图片变小，变模糊

使用这个方式，bitmap会有问题，在glide 的 transform 里面设置bitmap DisplayMetrics

```
Bitmap bmpGrayscale = Bitmap.createBitmap(LandApplication.getInstance().getContext().getResources().getDisplayMetrics(),
                width, height, Bitmap.Config.ARGB_8888);
```


## 框架缺陷
* activity 继承CancelAdapt后，如果setCustomFragment(true)，那么他里面的fragment没用用，仍然会自动缩放。这个会拉出一个分支自己实现。
* 设计尺寸是int，不能是float值。自己拉分支修改
* 圆角dp不准确，正在尝试解决为什么不准确。
*  splash 页面上也是bitmap，所以大小有问题，正在尝试怎么解决。


## FQA
### 1. 是否会对pad适配有影响。

对sw600 的值不会影响，如果sw600里面有值，仍然使用sw600的值。

### 2. density 是全局的，如果受第三方修改怎么办

重写Activity getResource

```
  @Override
    public Resources getResources() {
        AutoSizeCompat.autoConvertDensityOfGlobal((super.getResources());//如果没有自定义需求用这个方法
        AutoSizeCompat.autoConvertDensity((super.getResources(), 667, false);//如果有自定义需求就用这个方法
        return super.getResources();
    }
```

### 其他问题

[github上问题汇总](https://github.com/JessYanCoding/AndroidAutoSize/issues/13)




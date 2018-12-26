# Activity
## 生命周期

onCreate() -> onStart() -> onResume() -> onPause() -> onStop() -> onDestroy()

Android P(api : 28, version : 9) 之后  onSaveInstanceState(Bundle) 会在 onStop()之后调用。3.0 之后是在 onPause()之后，在onStop 之前。


```
For applications targeting platforms starting with Build.VERSION_CODES.P 
onSaveInstanceState(Bundle) will always be called after onStop(), 
so an application may safely perform fragment transactions in onStop() and 
will be able to save persistent state later.
```

Activity 跳转的时候Activity的生命周期怎么走。

Activity a -> b

a onPause() -> b onCreate -> b onStart - > b onResume() -> a -> onStot() -> a onDestroy()




# Fragment
## 生命周期
## 懒加载

# Context


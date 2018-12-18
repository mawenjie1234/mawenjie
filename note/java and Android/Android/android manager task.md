# Manager task

## 定义launch module 的不同方式
* 在Manifest.xml 中描述
* 使用 intent flags 在startActivity()

## Manifest 中的launch module

* standard(default)


  每次启动都是一个新的activity的实例，每个实例可以属于不同的task， 一个task 可以有多个实例。

* singleTop

  如果当前的activity D 是在栈中的最上方，startActivity 会触发D的 onNewIntent()， 不会穿件一个新的。
  如果startActivity 触发的是其他的，那么这个时候回重新创建一个新的Activity，就算B 的实例已经在栈中切launch module 是 single Top，
  
  所以singleTop的逻辑就是，查看当前要出的Activity是否在栈顶，如果是， 就调用栈顶Activity 的onNewIntent(), 如果不是栈顶，那么就新创建一个实例。
* singleTask


* singleInstance
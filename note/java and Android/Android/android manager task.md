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

  只会有一个实例。 如果有一个实例已经在当前task中，那么在这个实例上面的Activity都会被destroyed，这个实例并且会调用onNewIntene()。

注意 ： 文档中写说 如果使用singleTask， 

```
The system creates a new task and instantiates the activity at the root of the new task.
```

但是实际上并不会，所以我们需要和描述中说的一样，除了设置launchmode 还需要设置 taskAffinty


* singleInstance

一个task只能有一个Activity， 并且系统中只有一个实例。

  * 多个Activity back 表现
  * 多个Activity 会后台表现。
  * 多个Activity 会被干掉么
  * 多个activity 并使用 taskAffinty 后的表现。


# 综上产生的问题 

1. taskAffinty 是什么，怎么使用。有什么效果。
   * taskAffinty 的值如果不写的话，默认是包名，也可以写别的类似包名的值，必须包含点。
   * singleTask 加上他才会让Activity 创建到不同的task 中，并且之后从当前Activity启动的Activity都从在创建的task中。


2. 最好不要让新的Activity 到新的task 中，这样新的Activity 退到后台然后从icon进来的时候，是从默认task 中启动，

   结果 ： A(task a)-> B(task b)-> bg -> icon -> A(task a) -> onBackPress -> home
   
   中间的b会在退到后台然后重新点击icon进入的时候，无法出现。

# 补充

* singleTask 做启动页

  如果application被干掉的话，如果什么都不做，下一次点击icon会进上次用户停留的Activity，并saveInstance 不为空。如果我们有些必须要做的操作是在启动也上做，这个时候恢复Activity会出错，我们就必须要每次都进入启动页，那么可以设置启动也是singleTask,。
   
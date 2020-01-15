# UIWidgets 简介

* 简单看一下我们用UIWidgets做的APP

* 是 Unity 的一个UI Framework，从 Google 的 Flutter 演变过来的 UI 框架。
  * Flutter ： Design beautiful apps
  * Flutter 像一个游戏引擎帮你做app。
* UIWidgets 运行效率：和专业人员手工调整后运行效率媲美。

## 为什么要用UIWidget

### Unity 做app有什么劣势

* 打图集（一个Android程序员做app忽然要涉及打图集了）
* 有ui发生变化，canvas就需要重绘，不能只重绘脏数据。（所以需要把静态的节点和动态的节点放在不同的canvas上解决效率问题）
* 拖拉拽做UI的方式太好用了，结果是配置文件多人修改真的很难merge。
* 使用unity 原生做一个复杂app比较费事的（来自unity 中国开发团队）

### UIWidgets有什么优势

* 比起拖拉拽之后生成的文件，UIWidgets可以追踪，容易解决冲突。
* 要做复杂ui，要有很好的交互，UIWidgets更合适。
* 只绘制脏数据。（解放界面调优人力）
* 不再需要程序员打图集了，自动动态合批图。（解放在打图集的人力）
* 原生程序员转比较容易，不需要全部了解UGUI，了解一些Flutter就能写UIWidgets，一些原生的理念也容易理解。



## UIWidgets中设计语言

```c#
namespace MF.Art.Game
{
    public class FavoriteWidget : StatefulWidget
    {
        public override State createState()
        {
            return new _FavoriteWidgetState();
        }
    }
    
    class _FavoriteWidgetState : State<FavoriteWidget>
    {
        bool _isFavorited = true;
        int _favoriteCount = 41;

        public override Widget build(BuildContext context)
        {
            return new Center(child:
                new Column(children: new List<Widget>()
                {
                    new GestureDetector(
                        child: _isFavorited ? Image.asset("") : Image.asset(""), 
                        onTap: _toggleFavorite
                    ),
                    new Text($"{_favoriteCount}")
                }
            ));
        }

        private void _toggleFavorite()
        {
            setState(() =>
            {
                if (_isFavorited)
                {
                    _favoriteCount -= 1;
                    _isFavorited = false;
                }
                else
                {
                    _favoriteCount += 1;
                    _isFavorited = true;
                }
            });
        }
    }
}
```





## 一个例子 ：MFCachedImage



## 遇到问题？

### 举个例子

​	用户画了图之后，列表页面需要刷新，但是Image.file()没有提供删除特定文件缓存的API。

​	查看源码知道ImageCache中有个Map缓存了图，当到达一定内存后可以回收，发现evict方法可以删除map中特定图。

* 先使用flutter关键字搜索是否有解决方案
* 直接在UIWidgets源码看究竟如何实现。














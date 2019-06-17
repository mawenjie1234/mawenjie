# 需要解决的问题

## 提高速度
 
## 优化内存

目前 anr 中gc 导致的很多，需要内存重复利用


# 大量new 对象的地方

## Picture new 的时候

* mOriginalBitmap  BitMap
* mUserPaintBitMap BitMap
* mPixels 200 * 200 pixel 
  1. int x, y, color, drawcolor
 
*  mPaintColors 颜色对应的点
    每一个 PaintColor  中有 
  1. mPixelPositionList Point, 
  2. int color, paintCount



总结 

Pixel
* （mPixels + colorPoint） * 40000


Point 

* Line : startPoint, endPoint 一共有多少个line 对象？
* FindAdjacentPoint 找附近格子 ： 每次点击，点击中间产生2个point，点击周围 产生 4个point
* RecordView 回放功能， 每一帧都产生当前 帧数对应的point 和 RectInfo， 最后一帧有4w个点， 倒数第二针有3w以上个点， 时隔 20ms
* calculateGuidePoint 每次次都产生一个点
* PixelRender mHintLayout 初始化第一个颜色所有点， 如果颜色有2w个，就会create 2w个 point 和 RectInfo
* PixelCanvasRender initHintInfos 和上面类似，这个类已经没有用了
*  Pen pixelDrraw 错误涂色 会new point 和 RectInfo
* Pen drawRectAndSave 画一个点的时候，就会new point 和 RectInfo，
* BrushPen longPress 不是sand box 画法，长按就会new point 和 RectInfo 
* 长按 startLongPressAnimation 每次出现长按动画，都会new point 和 RectInfo
* BrushPen onColorCompleted 
* BrushPen 每次画一个点出现粒子的时候，会new point 和 RectInfo
* BrushPen getHintInfos 当前颜色的点都会new point 和 RectInfo
* BrushPen drawRectAndSave 会new point 和 RectInfo
* 



PointF
* mTextLayout initTextInfos() new 4w PointF 和 TextInfo


RectInfo


TextInfo
* mTextLayout initTextInfos() new 4w PointF 和 TextInfo

Line
* 线，最多1w个，一般几千个撑死了。


## drawing 中数据





# 目前卡顿点
* new picture 的点
* 


# 算法优化

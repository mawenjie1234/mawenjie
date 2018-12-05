1. 安装GT Android app  到[下载链接](https://github.com/Tencent/GT/releases)找到v3.1.0 下的 Android.GT.v3.1.0.release.zip
2. git clone [GT项目](https://github.com/Tencent/GT/tree/master/android) 主要用于最后查看报告。
3. 添加GT 3.+ sdk， 也可以参考zip包里面 《SDK引入说明》。
   * 我们项目 app 下 build.gradle 添加 implementation 'com.tencent.wstt.gt:gt-sdk:3.1.0'
   * 修改miniskd 到21
   * application 在初始化的时候 调用  GTRController.init(this);
4. 如何测试
   * 安装加好代码的 app到手机上。
   * 如果遇到 activities.MainActivity} did not call through to super.onCreate() 挂了，那么就换机器。经测试，可以进行测试的机器是 Android-032, Android-051 
   * 装好app能运行后，打开 GT， 选择测试app， 点击开始， 会自动打开我们的app， 直到我们认为测试完成后，回到GT的app 点击停止。
   * 导出数据 -> 导出到本地 文件放到了 sdcard/GTRData 下，可以使用 adb pull  /sdcard/GTRData/data.js 导出到自己的电脑上，
   * 复制导出的 data.js 到 GT项目的 android/GT_Report/data/data.js ,然后打开 GT_Report/result.html 就可以看到结果了。

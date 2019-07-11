## 结论

* 手机内存大的时候，native 分配1G内存也不会崩溃。
* java 分配内存就算在大内存手机上，开到500M+就崩溃了
* 如果java 分配了400M内存，没有到达oom上限，此时手机内存足够，native分配1G内存也没有问题
* 在内存小的机器上，比如s5的机器（机器2G），native 和java 都最多只能分配到500M+，因为手机确实没有内存可用了。

## 测试

* 小米9，内存6G，手机剩余内存3G+，native 分配1200M +内存后崩溃
* 小米9，内存6G，手机剩余内存3G+， java 分配内存500M+后崩溃
* 三星s5 ,内存2G，手机剩余内存不足1G， native 分配400M+后崩溃
* 三星s5，内存2G，手机剩余内存不足1G，java 分配400M+后崩溃。

以上测试都在pixel 程序上运行，无网，程序本身启动后就会有200到300M内存。

[Google Drive文档链接](https://drive.google.com/file/d/1HMz7kbVgqVK-hfDxznmddhrxrVratHAq/view?usp=sharing)
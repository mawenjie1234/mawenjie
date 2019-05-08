# CGFolder 设计


CGFolder 从命名角度考虑就是是个单独的模块，为了其他项目可以用，因此只需要一些简单的输入输出即可，可以配置的就从配置入手，

基于以上考虑，新的需求将采取以下策略

* 添加preload remote， 提前下载json 文件，
* 远端地址和本地地址都在folder sync 模块内自行读取，只调用 asyncAssets 或者asyncRemote 就可以。
*  远端读取那个地址由Folder sync 决定， 就是 CGFolder_UER 和 CGFolder_UER_olduser。
* 去掉sync time interval 每次都应该子线程请求。
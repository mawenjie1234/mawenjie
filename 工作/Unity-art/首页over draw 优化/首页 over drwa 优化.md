优化之前

<img src="%E9%A6%96%E9%A1%B5%20over%20drwa%20%E4%BC%98%E5%8C%96.assets/image-20201022113008050.png" alt="image-20201022113008050" style="zoom:40%;" />

理论优化

<img src="%E9%A6%96%E9%A1%B5%20over%20drwa%20%E4%BC%98%E5%8C%96.assets/image-20201022144349171.png" alt="image-20201022144349171" style="zoom:40%;" />



<img src="%E9%A6%96%E9%A1%B5%20over%20drwa%20%E4%BC%98%E5%8C%96.assets/image-20201022164844671.png" alt="image-20201022164844671" style="zoom:80%;" />

可优化点

* item上的board 中间镂空，减少一层overdraw
* 左上角 new 标志占用了一层over draw
* item 最外层的一个白色image 有一层，可以使用shader的方式去掉


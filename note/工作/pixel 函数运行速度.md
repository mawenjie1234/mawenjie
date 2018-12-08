
# picture 读取csv 版本 2018/12/8
* 测试机型 红米note3
## 测试数据
### PictureMeta
* 数据库 init 2 2 | 4 2 6
* picture Manage 初始化 144 116 | 93 96 81
* DBDao.getInstance().getAllPictureMeta() 100 90 | 48 67 47
  * 读取 loadResource  | 21 35 23
     1. 当前picture 的数量 997
     2. 读取csv ：31 32 | 13 21 11
     3. 解析csv ：13 30 | 8 14 12
    * 解析 56 | 
* DBDao.getInstance().getCategoryList()
  1. 当前数量
  2. 获取csv 1 1 | 1 1 1
  3.解析csv 8 6 | 6 4 3

### Picture 


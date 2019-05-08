# ES

## 数据结构

### 数据库

数据库是单独的一个数据库， es这个模块自己维护
* 名字
* log 的表， 表名 ， 表字段


## 结构

### es上报模块, ESUpload
#### 接口

* static commit(Log);
   * 创建线程池子上报，
   * 参数断言
   * 使用库里面的 HSConnection
   
* listener result(result : boolean, Error : Object, ) 

class : Log
listener
ids
List<String> logs

### 功能 Manager 名称 CGLog
* static logAction(String action, Map<>)
  * 给线程池
  * 拼接基础的key，
    *  db 存储
    * 存完 count ++
  * 够了10条， commit
  * 成功， db delete
  * 失败，
  
   
   
### DC
   
   
   
static Map<> baseEvent

### 数据库




* 新建线程，上报数据，
* 如果






 eventValue.put("action", eventName);
            eventValue.put("uid", HSApplication.getInstallationUUID());
            eventValue.put("log_time", getISOUTCString(new Date()));
            eventValue.put("ProductName", HSApplication.getContext().getApplicationInfo().packageName);
            eventValue.put("DeviceType", Utils.isTabletDevice() ? "android_pad" : "android_phone");
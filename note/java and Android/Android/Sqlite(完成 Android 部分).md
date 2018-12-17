# 疑问
* 为啥要用sqlite 
* transaction 啥时候用，怎么使用，能提高效率么✅
*  SQLiteStatement 是干嘛的，为什么事先compileStatement一次就优化性能。✅
*  Cursor是啥。 ✅


# Android 28 datebase 源码分析

  从以下四个方向入手。

## query

### db.rawQuery(String sql, String[] selectionArgs)

* 执行函数 
```
public Cursor rawQueryWithFactory(
            CursorFactory cursorFactory, String sql, String[] selectionArgs,
            String editTable, CancellationSignal cancellationSignal) {
        acquireReference();
        try {
            SQLiteCursorDriver driver = new SQLiteDirectCursorDriver(this, sql, editTable,
                    cancellationSignal);
            return driver.query(cursorFactory != null ? cursorFactory : mCursorFactory,
                    selectionArgs);
        } finally {
            releaseReference();
        }
    }
```

实际上让 SQLiteDirectCursorDriver 去查询，进入 query

```
    public Cursor query(CursorFactory factory, String[] selectionArgs) {
        final SQLiteQuery query = new SQLiteQuery(mDatabase, mSql, mCancellationSignal);
        final Cursor cursor;
        try {
            query.bindAllArgsAsStrings(selectionArgs);

            if (factory == null) {
                cursor = new SQLiteCursor(this, mEditTable, query);
            } else {
                cursor = factory.newCursor(mDatabase, this, mEditTable, query);
            }
        } catch (RuntimeException ex) {
            query.close();
            throw ex;
        }

        mQuery = query;
        return cursor;
    }
```

  返回的cursor CursorFactory 调用newCursor 拿出来的.
  * SQLiteQuery 
    1. bindAllArgsAsStrings // 把 上方 selectingArgs 分别插入到 sql中。
  * SQLiteCursor
     ```
     SQLiteCursor中的CursorWindow这个家伙去native 取数据。返回来的Cursor 并没有把全部的查询数据都取出来，只有cursor.getSring() 等操作发生的时候，去native取数据。
     例子 ：如果有5列，有1000行数据的话，那么就会调用native 的次数是 5*1000
      
     CorsirWindos 的查询函数是
          public String getString(int row, int column)
      
     ```


## insert
### insert 的方式
  * 使用db 
    ````
     db.insert()
    ````

  * 使用预选处理好的SQLiteStatement
    ```
    statement.clearBinding();
    statement.bindString(index, value);
    statement.executeInsert()
    
    ```

db.insert 会调用 insertWithOnConflict() 并创建一个sql的String，新生成一个SQLiteStatement。

如果大批量插入表的时候，可以使用第二种方式。直接生成一个sql语句的SQLiteStatement对象。不过使用第二种形式，需要调用 statement.close()。

#### 那么，插入操作又是使用了哪些类，哪个关键的哥们调用了Native的方法。

statement.executeInsert()后调用 getThreadSession()。

SqlSession 中使用 SQLiteConnection 调用native的方法进行插入。
```
问题： getThreadSession（）为啥要确保一个线程只有一个session。
确保一个线程只有一个数据库的链接，如果一个线程尝试有很多个链接，那么就有可能会发生死锁。
```


---
### 如何使用事务

1. 事务 ： 事务是在数据库上按照一定的逻辑顺序执行的任务序列。
2. 如果我们没有明显的使用事务，其实我们每一次的插入，修改等操作都是一个隐式事务。如果进行大批量的修改操作，可以使用显示事务提高效率



```
db.beginTransaction()；
try {
    //do 
    db.setTransactionSuccessful()；
}finally{
   db.endTransaction()；
}
```




## update
update 同上面的insert的用法一致，也是有两种形式，statement 执行executeUpdateDelete(), 所以在大量操作都修改的时候，也最好使用预先编译过一次的statement来进行。
也是由 SqLiteConnection调用antive 方法。


## delete

同 update 和 insert。


# 怎么写

## insert

* 大批量数据插入删除或者修改

```
  db.beginTransaction()；
try {
     
    String sql = "insert into table (id , name, isFree ) values(?,?,?)"；
    SQLiteStatement sqliteStatement = db.compileStatement(sql);
    for(100){
      sqliteStatement.bindValue("wenjiema", 1)；
      sqliteStatement.executeInsert();
    }
    sqliteStatement.close();
    db.setTransactionSuccessful()；
}finally{
   db.endTransaction()；
}
```

* 只有一个数据插入删除修改
 db.insert(), db.update, db.delete()；

# 数据库操作耗时

查询 1000个 



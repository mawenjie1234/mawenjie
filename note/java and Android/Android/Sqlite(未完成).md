# 疑问
* 为啥要用sqlite 
* transaction 啥时候用，怎么使用，能提高效率么
* 第一次创建表并添加完数据后，是什么让之后马上读取变得非常快。
*  SQLiteStatement 是干嘛的，为什么事先compileStatement一次就优化性能。✅
*  ContentValues做了什么
*  Cursor是啥。 ✅
*  Android 中的框架图


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
     CursorWindow windows 这个家伙去native 取数据 也就意味着，返回来的Cursor 就是一个对象，只有getSring 等操作发生的时候，去native取数据。
     所以如果有5列需要查，并且有1000行数据的话，那么就会调用native 的次数是 5*1000
          public String getString(int row, int column)
      
     ```


## insert
* insert 的方式
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

db.insert insertWithOnConflict() 的第一步会创建一个sql的String，并新生成一个SQLiteStatement。如果大批量插入表的时候，可以使用第二种方式。避免生成sql语句和SQLiteStatement对象。不过使用第二种形式，需要调用 statement.close()。 （基本上Sql的类都继承了SQLiteClosable）

那么，插入操作又是使用了哪些类，哪个关键的哥们调用了Native的方法。[这篇文章写的更好](https://wqyjh.github.io/2016/12/22/Android-SQLite-%E6%BA%90%E7%A0%81%E5%88%86%E6%9E%90/)










## update

## delete
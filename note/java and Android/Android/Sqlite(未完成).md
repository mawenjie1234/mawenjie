# 疑问
* 为啥要用sqlite 
* transaction 啥时候用，怎么使用，能提高效率么
* 第一次创建表并添加完数据后，是什么让之后马上读取变得非常快。
*  SQLiteStatement 是干嘛的，为什么事先compileStatement一次就优化性能。
*  ContentValues做了什么
*  Cursor是啥。 ✅
*  Android 中的框架图


# Android 28 源码分析

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
     ```


## insert


## update

## delete
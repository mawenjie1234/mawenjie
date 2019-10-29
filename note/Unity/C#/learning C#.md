# 数据类型
## 值类型
bool int char double float long

## 引用类型
* Object 所有引用类型的基类

```
Object obj;
obj = 100; 装箱
```

* Dynamic 动态类型，可以存储任何值。

```
dynamic d = 20;
```

* Strng 字符串类型
```
String str = "aaa";
string str = @"sds\dssd" // 加上@后\也是一个字符，不是转义
string str = "sds\\dssd" // 和上一行一样。
```

* 指针， 和c，c++一样。

# 常量 Const

# 运算符
* 判断对象是否同一个类型 is， if(Food is Car)
* 双问号 ？？，判断是否为null
```
double? num1 = null;
double? num2 = 3.14157;
double num3;
num3 = num1 ?? 5.34;      // num1 如果为空值则返回 5.34
```


# 封装
* 通过访问修饰符
* 默认访问修饰符是private

# 结构体 Struct
```
struct Books{
 private string title;
   private string author;
   private string subject;
   private int book_id;
   public void getValues(string t, string a, string s, int id) {
      title = t;
      author = a;
      subject = s;
      book_id =id;
   }
}
```

* 结构不能有默认构造函数
* 结构不支持集成
* 结构值值类型。

# 枚举
```
enum Days{Sun, Mon, Tue, Wed, Thu, Fir, Sat}
//sun is 0, Fir 是5
```


# 继承

```
class Rectangle : Shape, PaintCost{
...
}
```


# abstract 和 virtual
* 使用virtual后，子类要重写父类的同名函数，必须写override
* abstract 是为了不让new 
* 接口仍然使用interface



# C# 特性 Attribute

* [Conditional("DEBUG")]

```
  [Conditional("DEBUG")]
public void Message(string msg) {
  .....
}
```


* Obsolete 标记不应该使用的程序实体

```
  [Obsolete("Don't use OldMethod, use NewMethod instead", true)]
void OldMethod(){
  ...
}
```

* 自定义特性










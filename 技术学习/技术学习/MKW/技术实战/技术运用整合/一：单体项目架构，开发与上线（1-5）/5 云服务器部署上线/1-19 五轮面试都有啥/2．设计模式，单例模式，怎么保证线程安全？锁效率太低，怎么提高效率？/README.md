---
title: 2．设计模式，单例模式，怎么保证线程安全？锁效率太低，怎么提高效率？
---

# 2．设计模式，单例模式，怎么保证线程安全？锁效率太低，怎么提高效率？

好的,关于单例模式的线程安全,有以下几种方法:

1. 加同步锁
可以对getInstance()方法加同步锁,确保同一时间只有一个线程可以进入该方法。具体实现如下:

```java
public class Singleton {

  private static Singleton instance;

  private Singleton() {}

  public static synchronized Singleton getInstance() {
    if (instance == null) {
      instance = new Singleton();
    }
    return instance;
  }

}

```

这种方式可以保证线程安全,但是效率较低,因为每次调用都要加锁。

1. 双重检查锁定
先判断实例是否存在,如果不存在才加锁创建实例。这样可以提高效率。实现如下:

```java
public class Singleton {

  private volatile static Singleton instance;

  private Singleton() {}

  public static Singleton getInstance() {
    if (instance == null) {
      synchronized (Singleton.class) {
        if (instance == null) {
          instance = new Singleton();
        }
      }
    }
    return instance;
  }

}

```

需要注意的是实例变量需要加volatile关键字,保证线程可见性。

1. 静态内部类
利用静态内部类的初始化时机来保证线程安全。实现如下:

```java
public class Singleton {

  private static class SingletonHolder {
    private static final Singleton INSTANCE = new Singleton();
  }

  private Singleton (){}

  public static final Singleton getInstance() {
    return SingletonHolder.INSTANCE;
  }

}

```

静态内部类只会在第一次调用getInstance()时初始化,从而保证线程安全。

1. 枚举
可以直接使用枚举实现单例:

```java
public enum Singleton {
  INSTANCE;
}

```

枚举天然就是单例的,线程安全,并且可以防止反序列化导致重新创建新的对象。

以上几种方法都可以保证单例的线程安全,可以根据实际需要选择使用。



请问在多线程环境下，哪种单例模式的线程安全性最好？

在多线程环境下,想要实现单例模式线程安全,枚举实现单例模式是最好的选择。

理由如下:

1. 枚举天生就是单例的
Java枚举类型定义的枚举变量只会有一个实例,所以它天生就是单例的。

1. 线程安全
枚举类是线程安全的,它的编译完成时添加了线程安全处理的代码。

1. 防止反序列化破坏单例
如果单例类允许反序列化,通过反序列化可能会破坏单例,而枚举是不可反序列化的。

1. 直接使用
实现枚举单例很简单,只需要定义一个枚举类型,并在内部实例化单例对象。

所以在多线程环境下,枚举实现单例模式是最好的选择。它简单、直接、线程安全,综合性能是最好的。

例如:

```java
public enum Singleton {
  INSTANCE;
}

```

这样就可以直接通过 Singleton.INSTANCE 来获取单例实例,非常简单高效。

所以 多线程安全的单例模式,枚举实现是首选。


锁效率太低，怎么提高效率？

为了提高 synchronized 实现单例的效率,可以使用双重检测锁方式。

双重检测锁在 getInstance() 方法中,进行两次 null 检查,并只有在实例为 null 时,才对实例化代码加锁。这样可以大大提高效率。

具体实现代码如下:

```java
public class Singleton {

    private volatile static Singleton instance;

    private Singleton() {}

    public static Singleton getInstance() {
        if (instance == null) {
            synchronized (Singleton.class) {
                if (instance == null) {
                    instance = new Singleton();
                }
            }
        }
        return instance;
    }

}

```

这里主要改进有两点:

1. 加入 volatile 关键字,保证实例的可见性
1. 两次 null 检查,只在必要时加锁
这样当实例已经创建时,不加锁就直接返回实例,大大提升了效率。

但双重检测锁也有可能存在指令重排序的问题,需要注意正确实现。

所以综合来说,双重检测锁比直接加锁效率更高,但不如枚举实现的简单和高效。在追求高性能的场景下可以考虑使用。


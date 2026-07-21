---
title: 1-4 架构设计基本原则：迪米特原则与里式替换
---

# 1-4 架构设计基本原则：迪米特原则与里式替换

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/43e2527d-1e62-4390-b29b-b7af4162cd54/SCR-20240808-pkcc.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466URY56UPN%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230355Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGQQ2XACqSgtk6ZS9Vav%2ByZzM2I74wEl1LFEuX6qnjteAiAAmA6g41uswpo09rUKLZRynVOzZ4oCaedwlxlIdlgv7CqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRtEnJyFtyEU4pMkCKtwD8%2FpSrNGHnQvhqqPJlXSHsmu1sG4frxD3rPG%2FgmTcK01RK9%2B0El2faQTf9fE%2B5YBVzCFD%2FXdf660eXN%2B9DjmIa4gZ5Alg9v%2BJNfvVd9e8JdB%2F20uBuD9mtT13gdQaUUGXeAOsjO2F4ldaxWYgv1tnd6xUeGTeanpaUpyhUn8tVDCnHTRdbJl%2B6Lzc4yrAeqKiTPA911AovkNkTcGZoQioxUW37PrCJ74E50g1ZT0drBCh2xIfeIp%2FHIZ4ZfXgARBIo8cJA8xq%2FQQWv37fP%2BGR8GIP400WNcDtO9pDBh15k2ZC9ZcwgP%2FNjbQLiHuNayvZ36u%2FOPlsqf6XRjdhV427Jt8fEGxAdUQfmfbnEojE7%2FxqKS6hN8l%2FrqC0O9ppwDBJsLt4kMx05jCIJDTLtZuX5Bydx0I50otfaPtSR9D42OE68Ed8xlEhFiURN2yPKJ51cx31QdCJ46fHD0hw4ufgH%2FkoLf%2BNYnnYg%2FceIg2QzgJKZK7nZHxpY5ATWWnJgH4%2BgdddVV7TV874s5%2F7LuapAacoHhsnKHiJEFTazpSH707Q0QQGCsMZfKUpOCNIeBd30TL2P9AVF04tlWnePBI6qyNr34BgFV8C6Vpf81x57wxJtmHrHdwnF8nqFqIwzbf%2F0gY6pgHc1FaMxSvTW347qoF3ldlHuMXhj4SAK95loQelPq%2FwV2L8D%2BmRPyR9sGGV5iLkI%2BG63%2BRU4O%2Fevu2RBuwkEmz%2FZBlm7UW8ecQ5HIEqvS%2FyvYmJ8oAHSBgmVBaris%2Fvru%2Fyh588JghBxT%2BnX30eszs1oPHqgvIouaoGkhFD%2F1UEfOGgylbH33M2L2nPFES6HEhzOTWA64KlI8rXzl0PzioT5sMjLZ1e&X-Amz-Signature=2716aefac5727f930324c4f3bb802cf86b53eb94dff11ac9401403484d75c41a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

1—4架构设计基本原则：迪米特原则与里式替换
迪米特原则
迪米特原则可谓是出身不凡，它在1987年由North
7年由Northeastem University（美国的东北大学）的lan Holland提出， 在经典著作《The Pragmatic Programmer》中被普及开来。
迪米特原则（Law of Demeter）是指一个对象应该尽可能的保持高冷的姿态，少和其他对象勾搭，尽量对自己以外的对象保持最小了解。因此，迪米特原则又叫做最少知道原则（Least Knowledge Principle）。一句话总结就是—不要和陌生人说话。
在软件的微观架构层面，通过迪米特法则我们可以尽可能降低类之间的耦合。对于一个类来说，什么是朋友，什么是陌生人呢？我们用一个例子来解析迪米特原则：
有一波未来的架构师们（对没错就是你们）来慕课网上学习，学习何等枯燥，得找个有意思的老师跟着学才学
部个老师学风最风骚，这个过程可以用以下的三个类来表示：


```java
public class IMoocGirls{ 
public void findFengSaoTeacher(List<Teacher>1ist){
			Teacher teacher =1ist.stream().sorted(xxx).findFirst().g
			System．out．print1n（“最风骚的老师配最风骚的课程”＋teache }
}
```


慕课网的小姐姐们，通过这个方法筛选最风骚的老师


```java
public class Architect {
public void chatWithImoocGir1(IMoocGir1 gir1){ 
      List<Teacher> teacherList = Lists.newArrayList(); ／／xxxx 读取所有老师列表
			gir1.findFengSaoTeacher(teacherList): }
}
```


架构师通过勾搭小姐姐，打听到最风骚的讲师是谁。从这个例子中可以看出，Architect架构师只想获取结果就行了，他并不需要和讲师直接产生关系，在这个例子中，小姐姐是Architect
而Teacher是陌生人。 应用迪米特法则，我们应该如何修正架构呢？这样来：

```java
public class IMoocGirls {
			public void findFengSaoTeacher(){ 
			List<Teacher>teacherList =Lists.newArrayList(): 
      ／／xxxx 读取所有老师列表
			Teacher teacher= teacherList().sorted(xxx).findFirst().g
			System．out．print1n（“最风骚的老师配最风骚的课程”＋teache 
   }
}
public class Architect{
		public void chatWithImoocGir1(IMoocGir1 gir1){
		gir1.findFengSaoTeacher():
   }
}
```



从上面的例子中可以看出，Architect只和IMoocGirl打交道，而和Teacher已经完全没有关联了，避免了类与类之间的耦合。
**里氏替换原则**
里氏替换原则（Liskov Substitution Principle）的原文需要汉语十级才能读的明白，老师这里给大家做一个简化：对于继承关系的父子类来说，子类可以对父类的功能进行扩展，但不能改变父类中已经定义的功能。把这句话引申出来可以得出以下三点的内容：
·子类可以添加自己独有的方法（废话，不然定义子类干什么）
·子类重载父类方法时，方法的入参要比父类的入参更为宽松（接收更抽象的类），但返回值要比父类更严格（返回更具体的类）
·子类必须实现父类抽象方法，但不能覆盖父类中非抽象的正常业务逻辑
从上面的三点内容中我们可以看出，里式替换其实是为了我们的继承结构着想，用来约法三章来约束继承的泛滥。我们下面用一个例子来说明一个反模式：

```java
public abstract class Teacher( 
     public vroid saySomthing(){
				System．out．print1n（“我们的口号是”＋“同学们好”）； 

   }
}
／／正常老师
public class NormalTeacher extends Teacher [ 
        public void saySomthing(){
				System．out．print1n（“我们的口号是”＋“同学们好”）； 
   }
}
／／ 不正常老师
public class FengSaoTeacher extends Teacher [ 
		@Override
		public void saySomthing(){
		         System．out．print1n（“He11o慕课网的各位同学们大家好”）； 
   }
{

```


以上结构在实现功能上没有问题，但是违反了里式替换原则里的一点—子类必须实现父类抽象方法，但不能覆盖父类中非抽象的正常业务逻辑。更加合理的结构是这样的：

```java
public abstract class Teacher {

public void saySomthing(){
		    System．out．print1n（“我们的口号是”＋say（））； 
         }
         public abstract String say(); 
}
／／正常老师
public class NormalTeacher extends Teacher { 
@Override
public abstract String say(){ 
       return“同学们好”；
    } 
}
／／不正常老师
public class FengSaoTeacher extends Teacher{ 
			@Override
			public String say(){
			return“慕课网的同学们大家好”；
   }
}
```


从上面的例子中，似乎看出了前面某个原则的影子，那就是“开闭原则”，对扩展开放，对修改关闭，对父类行为的扩展，不仅可以通过声明一个新的类来做，也可以在方法级别声明这样一个扩展点。所以在架构领域，很多原则和准则都是相通的。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/820918f3-64c8-4dbb-9466-15b80eb2880d/1-4.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466URY56UPN%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230355Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGQQ2XACqSgtk6ZS9Vav%2ByZzM2I74wEl1LFEuX6qnjteAiAAmA6g41uswpo09rUKLZRynVOzZ4oCaedwlxlIdlgv7CqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMRtEnJyFtyEU4pMkCKtwD8%2FpSrNGHnQvhqqPJlXSHsmu1sG4frxD3rPG%2FgmTcK01RK9%2B0El2faQTf9fE%2B5YBVzCFD%2FXdf660eXN%2B9DjmIa4gZ5Alg9v%2BJNfvVd9e8JdB%2F20uBuD9mtT13gdQaUUGXeAOsjO2F4ldaxWYgv1tnd6xUeGTeanpaUpyhUn8tVDCnHTRdbJl%2B6Lzc4yrAeqKiTPA911AovkNkTcGZoQioxUW37PrCJ74E50g1ZT0drBCh2xIfeIp%2FHIZ4ZfXgARBIo8cJA8xq%2FQQWv37fP%2BGR8GIP400WNcDtO9pDBh15k2ZC9ZcwgP%2FNjbQLiHuNayvZ36u%2FOPlsqf6XRjdhV427Jt8fEGxAdUQfmfbnEojE7%2FxqKS6hN8l%2FrqC0O9ppwDBJsLt4kMx05jCIJDTLtZuX5Bydx0I50otfaPtSR9D42OE68Ed8xlEhFiURN2yPKJ51cx31QdCJ46fHD0hw4ufgH%2FkoLf%2BNYnnYg%2FceIg2QzgJKZK7nZHxpY5ATWWnJgH4%2BgdddVV7TV874s5%2F7LuapAacoHhsnKHiJEFTazpSH707Q0QQGCsMZfKUpOCNIeBd30TL2P9AVF04tlWnePBI6qyNr34BgFV8C6Vpf81x57wxJtmHrHdwnF8nqFqIwzbf%2F0gY6pgHc1FaMxSvTW347qoF3ldlHuMXhj4SAK95loQelPq%2FwV2L8D%2BmRPyR9sGGV5iLkI%2BG63%2BRU4O%2Fevu2RBuwkEmz%2FZBlm7UW8ecQ5HIEqvS%2FyvYmJ8oAHSBgmVBaris%2Fvru%2Fyh588JghBxT%2BnX30eszs1oPHqgvIouaoGkhFD%2F1UEfOGgylbH33M2L2nPFES6HEhzOTWA64KlI8rXzl0PzioT5sMjLZ1e&X-Amz-Signature=7c5afd55e661d0a8c00b626a71888cdd6346c808464502a6fe0d5ceb9fce101f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



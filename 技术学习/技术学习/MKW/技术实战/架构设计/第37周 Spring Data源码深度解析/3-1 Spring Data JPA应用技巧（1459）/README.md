---
title: 3-1 Spring Data JPA应用技巧（1459）
---

# 3-1 Spring Data JPA应用技巧（1459）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b2f5b472-f6e0-45c1-9e9b-41d59562a1c2/SCR-20240921-cgah.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466342NYKVF%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232142Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDOLbGpAP4%2FXRH%2BH%2F3vr%2FJ3NlEzySJ%2Br07D70IwVIPnaAIhAPYh0fNAAerdxOQDXxGqhv%2BRsmA93hrlGx3xZZY8Y%2FYbKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwfkk9SfqQOV%2Bpfjysq3AMvK78%2Fp7sPA9DgIHPaz2zxwXF03ddY7XUorlPdkfl7OSGDfe0boymM5DctrPZqXfXVIhF5z%2FE8GYUvyvO0tPegObu0Cd70hlWHhtua%2B17RkO3pYIb%2FtDipkm6VcICV%2BhtAwOsp7fIltXKi9ZQtiFy8tClbJ8PfP7LRXc91up7QM%2BVPRFx%2BDEIPGnwnCwp5K3o0lpHPL30IwZozFjbeG%2F1V3I5o9LqqHvRQpvTYHqHj9Cv3VsDtg5KKVFE9%2BdQCF46lrRlygT84AUsM7NyR3OC6Lk8VeaCOszn%2FVV%2FnMCQOU5zTm70S17vf3fA71lwFBoxbFPm%2FeGc6VpUuZZGbRqNHBgiTjoL12g62n4MMcnnV6rkgTuHY5YdlWSuEQt7r%2FaYSe%2BFX%2FCtvlgXUsvjwFo9WDXb2NgsHW1vO1frx4qeeyWMCW9Q0bRYL39sTkniwJWIKRtQz2pBygYQ0hmtrCDMCtgYvCuObLMZ%2FwcKrMBQJsUVw23Udxm2SYzViBmMGuzJ82agPNADb1TV8tt8fr0fhU%2F52N4fv7c7Fw1Nux9kSCZO89az0nW7%2B4ZOUxKx8iq1FdhQjuMTpBknWoBvey%2BehTqNKehYGaRPWDdVcPUG7zcoWV86Cpak9OgFmzzCOuP%2FSBjqkAfEDHP%2BBuZoopIUVl8sDX7xQHAc9VP83ku9VZ%2BJ9wOFEboKp6%2BRxOBs4TPWE%2FCgGfYjfijFyz%2BTPvAjHs%2FmKWmkjeua0mhWKWboli4nRCv2KeBQRJC16ZSwtlRJnxv%2B6ychdEfB82T7prm%2F5aGCSQ%2FvBljs%2FDsKLFtIeSRbgm54AMccSjjqtApkPwaaEIeMz%2BuRtbav9wseJT%2F0E1bYbGhDeuDbl&X-Amz-Signature=39851635a69d21c30d06de13aaad22c606d4f1ce12f3b071f2082f565bf3f651&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/8590c8db-4ee9-4c72-9fc6-6d35fc7dd2eb/SCR-20240921-bxvd.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466342NYKVF%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232142Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDOLbGpAP4%2FXRH%2BH%2F3vr%2FJ3NlEzySJ%2Br07D70IwVIPnaAIhAPYh0fNAAerdxOQDXxGqhv%2BRsmA93hrlGx3xZZY8Y%2FYbKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwfkk9SfqQOV%2Bpfjysq3AMvK78%2Fp7sPA9DgIHPaz2zxwXF03ddY7XUorlPdkfl7OSGDfe0boymM5DctrPZqXfXVIhF5z%2FE8GYUvyvO0tPegObu0Cd70hlWHhtua%2B17RkO3pYIb%2FtDipkm6VcICV%2BhtAwOsp7fIltXKi9ZQtiFy8tClbJ8PfP7LRXc91up7QM%2BVPRFx%2BDEIPGnwnCwp5K3o0lpHPL30IwZozFjbeG%2F1V3I5o9LqqHvRQpvTYHqHj9Cv3VsDtg5KKVFE9%2BdQCF46lrRlygT84AUsM7NyR3OC6Lk8VeaCOszn%2FVV%2FnMCQOU5zTm70S17vf3fA71lwFBoxbFPm%2FeGc6VpUuZZGbRqNHBgiTjoL12g62n4MMcnnV6rkgTuHY5YdlWSuEQt7r%2FaYSe%2BFX%2FCtvlgXUsvjwFo9WDXb2NgsHW1vO1frx4qeeyWMCW9Q0bRYL39sTkniwJWIKRtQz2pBygYQ0hmtrCDMCtgYvCuObLMZ%2FwcKrMBQJsUVw23Udxm2SYzViBmMGuzJ82agPNADb1TV8tt8fr0fhU%2F52N4fv7c7Fw1Nux9kSCZO89az0nW7%2B4ZOUxKx8iq1FdhQjuMTpBknWoBvey%2BehTqNKehYGaRPWDdVcPUG7zcoWV86Cpak9OgFmzzCOuP%2FSBjqkAfEDHP%2BBuZoopIUVl8sDX7xQHAc9VP83ku9VZ%2BJ9wOFEboKp6%2BRxOBs4TPWE%2FCgGfYjfijFyz%2BTPvAjHs%2FmKWmkjeua0mhWKWboli4nRCv2KeBQRJC16ZSwtlRJnxv%2B6ychdEfB82T7prm%2F5aGCSQ%2FvBljs%2FDsKLFtIeSRbgm54AMccSjjqtApkPwaaEIeMz%2BuRtbav9wseJT%2F0E1bYbGhDeuDbl&X-Amz-Signature=35167f165bf689783aff71963d3726be86ee74dc9afc11b6737b2508cc9d8f3e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

同学们大家好，这一章节我们来介绍 spring day 的 JPA 的应用技巧解析，那么关于 spring day 的 JPA 呢？它的应用的技巧很多，我们这里面抓住主要的我们基于查询的方式来去介绍。那么对于查询，我们介绍两方面，一个是基于方法名的查询，比如说我们这里面的 find by name，另一种是基于我们的注解查询，也就是我们通过 at query 的方式让我们进行对应的查询。当然这个 add query 这个注解，它不仅可以执行查询方法，它也可以执行类似于update， delete 这样的一些写超出的方法。


那么首先我们来看一下方法名查询，那么对于方法名查询，我们在程序里面跟大家有演示，对于比如说 find by name，那么我们 name 作为我们的参数，它就会生成对应的词或语句。我们同时也可以比如说你们 find by States，那么如果说 States 是我们对应的一个属性，它也可以生成我们正常的查询，我们可以看到通过我们的查询方法名查询，它通常是一些简单的查询，我们可以针对具体的某一个条件，当然其实它是可以针对多个条件的，因为涉及到多个条件的话，我们可以通过 find by name in 的 states 或者说是类似于我们年龄，我们可以通过 between 这样的方式。


句子项具体它支持哪一些关键字和一些查询的方式，我们来接着看一下这个里面我们可以看到对于一些关键字的keyword，我们比如这里面的是方法命名查询的一个例子，这里面是对应的这个查询的方法命名会生成一个g， p q r 语句的一个片段，大概是怎样的？首先我们可以看到这里面是 distinct 的，那么如果说我们要查找唯一的内容的话，我们可以通过 find distinct by last name and fast name。当然我们可以想象到 last name 和 fast name 是我们当前这个 being 的一个属性，这样的话我们可以看到它是通过两个查询条件，同时它还支持 distinct 进行一个防重复的过滤，那么对应生成的错口语句就是 select distinct 对应的属性。


这里面第二个关键词 end end 我们看在上个查询语句我们就已经包含进来了，所以说这里面我们可以看到它就是生成对应的查询语句，也就是我们 where 对应的查询条件一和查询条件 2 的一个组合，这个我们就不用过多介绍。那第三个是all，其实对于我们在做 SQL 查询的过程中， all 这种条件用的比较少，因为通常 on 的话，它涉及的处理的过程会比较复杂，比如说我们这里面对于 find by， last name， first name 这是什么呢？通常是我们在做一些模糊查询的时候，我们可能会引起 all 的操作，比如说我们只知道这个名称的关键字，但是我并不确定它是在 last name 还是 fast name，那么所以说我们可能也就可能会用到 all 的操作，那么这里面生成的 d p q r 语句的片段，也就是where。我们比如说对应的 x last name 指定了第一个我们的参数， how 我们的 first name 的第二个参数，那么这样的话就构成一个 all 的一个语句。


那么还有是什么呢？像 east 和equals。对于 east 和 equals 我们就不用过多介绍了，我感觉这个 east 和 equals 只是 spring 的JPA，它为了提供一种更像的标志性内容。当我们普通的 find by fast name， find by name，或者说是 find by name is 翻篇的equals，它是等价的，我们可以看到这里面，对于这里面翻的 by fastname IS 和 ECO 字，它存在不存在这个 IS 和 ECO 关键字它的效果是一样的，所以说我们还是建议大家用简洁一些，尽量的就不用去添加这个 IS 和 ECO 了。


那么这里面的 between 其实是比较有意思的，对于我们在使用一些范围查询的时候，基于范围查询之间的我们使用劈顿还是挺好。这里面向我们 find by start date 就是一个开始时间，我们笔衬在哪个时间区间，这样使用起来要比我们大于某个时间，小于某个时间，使用起来会更简洁一些。


下面我们可以看到是有listen， listen 下面还有 grid than equal，那么在这里面的话，这个 equal 就是可以包含进来了，为什么呢？因为像 list than 我们小于，那么 list than equal 呢？就是小于等于，所以说对于 IS 和 ECO 它在这里面其实没有太多用处，那么在我们这里 design ECO 是它就有它对应的作用了，所以说我们也需要去了解这个 ECO 意思它的存在的价值。


下面是我们的 Grid run 的一口，也就是说它对于大于等于的这种情况后面还有 OFT 和before，那么我们可以看到对于 find by start date OFT，那么 OFT 我们也去标明 OFT 是之后就是时间上是大于的， before 是之前时间是小于的，这里面我们可以看到并没有提出 of 的 equals 这样等等的一些操作。


下面我们可以看到还涉及到了像 its now 和null，那么对于这个我们也跟对应的 circle 语句也有对应的关系，比如说像 where is null 这个null，也就是说这个属性的不存在。比如说 is 通常是我们是一个int，我们通常是 0 到一定的一个年龄的一个范围，那么如果我们的 is 它并没有设置，那么它就是对应的null。


下面还有对应的 its not not， its not 和 is not，它其实就是一个相反相逆的一个过程，后面是like，那么因为我们知道在查询 SQL 的过程中，我们也是支持 like 的，那么这里面也是有对应 like 的关键字，比如我们 find by name 对应的是like，默认的话我们不加like，它是一个等于或者是 find by name 的equals。这里面的 Nike 和 ECO 做一个对应 equals 相等。 like 我们通过通配符的一个匹配，这里面还有对应的 not like，其实处理过程是一致的。这里面需要注意的，我们在 socker 查询的时候，我们的通配符通常是一个百分号，那么对于这个百分号的话，这个是需要我们在组装关键字的时候手工组装百分号，否则的话它其实起不到这个 like 查询的效果。


下面还有我们的是 starling weights，或者说是我们这里面是 found by fast name starts，其实这个 storing weights 跟我们的 like 关键字很类似，我们知道对于我们，通常的我们的缩影是通过左匹配的，那么左匹配对于 storing weights，它刚好属于左侧，那么这样的话它也可以使用到对应的缩音，对应的 in the 谓词也是对应的一个like，但是它是属于一个又匹配。那么对于这种情况下，它是使用不到 show in 的。通常我们很少使用 Indian 谓词这样的一个长音条语音的操作。


接下来我们来看一下这里面是包含的一个 one continuing，也就是说我们看一下当前的内容是否包含进来。这里面的包含并不是我们在查询 SQL 的时候用 in 指定一个集合，这里面包含也是一个针对单属性的查找，我们可以看到这里面会有一个解释，比如说我们看到对应的我们的 fast name 是like，那么 like 是指什么呢？对于我们这个关键字，之前和之后都有对应的通配符，也就是一个全匹配，那么这种匹配的效率是非常低的。当然这种 continuing 如果说我们在做全文检索的话，可能这种用途会更好一些，通常我们在进行 SQL 查询的时候，用到 continuing 的操作也比较少。


后面就是我们比较常见的我们看 order by，对于我们查询的过程中基于一个排序的标记，这里面是很重要的。对于 order by 我们可以看到对于这个 find by， its order by name 这里面还有一个DESC，那么涉及到 order by 通常会需要指定我们 order by 的属性，并且它是 ASC 还是DS，也就是正序还是倒序的这样一个查询的操作。
下面还是not，比如说我们 find by last name not 这个 not 也就是我们对应的一个不等于的一个操作，这里面是in，这个 in 我们使用的会比较多一些，我们 find by ADS in 几个指定的一个集合区间，通常我们认为这种 in 查询，它会使用到我们对应的索引，效率还是可以的。下面是 not in 的是一个对应关系，当然 not in 它这种使用场景也不是太多。


下面是我们的又是 find by activity true，对于这种情况，我们可以看到它是针对一些特定的属性才能用到这种方式查询。我们可以拿对应生成的 SQL 语句是 where activity 等于true，也就是是否激活我们是 true 或false，那么这种情况下我们可以进行 true 和 false 的这样一个操作，可以减少一个我们传入的参数。比如说我们通常会在做一些逻辑删除，我们标记为deleted，那么对于 DELETE 的这种操作，它是个布尔类型，我们就可以去这样用标准。比如说我们 find by user deleted 等于 true 这种应用效果，这是 ignore case，也就是说我们忽略大小写，那么这种情况其实对于我们通常的数据库查找效率也是比较低的，它会对我们这些操作进行一个相同的一个大小写的转换，我们统一把我们的直段和我们的参数都转回大写，再进行一个比较。


我们这样去想，如果说大家都涉及到了我们一个函数的计算，这里面即便 fast name 它是支持索引的，那么这种情况下它的索引也不会用到。现在我们知道在 Sprint GPT 里面，我们通过方法名查询它支持的一些关键字，可以给我们带来一些组合，对于这个我们还是比较容易理解的。


我们在前面的课程也介绍到，我们对于像 user repository，它继承了我们的 DP report，它这里面是 find by name，我们也可以 find by states，当然这里面的一些属性都可以支持我们通过这种方式去查询，那么关于命名查询的话，我也就是我们的方法名查询的内容我们就先介绍到这里，那么接下来我们来看一下我们基于注解查询的一个实现情况。


那么对于注解查询的话，它的实现也比较简单，通常就是我们对于方法名称，也就是方法名称里面，我们通过 x query 进行我们查询语句的写法，那么我们注意一下这里面的查询语句，它并不是我们的 native SQL，也就是并不是本地SQL。这里面我们是用的是 j p Q 2 语句，它跟对应的Hypernet，对应的 s Q 2 语句是有点类似，我们可以看到这里面我们 select u e from 我们的user，我们并不是表名，这里面是指定的对象名，这里面是我们对应的 user 的这个集合。同时我们支持一个别名儿，那么对于别名儿，下面我们支持的 user log name，那么所有的操作都是我们对于对象的一个查找，它的查询条件也是基于对象属性的一个查找。这里面我们对于一些变量的输入，参数的输入，我们通过问号作为我们的障碍符，标记它的对应的索引。通常我们如果说是需要一个参数的话，我们就是问号一，那么如果多个参数的话，就问号 1234 作为一个索引号去表达起来。


下面我们可以看到这里面是两个参数，我们是怎么去处理的，当然我们虽然是 add query，但是我们要去想清楚，它其实是一个对应我们 SQL 的操作语句，它不一定只是查询，它同时也支持修改。如果说涉及到修改的话，我们这里面是一个修改操作，对于修改操作的话，我们是需要通过 add modifying 这样一个注解进行修饰，我们基于这个注解，它会感知到我们这个 circle 语句，它是一个修改操作，那么通常修改会涉及到一些事物之间的逻辑的处理的话，我们可以通过它进行提前的一些与处理好。


这是我们可以看到的一些注解查询的query，那么我们来切到程序里面，我们看这里面是列出了我们两个基于 add query 注解的方式定义的查询语句，那么其实在执行的过程中，我们对于不管是我们的方法名查询，还是艾特 query 查询，他们得到的效果其实很类似的，他们对应的都是一个 query 方法， query 方法进行相应的一些操作，同时我们也写了对应这两个基于 query 方法的它的一些单元测试。我们来这里面看一下，又是 reports query test，那么对于我们这里面的是 find by login name 和我们这里面是基于 query 查询语句的一个修改方法， update 和 describe person，也就是我们修改一下它的描述的这个字段信息，这里面我们可以简单执行，我们看一下执行的效果。


好，现在执行完成，我们可以看一下这里面会生成对应的 circle 语句，其实这里面 SQL 语句的内容同时也有我们在打印输出这个 user 它的一些属性信息，整个生成这个搜口语句是基于 harbneter 的规范，我们可以看到对应的是 from 我们的 tea user，这次对应的 user 别名生成我们沃尔一个 user 别名对应的 login name 它的这样的一个参数的情况。下面我们来看一下对应的这是我们的修改操作，我们执行修改操作，看一下执行的效果。


通常我们在执行修改的过程中，我们这里面是首先需要把这个对象读取出来，我们对它进行一个修改，那我们可以看一下这里面。首先第一步我们需要把我们整个这个 user 对象读取出来以后，我们再对它进行修改，这里面生成的我们的搜索语句比较简单，我们可以看到对应词 update key， user set 我们的description，我们这个描述信息是什么，并且指定我们的 word 参数是什么。这两个 circle 语句都是对应 Hypernet 的方式去打印出来的，通过这样去看的话，我们如果说对于命名的这些我们的方法名称的查询，如果不能满足我们的要求，那么我们可以通过对应的 GPQL 语句去实现我们的这些正常改查操作，也是非常方便的。


这跟我们对应的mybadcase，它提供的这个 query 注解其实是很类似的，只是我们写的 SQL 的语法是有一些区别，对应的 GPQR 语句或者 SQR 语句，它是对于我们一个对象的一个查找，那么 Hypernet 它的 query 它可以理解为我们原生的词口语句，那么好对于我们这里面是 spring day 的 GPT 它的这些应用技巧，我们就先介绍这一些。


其实 spring day 的 GPT 它的一些应用技巧是非常多的，并不仅仅是一个通过两种方式的一个查询，如果大家想去自己去了解更多的这些 spring day 的 JP 的一些功能，我们可以在这里面，我们可以看到这里面是对应的我们 spring day 的JP，它的一个官方的文档，我们可以看这里面是列了很多内容，我们可以在这里面去针对自己感兴趣的内容去认真的去阅读它对应的路径，我们可以看到是对应的是 spring day 的 JPAD doc。我们可以在 spring 官网的链接里面进行切入，引入过来我们可以看到这里面列的这些我们的核心的一些概念，我们的一些 query 方法等等。我们定义我们 query 的 interface 各个章节的内容，其实写的内容还是挺细致的。 Sprint GPT 的应用技巧我们就先介绍到这里，同学们，我们下一章节再见。



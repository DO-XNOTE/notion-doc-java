---
title: 2-8 落地Nacos服务发现 - 搭建服务消费者进行服务发现
---

# 2-8 落地Nacos服务发现 - 搭建服务消费者进行服务发现

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/26540b4f-8494-438c-a601-66d75ad5ea43/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662AEAW2IP%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGIyBchkhWbjf%2B4pDgeWoCzM8Yy5wXi9pwAsVrZaRE4YAiEA%2F0FBXCmaXtPGaKvOV6stv%2F5e6meb%2FzR1b7g%2Bqw5PHhUqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGf6kE5i0gdF3f8NJircA4ZGhidl4bQxbx4BAEHMhSZZhvBKSd2jkGXePQt6iJ97uT80Kx3r%2FPvvglIpRnzamjE39LDh7dChJaTwToL6EMEh4G0KYRBqYasHGoGsX7KfrIlsh4XhBJklW5ZPI4tAki9jXT3AApf3xwOrSMchnISBB3ExUSdbl0ldnZaHnRWjGUFVUIqJw4UDhuVFPcCxSfZVKu9IHIOFduy6dq7V1gJyOzvbbAs5FeHDfh8%2BeP3U2vs%2BPxI2f5Ezq4HHIXTYtyPVsMYtrJ95myt9bS7m1Xp6cDiEg8jyfibcBd7mGwtKNSPZBj7FWyjbF5EPlOVAOrBXt6lC28lb6m57ezg17s2pF6H6BObUW%2B7uzzQmurwrocvwN%2FPsdZkK3UjyEzEyenyk9tg2tD4QwMm%2BkCZRpCZOLoCfoLTrHx1QB7zQHtQAdVtfgQnLCxIuF99Ex4VYAqrk%2BK5Z0Kk7K2woDg%2B3qxcHMrzFUSa8dDyVxQ0ehtqNKSIr8qxdbd%2Bylhkxw4I9ZmH7yx9HvFCVMDGHgmorGwi2h%2BttkluwTKEt51MxrkG8gXjaaNVrhhJA%2BRy2b64aEX7S9fnFdBzm%2BDdmygEGsAPii8EBpfXrMiIwcGnmUmQjGd9x6QCor5ghNXslMPK3%2F9IGOqUBiv94agjdOpLQn0xQic%2FTEE2iSqdmyL43Y5xvOziBlpcTl6rOL27E09dZvgHvI72xGnC%2F0oNXzTXAzue2yLUksFoA%2B3tvTtuwgdIWccNLkaJi%2FTiWqyYVkw5GGO5Iyqq2tTfZ5ni%2BgLgldFcaFLLlOraR0qOz8QpmKw38ePktQED7HQedGAW5r0nSjOIkWa63mmuk5bxyEn%2BVlF%2FBSktSBJd%2B0wjE&X-Amz-Signature=ec09b626f2d1dc7293901aaa01e21787de275003a070c26e0d0fc07a60698190&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/0c691ec0-5d37-48eb-afe7-5dbdc4c516bb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662AEAW2IP%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGIyBchkhWbjf%2B4pDgeWoCzM8Yy5wXi9pwAsVrZaRE4YAiEA%2F0FBXCmaXtPGaKvOV6stv%2F5e6meb%2FzR1b7g%2Bqw5PHhUqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGf6kE5i0gdF3f8NJircA4ZGhidl4bQxbx4BAEHMhSZZhvBKSd2jkGXePQt6iJ97uT80Kx3r%2FPvvglIpRnzamjE39LDh7dChJaTwToL6EMEh4G0KYRBqYasHGoGsX7KfrIlsh4XhBJklW5ZPI4tAki9jXT3AApf3xwOrSMchnISBB3ExUSdbl0ldnZaHnRWjGUFVUIqJw4UDhuVFPcCxSfZVKu9IHIOFduy6dq7V1gJyOzvbbAs5FeHDfh8%2BeP3U2vs%2BPxI2f5Ezq4HHIXTYtyPVsMYtrJ95myt9bS7m1Xp6cDiEg8jyfibcBd7mGwtKNSPZBj7FWyjbF5EPlOVAOrBXt6lC28lb6m57ezg17s2pF6H6BObUW%2B7uzzQmurwrocvwN%2FPsdZkK3UjyEzEyenyk9tg2tD4QwMm%2BkCZRpCZOLoCfoLTrHx1QB7zQHtQAdVtfgQnLCxIuF99Ex4VYAqrk%2BK5Z0Kk7K2woDg%2B3qxcHMrzFUSa8dDyVxQ0ehtqNKSIr8qxdbd%2Bylhkxw4I9ZmH7yx9HvFCVMDGHgmorGwi2h%2BttkluwTKEt51MxrkG8gXjaaNVrhhJA%2BRy2b64aEX7S9fnFdBzm%2BDdmygEGsAPii8EBpfXrMiIwcGnmUmQjGd9x6QCor5ghNXslMPK3%2F9IGOqUBiv94agjdOpLQn0xQic%2FTEE2iSqdmyL43Y5xvOziBlpcTl6rOL27E09dZvgHvI72xGnC%2F0oNXzTXAzue2yLUksFoA%2B3tvTtuwgdIWccNLkaJi%2FTiWqyYVkw5GGO5Iyqq2tTfZ5ni%2BgLgldFcaFLLlOraR0qOz8QpmKw38ePktQED7HQedGAW5r0nSjOIkWa63mmuk5bxyEn%2BVlF%2FBSktSBJd%2B0wjE&X-Amz-Signature=66c61ce74134d016cbdf5de81d7223ef8d70bb393e2fe1ffb982d01be793bb80&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/9602d58f-76fb-4e00-ac8b-a02613162aff/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662AEAW2IP%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGIyBchkhWbjf%2B4pDgeWoCzM8Yy5wXi9pwAsVrZaRE4YAiEA%2F0FBXCmaXtPGaKvOV6stv%2F5e6meb%2FzR1b7g%2Bqw5PHhUqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGf6kE5i0gdF3f8NJircA4ZGhidl4bQxbx4BAEHMhSZZhvBKSd2jkGXePQt6iJ97uT80Kx3r%2FPvvglIpRnzamjE39LDh7dChJaTwToL6EMEh4G0KYRBqYasHGoGsX7KfrIlsh4XhBJklW5ZPI4tAki9jXT3AApf3xwOrSMchnISBB3ExUSdbl0ldnZaHnRWjGUFVUIqJw4UDhuVFPcCxSfZVKu9IHIOFduy6dq7V1gJyOzvbbAs5FeHDfh8%2BeP3U2vs%2BPxI2f5Ezq4HHIXTYtyPVsMYtrJ95myt9bS7m1Xp6cDiEg8jyfibcBd7mGwtKNSPZBj7FWyjbF5EPlOVAOrBXt6lC28lb6m57ezg17s2pF6H6BObUW%2B7uzzQmurwrocvwN%2FPsdZkK3UjyEzEyenyk9tg2tD4QwMm%2BkCZRpCZOLoCfoLTrHx1QB7zQHtQAdVtfgQnLCxIuF99Ex4VYAqrk%2BK5Z0Kk7K2woDg%2B3qxcHMrzFUSa8dDyVxQ0ehtqNKSIr8qxdbd%2Bylhkxw4I9ZmH7yx9HvFCVMDGHgmorGwi2h%2BttkluwTKEt51MxrkG8gXjaaNVrhhJA%2BRy2b64aEX7S9fnFdBzm%2BDdmygEGsAPii8EBpfXrMiIwcGnmUmQjGd9x6QCor5ghNXslMPK3%2F9IGOqUBiv94agjdOpLQn0xQic%2FTEE2iSqdmyL43Y5xvOziBlpcTl6rOL27E09dZvgHvI72xGnC%2F0oNXzTXAzue2yLUksFoA%2B3tvTtuwgdIWccNLkaJi%2FTiWqyYVkw5GGO5Iyqq2tTfZ5ni%2BgLgldFcaFLLlOraR0qOz8QpmKw38ePktQED7HQedGAW5r0nSjOIkWa63mmuk5bxyEn%2BVlF%2FBSktSBJd%2B0wjE&X-Amz-Signature=f6dc23b0992f510b5de309dd81684888d5bc37a2ec652a9547041e056863b475&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

hello，幕后网的各位同学们，大家好，我是姚曼仙。咱们这一节继续来看 Nacos 的落地案例。我们将要搭建一个 employee service 做服务注册，同时向咱前面搭建的 restroom service 发起一个真实的服务调用。那为了简化流程，我这里已经在 intelligent 里面把这些项目给它创建出来了。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/08c92b31-2259-40ec-8293-07bc51c715b4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662AEAW2IP%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGIyBchkhWbjf%2B4pDgeWoCzM8Yy5wXi9pwAsVrZaRE4YAiEA%2F0FBXCmaXtPGaKvOV6stv%2F5e6meb%2FzR1b7g%2Bqw5PHhUqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGf6kE5i0gdF3f8NJircA4ZGhidl4bQxbx4BAEHMhSZZhvBKSd2jkGXePQt6iJ97uT80Kx3r%2FPvvglIpRnzamjE39LDh7dChJaTwToL6EMEh4G0KYRBqYasHGoGsX7KfrIlsh4XhBJklW5ZPI4tAki9jXT3AApf3xwOrSMchnISBB3ExUSdbl0ldnZaHnRWjGUFVUIqJw4UDhuVFPcCxSfZVKu9IHIOFduy6dq7V1gJyOzvbbAs5FeHDfh8%2BeP3U2vs%2BPxI2f5Ezq4HHIXTYtyPVsMYtrJ95myt9bS7m1Xp6cDiEg8jyfibcBd7mGwtKNSPZBj7FWyjbF5EPlOVAOrBXt6lC28lb6m57ezg17s2pF6H6BObUW%2B7uzzQmurwrocvwN%2FPsdZkK3UjyEzEyenyk9tg2tD4QwMm%2BkCZRpCZOLoCfoLTrHx1QB7zQHtQAdVtfgQnLCxIuF99Ex4VYAqrk%2BK5Z0Kk7K2woDg%2B3qxcHMrzFUSa8dDyVxQ0ehtqNKSIr8qxdbd%2Bylhkxw4I9ZmH7yx9HvFCVMDGHgmorGwi2h%2BttkluwTKEt51MxrkG8gXjaaNVrhhJA%2BRy2b64aEX7S9fnFdBzm%2BDdmygEGsAPii8EBpfXrMiIwcGnmUmQjGd9x6QCor5ghNXslMPK3%2F9IGOqUBiv94agjdOpLQn0xQic%2FTEE2iSqdmyL43Y5xvOziBlpcTl6rOL27E09dZvgHvI72xGnC%2F0oNXzTXAzue2yLUksFoA%2B3tvTtuwgdIWccNLkaJi%2FTiWqyYVkw5GGO5Iyqq2tTfZ5ni%2BgLgldFcaFLLlOraR0qOz8QpmKw38ePktQED7HQedGAW5r0nSjOIkWa63mmuk5bxyEn%2BVlF%2FBSktSBJd%2B0wjE&X-Amz-Signature=34c8f518413f8a5e3caeeef9b7cd804bf2b75bcc217cf327bb5fd67a9fb9c689&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那咱接下来要创建的这个服务叫做 employees service，同样它这里也有三个子项目，分别是 employee API，还有 do 层以及 service call。那么我们首先先来去写这个 employee API 这一层，那我们在这里已经创建了对应的包路径。


那接下来咱第一个要创建的类是我们的员工活动记录这个类，我们把它叫做 employee activity，那创建出来，在上面扣上一个 data 注解，那接下来我们来定义它的属性，同学们看都有哪些属性？第一，第一个 ID 是不能少， ID 完了之后，我当前是哪个员工做了什么事，咱要把这个员工的 ID employee ID 也给记录下来。


那第三个属性我要去记录一个什么呢？活动类型。那活动类型这里我希望把它去注册成一个什么呀？一个枚举类。那为了方便以后扩展，我这里把它定义成一个单独的枚举class，叫做 activity type。那这个枚举类目前来说只给他创建一个类型，就是叫 toilet break。那回到我们前面创建的 employee activity 这个类里面，我们在这边把这个属性声明出来，刚刚创建的 activity type 名称，属性名也叫同样的名字。


再往后，既然是员工记录，我记录了员工号，同时也要记录你去上厕所的这个厕所号。这个厕所号其实为了方便以后扩展的取名字我就不取成什么厕所 ID 了，不太好听，我把它取名叫什么呀？叫 resource ID，资源 ID 听起来就高大上了很多是不是？那再往后，我这里既然是记录员工的活动总，我要去记录这个活动的开始时间，对不啦？开始时间 start time 开始就要有一个结束，这叫有始有终。对应的一个 end time 结束时间以及一个什么呀。我这边给它记一个布尔值，叫active，也就是说你进入厕所之后，这条记录就是有效状态， active 就等于true，那你从厕所出来之后，对应的 end time 这里就会设置上一个值，那这条记录就相当于已经完成了历史使命，它就不是一个当前正在进行中的活动。


所以对应的 active 我们就会设置成false，那这个类创建出来之后，我们接下来去尝试定义一个具体的API，回到这个 employee API 这一层，咱去创建一个什么呀？创建一个interface，那这个 interface 我给它起名叫 i employee activity service OK，这个类我把它打算定义两个方法，第一个方法是去上厕所的，这个方法我给它起名叫 use toilet OK，那这里将要传入一个员工的ID，那为什么不传入厕所ID？我上厕所我肯定是当前哪个有坑位我就去哪个，所以我们在这里不用去指定厕所ID，它会去调用 restroom service 来去找到一个当前可用的坑位。


第二个方法 employee activity，这里我叫 restore toilet。OK，那这是相当于完成动作也传入一个 employee ID。那这两个 API 这里定义好了之后，我们接下来走到这个道层里面，我们已经把它相应的依赖项全部都给它加入了进来，同学们可以去来参考一下。那接下来我去到他的文件夹里面去先创建一个数据库访问的实体，这个实体和它前面已经创建好的这个叫什么呀？叫 employee entity 的对象非常相像，咱就直接把它 copy 过来做一些修改好了。

OK，那 copy 过来之后，首先把这个名称改成 employee activity， entity okay。改好之后，我们这里要给它多加几个注解，多扣几顶大帽子。 data 这里我首先要去给它添加的一个 entity 注解，这个不能忘。然后 table 注解，我指定你当前访问的数据库的名称是 employee activity，OK，然后再往后我们这里就去可以定义一些像 entity listeners。做一个什么呀？做一个auditing，一个审计工作。 entity listener okay，然后再往下继续走，我们这里要去定义一些 long book 的注解，一个 builder 注解，以及我要去定义它的构造器，有参构造器，还有无参构造器。定义完之后，我们对于这个 ID 要去参考前面创建好的 restroom Doc 里面的定义，直接把它给 copy 过来，不用一行打了，咱程序员能偷懒就偷懒，这里 copy 过来 ID 搞定了。


接下来这个 employee 可以定义这个 column 注解，同时在这上面去指定你的当前的属性名称，对应的你的数据库的列名，以及它是否可以允许为空。OK，那么如果你不定义，其实也没事，像这个 resource ID 我就不定义了，它默认就会去访问数据库当中的 resource ID 这一个列。那么这里同学们看有几个特殊的参数，我想去特殊照顾一下，比如说这个参数，你看它是一个枚举类，它怎么去对应成数据库当中的一列，怎么来办？同学们看 spring data，这里有一个神奇的注解，非常有用，叫什么呢？叫enumerated，名称非常的拗口，但是功能特别的强大，它这里有这样的一个参数，你看点进去看，它有一个 Enum type，指定了你想怎么样来保存这一个枚举对象。它这里提供了两个方法，分别是以当前枚举对象的名称，或者以当前枚举对象的序列号来把它翻译成对应的一个数据库的值。


那么我们这里选择什么呢？我们看选择它，那把当前的 Enum 当中的序列号作为一个参数保存到数据库当中，所以大家这里注意，你去定义这个枚举对象的时候，不要去改变它们之间的顺序，否则这里的数据库访问层会出现数据的错乱。那除了这个注解以外，我想来省事，你看这下面哪些可以来省事？ start time 开始时间，我不想每次开始的保存的时候给它指定一个时间，这时候可以怎么办？诶，我们可以使用这个注解 created date，这样一来我们的 display data g p a。就会在 save 这个类的时候，去对应的把当前的时间戳塞到这个字段上来。那你看，都是偷懒的小技巧。


那我们这个类创建好之后，接下来怎么办？对应的要去创建它的 Doc do 层 d a o。这里我同样的也去创建一个 interface 接口层，给它起名叫EMPLOY， tivity d a o。好，那这个类要去继承一个标准的 spring data g p a。

的类，它的名称叫 g p a g p a repostery，那我这里给它指定一个泛型，指定我当前的数据库的实体对象是谁，是它，以及对应的这个主键是一个launch。那接下来又可以愉快地写 SQL 了。当前的这个 SQL 暂时没有同学们虚晃大家一墙，我这里不用定义SQL。那好，那我们这个 do 层定义完之后，接下来去移步到最下面的这个 employee service call，在这里面去写业务逻辑层。那这个子的 module 里面，我们也已经把对应的依赖项全部都加入了进来，它这里把 employee API 以及 restroom API 同时引入了进来。


为什么也需要 restroom API？因为我要真实的发起一个调用，调用 restroom service，所以我需要去获取到它的公共的访问的类，那接下来还是像 spring boot 的一些标准注解，以及 Neques 的服务发现注解，那这部分都已经配置妥当之后，我们就可以去写对应的业务方法。


我创建一个services，给它起名叫做 employee activity，这个 activity 我就不写了，直接写 employee service，能省则省。这 employee service 我要去实现一个接口，同学们一看就知道接口是咱前面创建的 employee activity service，那自然我实现你就要去帮你把这个对应的每个方法给它，把业务逻辑添加上。在添加之前，我们先去声明一个 SL for g，那日志组件OK，在接下来去添加一个 rest controller 的注解，表示当前的服务通过 HTTP 对外提供一个 rest 访问的方式，以及我要给他定一个 request mapping，一个访问路径也叫employee。


好了，最简单。好，那这三个定义完之后，我们这里再去写业务代码之前我要做一个操作，那就是做几个注入，第一个注入，我要把 employee activity do 层给它添加进来，这是第一个注入。第二个注入这里有点意思。第二个注意，我要去注入一个这个类，同学们看是什么呀？ rest the template，它就是咱 spring 的框架定义的一个统一的 HTTP 请求发送的一个组件，我们这里只是把它 autowire 进来，但是我还没有去声明它，咱待会呢再去声明，先写业务逻辑，第一个业务逻辑我现在怎么样要去使用你的蹲坑？那这种情况下我传入了一个 employee ID，我首先不是要先去确认你有没有蹲坑，我首先是要确认你当前这个员工是否已经在蹲坑里了。那如果他已经在了话，我就不想让他脚踏两只船再去上一个蹲坑。这时候怎么办？我们就要杀个回马枪，回到咱前面的道层，这里创建一个访问方法。OK，这个访问方法它具体做什么事，它就去简单地查询你当前用户是否已经在某个坑位上。同学们，看 spring data g p a 这里应该怎么来做？那我查询你是否在坑位上，实际上它就是一个 Cant 操作。同学们， count 操作，返回一个 Int 值，怎么来count？我们这里打上 count by 谁？ by 第一个 employee ID 你不能少。


第二个你的 activity type 也不能少。因为咱是上厕所，所以你要选择对应的 activity type。这两个选择之后，我还要去查询一个什么呀？ active 如果你当前的这个员工的出勤记录是active，那说明你已经在厕所里了。那如果它这个返回的数量大于0，说明你在厕所里已经蹲着了。那么接下来去定义它的访问参数。


第一个 employee ID 写上去，那第二个是什么呀？第二个是咱们前面定义的枚举类 activity type，我给它起名也叫 activity type。那第三个我们是谁？第三个是布尔值 active 当前是否还生效？active？好，那我们再回到前面创建的这个 service 当中。第一步， Int 做一个count，去查询谁去查询你当前用户是否已经在一个蹲坑里蹲着了？我把 employee ID 给它传入进去一个 activity type， activity type 的具体的属性，我传入 tool break 以及一个true。OK，那我接下来的业务逻辑怎么写？如果你的 count 大于0，那这种情况下怎么办？大于0。好，那这种情况下直接扔出异常。


好嘞， new runtime exception，同学，你已经在坑位当中了，你不能再占一个坑位了，但是你可以选择什么呀？选择这个动作快一点。好，那接下来往后走，这里我们要去发起一个远程调用。发起远程调用做什么？去查询你当前的洗手间还有没有空余的位置可供我调用的？这个远程调用，咱就要通过 rest template 发起。 rest template 用起来诶，非常的难用，同学们，不过不用担心，咱也就用这么几节。后面我们将用份组件来代替这种艰难辛苦的钓友。那我们使用 get 方式来发出一个 get 请求，他发的地址HTTP，我们注意英文符号哎，不要打成中文了。


叫 Restary room service。这是什么网址？这个就是你的服务名 restroom service 的服务名。因为我们是用的谁用了 Nequos 的服务发现机制，所以前面只用配置服务名，它能帮你自动寻址。接下来我配它的访问路径， toilet service 杠 check available。那同时我还要去指定当前这个方法它的返回值的类型，我们这里用一个数组来接这个访问结果。好了叫 toll 的数组，好给大家定义这种类型，那接下来我怎么来接它？也同样的使用这个套类数组？OK，那用一个属性把它给揭下来， toilets 等于它。好，那这里调用完了之后，咱们来一个判断，用这样一个工具类，同学们要在自己项目当中善用这些工具类，能帮你把代码做得更整洁一些。使用工具类，先来判断你当前的这个数组是否为空，那如果为空了怎么办？为空了我直接扔出异常。


好啦，那你这个大号上不成喽？上不成怎么办？同学们，看，上不成你也有解决方案哎。 sheet in 什么？这个是小便池的意思，接下来我下一个动作就是要什么呀？抢坑，你代码走到这一个位置就说明一定有坑位可供你选择了。那同样的，我抢坑这里也是通过这个 rest template 发起调用，但是这里不同的是，我要发送一个post，调用 post for object。OK，那它的地址我们从上面把它给复制下来，那它最终的这个路径是要调用这个服务的 occupy 方法，抢空方法。与此同时我要传入一个参数，这个参数怎么定义来？我们通过这种方式定义 rest template，定义这种传参非常的麻烦，我特别不喜欢用它，所以后面我要用 phone 组件来解决同学们这个远程调用问题。我们给它起名叫参数，就叫 arguments okay，然后声明一个 linked multi value map 好，生命完了之后，我们要把一个参数传入进去。


同学们，还记得咱这个 restroom service，它是接收哪个参数吗？接受一个ID，谁的 ID 呢？哎，你当前蹲坑的这个ID。好，我们就通过这种方式把它传入进来。然后我们也同样的要给它指定一个返回值，你占用坑位，返回值是当前坑位的这个对象，那我们使用一个变量属性把它给接收下来。接收下来以后，我们这里就要去怎么样，就要去保存，如测记录。



okay，怎么来保存呢？我们要先定义一个 employee activity entity 这个对象。好嘞，给它起一个名字叫 toilet break。然后怎么来定义？我们就借用 loombook 里面的 builder 方法使用非常简洁、高效、优雅的方式给它把这些属性定义下来，那首先定义 employee i e d，然后当前是active，也就是正在进行中的一项活动。再往下它的 activity type 是谁？是 Tolly break，我们把这个枚举定义下来，然后你对应的 resource ID 就是你前面获取到的可用 toilet 的ID，那还差什么属性？我这里应该没有属性，直接 build 好那里面的这个 creation time，同学们这个时间就由这个注解来把它自动生成了。


好，那我们回过去，那定义完了之后，我直接 save 就可以了，非常的简单。 employee active doll，把它给 save 出来。OK，那这里基本上就大功完成了。那接下来我们只要返回一个最终的对象，那这个对象它不是数据库实体，它是这个 employee activity，我们怎么来去返回这样一个对象？老师前面说过，还要教大家一个简单的方法，我们可以利用这个 bin utils，它做一个反射，然后把这些属性自动给它 copy 过去，调用它的 copy properties 方法，那这第一个参数是我想要模仿的对象。第二个参数是我将要把属性 copy 到的目标地址。好，我们把它 copy 完了之后，给这个方法加上一个路径，那这个路径我要把它写成同样的，也是 post 方法，叫做 Tolly break 好了，OK，那这里牵扯到一些数据库操作，我们还要去加上一个 transactional 这个标签。


其实同学们想我这个事务性，它其实会延伸到你调用的微服务，那么如果你微服务这里调用成功，比如抢坑成功，但是你后面失败，那怎么做回滚呢？诶，没法回滚，因为它都属于不同的服务器上部署的资源了，这种情况怎么办？不用担心，同学们，后面我们有专门专制这种分布式事务的专题，到那时候再跟同学们展示黑科技。


那接下来我们写第二个方法restore，释放当前坑位。那非常简单。第一步，我们使用这个 employee activity Doc，把它当前的这个 activity ID 给它拿出来。呦，发现这个名字写错了，名字不是 employee ID，这里应该是 activity ID，OK，那错，把员工当成了一个厕所。如果你这个对象不存在，怎么办？ or else through 那就直接声明出一个异常，把它给抛出去好了。


new runtime exception 这个异常的名字叫做 record not fun。好嘞，同样的，我这里使用一个数据库对象，数据库实体对象，把你的记录给它拿出来。拿出来之后，我们这里要做这样一个判断，如果你当前的记录已经不是一个正在进行时的这样一个时态，已经是个过去时态了，怎么办？直接扔出异常？ new runtime exception。好，这个可以给它一个提示，叫做 activity is no longer active 或者 is inactive 都可以。然后在下面我们同样的也需要调用咱的远程方法，给它这个坑位做一个释放的操作，我们这里 copy 一下，省点事。


这里叫不叫抢坑了？这里叫释放坑，释放坑。好，我们这里传入的参数。首先这个 ID 从哪里拿？从这个当前记录里面的 resources ID 里面拿过来，那这就是那你的蹲坑的 ID 接下来调用的方法，这个不是occupy，我们把它的路径改成release，那其他的部分我们不变好。坑位释放掉了之后，我们把当前的记录给它设置active，变成false，然后再给它设置一个结束时间，就直接用这种 new date 好了。那讲究一点的同学可以使用新的时间类型的类， calendar 这种时间类。那定义完这些属性之后，别忘了同学们这里要把它给怎么样保存一下，直接给它 save 一下，那我比较喜欢这种显式的 save 保存，我不太喜欢那种透明持久方案，不过现在年轻人写代码比较喜欢用透明19。那我这里再去声明一个返回值好了，直接 new 一个 employee activity，然后还是采用这个 bin utils 方法好了，这样简单省事儿一些。copy，把这个 record 里面的记录 copy 到 result 里面，再把这个 result 返回一下，这个 tolet 咱用不到就不声明了。


最后一步，我们这里把这个当前类的访问路径也给它标识上， transactional 标签扣上之后，访问路径 post mapping 叫什么呀？叫个 done 好了，完事。OK，那这个类创建好了之后，接下来我们这里要去创建一个闷方法。那这个类创建好之后，我们要去创建一个闷函数，慢函数，我们直接 copy 前面的 restroom 里面的启动函数，把它 copy 进来。那注意这个包路径，把它给变一下，我比较喜欢把它去放到上一层的目录。


OK，上一层目录好移过去之后，别忘了我这里也需要对这个类做一个改名，从 restroom application 改成 employee application。那这里与前面的 restroom 不同的地方就是我还要再做一个动作，咱前面用了 rest template，那所以我这里要把这个 rest template 给它声明出来。声明好这个方法之后，我直接 return 一个新建的 rest template，然后别忘了这里用两个标签把它给括上，第一个是把它声明成一个bin，那第二个是开启 load balancer，把这个负载均衡给它给开启进来。


那定义好这些所有的属性之后，我们接下来剩下的最后一步就是 copy 资源文件，资源文件就是配置项了，我们这里为了节省时间，咱就直接抄作业，从 restroom 这里把这个 application YAML 文件给它 copy 过来。那 copy 过来之后抄作业，别把别人的名字也抄上去，我们这里要小改一番。怎么改？你这个端口号给它改一下，改成 21000 好了，与此同时你这个名字作业上写的这个名字给它改成 employee service。


改完这两个之后，同学们这里数据源，那如果懒省事的同学你们可以去定义一个数据源，那我后面为了演示一些像分布式事务这样的特性的，我这里就定义了 2 个数据源。我这里定义了 employee DB，其实它是同一个数据源下不同的schema。那我只是用这种方式模拟一个多数据源的场景。那这里定义好之后，剩下的都不用改啊，我们直接把应用启动起来。那前面咱这个 restroom service 已经启动好了，我接下来启动这个 employee service。OK，那直接把闷方法启动起来。 321 走，你好，出来了，看到它有started，那说明应用已经启动起来了。转向浏览器，瞄一眼neques，刷新好，同学们，看，这 employee service 还有 resume service 都已经在这里存在了。

那接下来我们这边就直接发起一个远程方法调用，去蹲坑，触坑一个慢动作，我们首先来一个蹲坑，发起一个请求，到两万零一的 employee service 这里，那它对应的路径是toolybreak。我们设了 post 的请求，在 body 里面，我们指定了 employee ID 是1，点击一个发送。好，稍等一下，OK，那这里已经返回了一个结果，那这个字有点小，这关键的一个信息是ID，那说明对应的 employee activity 这条记录已经创建出来了。那接下来我来尝试一下，再去发送一个请求。好，你看他这里报错了，那错误信息叫快拉，说明他已经进到了一个坑位里面，这个验证没有通过，那这是期望的结果。


接下来我们这里做一个起身操作，那把 URL 这里填对之后，我们这里直接在 body 里把这个参数 activity ID 给到咱前面返回的一个 11 点击发送，那这条记录也已经正确返回了。那稍后同学们如果在自己本地做实验，我们会把对应的数据库的建表语句给它去放到这个 employee do 里面，看到这里有个 create DB 点SQL，这就是我们的建表语句。同学们把这个 schema 创建出来之后，直接跑一下这个语句就可以了。那么这一节的内容就到这里结束了。我们搭建了两个应用生产者还有消费者来模拟了一个服务注册，还有服务发现的这个流程。那么在后面的小节里，我们对 Napus 的一些配置属性，还有它的元数据再做一些深入的介绍。好，同学们，我们下一小节再见



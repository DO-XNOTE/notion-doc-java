---
title: 2-5 Spring注解源码解析-1（1816）
---

# 2-5 Spring注解源码解析-1（1816）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/c4fe53c6-79b3-4789-be52-9c1867f7e822/SCR-20240803-lvwj.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XFVTYF64%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAQJQzOvhfbksR3Xv%2FO%2BkQJrqWIGtKmVMqcvF2H97FvuAiEAnIKgBCAYNHvP7JOj6gZqg6nx%2B0rJKBQnNNdFnhsVcYAqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFgm34Zt2l9MtJzWoyrcA%2Bwkbs0B%2FcjMjQ8SwF%2FY8sX23PJTkk8qarM7fzJCw1xKaqYoB%2F8kltWBpXOIys6MATXtZLpQFNdPWorU5tDhXiTRFutjpPFyOyDeevtUM4QHiZEggMhUyT8rQJP9ZZ2vHV51x%2FfAG%2F9h6YzK%2BeMdrf0BqOBwahNwbcJuHmIpheq1y8bGERjQnTylq%2FvzKyrat%2FXIqs35xfDe4KMOL4i3Zr5cHco8MhpRpWoQC41J0ldm%2B9GLR7oDIZQfiDZPKY6RKajJRx9Rbe%2FmVnxx5BePizeaNMLekkuANqJO4rE2uNZ8%2BH1H3EXRTNCzOEjmnwXH8%2FUZyIvj6AKfF1DRBy%2FW2FRUt%2BXLo93t1puf0NUocu6JEufjLoyd%2Bv3SyNSipyCnT89aOW3dfdx8QY9AGOvdzgikN14xKxQFztBO5%2FqquerI6qpyry1d94KiJvBfPh%2F4j5j%2BWfnJUEqHpbu%2BXUA649DReD%2BoxuZ59f%2FkaZJRCN30IuocRO0HLcLuySb4j1PXKYAfyiD4egdBsMWwhPPM38YGDR7T7M2SpJO%2BGHU%2BITRgtCPHm0UogQygtnAJdoecSI%2FRhDeZtPuCN6IBb5dDS%2BX3w6ZVlP1Cg2hNJ%2BZ7fNUUwwSDGmlRx5Rp2KumMIK3%2F9IGOqUB6JAe%2Fewub10YZPtCHv6BANjVoZxuy9wQGEhVdExP7jbFx4pWr54zyTPBhs6nF27CuCRAt3orSjLiwp9Lgz0sQcsrLBSUBNNxjjrfNQbXUTKqpOD771cg7BJwJe%2Fp26MUAKRV1SIGQga9%2F7NtEGmA7%2F1bZy8e2ZiJh%2B%2FQedVWm%2F%2Fnb1RXkTf%2FTAQbS4ixZoZBEnjMpHUqQR5ZhrwWh0W%2FlNIJ7xvi&X-Amz-Signature=2e879657e43e762b574a76198cd1a29360d10f8778183399b00a35c870fb76c0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

同学们大家好，这章节我们一起学习一下 spring 注解源码解析，我们主要是学习 spring 如何通过注解来把 bin 注册到容器中。上一节我们学习了 spring LC 容器，相信大家对 spring LC 容器中必应的运行流程都已经了解了，我们在使用 spring 开发的过程中会使用大量的注解，那么在上一节的容器的运行流程中提到注解非常少，那么主要是为了让大家更加聚焦到避孕容器的注册和避孕创建的流程。至于我们是使用 XL 还是使用加注解，这是核心容器外围的一些实现逻辑，大家首先要能理解清楚核心容器的运营流程。


接下来这一节我们来重点学习一下 spring 是如何通过注解把 bin 注册到 spring 容器中？首先我们来整理一下 spring 与核心容器相关的一些注解， spring 的注解非常多，比如说 spring Mac 相关的注解暂时就不在这一节课的讨论范围。然后我们通过 lotation configure application context 这个基于注解的一个 SP 容器来进行容器的构建。
最后我们来重点介绍一下这个容器的一些处理流程。首先我们来看一下思路， l c 常用的注解。这里面我把这个注解分为三类，第一类是用于 bin 声明的注解，第二类是用于定义 bin 配置的注解。第三类也就是其他常用的一些特定用途的注解。这里面我们通过脑图来学习一下这些区别，在这里面我们可以看到用于 bin 声明的可以分为三类，第一类是 spring 提供的注解，我们知道 stream 是在 2. 5 版本以后才提供基于注解的方式去注射b，另一种方式是 GSR 205250，还有一个 GSR 330，两个都是我们可以理解为 Java 定义的一些规范。对于 GSR 250 和330，它们之间其实并没有什么特别的依赖关系。这里面只是有几种规范， spring 它是基于自己定义的和已有的这些规范都进行了一些实现。


我们首先来看一下 string 的注解，像这个注解 at competent 是可以理解为我们定义闭隐最基础的注解，像 REPORTS service 和我们的control，它这样的三个注解都是基于 at compaign 的这个注解来完成的，通通过这种方式去可以定义b，那么我们对于 bin 的依赖注入，我们通过 at where 的方式去表示一下当前这个属性妥依赖的bin。还有我们的 add value，对应 add value 可以通过我们的上下文去获取一些属性的一些配置信息。


对于 GS 250 的话，我们对于有几个注解是不陌生的，比如说 post contract 和 Pre destroy 两个就是我们在生命周期里面提到的我们在构造方法之后，和我们在销毁之前的执行内容。我们看这里面的比较常用的像 resource 这个注解，其实跟我们的奥特威尔这个注解可以理解为是一个对等的一个关系，它们的区别点是奥特威尔是基于类型去依赖注入， resource 是基于名称去做依赖注入。我们看一下 GS 2330，这个用的相对来说比较少一些，比较少我们像 name 的是它跟我们 component 或者 report 是做一个对应关系，包括 manager 的bin，它也是用来声明这个类可以作为一个 bin 注册到容器里面，但这个相对来说用的比较少一些。跟我们这里面奥特维尔和 resource 对标的，也就是这里面 injects 作为一个注入的一个标记。这里面还有 quality file，它是可以标明一下针对一些特定一些描述。下面像 scope 跟 single ten，它也就是描述它是否单立的。对于string，它可以理解为我们 string 的注解是整个所有的一个全集，对于这些注解它其实并不存在什么难点，我们主要是学会使用，知道它是什么意义也就可以了。


接下来我们看一下并配置的这些注解，像这里面我们非常常见的，像艾特 configuration 和艾特bin，这是非常常用的这些注解也是非常整个基于配子 bin 注解的核心。这里面还有艾特profile，就是我们区分我们的环境信息的。像我们通过 add import 和 import resource，这个是我们基于 Java Configure 的注解方式，提供了一些外部配置集成的方式。爱的import，它可以去引入一个另外一个加 config 配置。


爱的 import resource，它可以引入一个我们已有的 XL 的鼻音配置，还有我们 campaign 的scan，也就是我们可以通过对于包的扫描去扫描对应包下面所有已经定义了这些像 at component 的或 add name 的这样的注。解的。这些 class 可以扫描注册为bin。下面这里面有 add lazy， property sauce 和primary。这就是我们在描述 bin 的一些常用的一些注解。这些注解其实它并不是在 spring 2. 5 刚出来的时候就提供的，它是在 spring 3. 0 以后才提供了一些这些注解，因为 spring 2. 5 我们可以通过注解来去注射病，这有 4 分钟三点儿零以后它来为因为提供了 at configuration 和 at being，这样为我们 Java 来定义 been 提供了一个更好的一个基础，我们来学习 spin 如何通过注解来把 bin 注册到容器里面。这里面最关键的几个注解就是 at configuration， add bin 这一类的操作，那么集成，像 import 和 import resource 可以提供一些辅助集成的一些功能。


好，接下来我们来看一下一些其他一些特定用途的一些注解。像这里面我们如果开启注解，提供AOP，像enable，aspect， auto process 和像 event listener 和Trash，这是四五的注解，这是 4 点监听的注解。还要等等一些这里面用于单元测试的一些注解，像这些注解虽然说它不像前面几个非常常用，那么，但是我们通过单元车 4 使用这些注解也可以很好的去提高我们的开发效率。当然像这里面跟 AOP 相关的，我们四件相关的，和我们的一些四五相关的注解，虽然不在我们重点的讲解范围，我们也应该了解一下它的一些工作原理。


接下来我们看一下基于注解的容器，也就是 annotation configuration application connect，它是如何使用的。我们来构建这样一个容器，我们可以通过这样的方式。首先我们是通过这个容器的默认的构造方法，我们创建一个 context 实例，在 context 指令里面，我们 register 也就是注册一下我们的 Java 的配置，作为我们一个配置的入口。注册完成以后，我们调用 context refresh 方法，也就是对我们注册的内容进行刷新，这样的话我们整个容器由初始化完成，我们可以通过容器里面去获得我们的bin，在这里面我们通过 context get bin 的方式去得到对应的 bin 操作，我们获取到这个 hello 这个鼻音以后，我们判断一下子 no 的no，这也是一个简单的一个断言。我们来执行对应的业务方法，最后把整个容器去 close 销毁。


我们看这里面整个执行的过程跟我们使用 defiled listable being factory 构建容器的方式和很相似的，唯一的区别就是在这里面我们是构建容器的过程是有一些不同的。我们来看一下整个处理流程，我们可以抽象成这几点，首先我们在这里面是通过默认的构造方法来构建我们的 annotation config application contact 的实例，我们构造为构造出这个实例以后，我们就注册一下扫描的入口币，在这里面我们扫描的入口 b 是我们的叫configure。


接下来我们去刷新我们的方法，也就是进行 refresh 方法刷新，刷新完成以后，整个我们的容器就构建完成了，我们可以通过容器里面该的 bin 方法去获取到 bin 执行c，hello，接下来是执行我们的容器的关闭操作，那么我们可以通过代码去来看一下整个这个过程。


这里面我们是首先通过默认的构造方法构造我们的注解，当然这里面是为了特意跟大家去演示一下这个构造方法，扫描，注册必应，并且是刷新方法这三个部分，所以说在这里面特意的把它拆分出来了。其实 annotations config application 它提供了一些工具方法，可以简化我们的操作，我们可以点进来看一下，在这里面如果说我们把我们的参数，把我们的入口类参数传入进来以后，整个这个过程调用默认构造方法和我们的注册我们的入口类和Refresh，它可以在一个构造方法里面完成好。所以说我们这些操作是只是为了让我们理解起来更清晰。


接下来是我们去获得 Bing 的这个过程，这个获取的 bin 的过程跟我们在使用 detailed visible be in fact 是有些区别的。我们知道在使用 debug 的 listable be in fact，它只有在 get 闭音的过程中才会对鼻音进行实例化，而我们使用对应的 application contact，它的实现的，它是在 refresh 的过程就已经把所有的这个 be in 的实例化。
这里面的所有 be in 初始化有些不严谨，因为 spring 容器它是支持懒加载的，懒家长的这些病是只有在病因使用的情况下才会实例化，所以说应该把这些支持懒家长的病因排除掉。接下来我们对整个代码的流程来进行分析。首先我们来看一下我们的默认构造方法执行的内容是什么，我们在这里面默认的构造方法，它会通过 stop step 去构造一个我们记录器，也就是记录一下我们整个运行程序启动的一些时间，消耗的一些信息。接下来是通过构建一个 annotation being 的 definition reader，也就是基于注解的一个 being 电影的一个读写器，还有一个是 pass definition scanner，也就是说这是一个扫描器，基于我们的类路径。对于 Bing definition 的一个扫描器，我们看一下我们代码里面是怎么实现的。


在这里面我们可以看到，首先我们是通过这种方式，我们的 get application start APP 是 start 去启动的时候，这里面去传入那个参数，也就是通过这个名称标明一下我们这个记录器的内容，这个记录器的名称也就是 spring context notice in reader Creator，也就是创建我们这个 BD reader 的一个过程，它消耗的时间在这里面会看到它对它进行一个 end 的操作，这个跟那 stop watch 的功能是比较相似的，只是说它可以通过我们在 spring boot 的时候通过 ACQ ator 提供的 endpoint 去暴露出来。获取到它加载的一些时间。


在这里面我们去构建我们的 advertise BD reader。我们构建的过程我们可以点进去看一下，在这里面我们跟一下，这里面我们可以看到它在我们这个 notisen being defined reader 的这个构造方法里面，首先把我们的registry，也就是我们的 being 注册表赋值给他，同时我们这里面创建了一个condition，它是做什么呢？是对于我们条件的一个校验判断，也就是判断当前这个鼻音是否需要装载容器里面的一个条件，接下来我们看这里面是对于我们的一些注解。


configuring process 就是注册到我们的容器里面，看这个注册的内容是什么，大家去看一下，这个是非常重要的一个关键步骤，就是在这里面我们定义了一些东西，让我们的容器去执行的过程去做一些操作，这里面我们可以向下看。首先这里面我们定义的是首先判断一下当前容器里面是否存在一个指定的一个 b name，这里面 b 的 name 是我们可以从这里面看一下它的名称，也就是对应的 configuration annotation process，也就是我们可以看到它是对 configuration 的一些注解进行处理的一个process。


好，我们回过来看一下，如果说它不存在的话，我们会通过 configuration class post process 去定义出来，把它装载到我们的变容器里面。首先这是第一个最重要的，也就是 configure class configuration class post process，它是用来去处理我们这些解的一个核心的 POS process，那么这是一个。接下来第二个是需要处理的内容是什么，也是相同的逻辑。


先判断一下当前指定的病是否存在，如果不存在的话，我们把这是 out where annotation being post process，我们可以看到这个 being post process 他做的什么事情，他 4 用来去解析我们的奥特威尔和 Y6 这样一个注解的，也就是说他去做一个 b n pose 后处理，当他去校验当前这个 b n 有奥特维尔，那么去通过容器里面找到奥特维尔指定的类型，把它复制到我们当前这个病因属性里面。


好，接下来我们再看下面是我们的一个 common annotation being pose precise，我们看到 common 的话，可能看到这属于常用的，那么常用的它处理的内容是什么呢？我们可以看一下里面是它是 check 一下对 GS 250 的一些支持，我们看这里面去看一下对于 GS 250 它里面支持的这些注解是哪一些，我们可以看到是这里面包括resource，也就是 resource 为最主要的我们刚才介绍的 resource 和 adware 的一些区别，当然还有一些其他的一些注解，这里面像 destroy 和我们的 post contract 等等这些一些，也就是说加 x 对应的 JSR 的这些标准通过这个 post process 去做处理。


好，我们回头看下后面的，接下来后面还会处理了一些，比如说像我们的你的内容，这里面我们可以看到是跟 GPA 相关的一些内容，这个其实对于我们来说并不是那么核心了，这里面我们可以看到它会找到一个类名是 person 的 adtation 并 post process。也就是说如果说我们涉及到一些 GPA 的一些依赖的话，它会通过这种方式这个并 pose process 对它做一些后处理。


后面的内容我们可以看到它是跟我们的 even 的 listener process， being name 相关的，也就是说跟我们定义我们的一些事件监听的一些方法的一些后处理。接下来后面是我们对于 defailed event listener factory，这是一个创建四件监听的一个工厂类，我们进来可以看到它里面主要的方法，也就是 create application additioner，它主要的功能也就是创建一个 application listener 的一个方法的一个适配器，也就是说我们通过它统一去调用对应的 listener 的执行的操作，我们通过这里面看到整个这个执行完成。那么对于我们这里面的操作，我们在这个构造方法里面做的事情，我们可以在这里面去看一下。


首先我们去创建我们的 being deep name reader，在这个 reader 里面去做了一些事情。首先创建一个肯迪森evaluate，也就是说我们的一个条件的一个判断器，接下来是通过 notisen configure UTOS 去注册一下我们这些跟注解相关的一些后处理的类，这里面我们总结出来，这里面涉及到，嗯， configuration class pose process 这是最重要的。其他的像自动注入的和我们的 common case，这是 DPA 相关的一些后处理，以及我们的四件四件监听器的一些工厂处理，以及我们的默认的四件监听的工厂创建方法。


接下来我们来看一下，嗯， class pass being scan，在这里面我们看我们去构建这个scanner，这个方法构建它来说相对是比较简单一些，我们跟进去看一下，在这里面也是多乘构造方法的调用。那么在这里面是他做的事情是首先去把我们的容器的注册表作为属性复制上来。


接下来要注的事情就是我们看一下 user defu 的 filter 是否使用我们默认的一个扫描的一个过滤器，我们可以看到默认它是一个处，我们可以当然也可以作为参数传进来，我们可以看一下它里面处理的逻辑，在这里面我们在一个 include filters，就是包含的filters，它创建了一个就是 noticing type filter，也就是基于注解类型的一个过滤器。也就是说它的意思就是说当如果说这个类它已经通过 component 的这个注解去修辞的话，那么它就会把它扫描作为一个鼻炎记录下来，这样的方式也就是说它去扫描出我们整个包，下面所有通过 component 修饰的这些类可以用它去做一个 bin 的注册，当然它不仅是一个compenter，我们提到它支持我们这里面是写到 GS 2330 和 GS 250 的操作。对于我们还包括哪些内容，我们可以可用这里面看到。对于 GS 250，在这里面有加 x notation manager 的 b 和我们 GS 2，这里面是 330 的，它里面包含的内容就是加 x inject name 的这样一个注解。那我们通过它可以看到其实在我们扫描的过程中，就会同时这 3 个类型的注解都会扫描完成。


好，这样我们就可以看到对应这个 class bug being definitely scanner，它住的公路，它的扫描功能也就支持了我们 spring 原生自定义的 component 和 JSR 250 的 manager 的bin，以及 JS 2330 的 name 的。


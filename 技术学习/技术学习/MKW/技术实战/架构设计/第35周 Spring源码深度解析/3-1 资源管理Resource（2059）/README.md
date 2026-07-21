---
title: 3-1 资源管理Resource（2059）
---

# 3-1 资源管理Resource（2059）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/029877a2-3384-4071-a495-446b42e4c518/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664RTMD333%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232019Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD0tThFe%2BTlvbwVcDPqO5Kjg5YNlvdF7A3WKRH45SfIXgIgO3z8IDEbYlhFC%2BAFnC51xA3T2tomOXN%2F0AgcENFmWfkqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGhDtkZRXMFs1682KircA15FLZFL8zjd4PMRRupBG55aQDzKFomMdW0tFspenUmPLlvKA0Tqh63RFrMd3dc8ibTGayk%2BjZHtUmKXtLqid7HYskV%2BqH8BSJfomadVYBk%2BWjsKkU%2FVubaQtW3rvuJKbXc7FPZrKTaRpMZE9lvaxOWBLI%2Bt9pPYurNTy6yJ6tmuane9CihKOwJeXJQoOiDOzZoCSDGTxLsqOmmuvtDW4PxiQkJkqv0Ed4FsiG28GW54v3P3fr%2B0RGMcFe9%2F8tOqRF91CeQcCH2AttL5tu9ZMHX%2BYa%2FELoCg0959fjw7RccRS8UlwMkWE%2FVMu6Y8ypeovAVTgG20qHgGcFi3oK9RyNFFCnF%2FfjL%2BsuHmMoCR0Vw1%2FwyFoylKsdhuyQcbx0ZoYVm2V3MVHYCur%2FeKwdeNmNXFoPXz7XwdO%2F0D5o2U1XcNkre50on8TP%2BSZ9ENjodsieFO5%2BwDCFSQrq05mHEjeemF%2BEkTDX2h5l%2FRk3HLa7wb9Nw9iBVoIcpBEP0jyluYDYHQGpcr8Nd46IeuXU7bH0tfn%2B0P5D1NsZhRY1mx7UEUX1RmCmcszd3H2sMB%2F5T5%2FhTUrAuopKdqd5GZ%2Fx9QO8P9jWXvvFb4ezHnEyNHZZjrYHGzksDqLYN9al4IMKK4%2F9IGOqUBtA1cdfkOqpCgvCRPvyV4bN3LgDk5rkK0XD8M3MTqa6ri%2FnWXnPnidBT8gx7r%2B3BWMfqLEEM4S4U2RjvXF804JxNwrY%2BKLjpp3dlFVwauVTJ6gLgRkN1vU%2FQdGUlq0qbzVP5mwS1PRjEExw7%2Bi89gh4NL9V7wUUWFZHWIukmuur9wSoDv4SxL8eAlz6VmIbK1aQ4TFB2B1VWsHyjhg%2FXyfCDoJJs0&X-Amz-Signature=8a2b02335ef0aff1d63397d10f934f5d88ffb93638a3c09ea6cb393e8dac1082&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

同学们大家好，这一章节我们介绍 spring 的资源管理 resource 这个抽象接口。我们在做 Java 功能开发的过程，经常会涉及到一些资源文件的读取，这里的资源文件包括多种，比如说本地资源或者说网络资源。本地资源又涉及到几个相对的根目录，比如说我们 class pass 的根目录，或者是 Web 工程相对的 Web APP 这个根目录。 spring 它为了方便各种资源的读取，抽象出我们这个资源接口，也就是resource。我们也通过三部分来介绍此不用资源相关的内容。


首先我们介绍一下 resource 接口它的设计与实现，我们看一下 resource 接口提供了哪些方法，以及它有哪些常用的实现类。其次这里面的 resource 它都会通过 resource loader 去加载，对于我们不同的resource，它不同的 resource loader 也显得比较重要。我们再学习一下 resource loader 的设计与实现。第三部分，也就是我们通过代码去看一下 resource 的使用实践。好，我们首先来看一下 resource 接口的设计与实践，在 spring 官方源码里面，我们定义的这样一个 resource 接口，它这里面有这么一些方法。看到这些方法的话，大家对于我们的 feel 类的话有一些相似，比如我们这里就判断一下当前资源是否存在的，或者是把整个资源获取成一个文件， get feel name 这样的一些操作，同时也有对应的 get URI 或 url 相关的操作，这里面我们有判断当前这个资源是否是一个 fill 或是否已经open。那么对于一个文件它是否可读，以及它最后的修改时间等等这样一些常用的。


我们看到这个文件它的这些接口其实是跟我们 ZDK 里面的 feel 类是有一些相同之处的。看一下这个 resource 里，它在 spring 源码的位置，在这里面我们打开 resource 这个接口，你看对应它的位置是在哪儿？它的位置是在我们的 spring core 里面，对应的 core 包下面，在 IO 下面，也就是整个它是我们这里面可以看到 RT spring framework core i o 这个 resource 接口，同时这个接口它既称 import stream source，这个 input stream source 它也是 spring 定义的一个接口规范，对于它来说唯一的一个方法是 get input stream，也就是说把我们的资源获取成一个输入流。


我们回过来看一下 resource 对于它有哪些实现，我们可以从这边看一下它继承结构，在这里面是比较复杂的。首先这里面有对应的 base resource，同时还有几个接口的实现，比如 context resource， ATP resource 以及一个可写的 resource 和这里面的每一个对应 abstract resource，以及它的一些子类。从这里面看的话是相对比较复杂的，我们不容易抓住重点。


我们现在来回到PPT，看一下我们比较关注的几个 resource 的子线，在这里面我认为相对比较重要的几个实现，也就是对应的 URL resource， class resource， file system resource 以及 surlight context resource 上面这几个，尤其是 class part resource 和 file system resource 这三个是比较重要的。对于这个 input stream resource 和 better resource，更像是对于 resource 功能的一个补充。这里面我们重点去看一下。


Passport resource 相当于 spring 跟我们定义了一个文件的协议，这个文件协议一般会通过 class Paas 冒号作为我们整个文件的前缀。那么我们对于一个普通的文件，比如说我们会通过 HTP 协议或 file FTP 协议，或者 file 我们的协议去读取。 Cuspaas 就是 spring 跟我们定义的一种协议法子，如果是以 Caspaas 为前缀的对应的资源，它会通过我们 Java 对应的 Cospass 根目录去读取。


这里面 serverless context resource 也是我们在做 Java Web 开发过程中常用的，假如说我们需要通过获取到我们当前加 Web 的根目录，也就是我们对应的 Web APP 部署程序的目录，那么我们需要通过 Server 的 context resource，也就是对应的 resource loader 获取到这个资源文件。这样的话我们的相对目镜就是我们的 YVP 的根目录。
好，这是几个 resource 比较重要的接口实现。这样同时我们现在可以到源码里面看一下，我们可以重点去看一下 field system resource 和 cut pass resource，我们来这里面去，在这里面我们可以看到这是 field system resource，同时我们看一下 class part resource，我们先看 feel resource，在这里面 feel resource 我们看到它其实就是把我们对应一个常规的 GDK feel 的一个包装，比如它的构造方法，也就是我们传入一个普通的pass，或者说是传入一个 fail 类，也就是 fail 的对象。把我们这个 fail 词的 resource 构建出来。


我们来看 class Paas，在这个 classpath resource 里面，它其实给我们定义了一种规范，也就是说整个 class pass resource，它是通过我们的根路径里去获取的，在这里面会定义对应的 class loader 或指定的 class 去获取我们 class loader 的内容，从这里面可以看到它这里面的一些操作，我们可以重点看这里面的 get UL，这个 get UL 操作它会通过 resolve UL 去解析我们的内容。


在这里面可以看到它在解析 URL 的过程中，首先会获取当前我们指定的class，在 class 里面去获取 get resource，这个 get resource 它会利用到我们的卡斯 loader 获取当前的路径，如果能获取到对应 URL 去获取，如果说它不能获取的话，它会通过我们的 class loader get system resource 方式去获取这样一种方式。这就是我们在解析类路径的一个优先级顺序，如果说指定class，那么优先使用 class 的方式获取它相对路径的resource，如果没有的话，它会根据 class loader 去获取，如果 class loader 也没设置的话，正常就会获取。我们 class loader 对应的默认的一类加载器去获取，这是 class part resource 的内容。


我们看到这几个对应的一些资源文件的实现，对于 resource 它这些资源怎么构建的？跟刚才可以看到像 feel system resource 或 class part resource，我们都可以通过构造参数去构建这个对象。其实我们在程序使用的过程中，更多的是指定一个u，r， l 或 URL 或者是一个路径，我们通过对应的 resource loader 去加载。那么我们来看 resource loader 它的情况是怎样的。对于 resource loader，它提供了两个方法，一个是 get pass loader，另一个是 get resource，这个 get resource 就是我通过传入我们的一个指定路径，通过指动路径你把我们对应的资源加载进来。至于我们加载的是什么类型的资源，可能跟我们对应的这个 resource 出的内容是有关系的。我们可以看到其实 resource loader 它还提供了一个常量，这个常量就是标记对应的这个卡斯 pass URL 的一个前缀，也就是说我们以这个对应的前缀指定的这些文件就会默认的使用 has pass resource 的 pass 去加载。


对于 resource loader，它还提供了一个更复杂的一个 resource loader，这里面是 resource partner reslower，也就是对于我们资源模式的一个解析。可以看到在这里面资源模式解析的时候，它支持两种 class pass 前缀的路径，一种是我们刚跟这里面是对应的，也就是普通的 classhouse 冒号一个前缀作为我们的一个加载的路径。另一种是我们可以看到它的定义是 clasps or URL，也就是前缀，它的使用方式就是 class pass 星，这里面相比较的话读了一个星的符号，这个星的符号它的意义是什么呢？就是不仅仅从当前卡死的一个路径里面去查找，甚至去查找对应的一些炸包里面的路径的内容，这样一个过程，我们其实整个我们的 spring 所有的 application context，它默认都会继承了 resource loader 里面的 result loader，也就是 debug result loader 的一个实现。那么我们这里面去看一下 result loader 它有哪一些关键的实现。


对于 resource loader，我们最基本的就是 default resource loader。我们在学习 application context 源码的时候，因为在它最顶层的一个依赖的类，也就是继承的类就是 default result loader。同时还提供类似于比如说基于 class 的一个相对路径的一个 resource loader，这里面和我们的系统文件的 resource loader 以及 THREAD context result loader，每一个 result loader 它使用的当前环境的路径是不一样的。对于卡死这里面的一个相对路径加载器，它其实是通过我们对应的卡斯 pass 路径去加载，像 feel system resource，它会根据我们文件系统的路径去加载。其实这个 file system resource loader 跟我们正常使用一个 java l u to java l file，这获取的路径是写类似的，也就是可以理解为一致的。这里面所有的 context resource，也就是我们在加 Web 跟目录里面获取我们相对路径的一些值。


好，我们这里面去看一下几个常用的 resource loader 的实现，这里面我们重点来看一下 default resource loader，在这里面 default store loader，我们可以在这里面看一下，它的继承结构非常复杂，我们可以从这里面看到整个它下面涉及到这里面是指定了几个常规的 resource loader。


在这几个常规的 resource loader 下面，我们可以看到这里面是 abstract applixin context 的，我们看到这个类的话，我们应该有所了解，对于它下面所有的这些实现，可以看到所有的 application contact 的实践都会继承直接或间接的继承底票的 resource loader。对于这个 detailed result loader，它的工作也比较简单，在这里面它只是实现对应的 get resource 的操作，通过传入一个 location 地址获取到我们的resource，通过这里我们看到。其次这种方法是非常常见的，因为我们在很多地方配置的时候会指定对应的location，比如说我们对应的 spring 点XL，也或者是我们在指定的一些其他的一些配置文件，都会通过这种方式去解析，在它解析的过程中会做一些逻辑的判断。


这里面我们可以自定义我们的一些协议解析器，但默认的话这个协议解析器是没有的，可能直接会执行到对应的location，我们去判断一下它是不是以对应我们的斜杠去获取，如果说没有的话，它再去判断是不是经过卡斯帕的URL，那么在这里面我们可以看它，也就是我们这里面指定的这个字，也就是 class pass 冒号这样一个协议的名称。同时我们可以看到在这个 resource UTOS 下面指定了几种文件的协议，这里面有 file 协议和 jar 协议，也挂包协议，普通的 fail 和普通的 job 这样一种方式。好，那么在这里面它处理的过程，如果说它不是一个普通的文件对应的协议获取的话，它会尝试去把我们这个 location 解析成一个URL，通过解析 URL 的方式去判断一下它是我们当前的一些资源解析的方案。


好，这里面我们可以看到对应的是 default result loader。那么对于这个 resource loader，它另一个扩展接口，也就是我们的一个资源模式的一个解析器。对于资源模式的解析器，它这里面也包含两个，一个是普通的基于我们这次 and pass 的方式去解析我们的资源，另一种方式基于 Server net contact resource 的方式去解析。


接下来我们来看一下 resource 它的一些使用实践，这里面我们主要是对 resource loader 的一些方式进行验证。好，在这里面我们定义了一个模块是 spring scale，这个模块我们先看一下泡沫依赖，里面是非常常规的一些依赖，注意这里面我们是依赖了 showcase spend IOC，这是我们为了去演示一下多配子文件加载的这个过程。好，其他的像 spring context 和lombbook，这是我们常规经常用到的一些内容。那么在这里面我们看一下电影的这个 resource skill 这个类，它其实就是构造了我们几个常用的 result loader，我们可以看到这里面是 defailed result loader，以及这里面是我们的 file system resource loader。下面这个是我们的 class 相对路径的一个加载的 resource loader。同时我们在定义这个 loader 时候，指定了一下我们的 class 相对路径，也就是 resource skill，也就是说相对于我们这个类路径，相对于这个路径它的目录是哪？它的目录也就是对应的我们这个包结构下面，但是我们的类编译完成以后，它就会对应到我们 target 对应的class，我们对应的 resource scale 点class，而不是对 Java 对应的目录，这是几个？下面我们看一下，这是我们的 resource partner resolver，也就是说我们对于资源的模式的一个解析。


我们看一下对应的单元测试类，这个类里面我们执行的一些验证的效果。首先我们在这里面是通过 new 的方式构建一个 resource scale 这样一个实例，那么我们首先来看一下它的默认的 resource loader，在默认的 result loader 我们盖的resource，比如说我们如果不指定路径的话，它就会通过我们默认的 resource loader 去加载我们的资源，这个资源默认它会采用卡斯 pass 的方式去加载，现在我们可以指定一下运行一下，看一下它执行的效果。好现在执行完成。


我们从这里面可以看到当前这个 resource 它是一个 classpath resource，虽然我们没有指定它的路径名称，那么我们可以从这里面去看到当前文件是存在的，也就是说它是能定义到一个 fail 文件，那么 fail 文件它的绝对路径是什么呢？我们可以从这里面看到，在我们当前的 showcase spring scale 下面有一个对应的目录，也就是 token 的 test classes，这是什么意思？假如说我们使用默认的 debug resource loader 去加载的话，加载到的内容是什么？因为我们在当前的一个测试环境，它加载的我们的根目录是哪里？是 target 对应的 test class 下面的一些内容。


这样的话，如果说我们想加载对应的文件，比如说我们想要加载 log back 或者是其他的一些文件，那么我们就可以在这里面去指定这个文件去加载了，我们可以在这里面跟大家去演示一下，如果说我把它改成 log back 我们能看到的效果，那么这样的话就加载到 Lockback 这样对应文件，那么我们执行看现在我们可以看到当前的文件就是对应的这个目录下面的 logback 文件。


如果说我们在加载其他的一些不存在的文件的话，它就会提示我们当前文件不存在这样一个问题，那么这是我们的一个默认的 resource loader。如果说我们想加载一下其他的一些正常的文件，我们怎么做？可以看到在这里面我们知道 string 给我们定义了一些协议，我们看这是一个文件协议。


如果说我们通过 debug 的 result loader 去加载我们一个 palm 文件，我们怎么加载？这里面我们指定一下 field 点palm，点 x now，它有这个 field 前缀，它在执行的过程中就不会解析我们的 cospah 了，它会解析 field system，也就是我们的文件系统的路径。那我们来看一下解析执行的效果。


好，现在执行完成，我们可以看到这样的话，它的类型是一个 URL 的一个 result 类型，通过这种发送我们获取到我们的当前文件是存在的，那么这个文件的路径是哪里？我们可以看到在这里面对应的是我们这里面的 spring scale a palm 的XL。


大家注意一下，这个文件是我们源码的目录，它不是对应的 target 的目录，在这里面也就是对应的这个 palm 文件，它也就是这个文件的目录。我们再看下一个，也就是说我们默认的 resource loader，它可以通过不同的协议去加载不同的文件。如果说我们不使用 default loader，我们要用指定的一个 file system 去加载我们的文件，那么如果说我们确定它是一个文件系统的资源的话，那么我们可以直接使用 feel loader 去加载，加载的过程中它就会去简化我们的配置。在这里面如果说我们确定用 file system result loader 去加载这个资源，那我们可以只需要写我们的 palm Mac，那也就是文件路径就可以，在这里面就不需要再强制的去指定这个协议了。
这里面我们可以再跟大家去执行一下，看一下效果，我们可以看到当前也获取到这个文件，它对应的路径也是 spin scales 对应的 palm 的 XR 文件。好这样去找到这样文件。接下来我们来看一下这是我们是类路径的一个相对的 solid loader，那么在这里面他怎么理解这个相对类路径呢？假如说我们如果说是在写配置文件的时候，通常我们会放到 Meta info 下面，但也有一些情况，比如像我们介绍到 dispatser serverlite，它有一个 property 文件，它就会在对应 Dispatch Server Lite 相对的一个目镜去写。


那么在这里面我们如果说加载一个路径，我们可以看到当前我们要加载的，比如说我们指定的一个空路径，它的相对路径在哪？我们先看一下结果是什么。在这里面我们看到如果说我们只传一个空路径，它得到的 class pass resource，我们可以看到它指定的 cut pass resource 指定是什么？可以看到是 showcase scale 在这个目录下面，这个目录是哪里？刚才介绍到了这个目录句，就是 resource scale 这个类相对的目录，也就是我们相对的这个包结构。


这里面我们因为定义了它的一个相对class，是指定的日常scale，这个 class 它的绝对路径在哪里？它的绝对路径我们可以看到它的绝对路径，也就是在我们向项目对应的target，也就是 test classes 这里面我们可以看到，也就是在我们的测试目录，我们 target 对应特色目录下面的这个包结构下面，我们可以点开它，其实就是我们对应的这个目录的 d 相对位子。


那么我们接下来再看下面这个 result partner resolve，也就是说我们的资源模式匹配的话，我们可以看到这里面我们只是用构造方法默认构建出这个 partner resolve，其实这个路径这里面是使用了默认的 and 通配符的方式去处理的，这里面 pass master，也就是说我们的路径匹配是通过 ant 一个路径匹配，我们知道 and 路径匹配也就是通过斜杠和星号对应去查找匹配我们的目录。


在这里面我们来看一下这个执行的效果，那么如果在这里面我们去看到我们是使用了，如果说我们使用这个通配符去匹配的话，我们需要指定一下我们当前类路径的通配符，当前类路径通配符也就是 class pass 性，这里面对应的这路径也就是在我们的 resource partner resolver 这个接口下面，定义了一下这个路径的名称，我们看一下这个接口的实现，这里面对于卡斯帕斯全部的 URK 前缀的资质，卡斯帕斯星冒号这样一个结构。


这里面我们咨询一下，看一下它获取到的结果。我们可以看到在这里面我们打印出来这个resource，对于 hello Bing 这个SL，我们可以看到我们获取到两个资源文件，这两个资源文件它的区别是什么？分别对应的是 spring scale 和 spring l c 这两个对应的target，下面一些编译出来的文件，也就是我们对应的Hallobin，我们这里面是两份文件同时找着了它通过这个通配符的方式找到的原因是什么呢？我们刚才给大家介绍到，因为在我们这个 palm 里面依赖到了我们的 spring LC 这样一个模块儿，因为在 idea 它去做了一些处理。


如果说我们当前同样一个模块儿，也就是一个 product 里面的依赖的话，它会把我们当前对应的这个 string LC 所在模块儿里面的 target 也会加载到我们的 class 里面，所以基于这个原理的话，在这里面执行完成以后，可以找到了两个这样的配置文件，一个是在我们的 string skills 对应的resource，它通过编译到对应的 target 下面，也就是这里面对应的 spring 的这类这个文件。


以及我们在这里面是 spring l c 下面这里面的resource， hello bin 和 hello context 对应它编译的目录是哪里？是这里面 target 对应的classes，这样是 string 的目录，这样的话，也就是说两个对于同名的文件，我们它通过相同的一个通配符去把它给找出来。好了，关于 spring resource 相关的一些内容，我们就先介绍到这里，同学们，我们下一节再见。


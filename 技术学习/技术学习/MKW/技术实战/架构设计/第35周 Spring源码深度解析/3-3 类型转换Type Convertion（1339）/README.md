---
title: 3-3 类型转换Type Convertion（1339）
---

# 3-3 类型转换Type Convertion（1339）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/ff927a38-6e54-4be2-b53e-08100ff6ad9e/SCR-20240803-opug.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466W7J73LRT%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232021Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDDdonizqeWRwQN0vkKBOjjF%2FkKgIXgtQ0KKm%2Bd1IkdIgIhAOuPK01n%2FRb3WYtd398JbRbyLusrmug7S0S%2BVnO5mnr2KogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxYzI7VsASo%2Bhcoj2Eq3ANwnvL3vxDcy5GfUgR1PsXZqPqpTJ7rFT8G3fSL5HlcbY6uYooDWHXUrp7GdZoGN6h15lxxDoX5UE1kznZnGdH4YH2Hy6DOXAVdvYt2qQ08hfbdj8INK0vcdJY7K3NeJhvKWHySwlLhzA3qof74pgZ%2B4kTG9%2B0OETrSEbzkF4F%2BGgzTjXkUKy%2B0Lmms%2F%2Bz54RG%2B5x75W9YnsHlbso6L8VFoBk7QVkAM%2BnrB5QKTumC1lmvpjYOExYXdIdep5IGROG89HfLH6%2B2Yjdfq4JyVZXQO7nviL7EKx7tSMxY4lZ3JojS7krBDastGgO2yk1PzEUUTqPfR5sDBKOv4IuC5AIj3p2fZiTJ5WL2TVFXvLOa9t%2F1WnfnqnQ4ilOG313REwWbhCwiL8VFktSHmzx4gtxDxvmdZgysIjqBKxoglL1kR4TJNdlW8jjvaaeZbmSXCbHQuD%2FaJYmKKYoOue77MbgpOVdIEon4Ma9223jusjzSfS%2Bxahk%2FmIeTUDzzem79zVtzJ5l509dQmyTKOkH2jgFR2V%2FEr9DPpQqCFy3M%2BqYascn88MzZMjxSwNhFI65PFo6V5zqiGYlKhf05XsiXJAQR6Wjpe3rt%2Fr%2FM5xyJLOKvcwOHHOxZ7kehuruMTUDCruf%2FSBjqkAf3gPOEbS2PYjqf9tzYaeQzcBwFM8VSD%2FMi5wqXZGrGrTwO7mUAIBinyBWecUhKVShGG30JxRlSAhlSLAOFIs5BFVqZuU1wrLykQPz8tVyGiBK%2B1km795%2B5wQLtKR9RyhZXBlhbzdTHVCR%2FSl%2Fqkp44FsGB9TXnB6r81PkFRrzwmLT3dFE%2Bs5TbrTUibEkoMFFCIBRBvFpIkoQJTSp0XvgdTjg1S&X-Amz-Signature=1893a6a1d1b1f4e98e4e23fc1e8fa30ffee00fd731e315159bd105a3305e3a3c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

同学们大家好，这一章节我们来介绍 spring 的类型转换。 type conversion 数据的类型转换属于使用频繁的一个基础操作，因为是基础操作，加上 spring 合理的封装，我们经常感觉不到这个数据转换的存在。其实程序处理业务的过程与外部交互，输入和输出都会涉及到数据类型的转换。比如说 MVC 作为输入端，从外部请求把参数转换为加 2 对象参数，那么这个过程是涉及到了类型转换，那么经过业务处理，加 r 对象会序列化为JSON，在输出过程这个过程也涉及到了类型转换，所以说类型转换是使用非常频繁的。


那么在这里面我们介绍这个类型转换，我们还是通过三方面。首先我们来介绍一下 spring Converse 它相关的一些核心的API，那么再介绍一下 spring conversion 使用的场景以及 spring conversion 它的一些使用实践。我们首先来看一下跟 spring 类型转换相关的API，那么在这里面对于 spring 的 conversion 怎么样？它最重要的接口也就是 convert 这个接口，它就提供了一个数据的转换。我们来这里面去看一下对于这个 convert 这个类型的转换，它的方法就是 convert 我们的参数是s，我们的返回值是t，也就是说 source 和 token 的这个接口其实非常简单，也非常容易理解。


那么如果说我们的类型转化会涉及到很多的类型，比如说像我们的数据和字符串或数据，字符串和日期等等这些相互的转化，它会涉及到很多convert，那么对于 convert 我们使用起来管理起来会比较麻烦，那对于 convert 它还会提供了对应的，从这里面可以看到是它的一个 convert service，那么 convert service 也就是对于我们的 convert 进行了一些集成包装。


在 convert service 里面它会把所有的 convert 管理起来，我们在这里面首先去判断 can convert，也就是是否可以转换，如果可以转换的话，我们再进行我们的转换的实际的操作，进行 convert 操作。这里面的 convert 操作跟我们在 convert 接口的操作其实是类似的，只是因为我们对所有的 convert 进行管理的话，需要关注一下具体我们这个 convert 的类型，所以说我们在这里面执行的时候需要指定对应的 sauce 以及它的 pocket type，我们对于相同的一个sauce，它转换成不同的类型，可以去选择不同的convert，在这里面也是通过 convert service 去进行选择的。


我们再看一下这里面是 convert 和 convert service，那么对于跟 convert service 相关的还有哪些？像 convert registry 和 convert factory，这里面是一个convert，一个注册器，我们可以知道如果说我们在管理多个 convert 的时候，需要有一个空间来去管理一下我们的所有的 convert name，这里面就是一个注册器的一个概念，在这里面跟 convert 相关的我们可以看到这里面还有 convert factory。


confirm 的 factory 是什么呢？它可以就是说我们在构建 convert 的过程，这里面有一个 convert 工厂，可以快速的生成我们的 convert 不同的一些convert，我们可以看到在这里面我们通过这个 convert factory，它里面去 get convert 的时候是指定了一个类型，也就是说我对一个指定的一个目标类型生成跟它相关的一些转换器。
我们可以看到在这里面 convert factor 里面，这里面比较典型的是也就是我们的一个 stream number convert，那么在这里面我们知道对于 string 它作为一个类型，那么它转换成数据，那么数据的类型的格式会非常多，那么在这里面是使用 convert 的过程，它会构交出一个 stream number 这样一个convert。


对于这个 string number 它的实现，它是怎么实现的？我们可以看到 string number 它实现的过程，其实也就是说调用了 number you two 的一个 plus number，也就是它一个数据处理的过程。在这里面它可以对相同的一个 source 一个输入，它可以进行不同的目标输出。也就是我们作为string，它会转换成 long int，或者说其它的一些类型，它都可以通过这个 convert factory 得到对应的一个转换器。我们可以看到如果说它需要的是一个 string to long 的转换器，那么我们可以得到一个 string number，它这里面是一个 long 类型的 talk type，如果是 in 的话就是 integer 一个 talk tap，这样就相当于是把我们这些 convert 进行了一个归类。


接下来我们看这里面是 convert the factor， convert Jackson，剩下是一个相对比较重要的，就是我们 convert service 的一个实现，对于 convert the service 的实现默认是 default convert service，对于 convert service 它已经把一些我们常用的这些数据转换都集成起来了。


那么对于 Defin 的 convert service 呢？它 spring 提供了一个构造的一个 factory b，这个 factor bin，也就是 convert service factor bin，那么我们可以冲 convert service factor bin 来去了解一下它这个构建的过程，我们可以看一下在这里面是 compare service factor bin，在这里面我们看到首先这是一个 factor bin 类型的一个对象，那么它首先是继承了 factor bin，继承 fact bin 它的参数类型是 convert service。通过这里面我们知道它一定有一个 get object 的操作，这个 get object 的操作，它返回的类型也就是我们这里面的是 convert service。好，这里面对于我们这个 b 构造完成的时候，它会去对我们的 off 的 protosize 去 create 这个 convert service。这个创建的过程是比较简单的，这个创建的过程简单的是 new 了一下 debug confirm service。


那么创建完成以后它底下要做的一些事情是什么呢？这里面还做了一些对于 convert 一些注册，因为这是一个 factory bin 操作，它其实注册支持我们在这里面自定义一些 converse 的方式去注册进去。当我们在后处理就是 after process 的过程的时候，同时把我们手工去注册的这个 convert 注册到这个 convert service 这样一个过程，其实更重要的逻辑，也就是在我们构造这个 convert service 的实现。


在这里面我们创建这个 debug 的 convert service 的时候，我们可以看一下它其实也就是注的是 add debug convert，其实这里面的东西是非常多的，我们可以进来看一下。在这里面首先它会去我们可以分为三个部分，第一部分是 at Scala convert 和 at Clacson convert，这个 scaler 我们可以理解为这是一些标量，比如说数字和字符串、日期、货币等等，这些转换的类型我们在这里面去完成，这是跟集合相关的内容。


那么我们来先看一下跟标量相关的这些convert，在这里面我们可以看到这是数字类型的转换，是 string 类型的转换，这里面有一些 correct 和下面还有一些布尔类型等等，我们看有 local 相关的一些转换，这里面有货币相关的一些转换等等，这里面也有uid，也就是说这些常用的这些类型的转换的，其实 spring 台它已经给我们提供完成了。


那么另一个我们可以看一下是 add collection convert，这是跟集合相关的，我们看集合相关的，这里面有 array to Clacson，我们的 clacson to array 就是副主和集合的一些转换，这里面有 map 相关的转换等等。这里面的内容其实也是相对比较丰富的，也就是把即可相关转化也跟我们去加入进来了。


我们看下面还有一些具有典型特征的一些convert，我们可以看到这里面像 string to time row，也就是我们的一些死去的一些转换。下面还有一个，这是比如说 i d to entity，我们可以把一个 it 和实体进行一个转换，通过这种方式或者是实体和 ID 的一个转换的过程。当然这里面把一个 ID 转换成一个实体，它会依赖到我们实现的一些 do 层的操作，这是我们看到我们跟 spring 速率转换的一些核心的一些 API 的情况，接下来我们看一下 spring conversion 1 的使用场景。


对于它使用场景最典型的场景就是 spring Mac 层的一些数据转换，我们的输入输出它都会进行转换，比如输入的话，我们可以理解为是它最终的一些直符串的内容转换成我们的加压对象，输出的话把我们的加压对象转换成直符串的内容，这个直符串可能是JSON，也可能是我们指定的一个 view 视图。


那么另一个场景就是 spring g，d，b、 c 层的一些数据转换，这里面的数据转换主要是指我们的加 2 程序跟外部交互的过程中，涉及到一些序列化、反序列化的操作，其实跟我们这个 conversion 是比较对应的。好，接下来我们来看一下 string conversion 的一些使用实践。进入我们的代码实例，我们看一下，在这里面我们定义了一个 convert skill 的一个test，也就是我们通过它来去校验一下我们 convert 功能。


在这里面我们使用的是 conversion service，在这里面我们可以看到 conservice 这个接口，那么它的默认实现是什么呢？在这里面我们定义了一个 convert skill 的一个配置类，在这个配置类里面我们定义的是 conversion service texture bin，在这里面我们构建这个 convince service，这个给大家也展示过了，我们可以通过这个 service texture bin 得到一个 convention service 这样一个对象，那我们可以通过这里面去，在这里面是通过依赖注入引入这个 commit service。我们进行一个简单的操作，比如说在这里面我们进行一个字符串类型转换，这个 long 类型的一个操作。那么在这里面操作的过程中，我们可以先简单执行一下我们的单元测试，让它能正常跑通过，我们可以看到它执行成功了以后，它就是对应的返回的 1. 3，我们可能从这里面词很难区分出它的数据类型，但是我们可以看到这个转换的过程我们返回是 long 类型。


那么接下来我们去看一下它在执行的过程中做了哪些操作，我们来这里面加一个断点，同时我们在执行，我们可以看一下我们执行这个过程，好在执行的过程我们可以看到这里面是在 conversion service effective b 里面去做这个 after prodecide 的操作。


这里面我们来先看一下这个创建 conversion service 的过程，好，我们在这里面去跟进去断点，在这里面也跟大家去介绍过，这里面是一些创建 debug conference service，那么在这里面我们要去艾特底色的 convert 机，就是把我们这些常规的这些 convert 添加进去。


好，这是添加我们这些标量的一些数据，这就我们就快速的通过，接下来添加一些集合相关的内容，那么集合相关内容我们也不再去跟进去，这样我们快速的把这些添加完成，那么这个完成以后我们要注的就是我们 regist convert，当然在这里面我们并没有去手工的去注释这convert，所以 convert 为null，所以说我们也就不用观察。
进去这里面我们可以看到它在执行完成以后，整个我们的 being factor 构建完成，那么我们跳过这个断点，好好，现在我们进入 Converse 的操作， convert 操作里面它要注的思想是什么呢？首先第一步它会把我们这个 convert 原始的 source 转换成一个 type descriper，也就是我们的类型描述符，那么我们的目标类型也会转换成一个我们的类型描述符，通过类型描述符去找对应的convert，好，我们跟进去。


在这里面我们可以看到在这里面，对于这个方法，它是一个source，加上我们的来源的类型描述符和我们的目标的类型描述符进行我们的这个转化器的查找。这里面首先是注了一些参数的校验， source time 不能为null，同时 source 也不能为null。


接下来我们去 get convert，通过我们的 source type 和 target type 去找我们的这个 convert 是否存在。在查找 convert 的过程，它会首先构造一个 convert cats key，因为在 convert 比较多的情况下，它可能查到还是比较耗死的，所以说在这里面会进行了一个缓存处理，它构建为这个 cats key 以后，先从我们的 convert cats 里面去查找。
当然第一次执行的时候是找不到这个convert，我们找不到的话需要从我们的 convert 列表里面去查找这个类型，这个查找的类型是比较复杂的，它首先会把我们的 SaaS 和我们的 target 这两个目标，所有的这些继承的类和接口都都构建出来，我们可以看到从这里面我们看一下它这里面的内容。


首先是我们这个来源的看你候选对象，那么来源的候选对象里面，这里面我们知道我们的原始的是一个 string 类型，这里面像 thrillable comparable 和 pair sequence 和 black 的，也就是它所有的这些接口和一些父类都会在这里面体现出来。这样的话在这里面去做一个循环的操作，找到合适的我们的convert。好，我们现在快速的跟进。


好，现在已经找到了这个convert，我们可以看到这个 convert 类型的实现是什么啊？这个 convert 它是，我们从这里面可以看到它其实是一个 convert packs Adapter 的一个适配，它真正的内容是 string toolbar，也就是 string to number convert。对于 string to never convert，它的实现应该是 string too long 的一个实现。现在我们得到这个 convert 以后，它会对 convert 去进行一个去 cats 处理，比如说它得到了 convert 不会null，那么我们在这一次把它放到我们的 cats 缓存里面，以便下次的时候可以快速获取到，这样就得到了convert，这个时候我们的 result 已经获取到了，这里面 result 已经是个 long 类型的123，大家可以重新看到。那么 handler result 它其实在这里面并没有做什么处理，我们跳出，那么现在我们已经得到了我们的对象，那么执行完成，我们快速结束我们的断点，这就是我们在以 convert 转换的一个过程。好了，我们关于 spring convert 的内容我们先介绍到这里，同学们，我们下一节再见。


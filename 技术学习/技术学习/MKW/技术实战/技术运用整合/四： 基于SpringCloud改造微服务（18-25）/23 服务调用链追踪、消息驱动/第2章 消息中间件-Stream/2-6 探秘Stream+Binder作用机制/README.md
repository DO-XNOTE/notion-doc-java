---
title: 2-6 探秘Stream+Binder作用机制
---

# 2-6 探秘Stream+Binder作用机制

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/8f3017ca-27f6-4d76-9414-36713692ffc9/SCR-20240722-bisz.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSGZITIP%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDBqwswugdcNjcfGzKFLz%2FBuGFTnL6nOz8LfVBeUu0qrwIgeedRQ2fo39SFG9kEVn6KsHeJeD%2BhmsPuBya9vW49RroqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDERx6CEpO9iozmLLJyrcA3tt6FRzO3QHgj5%2F2toNAVUl%2F6FIeWRVAyG7klPEbV93RpyqiZ5TDKJAk%2B0jRiR4JiHUrdev0scVHlvt1M8xKwRUrCiNqkBFRS7enJXM4gCu1o3BaHDpDjwjhKS0ipc7UB7T8eEuLv1%2B4GSTntsR3r3bCwOLMTAaa3Fqv7Bt4aMewPbMVMBeBOgYg3Rwe4SXRllkLPYieuJLPHebf%2Bb2YW8%2F%2BOdeRUU3VLX1Fz3OAurgB2HsZzg7Tq9ctGHi4aqQ5WCVvzSrqaDCQReAoUXpK1%2B1LhqdI%2FZsN8XpzdqmkULOKFftPTL9xOr8KPMwou6Zg498V1L5dRC0V1MmWWQWgNRd8h0H6ae5hg6BU1%2FlpiaEF8g3tCpCc1syilhiRm3s%2FetQ5h9y0vt2ABJS%2F0kakoOIvOLOHspLqbPgyKX%2BHNh9Fcedeb%2FgmBev5XJP%2BrsG%2BuCstH77%2Fnft2mKAep%2Fbe6JCIGvjnELl2SMoxP49ZUiE%2FNg8XdVkXmiCBVmLttAaab7IKBnl0175rcUrsDb9Ki4Ig2Y1u0DC0Iwg8AR5eVdS0n039jdhrYyK0ErRIvlf8G66VZwSOsH%2BWSl1C%2FYzQTgWF0dZaZzBu2%2FdDYHrHnIvEDKDCHNxdd9ehS9kMNu5%2F9IGOqUBqfJQY3SG4Q%2F09PQO6JkOeITxLsaH6SXtnxgNsCvlcryZCAeKfny60y6NpAFNJXtRFrpTsnxnEKMNhOwSBiS4pIgEzAC4R2xjFofiIeqxGcL%2FtOsfHnMraGujJMTFVSuj4n3miiOAlurZcEihZWbp6Pqgc184YMWF66LnhBJ5DuKfEEBxR%2F772HdFUdMe8nuJC9taOvmiLF7vZr6a0AmoAoBd5hOi&X-Amz-Signature=8fd523f4efda2f8c8d37fcecefb687783e45e866bf082a73dfd5f0de73266565&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/828e6702-ed42-4516-9a0f-a934aebcbad5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSGZITIP%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDBqwswugdcNjcfGzKFLz%2FBuGFTnL6nOz8LfVBeUu0qrwIgeedRQ2fo39SFG9kEVn6KsHeJeD%2BhmsPuBya9vW49RroqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDERx6CEpO9iozmLLJyrcA3tt6FRzO3QHgj5%2F2toNAVUl%2F6FIeWRVAyG7klPEbV93RpyqiZ5TDKJAk%2B0jRiR4JiHUrdev0scVHlvt1M8xKwRUrCiNqkBFRS7enJXM4gCu1o3BaHDpDjwjhKS0ipc7UB7T8eEuLv1%2B4GSTntsR3r3bCwOLMTAaa3Fqv7Bt4aMewPbMVMBeBOgYg3Rwe4SXRllkLPYieuJLPHebf%2Bb2YW8%2F%2BOdeRUU3VLX1Fz3OAurgB2HsZzg7Tq9ctGHi4aqQ5WCVvzSrqaDCQReAoUXpK1%2B1LhqdI%2FZsN8XpzdqmkULOKFftPTL9xOr8KPMwou6Zg498V1L5dRC0V1MmWWQWgNRd8h0H6ae5hg6BU1%2FlpiaEF8g3tCpCc1syilhiRm3s%2FetQ5h9y0vt2ABJS%2F0kakoOIvOLOHspLqbPgyKX%2BHNh9Fcedeb%2FgmBev5XJP%2BrsG%2BuCstH77%2Fnft2mKAep%2Fbe6JCIGvjnELl2SMoxP49ZUiE%2FNg8XdVkXmiCBVmLttAaab7IKBnl0175rcUrsDb9Ki4Ig2Y1u0DC0Iwg8AR5eVdS0n039jdhrYyK0ErRIvlf8G66VZwSOsH%2BWSl1C%2FYzQTgWF0dZaZzBu2%2FdDYHrHnIvEDKDCHNxdd9ehS9kMNu5%2F9IGOqUBqfJQY3SG4Q%2F09PQO6JkOeITxLsaH6SXtnxgNsCvlcryZCAeKfny60y6NpAFNJXtRFrpTsnxnEKMNhOwSBiS4pIgEzAC4R2xjFofiIeqxGcL%2FtOsfHnMraGujJMTFVSuj4n3miiOAlurZcEihZWbp6Pqgc184YMWF66LnhBJ5DuKfEEBxR%2F772HdFUdMe8nuJC9taOvmiLF7vZr6a0AmoAoBd5hOi&X-Amz-Signature=8aeae1922e817af752448e4892aa35e195817cf4d5f532acdbef9e82f297208a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/d1460656-3d70-4abc-97c5-947ddd46e80c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSGZITIP%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDBqwswugdcNjcfGzKFLz%2FBuGFTnL6nOz8LfVBeUu0qrwIgeedRQ2fo39SFG9kEVn6KsHeJeD%2BhmsPuBya9vW49RroqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDERx6CEpO9iozmLLJyrcA3tt6FRzO3QHgj5%2F2toNAVUl%2F6FIeWRVAyG7klPEbV93RpyqiZ5TDKJAk%2B0jRiR4JiHUrdev0scVHlvt1M8xKwRUrCiNqkBFRS7enJXM4gCu1o3BaHDpDjwjhKS0ipc7UB7T8eEuLv1%2B4GSTntsR3r3bCwOLMTAaa3Fqv7Bt4aMewPbMVMBeBOgYg3Rwe4SXRllkLPYieuJLPHebf%2Bb2YW8%2F%2BOdeRUU3VLX1Fz3OAurgB2HsZzg7Tq9ctGHi4aqQ5WCVvzSrqaDCQReAoUXpK1%2B1LhqdI%2FZsN8XpzdqmkULOKFftPTL9xOr8KPMwou6Zg498V1L5dRC0V1MmWWQWgNRd8h0H6ae5hg6BU1%2FlpiaEF8g3tCpCc1syilhiRm3s%2FetQ5h9y0vt2ABJS%2F0kakoOIvOLOHspLqbPgyKX%2BHNh9Fcedeb%2FgmBev5XJP%2BrsG%2BuCstH77%2Fnft2mKAep%2Fbe6JCIGvjnELl2SMoxP49ZUiE%2FNg8XdVkXmiCBVmLttAaab7IKBnl0175rcUrsDb9Ki4Ig2Y1u0DC0Iwg8AR5eVdS0n039jdhrYyK0ErRIvlf8G66VZwSOsH%2BWSl1C%2FYzQTgWF0dZaZzBu2%2FdDYHrHnIvEDKDCHNxdd9ehS9kMNu5%2F9IGOqUBqfJQY3SG4Q%2F09PQO6JkOeITxLsaH6SXtnxgNsCvlcryZCAeKfny60y6NpAFNJXtRFrpTsnxnEKMNhOwSBiS4pIgEzAC4R2xjFofiIeqxGcL%2FtOsfHnMraGujJMTFVSuj4n3miiOAlurZcEihZWbp6Pqgc184YMWF66LnhBJ5DuKfEEBxR%2F772HdFUdMe8nuJC9taOvmiLF7vZr6a0AmoAoBd5hOi&X-Amz-Signature=508a3c1252c22165a1b38de396ea9707f5bc160efbed751f042efc8557bd7cce&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[上一节我们通过一个实际业务场景，了解了消息组件如何做流量削峰，这一节我们来深入学习下Stream是如何对接外部的消息中间件的](/05f59d36344e486c9889853acfc258fe)，这就要讲到Stream底层的Binder机制。在Stream体系架构一节中我们了解到，Stream为每种不同类型的消息组件开发了一套Binder作为适配器，从而打通消息中间件和Stream的Input、Output通道之间连接。接下来，我们就拿最常用的RabbitMQ来举例，深入研究RabbitMQ的Binder适配方案源码。本节内容比较晦涩，建议一鼓作气一次读完，读完就忘，忘了再读，如此反复，神功必成。

**Binder来自何方**

了解这个底层组件之前，我们先来看下它师出何门何派。大家打开最近的Demo项目中的pom文件，找到Stream的依赖 spring-cloud-starter-stream-rabbit，我们从开发工具点击这个依赖项的“artifact”标签进到stream-rabbit的pom文件，发现里面只有一个依赖项：

```java
<dependencies>
				<dependency>
								<groupId>org.springframework.cloud</groupId>
								<artifactId>spring-cloud-stream-binder-rabbit</artifactId>
				</dependency>
</dependencies>
```

没错，这个就是真身了！这个binder-rabbit就是Stream用来适配RabbitMQ的底层组件，它的所有源代码都在Spring Cloud的Git仓库中：

```java
https://github.com/spring-cloud/spring-cloud-stream-binder-rabbit
```

当我们将一个Binder组件引入Pom文件之后，它将在项目启动的时候进行自动装配，分别对我们代码中声明的@Input，@Output和@StreamListener注解进行解析，并绑定到对应的通信通道。下面我们来看一看RabbitMQ的核心加载流程，这部分源码略显晦涩，建议大家到上面给出的Git地址上把源码拉到本地，边看图文边比照源码加深理解。

**Stream Core层的装配**

Stream Core子模块主要负责初始化一些核心类，触发Stream内部的资源加载，比如说绑定生产者和消费者，解析StreamListener注解。这个装配过程由BindingServiceConfiguration承接。我们挑选其中的几个核心流程看一下：

**解析@StreamListener注解**

在之前的Demo中，我们在消费者这一端的方法上添加了@StreamListener注解，使其可以获取外部消息组件的消息，那么这个注解是怎么被Stream识别的呢？我们知道Spring中的注解都需要一个对应的解析器来执行具体业务，对于@StreamListener注解来说，它的对应解析器就是StreamListenerAnnotationBeanPostProcessor，在这个类中定义了一个变量，专门用来存储所有声明@StreamListener注解的消费者列表：

```java
private final MultiValueMap<String, StreamListenerHandlerMethodMapping>

mappedListenerMethods = new LinkedMultiValueMap<>();
```

那Stream是如何找到所有@StreamListner注解并添加到上面这个map结构中的呢？我们看下这个类所实现的接口就明白了，它实现了BeanPostProcessor接口，并且覆盖了postProcessAfterInitialization方法。这个方法其实是Spring中的Bean生命周期管理的一个环节，具体来说就是在Spring完成每个Bean的初始化之后，会调用该方法执行一段逻辑。我将这段方法摘取了出来，添加了部分注释，这段代码的主要作用就是找到所有@StreamListener的注解对象

```java
@Override
    public final Object postProcessAfterInitialization(Object bean, final String beanName) throws BeansException {

				// 对每个托管到Spring的Bean，先通过反射拿到class对象
        Class<?> targetClass = AopUtils.isAopProxy(bean) ? AopUtils.getTargetClass(bean) : bean.getClass();
				// 再通过反射获取该类声明的方法
        Method[] uniqueDeclaredMethods = ReflectionUtils.getUniqueDeclaredMethods(targetClass);

        for (Method method : uniqueDeclaredMethods) {
						// 找出那些添加了@StreamListener注解的方法
            StreamListener streamListener = AnnotatedElementUtils.findMergedAnnotation(method, StreamListener.class);
            if (streamListener != null && !method.isBridge()) {
								// streamListenerCallbacks是一个Runnable的数组
								// 这里会将符合条件的方法转为一个Runnable对象，添加到数组中
                this.streamListenerCallbacks.add(() -> {
										// 断言检测，该方法不能同时定义@Input注解和@StreamListener注解
                    Assert.isTrue(method.getAnnotation(Input.class) == null, StreamListenerErrorMessages.INPUT_AT_STREAM_LISTENER);
                    this.doPostProcess(streamListener, method, bean);
                });
            }
        }
        return bean;
    }
```


通过上面的逻辑，在Spring加载Bean的时候，Stream就找出了所有标注的@StreamListener的消费者方法，然后这些消费者被装进一个个Runnable线程对象中，等待后面启动线程对象并开启消息监听。

这个Runnable线程对象将会在解析器内的afterSingletonsInstantiated方法中被执行（这里涉及到Spring的Bean初始化生命周期），在这个阶段就启动了消息监听。同学们感兴趣的话可以到这个方法中看一下监听器的启动流程，这部分就留给同学们自由发挥，我们就不再展开讲解了，不过我觉得倒是可以趁这个机会回顾一下Spring中的实例化流程，前面的postProcessAfterInitialization和afterSingletonsInstantiated两个方法都是借助Spring的Bean生命周期管理按照指定的顺序执行的，我这里抽出了几个关键环节一起看一下Bean的实例化：通过构造器或者工厂方法等创建一个实例执行一系列的Aware接口：这些接口大家在工作中应该经常会见到，比如BeanClassLoaderAware、ApplicationContextAware等实现了Aware接口的类，如果你的Bean继承了这些接口并实现了对应的回调方法，那么Spring就会在Bean初始化的相应阶段触发回调方法。刚刚我们提到的在@StreamListener加载流程中被调用postProcessAfterInitialization方法就是在这个阶段执行的

```java
BeanPostProcessor.postProcessBeforeInitialization：在Bean初始化之前执行的操作

BeanPostProcessor.postProcessAfterInitialization：在Bean初始化之后执行的操作

SmartInitializingSingleton.afterSingletonsInstantiated：在所有Bean都完成实例化之后调用

SmartLifecycle.start：当这一步执行完成以后，就可以认为容器已经成功加载了这个Bean

SmartLifecycle.stop和DisposableBean.destroy：这两个步骤在应用关闭的时候会执行（Application.close）
```

**绑定消费者**

看完了上面@StreamListener复杂的加载流程，接下来我们了解下Stream是如何将一个Consumer绑定到对应通道中的。这个过程在BindingService类中实现，具体方法为bindConsumer，它的方法签名是这样的：

```java
public <T> Collection<Binding<T>> bindConsumer(T input, String inputName)
```

第一个参数input是Stream封装好的一个Channel对象，第二个参数inputName是我们定义@Input注解时给定的通道名称。我们先来看看方法的前半部分

```java
Collection<Binding<T>> bindings = new ArrayList<>();

        // 获取底层用来适配外部消息组件的RabbitMessageChannelBinder
        Binder<T, ConsumerProperties, ?> binder = getBinder(inputName, input.getClass());
        // 读取Consumer端的配置信息
        ConsumerProperties consumerProperties = this.bindingServiceProperties.getConsumerProperties(inputName);
        // 读取扩展配置信息
        if (binder instanceof ExtendedPropertiesBinder) {
            Object extension = ((ExtendedPropertiesBinder) binder).getExtendedConsumerProperties(inputName);
            ExtendedConsumerProperties extendedConsumerProperties = new ExtendedConsumerProperties(extension);
            BeanUtils.copyProperties(consumerProperties, extendedConsumerProperties);
            consumerProperties = extendedConsumerProperties;
        }
        // 对属性值进行验证
        validate(consumerProperties);
        上半部分的代码主要做了两件事儿，第一件事是加载底层Binder类用来与外部消息组件通信，二是获取Consumer属性值。第二步中的属性值并非所有Consumer的属性全集，而仅仅是当前InputName对应的属性。
        我们接下来看后半部分的代码：
        // 从配置文件中获取Input绑定的Topic，就是下面这行配置的destination值
        // spring.cloud.stream.bindings.input.destination=broadcast
        // 一个Input可能被绑定到多个Topic中，每个Topic以逗号隔开返回成String
        String bindingTarget = this.bindingServiceProperties.getBindingDestination(inputName);
        if (consumerProperties.isMultiplex()) {
            bindings.add(doBindConsumer(input, inputName, binder, consumerProperties, bindingTarget));
        } else {
            // 一般逻辑都进到else分支来
            // 先把上一步中逗号隔开的Topic拆分成一个String数组
            String[] bindingTargets = StringUtils.commaDelimitedListToStringArray(bindingTarget);
            // 把每个Topic绑定到Binder上
            for (String target : bindingTargets) {
                Binding<T> binding = input instanceof PollableSource ? doBindPollableConsumer(input, inputName, binder, consumerProperties, target) : doBindConsumer(input, inputName, binder, consumerProperties, target);
                bindings.add(binding);
            }
        }
        // 这三行是打酱油的逻辑
        bindings = Collections.unmodifiableCollection(bindings);
        this.consumerBindings.put(inputName, new ArrayList<>(bindings));
        return bindings;
```

上面的代码做了两件事请，第一件是找到每个@Input通道在配置文件中所指定的Topic，第二件就是将Topic绑定到Binder上，搭建了Stream业务代码和外部消息组件的通道。

RabbitMessageChannelBinder是对接RabbitMQ核心适配器，上面看到了BindingService是如何绑定消费者到外部消息组件的，那么这里底层调用的就是RabbitMessageChannelBinder这个类。

**绑定生产者**

这一步和绑定消费者的步骤一样，同样是在BindingService类中实现的，具体方法为bindProducer。同学们可以沿着同样的方式自己去读一下源码。我强烈建议大家在这两个方法上打一个断点，用debug模式启动项目，跟着注解走一遍流程。这是最快速熟悉项目结构的方式。

**@EnableBinding注解的作用**

@EnableBinding是带主角光环的，它会将Stream的内部通道（也就是我们使用@Input和@Output注解定义的通道对象）绑定到外部消息组件上。在@EnableBinding注解中引入了一个配置类BindingBeansRegistrar，专门用来注册@EnableBinding注解的类，它的核心代码部分如下：

```java

public void registerBeanDefinitions (AnnotationMetadata metadata, BeanDefinitionRegistry registry) {
            // 获取@EnableBinding注解中定义的属性值
            AnnotationAttributes attrs = AnnotatedElementUtils.getMergedAnnotationAttributes(ClassUtils.resolveClassName(metadata.getClassName(), null), EnableBinding.class);

            // collectClasses方法会将@EnableBinding注解中配置的类名转化成Class对象
            for (Class<?> type : collectClasses(attrs, metadata.getClassName())) {
                // 如果这个类没有被重复注册过，则执行注册逻辑
                if (!registry.containsBeanDefinition(type.getName())) {
                    // 注册当前类中定义的@Input和@Output注解的对象
                    BindingBeanDefinitionRegistryUtils.registerBindingTargetBeanDefinitions(type, type.getName(), registry);
                    // 注册当前类 
                    BindingBeanDefinitionRegistryUtils.registerBindingTargetsQualifiedBeanDefinitions(ClassUtils.resolveClassName(metadata.getClassName(), null), type, registry);

                }
            }
        }
```

**小结**

这一小节我们深入了解了Stream的Binder机制，下一节我们先复习一下发布订阅模型，再基于这个模型做一个消息广播的小Demo

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e069fd72-5e60-4110-ba60-8e1c8fc8f834/2020-09-17_061434.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XSGZITIP%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225813Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDBqwswugdcNjcfGzKFLz%2FBuGFTnL6nOz8LfVBeUu0qrwIgeedRQ2fo39SFG9kEVn6KsHeJeD%2BhmsPuBya9vW49RroqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDERx6CEpO9iozmLLJyrcA3tt6FRzO3QHgj5%2F2toNAVUl%2F6FIeWRVAyG7klPEbV93RpyqiZ5TDKJAk%2B0jRiR4JiHUrdev0scVHlvt1M8xKwRUrCiNqkBFRS7enJXM4gCu1o3BaHDpDjwjhKS0ipc7UB7T8eEuLv1%2B4GSTntsR3r3bCwOLMTAaa3Fqv7Bt4aMewPbMVMBeBOgYg3Rwe4SXRllkLPYieuJLPHebf%2Bb2YW8%2F%2BOdeRUU3VLX1Fz3OAurgB2HsZzg7Tq9ctGHi4aqQ5WCVvzSrqaDCQReAoUXpK1%2B1LhqdI%2FZsN8XpzdqmkULOKFftPTL9xOr8KPMwou6Zg498V1L5dRC0V1MmWWQWgNRd8h0H6ae5hg6BU1%2FlpiaEF8g3tCpCc1syilhiRm3s%2FetQ5h9y0vt2ABJS%2F0kakoOIvOLOHspLqbPgyKX%2BHNh9Fcedeb%2FgmBev5XJP%2BrsG%2BuCstH77%2Fnft2mKAep%2Fbe6JCIGvjnELl2SMoxP49ZUiE%2FNg8XdVkXmiCBVmLttAaab7IKBnl0175rcUrsDb9Ki4Ig2Y1u0DC0Iwg8AR5eVdS0n039jdhrYyK0ErRIvlf8G66VZwSOsH%2BWSl1C%2FYzQTgWF0dZaZzBu2%2FdDYHrHnIvEDKDCHNxdd9ehS9kMNu5%2F9IGOqUBqfJQY3SG4Q%2F09PQO6JkOeITxLsaH6SXtnxgNsCvlcryZCAeKfny60y6NpAFNJXtRFrpTsnxnEKMNhOwSBiS4pIgEzAC4R2xjFofiIeqxGcL%2FtOsfHnMraGujJMTFVSuj4n3miiOAlurZcEihZWbp6Pqgc184YMWF66LnhBJ5DuKfEEBxR%2F772HdFUdMe8nuJC9taOvmiLF7vZr6a0AmoAoBd5hOi&X-Amz-Signature=43c53ea7738871d53072749372972a52411340b995bc0a471e372afaca0c6521&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





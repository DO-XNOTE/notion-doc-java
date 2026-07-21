---
title: 3-13 可靠性投递落地-ESJOB定时任务讲解-1
---

# 3-13 可靠性投递落地-ESJOB定时任务讲解-1

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/aff68bf9-13b8-4c35-b2a3-2ab94ce15219/SCR-20240806-rxnn.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMMOJCUQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225306Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFEdGB6adSwBKbYijrIZdVAQPmXt9BhWfJKajno6F7glAiEAziAtF6gg5WtJXsfECb9a4aMjbesZSZg0bpWGMoXqQGYqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCKr9EBys%2Fi4lXQLNyrcA2AxKAPQHH0JbQgu1c%2FLl7K5SEUT1y0LFWFjMrNIilWk6dP4KigwAX74ETF6Gk6KW381dYG2jFG4%2FLKR7YuzFZYvMlKnfuV0Z9EHKDBSRv0auGdcATSk77dk1iqlU9bmUbsnCVvuH8QbvqHLGK9ftvYXghXmf2uRLS6Ke505XyuzC%2FBn2ECT%2BzGovsw5jekEwfbd7JMdOouNgMBAic7Q%2BB%2FElknfWQ%2BW8Pg2U3k4KE2hiLe8BgNId15R75lH0csNu5yNk3JfeWQ7jwyVu%2B1qLPQLx5%2F5cRQGZubBU10XYfTXgLzwoM%2F%2Bsae8nnAWqguJdyi%2F7i4uP2tgPas0Trbq7EUKvJNle9xtqAsBJUVq%2FI90qz7E6QSOiU2dba1aIVPLuGFjhjJqMn49ZOewWlAiJq2rFnK%2FcvMdEk9C0rNCg5kvPtUG7uIfHQ%2FWTePgipRCG3Cry16nKWevQb1WhQ%2FV86AqA9%2F4Nr5ih83GcIrIXNCwvbNMcRwTdgHGbDUowbcMUZAf3rJRW5v4UCOKvTq7gzmjGnBuygmhd2fIZz5OmCBAWcdwXra8qLBWkmqEDS9oXs54VsKuixrughVa9wJCUcQ1k1a3Adv705EbNOFKHj4I3MHdKFjS4CFiFzurMN63%2F9IGOqUBTmlBxOC95DC7H52HvoPqlDwOUfxG39y%2BFDbD18hVsEoBjYUEibkYCX28K0oNXmK%2BAaPj46QK9ZMJuLc5009XF6jJK7yCdevJQM6dqWbGBBTug7i79Gz2ioczEaMVlPyuYDM2PjwKcKxfBL1WLK4smgQe%2Fc9IByyDicCBF2CN%2FpxhPV%2FIf1dcBLp%2BeSR%2By6cNMJspF0%2F2zffxevrJEF4v4wBionx2&X-Amz-Signature=a817cd367d0a3ecdf5b7d9b1c82729bb3c5989a4f02f09be9127398984b0680a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/a4962d78-728c-4d67-a8c7-afd907e260e1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMMOJCUQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225306Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFEdGB6adSwBKbYijrIZdVAQPmXt9BhWfJKajno6F7glAiEAziAtF6gg5WtJXsfECb9a4aMjbesZSZg0bpWGMoXqQGYqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCKr9EBys%2Fi4lXQLNyrcA2AxKAPQHH0JbQgu1c%2FLl7K5SEUT1y0LFWFjMrNIilWk6dP4KigwAX74ETF6Gk6KW381dYG2jFG4%2FLKR7YuzFZYvMlKnfuV0Z9EHKDBSRv0auGdcATSk77dk1iqlU9bmUbsnCVvuH8QbvqHLGK9ftvYXghXmf2uRLS6Ke505XyuzC%2FBn2ECT%2BzGovsw5jekEwfbd7JMdOouNgMBAic7Q%2BB%2FElknfWQ%2BW8Pg2U3k4KE2hiLe8BgNId15R75lH0csNu5yNk3JfeWQ7jwyVu%2B1qLPQLx5%2F5cRQGZubBU10XYfTXgLzwoM%2F%2Bsae8nnAWqguJdyi%2F7i4uP2tgPas0Trbq7EUKvJNle9xtqAsBJUVq%2FI90qz7E6QSOiU2dba1aIVPLuGFjhjJqMn49ZOewWlAiJq2rFnK%2FcvMdEk9C0rNCg5kvPtUG7uIfHQ%2FWTePgipRCG3Cry16nKWevQb1WhQ%2FV86AqA9%2F4Nr5ih83GcIrIXNCwvbNMcRwTdgHGbDUowbcMUZAf3rJRW5v4UCOKvTq7gzmjGnBuygmhd2fIZz5OmCBAWcdwXra8qLBWkmqEDS9oXs54VsKuixrughVa9wJCUcQ1k1a3Adv705EbNOFKHj4I3MHdKFjS4CFiFzurMN63%2F9IGOqUBTmlBxOC95DC7H52HvoPqlDwOUfxG39y%2BFDbD18hVsEoBjYUEibkYCX28K0oNXmK%2BAaPj46QK9ZMJuLc5009XF6jJK7yCdevJQM6dqWbGBBTug7i79Gz2ioczEaMVlPyuYDM2PjwKcKxfBL1WLK4smgQe%2Fc9IByyDicCBF2CN%2FpxhPV%2FIf1dcBLp%2BeSR%2By6cNMJspF0%2F2zffxevrJEF4v4wBionx2&X-Amz-Signature=fb9cb113098abda4454a46bd78be31f1b544441836dfea89be18191c4df48aa0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

这节课呢，我们花点时间快速的去把当当朗的这个 elected job 跟大家来讲一讲，可能有些小伙伴们已经学过，或者已经在工作中用到了其实现在的一些分布式定时任务，如果你自己公司内部没有去自研的话，那大多数都会去使用 elected job 或者是 XXL job 这两种，那如果说你公司自研的话，可能有自己的一些需求，那我们在这里废话不多说，老师已经准备好了一个工程就是 ES 杠job。那这个工程呢？到时候都会提交到我们的这个慕课网的 IT 上。


好了，那我们来看一看这个到底怎么去用。用之前我们先看一下它对应的这个 Pom 文件依赖在这里，老师已经准备好了，我们把它换成二点幺点五，因为我们现在用的都是 215 这个版本，然后我们来看一看它最关键的依赖包有哪些。首先比较关键的依赖包我们来找一下看，就是这两个，

```java
     <!--  elastic-job dependency -->
	    <dependency>
	      <groupId>com.dangdang</groupId>
	      <artifactId>elastic-job-lite-core</artifactId>
	      <version>${elastic-job.version}</version>
	    </dependency>
	    <dependency>
	      <groupId>com.dangdang</groupId>
	      <artifactId>elastic-job-lite-spring</artifactId>
	      <version>${elastic-job.version}</version>
	    </dependency>
```

第一个就是我们的 electic job 杠 lite 杠 core 这个核心包，还有一个是跟 spring 整合的这么一个包。接下来就是关于 spring 的一些这个配置了，没什么可说的，

那既然有了这个东西，我们来一起说一说。

这两个包引入了之后，那么你就可以去用当网的 elastic-job 了，并且你可以在 spring boot 工程里边你就可以写配置，就是在 application 点 properties 里边，在这里老师写了关于什么zookeeper 的配置，以及关于我们的 ES-job 的配置，还有关于我们对应着可能会有一些 spring 的一些配置。


那接下来我们就开始去讲这个 es job 了。首先我们这个 es job 从哪入手？ es job 它是属于分布式定时任务。什么是分布式定时任务？也就是说当我们一个 job 执行在集群中一个 job 执行，那其他的 job 可能就执行不了。或者是说这个 job 能够帮我们去分片去处理。比如说我的一个数据库里边有 100 条记录，那我可能有 10 个应用程序同时启动，那我们可以做到每一个应用程序只处理其中的 1/ 10，也就是说每一个应用程序只处理 10 条数据，当然你得去做合理的分片去设置才可以在这里跟小伙伴们把这个概念说清楚。


那 **ES job 既然是分布式的，那所以说它肯定是依赖一些分布式的组件，能够保障我们类似于分布式锁的概念。所以说在 ES job 里边它用 ZK 去做分布式锁，原因就是因为对于定时任务而言，它的这个并发也不是很高，像我们高并发的场景肯定不会去选择 CK 去做分布式锁，肯定会用一些像高性能的 Redis 去做一些分布式锁的处理。**


OK，那他既然选择我们的 ZK 去做分布式锁的话，所以说它里边肯定是要依赖 ZK 的，那第一件事情就是要加载 ZK 的一些内容，那你看我的这个application，它里边就是一个普通的 spring boot 工程，然后他帮我去扫描Com，点 b f s y，点 e s shop，点星点service。你帮我去扫描什么task，这里边就做一个最基础的配置。那我们首先来看它对应的比较关键的configuration，就是 config 这块儿， annotation 这块儿先不用管，先看这个config。


ES job 给我们提供 3 种 job 类型，第一种 job 类型叫做 simple job，也就是我们实际工作中用的最多的，其实就是简单任务。第二种 job 叫做 data flow，就是流式处理的，它可能不间断的循环的去到某一个地方去拉取数据，然后去执行。第三种方式叫做 script job script 就是利用脚本的方式帮我们去执行，就是任务。那一般来讲工作用的比较多的就是 simple 跟 data flow。关于说脚本这块呢，老师其实实际工作中也没有遇到过，那我们就重点讲这两种就好了。好了，那第一件事情它最关键的就是既然依赖于ZK，所以说它一定会要做 ZK 的一些处理，比如说注册对不对？所以说我们首先要看的就是我们的reject。

Free central configure registry center.

这个他做了什么事情？我们来最大化来看一看这个代码。 configuration 标识，它是一个配置文件，或者是一个 Xmail 文件，然后它加了一个注解，叫做 at conditional on expression，就是一个正则表达式的匹配。如果说你满足这个，那我才会去帮你去加载这个配置文件。如果说你连这个表达式都不满足，那我帮你加载什么，我就不帮你加载了，那什么意思？这里边设置了ZK，就是 zookeeper 点 address 点 lens 大于0，就是是否你的配置文件里有这行配置，并且它的 lens 是大于 0 的，如果是大于 0 的，我才帮你去加载，对吧？那它到底大不大于0？我们来看一看 practice 里边是不是 ZK 点 address 已经有了，对吧？然后它的 nice 你知道这个很明显是一个数组，用逗号分隔的，那这个就是我们的租 keeper 的配置了，租 keeper 的地址就是幺九二点幺六八点幺幺幺2181，然后以及 112 的2181， 113 的2181。有了这个，所以说那个配置会帮我们去做。


然后这里边关于 zk 的四个配置，就是比如说它的 namespace 工作空间，这个 namespace 其实你可以理解为就是根节点，然后 timeout 时间 10 秒钟， session time out 10 秒钟，然后它的 Max Retry 最大三次重试。


那有了这几个配置之后，那我期望我的这个 registry center config 这个配置文件，把我的配置读取出来，然后创建 ZK registry center 这个对象，这个 register center 是我们什么？是我们当网给我们封装的 ZK 的一个注册中心，你看Com，点down，down，点 d framework，点job，点registry、点 zookeeper registry center。

```java
package com.bfxy.esjob.config;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.boot.autoconfigure.condition.ConditionalOnExpression;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import com.dangdang.ddframe.job.reg.zookeeper.ZookeeperConfiguration;
import com.dangdang.ddframe.job.reg.zookeeper.ZookeeperRegistryCenter;

@Configuration
@ConditionalOnExpression("'${zookeeper.address}'.length() > 0")
public class RegistryCenterConfig {
	
	/**
	 * 	把注册中心加载到spring 容器中
	 * @return
	 */
	@Bean(initMethod = "init")
	public ZookeeperRegistryCenter registryCenter(@Value("${zookeeper.address}") final String serverLists, 
			@Value("${zookeeper.namespace}") final String namespace, 
			@Value("${zookeeper.connectionTimeout}") final int connectionTimeout, 
			@Value("${zookeeper.sessionTimeout}") final int sessionTimeout,
			@Value("${zookeeper.maxRetries}") final int maxRetries) {
		ZookeeperConfiguration zookeeperConfiguration = new ZookeeperConfiguration(serverLists, namespace);
		zookeeperConfiguration.setConnectionTimeoutMilliseconds(connectionTimeout);
		zookeeperConfiguration.setSessionTimeoutMilliseconds(sessionTimeout);
		zookeeperConfiguration.setMaxRetries(maxRetries);
		
		return new ZookeeperRegistryCenter(zookeeperConfiguration);
		
	}
	
	
}
```

然后这个方法就是在初始化的时候会调用它的init。方法是什么意思？就说明这个 keeper just center 它里边一定会有这个 init 方法，我们可以点进去看一下。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/c5c1ab19-0b54-4eb5-a38c-a0dbf6a57837/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMMOJCUQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225306Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFEdGB6adSwBKbYijrIZdVAQPmXt9BhWfJKajno6F7glAiEAziAtF6gg5WtJXsfECb9a4aMjbesZSZg0bpWGMoXqQGYqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCKr9EBys%2Fi4lXQLNyrcA2AxKAPQHH0JbQgu1c%2FLl7K5SEUT1y0LFWFjMrNIilWk6dP4KigwAX74ETF6Gk6KW381dYG2jFG4%2FLKR7YuzFZYvMlKnfuV0Z9EHKDBSRv0auGdcATSk77dk1iqlU9bmUbsnCVvuH8QbvqHLGK9ftvYXghXmf2uRLS6Ke505XyuzC%2FBn2ECT%2BzGovsw5jekEwfbd7JMdOouNgMBAic7Q%2BB%2FElknfWQ%2BW8Pg2U3k4KE2hiLe8BgNId15R75lH0csNu5yNk3JfeWQ7jwyVu%2B1qLPQLx5%2F5cRQGZubBU10XYfTXgLzwoM%2F%2Bsae8nnAWqguJdyi%2F7i4uP2tgPas0Trbq7EUKvJNle9xtqAsBJUVq%2FI90qz7E6QSOiU2dba1aIVPLuGFjhjJqMn49ZOewWlAiJq2rFnK%2FcvMdEk9C0rNCg5kvPtUG7uIfHQ%2FWTePgipRCG3Cry16nKWevQb1WhQ%2FV86AqA9%2F4Nr5ih83GcIrIXNCwvbNMcRwTdgHGbDUowbcMUZAf3rJRW5v4UCOKvTq7gzmjGnBuygmhd2fIZz5OmCBAWcdwXra8qLBWkmqEDS9oXs54VsKuixrughVa9wJCUcQ1k1a3Adv705EbNOFKHj4I3MHdKFjS4CFiFzurMN63%2F9IGOqUBTmlBxOC95DC7H52HvoPqlDwOUfxG39y%2BFDbD18hVsEoBjYUEibkYCX28K0oNXmK%2BAaPj46QK9ZMJuLc5009XF6jJK7yCdevJQM6dqWbGBBTug7i79Gz2ioczEaMVlPyuYDM2PjwKcKxfBL1WLK4smgQe%2Fc9IByyDicCBF2CN%2FpxhPV%2FIf1dcBLp%2BeSR%2By6cNMJspF0%2F2zffxevrJEF4v4wBionx2&X-Amz-Signature=dcb6fc1c2f3a097e0b080cdabdf018862c07ba88b555b92d7f43e4eb0c76aac3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

好了，那我们来点进去看一看它有没有以内的方法。这是它底层代码，就是当网的这个底层的这个 ES job，其实整个这个 ES job 代码也没多少。其实我建议初学者有兴趣的话可以看一看在当当网的这个整个怎么去实现的，看一看是不是跟你想的一样，其实你可以自己先想一想这个东西应该怎么去实现，我们去找到 init 是不是？你看这就有一个 init 方法，这个 init 方法初始化的时候干什么呀？它底层用的是朱 paper 的一个库瑞特阿帕奇的一个 crate 框架，用的 criter from work 去创建了连接，然后创建这个 build 对象，对吧？然后对它进行一些设置，比如说 time out、session， time out，connect， time out 以及 author 认证，对吧？就做一些初始化的操作，然后把这个我们的client，这 client 就是谁，就是我们自己的这个 reader framework 去做一个start，对吧？你看这个初始化的工作其实很简单，就是相当于把我们阿帕奇的 crater from mock factory 给客户端去做一个初始化，回过头来我们来看一看这里边都有哪些配置呢？比如说 at value address，对吧？我们的地址还有 namespace time out 以及 session time out 和 Max retry，就这 4 个配置项都帮我们去读取出来。


然后在 new 这个我们的这个 zookeeper configuration 的时候会去用到，看见了都去设置好了之后，把我们的这个 configuration 这个类给它扔到主 paper registry center 里，然后返回并注入给我们的 spring 容器，那这个对象就已经搞定了。这是第一步作为一个注册。


第一步，注册好了我们的这个朱 keeper 它的这个 registry center 以后，


第二步，做什么事情。第二步其实你就要比如说看你用什么样的job，比如说你用 simple job 就是最简单的job，对不对？那我们来打开我们最简单的job，看看它里边怎么去做的。最简单的 job 它也是一个configuration，

[file](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/3dff990d-0950-49f7-a297-07f2aeb40303/MySimpleJobConfig.java?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMMOJCUQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225306Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFEdGB6adSwBKbYijrIZdVAQPmXt9BhWfJKajno6F7glAiEAziAtF6gg5WtJXsfECb9a4aMjbesZSZg0bpWGMoXqQGYqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCKr9EBys%2Fi4lXQLNyrcA2AxKAPQHH0JbQgu1c%2FLl7K5SEUT1y0LFWFjMrNIilWk6dP4KigwAX74ETF6Gk6KW381dYG2jFG4%2FLKR7YuzFZYvMlKnfuV0Z9EHKDBSRv0auGdcATSk77dk1iqlU9bmUbsnCVvuH8QbvqHLGK9ftvYXghXmf2uRLS6Ke505XyuzC%2FBn2ECT%2BzGovsw5jekEwfbd7JMdOouNgMBAic7Q%2BB%2FElknfWQ%2BW8Pg2U3k4KE2hiLe8BgNId15R75lH0csNu5yNk3JfeWQ7jwyVu%2B1qLPQLx5%2F5cRQGZubBU10XYfTXgLzwoM%2F%2Bsae8nnAWqguJdyi%2F7i4uP2tgPas0Trbq7EUKvJNle9xtqAsBJUVq%2FI90qz7E6QSOiU2dba1aIVPLuGFjhjJqMn49ZOewWlAiJq2rFnK%2FcvMdEk9C0rNCg5kvPtUG7uIfHQ%2FWTePgipRCG3Cry16nKWevQb1WhQ%2FV86AqA9%2F4Nr5ih83GcIrIXNCwvbNMcRwTdgHGbDUowbcMUZAf3rJRW5v4UCOKvTq7gzmjGnBuygmhd2fIZz5OmCBAWcdwXra8qLBWkmqEDS9oXs54VsKuixrughVa9wJCUcQ1k1a3Adv705EbNOFKHj4I3MHdKFjS4CFiFzurMN63%2F9IGOqUBTmlBxOC95DC7H52HvoPqlDwOUfxG39y%2BFDbD18hVsEoBjYUEibkYCX28K0oNXmK%2BAaPj46QK9ZMJuLc5009XF6jJK7yCdevJQM6dqWbGBBTug7i79Gz2ioczEaMVlPyuYDM2PjwKcKxfBL1WLK4smgQe%2Fc9IByyDicCBF2CN%2FpxhPV%2FIf1dcBLp%2BeSR%2By6cNMJspF0%2F2zffxevrJEF4v4wBionx2&X-Amz-Signature=e21807ea26c56a7d0ac1ba8902c8aa5ea239e3be81b0ba0bac362e5678ffadfa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/42cb7a19-8411-4f22-8fce-0e01ae574d7d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMMOJCUQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225306Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFEdGB6adSwBKbYijrIZdVAQPmXt9BhWfJKajno6F7glAiEAziAtF6gg5WtJXsfECb9a4aMjbesZSZg0bpWGMoXqQGYqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCKr9EBys%2Fi4lXQLNyrcA2AxKAPQHH0JbQgu1c%2FLl7K5SEUT1y0LFWFjMrNIilWk6dP4KigwAX74ETF6Gk6KW381dYG2jFG4%2FLKR7YuzFZYvMlKnfuV0Z9EHKDBSRv0auGdcATSk77dk1iqlU9bmUbsnCVvuH8QbvqHLGK9ftvYXghXmf2uRLS6Ke505XyuzC%2FBn2ECT%2BzGovsw5jekEwfbd7JMdOouNgMBAic7Q%2BB%2FElknfWQ%2BW8Pg2U3k4KE2hiLe8BgNId15R75lH0csNu5yNk3JfeWQ7jwyVu%2B1qLPQLx5%2F5cRQGZubBU10XYfTXgLzwoM%2F%2Bsae8nnAWqguJdyi%2F7i4uP2tgPas0Trbq7EUKvJNle9xtqAsBJUVq%2FI90qz7E6QSOiU2dba1aIVPLuGFjhjJqMn49ZOewWlAiJq2rFnK%2FcvMdEk9C0rNCg5kvPtUG7uIfHQ%2FWTePgipRCG3Cry16nKWevQb1WhQ%2FV86AqA9%2F4Nr5ih83GcIrIXNCwvbNMcRwTdgHGbDUowbcMUZAf3rJRW5v4UCOKvTq7gzmjGnBuygmhd2fIZz5OmCBAWcdwXra8qLBWkmqEDS9oXs54VsKuixrughVa9wJCUcQ1k1a3Adv705EbNOFKHj4I3MHdKFjS4CFiFzurMN63%2F9IGOqUBTmlBxOC95DC7H52HvoPqlDwOUfxG39y%2BFDbD18hVsEoBjYUEibkYCX28K0oNXmK%2BAaPj46QK9ZMJuLc5009XF6jJK7yCdevJQM6dqWbGBBTug7i79Gz2ioczEaMVlPyuYDM2PjwKcKxfBL1WLK4smgQe%2Fc9IByyDicCBF2CN%2FpxhPV%2FIf1dcBLp%2BeSR%2By6cNMJspF0%2F2zffxevrJEF4v4wBionx2&X-Amz-Signature=6511e4fa5abef325c4193b94e4d0fd5ecce9e099670ea950870c2b031ea52696&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

然后它需要用到我们刚才看到的那个什么 zookeeper registry center，对吧？注意这个名字一定要跟你的方法名保持一致，因为他们是用方法名字去当成 bin 的 name 的，所以说你在这里边你的 register center 叫这个叫 register center，所以说你在这里边也应该叫做 register center，你叫别的他可能会有问题。

```java
package com.bfxy.esjob.config;

import javax.sql.DataSource;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import com.dangdang.ddframe.job.event.JobEventConfiguration;
import com.dangdang.ddframe.job.event.rdb.JobEventRdbConfiguration;

@Configuration
public class JobEventConfig {

    @Autowired
    private DataSource dataSource;

    @Bean
    public JobEventConfiguration jobEventConfiguration() {
        return new JobEventRdbConfiguration(dataSource);
    }
}
```

OK，好了，有了它之后，然后这里边也有一个叫做 job event configuration，这是干什么的？其实这个也是我们在这里有的，其实我们的当当网的这个 ES job，它提供控制台，能够帮我们去查看。除了提供控制台以外，它能够提供比如说我对于定时任务的一些日志轨迹，它可以做一些链路跟踪，记录一下他每次 job 执行成功了还是执行失败了，能看到一些具体的这个执行的定时任务的一些信息。当然这个他不是说非常非常完善，老师公司其实对这个 ES job 做了一些扩展，把一些定时任务中出现一些关键的、一些异常、一些错误的点都去重新实现了一下，这样的话更有助于在实际生产环境中排查问题。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/5cc18160-3c35-40b0-a666-f57daca819c8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMMOJCUQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225306Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFEdGB6adSwBKbYijrIZdVAQPmXt9BhWfJKajno6F7glAiEAziAtF6gg5WtJXsfECb9a4aMjbesZSZg0bpWGMoXqQGYqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCKr9EBys%2Fi4lXQLNyrcA2AxKAPQHH0JbQgu1c%2FLl7K5SEUT1y0LFWFjMrNIilWk6dP4KigwAX74ETF6Gk6KW381dYG2jFG4%2FLKR7YuzFZYvMlKnfuV0Z9EHKDBSRv0auGdcATSk77dk1iqlU9bmUbsnCVvuH8QbvqHLGK9ftvYXghXmf2uRLS6Ke505XyuzC%2FBn2ECT%2BzGovsw5jekEwfbd7JMdOouNgMBAic7Q%2BB%2FElknfWQ%2BW8Pg2U3k4KE2hiLe8BgNId15R75lH0csNu5yNk3JfeWQ7jwyVu%2B1qLPQLx5%2F5cRQGZubBU10XYfTXgLzwoM%2F%2Bsae8nnAWqguJdyi%2F7i4uP2tgPas0Trbq7EUKvJNle9xtqAsBJUVq%2FI90qz7E6QSOiU2dba1aIVPLuGFjhjJqMn49ZOewWlAiJq2rFnK%2FcvMdEk9C0rNCg5kvPtUG7uIfHQ%2FWTePgipRCG3Cry16nKWevQb1WhQ%2FV86AqA9%2F4Nr5ih83GcIrIXNCwvbNMcRwTdgHGbDUowbcMUZAf3rJRW5v4UCOKvTq7gzmjGnBuygmhd2fIZz5OmCBAWcdwXra8qLBWkmqEDS9oXs54VsKuixrughVa9wJCUcQ1k1a3Adv705EbNOFKHj4I3MHdKFjS4CFiFzurMN63%2F9IGOqUBTmlBxOC95DC7H52HvoPqlDwOUfxG39y%2BFDbD18hVsEoBjYUEibkYCX28K0oNXmK%2BAaPj46QK9ZMJuLc5009XF6jJK7yCdevJQM6dqWbGBBTug7i79Gz2ioczEaMVlPyuYDM2PjwKcKxfBL1WLK4smgQe%2Fc9IByyDicCBF2CN%2FpxhPV%2FIf1dcBLp%2BeSR%2By6cNMJspF0%2F2zffxevrJEF4v4wBionx2&X-Amz-Signature=479a209e914a5f8c4eeffd0141d30d3063e606ee4f570427ca6ae0d4accd97d9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


这个任务为什么跑不起来？跑一半为什么卡死了，对不对？或者说为什么执行这么慢，都能观测得到具体的这个一些细节信息，那我觉得这个是很有意义的。所以说很多公司它都会基于开源的job，就是我自己去做扩展。并且比如说我这个 job 可能是有串并行关系的，可能是他先执行完了之后才能后面的 job 才能执行，或者是他们两个并行，然后最后汇总给最后一个job，然后去执行，这些都有可能。


当然我们这个开源的 ES 站网目前它功能没有这么强大，并且现在其实维护的也并不多了，但是在实际工作中使用还是可以的。这个是干什么呀？叫做 job event，就是事件的configuration，那它其实是依赖于数据源的，我们在这里面其实你可以看到我在配置文件里对于 spring 的这个 data source 看，这就我就使用原生的 spring data source，然后连接我的数据库叫做 elected job，然后去做了一些相关的配置 driver 以及 user name 和password。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/23932995-8f2a-4baa-9024-67a708b93d61/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMMOJCUQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225306Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFEdGB6adSwBKbYijrIZdVAQPmXt9BhWfJKajno6F7glAiEAziAtF6gg5WtJXsfECb9a4aMjbesZSZg0bpWGMoXqQGYqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCKr9EBys%2Fi4lXQLNyrcA2AxKAPQHH0JbQgu1c%2FLl7K5SEUT1y0LFWFjMrNIilWk6dP4KigwAX74ETF6Gk6KW381dYG2jFG4%2FLKR7YuzFZYvMlKnfuV0Z9EHKDBSRv0auGdcATSk77dk1iqlU9bmUbsnCVvuH8QbvqHLGK9ftvYXghXmf2uRLS6Ke505XyuzC%2FBn2ECT%2BzGovsw5jekEwfbd7JMdOouNgMBAic7Q%2BB%2FElknfWQ%2BW8Pg2U3k4KE2hiLe8BgNId15R75lH0csNu5yNk3JfeWQ7jwyVu%2B1qLPQLx5%2F5cRQGZubBU10XYfTXgLzwoM%2F%2Bsae8nnAWqguJdyi%2F7i4uP2tgPas0Trbq7EUKvJNle9xtqAsBJUVq%2FI90qz7E6QSOiU2dba1aIVPLuGFjhjJqMn49ZOewWlAiJq2rFnK%2FcvMdEk9C0rNCg5kvPtUG7uIfHQ%2FWTePgipRCG3Cry16nKWevQb1WhQ%2FV86AqA9%2F4Nr5ih83GcIrIXNCwvbNMcRwTdgHGbDUowbcMUZAf3rJRW5v4UCOKvTq7gzmjGnBuygmhd2fIZz5OmCBAWcdwXra8qLBWkmqEDS9oXs54VsKuixrughVa9wJCUcQ1k1a3Adv705EbNOFKHj4I3MHdKFjS4CFiFzurMN63%2F9IGOqUBTmlBxOC95DC7H52HvoPqlDwOUfxG39y%2BFDbD18hVsEoBjYUEibkYCX28K0oNXmK%2BAaPj46QK9ZMJuLc5009XF6jJK7yCdevJQM6dqWbGBBTug7i79Gz2ioczEaMVlPyuYDM2PjwKcKxfBL1WLK4smgQe%2Fc9IByyDicCBF2CN%2FpxhPV%2FIf1dcBLp%2BeSR%2By6cNMJspF0%2F2zffxevrJEF4v4wBionx2&X-Amz-Signature=1021f060cd0d917fce39070e37960941749f1c7ca6bc24510824145296af4457&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那其实我们这个数据库之前已经有了，我们看到以来其 job 你看已经有这个了，只不过这里边它会帮我们生成两张表，一个叫做 job execution log，打开表我这里边已经有好多日志了，对不对？那就是说老师在之前已经执行过很多任务，然后还有什么 States trans log，就是关于日志的一些 trans 轨迹跟踪，它会有执行时机，包括执行的这个服务的ID，包括具体执行什么哪个 job 以及 task ID 都会有，那其实我们可以把这两张表清空，你比如说把表从数据库删除，包括这个因为这里面有数据，这个我也从数据库中删除。


现在我就有一个 elected job 这个数据库，这里边表肯定都是没有的哈，都是空的哈。然后我们在指定数据库的时候，已经指定好了是不是叫做 elected job，所以库是已经有的，就是做这个事情的，有了它之后我把它也创建好了。那 registry center 跟这个 job event config 都有了之后，我们再回过头来看这个 my simple job configuration，把这两个注入进来之后，然后要干什么事情？要做一个艾特bin，这个并是什么呢？这个并是你自己的job，就是你自己定时任务里面要做什么业务处理，那你就自己应该写了，这就是具体真正的定时任务执行逻辑了。


那具体说这个我们一会再看，我们先不关注他，我们先看看配置，还没有什么其他的配置，再往下看。这有一个 job scheduler，也是当网给你提供的，其实它是比较核心的，就是用来运作 job 的，什么时间点执行，他会帮你去做处理的。然后 job schedule 的这里边也有一堆的配置项，这是我自己定义的，叫做 simple job。什么？就是我的表达式嘛，对不对？还有 selling total card，就是我的分片，还有我的分片的参数，包括我的 job 参数，包括 fail over 失败的情况下，我会不会做一些 fail over 失败的转移？还有monitor， monitor execution 就是监控， monitor port，监控对应的这个相当于端口。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/2e8bbf35-fa37-411d-b2c0-1ccd9d9342a0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMMOJCUQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225306Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFEdGB6adSwBKbYijrIZdVAQPmXt9BhWfJKajno6F7glAiEAziAtF6gg5WtJXsfECb9a4aMjbesZSZg0bpWGMoXqQGYqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCKr9EBys%2Fi4lXQLNyrcA2AxKAPQHH0JbQgu1c%2FLl7K5SEUT1y0LFWFjMrNIilWk6dP4KigwAX74ETF6Gk6KW381dYG2jFG4%2FLKR7YuzFZYvMlKnfuV0Z9EHKDBSRv0auGdcATSk77dk1iqlU9bmUbsnCVvuH8QbvqHLGK9ftvYXghXmf2uRLS6Ke505XyuzC%2FBn2ECT%2BzGovsw5jekEwfbd7JMdOouNgMBAic7Q%2BB%2FElknfWQ%2BW8Pg2U3k4KE2hiLe8BgNId15R75lH0csNu5yNk3JfeWQ7jwyVu%2B1qLPQLx5%2F5cRQGZubBU10XYfTXgLzwoM%2F%2Bsae8nnAWqguJdyi%2F7i4uP2tgPas0Trbq7EUKvJNle9xtqAsBJUVq%2FI90qz7E6QSOiU2dba1aIVPLuGFjhjJqMn49ZOewWlAiJq2rFnK%2FcvMdEk9C0rNCg5kvPtUG7uIfHQ%2FWTePgipRCG3Cry16nKWevQb1WhQ%2FV86AqA9%2F4Nr5ih83GcIrIXNCwvbNMcRwTdgHGbDUowbcMUZAf3rJRW5v4UCOKvTq7gzmjGnBuygmhd2fIZz5OmCBAWcdwXra8qLBWkmqEDS9oXs54VsKuixrughVa9wJCUcQ1k1a3Adv705EbNOFKHj4I3MHdKFjS4CFiFzurMN63%2F9IGOqUBTmlBxOC95DC7H52HvoPqlDwOUfxG39y%2BFDbD18hVsEoBjYUEibkYCX28K0oNXmK%2BAaPj46QK9ZMJuLc5009XF6jJK7yCdevJQM6dqWbGBBTug7i79Gz2ioczEaMVlPyuYDM2PjwKcKxfBL1WLK4smgQe%2Fc9IByyDicCBF2CN%2FpxhPV%2FIf1dcBLp%2BeSR%2By6cNMJspF0%2F2zffxevrJEF4v4wBionx2&X-Amz-Signature=fa77beb4bb9e6448ab6e74ff24e0c4b8d9cc320c712e13fe39f9122449df1460&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

然后还有什么叫做 Max digital，就是最大的误差时间，因为什么呢？因为 ZK 它也会记录一些你 job 运行的一些时间什么的，就跟我本地的这个当前应用服务的时间，它可能有一些误差，有一些这个时间上，比如说NTP，有些时间回调，有一些最大的误差，能够接受多少？这些都可以去配，还有什么呢？还有分片的， city g class 就是分片的策略，到底怎么去选择这里边？总之就是一堆配置，你先暂时不用特别的去关心，总之这些配置也是我在配置文件里配置好的，看见了，你看我这里边配置的，其实就是把它读出来，然后设置到下面这些内容里，就是做这个事情。当然后面还有一些都是为了去对 application 点 practice 里面配置的参数进行实例化的一些内容。


那我们回过头来看一下 practice 里面，首先第一个就是 Com 表达式，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/31c00224-9cff-454f-969e-c03243fb635d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMMOJCUQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225306Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFEdGB6adSwBKbYijrIZdVAQPmXt9BhWfJKajno6F7glAiEAziAtF6gg5WtJXsfECb9a4aMjbesZSZg0bpWGMoXqQGYqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCKr9EBys%2Fi4lXQLNyrcA2AxKAPQHH0JbQgu1c%2FLl7K5SEUT1y0LFWFjMrNIilWk6dP4KigwAX74ETF6Gk6KW381dYG2jFG4%2FLKR7YuzFZYvMlKnfuV0Z9EHKDBSRv0auGdcATSk77dk1iqlU9bmUbsnCVvuH8QbvqHLGK9ftvYXghXmf2uRLS6Ke505XyuzC%2FBn2ECT%2BzGovsw5jekEwfbd7JMdOouNgMBAic7Q%2BB%2FElknfWQ%2BW8Pg2U3k4KE2hiLe8BgNId15R75lH0csNu5yNk3JfeWQ7jwyVu%2B1qLPQLx5%2F5cRQGZubBU10XYfTXgLzwoM%2F%2Bsae8nnAWqguJdyi%2F7i4uP2tgPas0Trbq7EUKvJNle9xtqAsBJUVq%2FI90qz7E6QSOiU2dba1aIVPLuGFjhjJqMn49ZOewWlAiJq2rFnK%2FcvMdEk9C0rNCg5kvPtUG7uIfHQ%2FWTePgipRCG3Cry16nKWevQb1WhQ%2FV86AqA9%2F4Nr5ih83GcIrIXNCwvbNMcRwTdgHGbDUowbcMUZAf3rJRW5v4UCOKvTq7gzmjGnBuygmhd2fIZz5OmCBAWcdwXra8qLBWkmqEDS9oXs54VsKuixrughVa9wJCUcQ1k1a3Adv705EbNOFKHj4I3MHdKFjS4CFiFzurMN63%2F9IGOqUBTmlBxOC95DC7H52HvoPqlDwOUfxG39y%2BFDbD18hVsEoBjYUEibkYCX28K0oNXmK%2BAaPj46QK9ZMJuLc5009XF6jJK7yCdevJQM6dqWbGBBTug7i79Gz2ioczEaMVlPyuYDM2PjwKcKxfBL1WLK4smgQe%2Fc9IByyDicCBF2CN%2FpxhPV%2FIf1dcBLp%2BeSR%2By6cNMJspF0%2F2zffxevrJEF4v4wBionx2&X-Amz-Signature=d1ff60429ffd206468ea222814901de0e9d8360511da0ad4090fbfaee1557c90&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那这个 simple job 这个不是固定的，你可以写 simple job 叉这个你按照自己约束，你自己想怎么叫OK，比如说这个一般来讲你可以自己去定义，那我在这里定义这个，那我在解析的时候就以这个前缀就好了。后面这个东西是当然给你提供的固定的，你这个写错了就不行了。

```java
server.port=8881


elastic.job.zk.namespace=elastic-job
elastic.job.zk.serverLists=192.168.13.245:2181,192.168.13.246:2181,192.168.13.247:2181
//zookeeper.address=192.168.11.111:2181,192.168.11.112:2181,192.168.11.113:2181
zookeeper.namespace=elastic-job
zookeeper.connectionTimeout=10000
zookeeper.sessionTimeout=10000
zookeeper.maxRetries=3


simpleJob.cron=0/5 * * * * ?
#simpleJob.cron=00 03 21 * * ?
simpleJob.shardingTotalCount=5
simpleJob.shardingItemParameters=0=beijing,1=shanghai,2=changchun,3=changsha,4=hangzhou
simpleJob.jobParameter=source1=public,source2=private
simpleJob.failover=true
simpleJob.monitorExecution=true
simpleJob.monitorPort=8889
simpleJob.maxTimeDiffSeconds=-1
simpleJob.jobShardingStrategyClass=com.dangdang.ddframe.job.lite.api.strategy.impl.AverageAllocationJobShardingStrategy

#dataflowJob.cron=0/10 * * * * ?
#dataflowJob.shardingTotalCount=2
#dataflowJob.shardingItemParameters=0=Beijing,1=Shanghai

spring.datasource.url=jdbc:mysql://localhost:3306/elasticjob?useUnicode=true&characterEncoding=utf-8&verifyServerCertificate=false&useSSL=false&requireSSL=false
spring.datasource.driver-class-name=com.mysql.jdbc.Driver
spring.datasource.username=root
spring.datasource.password=guojun12
```


首先第一个就是你当前这个 job 多长时间执行一次？那我在这里边是不是就每 5 秒钟执行一次嘛？OK，这就是我们标准的科昂表达式。然后接下来就是说当前你的这个定时任务，你一共分了几片？这个什么意思？这个就是涉及到分布式定时任务了，我一共分了几片？假设说 5 秒钟执行一次，下一个 5 秒我执行一个大任务，比如说我里面有 5 台服务器， 5 台服务器的话就是每台服务器去执行整个这个大任务的其中的一小部分就是 1/ 5，我把它分成 5 片，对吧？接下来我们看还有一个 sharding item parameters，就是说这里边我说第零片是北京，第一片是上海，第二片是长春，然后第三片是长沙，然后第四片是杭州，那其实这个值等于啥？这个值一共不就是 5 嘛，对不对？你这里边分片的 parameters 你千万不要大于这个 total count，你小于都没问题，但是不能大于。


什么意思？如果大于他会报错的，他认为你分成 5 片，那就是第0片、第一片、第二片、第三片、第四片，一共 5 片。这个什么意思？就是说我分片了之后，我按照什么规则去确定它是一片，是不是？我说这一片把所有内容叫北京的当成一片，把所有内容叫上海的当成一片，所有内容叫长春的当成 1 片，设置成 5 片，就这个意思，后面我们演示的时候小伙伴们就懂了。然后这个 job 里边你可以带一些自己的参数，比如说我带自己的这个 source 1 等于public，逗号分隔 source 2 等于private，就是我带两个自己的参数，可能会用到OK，这就是他给你携带的一些你可以自定义的一些参数。上面这个是固定的，下面这个值你可以自己去定义，但是说这个肯定是从 0 开始的， 0 等于什么？什么 1 等于什么？什么 2 等于什么？什么？分片的时候，你肯定得按照这个 value 这个值去找到对应的信息，然后去针对于这个数据都是北京的，当成地理名片，然后去做处理，然后下面这里面有个 file over，就是失败转移。


比如说某一个分片由于某些原因我执行失败了，或者说我的服务挂掉了，那 ZK 呢？会不会做协调？比如说一共你分成 5 片，我在执行第二片的时候，发现这个第二天的数据执行这个任务执行失败了，那我是不是把第二片任务分给其他的这四代机器？这是可以的。我举个例子，这个分片其实它是根据机器来的。比如说我现在分出 5 片，我有 8 台机器，那永远会有 3 台机器是没有意义的。为什么呢？一共你分成了 5 片，你一共有 8 台机器去执行，肯定有 3 台没有作用。


这个其实就跟我们很多很多核心的概念都是类似的。我们随便找个例子嘛，我们卡夫卡里面 topic partition，一个 topic 下面可以有很多个partition，比如说我这个 topic 下面我有 4 个partition，那我一定是一个 partition 对应着一个consumer，这才会消费，才有意义。如果说我 4 个 partition 下面对应着 10 个consumer，那其中有 6 个 consumer 肯定是没在工作，没有意义。OK，那分片也是一样。我如果 5 个分片一共有 10 台机器，肯定有另外 5 台机器是没有工作的。但是我举个例子，我有 5 个分片，我就 2 台机器的话，是不是一个机器做了两片的事情，另外一个做了 3 片的事情？道理是一个意思，其实 Rocketmq 卡不卡都是这样的， Rocketmq 里边 consumer 也是一样的，是不是？比如说看你的队列，你队列数，如果有 5 个队列或者 6 个队列，那你一共有七八台机器，那肯定有两三台它是没有在工作的。

```java
simpleJob.monitorPort=8889

simpleJob.jobShardingStrategyClass=com.dangdang.ddframe.job.lite.api.strategy.impl.AverageAllocationJobShardingStrategy
```

好了，回过头来，这个 Moniter 它是否是监控这个 job 执行的状态，如果等于 true 就执行，然后你既然想监控它，你肯定有个监控的端口，这里边你可以随便去设。比如说我设置8889，那我这个是881，就当前我应用服务的，然后这个就最大的这个允许的误差是多少。比如说我的 Jupiter 上，它的时间跟你当前每台机器这五台机器，它的时间可能会有一些细微的差别，可能不一致。如果你要等于- 1 的话，就表示忽略这个差别。如果说某一台机器差了 10 秒钟了，那它就会报错，出问题就会不执行。


OK，这个就是关于误差这一块，然后他的这个 sharding city class，那我这里边可以选择很多种city，我们看到这个 a v g a lock it，然后 job sharding strategy 这什么意思？就是进行平均的分配，当然它还有一些其他的策略，这个你可以去参考一下当当网的这个源码，后面我会给你一些对应的这个当当的一些文章。


ES 照的这个事情其实我个人觉得小伙伴们应该都会有了解，因为毕竟上咱们的课程肯定不是一个对这个互联网技术框架一无所知的，如果你是一无所知，那你就应该加油了，那其实关于这几个配置我已经说清楚了，然后我们回过头来看一看它这个里面的东西，看看它到底怎么去做的。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/2e8bbf35-fa37-411d-b2c0-1ccd9d9342a0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMMOJCUQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225306Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFEdGB6adSwBKbYijrIZdVAQPmXt9BhWfJKajno6F7glAiEAziAtF6gg5WtJXsfECb9a4aMjbesZSZg0bpWGMoXqQGYqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCKr9EBys%2Fi4lXQLNyrcA2AxKAPQHH0JbQgu1c%2FLl7K5SEUT1y0LFWFjMrNIilWk6dP4KigwAX74ETF6Gk6KW381dYG2jFG4%2FLKR7YuzFZYvMlKnfuV0Z9EHKDBSRv0auGdcATSk77dk1iqlU9bmUbsnCVvuH8QbvqHLGK9ftvYXghXmf2uRLS6Ke505XyuzC%2FBn2ECT%2BzGovsw5jekEwfbd7JMdOouNgMBAic7Q%2BB%2FElknfWQ%2BW8Pg2U3k4KE2hiLe8BgNId15R75lH0csNu5yNk3JfeWQ7jwyVu%2B1qLPQLx5%2F5cRQGZubBU10XYfTXgLzwoM%2F%2Bsae8nnAWqguJdyi%2F7i4uP2tgPas0Trbq7EUKvJNle9xtqAsBJUVq%2FI90qz7E6QSOiU2dba1aIVPLuGFjhjJqMn49ZOewWlAiJq2rFnK%2FcvMdEk9C0rNCg5kvPtUG7uIfHQ%2FWTePgipRCG3Cry16nKWevQb1WhQ%2FV86AqA9%2F4Nr5ih83GcIrIXNCwvbNMcRwTdgHGbDUowbcMUZAf3rJRW5v4UCOKvTq7gzmjGnBuygmhd2fIZz5OmCBAWcdwXra8qLBWkmqEDS9oXs54VsKuixrughVa9wJCUcQ1k1a3Adv705EbNOFKHj4I3MHdKFjS4CFiFzurMN63%2F9IGOqUBTmlBxOC95DC7H52HvoPqlDwOUfxG39y%2BFDbD18hVsEoBjYUEibkYCX28K0oNXmK%2BAaPj46QK9ZMJuLc5009XF6jJK7yCdevJQM6dqWbGBBTug7i79Gz2ioczEaMVlPyuYDM2PjwKcKxfBL1WLK4smgQe%2Fc9IByyDicCBF2CN%2FpxhPV%2FIf1dcBLp%2BeSR%2By6cNMJspF0%2F2zffxevrJEF4v4wBionx2&X-Amz-Signature=fa77beb4bb9e6448ab6e74ff24e0c4b8d9cc320c712e13fe39f9122449df1460&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

总之我有一个 job scheduler，然后去把这些配置都加载完了之后做什么事情，总之我最终要返回一个 job schedule 的对象，然后这里边幸好当官网给我们跟 spring 集成写了一个叫做 spring job schedule 了，可以了，然后干什么呢？通过它把它拗出来，里边需要好多好多配纸项，看见了吗？第一个参数就是 simple job， simple job 是什么呢？就是你要具体执行哪个任务，这个是哪来的？这个其实就是我们上面这个实例b，这个就是我们具体执行任务写的逻辑了，我直接把它注入给spring，叫做 my job，它的名字注意方法，名字就是这个 bin 里边对应的 name 叫做 simple job，所以说我在这里直接可以用，相当于一个注入。那第一件事情要把这个具体执行的 job 传进来。

然后第二件是要把什么呢？你具体的注册中心就是 ZK 也传进来。

第三个它其实是要有一些配置项，这个配置项配置什么内容？比如说配置是否加监控，是否加那个什么 file over 的机制，这些一大堆的配置都需要有。然后这里边只需要传什么呢？你看到它里边只需要传一堆参数到这儿，这么多参数都是这个配置项要传的。


搞定了之后下一个参数什么呢？就是 job event configuration。还记得他吗？他是什么？

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/688be11c-f95f-4367-b97e-198d3172e44f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMMOJCUQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225306Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFEdGB6adSwBKbYijrIZdVAQPmXt9BhWfJKajno6F7glAiEAziAtF6gg5WtJXsfECb9a4aMjbesZSZg0bpWGMoXqQGYqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCKr9EBys%2Fi4lXQLNyrcA2AxKAPQHH0JbQgu1c%2FLl7K5SEUT1y0LFWFjMrNIilWk6dP4KigwAX74ETF6Gk6KW381dYG2jFG4%2FLKR7YuzFZYvMlKnfuV0Z9EHKDBSRv0auGdcATSk77dk1iqlU9bmUbsnCVvuH8QbvqHLGK9ftvYXghXmf2uRLS6Ke505XyuzC%2FBn2ECT%2BzGovsw5jekEwfbd7JMdOouNgMBAic7Q%2BB%2FElknfWQ%2BW8Pg2U3k4KE2hiLe8BgNId15R75lH0csNu5yNk3JfeWQ7jwyVu%2B1qLPQLx5%2F5cRQGZubBU10XYfTXgLzwoM%2F%2Bsae8nnAWqguJdyi%2F7i4uP2tgPas0Trbq7EUKvJNle9xtqAsBJUVq%2FI90qz7E6QSOiU2dba1aIVPLuGFjhjJqMn49ZOewWlAiJq2rFnK%2FcvMdEk9C0rNCg5kvPtUG7uIfHQ%2FWTePgipRCG3Cry16nKWevQb1WhQ%2FV86AqA9%2F4Nr5ih83GcIrIXNCwvbNMcRwTdgHGbDUowbcMUZAf3rJRW5v4UCOKvTq7gzmjGnBuygmhd2fIZz5OmCBAWcdwXra8qLBWkmqEDS9oXs54VsKuixrughVa9wJCUcQ1k1a3Adv705EbNOFKHj4I3MHdKFjS4CFiFzurMN63%2F9IGOqUBTmlBxOC95DC7H52HvoPqlDwOUfxG39y%2BFDbD18hVsEoBjYUEibkYCX28K0oNXmK%2BAaPj46QK9ZMJuLc5009XF6jJK7yCdevJQM6dqWbGBBTug7i79Gz2ioczEaMVlPyuYDM2PjwKcKxfBL1WLK4smgQe%2Fc9IByyDicCBF2CN%2FpxhPV%2FIf1dcBLp%2BeSR%2By6cNMJspF0%2F2zffxevrJEF4v4wBionx2&X-Amz-Signature=a78c0107c937f748b683dfa95ab5ec602e3ab469b360528969d6cf6351442546&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

他就是他，他就是比如说你执行的job，你需要做一些链路，做一些日志的跟踪，你可以放到 MySQL 里边，方便我去查看。所以说后面这个参数就是传他的。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/564acc7a-d946-470f-a906-5ede4ece0c72/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMMOJCUQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225306Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFEdGB6adSwBKbYijrIZdVAQPmXt9BhWfJKajno6F7glAiEAziAtF6gg5WtJXsfECb9a4aMjbesZSZg0bpWGMoXqQGYqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCKr9EBys%2Fi4lXQLNyrcA2AxKAPQHH0JbQgu1c%2FLl7K5SEUT1y0LFWFjMrNIilWk6dP4KigwAX74ETF6Gk6KW381dYG2jFG4%2FLKR7YuzFZYvMlKnfuV0Z9EHKDBSRv0auGdcATSk77dk1iqlU9bmUbsnCVvuH8QbvqHLGK9ftvYXghXmf2uRLS6Ke505XyuzC%2FBn2ECT%2BzGovsw5jekEwfbd7JMdOouNgMBAic7Q%2BB%2FElknfWQ%2BW8Pg2U3k4KE2hiLe8BgNId15R75lH0csNu5yNk3JfeWQ7jwyVu%2B1qLPQLx5%2F5cRQGZubBU10XYfTXgLzwoM%2F%2Bsae8nnAWqguJdyi%2F7i4uP2tgPas0Trbq7EUKvJNle9xtqAsBJUVq%2FI90qz7E6QSOiU2dba1aIVPLuGFjhjJqMn49ZOewWlAiJq2rFnK%2FcvMdEk9C0rNCg5kvPtUG7uIfHQ%2FWTePgipRCG3Cry16nKWevQb1WhQ%2FV86AqA9%2F4Nr5ih83GcIrIXNCwvbNMcRwTdgHGbDUowbcMUZAf3rJRW5v4UCOKvTq7gzmjGnBuygmhd2fIZz5OmCBAWcdwXra8qLBWkmqEDS9oXs54VsKuixrughVa9wJCUcQ1k1a3Adv705EbNOFKHj4I3MHdKFjS4CFiFzurMN63%2F9IGOqUBTmlBxOC95DC7H52HvoPqlDwOUfxG39y%2BFDbD18hVsEoBjYUEibkYCX28K0oNXmK%2BAaPj46QK9ZMJuLc5009XF6jJK7yCdevJQM6dqWbGBBTug7i79Gz2ioczEaMVlPyuYDM2PjwKcKxfBL1WLK4smgQe%2Fc9IByyDicCBF2CN%2FpxhPV%2FIf1dcBLp%2BeSR%2By6cNMJspF0%2F2zffxevrJEF4v4wBionx2&X-Amz-Signature=409c8d9dbd4c786c07fe8326fc9f2e0767028223eec388ef22a74f313637aa42&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

最后老师你这里边怎么又加了一个 listener 呢？看见了有一个叫做 simple job listener。这是什么东西？这个是我们自己写，当然我们自己写的这个 simple job listener 了，他也去实现了当当网的一个接口。那我们看到这个 simple job listener 在哪里？在，这是不是叫做 simple job listener？我们点进去来看一眼就知道了，

```java
package com.bfxy.esjob.listener;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import com.alibaba.fastjson.JSON;
import com.dangdang.ddframe.job.executor.ShardingContexts;
import com.dangdang.ddframe.job.lite.api.listener.ElasticJobListener;

public class SimpleJobListener implements ElasticJobListener {

	private static Logger LOGGER = LoggerFactory.getLogger(SimpleJobListener.class);
	
	@Override
	public void beforeJobExecuted(ShardingContexts shardingContexts) {
		LOGGER.info("-----------------执行任务之前：{}", JSON.toJSONString(shardingContexts));
	}

	@Override
	public void afterJobExecuted(ShardingContexts shardingContexts) {
		LOGGER.info("-----------------执行任务之后：{}", JSON.toJSONString(shardingContexts));		
	}
	
}
```

它一定要实现当当网的 elected job listener。然后要重写两个方法，一个叫做 before job executed，还有一个叫做 after job excuted。什么意思？就是说在定时任务执行之前，我要做一些逻辑，定时任务执行之后，我要做一些逻辑，那我就简单的去打印了两个 info 的日志，就是执行之前执行之后具体的内容就是把当前的这个 starling context 里边的做一个 JSON 输出好了，很简单。那也就是说其实我们这个 simple job config 里边最核心的就是这个 spring job schedule，怎么去创建它？用到哪些参数？那我现在其实给小伙伴们讲的就是参数最全的了，其实它还有一个，比如说你看还有这个listener，你看它是三个点，就是说后边两个参数我可以不要不要，你看他也不报错，开通这个是最少的方式。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/edc0d80d-3eb2-4431-9525-ed22ee667273/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMMOJCUQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225306Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFEdGB6adSwBKbYijrIZdVAQPmXt9BhWfJKajno6F7glAiEAziAtF6gg5WtJXsfECb9a4aMjbesZSZg0bpWGMoXqQGYqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCKr9EBys%2Fi4lXQLNyrcA2AxKAPQHH0JbQgu1c%2FLl7K5SEUT1y0LFWFjMrNIilWk6dP4KigwAX74ETF6Gk6KW381dYG2jFG4%2FLKR7YuzFZYvMlKnfuV0Z9EHKDBSRv0auGdcATSk77dk1iqlU9bmUbsnCVvuH8QbvqHLGK9ftvYXghXmf2uRLS6Ke505XyuzC%2FBn2ECT%2BzGovsw5jekEwfbd7JMdOouNgMBAic7Q%2BB%2FElknfWQ%2BW8Pg2U3k4KE2hiLe8BgNId15R75lH0csNu5yNk3JfeWQ7jwyVu%2B1qLPQLx5%2F5cRQGZubBU10XYfTXgLzwoM%2F%2Bsae8nnAWqguJdyi%2F7i4uP2tgPas0Trbq7EUKvJNle9xtqAsBJUVq%2FI90qz7E6QSOiU2dba1aIVPLuGFjhjJqMn49ZOewWlAiJq2rFnK%2FcvMdEk9C0rNCg5kvPtUG7uIfHQ%2FWTePgipRCG3Cry16nKWevQb1WhQ%2FV86AqA9%2F4Nr5ih83GcIrIXNCwvbNMcRwTdgHGbDUowbcMUZAf3rJRW5v4UCOKvTq7gzmjGnBuygmhd2fIZz5OmCBAWcdwXra8qLBWkmqEDS9oXs54VsKuixrughVa9wJCUcQ1k1a3Adv705EbNOFKHj4I3MHdKFjS4CFiFzurMN63%2F9IGOqUBTmlBxOC95DC7H52HvoPqlDwOUfxG39y%2BFDbD18hVsEoBjYUEibkYCX28K0oNXmK%2BAaPj46QK9ZMJuLc5009XF6jJK7yCdevJQM6dqWbGBBTug7i79Gz2ioczEaMVlPyuYDM2PjwKcKxfBL1WLK4smgQe%2Fc9IByyDicCBF2CN%2FpxhPV%2FIf1dcBLp%2BeSR%2By6cNMJspF0%2F2zffxevrJEF4v4wBionx2&X-Amz-Signature=3581bef192d4b2b689045386b04c7ec876939d9acde306a87599392f044a3c47&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

然后如果你有特殊需求，你说你加上日志，加上 listener 也是可以的，所以说我讲的时候一定是讲最全的。


OK，关于这个 spring 的这个 schedual 我们已经讲完了，那最核心的就是这个叫做 late job configuration，它里边传了这么多参数，我们来看一看它吧，点进去它就是当网的一个逻辑了。这里边首先第一件事情是要把它的这个 configuration 创建出来，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/8a3b664f-56ff-4c86-b983-393c3d2a20ce/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMMOJCUQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225306Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFEdGB6adSwBKbYijrIZdVAQPmXt9BhWfJKajno6F7glAiEAziAtF6gg5WtJXsfECb9a4aMjbesZSZg0bpWGMoXqQGYqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCKr9EBys%2Fi4lXQLNyrcA2AxKAPQHH0JbQgu1c%2FLl7K5SEUT1y0LFWFjMrNIilWk6dP4KigwAX74ETF6Gk6KW381dYG2jFG4%2FLKR7YuzFZYvMlKnfuV0Z9EHKDBSRv0auGdcATSk77dk1iqlU9bmUbsnCVvuH8QbvqHLGK9ftvYXghXmf2uRLS6Ke505XyuzC%2FBn2ECT%2BzGovsw5jekEwfbd7JMdOouNgMBAic7Q%2BB%2FElknfWQ%2BW8Pg2U3k4KE2hiLe8BgNId15R75lH0csNu5yNk3JfeWQ7jwyVu%2B1qLPQLx5%2F5cRQGZubBU10XYfTXgLzwoM%2F%2Bsae8nnAWqguJdyi%2F7i4uP2tgPas0Trbq7EUKvJNle9xtqAsBJUVq%2FI90qz7E6QSOiU2dba1aIVPLuGFjhjJqMn49ZOewWlAiJq2rFnK%2FcvMdEk9C0rNCg5kvPtUG7uIfHQ%2FWTePgipRCG3Cry16nKWevQb1WhQ%2FV86AqA9%2F4Nr5ih83GcIrIXNCwvbNMcRwTdgHGbDUowbcMUZAf3rJRW5v4UCOKvTq7gzmjGnBuygmhd2fIZz5OmCBAWcdwXra8qLBWkmqEDS9oXs54VsKuixrughVa9wJCUcQ1k1a3Adv705EbNOFKHj4I3MHdKFjS4CFiFzurMN63%2F9IGOqUBTmlBxOC95DC7H52HvoPqlDwOUfxG39y%2BFDbD18hVsEoBjYUEibkYCX28K0oNXmK%2BAaPj46QK9ZMJuLc5009XF6jJK7yCdevJQM6dqWbGBBTug7i79Gz2ioczEaMVlPyuYDM2PjwKcKxfBL1WLK4smgQe%2Fc9IByyDicCBF2CN%2FpxhPV%2FIf1dcBLp%2BeSR%2By6cNMJspF0%2F2zffxevrJEF4v4wBionx2&X-Amz-Signature=d382c879a9c19ff612b1d8690fb808cbee5bc70314d81c7a5816a89280b174df&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

叫做 job call configuration 创建出来，它采用的也是这种build，就是建造者模式，你有一个build，然后最后去做build，在他们之间去做一些 set 的操作。它 build 的时候首先需要job，它的 class 是什么？对不对？然后这里边也有范型规定，说当前这个一定是继承这个类才能够去填到这里边，为什么？因为这里边它的这个配置叫做，后面你会看到叫做 simple job configuration。


好，第一个参数传的就是这个类名，第二个参数传的就是你的 crowd 表达式是什么？然后第三个就是你的这个 shared total 一共分几片？OK，然后有了它之后，你会看到它里边是不是也用到其他参数，比如说一些miss，fire，这些参数我可以直接设置为true，然后 fail over，根据你的配置是否去进行 fail over 了。然后 job Pym 是否要传一些参数？对不对？就是说你自定义的参数你是否要传，对吧？然后这个叫做 sharedeal atom parameters，就是 0 等于北京， 1 等于上海， 3 等于长春， 4 等于什么？什么 5 等于杭州。就是那个分片你一定要添进去，然后最后把它 build 出来，返回了之后你要创建一个 simple job configuration，然后把当前的这个扔进去。明白，然后还不够他还要做什么事情？还要传一个 job class，就是你要 get 它的什么， get name 就可以了。


接下来最后一步就是对这个 let job configuration 进行返回，然后最终你要把它返回去，也就是说这里边去设置的是 simple job configuration，那其实它们是一个依次的，这个引用的关系就是上面这个 configuration 会被注入到这个 simple job configuration 里面，对吧？你看上面这个 job configuration 是放到了 simple job configuration 里，然后 simple job configuration 一定是放到这个 late job configuration 里，因为最终我是要返回这个 late job configuration，你要把它传入出来，然后这里边我可以设置它的这个 city 自带进程策略，我可以放进去，我们之前看到了那个配置里写的是平均分配，然后他是否要加监听？然后他的监听端口是什么？允许误差吗？ -1 的话就表示忽略误差。


然后这有个override，我们点进去吧，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/8b34976a-4ac6-4894-9d3b-3a9620e19275/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UMMOJCUQ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225306Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFEdGB6adSwBKbYijrIZdVAQPmXt9BhWfJKajno6F7glAiEAziAtF6gg5WtJXsfECb9a4aMjbesZSZg0bpWGMoXqQGYqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDCKr9EBys%2Fi4lXQLNyrcA2AxKAPQHH0JbQgu1c%2FLl7K5SEUT1y0LFWFjMrNIilWk6dP4KigwAX74ETF6Gk6KW381dYG2jFG4%2FLKR7YuzFZYvMlKnfuV0Z9EHKDBSRv0auGdcATSk77dk1iqlU9bmUbsnCVvuH8QbvqHLGK9ftvYXghXmf2uRLS6Ke505XyuzC%2FBn2ECT%2BzGovsw5jekEwfbd7JMdOouNgMBAic7Q%2BB%2FElknfWQ%2BW8Pg2U3k4KE2hiLe8BgNId15R75lH0csNu5yNk3JfeWQ7jwyVu%2B1qLPQLx5%2F5cRQGZubBU10XYfTXgLzwoM%2F%2Bsae8nnAWqguJdyi%2F7i4uP2tgPas0Trbq7EUKvJNle9xtqAsBJUVq%2FI90qz7E6QSOiU2dba1aIVPLuGFjhjJqMn49ZOewWlAiJq2rFnK%2FcvMdEk9C0rNCg5kvPtUG7uIfHQ%2FWTePgipRCG3Cry16nKWevQb1WhQ%2FV86AqA9%2F4Nr5ih83GcIrIXNCwvbNMcRwTdgHGbDUowbcMUZAf3rJRW5v4UCOKvTq7gzmjGnBuygmhd2fIZz5OmCBAWcdwXra8qLBWkmqEDS9oXs54VsKuixrughVa9wJCUcQ1k1a3Adv705EbNOFKHj4I3MHdKFjS4CFiFzurMN63%2F9IGOqUBTmlBxOC95DC7H52HvoPqlDwOUfxG39y%2BFDbD18hVsEoBjYUEibkYCX28K0oNXmK%2BAaPj46QK9ZMJuLc5009XF6jJK7yCdevJQM6dqWbGBBTug7i79Gz2ioczEaMVlPyuYDM2PjwKcKxfBL1WLK4smgQe%2Fc9IByyDicCBF2CN%2FpxhPV%2FIf1dcBLp%2BeSR%2By6cNMJspF0%2F2zffxevrJEF4v4wBionx2&X-Amz-Signature=ba71b9c3d3710673915c486869a2857983dec7668b9460433a5f3b6c49f2c6a0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

因为它点进去里边你能看到这个源码设置本地配置是否可以覆盖注册中心的配置？如果可以覆盖，每次启动的时候都以本地为准。 override 的目的是本地配置是否可以覆盖注册中心的配置？也就是说其实我们在做注册中心的时候，他怎么去做的？它是相当于就是把我们自己的这个 application 点 practice 里边这些配置，它这叫本地的配置，但是这些配置它也一并会帮我们去注册到租 keeper 上，然后那个配置项等于 true 和false，含义就是说到底以哪个为准？到底是以租 keeper 以前注册的为准，还是以我最新的以我本地的这个配置文件为准？如果你设置成 true 的话，那就以本地的为准。设置成 true 的话就是注册中心。我不管每次我重启应用服务的时候，我都不会去从注册中心上去拉配置，我去拿我本地的这个 application 加 promise 里面的配置为准。


如果你写成 false 呢？那就是说你之前已经放到 ZK 上了，对不对？那就以 ZK 上为准。那这个在实际工作中**，那我个人建议小伙伴们应该根据需求而定。如果说你期望说以后我们直接通过改 ZK 去做，那你可以干什么？其实说白了，这些配置我都可以不写能力有什么意思吗？我只需要配制作中心就好。**


**如果你熟悉 ES job 的话，以后我们都是统一的，在我的这个有任务的时候，我直接我自己画一控台，我自己去在 ZK 上去添加我自己的这些分片策略，包括corn 表达式，我直接可以那么去玩，我不在这里去做。所以说老师在实际工作中都是以 ZK 为准的，所以说这个配置项一直是等于false，就是不以本地为主了。**


**要改的话去 ZK 上改，因为你在这里改的话怎么办？在这里改的话，你的服务是不是得重新启动啊？又重新启动一次，你比如说我的服务已经起来了，然后我是不是想改下配置？那你只能改 CK 的对不对？OK，或者在这里边你用一些其他的第三方的配置，中心的一些组件，**比如说像耐克斯或者是像阿波罗、携程的也可以。不过这个 ES job 既然给你提供了这个功能了，那你最好用它，这个功能就是最好的了。好了，那其实最终把它返回之后，这个对象就已经获取了。那这个就是关于我们当网 ES job 的一些比较繁琐的一些配置了。确实是有点繁琐，不过其实这个东西都是一些模板代码，大体上了解了之后，后面你直接 copy 过来用就好了，就是一些模板好啰嗦了这么多，


最核心的就是你的定时任务要怎么写，是不是它在哪？它就是在这里，

```java
/**
	 * 	具体真正的定时任务执行逻辑
	 * @return
	 */
	@Bean
	public SimpleJob simpleJob() {
		return new MySimpleJob();
	}
```

就是这个 simple job，这个 simple job 是当晚给你提供的一个父类，它是一个 interface 接口，那你的子类 MySQL job 怎么做了？我点进去，这个 my simple job 是我自己写的，

```java
package com.bfxy.esjob.task;

import com.bfxy.esjob.annotation.JobTrace;
import org.springframework.stereotype.Component;

import com.bfxy.rabbit.task.annotation.ElasticJobConfig;
import com.dangdang.ddframe.job.api.ShardingContext;
import com.dangdang.ddframe.job.api.simple.SimpleJob;

@ElasticJobConfig
@Component
public class MySimpleJob implements SimpleJob {

	
	@JobTrace
	@Override
	public void execute(ShardingContext shardingContext) {

		System.err.println("---------	开始任务 MySimpleJob	---------");

		System.err.println(shardingContext.getJobName());
		System.err.println(shardingContext.getJobParameter());
		System.err.println(shardingContext.getShardingItem());
		System.err.println(shardingContext.getShardingParameter());
		System.err.println(shardingContext.getShardingTotalCount());
		System.err.println("当前线程 : ---------------" + Thread.currentThread().getName());

		System.err.println("----------结束任务------");
	}
	
	
	
}
```

我们来最大化，它一定是 implements simple job 当网的重写一个方法，重写 excuse 方法，然后他会把这个 sharding context 给你传过来。


那同学们想一想，那这个 sharding context 里面到底都有啥东西？这里边肯定会告诉我到底是怎么去分片的，就相当于我在 application 点 props 里边，这些配置肯定都会帮我们放到context，对不对？要不然我怎么去区分片？我怎么去说等于 0 的，等于 1 的，等于 2 的，我怎么去区分它到底做不做事情？所以说这里边肯定都是比较核心的配置项啊，你看到老师在这里都已经把这些东西都打印出来了。


OK，那我们搞定了这件事情之后，基本上我们当网的这个 ES job 就跟大家已经讲完了。那我们来真正的去尝试把它运行起来看一看。我先把这个东西都关掉，然后我先看一下这个 data flow config，我先注释掉了，对不对？然后还有什么trans，这个 trans configuration 这是我自己写的，我也把它先注一下，我们暂时你就关注什么呢？就关注 simple job configuration 就可以了，我们把它提起来，那这个配置说的是每 5 秒钟执行一次，然后一共有 5 个分片，对吧？我们来看一看就行了，我们直接把它运行起来，老师的 Jupiter 已经启动起来了，我已经开启了这个虚拟机，有三个节点， Jupiter 现在已经是启动的了。好，因为它是一个 sprint boot 工程，所以说我直接能够启动右键 run as sprint boot application 已经启动了。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/af708841-35f3-4c35-bd5f-a3a77905ddbe/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663HVGZM4Y%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225306Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDyw2VthGenu4jbvA0vyGM%2BK4aTKZID5GEj02Y7Cp9yEAIhAIybjOxZAMHcOtqGzM4cU5GuBNkz6C%2BCZp4UkpRryGQrKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwc4%2BW5ipTV4wb0HEYq3ANnxQiuDWDche%2FLgFVtfvAx%2Bl7G4OfyCgWZOdaxt%2FMcjabVVOmrmoTIeubF0ybjOhAcO2URVdHEwNu6jU7VZdYF%2BFkwUPWz9WqZYZ7qacPgHm9TH%2Bo9A3iwhrNQcLecoUNb38%2Bem5HXARAPi5Nyn97siMacOUXzKlNRefKA2ZdJT9OVEMhLjV1MjB0pO7Mq%2Bgujq1R%2ByNUtTkPPvCLFkIjuHtgCYscrvaS5G%2FzXAu1PebcGcWVGhTpggc4OplEPFAhI2CWMJhmUs8N88T9pzby1Zcfv00Le5LU%2BuMjiapdvNOK2JqdUFfBVCKaLdLAHlP1i%2BZ8gLOwAac7riXg9hZ1b51Z84nJYkYjRZNeA8%2F1ZbyNKBNw1%2FU6k%2BeaiU9II%2B73pQDJBOwev7NJ9sbcS95xcCGo6LV0eUNiuAnny0NT0hgVWCpCzA%2BlWVyip%2BP4f0yksN%2FEJx0sgWIv7v0lGYsnjuwmVyEQ5VpUBNTR2EVXhI4z3ratkmiN7KEQ1GBSR3y6NZ6z%2BpeNRBMyMIceIjo2J96XbVrmaD7ns0bVUTulK8%2FU%2BuEkxcGnbe7Kpbpf8jVRIRYoOn%2Bq8d%2FyZuc0ZvVsPlrlhV5Wdd8kh76PAwfs%2Blmpd%2BnCDZSamY6abszDCuP%2FSBjqkAeoYDAxutx3T64Xq0oKO%2BfNDUqUsNIM0scey6JX%2Bw2uAGicdpsKmu%2BvTIdNdfz7HnwfrAFF9XedjiP%2B9va8FC7%2Fu%2BD0WUM2v4wSoZtrRL5%2FvPd%2BUSMqLvr4xRLztTAOk3Vc1mnv%2BJNPzHrp1m3Tfc6SSF7dozePrDzPHpUPTZdTCnzC8Qmcgz%2BNGtXQWiha02haTRL9bIjFXCKcE72ay8HzJGbEg&X-Amz-Signature=7f68241ea9afb257d69358f3290ef62d13807b762b41ec64e2f2db18909e4371&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

我们来观察一下，你看，开始执行了，这是执行第一次看 5 秒钟，之后执行，第二次看到了，然后再过 5 秒 3540 对不对？然后再过 5 秒就是 45 秒，也就是说每 5 秒钟它会执行一次定时任务，为什么它会打印 5 次？同学们想一想，因为你一共有 5 个分片，它会分成 5 个线程来去执行。


虽然说我的代码上就打印了一次，你看我的代码上那个 task 就是 MySQL job 里边是不是就打印了一句话，但是他帮我打印了 5 次，那就说明这个分片已经起到作用了，这个是我想跟小伙伴们说的。好，我把它停掉好了。那这个关于 ES job 的一个简单的入门，咱们的这个上半部分就讲到这，然后一会我们来看一看，继续去把这一些下半部分再讲一讲，咱们先休息一下。好，这节课先到这，感谢小伙伴们收看。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/5b388416-8582-4301-b365-feeb56d0b64e/2020-09-17_173816.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663HVGZM4Y%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225306Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDyw2VthGenu4jbvA0vyGM%2BK4aTKZID5GEj02Y7Cp9yEAIhAIybjOxZAMHcOtqGzM4cU5GuBNkz6C%2BCZp4UkpRryGQrKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igwc4%2BW5ipTV4wb0HEYq3ANnxQiuDWDche%2FLgFVtfvAx%2Bl7G4OfyCgWZOdaxt%2FMcjabVVOmrmoTIeubF0ybjOhAcO2URVdHEwNu6jU7VZdYF%2BFkwUPWz9WqZYZ7qacPgHm9TH%2Bo9A3iwhrNQcLecoUNb38%2Bem5HXARAPi5Nyn97siMacOUXzKlNRefKA2ZdJT9OVEMhLjV1MjB0pO7Mq%2Bgujq1R%2ByNUtTkPPvCLFkIjuHtgCYscrvaS5G%2FzXAu1PebcGcWVGhTpggc4OplEPFAhI2CWMJhmUs8N88T9pzby1Zcfv00Le5LU%2BuMjiapdvNOK2JqdUFfBVCKaLdLAHlP1i%2BZ8gLOwAac7riXg9hZ1b51Z84nJYkYjRZNeA8%2F1ZbyNKBNw1%2FU6k%2BeaiU9II%2B73pQDJBOwev7NJ9sbcS95xcCGo6LV0eUNiuAnny0NT0hgVWCpCzA%2BlWVyip%2BP4f0yksN%2FEJx0sgWIv7v0lGYsnjuwmVyEQ5VpUBNTR2EVXhI4z3ratkmiN7KEQ1GBSR3y6NZ6z%2BpeNRBMyMIceIjo2J96XbVrmaD7ns0bVUTulK8%2FU%2BuEkxcGnbe7Kpbpf8jVRIRYoOn%2Bq8d%2FyZuc0ZvVsPlrlhV5Wdd8kh76PAwfs%2Blmpd%2BnCDZSamY6abszDCuP%2FSBjqkAeoYDAxutx3T64Xq0oKO%2BfNDUqUsNIM0scey6JX%2Bw2uAGicdpsKmu%2BvTIdNdfz7HnwfrAFF9XedjiP%2B9va8FC7%2Fu%2BD0WUM2v4wSoZtrRL5%2FvPd%2BUSMqLvr4xRLztTAOk3Vc1mnv%2BJNPzHrp1m3Tfc6SSF7dozePrDzPHpUPTZdTCnzC8Qmcgz%2BNGtXQWiha02haTRL9bIjFXCKcE72ay8HzJGbEg&X-Amz-Signature=e09e41c4b59f3adb97b711e909d82593db10a873aa49a008748ba21abd645225&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)




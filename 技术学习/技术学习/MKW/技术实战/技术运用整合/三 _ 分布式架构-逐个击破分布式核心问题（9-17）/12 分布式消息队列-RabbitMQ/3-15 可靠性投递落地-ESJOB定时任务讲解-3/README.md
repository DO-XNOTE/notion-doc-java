---
title: 3-15 可靠性投递落地-ESJOB定时任务讲解-3
---

# 3-15 可靠性投递落地-ESJOB定时任务讲解-3

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/f0cca36e-20f9-433b-b7d1-9f52e96565b7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZLGIZIOB%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDsT15l7Z7B1B%2BJ4Cwnqf2xX6q%2B9dTc3pR8f751r0rJrgIhAKOSuU83OMHZp46MeWvVw9NL%2BUnKXWFGIEz32TpcC72rKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz%2Fkn5SRmIzvDCGTOwq3APjHn8iAjrbHeOj65V8cqi%2FqUCyt4jlWJN1W8nH9G9J8ipT4EAJ4tdSi30YdOxyK%2F5oJRUj9H%2Ftg%2BCMZS2TsJ4QYCacqDWcPXGvjWlCLPWuome50p11xOLuy3PO2xzNTBcgNpfXbMlElauTozySw6MyKc4zWDwRAFKfCvXX%2FUfCp7R%2FyKOyQ7ZCOVdIltWnIkwk6gtmK38EadABzTlhK3ajuqZ4HKqFYk%2FqQCORmLtAefKESLan%2FmsyekngyJim1VLGfq3qVaMWn69TaOxG61Ug4r2w%2FHe16rP1FyVUqxHnTiPZsYN0CRwP2JN6yjI%2BIJ6Og5Tn0rf5YHKgh%2BDWNITDHkXxbNHrMj5JKExPRulk75MxTUVV%2BfIIcAGYyOVMVXAPkAPk6%2B%2FVT3pu9cW8DPM1YkfnzsgmqF22vtRD9gnvFJe4hAHW8qfFraABIlPEbnCY0KCCg%2FBzWX%2BADvG2Me5u8PSC%2FLF0Lnz1O8UjbyN6di8O8P1oLfDrHSDmP1PwfGXXNwr8PicOc3LfLWCWUfH5leh9KoydHyR9jvyYUUslO%2FiqjvZwJfar8OQe7g4cRs4IGxhEaKiTIx3iT%2FIjFWp71QI3AHYgz9XDYx2GBw7rvfShuH0HF8ZTrnf%2FADDyuv%2FSBjqkAb%2Fwm%2FYK45%2Frdnkh0uEdZSvtElSnN5XiVpOwsB%2FhNmVIBnzwzUCc0cvHSiNwxnXOvKCfsXkZWkAGvYWzHRLcvKkDcidtw%2FbjaQEr2BFJ2o7ab1LnWjGwXNlajlPY%2BUMMH8IJWunCLCyBNsgkDjgccJtzK8vu5EO24aGN%2B3d35H147pVaFrhPIvDcTrwpDTeUZ9cIra3fHIIp7hPPMa2TEcdnohAk&X-Amz-Signature=16bd182941b5ad4648228d80ce10492a72fd23da47de29af4b28ec601122fe97&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/c47f3fc0-662d-4fd6-b27f-d4d7797dc39f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZLGIZIOB%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDsT15l7Z7B1B%2BJ4Cwnqf2xX6q%2B9dTc3pR8f751r0rJrgIhAKOSuU83OMHZp46MeWvVw9NL%2BUnKXWFGIEz32TpcC72rKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz%2Fkn5SRmIzvDCGTOwq3APjHn8iAjrbHeOj65V8cqi%2FqUCyt4jlWJN1W8nH9G9J8ipT4EAJ4tdSi30YdOxyK%2F5oJRUj9H%2Ftg%2BCMZS2TsJ4QYCacqDWcPXGvjWlCLPWuome50p11xOLuy3PO2xzNTBcgNpfXbMlElauTozySw6MyKc4zWDwRAFKfCvXX%2FUfCp7R%2FyKOyQ7ZCOVdIltWnIkwk6gtmK38EadABzTlhK3ajuqZ4HKqFYk%2FqQCORmLtAefKESLan%2FmsyekngyJim1VLGfq3qVaMWn69TaOxG61Ug4r2w%2FHe16rP1FyVUqxHnTiPZsYN0CRwP2JN6yjI%2BIJ6Og5Tn0rf5YHKgh%2BDWNITDHkXxbNHrMj5JKExPRulk75MxTUVV%2BfIIcAGYyOVMVXAPkAPk6%2B%2FVT3pu9cW8DPM1YkfnzsgmqF22vtRD9gnvFJe4hAHW8qfFraABIlPEbnCY0KCCg%2FBzWX%2BADvG2Me5u8PSC%2FLF0Lnz1O8UjbyN6di8O8P1oLfDrHSDmP1PwfGXXNwr8PicOc3LfLWCWUfH5leh9KoydHyR9jvyYUUslO%2FiqjvZwJfar8OQe7g4cRs4IGxhEaKiTIx3iT%2FIjFWp71QI3AHYgz9XDYx2GBw7rvfShuH0HF8ZTrnf%2FADDyuv%2FSBjqkAb%2Fwm%2FYK45%2Frdnkh0uEdZSvtElSnN5XiVpOwsB%2FhNmVIBnzwzUCc0cvHSiNwxnXOvKCfsXkZWkAGvYWzHRLcvKkDcidtw%2FbjaQEr2BFJ2o7ab1LnWjGwXNlajlPY%2BUMMH8IJWunCLCyBNsgkDjgccJtzK8vu5EO24aGN%2B3d35H147pVaFrhPIvDcTrwpDTeUZ9cIra3fHIIp7hPPMa2TEcdnohAk&X-Amz-Signature=0c900cd9bfbb965e9709b904308b09e5cbfdcda0ef01bf2792793acc96a26e81&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

我们来看一看另外的一种 job ，data flow job。 data flow 是什么意思？就是说我可以实时的去抓取数据，不停的去抓取，那我们来看一看具体它的配置，它的写法其实跟 simple job 都大同小异，我们来看一看对于 data flow job config 它里边应该怎么去配置。

```java
#dataflowJob.cron=0/10 * * * * ?
#dataflowJob.shardingTotalCount=2
#dataflowJob.shardingItemParameters=0=Beijing,1=Shanghai
```

首先第一点也是一样的，看见了把这两个东西，一个是 registry center，还有一个是我们的 event configuration 都注入进来，然后这回名字变了，看到变成 data flow job，然后这个就是我自己创建的叫做 spring data flow job，我自己起的一个名字，它注入给 spring 之后它的名字叫做 data flow job。也是一样在 init 方法的时候传进来，然后把关于 data flow job 的一些配置都设置进来，然后去创建的  scheduler，创建 scheduler 了之后也是一样，返回这些代码都大同小异的，它的分片item，分片total，包括它的 sharding 策略都是一样的。

```java
/*
 * Copyright 1999-2015 dangdang.com.
 * <p>
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 * </p>
 */

package com.bfxy.esjob.config;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import com.bfxy.esjob.task.SpringDataflowJob;
import com.dangdang.ddframe.job.api.dataflow.DataflowJob;
import com.dangdang.ddframe.job.config.JobCoreConfiguration;
import com.dangdang.ddframe.job.config.dataflow.DataflowJobConfiguration;
import com.dangdang.ddframe.job.event.JobEventConfiguration;
import com.dangdang.ddframe.job.lite.api.JobScheduler;
import com.dangdang.ddframe.job.lite.config.LiteJobConfiguration;
import com.dangdang.ddframe.job.lite.spring.api.SpringJobScheduler;
import com.dangdang.ddframe.job.reg.zookeeper.ZookeeperRegistryCenter;

//@Configuration
public class DataflowJobConfig {
    
	@Autowired
    private ZookeeperRegistryCenter regCenter;
    
    @Autowired
    private JobEventConfiguration jobEventConfiguration;
    
    @Bean
    public DataflowJob dataflowJob() {
        return new SpringDataflowJob();
    }
    
    @Bean(initMethod = "init")
    public JobScheduler dataflowJobScheduler(final DataflowJob dataflowJob, @Value("${dataflowJob.cron}") final String cron,
                                             @Value("${dataflowJob.shardingTotalCount}") final int shardingTotalCount,
                                             @Value("${dataflowJob.shardingItemParameters}") final String shardingItemParameters) {
       
    	SpringJobScheduler springJobScheduler = new SpringJobScheduler(dataflowJob, regCenter, getLiteJobConfiguration(dataflowJob.getClass(), cron,
                shardingTotalCount, shardingItemParameters), jobEventConfiguration);
//    	springJobScheduler.init();
    	return springJobScheduler;
    }
    
    private LiteJobConfiguration getLiteJobConfiguration(final Class<? extends DataflowJob> jobClass, final String cron, final int shardingTotalCount, final String shardingItemParameters) {
        return LiteJobConfiguration.newBuilder(
        		new DataflowJobConfiguration(JobCoreConfiguration.newBuilder(jobClass.getName(), cron, shardingTotalCount)
        		.shardingItemParameters(shardingItemParameters).build(), 
        		jobClass.getCanonicalName(),
        		false))	//streamingProcess
        		.overwrite(false)
        		.build();
    }
}
```

只不过在创建 late job configuration 的时候，里边还记得吗？我们之前加载的是 simple job，现在变成 date flow job configuration 就这儿发生了变化，其他的都不变。然后这里边有一个参数，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/4cc39563-316a-4fe9-8486-baa6e659ab5f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZLGIZIOB%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDsT15l7Z7B1B%2BJ4Cwnqf2xX6q%2B9dTc3pR8f751r0rJrgIhAKOSuU83OMHZp46MeWvVw9NL%2BUnKXWFGIEz32TpcC72rKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz%2Fkn5SRmIzvDCGTOwq3APjHn8iAjrbHeOj65V8cqi%2FqUCyt4jlWJN1W8nH9G9J8ipT4EAJ4tdSi30YdOxyK%2F5oJRUj9H%2Ftg%2BCMZS2TsJ4QYCacqDWcPXGvjWlCLPWuome50p11xOLuy3PO2xzNTBcgNpfXbMlElauTozySw6MyKc4zWDwRAFKfCvXX%2FUfCp7R%2FyKOyQ7ZCOVdIltWnIkwk6gtmK38EadABzTlhK3ajuqZ4HKqFYk%2FqQCORmLtAefKESLan%2FmsyekngyJim1VLGfq3qVaMWn69TaOxG61Ug4r2w%2FHe16rP1FyVUqxHnTiPZsYN0CRwP2JN6yjI%2BIJ6Og5Tn0rf5YHKgh%2BDWNITDHkXxbNHrMj5JKExPRulk75MxTUVV%2BfIIcAGYyOVMVXAPkAPk6%2B%2FVT3pu9cW8DPM1YkfnzsgmqF22vtRD9gnvFJe4hAHW8qfFraABIlPEbnCY0KCCg%2FBzWX%2BADvG2Me5u8PSC%2FLF0Lnz1O8UjbyN6di8O8P1oLfDrHSDmP1PwfGXXNwr8PicOc3LfLWCWUfH5leh9KoydHyR9jvyYUUslO%2FiqjvZwJfar8OQe7g4cRs4IGxhEaKiTIx3iT%2FIjFWp71QI3AHYgz9XDYx2GBw7rvfShuH0HF8ZTrnf%2FADDyuv%2FSBjqkAb%2Fwm%2FYK45%2Frdnkh0uEdZSvtElSnN5XiVpOwsB%2FhNmVIBnzwzUCc0cvHSiNwxnXOvKCfsXkZWkAGvYWzHRLcvKkDcidtw%2FbjaQEr2BFJ2o7ab1LnWjGwXNlajlPY%2BUMMH8IJWunCLCyBNsgkDjgccJtzK8vu5EO24aGN%2B3d35H147pVaFrhPIvDcTrwpDTeUZ9cIra3fHIIp7hPPMa2TEcdnohAk&X-Amz-Signature=62f42b33238271afdec25f96072ddada563059bce5f0b18bde0697de7e71db24&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

这个很有意思，这个叫做 streaming process， streaming process 是流式的处理，就是说如果你想让 job 一直的去抓取数据，从一个数据源抓取，那我就会不停的去抓取，你会看到它里边有个配置 word 类型的 streaming process，其实我们可以点进去它的实现，我们来点进去它的 streaming process。这个就是说如果你设成true，它就是说数据流作业配置项，你设置处它就会一直不停的去抓取，你设置false，它就根据 crowd 去做处理好了。


这个是一个比较有意思的事情，然后后面其实都差不多了，然后回过头来我们继续的去看最核心的这个东西到底怎么去实现的。我们点进去我们自己实现的这个job，它里边要实现这个接口，实现这个接口叫做 dataflow job，然后他传一个泛型进来，就是说你可以指定一个对象去作业，比如说我批量的去处理一个集合，叫做 fetch date 去抓取完集合之后这就是流处理了，抓取完直接之后它会直接把抓取符合条件的数据转到 process date 下一个接口，这个 process 接口才是真正的处理。


看见了，那我在这里面定义了两个，一个叫做抓取集合的方法，打印了一句话，还有一个就是真正处理集合的数据，当然你返回空了，它肯定就没数据，那这个 process 它可能不一定能执行。如果有数据，它会把数据交给下面去做处理，你看它下面直接返回的就是上面抓取的这个集合，我们看到了，好了，那我们其实可以把它演示一下，来给小伙伴们去演示一下。


现在我们除了有 simple job，我们还有什么呢？我们还有这个下面的，把它这个注释放开，看见了叫做 data flow job， data flow job 就是每 10 秒钟执行一次，这个是每 30 秒，对吧？然后两个分片，一个是北京，一个是上海，其他的都保持不变。


好，我们直接启动这个应用服务去运行一下，我们主要来看一下是否抓取那个代码，打印了那句话就可以稍微耐心等待一下，等它初始化成功之后，我们倒计时数 10 秒，这个 query 表达式是每 10 秒执行一次。为什么执行的是新手招？那证明我们抓取那个数据它没执行，我们抓取的数据没执行是什么原因？我们停掉。


又有一个问题，为什么是 5 次？因为我们在这里设置的那个有一个配置项叫做override，对不对？就是否覆盖我们设置之前设置 true ，所以说就算你 ES 那个配置中心，你这里边改的是多少？你这里边是 10 片，但它也不以这个为准。除非什么呢？除非我把它刷新一下，我们回过头来还是看这个，你看又变成 5 了，因为什么？因为它是告诉你以那个配置为准，那个配置是 5 片，那你就是 5 片，就这意思，除非干什么？除非你把那个 simple job 里边的配置改了，对不对？你把那个 override 这个设置成什么？设置成false。正常工作中我们一般都是设成false， simple job 设成false，然后刚才我们的这个具体的那个 data flow job，其实它也有个 override ，我们也给它设成 false 就好了。


这两个参数我们都以 ZK 为准，为什么它不执行？是不是我们少configuration？是不是我们刚才把它注释掉了，他们根本就没读这个配置？这个问题重新再来启动一下我们的应用服务。好，我们来观察一下具体的这个日志输出。好，你看到这了就证明已经注册成功了，你看抓取数据它肯定会执行，是不是？每次抓取数据为什么执行两次？因为我们是两个片，对吧？还记得吗？我们配置文件配的时候配的是两个片，抓取数据是不是 20 秒我把它清空，我们配置的时候配置只是 2 片，所以说每次执行 2 片，对不对？有的同学说，老师，那这个抓取数据执行了，下面那个 process date 为什么没执行啊？这个 process data 为什么没执行？我们来找到那个 spring 的 data flow job，就是说处理数据的集合，为什么没执行，而只执行的是抓取数据的集合？原因很简单，就是因为你这里边没数据，他就不会帮你转到下面，他自己很智能的。那怎么办？那如果你同时想看到这个效果，很简单，我们把它再搞一下这个玩意儿，你把它弄出来就好了嘛，这不是个集合嘛，我们说 list 等于，当然现在我们都写死了的哈。


又一个releast，然后这个 list 给他艾特两条数据，艾特一个，当然他是一个 for 这个对象，他有两个，一个 ID ID，我们叫做001， name 叫做张三。然后还有一个人毋庸置疑，那就是李四了。好，然后最后把这个 list 返回，看见了，这回每次抓取都能抓到张三李四这俩哥们，然后我们看一看下面到底处不处理，是不是这个 list 里边肯定会有张三李四这俩哥们吗？当然，我们来试一下，只有做实验你才能知道他自己的这个处理的结果。


唉，同学们看到了吗？他这是什么鬼？老师，你之前不是说每隔 10 秒钟才执行一次，但是你现在我这怎么一直抓取一直处理呢？那起码咱们能印证的一点是什么呢？这里边有数据的时候肯定能走到下面去处理嘛，对不对？唯一还有一点你可能不了解的是，这怎么一直时时在玩，他不按照我们的 crowd 表达式去走吗？我这里面 cross 是每 10 秒一次，注意这里边有个特性，我们在这里设置什么 streaming 等于true，看见了这个 streaming 就表示你是否是流处理，就一直去抓数据。如果你把它 stream 设成 false 的话，我们再请同学们请看，这里边有几个关键的配置，在实际工作中大家一定要注意什么概念？ streaming 的意思就是不按照你的 CROWN 表达式去走了，我就是实时的去玩，实时的去抓，处理完了之后有数据就给你扔到下一个 process date 里边，你自己去处理。如果非streaming，那么就是按照定时任务去走，你看这回他就消停多了。


OK，这个 streaming 设置成 false 之后，override，我们来刷新一下，现在有两个 job override，它有一个配置项是否覆盖 date flow 的方式？尴尬的原因是因为它是以这个为准的。看见了，你看我把这个去掉哈。 streaming process 这个勾去掉，然后 submit 好了。那现在呢？我们来看这个 streaming 这个勾已经没有了，我现在就把它关掉了，然后再回过头来看代码，就是刚才我们虽然说改 false 了，但是你不生效。原因是因为我是以 JK 为主的，因为这个 override 那个参数就是我虽然说这改成 false 了，但是这个 over ride 不以本地配置为主了，我是要以 ZK 配置为主，对不对？所以说你只你在这改没意义，你重启服务也没意义，你只有干什么呀？只有去修改 to keeper 上的这个配置，你把它这个勾去掉，这样的话它才会生效，才会有意义，我们耐心等待一下哈。


你看抓取数据处理数据是不是 10 秒钟一次，这回就消停多了？它不是这种实时的了，它是按照 count 表达式正常的去，每过 10 秒钟他去抓一批，然后去处理，每过 10 秒钟他去抓一批去处理，他现在是按照正常的流程去走了，对不对？按照 crowd 去走了，OK，那这一块其实有几个比较关键的参数，就是 streaming 以及override，我们充分的去通过实验证明了它到底是干什么用的。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/6c58e3d5-c40a-4f46-9265-d5dada2d171a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZLGIZIOB%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225308Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDsT15l7Z7B1B%2BJ4Cwnqf2xX6q%2B9dTc3pR8f751r0rJrgIhAKOSuU83OMHZp46MeWvVw9NL%2BUnKXWFGIEz32TpcC72rKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz%2Fkn5SRmIzvDCGTOwq3APjHn8iAjrbHeOj65V8cqi%2FqUCyt4jlWJN1W8nH9G9J8ipT4EAJ4tdSi30YdOxyK%2F5oJRUj9H%2Ftg%2BCMZS2TsJ4QYCacqDWcPXGvjWlCLPWuome50p11xOLuy3PO2xzNTBcgNpfXbMlElauTozySw6MyKc4zWDwRAFKfCvXX%2FUfCp7R%2FyKOyQ7ZCOVdIltWnIkwk6gtmK38EadABzTlhK3ajuqZ4HKqFYk%2FqQCORmLtAefKESLan%2FmsyekngyJim1VLGfq3qVaMWn69TaOxG61Ug4r2w%2FHe16rP1FyVUqxHnTiPZsYN0CRwP2JN6yjI%2BIJ6Og5Tn0rf5YHKgh%2BDWNITDHkXxbNHrMj5JKExPRulk75MxTUVV%2BfIIcAGYyOVMVXAPkAPk6%2B%2FVT3pu9cW8DPM1YkfnzsgmqF22vtRD9gnvFJe4hAHW8qfFraABIlPEbnCY0KCCg%2FBzWX%2BADvG2Me5u8PSC%2FLF0Lnz1O8UjbyN6di8O8P1oLfDrHSDmP1PwfGXXNwr8PicOc3LfLWCWUfH5leh9KoydHyR9jvyYUUslO%2FiqjvZwJfar8OQe7g4cRs4IGxhEaKiTIx3iT%2FIjFWp71QI3AHYgz9XDYx2GBw7rvfShuH0HF8ZTrnf%2FADDyuv%2FSBjqkAb%2Fwm%2FYK45%2Frdnkh0uEdZSvtElSnN5XiVpOwsB%2FhNmVIBnzwzUCc0cvHSiNwxnXOvKCfsXkZWkAGvYWzHRLcvKkDcidtw%2FbjaQEr2BFJ2o7ab1LnWjGwXNlajlPY%2BUMMH8IJWunCLCyBNsgkDjgccJtzK8vu5EO24aGN%2B3d35H147pVaFrhPIvDcTrwpDTeUZ9cIra3fHIIp7hPPMa2TEcdnohAk&X-Amz-Signature=9d7cfb1d50338a118f480cfa7d0184e2f89701dcdf73e07168bca98bec13394d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那也就是说希望小伙伴们在实际工作中一定要注意这两个特点，那我建议小伙伴一定要是以 ZK 为主，这里边一定要设置false，具体这个 stream 你到底需不需要，那看你具体实际的需求，如果你 stream 你确实想实时的去处理，那其实你这corn ，而是你配不配都没有意义。


OK，那在这里老师已经把关于 es job 它的两大核心，一个是 simple job，还有一个是 dataflow job，还有跟 JK 怎么去集成，跟我们的控制台怎么去用，都跟大家讲清楚了。好，那么我们后面呢，就去在真正的实际的工作中，再回到我们基础组件的封装，把这个 ES job 用到我们对于高可靠性投递消息的一个补偿，把它用上去，学完了技术我们把它用上去，这才是最nice。OK，那么这节课呢，我们先讲到这儿，感谢小伙伴们收看






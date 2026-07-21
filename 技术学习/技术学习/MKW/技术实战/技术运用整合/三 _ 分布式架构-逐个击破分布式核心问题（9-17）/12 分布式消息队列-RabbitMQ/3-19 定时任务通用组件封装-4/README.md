---
title: 3-19 定时任务通用组件封装-4
---

# 3-19 定时任务通用组件封装-4

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/119f8fc8-20ce-42b7-9daa-a040458293f5/SCR-20240806-tgrq.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNCMFJRN%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGwgpOImsrfnuHTJ1YcZua%2Bcgk69MCjKidXCQcPeDN6fAiEA5Xyc3TT6YFvX5ILlClZVdr3vCXHuZVaIhuc8jS5y3EkqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKTH2hUMWNX1CgJEhyrcA4JzMOV8TCspBwPoJfe3viIYG9O4nyNgSFv%2Bteet6V%2BeB4LgLUeoUM3unTb4j8XxILVre%2BhRNEbUDxQfd7sg4cAFm631o8qoK5c5zOzZ2ZLTZ73i1eKPQvfyD2cEdzrCoEmGn69RD2qv%2FJbYGm%2F08OT121U6Vp1bBs%2Bhp40gZwz15Sih5FVk521lbKA4QPQbQN6myDqmhPYsQrJM7JyJyjEUHVX9ihRrvBgLLSHlfO6EtW8grSAOnZVEKADPMKR6b%2Fn6bEh6mqB19mNCjSDWrQ4Q91AuMI6XTQoW3zuRRK2qwlJ0t8Fp2S42ed3z1ouzIXtchY7NNcgPcNYvW1%2BKGOz137Q2Slr%2Fj6iMxs1aZz%2FyqQgVerNJagWWzLjyxXmANVHRfzNbdodJ%2FCKamxbHDzbstL5nPtYzFmZ7AOtF9SXqcWQL02Z9NfzbJicIwWlTuNeH%2Bsj1yQSqIgK8vmwAsr0Ocq%2BUaUcqy3SArvFUHgKVgpFiHvCYds3QJdGL2HLV533CSklX%2F6vssuftSvU%2B6h%2FP5OP92oRDQczqztyf8apQRYx6vg5g0JTosMmeMkx89oa9cyYBqSBjGaDKyv63Y8JbtRz7vw1PxLAlylpe4%2BO7OcNoHwR1JkuFS%2BqWMP3O%2F9IGOqUBFSstEJ6CsV6YdCRUtR4eIDcB99pQAkrp1yfj8KQDOcD4CEX1XXQwmhEcD1JJisghN4j4xHng1LA4Q1%2BUPmHKOAd5wcDVCR4e%2FffK4EhSQpxhwePHdQA1pbPMPI7ZHioKGf2dnJbV0mZfVOM%2BRXrtGMBfGtbQnPwU%2FjJjb00FfbwrxxvEXnMvAsp8U8yzygY5C4VFS7SyEfTJaSzR7oyP21hSSIw3&X-Amz-Signature=8dc39bf536d971cb4dbb60c31914ad1da6eb9f165636152c533b5690fb268983&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/4a8a8182-3f99-4e12-ad4e-e6a7ba17737f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNCMFJRN%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225310Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGwgpOImsrfnuHTJ1YcZua%2Bcgk69MCjKidXCQcPeDN6fAiEA5Xyc3TT6YFvX5ILlClZVdr3vCXHuZVaIhuc8jS5y3EkqiAQIx%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKTH2hUMWNX1CgJEhyrcA4JzMOV8TCspBwPoJfe3viIYG9O4nyNgSFv%2Bteet6V%2BeB4LgLUeoUM3unTb4j8XxILVre%2BhRNEbUDxQfd7sg4cAFm631o8qoK5c5zOzZ2ZLTZ73i1eKPQvfyD2cEdzrCoEmGn69RD2qv%2FJbYGm%2F08OT121U6Vp1bBs%2Bhp40gZwz15Sih5FVk521lbKA4QPQbQN6myDqmhPYsQrJM7JyJyjEUHVX9ihRrvBgLLSHlfO6EtW8grSAOnZVEKADPMKR6b%2Fn6bEh6mqB19mNCjSDWrQ4Q91AuMI6XTQoW3zuRRK2qwlJ0t8Fp2S42ed3z1ouzIXtchY7NNcgPcNYvW1%2BKGOz137Q2Slr%2Fj6iMxs1aZz%2FyqQgVerNJagWWzLjyxXmANVHRfzNbdodJ%2FCKamxbHDzbstL5nPtYzFmZ7AOtF9SXqcWQL02Z9NfzbJicIwWlTuNeH%2Bsj1yQSqIgK8vmwAsr0Ocq%2BUaUcqy3SArvFUHgKVgpFiHvCYds3QJdGL2HLV533CSklX%2F6vssuftSvU%2B6h%2FP5OP92oRDQczqztyf8apQRYx6vg5g0JTosMmeMkx89oa9cyYBqSBjGaDKyv63Y8JbtRz7vw1PxLAlylpe4%2BO7OcNoHwR1JkuFS%2BqWMP3O%2F9IGOqUBFSstEJ6CsV6YdCRUtR4eIDcB99pQAkrp1yfj8KQDOcD4CEX1XXQwmhEcD1JJisghN4j4xHng1LA4Q1%2BUPmHKOAd5wcDVCR4e%2FffK4EhSQpxhwePHdQA1pbPMPI7ZHioKGf2dnJbV0mZfVOM%2BRXrtGMBfGtbQnPwU%2FjJjb00FfbwrxxvEXnMvAsp8U8yzygY5C4VFS7SyEfTJaSzR7oyP21hSSIw3&X-Amz-Signature=bbd2751f1335b42a2a9955e04f489bcb70390df10101c3c89ada3b61ac611f7a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

首先一个很重要的点就是你要做配置项，配置就是 call configuration，在这里它叫做 job call configuration，有了这个 call configuration 之后，然后才能去做其他的事情。现在还没到 spring 内部，我们现在先干什么呀？你第一件事情先把当当网的ES， job 的相关等一系列的什么 configuration 先实例化出来，然后慢慢的再把它跟 spring 做一个集成，它是一个静态的，它要做的是一个 new builder，我们直接回车。


第二， new 一个builder， new builder 里边就要传递三个参数，分别是 job name 跟 CRON 的表达式以及它的分片总数。那这三个参数我们都有了，为什么这么说？因为我们在这里 job name 看见了吗？ job name 在这里 crowd 表达式分片总数我刚才已经看到了，就是sharding， total count 这三个参数都有了，然后接下来再点儿，比如说它的 sharding item params，它有没有一些分片的参数？如果有的话加上，然后再往下去点儿，比如说它有没有一些描述description，有的话加上，然后它是否是什么啊？ fail over，你把 fail over 的属性带过来，然后它有没有 job paramo？有 job param，把那 param 拿到，然后有没有 job practice，但是这个 job practice 它的 key 是写死了，我们就叫做 job properties。


找到当当网的 job properties 点叫做 job practice item，点enument，然后有一个 job execution handler，这个 key 其实不用你去做的，你直接用当网这个 key 就好了，然后把它的 value 拿过来， value 是谁？就是我们的 job exception handler 就是它。好，然后可以再去点什么呀？ job property 这个代码都是不变的，只不过这个 key 我取的是另外的一个 key 了。另外一个什么呢？叫做 executor service handler get key，然后有没有？如果有我也拿过来，因为我这里边都当成配置项了，所以说有的话都可以带进来。


好配置完这两个最复杂的事情以后，然后我们做的一个事情还有哪些属性？我们来看一看，我们来看一下我们落没落下哪些属性。这有个属性叫做 miss fair，就是错过执行，你配了true，那就是 true get false，那就是错过就不执行了。好，这些都搞定了之后，然后调一下 build 方法，这些是不是都是我们配置的？就是我们自己做注解配置的，这这些是不是也是当网的原生API？我们就把它写到这里就好了，你没必要说每次我都搞一个配置文件，写好多次就太麻烦了。然后搞完这个事情之后，我们接下来想一想，我们有了这个 call config 之后，接下来我就很关键的一件事情了，我要来看一看我到底要创建什么样的任务，到底是 simple job 还是 dead flow job？那我们这里边有一个类型 job type configuration，这是当网的，咱们叫做 type config，等于我先去判断什么呢？就是它，如果它是简单任务的话，我们应该做什么事？这个应该跟谁做 equals 比对？就跟我们之前上面获取的这个 shop time name，我说我现在就是获取它的 simple name，如果它是 simple name 的话，那就证明你是一个简单任务。


同学们能理解吗？为什么？因为你看我们这个里边这个 simple 里面这个名字跟我们自己写的这个 simple name 是不是一致？如果这个简单名称和我们自己定义的这个名称是一致的，那就证明你是一个简单任务，因为你实现的接口是 simple job，那你肯定是一个简单任务。废话不多说，把刚才的再写一遍。 if 我们有三种类型的任务，除了有简单的，还有 data flow，然后除了有 data flow，还有一个叫做script，当然 script 用的不多。好，那我们的 job type 呢？那就很简单了，等于 new 一个 simple job configuration，然后把我自己的 call configuration 跟 job class 放进去。 call configuration 就是我刚才最核心的，这个东西是不是我第一次配置的？然后 job class， job class 就是当前的你的类的名字就是 get name，就是全名称都有了。


好，同理一样的，这我 new 什么呀？我 new 一个 data flow configuration，这里边首先 call configuration job class，还有这个东西是什么？表示你是否是这种实时的流处理？这个是不是也是配置项里头有的？配置箱里有的，我直接拿过来了，带过来了，然后接下来就是一个script，你有一个什么 script job configuration，它需要传的是一个 call configuration，加一个 script command line。


好，这个里边其实我之前在写注解的时候，这个属性我也封装了，它就是在这。OK，那不管是哪种任务，我只需要知道它实现了那个接口，它的名字跟我的这个定义的这个枚举里边的那个值到底是否一致，我就知道它到底是什么任务了。然后我就把这个 tap 取出来了，我取出来这个 tap 之后，接下来我是不是就可以往下去走？往下走什么？其实下面的事情还是当网的事情，还是去做 lead job configuration，有了这个 lead job configuration 之后，然后你就可以把它扔到我们的 sprint schedule 里了。


其实同学们你发现了这个是一个什么逻辑嘛？我们回过头来，我们看自己最开始所定义的普通的就是我们最开始所学的这个当网的 ES job，我们来看一看之前的配置是怎么样的？你看这个 simple job 它要做什么事情？它最开始在 init 的时候，它要初始化一个scheduler，这个 scheduler 是谁的？是 sprint scheduler，然后从 sprint scheduler 里边它又要获取一个东西，叫做 late job configuration。那这个 late job configuration 里边你又会看到一个叫做 job call configuration，然后又看到一个simple，它到底是简单任务还是留任务，还是说 script 任务？OK，那其实你会发现什么呢？在你去正常写代码的时候，你是先从 spring 初始化，然后再搞定什么啊？再搞定这个 late job，然后再搞定 simple job，然后再搞定call，就是 job call configuration 这样从 spring 往下来去编写的。但是同学们想一想，如果你像我刚才那样去写，你就要反着你的 spring 这个 scheduler 应该是最后一步去做，你先把什么呢？你先把这个 call simple，然后 late job 都初始化完毕之后，然后再初始化 spring 的这个scheduler，对不对？你要把下面当网，所有的东西都给它装到 sprint schedule 这个容器里，因为它你也是动态去生成的。OK，所以说这个是一个反向的过程，希望小伙伴们应该能听懂。


好了，那我们看看这个 late job 应该怎么去写吧？这个 late job configuration 很简单，就是 job configuration，然后等于 late job configuration，它也是一个静态的，需要做一个 new builder，然后这个 new builder 首先传的第一个事情就是 job config，就它到底是什么job？到底是简单job，还是说流式job，我们直接过去就好了。然后里边有一些属性，比如说 override 是否覆盖，这也是我们参数带进来的，我们可以来回车。


然后还有哪些属性？还有比如说 disable 的它到底禁没禁用？包括它的这个 monitor 的一些参数，就是说它到底有没有monitoring？ monitoring 的 point 是什么呀？然后他的 moniting 的 execution 是什么呀？接下来比如说他是不是去忽略他的这个服务器的时间？如果不一致的时候是不是要忽略还有什么？还有 job city 就是它的这个分片策略到底是什么呀？还有哪些relate，interval， minutes 是什么？然后看一下哈 monitor override 的差不多了，直接 build 好。同学们请看这些参数是哪来的？是不是也是老师封装的这个 elastic job config 里边的配置？所以说你都把它封装到这个配置里就好了。


OK，现在 late job 搞定了之后，接下来事情就是 spring 了。 spring 我们应该怎么去做？我现在我说我想要去做一件事情，就是说我要去创建 spring 的一个对象，这个对象就是我们之前例子里边的这个，就是下面这个对象以及这个 lit job 我们都已经搞定了，现在我们就要把它去搞定，就是 spring job schedule 了，然后把这个 spring jump scheduler 里边的空都填好，把这个 spring jump scheduler 给它去注入到我们的 spring 容器里就搞定了。


好，就是这么简单的一件事情，这个东西我怎么去创建spring？能不能够帮我去创建一个我想指定的一个bin？这是可以的，我们怎么去做？同学们，如果你知道这个类的话，就是创建一个 spring 的bin，叫做definition，定义 definition OK，那我们来看一看，叫做 bin definition，有这个builder，那个 builder 可以。这个就是创建 spring 的一个 bin 的一个什么？一个 definition 定义，我们叫factory，然后通过它直接等于 root 并


definition。 root 并 definition 可以了，你要创建什么class？我要创建的给你 class 就是 sprint class，就是 spring 的那个 job scheduler 点class。好，我把这个 definition 定义出来之后，它是一个什么呢？它要 set 一个 init method，我们也叫init。为什么这么去说？其实这些东西都是在最开始，你看这个方法里边本身就有一个 init method，所以说我们还是设置一下它的 name 叫init，然后接下来它是一个什么模式？ set scope，它是一个单例吗？单例就是sygotta，多例就是 Pro to type，它肯定是一个多例，为什么呢？因为我刚才老师说了，我说这个东西我现在有一个 simple job，我要写这一遍配置文件，有一个 simple job，我写这一篇配置文件，我要自己有一个sprint，这个 job scheduler 我把它扔到 sprint 里。


那如果有两个 simple 账目，那你其实相当于你不能用同一个，这肯定不行，也就说你还得去把这个东西 control 私域，就把这个整体 Ctrl c、 Ctrl v 再写一个，然后你那个名字，你注意这个里边它注入到 b 的名字叫这个那个，你肯定要知道这个 r 了，肯定要不一样的。所以说我跟你说一定是prototype，就是一个多例，肯定不是单例的话，那肯定不行，多例才可以。


OK，然后接下来接下来的事情不就是往我的这个并 definition 里边去填充它的一些构造器的一些参数吗？说白了还是在这里就是我要对它拗出来，它，我要添一堆这些参数，这一堆参数是不是我刚才老师写了那么半天写的那些东西，我们就把它都添上就好了，就往里去添一些constructor，那在这里呢？下面的代码其实很简单，老师在这把这个也是 copy 一下，然后跟小伙伴们来讲一下，因为这个代码其实没有什么含量。


OK，我们来看一下哈 elastic job type， enumer 写错了哈，sorry，应该是ENU，重点是 e n u m，这是对的。然后这个 job config 是我们之前所看到的，我先把它最大化一下，它现在报错的地方，我先把它注释掉，这块起码是不报错了。然后这个叫做add，这个 scheduler 里边当成一个构造器去用，然后同时 do capture 也是一样的，就是registry，这个 registry 我们也要给它放到构造器里。


这个东西是怎么来的？其实大家有兴趣的话可以看一看这个东西，你可以看一下我们这个还是 simple job 它的配置吗？ 

simple job 它的配置是不是？我是不是要这构造器？我也要这个 late job，它就四个东西，当前这个 simple job 是什么？还有注册中心是什么？还有这个 lead job configuration 是什么？以及它有没有什么trace，就是跟数据库相关的，就是我们可以看到轨迹的以及它的这个 simple job listener，这个 listener 可有可无了都，如果你有 listener 你可以用，没有 listener 其实你完全可以干什么呀？把这去掉可不可以？也可以少参数，没问题。好了，那其实呢，我们现在做的事情，第一个事情就是把当前这个 bin 放进去，当然只要它不是脚本，那它肯定是Java，那我就可以放进去，然后 registry center 放进去。

接下来 job config，这个 job config 就在我们上面，找到，找我 config 他为什么报错？我们来看一下，写错了， job config，OK， job config 有了添加并的构造器参数相当于什么呢？相当于添加自己的真实的任务实现类，然后这个就不用说了，相当于添加注册中心，然后这个东西就是添加 late job。好，这是第一步，这是第二步，这是第三步。那你可以对应上我们之前所学的那个 simple job，你会看到这三步是不是就相当于就这是自己真实的job？第一个，然后注册中心，然后 late job 还是要俩东西，一个是什么呢？ event 是不是是否有这个job？ event configuration 就是说数据库里是否要记录一些trans，一些这个定时任务执行的一些日志，或者是最后一个你是否有listener，就是你自己定任务是否要有坐监听。

```java
package com.bfxy.rabbit.task.parser;

import com.bfxy.rabbit.task.annotation.ElasticJobConfig;
import com.bfxy.rabbit.task.autoconfiguration.JobZookeeperProperties;
import com.bfxy.rabbit.task.enums.ElasticJobTypeEnum;
import com.dangdang.ddframe.job.config.JobCoreConfiguration;
import com.dangdang.ddframe.job.config.JobTypeConfiguration;
import com.dangdang.ddframe.job.config.dataflow.DataflowJobConfiguration;
import com.dangdang.ddframe.job.config.script.ScriptJobConfiguration;
import com.dangdang.ddframe.job.config.simple.SimpleJobConfiguration;
import com.dangdang.ddframe.job.event.rdb.JobEventRdbConfiguration;
import com.dangdang.ddframe.job.executor.handler.JobProperties;
import com.dangdang.ddframe.job.lite.config.LiteJobConfiguration;
import com.dangdang.ddframe.job.lite.spring.api.SpringJobScheduler;
import com.dangdang.ddframe.job.reg.zookeeper.ZookeeperConfiguration;
import com.dangdang.ddframe.job.reg.zookeeper.ZookeeperRegistryCenter;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.support.BeanDefinitionBuilder;
import org.springframework.beans.factory.support.DefaultListableBeanFactory;
import org.springframework.boot.context.event.ApplicationReadyEvent;
import org.springframework.context.ApplicationContext;
import org.springframework.context.ApplicationListener;
import org.springframework.util.StringUtils;

import java.util.Iterator;
import java.util.List;
import java.util.Map;

/**
 * <h1>解析注解</h1>
 */
@Slf4j
public class ElasticJobConfParser implements ApplicationListener<ApplicationReadyEvent> {

    private JobZookeeperProperties jobZookeeperProperties;

    private ZookeeperRegistryCenter zookeeperRegistryCenter;


    public ElasticJobConfParser(JobZookeeperProperties jobZookeeperProperties, ZookeeperRegistryCenter zookeeperRegistryCenter) {
    }

    /**
     * Handle an application event.
     *
     * @param event the event to respond to
     */
    @Override
    public void onApplicationEvent(ApplicationReadyEvent event) {
        try {
            ApplicationContext applicationContext = event.getApplicationContext();

            Map<String, Object> beanMap = applicationContext.getBeansWithAnnotation(ElasticJobConfig.class);

            for (Iterator<?> it = beanMap.values().iterator(); it.hasNext(); ) {
                Object confBean = it.next();
                Class<?> clazz = confBean.getClass();

                if (clazz.getName().indexOf("$") > 0) {
                    String clazzNmae = clazz.getName();
                    clazz = Class.forName(clazzNmae.substring(0, clazzNmae.indexOf("$")));
                }

                /** 获取接口的类型， 判断是什么类型的任务 */
                String jobTypeName = clazz.getInterfaces()[0].getSimpleName();
                /** 获取配置项 ElasticJobConfiguration */
                ElasticJobConfig conf = clazz.getAnnotation(ElasticJobConfig.class);
                String jobClass = clazz.getName();
                String jobName = this.jobZookeeperProperties.getNamespace() + "." + conf.name();

                String cron = conf.cron();
                String shardingItemParameters = conf.shardingItemParameters();
                String description = conf.description();
                String jobParameter = conf.jobParameter();
                String jobExceptionHandler = conf.jobExceptionHandler();
                String executorServiceHandler = conf.executorServiceHandler();

                String jobShardingStrategyClass = conf.jobShardingStrategyClass();
                String eventTraceRdbDataSource = conf.eventTraceRdbDataSource();
                String scriptCommandLine = conf.scriptCommandLine();

                boolean failover = conf.failover();
                boolean misfire = conf.misfire();
                boolean overwrite = conf.overwrite();
                boolean disabled = conf.disabled();
                boolean monitorExecution = conf.monitorExecution();
                boolean streamingProcess = conf.streamingProcess();

                int shardingTotalCount = conf.shardingTotalCount();
                int monitorPort = conf.monitorPort();
                int maxTimeDiffSeconds = conf.maxTimeDiffSeconds();
                int reconcileIntervalMinutes = conf.reconcileIntervalMinutes();


                /** 先把当当网的 esjob 的相关 congfiguration 配置上 */
                JobCoreConfiguration coreConfiguration = JobCoreConfiguration.newBuilder(jobName, cron, shardingTotalCount)
                        .shardingItemParameters(shardingItemParameters)
                        .description(description)
                        .jobParameter(jobParameter)
                        .misfire(misfire)
                        /** 当当的原生 api */
                        .jobProperties(JobProperties.JobPropertiesEnum.JOB_EXCEPTION_HANDLER.getKey(), jobExceptionHandler)
                        .jobProperties(JobProperties.JobPropertiesEnum.EXECUTOR_SERVICE_HANDLER.getKey(), executorServiceHandler)
                        .build();

                JobTypeConfiguration typeConfig = null;
                if (ElasticJobTypeEnum.SIMPLE.getType().equals(jobTypeName)) {
                    typeConfig = new SimpleJobConfiguration(coreConfiguration, jobClass);
                }

                if (ElasticJobTypeEnum.DATAFLOW.getType().equals(jobTypeName)) {
                    typeConfig = new DataflowJobConfiguration(coreConfiguration, jobClass, streamingProcess);
                }

                if (ElasticJobTypeEnum.SCRIPT.getType().equals(jobTypeName)) {
                    typeConfig = new ScriptJobConfiguration(coreConfiguration, scriptCommandLine);
                }

                /** LiteJobConfiguration */
                LiteJobConfiguration jobConfig = LiteJobConfiguration
                        .newBuilder(typeConfig)
                        .overwrite(overwrite)
                        .disabled(disabled)
                        .monitorExecution(monitorExecution)
                        .maxTimeDiffSeconds(maxTimeDiffSeconds)
                        .reconcileIntervalMinutes(reconcileIntervalMinutes)
                        .build();


                /** 创建一个 spring 的 beanDefinition */
                BeanDefinitionBuilder factory = BeanDefinitionBuilder.rootBeanDefinition(SpringJobScheduler.class);
                factory.setInitMethodName("init");
                factory.setScope("prototype");

                /**	1.添加bean构造参数，相当于添加自己的真实的任务实现类 */
                if (!ElasticJobTypeEnum.SCRIPT.getType().equals(jobTypeName)) {
                    factory.addConstructorArgValue(confBean);
                }
                /**	2.添加注册中心 */
                factory.addConstructorArgValue(this.zookeeperRegistryCenter);
                /**	3.添加 LiteJobConfiguration */
                factory.addConstructorArgValue(jobConfig);

                /**	4.如果有eventTraceRdbDataSource 则也进行添加 , 是否需要数据库中记录一些定时任务的日志啊 之类的*/
                if (StringUtils.hasText(eventTraceRdbDataSource)) {
                    BeanDefinitionBuilder rdbFactory = BeanDefinitionBuilder.rootBeanDefinition(JobEventRdbConfiguration.class);
                    rdbFactory.addConstructorArgReference(eventTraceRdbDataSource);
                    factory.addConstructorArgValue(rdbFactory.getBeanDefinition());
                }

                /**  5.添加监听 */
//                List<?> elasticJobListeners = getTargetElasticJobListeners(conf);
//                factory.addConstructorArgValue(elasticJobListeners);
//
//                // 	接下来就是把factory 也就是 SpringJobScheduler注入到Spring容器中
//                DefaultListableBeanFactory defaultListableBeanFactory = (DefaultListableBeanFactory) applicationContext.getAutowireCapableBeanFactory();
//
//                String registerBeanName = conf.name() + "SpringJobScheduler";
//                defaultListableBeanFactory.registerBeanDefinition(registerBeanName, factory.getBeanDefinition());
//                SpringJobScheduler scheduler = (SpringJobScheduler)applicationContext.getBean(registerBeanName);
//                scheduler.init();
//                log.info("启动elastic-job作业: " + jobName);

            }
        } catch (Exception e) {
            // TODO
            e.printStackTrace();
        }
    }
}
```


那接下来我们再看吧，这代码也是一样的，应该是 spring framework。okay，就说如果有这个值的话，那我干什么呀？我要定义一个，你看 root bin definition，但是这里面叫做 job event RDB configuration，对于这个轨迹就是trace，相当于定制任务执行完了之后，如果我们想记录一些，就是一些时机，那我们可以去加上这个bin，然后把这个 bin 给它加上一个 constructor 就是它，然后把它再装进我们的factory。所以说这个就相当于第四步，就跟我们 simple job config 里边的这一步就是它一样的。然后最后就是 listener 了， listener 就更简单了，然后第五步就是添加监听listener，这个添加监听其实有两种，它有一个分布式的 distributor listener，还有一个本地的这个listener，所以说老师在这里直接把代码给大家拿过来，然后让大家看一下，就。


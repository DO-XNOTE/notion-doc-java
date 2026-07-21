---
title: 3-20 定时任务通用组件封装-5
---

# 3-20 定时任务通用组件封装-5

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/fa5a4cd9-9c71-40a9-9aeb-7c689959b2d1/SCR-20240807-fcmj.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YNCKXZLB%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCYkxKMk2LaJ2FIDBE1YSYTxDga%2FcTf4kW%2BPXPxZZ3EgQIgdBVv4F%2BA87eovQHrQ5UX%2BfG8zpNsf%2BTQytllBobdSTcqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPr7yNvacHHsYQgQ7CrcA0QAQwAPgLcvFsE3tCyH2u1TMxy%2FNyp8lI7vQdKNU%2FuEwbWykSbFTkK%2FrxAMiS45njNsuxBdNLehC1FmTxiaNKlDPKlKePd2GU3XGbZA5r3ouHdAroWK%2FYgovb3%2B%2Bujw4F7fUUPcSMwjwYW84ASXfQwpByuwH9QiV2Tb6AZycJe%2BiKVhzr4QFzboUmk7jCAsExPNO6F88y5Ekp6WIpkyigU9aObt%2BPgiggEXcQf%2BYw32rPBc5rycL%2BVsnprnsxlW6jPdGxuuFc7vvJAty2JGBTDeWennCYqk4y4PooByCZKFWuG%2FjiBAiIi4PRCjuiWc5syfAFHC583j6LNsMqAc%2BlvNZUOpn%2FJcvlMwOdv4Qb3Y28b8nHcV7nJPn4GnIgW91loNp0thI6u1%2FgG%2BsdgyKF6TgFmkyvGN%2FdhrBAy61d2C89xLqLPQHCUOB8OVktQwQBX2hW1Gygxdfsk%2BQbR94E1O0u%2FFjgzVuQgQxrzyoUomrhVDIx3Gtuuc3keTpSzXAJwUMJBj8t7IjgznVPPbmqA58BZTyjXC4221yEpOwj0r8EaCUCttK5MCoIyIjw8R0v7NulBIPd0Ya8qRy8A%2F19PcAq3imX4bKh9jM%2BMBWJj1JQ4OSbdlCJjujwFcML%2B7%2F9IGOqUBnkTb0R5eIJ3eyFYrtw0TH%2BEGr9fts1yjvGYp6EaCbT86LZIOXJeJq9Lg1EMsc0XBnaPF0r3Jn4v52z6XA%2BQTy3BBawmHcLT2ZKJMBuGD1dyayV3b%2BT82Urmuvc%2F8YOqon7SSy19yYYTM1FhfWskRMX6BHdvfSkj3mOdX%2F4UDk9kuIjAp2YySUFgZ%2Fps0el4t8RmRg8dmbUj9MELYKMfk0tR9yxW6&X-Amz-Signature=1c320ee9e71952621ea02c78d1cc0481be9d8aca068aef61fa8520919805a987&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/baeda78c-ddf4-4ef8-9cd4-9c8df512a0a5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YNCKXZLB%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225311Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCYkxKMk2LaJ2FIDBE1YSYTxDga%2FcTf4kW%2BPXPxZZ3EgQIgdBVv4F%2BA87eovQHrQ5UX%2BfG8zpNsf%2BTQytllBobdSTcqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPr7yNvacHHsYQgQ7CrcA0QAQwAPgLcvFsE3tCyH2u1TMxy%2FNyp8lI7vQdKNU%2FuEwbWykSbFTkK%2FrxAMiS45njNsuxBdNLehC1FmTxiaNKlDPKlKePd2GU3XGbZA5r3ouHdAroWK%2FYgovb3%2B%2Bujw4F7fUUPcSMwjwYW84ASXfQwpByuwH9QiV2Tb6AZycJe%2BiKVhzr4QFzboUmk7jCAsExPNO6F88y5Ekp6WIpkyigU9aObt%2BPgiggEXcQf%2BYw32rPBc5rycL%2BVsnprnsxlW6jPdGxuuFc7vvJAty2JGBTDeWennCYqk4y4PooByCZKFWuG%2FjiBAiIi4PRCjuiWc5syfAFHC583j6LNsMqAc%2BlvNZUOpn%2FJcvlMwOdv4Qb3Y28b8nHcV7nJPn4GnIgW91loNp0thI6u1%2FgG%2BsdgyKF6TgFmkyvGN%2FdhrBAy61d2C89xLqLPQHCUOB8OVktQwQBX2hW1Gygxdfsk%2BQbR94E1O0u%2FFjgzVuQgQxrzyoUomrhVDIx3Gtuuc3keTpSzXAJwUMJBj8t7IjgznVPPbmqA58BZTyjXC4221yEpOwj0r8EaCUCttK5MCoIyIjw8R0v7NulBIPd0Ya8qRy8A%2F19PcAq3imX4bKh9jM%2BMBWJj1JQ4OSbdlCJjujwFcML%2B7%2F9IGOqUBnkTb0R5eIJ3eyFYrtw0TH%2BEGr9fts1yjvGYp6EaCbT86LZIOXJeJq9Lg1EMsc0XBnaPF0r3Jn4v52z6XA%2BQTy3BBawmHcLT2ZKJMBuGD1dyayV3b%2BT82Urmuvc%2F8YOqon7SSy19yYYTM1FhfWskRMX6BHdvfSkj3mOdX%2F4UDk9kuIjAp2YySUFgZ%2Fps0el4t8RmRg8dmbUj9MELYKMfk0tR9yxW6&X-Amz-Signature=2b711516d9e0e4a1ac1c341b51382439b3538e36d12e24f981df87ea7b235c60&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

这个里边我们其实已经有一个 class 了，我们在这里把这个下面的代码 **control shift o 都包导进来**。它有两种类型，一个是正常的listener，如果你想创建一个正常listener，你 1 都是用这种 bin definition builder 去做一个 root builder，然后对 listener 或者对这个 distribute listener，它是两个类，这两个类是我们自己配置的。


在我们注解配置的这下面，在这 config listener 是不是就是它？还有 distribute listener 也是一样的，就这两个 list 默认都是空，但是如果你配了的话，我就可以帮你把 listener 也注入进去，那我在这个逻辑就是判断它到底使用的是正常的 listener 还是 distribute listener，然后最终把这个 listener 或者是 distribute listener，它的这个 bin definition 去创建出来，然后最后把它返回他要么是第一种，要么是第二种，只能是一种然后返回好了。


那这样的话我们回过去接下来的事情就是添加listener，添加监听，这个添加监听就很简单了，我们知道这个监听是什么了，我们就调这个方法就好了。 get 把 config 就是 ES job 的那些配置传进去，然后它会帮你去返回你具体的这个 bin definition，如果你不确定它是什么的话，你写一个问号其实也可以，我们叫做 elastic job listeners。好，然后最终我们直接还是教这个方法，很简单，把它 lessness 扔到里边就可以了。


这 5 步做完了之后，相当于我们整个已经把我们 spring 的这个 job skater，它里边的一些构造参数都已经帮忙设置好了，接下来这个事情这个 factor 要做什么呢？接下来是不是你就是想方式去把它扔到 spring 里，把这个对象给它注入到 spring 里就可以了，对吧？所以说接下来的事情很简单，就把它注入到 super 里就好了。


接下来就是把 factor 对象，也就是我们的 spring job scheduler 注入到 spring 容器中，很简单，对不对？那这个怎么去注入到 spring 游戏中？我们现在这个时机是非常的好。 event 是叫做 application read event 就是啥都有，就是要什么有什么的一个阶段，直接 application context get all to where auto wear 的 chapel bin factory，这是什么意思？同学们有没有用过这个类？这个类就是说能够帮我们去做一个自动注入它，返回一个这个类，或者我们直接用它的子类叫做 default list。

In factory, just people are listable.


inside free 有了它之后，那我们要强转一下，通过这个方法我们拿到了这个对象，这个对象能够帮我们去做自动的注入，要直接调它的什么registry，看见了它 registry bin definition 已经有了，然后 b name 是什么呢？在这里起个名字，这个叫做 register a name 可以，那我们叫做 config name，然后再加上 job skater，你现在是相当于把 spring job skater 实例化了，然后把它的这个一些构造参数都填充好了。接下来你只需要把 spring 你弄出来这个 spring job scheduler，给它注入到spring，那一串就直接都在 spring 里了。OK，好了，那其实这个 register name 我们知道是它，然后这个 bin definition 我们 factory 都有了，那 bin definition 不很简单，在 get bin definition 知道好，把它注入到 spring 以后，然后放到 spring 里了。


接下来我们干什么？我们是不是要启动点 get in，对不对？我们知道 be name 吗？知道，我们注入的时候就叫做 registry be name。我们让我把它拿出来，它一定是我们想要的那个 screen job scheduler 是一个 spring job scheduler，我们就可以拿到scheduler，然后它得做一个强转，拿到这个 scheduler 它的 inmate 方法，对不对？这就相当于启动了 spring 这个任务，然后我可以打印一句话，我可以打印说这个 job 已经启动了，在这里我用一个s，l，f， o g 下面在这里打印一下log，点 info 说启动 elastic 杠 job 作业，把这个 job 内幕输出一下是不是 job name 就是我们之前所定义的那个项目。


name 是最开始在这里就是你的租 keeper 的，他的 name space，然后再加上你的 config name，OK，好，回过头来搞定了之后，然后这是负循环，里边我只处理了一个同学们想一想他如果说有 10 个类都带这个 e last job，那刚才我写的这一大坨逻辑他要执行 10 次。


所以说在最外面我说我能不能统计一下这个总共起了多少个兆，是不是共计启动作业数为多少个，可以用一个大括号表示，然后这里边就是有多少个卖法就是多少个了。 sense OK，搞定了，然后如果抛异常呢？其实你的 ES job 抛异常了，你就打着 l 吧， e r o r，然后说 elastic job 启动异常，然后比如说系统强制退出，对不对？就不让系统起了，那 ES job 起都起不来，那是说明有问题，那系统强制推出是 system s t e 是吧？搞定了，那其实我们已经把整个自己去封装的一个 e s job 这么一个小的基础组件到这里，就已经封装好了。


已经封装好了之后，然后接下来差什么事就我们做一下测试，对吧？怎么去做一下测试呢？这个很简单，我们之前不是有了这个 ES job 嘛，对吧？有了这个之前有了这么一个 ES job 了，我已经把这个包引到这里边了，是不是？我之前已经引了这个 rabbit task 到里边了哈。OK，那就可以了。那这样的话，我说我现在，我说这个 application 里边我要加一个注解。加什么注解？叫做 enable elastic job，这是第一步，第二步我们要做的事情就没有意义，暂时没有意义。我们把这个之前 job 相关的这个配置我都注释掉，我把这个 configuration 注释掉就可以了。注意这个 configuration 注释掉，然后 simple job 这个 configuration 注释掉，只要这个 configuration 注释掉，它就都不会写了。这个都注释掉，看见了吗？我全都注释掉。这个已经是注释的。好，我都保存哈。


然后比如说它里边有一些这个listener，还有一些什么，什么service，什么我都不管了，这这都不管了？然后他这个就相当于我们现在应用服务，只要起来相当于什么也没做，那这些都是不可用的。比如说我这里边是 5 秒钟一次，然后这些地址肯定也都不会去读嘛？我们来起一下。


先这是一个普通的工程， 4 分布的来起一下，他只能帮我去起了一下那个他的 IP 端口，然后我们看到他起来的时候，对，是881，我的配置文件里它只有这个 881 起到作用，其他的配置肯定都不起到作用。因为 5 秒钟一次对不对？现在肯定超过 5 秒了，就这些配置都是没有意义的，可以理解。


因为什么呢？因为我把所有的 configuration 全都注释了，看见了，全都注释了，没有意义，好，我停掉，停掉之后，然后我们按照我们自己刚才封装的那个东西，然后我们来做一下，看看 o 不OK？其实这里边的这些配置我们也都给它干掉，先都注释掉了，反正都没用，包括租 keeper 这些都没用，都注释掉，然后呢？我们来看一看，我说我自己想要配哪几个，配两个就够了。


第一个就是你对应的它的那个配置，就是从这个 auto configuration 必须要配的这两项，就是它里边的 name space 跟 server list，也就是说我其实在这里边我就配他点什么叫做 names pace，然后等于我们还是按照这个叫做 e s c job，然后还有一个配置项，这回变了，叫做 server lists 点 so list 它的值是什么呀？它的值就是我们之前那个地址，对吧？我们直接粘过来放到这里，我现在 ZK 也是起着的好，就配这两个，其他的都不配。


这是第一步，做完了第二步当前刚才我们 enable 也启动了哈， enable 这个注解也是 OK 的，这个没问题。然后我这里边是扫描到这个 es 的 job 点星浪，所以说这没问题。我们在这里边再建一个package，叫做test，可以就我们这不要做测试，我们自己就写一个实现 simple job 的这么一个自己的一个类，咱们叫做 test job 就简写，然后呢？它 implements 我们的 simple job，然后实现它是当网的这个 l 实现对应的 excuse 的方法对不对？这个 excuse 的方法我们表示说执行 test job，就这么写一句话，然后加上我们自己的配置，只要加上我们配置成功，那就认为我们的 simple job 就是自己的。这个注解确实是 OK 的，就自己封装这东西确实 OK 的。然后有个特点就是说你必须要给它加一个艾特component，就必须要保证它是在我们 spring 中的，在 spring 中然后再去扫描这个类，加上你自己的注解就是 elastic config， job config，它里边有几个必须要填的，第一个就是那个name，是不是必须要填 name 等于什么呢？就等于你的权限命名 test 点 test dog 权限命名。


然后第二一个就是它的 ground 表达式是什么？ground，ground，它比如说我们就粘过来说它是那个 5 秒钟一次，那这个是 5 秒钟一次，找一下就这五秒钟一次， 5 秒钟跑一次。然后接下来比如说它有什么呀？description，你写一下，这就是对这个你自己写的定时任务的一个描述，这就是一个测试定时任务。然后接下来比如说 over ride，我们说让它等于true，然后我们再搞一个比较关键的叫做 sharding total count，比如说我们这里边分几片？分 5 片可以吗？OK，搞定，其他的我都不要了，我就这样写完了。其实这些配置你完全也都可以配到配置文件里，那你有说意思吗？但是我们说我们就用这个我们现在的这个注解来搞一下，看看行不行？现在这是 test job，然后我们再来一个，咱们叫做 demo job，看见了。


好， demo job 跟 test job 其实是一样的，看见了吗？一样的，只不过这个里边我们叫做 demo job，看见了吗？然后这个叫做样例样例定时任务，然后之前那是 5 秒钟一次，这个我比如说是 10 秒钟一次，OK，那例如说意思几个分片，我就说两个分片可以吗？这没问题。然后这个叫测试 test job，这个我叫做测试 demo job。好，同学们请看，我现在呢里面有两个定时任务，对不对？一个是 5 秒钟执行一次是 test job，还有一个是样例定时任务，是 10 秒钟执行一次。


好，那我们来看一看，走着 right spring boot application 你看行不行？唉，报错了哈，这里边说这是 date source 的问题，就跟我们现在目前的这个没有太大的关系，我们把这个放开一些，因为我们配置了一些 MySQL 相关的东西了，所以说因为我们自己有这个 GDBC starter，你等他注释他读取就失败了。那现在这个 schedule 看已经打印这句话了。

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
import com.sun.org.apache.bcel.internal.generic.FADD;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.config.BeanDefinition;
import org.springframework.beans.factory.support.BeanDefinitionBuilder;
import org.springframework.beans.factory.support.DefaultListableBeanFactory;
import org.springframework.beans.factory.support.ManagedList;
import org.springframework.boot.context.event.ApplicationReadyEvent;
import org.springframework.context.ApplicationContext;
import org.springframework.context.ApplicationListener;
import org.springframework.context.annotation.Bean;
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
                List<?> elasticJobListeners = getTargetElasticJobListeners(conf);
                factory.addConstructorArgValue(elasticJobListeners);

                /** 	接下来就是把factory 也就是 SpringJobScheduler 注入到Spring容器中 */
                DefaultListableBeanFactory defaultListableBeanFactory = (DefaultListableBeanFactory) applicationContext.getAutowireCapableBeanFactory();

                String registerBeanName = conf.name() + "SpringJobScheduler";
                defaultListableBeanFactory.registerBeanDefinition(registerBeanName, factory.getBeanDefinition());
                SpringJobScheduler scheduler = (SpringJobScheduler)applicationContext.getBean(registerBeanName);
                scheduler.init();
                log.info("启动elastic-job作业: " + jobName);
            }
            log.info("共计启动elastic-job作业数： {}  个 "  + beanMap.values().size());
        } catch (Exception e) {
            log.error("elastic-job 启动异常， 系统强制退出", e);
            System.exit(1);
        }
    }

    private List<?> getTargetElasticJobListeners(ElasticJobConfig conf) {

        List<BeanDefinition>  result =  new ManagedList<BeanDefinition>(2);
        String listeners = conf.listener();
        if (StringUtils.hasText(listeners)) {
            BeanDefinitionBuilder factory = BeanDefinitionBuilder.rootBeanDefinition(listeners);
            factory.setScope("prototype");
            result.add(factory.getBeanDefinition());
        }
        String distributeListenners = conf.distributedListener();
        long startedTimeoutMilliseconds = conf.startedTimeoutMilliseconds();
        long completedTimeoutMilliseconds = conf.completedTimeoutMilliseconds();

        if (StringUtils.hasText(distributeListenners)) {
            BeanDefinitionBuilder factory = BeanDefinitionBuilder.rootBeanDefinition(distributeListenners);
            factory.setScope("prototype");
            factory.addConstructorArgValue(Long.valueOf(startedTimeoutMilliseconds));
            factory.addConstructorArgValue(Long.valueOf(completedTimeoutMilliseconds));
            result.add(factory.getBeanDefinition());
        }
        return result;
    }
}
```

这是 demo job，这是 test job，这是 test job 执行了 demo job 是 10 秒钟执行一次，看见了吗？然后 test job 是 5 秒钟执行一次，下一次的时候我的 demo job 和 test job 一起执行，然后再执行肯定是 test job，对不对？它没到 10 秒的话， demo job 相当于我们的 test job，执行 10 次它才执行 2 次，OK，那我们现在自己封装的这个分布式定时任务就是基于我们的这个spring，然后帮我们去省了非常非常多的事情，我们只需要简单的去做这一点注解就可以去把原生的那种 config 方式，就很复杂的 config 方式，我们把它封装起来了就很简单的就给搞定了好了。


那么其实我们整个的这个对于 ES job 基础组件的这个封装就已经讲了，那我希望通过学习如何去封装，然后跟着老师一步步走，其实你也就相当于对这个 ES job 其实理解就更深入了。对于封装这块大家应该也是学到了一些，如果小伙伴们之前有对 spring 就比较了解的话，那这个其实相当于你也应该能理解。如果说你对 spring 就了解的不是很多的话，那我觉得这个小 demo 其实是比较有意义的，在你实际的工作中有各种各样的场景，可能会需要你用类似的这种方式去做相关的分装。好了，感谢小伙伴们对这进行收看。


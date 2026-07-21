---
title: 2-1 电商系统集成Hystrix - 基础组件Turbine 
---

# 2-1 电商系统集成Hystrix - 基础组件Turbine 

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/1adb823d-eaa8-4c2c-ae7d-a50bc0267817/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2OSU26G%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225654Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGRl6oucOequ6LkMdDNpEkUNsDRS883rio2A48Mec8etAiAYwTmSNzWJJjXU0M%2Fmfyf6ehZ8OUYE2pZDdfRR5cUUfCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMrr4cyNhkDAYqClYKtwDx%2BD153H1JnS5wf6LjVGcVMezM1TyFFSEZhuPaJxmBpE%2FSBXD0x6eRvhVPNHq%2B9hVs2H9uUJG8KEsSVF%2FAfUBVpd4zk%2FZDxXSnSI1xN1Vul831G3Fr0IDzhL9V%2B3IyovqNnIbHAe7Dbm4257hJT4I0iJLOdz0HcdpPUgh3h06mDQgzMYIX%2BTDVAjvX0%2Bbng3HJzeivDX7Qb1cDNGTzU9qNjnPRv93DHlGC3h3M8oiNyJOmz%2FKmpApOAtnq0vJUObXnqCmY1YWSlsHwoJV3qvjDSHmKqWDcjHolbF6yJxYkn%2Bl4WFq5WIMViXHIldwVJSJrwFXb2cloR1CcbbgzkywUJWeXPYrB4aM0fp1TXv%2BHgmyBJvZNQJHnzkZgqkuorO%2BR6Hu3JePq%2FERFzYja7FfDbg5zbFtcnKHl2rhfz1mTmSnLWTM7AHV2o4XQxDzZhFwKEmaxeWK7DFDu%2FeuPFVd8x3esHXvQcQEYoHLKzVlS8kK2zEpod8wlaolC8kSRsP0Szuxyh%2FjQGkFPUoBtS7svpPl7QlzuyFa9povKwTgapaG%2BgpeRXXfuOqL%2F2tgYnQCbdQEfh%2Fh2Om%2Fl%2B3oLjtL4SqnaTKQpe%2Bw5IGnFvFePdxzN7bYww3LhKEXX%2Bwwsrr%2F0gY6pgFIViOAc2kZ9UGQQ991Tcf%2Br3bniaawzX069teeCLJvPJhZzJ920GDvFEUpJD%2FUdP6JiMXL4ZwfCLoJjP8N6fTTrLYs3hKBxyUghcPYKhoYH0bG3u3AlA9SJEkiuIfmmFsrbVtC%2FLO67wGYFf5R%2Fk8JE7WUXF3x1TjzDS1ZI%2BTtfEyjLiVY3VXXcGqis8RS1cTl5aLjQa9fHDmRhLQdRziBzOkAvCBn&X-Amz-Signature=b9da4328da3d63a5f48df4c50d69b8f8f15ea293c326360223a1c885f18c9f4b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e00ccbd5-f676-4208-b71c-9251298aa288/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2OSU26G%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225654Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGRl6oucOequ6LkMdDNpEkUNsDRS883rio2A48Mec8etAiAYwTmSNzWJJjXU0M%2Fmfyf6ehZ8OUYE2pZDdfRR5cUUfCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMrr4cyNhkDAYqClYKtwDx%2BD153H1JnS5wf6LjVGcVMezM1TyFFSEZhuPaJxmBpE%2FSBXD0x6eRvhVPNHq%2B9hVs2H9uUJG8KEsSVF%2FAfUBVpd4zk%2FZDxXSnSI1xN1Vul831G3Fr0IDzhL9V%2B3IyovqNnIbHAe7Dbm4257hJT4I0iJLOdz0HcdpPUgh3h06mDQgzMYIX%2BTDVAjvX0%2Bbng3HJzeivDX7Qb1cDNGTzU9qNjnPRv93DHlGC3h3M8oiNyJOmz%2FKmpApOAtnq0vJUObXnqCmY1YWSlsHwoJV3qvjDSHmKqWDcjHolbF6yJxYkn%2Bl4WFq5WIMViXHIldwVJSJrwFXb2cloR1CcbbgzkywUJWeXPYrB4aM0fp1TXv%2BHgmyBJvZNQJHnzkZgqkuorO%2BR6Hu3JePq%2FERFzYja7FfDbg5zbFtcnKHl2rhfz1mTmSnLWTM7AHV2o4XQxDzZhFwKEmaxeWK7DFDu%2FeuPFVd8x3esHXvQcQEYoHLKzVlS8kK2zEpod8wlaolC8kSRsP0Szuxyh%2FjQGkFPUoBtS7svpPl7QlzuyFa9povKwTgapaG%2BgpeRXXfuOqL%2F2tgYnQCbdQEfh%2Fh2Om%2Fl%2B3oLjtL4SqnaTKQpe%2Bw5IGnFvFePdxzN7bYww3LhKEXX%2Bwwsrr%2F0gY6pgFIViOAc2kZ9UGQQ991Tcf%2Br3bniaawzX069teeCLJvPJhZzJ920GDvFEUpJD%2FUdP6JiMXL4ZwfCLoJjP8N6fTTrLYs3hKBxyUghcPYKhoYH0bG3u3AlA9SJEkiuIfmmFsrbVtC%2FLO67wGYFf5R%2Fk8JE7WUXF3x1TjzDS1ZI%2BTtfEyjLiVY3VXXcGqis8RS1cTl5aLjQa9fHDmRhLQdRziBzOkAvCBn&X-Amz-Signature=a8cef72c457e52f216ebc6ea5edd9568af525a82513f892e8ce5dc230c72f9d3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/6d9213c1-f7fe-4035-a8e8-bb7e7fcf4634/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2OSU26G%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225654Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGRl6oucOequ6LkMdDNpEkUNsDRS883rio2A48Mec8etAiAYwTmSNzWJJjXU0M%2Fmfyf6ehZ8OUYE2pZDdfRR5cUUfCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMrr4cyNhkDAYqClYKtwDx%2BD153H1JnS5wf6LjVGcVMezM1TyFFSEZhuPaJxmBpE%2FSBXD0x6eRvhVPNHq%2B9hVs2H9uUJG8KEsSVF%2FAfUBVpd4zk%2FZDxXSnSI1xN1Vul831G3Fr0IDzhL9V%2B3IyovqNnIbHAe7Dbm4257hJT4I0iJLOdz0HcdpPUgh3h06mDQgzMYIX%2BTDVAjvX0%2Bbng3HJzeivDX7Qb1cDNGTzU9qNjnPRv93DHlGC3h3M8oiNyJOmz%2FKmpApOAtnq0vJUObXnqCmY1YWSlsHwoJV3qvjDSHmKqWDcjHolbF6yJxYkn%2Bl4WFq5WIMViXHIldwVJSJrwFXb2cloR1CcbbgzkywUJWeXPYrB4aM0fp1TXv%2BHgmyBJvZNQJHnzkZgqkuorO%2BR6Hu3JePq%2FERFzYja7FfDbg5zbFtcnKHl2rhfz1mTmSnLWTM7AHV2o4XQxDzZhFwKEmaxeWK7DFDu%2FeuPFVd8x3esHXvQcQEYoHLKzVlS8kK2zEpod8wlaolC8kSRsP0Szuxyh%2FjQGkFPUoBtS7svpPl7QlzuyFa9povKwTgapaG%2BgpeRXXfuOqL%2F2tgYnQCbdQEfh%2Fh2Om%2Fl%2B3oLjtL4SqnaTKQpe%2Bw5IGnFvFePdxzN7bYww3LhKEXX%2Bwwsrr%2F0gY6pgFIViOAc2kZ9UGQQ991Tcf%2Br3bniaawzX069teeCLJvPJhZzJ920GDvFEUpJD%2FUdP6JiMXL4ZwfCLoJjP8N6fTTrLYs3hKBxyUghcPYKhoYH0bG3u3AlA9SJEkiuIfmmFsrbVtC%2FLO67wGYFf5R%2Fk8JE7WUXF3x1TjzDS1ZI%2BTtfEyjLiVY3VXXcGqis8RS1cTl5aLjQa9fHDmRhLQdRziBzOkAvCBn&X-Amz-Signature=dd93321d79d1c1352081afb1d6e7c17573744dd9010e1a9124e816ca7c6b4c25&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

hello 慕课网的各位同学们，大家好，我是姚半仙。那这一节当中，我们开始做电商项目的 hystrix 改造。首先上半场部分我们来进行 hystrix 的基础设施搭建。咱说过 hystrix 有一个左膀右臂，左青龙右白虎，分别是 turban 还有 hystrix dashboard 那首先我们在咱的商城应用的 platform 这个文件夹下面，把这两个模块先给它构造出来。那接下来就是到各个的微服务模块当中去添加 hystrix 的项目依赖以及打开 accurator 大家还记得 accurator 这里做什么用，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/c1b54075-c261-41e0-8a27-aabd38547f6f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2OSU26G%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225654Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGRl6oucOequ6LkMdDNpEkUNsDRS883rio2A48Mec8etAiAYwTmSNzWJJjXU0M%2Fmfyf6ehZ8OUYE2pZDdfRR5cUUfCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMrr4cyNhkDAYqClYKtwDx%2BD153H1JnS5wf6LjVGcVMezM1TyFFSEZhuPaJxmBpE%2FSBXD0x6eRvhVPNHq%2B9hVs2H9uUJG8KEsSVF%2FAfUBVpd4zk%2FZDxXSnSI1xN1Vul831G3Fr0IDzhL9V%2B3IyovqNnIbHAe7Dbm4257hJT4I0iJLOdz0HcdpPUgh3h06mDQgzMYIX%2BTDVAjvX0%2Bbng3HJzeivDX7Qb1cDNGTzU9qNjnPRv93DHlGC3h3M8oiNyJOmz%2FKmpApOAtnq0vJUObXnqCmY1YWSlsHwoJV3qvjDSHmKqWDcjHolbF6yJxYkn%2Bl4WFq5WIMViXHIldwVJSJrwFXb2cloR1CcbbgzkywUJWeXPYrB4aM0fp1TXv%2BHgmyBJvZNQJHnzkZgqkuorO%2BR6Hu3JePq%2FERFzYja7FfDbg5zbFtcnKHl2rhfz1mTmSnLWTM7AHV2o4XQxDzZhFwKEmaxeWK7DFDu%2FeuPFVd8x3esHXvQcQEYoHLKzVlS8kK2zEpod8wlaolC8kSRsP0Szuxyh%2FjQGkFPUoBtS7svpPl7QlzuyFa9povKwTgapaG%2BgpeRXXfuOqL%2F2tgYnQCbdQEfh%2Fh2Om%2Fl%2B3oLjtL4SqnaTKQpe%2Bw5IGnFvFePdxzN7bYww3LhKEXX%2Bwwsrr%2F0gY6pgFIViOAc2kZ9UGQQ991Tcf%2Br3bniaawzX069teeCLJvPJhZzJ920GDvFEUpJD%2FUdP6JiMXL4ZwfCLoJjP8N6fTTrLYs3hKBxyUghcPYKhoYH0bG3u3AlA9SJEkiuIfmmFsrbVtC%2FLO67wGYFf5R%2Fk8JE7WUXF3x1TjzDS1ZI%2BTtfEyjLiVY3VXXcGqis8RS1cTl5aLjQa9fHDmRhLQdRziBzOkAvCBn&X-Amz-Signature=8276001023e16b0095750c90bd5664ece4aff1ec9bf4c1d924d7cf040e73453b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

它是让我们的 turban 可以去访问你在 activator 当中开放的端点来收集 API 调用的信息。 OK 那准备好的话我们到 entire jelly 开工好。
来到影泰立 G 之后，咱打开这个 platform 文件夹。在这个下面我们要创建一个新的 module 那这个 module 咱给它起名字叫什么呢？咱先来创建一个 hystrix turbine 所以这个名字就叫 hystrix 杠 turbine 点击 next 然后这里的文件夹把它塞到 platform 下面一个斜杠。


好走，你三二一出来。那接下来这里面需要放的依赖项，和之前咱在教学项目当中创建的 turben sample 是一模一样的。好，我们这里直接把它 copy 过来，顺带再稍微过一下。那这第一个是 eurika 的 client 这个大家都非常熟悉了，因为待会咱需要在 turbine 的配置项当中配置上需要监听的服务名称。那这里就是通过注册中心来获取这些指定名称都有哪些机器？接下来下面这两个老生常谈了，我们就不看了。


往后就是咱应用中间件的主角部分，它就是特本。 OK 那配置完这些项目之后，我这里还要配置一个启动类，所以我们把之前项目里的启动的这个 build 节点给它 copy 过来，我们随便找一个应用比如这里 user 下面的 foodie user web 好，我们把这个应用拉到下面 build 节点给它拿过来，然后 copy 到这里。但是不要忘了这个名称需要改一下哪个名称咱的 main class 这 main class 咱给它起名就叫做 high strikes turban application 好长的名字。好嘞，咱这里依赖项已经添加完毕了，然后我们去把这个门 class 给它创建出来。好，这里点击到 SRC 里面，每当创建一个类的时候，我们先要把咱的冠名商 M OK 给它打上，然后直接在这个文件夹里面新建一个点 class 走你。那咱接下来顺带的去再回顾一下这上面的注解。第一个我们先要把带头大哥谁 eurika 给他添加进来，enable discovery client 那前面说到咱要依赖 eurika 的服务发现去找到咱需要监听的那些节点的物理历史。


那接下来咱要配置一个核心的注解是 enable turban 好，把它配置上之后，我们再来去把自动装配也给它打开。 enable auto configurationok 好，然后咱这个启动类，去随便找一个应用，把它拿过来改一下名字就可以了。我们这里找到了注册中心 registry center 拿到它的闷方法里给它 copy 过来抄一把作业。好，这里放过来。放过来之后，咱们把这个 high strikes turban application 替换过来。 OK 大功告成。
那最后一步非常简单，咱去 resources 下面创建一个配置项之前咱都是用的 properties 文件来做的配置。那咱这里怎么样呢？换一个口味，咱使用 YAML 的方式给它起名 application YAML okay 好，这个 YAML 文件里面都有哪些内容呢？第一个当然是谁是注册中心，咱把注册中心的 URL 给它 copy 过来。好，这里放过来，那注册中心我们依然连接到 2 万端口的尤瑞卡下面。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/5a026006-9e06-4073-aba1-392283993044/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2OSU26G%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225654Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGRl6oucOequ6LkMdDNpEkUNsDRS883rio2A48Mec8etAiAYwTmSNzWJJjXU0M%2Fmfyf6ehZ8OUYE2pZDdfRR5cUUfCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMrr4cyNhkDAYqClYKtwDx%2BD153H1JnS5wf6LjVGcVMezM1TyFFSEZhuPaJxmBpE%2FSBXD0x6eRvhVPNHq%2B9hVs2H9uUJG8KEsSVF%2FAfUBVpd4zk%2FZDxXSnSI1xN1Vul831G3Fr0IDzhL9V%2B3IyovqNnIbHAe7Dbm4257hJT4I0iJLOdz0HcdpPUgh3h06mDQgzMYIX%2BTDVAjvX0%2Bbng3HJzeivDX7Qb1cDNGTzU9qNjnPRv93DHlGC3h3M8oiNyJOmz%2FKmpApOAtnq0vJUObXnqCmY1YWSlsHwoJV3qvjDSHmKqWDcjHolbF6yJxYkn%2Bl4WFq5WIMViXHIldwVJSJrwFXb2cloR1CcbbgzkywUJWeXPYrB4aM0fp1TXv%2BHgmyBJvZNQJHnzkZgqkuorO%2BR6Hu3JePq%2FERFzYja7FfDbg5zbFtcnKHl2rhfz1mTmSnLWTM7AHV2o4XQxDzZhFwKEmaxeWK7DFDu%2FeuPFVd8x3esHXvQcQEYoHLKzVlS8kK2zEpod8wlaolC8kSRsP0Szuxyh%2FjQGkFPUoBtS7svpPl7QlzuyFa9povKwTgapaG%2BgpeRXXfuOqL%2F2tgYnQCbdQEfh%2Fh2Om%2Fl%2B3oLjtL4SqnaTKQpe%2Bw5IGnFvFePdxzN7bYww3LhKEXX%2Bwwsrr%2F0gY6pgFIViOAc2kZ9UGQQ991Tcf%2Br3bniaawzX069teeCLJvPJhZzJ920GDvFEUpJD%2FUdP6JiMXL4ZwfCLoJjP8N6fTTrLYs3hKBxyUghcPYKhoYH0bG3u3AlA9SJEkiuIfmmFsrbVtC%2FLO67wGYFf5R%2Fk8JE7WUXF3x1TjzDS1ZI%2BTtfEyjLiVY3VXXcGqis8RS1cTl5aLjQa9fHDmRhLQdRziBzOkAvCBn&X-Amz-Signature=9c09d8e784b3e633b801dbf336fddb23ccbc123b1f86fb2afa647f4d96fcc37b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

好，第二个配置咱和之前在 spring cloud demo 当中学习的配置下是一样的。那这里只是带大家回顾一下，就不进入到每一个配置，跟大家再仔细讲解了。咱首先这个端口要给它定义。好，前面的尤瑞卡已经定义了二万端口，咱给他起叫20,001。好了，因为它是咱这个 platform 文件夹下的第二个类。带头二哥的 management 端口，不要把它搞冲突了，给它起一个还是把它放到五万，五万两千零一。


OK 那剩下的咱接下来就是给它定义一个 application 的名称 string application 给它起名叫做 high streaks 杠 turbine OK 那最后就是 high strikes turbine 它自己的配置了 turbine 那这里一个 aggregator 那在 aggregator 下面的 cluster config 谁 default 因为咱现在目前为止只起了一个 default 的cluster 。


那如果我们的 spring cloud 微服务当中，在我们服务提供者做服务注册的时候，在尤瑞卡注册信息当中配置了一些元数据 meta data 来指定了它的集群。那我们这里就可以根据服务提供者的元数据配置来制定相应的聚合逻辑。那咱这里就直接指定成了default ，因为我们只有一个单节点的服务集群。


好那接下来我们给它指定 App config 那咱在这个应用当中有很多的微服务，比如说 food user service 那除了这个，还有一系列的 foodie item service 以及 food order service 那大家根据自己的服务拆分情况，在这里配置上你需要去监听的服务。


好，这里把这些配置先给注释掉，我只留一个谁我只留一个 foodie order service ，因为它属于比较下游的服务，它需要调用更多的上游服务，所以 foodie order service 中的方法调用信息比较丰富，咱这里就把它给留在这里了。


OK 那接下来咱配置 cluster name expression OK 那这里依然是配置一个 default default 好，那我这里给大家加个注释，方便去回顾。这个表示集群名称叫 defaultok 那接下来我们是不是需要去 combine 的 host 和 port 我这里给它设置成 true 那这个业务含义之前跟大家已经有讲过，它代表着叫什么呢？根据 host 加上 pot 的形式怎么样呢？用这种组合形式来进行区分。


那最后一个我们给它指定 instance URL suffix 好这个含义是什么呢？那这个我们依然把它指向到 activator 的下面的 high streaks stream 当中。这个业务含义大家应该也比较了解了，它是从哪个 actiurator 的端点上面去拉取你的方法调用信息。 OK 那到这里，一个最简单的 turbine 配置就已经完成了。


不过如果大家面对的是一个集群环境，那么它这里实际上是有一些额外的配置变化的。比如说我拿这个 cluster name expression 做例子，同学们知道这个配置项其实它的 value 它不止可以指定成 default 如果你有多个集群，并且同一个服务会部署到不同集群上。那这些服务在你做服务注册的时候，会以一种特殊的形式来告诉尤瑞卡注册中心说我叫什么名字，我是属于哪一个集群 cluster 的。
比方说它可以这样配它叫 eureka 咱知道 eureka 下面都有一个 instance 的节点对不对咱给它下面配了一个 instance 然后在 instance 下面还有一个叫 matter data 杠 map 那后面我们就可以做一些自定义的配置了，比如说我们这边配置一个 my cluster name

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/8a7a2ae9-dbef-4334-8391-d5b79a676bae/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2OSU26G%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225654Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGRl6oucOequ6LkMdDNpEkUNsDRS883rio2A48Mec8etAiAYwTmSNzWJJjXU0M%2Fmfyf6ehZ8OUYE2pZDdfRR5cUUfCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMrr4cyNhkDAYqClYKtwDx%2BD153H1JnS5wf6LjVGcVMezM1TyFFSEZhuPaJxmBpE%2FSBXD0x6eRvhVPNHq%2B9hVs2H9uUJG8KEsSVF%2FAfUBVpd4zk%2FZDxXSnSI1xN1Vul831G3Fr0IDzhL9V%2B3IyovqNnIbHAe7Dbm4257hJT4I0iJLOdz0HcdpPUgh3h06mDQgzMYIX%2BTDVAjvX0%2Bbng3HJzeivDX7Qb1cDNGTzU9qNjnPRv93DHlGC3h3M8oiNyJOmz%2FKmpApOAtnq0vJUObXnqCmY1YWSlsHwoJV3qvjDSHmKqWDcjHolbF6yJxYkn%2Bl4WFq5WIMViXHIldwVJSJrwFXb2cloR1CcbbgzkywUJWeXPYrB4aM0fp1TXv%2BHgmyBJvZNQJHnzkZgqkuorO%2BR6Hu3JePq%2FERFzYja7FfDbg5zbFtcnKHl2rhfz1mTmSnLWTM7AHV2o4XQxDzZhFwKEmaxeWK7DFDu%2FeuPFVd8x3esHXvQcQEYoHLKzVlS8kK2zEpod8wlaolC8kSRsP0Szuxyh%2FjQGkFPUoBtS7svpPl7QlzuyFa9povKwTgapaG%2BgpeRXXfuOqL%2F2tgYnQCbdQEfh%2Fh2Om%2Fl%2B3oLjtL4SqnaTKQpe%2Bw5IGnFvFePdxzN7bYww3LhKEXX%2Bwwsrr%2F0gY6pgFIViOAc2kZ9UGQQ991Tcf%2Br3bniaawzX069teeCLJvPJhZzJ920GDvFEUpJD%2FUdP6JiMXL4ZwfCLoJjP8N6fTTrLYs3hKBxyUghcPYKhoYH0bG3u3AlA9SJEkiuIfmmFsrbVtC%2FLO67wGYFf5R%2Fk8JE7WUXF3x1TjzDS1ZI%2BTtfEyjLiVY3VXXcGqis8RS1cTl5aLjQa9fHDmRhLQdRziBzOkAvCBn&X-Amz-Signature=ff395ae643d87c5422ee939d3cf1ab25ba65c6bc74a6c850b8820e1dc25a9ead&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

 那好它可以给它指定成谁指定成 imockok 那这是什么含义呢？这是你在服务注册时候自己去定义的一个元数据。那这个 meta data map 是一个可扩展的结构。那咱的服务提供者如果做了这样的配置，并且我们想把它通过 class name expression 给它读取出来。那怎么办呢？我们用什么格式读取非常简单。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/3ffe5c04-1256-4bda-9a6c-cc50e14d743f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R2OSU26G%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225654Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIGRl6oucOequ6LkMdDNpEkUNsDRS883rio2A48Mec8etAiAYwTmSNzWJJjXU0M%2Fmfyf6ehZ8OUYE2pZDdfRR5cUUfCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMMrr4cyNhkDAYqClYKtwDx%2BD153H1JnS5wf6LjVGcVMezM1TyFFSEZhuPaJxmBpE%2FSBXD0x6eRvhVPNHq%2B9hVs2H9uUJG8KEsSVF%2FAfUBVpd4zk%2FZDxXSnSI1xN1Vul831G3Fr0IDzhL9V%2B3IyovqNnIbHAe7Dbm4257hJT4I0iJLOdz0HcdpPUgh3h06mDQgzMYIX%2BTDVAjvX0%2Bbng3HJzeivDX7Qb1cDNGTzU9qNjnPRv93DHlGC3h3M8oiNyJOmz%2FKmpApOAtnq0vJUObXnqCmY1YWSlsHwoJV3qvjDSHmKqWDcjHolbF6yJxYkn%2Bl4WFq5WIMViXHIldwVJSJrwFXb2cloR1CcbbgzkywUJWeXPYrB4aM0fp1TXv%2BHgmyBJvZNQJHnzkZgqkuorO%2BR6Hu3JePq%2FERFzYja7FfDbg5zbFtcnKHl2rhfz1mTmSnLWTM7AHV2o4XQxDzZhFwKEmaxeWK7DFDu%2FeuPFVd8x3esHXvQcQEYoHLKzVlS8kK2zEpod8wlaolC8kSRsP0Szuxyh%2FjQGkFPUoBtS7svpPl7QlzuyFa9povKwTgapaG%2BgpeRXXfuOqL%2F2tgYnQCbdQEfh%2Fh2Om%2Fl%2B3oLjtL4SqnaTKQpe%2Bw5IGnFvFePdxzN7bYww3LhKEXX%2Bwwsrr%2F0gY6pgFIViOAc2kZ9UGQQ991Tcf%2Br3bniaawzX069teeCLJvPJhZzJ920GDvFEUpJD%2FUdP6JiMXL4ZwfCLoJjP8N6fTTrLYs3hKBxyUghcPYKhoYH0bG3u3AlA9SJEkiuIfmmFsrbVtC%2FLO67wGYFf5R%2Fk8JE7WUXF3x1TjzDS1ZI%2BTtfEyjLiVY3VXXcGqis8RS1cTl5aLjQa9fHDmRhLQdRziBzOkAvCBn&X-Amz-Signature=14a953cc52911b947c6ae5c2f6a638ce7bf1e20aca932bf15efbbe2c5091bc49&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```java
####################################################################################
#
#  注册中心
#
################################################################################
eureka:
  client:
    service-url:
      defaultZone: http://localhost:20000/eureka

spring:
  application:
    name: Hystrix-Turbine


server:
  port: 20001
management:
  server:
    port: 50001


turbine:
  aggreator:
    # cluster1, cluster2
    clusterConfig: default
#  app-config: foodie-order-service, foodie-item-service, foodie-user-service
  app-config: foodie-order-service
  # 集群名称叫 default
  # eureka: instance: metadata-map：abcd -> imooc
  # metadata:['abcd']
  cluster-name-expression: "default"
  # 根据host + port 的形式组合来进行区分
  combine-host-port: true
  # 从哪个actuator的端点上拉取方法调用信息
  instanceUrlSuffix:
    default: actuator/hystrix.stream
```


matedata 然后后面跟一个画括号。那这里就可以跟你的属性的名称，比方说我这里起的名称叫 abcd 那你这里也可以给它起名叫 abcdok 这就是一个可扩展的结构。那如果同学们这样配置了，那同样的，咱在上面的 aggregator 这里也可以去体现一个集群的聚合作用。比如说我这里想要配置多个集群怎么办呢？咱这里配置的可是 default 默认的如果你这里有多个集群，比如小 A 小 B 小 C 小 D 那这些集群你想要把它其中 command K 这些相同特征的服务 high streaks 调用信息全给它聚合起来。那我这里就可以把每一个集群通过逗号来进行连接，比方说我这个集群是 cluster 1 那后面我可以跟 cluster two 你这里可以通过逗号聚集多个集群的服务调用信息，并且把它做一个 aggregation 也就是聚合


OK 那到这里咱的特本就算已经创建完成了。 OK 那接下来我们去创建下一个应用是谁呢？ high strikes ，dashboard它的监控大盘。那监控大盘也属于在 high strikes 的基础组件部分。 OK 那同学们去做一个小的中场休息，我们下一节再跟大家一起去搭建 high streaks portal 然后在各个微服务当中添加必要的依赖和配置。同学们，咱下一节再见喽。



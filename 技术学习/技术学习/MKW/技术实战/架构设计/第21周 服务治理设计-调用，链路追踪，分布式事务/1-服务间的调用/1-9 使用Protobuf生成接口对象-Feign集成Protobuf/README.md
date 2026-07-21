---
title: 1-9 使用Protobuf生成接口对象-Feign集成Protobuf
---

# 1-9 使用Protobuf生成接口对象-Feign集成Protobuf

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/59932ee5-5144-4d58-8d34-9c207e067a84/SCR-20240802-cobh.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y6K6ZGFU%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCJ6d5Kg%2Fuvb3JJolTCWqy2HkCIc1V4sxVDK7zdUyaQEgIgQ2KPgTcQb4e8X%2F1dEqHTE0hBJZT7k6eG4mxDhY88lgcqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFiVI8eX4okCqBOfrircA9ClXjU6Wp5kwg6W0wvBhn7RSUGYkevRO4gGaUx0%2BaYpHXTBTE0%2B14xkBbgNrbuhYFyfzU1OE0uhuyALZl7lQ41E%2B4fmWMCnVpaGsJ%2BeTSzu7E7kOnveUu7FmM3LZ0Xttk5ysdC9oFKrStvZKf86ZbRLtW5LHlqSJCIRAsvN9Q5nQi38IL4bLqGUyXaRT8Oecc9i%2FZEvaHhmCz4V%2BOLUZ0sMnBC6aK%2FbcwkprepoqwD7rjuRbqzVy2YTWWmy2HQFlA5NPSF%2FWW3egmVdSs2ixg8F2LgyVi6c%2B0gn83drT5CaF8vMpynFbZPA7VHqbfTzElcyehAnVpx7etFAHWCw0MmdtR0eMe7yC9WNMuYG5o3jWGqmcG9potHVuZxUrDiF1csr1wuBnbZyy6xCVDTrB%2BDURJR%2B65MJORX8%2B502CTlWCLE7CW7TvlAoPKJm3T7Ey5ZK%2FdqXoK01ofeZdMI%2BFReSk1mdPhlFCxmJCOVY2f5oe%2F3p6m805Wqno55Beav4hJY4Lpm0ClHbBnWNvUiZVNCXDJ7RYxbki5RQx6AAYhHH0FakETbVkHKcO0mFZXwADZG%2BzQD54vlVVIMPSqyCDmy7THdF0vwX5w5Y%2B7vAwDVd9O385tiygUyHAiyTMJy5%2F9IGOqUBEVryZ1Q8vgLMFS9yg1bDpbY1Iq1Iq%2FbNwIC2ZbHOiNeHPpzfMKogDMzNpaC5Ew7DOXGAGIcAEKMfecdqca0igSRmJ6hXSLehmNghab6gnh0ie3qMGLEG%2FAoI%2FTBKuzloaYNrtkpTXMYPoC8KekXQei0UwwFpGb%2FAOsiGRfx6A2kyN%2F3S1ATW5qkekL6DE%2BvLG6Mu8qf5du8cAH6zzzeBQtpWmU87&X-Amz-Signature=c3a61b1e7037c5f1a7141a157efa520368729c6b5bb925b2a165d2711cf1d6c9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/3e2b9845-d54f-4000-936c-45fffa59dbd3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y6K6ZGFU%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCJ6d5Kg%2Fuvb3JJolTCWqy2HkCIc1V4sxVDK7zdUyaQEgIgQ2KPgTcQb4e8X%2F1dEqHTE0hBJZT7k6eG4mxDhY88lgcqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFiVI8eX4okCqBOfrircA9ClXjU6Wp5kwg6W0wvBhn7RSUGYkevRO4gGaUx0%2BaYpHXTBTE0%2B14xkBbgNrbuhYFyfzU1OE0uhuyALZl7lQ41E%2B4fmWMCnVpaGsJ%2BeTSzu7E7kOnveUu7FmM3LZ0Xttk5ysdC9oFKrStvZKf86ZbRLtW5LHlqSJCIRAsvN9Q5nQi38IL4bLqGUyXaRT8Oecc9i%2FZEvaHhmCz4V%2BOLUZ0sMnBC6aK%2FbcwkprepoqwD7rjuRbqzVy2YTWWmy2HQFlA5NPSF%2FWW3egmVdSs2ixg8F2LgyVi6c%2B0gn83drT5CaF8vMpynFbZPA7VHqbfTzElcyehAnVpx7etFAHWCw0MmdtR0eMe7yC9WNMuYG5o3jWGqmcG9potHVuZxUrDiF1csr1wuBnbZyy6xCVDTrB%2BDURJR%2B65MJORX8%2B502CTlWCLE7CW7TvlAoPKJm3T7Ey5ZK%2FdqXoK01ofeZdMI%2BFReSk1mdPhlFCxmJCOVY2f5oe%2F3p6m805Wqno55Beav4hJY4Lpm0ClHbBnWNvUiZVNCXDJ7RYxbki5RQx6AAYhHH0FakETbVkHKcO0mFZXwADZG%2BzQD54vlVVIMPSqyCDmy7THdF0vwX5w5Y%2B7vAwDVd9O385tiygUyHAiyTMJy5%2F9IGOqUBEVryZ1Q8vgLMFS9yg1bDpbY1Iq1Iq%2FbNwIC2ZbHOiNeHPpzfMKogDMzNpaC5Ew7DOXGAGIcAEKMfecdqca0igSRmJ6hXSLehmNghab6gnh0ie3qMGLEG%2FAoI%2FTBKuzloaYNrtkpTXMYPoC8KekXQei0UwwFpGb%2FAOsiGRfx6A2kyN%2F3S1ATW5qkekL6DE%2BvLG6Mu8qf5du8cAH6zzzeBQtpWmU87&X-Amz-Signature=0cd7942e467ba2181c3e6fa257859f31c35c41062b211972088f011b20c60731&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

hello，幕后网的各位同学们大家好，我们这里进入咱 protobuf 这一节的下半场。那我们跟同学们去来演示一下如何使用 Protobuf 这种黑科技来去定义份组件当中的入参出散。


那同学们这里跟我 Intelligent 里面走起，每天 coding 一小时，健康工作 50 年，我们这里第一次去定义这个 PORTAL buff，选择哪个项目？ restroom service，咱要选择这两个应用当中的这个上游的应用，我们这里打开 restroom API，我想要接下来在这个 API 层去来定义这个purlubuff，然后自动使用某些插件把咱的这个 purlubuff 文件给它生成出来。这个第一步就是我要把必要的依赖项给它引入。同学们看，我这里要依赖两个依赖项，我把这个 dependency 给它打入进来，我接下来这里引入两个谷歌相关的依赖项。第一个dependency，我把它给它的 group ID，我设置成com，点Google，点Purdubuff，然后我引入的是 Purdubuff 加 okay 它对应的版本。


同学们，这里一定要跟本地的 photobuf 版本相对应，比如说我在这个自己的命令行当中，我输入 part to see version，我打开看，你看它的 library 是 3. 13. 0 这个版本，那我对应的这里我也要设置成同样的 3. 13. 0。那接下来我再添加另外一个dependency，它是做一个类型转换的，这样的一个组件是com，点 Google code，点protobuf，然后我选择 Java for matter 对应的version，我把它规定到 1. 2。那这两个依赖参数我们把它定义好了之后，接下来我这边去尝试创建一个 protobuf 的文件，咱这个文件的安生立命之所在哪里？那我这里在这个 Java 目录和 resources 目录下面，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/213dbc84-668a-425b-874e-d6ca34a1708a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y6K6ZGFU%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCJ6d5Kg%2Fuvb3JJolTCWqy2HkCIc1V4sxVDK7zdUyaQEgIgQ2KPgTcQb4e8X%2F1dEqHTE0hBJZT7k6eG4mxDhY88lgcqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFiVI8eX4okCqBOfrircA9ClXjU6Wp5kwg6W0wvBhn7RSUGYkevRO4gGaUx0%2BaYpHXTBTE0%2B14xkBbgNrbuhYFyfzU1OE0uhuyALZl7lQ41E%2B4fmWMCnVpaGsJ%2BeTSzu7E7kOnveUu7FmM3LZ0Xttk5ysdC9oFKrStvZKf86ZbRLtW5LHlqSJCIRAsvN9Q5nQi38IL4bLqGUyXaRT8Oecc9i%2FZEvaHhmCz4V%2BOLUZ0sMnBC6aK%2FbcwkprepoqwD7rjuRbqzVy2YTWWmy2HQFlA5NPSF%2FWW3egmVdSs2ixg8F2LgyVi6c%2B0gn83drT5CaF8vMpynFbZPA7VHqbfTzElcyehAnVpx7etFAHWCw0MmdtR0eMe7yC9WNMuYG5o3jWGqmcG9potHVuZxUrDiF1csr1wuBnbZyy6xCVDTrB%2BDURJR%2B65MJORX8%2B502CTlWCLE7CW7TvlAoPKJm3T7Ey5ZK%2FdqXoK01ofeZdMI%2BFReSk1mdPhlFCxmJCOVY2f5oe%2F3p6m805Wqno55Beav4hJY4Lpm0ClHbBnWNvUiZVNCXDJ7RYxbki5RQx6AAYhHH0FakETbVkHKcO0mFZXwADZG%2BzQD54vlVVIMPSqyCDmy7THdF0vwX5w5Y%2B7vAwDVd9O385tiygUyHAiyTMJy5%2F9IGOqUBEVryZ1Q8vgLMFS9yg1bDpbY1Iq1Iq%2FbNwIC2ZbHOiNeHPpzfMKogDMzNpaC5Ew7DOXGAGIcAEKMfecdqca0igSRmJ6hXSLehmNghab6gnh0ie3qMGLEG%2FAoI%2FTBKuzloaYNrtkpTXMYPoC8KekXQei0UwwFpGb%2FAOsiGRfx6A2kyN%2F3S1ATW5qkekL6DE%2BvLG6Mu8qf5du8cAH6zzzeBQtpWmU87&X-Amz-Signature=f0bc9c163c07ef00c5c2e053b11dc3c8ac23c5a2bacaa37ff60e31a9d3286f26&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

我给它另起炉灶，我创建一个新的文件夹，这个文件夹我就给它起名叫 Purdue P R O t o p t buff 的 p to。


接下来我这里创建一个具体的file，这个 file 的名称同学们可以随便起，比方说叫 rest room，点它的后缀一定要相同叫，那这个文件我创建好之后，接下来我要在这里面去声明两个类，这个声明类之前我要去定义你的 Purdo 协议。比方说我在协议的最上面打下我当前使用的是谁，是 part two 3 协议， Claude two three 哪一个分号？然后接下来我给它添加几个 option 参数，比如说 Java multiple FILES，我把它给打开，等于true。


第二个option，我给它定义一个包路径， java 杠 package 包路径，这里我们遵循同样的秘密规范好了，我就把它去给丢到 com 点emock，点restroom，然后再一个点 porch okay their beans。接下来我们生成的这个 Java 类就会自动跑到我这边定义的这个目录下面。那这里 Java 的 package 定义好了之后，我还要去管下自己的命名空间package，我给它起名叫 comm 点 i mock the restroom，我直接应该复制的，后知后觉算了，把这两行复制下来，那这里定义好，接下来我就可以去定义具体的类了。那因为咱不是一个 GRPC 方法，所以咱在前面一节当中看到的这个 GRP seed 定义，我们先去不管它，我们这里只去定义一些实体类。 message 定义一个实体类叫 approach request，那它的这个参数我可以给它定义一个 long 型 INT 6 十四 long 型，把它叫做ID。


好了，后面是一个具体的参数的位置，如果同学们这里定义了其他参数，那比如 i d two，那对应的后面的数字要依次往下递增，那我们在线上实践当中还有一个经验，也算是教训，就是说我一个已经上线的接口，如果我要去修改这里面的字段名尽量的不要去在它原地上修改。而是说我把其中的一个字段标记成deprecated，标记成已经过期。与此同时我去定义一个新的字段。为什么这样做？这是跟 protobuf 它的序列化反序列化有关。以一个上限的接口，那如果别人在这个数字 2 的位置使用一个A，b， c 来接收你的参数，那你这里把这个名称改成了i，d，two。这就有可能去引发线上别人的 client 无法来去消费你新的改变过后的这个结构体，那这个就是 PORTAL buff 的一个小限制。哎，同学们心里有个数就可以了。


如果对于已上线的接口去修改一个已经存在的属性，尽可能的我们直接定义新的，把原先的标记成deprecated，那我这个 request 定义好了之后，我接下来再定义一个response，那咱的响应和请求算是定义好了，那接下来我如何来把它生成 Java 类？这一步就要靠我们的一个插件来帮忙了，这个插件非常的长，老师这里就不跟同学们一行一行打了，我直接把它复制过来，变个魔术，屏住呼吸321，好嘞，这边出来了我这个配置带同学们看一下它主要是下面的plugin，看它的名称 Prato Maven plugin 这里是做什么事儿？第一个我要去对应的一个文件夹儿里面去读取所有 per to buff 文件的定义，那这个就是咱刚才在这里同学们看啊， Purto 这里创建出来的这个文件夹，这下面躺着咱的 Purto buff 的文件，还有 output directory，是说我接下来打包出了这个文件要放在什么位置，同学们，我建议大家尽可能的选什么呀？选 generate sources 这个目录。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/34b17ff7-58cb-483e-9a4e-bb96e23f244c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y6K6ZGFU%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCJ6d5Kg%2Fuvb3JJolTCWqy2HkCIc1V4sxVDK7zdUyaQEgIgQ2KPgTcQb4e8X%2F1dEqHTE0hBJZT7k6eG4mxDhY88lgcqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFiVI8eX4okCqBOfrircA9ClXjU6Wp5kwg6W0wvBhn7RSUGYkevRO4gGaUx0%2BaYpHXTBTE0%2B14xkBbgNrbuhYFyfzU1OE0uhuyALZl7lQ41E%2B4fmWMCnVpaGsJ%2BeTSzu7E7kOnveUu7FmM3LZ0Xttk5ysdC9oFKrStvZKf86ZbRLtW5LHlqSJCIRAsvN9Q5nQi38IL4bLqGUyXaRT8Oecc9i%2FZEvaHhmCz4V%2BOLUZ0sMnBC6aK%2FbcwkprepoqwD7rjuRbqzVy2YTWWmy2HQFlA5NPSF%2FWW3egmVdSs2ixg8F2LgyVi6c%2B0gn83drT5CaF8vMpynFbZPA7VHqbfTzElcyehAnVpx7etFAHWCw0MmdtR0eMe7yC9WNMuYG5o3jWGqmcG9potHVuZxUrDiF1csr1wuBnbZyy6xCVDTrB%2BDURJR%2B65MJORX8%2B502CTlWCLE7CW7TvlAoPKJm3T7Ey5ZK%2FdqXoK01ofeZdMI%2BFReSk1mdPhlFCxmJCOVY2f5oe%2F3p6m805Wqno55Beav4hJY4Lpm0ClHbBnWNvUiZVNCXDJ7RYxbki5RQx6AAYhHH0FakETbVkHKcO0mFZXwADZG%2BzQD54vlVVIMPSqyCDmy7THdF0vwX5w5Y%2B7vAwDVd9O385tiygUyHAiyTMJy5%2F9IGOqUBEVryZ1Q8vgLMFS9yg1bDpbY1Iq1Iq%2FbNwIC2ZbHOiNeHPpzfMKogDMzNpaC5Ew7DOXGAGIcAEKMfecdqca0igSRmJ6hXSLehmNghab6gnh0ie3qMGLEG%2FAoI%2FTBKuzloaYNrtkpTXMYPoC8KekXQei0UwwFpGb%2FAOsiGRfx6A2kyN%2F3S1ATW5qkekL6DE%2BvLG6Mu8qf5du8cAH6zzzeBQtpWmU87&X-Amz-Signature=efab2c823d976734208e1275fe503dd410155960365f49db4c82aae878029e20&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/1d1deb54-f82e-454b-b4d1-f3df7017c7a1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y6K6ZGFU%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231340Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCJ6d5Kg%2Fuvb3JJolTCWqy2HkCIc1V4sxVDK7zdUyaQEgIgQ2KPgTcQb4e8X%2F1dEqHTE0hBJZT7k6eG4mxDhY88lgcqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFiVI8eX4okCqBOfrircA9ClXjU6Wp5kwg6W0wvBhn7RSUGYkevRO4gGaUx0%2BaYpHXTBTE0%2B14xkBbgNrbuhYFyfzU1OE0uhuyALZl7lQ41E%2B4fmWMCnVpaGsJ%2BeTSzu7E7kOnveUu7FmM3LZ0Xttk5ysdC9oFKrStvZKf86ZbRLtW5LHlqSJCIRAsvN9Q5nQi38IL4bLqGUyXaRT8Oecc9i%2FZEvaHhmCz4V%2BOLUZ0sMnBC6aK%2FbcwkprepoqwD7rjuRbqzVy2YTWWmy2HQFlA5NPSF%2FWW3egmVdSs2ixg8F2LgyVi6c%2B0gn83drT5CaF8vMpynFbZPA7VHqbfTzElcyehAnVpx7etFAHWCw0MmdtR0eMe7yC9WNMuYG5o3jWGqmcG9potHVuZxUrDiF1csr1wuBnbZyy6xCVDTrB%2BDURJR%2B65MJORX8%2B502CTlWCLE7CW7TvlAoPKJm3T7Ey5ZK%2FdqXoK01ofeZdMI%2BFReSk1mdPhlFCxmJCOVY2f5oe%2F3p6m805Wqno55Beav4hJY4Lpm0ClHbBnWNvUiZVNCXDJ7RYxbki5RQx6AAYhHH0FakETbVkHKcO0mFZXwADZG%2BzQD54vlVVIMPSqyCDmy7THdF0vwX5w5Y%2B7vAwDVd9O385tiygUyHAiyTMJy5%2F9IGOqUBEVryZ1Q8vgLMFS9yg1bDpbY1Iq1Iq%2FbNwIC2ZbHOiNeHPpzfMKogDMzNpaC5Ew7DOXGAGIcAEKMfecdqca0igSRmJ6hXSLehmNghab6gnh0ie3qMGLEG%2FAoI%2FTBKuzloaYNrtkpTXMYPoC8KekXQei0UwwFpGb%2FAOsiGRfx6A2kyN%2F3S1ATW5qkekL6DE%2BvLG6Mu8qf5du8cAH6zzzeBQtpWmU87&X-Amz-Signature=129a50cd1dad2a879dbe5f0a271b3f6a2bf6b5d393ba430b405fc181d1125e41&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



当然了，同学们如果想要在我们的 Java 目录下面看到这些类，你也可以用下面的这行配置，直接在我们的 sauce directory 上面取来，输出经过转化过后的 Java 的类。那剩下这个属性我是叫做 clear output directory，就是说你每次做生成的时候，哎，是不是把你这整个文件夹全给清空，那我们这里可以直接放个false，因为你每次去创建文件的时候，如果文件名相同，实际上它也会替换的。主要就是这三个属性，接下来我们不妨走到外面对这个项目做一个完整的 Maven 的编译。在它编译的过程当中，我们可以去观察这个 generated sources，一旦它编译完成，我们点开，现在应该很快编译完成了。同学们看到这里，你这段 build 它 plugin 的操作就是让它在 generate sources 下面，根据你前面定义的这个 PORTAL buff 的文件，咱就生成了一系列的 Java 类，非常的神奇。这里面的 Java 类有一个好处就是它不碍眼。同学们，它不会像我生成在 Java 文件当中，你每次提交Git，可能也要把这个对应的文件提交上去，你这生成在 target 这里，你只管用就好了，不用去做提交。


那我们现在 part buff 这一层已经把它给定义妥当了，那接下来我们去尝试的写一个 photobuf 的方法好了，那咱打开这个API，在这个 API 里面我们创建一个新的方法，这个新的方法咱给它起名叫，叫什么呀？我先把这个定义好叫 per to response，那这是它的返回值，那它的方法名就叫 test per to buff。


那平淡无奇的方法名还要接收一个非凡的参数，这个参数是个浪，那咱接收好之后，接下来就要去对应的实现类 restroom service 这个实现类当中，把这个方法也给它去添加出来，我直接 implement 没有实现的方法。在这里同学们有一点小动作需要同学们来做了。这个方法的组装非常简单，但是它的方法头我们需要去来费一点周章方法的响应，我们给它直接塞入一个参数 set ID，OK，同学们，这里记住 pertobuf 有一个非常明显的一个使用上的规矩，就是说你每次调用 set 方法的时候，不管 set 谁，你这里不能 set 一个空。那如果你 set 一个 none 的话，它这边在这一行就会直接抛出异常有这样的一个规矩。所以大家记住每次调用 set 方法一定要 set 一个有值的东西，那接下来我们在这个方法体当中去定义一些参数。


首先我这边需要去定义一个谁 request mapping，我给它的对应的 value 叫做谁叫做 test part，这就好了，接下来我需要对这个方法内的可以接收的 content 类型做一个定义，那我这里直接 copy 过来一个什么呀？ method 是post。与此同时，上面的这一个关键 produces 是我允许接收什么application，杠 x part of buff 允许接受这样的一个协议，允许接收我的访问请求使用这样的一个响应类型。


那咱的这个方法把它已经定义好了，实际上这个任务只完成了一半儿，那剩下一半的任务我们需要到 employee service 当中来进行，发起一个真正的调用这个接口。我们走到 employee core。那在这个项目当中，由于我们实际上在底层已经继承添加了这个 restroom API 的依赖，那么因此 pertobuf 的这些依赖也被顺理成章地添加了进去，接下来我们这里就来写一个份方法，打开原先的份的定义类，它叫 restroom 份client，那在这个类里面我们去添加一个方法，来去调用咱前面已经定义好的 resume service 当中的这个新的方法。它返回的值，我把它叫做string，直接返回一个 string 就可以了，那它返回的值呢？就是我们的 proto response，那方法名也叫 per to 号了对应的接收的参数，这个平淡无奇的参数叫 request param，它的名称叫做赐予你姓名ID，给它一个 long 型号了。


那这个方法定义完之后，同学们这里也要去麻烦一下，我们要定义一个 request mapping，那我这里直接把它 copy 过来，不跟同学们一行打了，大家来看一下发起的这个请求，地址和刚才咱在 restroom 里面定义的是一样的，对应的 method 也是post。这里我不光要定义一个produces，我还要定一个consumers，那证明我发送接收实际上都是以 part two buff 这样的协议来去做的。


到这里，同学们我们可以去写一个 Controller 的方法了，似乎离完成又近了一步。咱在 Controller 里我们填写的这个方法可以给它起一个名字，叫做 public string test proto buff。那它接收的参数是一个long，我可以写一个count，跟下面的保持一致对应的返回值。我们从这个 rest service 里面做一个调用，叫 turn to，然后传入一个具体的 I d 就是 count 接收，拿什么来接它？拿 prayer to response 来把它接收好嘞？对应的我这边返回之前咱先打一个log。同学们在生产环境当中要记住这是一个好习惯，在一些关键路径上打一些日志，咱以后生产环境碰到什么各种各样的问题，只能靠它了。那在最后返回的时候，可以直接返回 part to response 这个对象，但是因为我们的 Postman 有一些限制， Postman 现在还不支持 pertobuff 这种协议的调用，所以我们这里要搞一个曲线救国。怎么救？就是把这个类给它转换一下，转换成 pure string，纯一个 string 的对象。我这里使用的转换的类就是 json for matter，那它是个咱前面加入的这个依赖项， Google code 里面的一个类，我去调用它的 print two string 方法来，非常的方便把它扔进去。好嘞，大功告成。 llama 没有，这里还差最后一步，万里长征最后一步是什么？是添加一个page。


同学们还记得咱的份组件啊？我们在份组件干了啥事儿？哎，我们对它干了啥事儿？我们这里定义了一个接收 expert buff 的这样的一个方法。那么对应诶，咱有没有去设置一些Converter？没有。那所以份这里还不能处理 purdubuff 这种协议的反序列化的操作。


所以说我们接下来在这个孟函数的这个地方，咱给它创建一个类，这个类是一个配置类，叫做 FIN part to buff configuration okay，创建出来，那创建出来之后，咱在这个类上面挂一顶大帽子，绿帽子扣上configuration。


紧接着我们这里声明一个 b 这个 bin 它是什么类型？同学们看 per to buff h t p message converter，从这个名字就可以很清晰的看出来它是做什么的。那转化 HTTP message，它这边 return 的时候，我什么都不用做，直接 return 一个新创建的 purdubuff message converter。那这里边有参数吗？哎，非常的贴心，什么参数都没有，一个分号结尾。


OK，定义好了这个 Converter 之后，独越乐与众，乐乐，熟乐不若与众。好东西要拿出来跟大家分享。我们这里不光咱的这个调用方使用了Converter，咱的这个服务提供者 restroom 这里它是不是也是要使用它？没错，我们把这个 Bing 也同样的给这个 restroom application 也送他一份。那OK，那送完一份还不够，我们这里还要去买一送一。


这是序列化的Bing，接下来我要给它去定义一个反序列化的Bing，叫 rest template，然后它接收的是谁？你前面创建什么，我后面接收什么。结束完了之后，直接 return 一个新的 arrest template，然后它接收的值 collections single town list，这个 list 里面传入的就是咱上面的这个converter。那我这里定义好之后，同学们别忘了把这个 bin 也给它加上去。


好，这里都已经被置妥当了之后，我们要把这个应用给大家重新启动一下，把这个序列化还有反序列化这两步的 b 都给它重，再加入到上下文当中。那么在启动 resume service 的过程当中，我这边也可以去同步的把 employee application 也给它启动起来。好，组里，这两个等到都启动起来之后，我们打开 postman 来发起一个严肃的方法，调用好。我们点开postman，去调用咱前面创建的这个 per to buff 的一个Controller，那这个 Controller 是指向谁呢？ employee service，同学们不要调用错了，咱这个矛头要对准 employee service 里面新创建的这个 Purdue 这样的一个方法，它是post，我接下来在这边去调用它一下，传入的这个 count 是10，准备321。同学们看到这里它返回了一个纯string，这个 string 我把它改成 json 格式。同学们看到它对应的这个数，这个内容是这样的，我把它贴到这里，看得清楚一些 ID 要领，那你这边的 count 填多少，它对应的就会返回一个同样 ID 的这样的一个对象，那从这个角度来，我们就看出来咱的这个 protobuf 已经成功地集成到了份组件当中。


那如果同学们在自己项目当中需要去做一些跨语言、跨平台的这样的服务，可以使用 Protobuf 作为它的不描述语言。这样的话对应的 Python 也好， go 也好，任何语言都可以基于某些插件来去将你的 part buff 文件做一个解析，自动地生成对应的类，那你一行代码都不用写，不拿老百姓一针一线，这个类就这样写好送给大家了。


而且你的代码结构还会非常整洁，因为这些最终生成的类，它其实直接跑到了你的这个 generate sources 下面的 protobuf 文件里，它不会去在你的 Java 文件夹下面生成了一堆内容。同时在我们提交 GitHub 的时候， target 下面的类是不会随着一同提交的，所以你的代码就会非常整洁。OK，同学们，那我们这一节的内容就到这里结束了，那我们下一节当中跟同学们做一些篇墨章节的总结，以及对应的面试辅导，还有作业。好，同学们，我们下一小节再见。



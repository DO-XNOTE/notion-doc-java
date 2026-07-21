---
title: 3-9 Seata TCC方案落地（上）
---

# 3-9 Seata TCC方案落地（上）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/deb1f201-1ea6-4657-be4a-1e5f246bf380/SCR-20240921-cpym.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664Z6IJJL2%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGefkSfK5qjOU4LkRgvZXXJdrNGJQkLJ7qrso%2Bv2VsPWAiEAiTYpKhDcE%2BopUM2KEZTHNU8C2rBZ3w9QefEiLOUNubwqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFSfiBhsA2QBaJ%2BTpircA8aWTFPw0byuRMndqeIR7oOT7%2BPlVV%2B5ra1LQxqkss%2Ftib%2FYYs5ThR0r1AMk4DG1EvGROA0uYeRyPDwHX489WvENli8ctCBVp3%2BIc5%2B13pTQx%2BiTp8%2BA6uZQtv8aQoGXxiNmnxTM9PO5xIuHGfTwIFFDR01LsRCZyGkzNbAideOg59EnnvwUUNRI75EOHuMm5LKndgCz%2F%2Bdj5DcS5ShKCZSGd5AYZnuvuiaefNQ1j7ZTdYqeYq1waClvi89fxdeeWwWW%2BTbJd4yhbwjA41Z9LA4g3jA%2B3mckcxVW3W%2BAgjFOsQO8ZtOtmLDsjO3%2F3WRxhpxZ1Kay4Ko2x9bbQfJMp9REpSRyivska%2BaOY3gM2nulyYmCTucHud3bOcdwBYkcALBeVywipQpUJplug0VybKnKHgtY9vCzwMq7W4cHPzMWpti4ntnJmACfTSJfK0J%2BoBUuHjoJ7KP4HH7EJP5R%2FPfsKzl60UakKsMLOEOj%2Fn0Qud4%2BAFUTMaDlvFs9x7BX9o7wIw%2B73LmZpD%2B7iCP7BvDJwSbd%2BBm7%2Bw10vgedSJr91p%2F7kzUMUoZ9lDc9yU8KefMh1ISmbwjL0Tm7XqLpVp0FFfRiZDI3BQ9JNOjMA5y5BL7nTt%2BluwDiaYKWMNi5%2F9IGOqUBT4chaotZjBC10AeO0uo03kyLEKdOFSwfcCGO1Yrm9rGhLOWoHpwNQxbnwa%2F8ayBEbmsSsGVY218Yo56pa4t9KQ7ChgqnKzVk3Etf3mMp7kvWHCcShgX4x%2BRKmIpn%2BUiZsPXd41VTHq2%2BWbOMblJIMFD6vwgJrZ2%2Ff5YFJxK0I6ZNXj5i4Q9JZ0PFqWgvyL15DVwhhbcA6dXMcyckIczYQQQwGfpp&X-Amz-Signature=59bf3575036acc485aa79e78ac5beadba7c572f723f01c8b3e56e8bd74f0d686&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/83fe9c26-1cf7-4aee-998c-0dbe1be3d60a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664Z6IJJL2%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGefkSfK5qjOU4LkRgvZXXJdrNGJQkLJ7qrso%2Bv2VsPWAiEAiTYpKhDcE%2BopUM2KEZTHNU8C2rBZ3w9QefEiLOUNubwqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFSfiBhsA2QBaJ%2BTpircA8aWTFPw0byuRMndqeIR7oOT7%2BPlVV%2B5ra1LQxqkss%2Ftib%2FYYs5ThR0r1AMk4DG1EvGROA0uYeRyPDwHX489WvENli8ctCBVp3%2BIc5%2B13pTQx%2BiTp8%2BA6uZQtv8aQoGXxiNmnxTM9PO5xIuHGfTwIFFDR01LsRCZyGkzNbAideOg59EnnvwUUNRI75EOHuMm5LKndgCz%2F%2Bdj5DcS5ShKCZSGd5AYZnuvuiaefNQ1j7ZTdYqeYq1waClvi89fxdeeWwWW%2BTbJd4yhbwjA41Z9LA4g3jA%2B3mckcxVW3W%2BAgjFOsQO8ZtOtmLDsjO3%2F3WRxhpxZ1Kay4Ko2x9bbQfJMp9REpSRyivska%2BaOY3gM2nulyYmCTucHud3bOcdwBYkcALBeVywipQpUJplug0VybKnKHgtY9vCzwMq7W4cHPzMWpti4ntnJmACfTSJfK0J%2BoBUuHjoJ7KP4HH7EJP5R%2FPfsKzl60UakKsMLOEOj%2Fn0Qud4%2BAFUTMaDlvFs9x7BX9o7wIw%2B73LmZpD%2B7iCP7BvDJwSbd%2BBm7%2Bw10vgedSJr91p%2F7kzUMUoZ9lDc9yU8KefMh1ISmbwjL0Tm7XqLpVp0FFfRiZDI3BQ9JNOjMA5y5BL7nTt%2BluwDiaYKWMNi5%2F9IGOqUBT4chaotZjBC10AeO0uo03kyLEKdOFSwfcCGO1Yrm9rGhLOWoHpwNQxbnwa%2F8ayBEbmsSsGVY218Yo56pa4t9KQ7ChgqnKzVk3Etf3mMp7kvWHCcShgX4x%2BRKmIpn%2BUiZsPXd41VTHq2%2BWbOMblJIMFD6vwgJrZ2%2Ff5YFJxK0I6ZNXj5i4Q9JZ0PFqWgvyL15DVwhhbcA6dXMcyckIczYQQQwGfpp&X-Amz-Signature=9db878f367145bfade97ae324d7aacbe3b278aedd269be497ea9d06c90a5122c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/dda99e79-a34b-49a1-af17-4eb0b556506d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664Z6IJJL2%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGefkSfK5qjOU4LkRgvZXXJdrNGJQkLJ7qrso%2Bv2VsPWAiEAiTYpKhDcE%2BopUM2KEZTHNU8C2rBZ3w9QefEiLOUNubwqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFSfiBhsA2QBaJ%2BTpircA8aWTFPw0byuRMndqeIR7oOT7%2BPlVV%2B5ra1LQxqkss%2Ftib%2FYYs5ThR0r1AMk4DG1EvGROA0uYeRyPDwHX489WvENli8ctCBVp3%2BIc5%2B13pTQx%2BiTp8%2BA6uZQtv8aQoGXxiNmnxTM9PO5xIuHGfTwIFFDR01LsRCZyGkzNbAideOg59EnnvwUUNRI75EOHuMm5LKndgCz%2F%2Bdj5DcS5ShKCZSGd5AYZnuvuiaefNQ1j7ZTdYqeYq1waClvi89fxdeeWwWW%2BTbJd4yhbwjA41Z9LA4g3jA%2B3mckcxVW3W%2BAgjFOsQO8ZtOtmLDsjO3%2F3WRxhpxZ1Kay4Ko2x9bbQfJMp9REpSRyivska%2BaOY3gM2nulyYmCTucHud3bOcdwBYkcALBeVywipQpUJplug0VybKnKHgtY9vCzwMq7W4cHPzMWpti4ntnJmACfTSJfK0J%2BoBUuHjoJ7KP4HH7EJP5R%2FPfsKzl60UakKsMLOEOj%2Fn0Qud4%2BAFUTMaDlvFs9x7BX9o7wIw%2B73LmZpD%2B7iCP7BvDJwSbd%2BBm7%2Bw10vgedSJr91p%2F7kzUMUoZ9lDc9yU8KefMh1ISmbwjL0Tm7XqLpVp0FFfRiZDI3BQ9JNOjMA5y5BL7nTt%2BluwDiaYKWMNi5%2F9IGOqUBT4chaotZjBC10AeO0uo03kyLEKdOFSwfcCGO1Yrm9rGhLOWoHpwNQxbnwa%2F8ayBEbmsSsGVY218Yo56pa4t9KQ7ChgqnKzVk3Etf3mMp7kvWHCcShgX4x%2BRKmIpn%2BUiZsPXd41VTHq2%2BWbOMblJIMFD6vwgJrZ2%2Ff5YFJxK0I6ZNXj5i4Q9JZ0PFqWgvyL15DVwhhbcA6dXMcyckIczYQQQwGfpp&X-Amz-Signature=e9b6429c2b738a7d38f82925c49767680e9486b7883a51166cb7b84c5e5c3825&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b9821cec-fbcb-4eac-8dc9-bc2a68d3cef9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664Z6IJJL2%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGefkSfK5qjOU4LkRgvZXXJdrNGJQkLJ7qrso%2Bv2VsPWAiEAiTYpKhDcE%2BopUM2KEZTHNU8C2rBZ3w9QefEiLOUNubwqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFSfiBhsA2QBaJ%2BTpircA8aWTFPw0byuRMndqeIR7oOT7%2BPlVV%2B5ra1LQxqkss%2Ftib%2FYYs5ThR0r1AMk4DG1EvGROA0uYeRyPDwHX489WvENli8ctCBVp3%2BIc5%2B13pTQx%2BiTp8%2BA6uZQtv8aQoGXxiNmnxTM9PO5xIuHGfTwIFFDR01LsRCZyGkzNbAideOg59EnnvwUUNRI75EOHuMm5LKndgCz%2F%2Bdj5DcS5ShKCZSGd5AYZnuvuiaefNQ1j7ZTdYqeYq1waClvi89fxdeeWwWW%2BTbJd4yhbwjA41Z9LA4g3jA%2B3mckcxVW3W%2BAgjFOsQO8ZtOtmLDsjO3%2F3WRxhpxZ1Kay4Ko2x9bbQfJMp9REpSRyivska%2BaOY3gM2nulyYmCTucHud3bOcdwBYkcALBeVywipQpUJplug0VybKnKHgtY9vCzwMq7W4cHPzMWpti4ntnJmACfTSJfK0J%2BoBUuHjoJ7KP4HH7EJP5R%2FPfsKzl60UakKsMLOEOj%2Fn0Qud4%2BAFUTMaDlvFs9x7BX9o7wIw%2B73LmZpD%2B7iCP7BvDJwSbd%2BBm7%2Bw10vgedSJr91p%2F7kzUMUoZ9lDc9yU8KefMh1ISmbwjL0Tm7XqLpVp0FFfRiZDI3BQ9JNOjMA5y5BL7nTt%2BluwDiaYKWMNi5%2F9IGOqUBT4chaotZjBC10AeO0uo03kyLEKdOFSwfcCGO1Yrm9rGhLOWoHpwNQxbnwa%2F8ayBEbmsSsGVY218Yo56pa4t9KQ7ChgqnKzVk3Etf3mMp7kvWHCcShgX4x%2BRKmIpn%2BUiZsPXd41VTHq2%2BWbOMblJIMFD6vwgJrZ2%2Ff5YFJxK0I6ZNXj5i4Q9JZ0PFqWgvyL15DVwhhbcA6dXMcyckIczYQQQwGfpp&X-Amz-Signature=a4348422c57d7a6a48750d963ef05ac6d5e74632c31268a5de9172d772b768aa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

哈喽，木框的各位同学们，大家好，我是姚半仙。那我们这一节就开始进入一个动手的环节，咱在项目当中对 Theta 的 TCC 方案做一个快速落地，这样的话我们项目里就会同时存在两套分布式事务解决方案，那几个接口使用 Theta 的 at 方案，另一个接口使用咱 Theta 的 TCC 方案，我们把这两个方案的实现方式做一个小的比较。


OK，同学们，那准备好的话跟我就到 Intellijitly 走起，写 bug 的每一天都是超越自己。同学们呐，现在我们又回到了项目里，那咱在这个一篇章的改造环节，我们先从哪一个开始？按照老规矩，咱就先从这个 restroom service 这个应用来开刀了。

OK，那我们这个 Theta 的 TCC 方案，别管是 TCC 还是说是at，那实际上它这里面的依赖项是不变的，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/adc66433-5f39-4752-a3de-7972d04788ba/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664Z6IJJL2%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231411Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGefkSfK5qjOU4LkRgvZXXJdrNGJQkLJ7qrso%2Bv2VsPWAiEAiTYpKhDcE%2BopUM2KEZTHNU8C2rBZ3w9QefEiLOUNubwqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFSfiBhsA2QBaJ%2BTpircA8aWTFPw0byuRMndqeIR7oOT7%2BPlVV%2B5ra1LQxqkss%2Ftib%2FYYs5ThR0r1AMk4DG1EvGROA0uYeRyPDwHX489WvENli8ctCBVp3%2BIc5%2B13pTQx%2BiTp8%2BA6uZQtv8aQoGXxiNmnxTM9PO5xIuHGfTwIFFDR01LsRCZyGkzNbAideOg59EnnvwUUNRI75EOHuMm5LKndgCz%2F%2Bdj5DcS5ShKCZSGd5AYZnuvuiaefNQ1j7ZTdYqeYq1waClvi89fxdeeWwWW%2BTbJd4yhbwjA41Z9LA4g3jA%2B3mckcxVW3W%2BAgjFOsQO8ZtOtmLDsjO3%2F3WRxhpxZ1Kay4Ko2x9bbQfJMp9REpSRyivska%2BaOY3gM2nulyYmCTucHud3bOcdwBYkcALBeVywipQpUJplug0VybKnKHgtY9vCzwMq7W4cHPzMWpti4ntnJmACfTSJfK0J%2BoBUuHjoJ7KP4HH7EJP5R%2FPfsKzl60UakKsMLOEOj%2Fn0Qud4%2BAFUTMaDlvFs9x7BX9o7wIw%2B73LmZpD%2B7iCP7BvDJwSbd%2BBm7%2Bw10vgedSJr91p%2F7kzUMUoZ9lDc9yU8KefMh1ISmbwjL0Tm7XqLpVp0FFfRiZDI3BQ9JNOjMA5y5BL7nTt%2BluwDiaYKWMNi5%2F9IGOqUBT4chaotZjBC10AeO0uo03kyLEKdOFSwfcCGO1Yrm9rGhLOWoHpwNQxbnwa%2F8ayBEbmsSsGVY218Yo56pa4t9KQ7ChgqnKzVk3Etf3mMp7kvWHCcShgX4x%2BRKmIpn%2BUiZsPXd41VTHq2%2BWbOMblJIMFD6vwgJrZ2%2Ff5YFJxK0I6ZNXj5i4Q9JZ0PFqWgvyL15DVwhhbcA6dXMcyckIczYQQQwGfpp&X-Amz-Signature=6198e2051f9c105e077388a9bcc5014cb8d8bb52b5a571740cf2cb2b15c04dfb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

都是依赖于我们的这个 Theta 的服务，所以说我们在这个 dependency 里面不用做任何的改动，那咱就直接使用这个阿里巴巴 Theta starter 这一个依赖项就够了。那咱现在开始直接来写代码，尝试着把其中的一个服务改成 TCC 的调用。


哪一个服务？我们点开这个 resume service 这里来看一眼。好，现在去挑选一位随机观众，把它给改成咱的分布式调用，挑选谁？同学们，还记得我们在前面的小节里，这个 at 方案是选择的哪一个方法吗？我们点开这个 employee service 这里来看一下咱在这个 at 方案里面，我们的 global transaction 加到了这个 use toilet 上面。OK，那这个抢占坑位使用的是 at 方案。接下来我要把这个释放坑位这个 restore toilet 这个方法相应的改成 TCC 方案。好，那我们回到 restroom 这里面，我们把这个方法开始动手改起来，这里就是我们的 release 方法，那这是释放坑位的一个操作，那在这个方法里，我们读取到了一个toilet，然后对它做了相应的改造，对吧？那我们这里如何把它改成TCC？同学们想 TCC 的第一个阶段三步走，第一个阶段是什么呀？no，做 no die， why you try？那我们这里怎么try？要锁定资源，锁定资源，我这里对它底层的这个 toilet entity 咱做一个小的改动，前面有 available 和 clean 这两个动作，我这里给它添加一个锁定资源的字段，叫 booked 或者叫reserved，也都可以预定，应该叫 reserve 的更好一些。好，然后把这个 column 给它加上，那这个knowable，我给它设置成 true 好了。


OK，那其实同学们如果用这个available，实际上也可以把它当做是一个锁定资源的标签。但是我这里更建议同学们使用一个单独的标签来专门作为 TCC 阶段的一个锁定。比方说这个reserved，那我们可以把它映射成咱的数据库，数据库 data grade 这里同学们看到这个 toilet DB，我们把这个 toilet DB 做一个增强，给它 edit 这么一下， edit table，把其中的这个字段改成reserved，把这里新添加一个字段改成reserve。


OK，好，改完之后我们去搜索一下这个toilet，我们可以看到它现在除了 ID clean available，这里还有一个多余的参数，reserved，就是我们新添加了这个。OK，那咱添加完了这个之后，接下来我就要去开始写 TCC 的三阶段的方法了。那这个三阶段的方法写起来有这么点意思，同学们记住第一步，我们写三阶段方法的第一步，我要去先定义一个 try 方法，那这个 try 方法我就直接把这个 release 给它 copy 一下，原先的方法咱不动，咱另起炉灶好了，这样显得干净一些。咱另起炉灶这个方法给它起名叫 release TCC。


OK，那把这个 override 先去，先暂时给它去掉，那这个 release DCC 它这里怎么来操作？那首先我一个 try cache 先给它包裹起来，这个 try cache 加不加都可以。那我这里加上只是为了更好地捕捉打印一些日常日志。 try 这里第一步我要给它打印一些 log info，给它非常响亮地标记出我当前是什么阶段，是个 try release TCC 阶段。OK，那我在这个 try release 里面我打印一些关键的参数，比如说当前的ID，给它 c 进去。好，那 c 完 ID 之后，那咱这个后面的流程都跟我们前面保持一致就好了。咱把这一段给 copy 下来。OK，全部 copy 下来，然后复制进来的同时，同学们想我们这个是锁定词源对不对？那锁定怎么锁定？我们先不要把它给占用，这个 set clean， set available，这属于已经去执行业务了，那我们要放到这个 confirm 阶段执行，那我们的 try 阶段，咱就直接去 set reserve 的标记说我当前这个卫生间已经被预定住了。


OK，如果我当前阶段没有这个可用的卫生间，或者这个卫生间已经被人给锁定了，那么这种情况下就相当于我这个锁定资源失败，对吧？好，那失败的话我就怎么样扔出一个异常，那在扔出异常的同时，我这边 log 把它给接住，打印一个日常日志叫 cannot release the restroom OK，嗯，那这里我把这个异常直接扔出去。


through e，好，那咱的 TCC 这个 try 方法呢？已经把它给完成了。 release TCC，接下来我要去执行那个confirm，还有 cancel 方法。 confirm 和 cancel 这里我采用同样的方式，我把这个方法给它 copy 一下，把这个 public 全部给它 copy 过来。在这里创建一个新方法，给它起名字，我要起的不一样，叫 release commit OK commit 好，那这个 commit 它接收的参数这里不是 ID 了。


同学们，我这里变一个姿势，大家看，我传入的是一个当前分布式事物的上下文，它的对象的名称叫 business action context，叫 action context OK，我传入它同学们想有什么作用没有？那跟同学们讲大有作用。这里首先第一步我要打印出一些标志的日志，我要打出你的这个 confirm 阶段， confirm release TCC，好，打出这个阶段。与此同时我这边还要再多打出一个参数，是谁？同学们跟我看，你这个 confirm 自然要去查找一个 toilet 的ID，对不对？这个 ID 从哪来？咱前面不是加入了一个上下文对不对？咱这个 ID 就从我们的上下文当中来，怎么来？同学们跟我看，这个上下文里面别有洞天。


这里有个方法， get action context，我可以指定一个key，那咱这里指定的这个 key 就是我们的ID。OK，那这个 ID 如何来获取？我们先把这个问题暂时保留着，等会再跟同学们揭晓。那我获取了这个当前的 ID 之后，我这边要再输入一些标志性的信息，比方说 ID 等于谁？然后我再输入一个 XIDXID 是什么呀？全局的分布式事务对不对？从哪里来？咱这个 action 不是吃浅饭的。 get XID 好，获取到之后，同学们看我这里原封不动，通过它把这个 ID 给它 get 到，那 get 到了以后，我这边给它来一个转换，我把这个参数改成optional。这里我要去做一个小的判断，咱的这个 confirm 阶段是提交业务，执行业务的阶段。所以说一旦 if 你的 optional 这个toilet，我把它改成 optional toilet。一旦它当前是存在的，我们这里要写一段逻辑，这个逻辑是，那如果present，如果它存在我这里，把它给拿到好了。 toilet entity，我把它给拿到。拿到之后干什么？我要去执行业务。


同学们，执行什么业务？很简单，第一个我要 set clean，把它设置成true，已经清空了，对不对？然后物归原位， set available，你当前也处于一个可用状态了。与此同时，怎么样？我要把咱这个踹阶段这里冻结的这个 flag 给它置空，给它置成false。


好嘞，就这 3 步，很简单。然后 save 的时候同学们想，我 save 完我要 return 一个值，对不对？咱这个 TCC 这里有一个不一样的地方，我在 commit 方法里，实际上我不用 return 这个对象，你 return 对象会直接报错的，我 return 谁？布尔值，那这个布尔值怎么界定？同学们，看你更新成功， commit 已经成功，我 return 一个true，证明你当前分布式事务 commit 阶段成功了。


那假如它不成功怎么办？很简单，我们在这个 cache 方法里给它 return 一个false，OK，那同学们，这里跟大家提一个问题诶，你查找这个toilet，如果查询到了诶，那接下来我走一个 commit 对不对？那如果查询不到怎么办？这里实际上就要根据业务来去思考了，因为为什么呢？如果你查询不到，想让上游链路都回滚，OK，那你这时候可以扔出一个false，查询不到else，直接扔出一个false，这种情况下我们就会去转而执行一个 cancel 方法，那你所有的这种业务逻辑要在 cancel 里面把它给处理好。OK，那这个是我们的 TCC 三阶段当中需要注意的一个点，也就是什么时候你认定这个 commit 成功，什么时候认定失败。OK，那咱这个 commit 完了之后，我们接下来再来写一个方法，这个方法叫cancel。好嘞，那把这个方法名咱给它改一下，改成cancel，改完之后这里我们把这个前面的 log 也给它改成 cancel 好了。


那同学们想我在自己的这个业务当中 cancel 是什么含义？我的 cancel 是想要把这个当前的数据库的这些字段信息，把它重新打回到你在执行这个 try 之前的样子，对吧？所以说我这边要怎么打？这里clean，我执行之前应该是false，OK，我这里把它置成false， available 也是false，与此同时，这个 reserve 是不是也是false，对吧？ 3 个全部执行完毕之后，直接 return 一个true，如果失败 return false，OK，那这里也给同学们提一个小的点，就是说一旦你这个 ID 找不到，我在 cancel 里面应该怎么来做？咱在 confirm 里，如果你 ID 找不到，还可以这里，对吧？这里直接 else return 一个false，然后进入到咱的这个 cancel 流程当中，但是同学们想，你在 cancel 当中应该怎么来做？如果你这边接收到了一个不存在的ID，假设你这边把它 return 了一个false，那你知道这个任性的 TCC 将要执行什么操作吗？它这里会进入一个无限循环，不停地重试，重试谁不停地重试cancel，你不是失败吗？失败我就不停地重试，以保证我的 TCC 三阶段的幂等性。所以同学们在这个 cancel 里记住，要做一轮最后的兜底容错，把所有的异常情况全部给它考虑进来，最终把它执行一个成功。


什么？成功？回滚成功？即使你当前的参数根本没有任何值要回滚的，哪怕它是一个空回滚，咱都要保证最后返回一个true。除非你正儿八经真正的在回滚过程当中，比如说你 save DB 的时候抛出了一场，那么这种情况下我们才会返回false，这是我们做 TCC 方案当中一个非常重要，非常需要关注的点，就是说咱这个方法返回 true 还是返回false，是否回滚成功？它的语义是取决于你当前的这个数据是否已经回滚到了你在执行 try 方法之前的样子。假如你这个 ID 根本找不到，那说明没有东西需要你回滚的，那你这里也可以直接返回一个true。


OK，那这是需要关注的几个点。那到这里呢？我们整个业务逻辑就已经全部完成了，接下来我们才进入正系咱这个 TCC 的一个核心的部分。同学们记住我们这里的 TCC 方案是什么呀？是使用 rest API 的形式，它不是一个 RPC 调用，所以说我们要对它做一番小小的改造。


老师这里创建一个新的 Java 类，给它指明成一个叫 interface 接口，然后把它命名叫 irrestroom t c c series。OK，这个接口创建好之后，我把它extend，然后把它继承自一个什么接口，继承自我们外层的 i restroom service 好，然后在这里同学们，我们要编写 3 个不同的方法。



这 3 个方法来自于谁？我们来看来自于刚才写完的这个 resume service。我把它的这个继承类由 i restroom service 改成咱刚才创建的这个 TCC service。然后我在这里把咱刚才创建出来的这个 release 方法给它 copy 一下。好，这里另有用处，我们把它 copy 到这个 resume service 这里。好， copy 进来。我接下来要来加一些特殊的标签。


这个是我们 TCC 的关键，拟一个分布式方法，分布式的事务，它执行到这个方法究竟是走 AD 方案还是走 TCC 的方案，取决于这样的一个注解，同学们看 to face business action，那这就是我们关键的 TCC 的注解。有了它，同学们就记着，有了它，我们方法执行到这里的时候就会走 TCC 的路子。那我们首先第一个给这个 TCC 起个名字，好吧，就叫 release TCC。好，那与此同时我还要额外指定 commit method 是谁。当前我如果 try 方法执行成功，我要执行这个对应 confirm 方法，以及我要对应 rollback 方法是谁，那release，rollback， release cancel。好，我这里都给它写上来。OK，那这是其一。其二还有一个要改造的东西，是第二个标签，我们这里要将这个 ID 把它加入到分布式事务的上下文。

为什么？同学们看咱的 restroom service，这里前面一个方法是 release TCC try 阶段，在我们的 commit 阶段和咱的 cancel 阶段里，你的这个 ID 从哪来的？同学们，看到这里，你的这个当前 toilet ID 是从上下文来的，所以说我们这里要给它做一个特殊的属性，叫 business action context parameter，我通过这个属性来把一个 ID 把它添加到上下文当中。


OK，把它添加到分布式事务上下文里。这是第二个注解，这里还有最后一个注解。同学们，记住，你如果不是用的 double 这种 RPC 形式的调用，你用 spring MVC 或者是 spring cloud 这种 HTTP 的方案，要把这个注解也给加上 local TCC。OK，这个注解这里同学们记住必须加在接口上，如果你加在实现类上面这个接口，这个注解它不生效的。 3 个注解加完三杯酒下肚，接下来我们怎么做？咱不是填写了这个 commit 和 rollback 方法，对吧？我们这里紧接着就把这两个方法在接口层里面，咱都给它定义出来好了。好，我们把这个方法给它 copy 一下，走到接口层里面，不紧不慢，我们把它给复制过来。OK，那这是 cancel 方法，接着再把这个 commit 方法也给它复制过来。好嘞，复制完这两个之后，咱什么注解都不需要再额外添加，只用我们把这个当前的 resume service，我为了编程安全，我给它加一个override。


OK，那这是 cancel 方法。再往上这个 commit 方法也给它大帽子盖上，在上面的这个 release DCC 盖上。好，让我们再稍微地梳理一下这 3 个方法。 try 方法阶段，那我去获取一个坑位，然后做一层过滤。如果你坑位没有被reserve，你看这里就有一个小的不一样的地方，你这个坑位要是没有被 is reserved，要是没有被reserve，才能被它 filter 出来，对吧？这才是正确的。如果没有被reserve，我把它设成reserve。如果所有的没有获取结果，那么直接抛出一场，OK，那这是 try 阶段的一个正确的代码。


接下来我们再看这个 commit 阶段，这里实际上当我发现了一个 toilet 之后，那我们在 commit 这里实际上不光是要判断它是否存在，与此同时我还要再去判断你当前它这个存在的这个单元，它里面是不是一个 reserved 的对象。如果没有 reserve 怎么办？没有 reserve 那就直接到 else 了，说明你的 try 方法没有执行。对，OK，同学们要把这个弯给它绕过来，那这里我们把这个方法呢都已经执行完了，那对应的 cancel 这里没有什么问题。


好，接着还有一个地方，同学们不要忘记了，咱的 spring MVC 在启动的时候，将要去检查你上面的所有的注解的访问路径，这里不能有重复，因为我们前面已经有一个服务，它使用了这个 release 路径了。所以我们这里要把这个 release 给它改一下，换一个名称，我这里就把它换成叫 release TCC。


OK，紧接着我们就可以发起一个服务启动的命令，把这个 restroom 跑起来。在执行之前，我们先确保你的 Theta server 在本地已经是一个启动状态了，然后才能启动这些对应的服务。好，我们稍等片刻，看一下他这边会报什么异常。OK，走到这里，看样子已经全部启动成功了。好，我们关闭它，走到我们的浏览器里刷新一下。


好，我们可以看到一个 resume service 已经完整的启动起来了。OK，那接下来我们回过来，那这个分布式事务改造完 resume service 这里只算是完成了大概 2/ 3，紧接着我这里要对咱的 employee service 也做一个改造。





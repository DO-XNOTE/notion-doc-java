---
title: 2-4 上传头像 - 为静态资源提供网络映射服务
---

# 2-4 上传头像 - 为静态资源提供网络映射服务

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/062fdb6e-439b-414f-ac58-7c099339cdff/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHVD73OL%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224726Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDC7iTC06Gz6jYU6kiq9vnPIEQptMXPMUL57y1LCAeeVQIgPX6GV860oVxp1xYMaEI%2BXA%2FZSwdIp93shjPkK%2BgXNbkqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHx97TMHh9QzI3qLTircA5Nm2KT3cRjP0f%2BnxLP4b5jaZlUnTkN1uc4kQVLvzL950e7yTXLWVAmDcvIWNBQH04zdsPBWLy9sGbSuxQ2VxQhF7wIfBpBO45MfSAKeIrgNroOg7%2B2UKAtahMQlBAV3LRJOwDn%2BZ3zLQfNSiJJEXwGjOzr76AJnoVKzHfE5H2lfM5xxshjyxx5MoDyjdalk5Xikf7J8fSv3DG05F2Zmz9hKTFinJH4FElgfapg4KPoEM2NVl%2B7Atqaa%2B2rw05ZIRH1fjw%2BsgprpQegn0KAVbzQ5fbEXitThTiSvNmRIyXcHmKHfO4Si6WLV0DBUvrWzi%2BCcQ0NIVslrKrelV6T1cwAEsYNr8q0emMNDGBJHX06f%2BTI9DS2GQdSkBOn6QUtw0%2FsoWZEM6Ekg6sxxE1TTrkGXCZKA8WAZ%2FvR%2B5Nt7EQdN1m417WwNaXGjMjBD5VNLrLOHxRl0zmqxBZ1a8uqimgUGuC3kgwxqj5MMEWLGn%2FgXcz1u9VvihOoI1dH6asVf16NVs7o7yHDLPGvsHxIUwLmq%2FbWRlcnoMSzoYlYvu0%2Fia8gIcHBbKxRzy6QLxs7I9RJ9ltkD23ap%2FLs5bnpIF%2F1aGMeJBylP2FtvpYbs87UiMCLU8pmEK%2B9gy01VMMG3%2F9IGOqUBjLUtahIb5jOv0LYe5EbNjl3IR1W3zNdOun0E2q%2FxXCyquNdw5GbKlH2uHy%2BmnHRRTy9Mgkjp80PfE%2B0UKKArvoeHQqMKEo%2FFPTrWdQX%2FepnjgXlXXm%2FjbTmyW%2FgYy6Jas%2FvHXM0mzIaEhPXzZSyeEowsmoeg6hl%2BIhSXEhHhJf0QgFOhrG9seMK31lQ5cMFiwG3GDOhhJv3kEutvujjcZMh4Z%2FI7&X-Amz-Signature=72f44cc4c4bfdc82ba82aa91e34292ce5d6dccb9f828a96ecf03ec1311a9940d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

现在我们的图片是上传到了服务器，也就是在我们当前本地的文件系统里面，我们要去查看。我们是需要双击进行打开的，双击打开以后，我们在浏览器上是看不了的，因为它没有服务如何去看，如何去把图片在浏览器上打开，很明显我们要为它增加一个服务。在 spring boot 里面或者是在 top net 里面，它其实会有一个资源映射的这种说法。它可以把服务器里面或者是在文件系统里面的一些静态资源文件发布到服务了。以后我们就可以通过浏览器的形式去访问了。这些自研文件不仅仅是图片，包括音频、视频，其实都是可以去进行发布的。这节我们就来看一下如何去做一个服务资源的映射。


首先我们先来看一下，在我们当前的目录里面，我们创建了一个 WebMvcConfig，这个是我们之前创建的。在这里面我们来看一下我们在我们实现一个接口，有一个叫做 web MVC config，它是一个接口。在这里面包含了很多的内容。其中我们来搜一下，有一个叫做 add resource handlers。看一下，从字面意义上去看是添加资源的助手，它是为我们的一些静态资源做辅助的。在这边它会有一段注释。来看一下，它会为我们当前的一些静态资源。这些静态资源比方有图片，JS，CSS，还有一些文件，它会为它们去添加一些相应的助手。


from 是从哪里来？这些文件的地址是在我们的 location 发布到哪里，会发布到 web application roots，也就是发布到我们的一个 web 应用。下巴。发布了以后，我们就可以以一个 web 服务的形式去进行访问了，所以它就可以为我们提供这样的一种帮助。OK，所以我们要去把这个去实现一下。在我们当前这个方法里面就可以去进行一个实现了。我们可以来这样子，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/12101a0d-5ae4-46b6-a48c-4c638569286b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHVD73OL%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224726Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDC7iTC06Gz6jYU6kiq9vnPIEQptMXPMUL57y1LCAeeVQIgPX6GV860oVxp1xYMaEI%2BXA%2FZSwdIp93shjPkK%2BgXNbkqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHx97TMHh9QzI3qLTircA5Nm2KT3cRjP0f%2BnxLP4b5jaZlUnTkN1uc4kQVLvzL950e7yTXLWVAmDcvIWNBQH04zdsPBWLy9sGbSuxQ2VxQhF7wIfBpBO45MfSAKeIrgNroOg7%2B2UKAtahMQlBAV3LRJOwDn%2BZ3zLQfNSiJJEXwGjOzr76AJnoVKzHfE5H2lfM5xxshjyxx5MoDyjdalk5Xikf7J8fSv3DG05F2Zmz9hKTFinJH4FElgfapg4KPoEM2NVl%2B7Atqaa%2B2rw05ZIRH1fjw%2BsgprpQegn0KAVbzQ5fbEXitThTiSvNmRIyXcHmKHfO4Si6WLV0DBUvrWzi%2BCcQ0NIVslrKrelV6T1cwAEsYNr8q0emMNDGBJHX06f%2BTI9DS2GQdSkBOn6QUtw0%2FsoWZEM6Ekg6sxxE1TTrkGXCZKA8WAZ%2FvR%2B5Nt7EQdN1m417WwNaXGjMjBD5VNLrLOHxRl0zmqxBZ1a8uqimgUGuC3kgwxqj5MMEWLGn%2FgXcz1u9VvihOoI1dH6asVf16NVs7o7yHDLPGvsHxIUwLmq%2FbWRlcnoMSzoYlYvu0%2Fia8gIcHBbKxRzy6QLxs7I9RJ9ltkD23ap%2FLs5bnpIF%2F1aGMeJBylP2FtvpYbs87UiMCLU8pmEK%2B9gy01VMMG3%2F9IGOqUBjLUtahIb5jOv0LYe5EbNjl3IR1W3zNdOun0E2q%2FxXCyquNdw5GbKlH2uHy%2BmnHRRTy9Mgkjp80PfE%2B0UKKArvoeHQqMKEo%2FFPTrWdQX%2FepnjgXlXXm%2FjbTmyW%2FgYy6Jas%2FvHXM0mzIaEhPXzZSyeEowsmoeg6hl%2BIhSXEhHhJf0QgFOhrG9seMK31lQ5cMFiwG3GDOhhJv3kEutvujjcZMh4Z%2FI7&X-Amz-Signature=ff21c03d1845ebf1c5bf2301239c881871dbf1d0ff47bf9cc28107a89ddef2a0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

通过 code 有一个generate，放大一下，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/0e3bc5c0-d31a-4f51-beac-177bed546f69/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHVD73OL%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224726Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDC7iTC06Gz6jYU6kiq9vnPIEQptMXPMUL57y1LCAeeVQIgPX6GV860oVxp1xYMaEI%2BXA%2FZSwdIp93shjPkK%2BgXNbkqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHx97TMHh9QzI3qLTircA5Nm2KT3cRjP0f%2BnxLP4b5jaZlUnTkN1uc4kQVLvzL950e7yTXLWVAmDcvIWNBQH04zdsPBWLy9sGbSuxQ2VxQhF7wIfBpBO45MfSAKeIrgNroOg7%2B2UKAtahMQlBAV3LRJOwDn%2BZ3zLQfNSiJJEXwGjOzr76AJnoVKzHfE5H2lfM5xxshjyxx5MoDyjdalk5Xikf7J8fSv3DG05F2Zmz9hKTFinJH4FElgfapg4KPoEM2NVl%2B7Atqaa%2B2rw05ZIRH1fjw%2BsgprpQegn0KAVbzQ5fbEXitThTiSvNmRIyXcHmKHfO4Si6WLV0DBUvrWzi%2BCcQ0NIVslrKrelV6T1cwAEsYNr8q0emMNDGBJHX06f%2BTI9DS2GQdSkBOn6QUtw0%2FsoWZEM6Ekg6sxxE1TTrkGXCZKA8WAZ%2FvR%2B5Nt7EQdN1m417WwNaXGjMjBD5VNLrLOHxRl0zmqxBZ1a8uqimgUGuC3kgwxqj5MMEWLGn%2FgXcz1u9VvihOoI1dH6asVf16NVs7o7yHDLPGvsHxIUwLmq%2FbWRlcnoMSzoYlYvu0%2Fia8gIcHBbKxRzy6QLxs7I9RJ9ltkD23ap%2FLs5bnpIF%2F1aGMeJBylP2FtvpYbs87UiMCLU8pmEK%2B9gy01VMMG3%2F9IGOqUBjLUtahIb5jOv0LYe5EbNjl3IR1W3zNdOun0E2q%2FxXCyquNdw5GbKlH2uHy%2BmnHRRTy9Mgkjp80PfE%2B0UKKArvoeHQqMKEo%2FFPTrWdQX%2FepnjgXlXXm%2FjbTmyW%2FgYy6Jas%2FvHXM0mzIaEhPXzZSyeEowsmoeg6hl%2BIhSXEhHhJf0QgFOhrG9seMK31lQ5cMFiwG3GDOhhJv3kEutvujjcZMh4Z%2FI7&X-Amz-Signature=3919b93355736d8ff3a59c697d3a263e52cf620e4585e4aa3fe491f03cfbe983&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

在这里 generate 或者你可以使用一下快捷键，也可以点击了。以后在这边会有一个 implement message，也就是去实现它的一些接口。在这边我们可以去选择找一下 add resource，双击一下。好，这个方法就会为我们添加，并且让我们去实现。我们可以加一个注释，实现静态资源的映射。其中这就是一个注册。我们把一些相应的地址进行一个注册就可以了。通过 registry 可以点它有一个 add resource handle 了。在这里它会有一个 pass patterns，也就是一个映射的一个路径地址。在这边我们通过直接写上一个斜杠星星就可以了。它是映射所有的一个资源的。在下方就可以去添加你的地址了，点 add。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/9a91314a-e9d5-442a-9d6f-edf47787b027/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHVD73OL%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224726Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDC7iTC06Gz6jYU6kiq9vnPIEQptMXPMUL57y1LCAeeVQIgPX6GV860oVxp1xYMaEI%2BXA%2FZSwdIp93shjPkK%2BgXNbkqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHx97TMHh9QzI3qLTircA5Nm2KT3cRjP0f%2BnxLP4b5jaZlUnTkN1uc4kQVLvzL950e7yTXLWVAmDcvIWNBQH04zdsPBWLy9sGbSuxQ2VxQhF7wIfBpBO45MfSAKeIrgNroOg7%2B2UKAtahMQlBAV3LRJOwDn%2BZ3zLQfNSiJJEXwGjOzr76AJnoVKzHfE5H2lfM5xxshjyxx5MoDyjdalk5Xikf7J8fSv3DG05F2Zmz9hKTFinJH4FElgfapg4KPoEM2NVl%2B7Atqaa%2B2rw05ZIRH1fjw%2BsgprpQegn0KAVbzQ5fbEXitThTiSvNmRIyXcHmKHfO4Si6WLV0DBUvrWzi%2BCcQ0NIVslrKrelV6T1cwAEsYNr8q0emMNDGBJHX06f%2BTI9DS2GQdSkBOn6QUtw0%2FsoWZEM6Ekg6sxxE1TTrkGXCZKA8WAZ%2FvR%2B5Nt7EQdN1m417WwNaXGjMjBD5VNLrLOHxRl0zmqxBZ1a8uqimgUGuC3kgwxqj5MMEWLGn%2FgXcz1u9VvihOoI1dH6asVf16NVs7o7yHDLPGvsHxIUwLmq%2FbWRlcnoMSzoYlYvu0%2Fia8gIcHBbKxRzy6QLxs7I9RJ9ltkD23ap%2FLs5bnpIF%2F1aGMeJBylP2FtvpYbs87UiMCLU8pmEK%2B9gy01VMMG3%2F9IGOqUBjLUtahIb5jOv0LYe5EbNjl3IR1W3zNdOun0E2q%2FxXCyquNdw5GbKlH2uHy%2BmnHRRTy9Mgkjp80PfE%2B0UKKArvoeHQqMKEo%2FFPTrWdQX%2FepnjgXlXXm%2FjbTmyW%2FgYy6Jas%2FvHXM0mzIaEhPXzZSyeEowsmoeg6hl%2BIhSXEhHhJf0QgFOhrG9seMK31lQ5cMFiwG3GDOhhJv3kEutvujjcZMh4Z%2FI7&X-Amz-Signature=4e08ae96c63242d8de4122bd8a3a615ad4a56aacbab518c13fb29e728d1c1d38&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

首先第这是一个 location 是吧？你所有的一些内容。在这个里面你可以传入一个的单个string。可以看到这是三个点，代表它可以传入一个数组。或者你是单个的一个 string 也是可以的。在这里我们就可以去做一个添加了。添加由于我们的一个内容是在我们本地的操作系统里面所存在的某一个目录，所以在这边我们应该写上一个file，这是一个固定的写法， file 冒号。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/c79856d9-3d11-4e1b-9d44-b2c31564a364/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHVD73OL%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224726Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDC7iTC06Gz6jYU6kiq9vnPIEQptMXPMUL57y1LCAeeVQIgPX6GV860oVxp1xYMaEI%2BXA%2FZSwdIp93shjPkK%2BgXNbkqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHx97TMHh9QzI3qLTircA5Nm2KT3cRjP0f%2BnxLP4b5jaZlUnTkN1uc4kQVLvzL950e7yTXLWVAmDcvIWNBQH04zdsPBWLy9sGbSuxQ2VxQhF7wIfBpBO45MfSAKeIrgNroOg7%2B2UKAtahMQlBAV3LRJOwDn%2BZ3zLQfNSiJJEXwGjOzr76AJnoVKzHfE5H2lfM5xxshjyxx5MoDyjdalk5Xikf7J8fSv3DG05F2Zmz9hKTFinJH4FElgfapg4KPoEM2NVl%2B7Atqaa%2B2rw05ZIRH1fjw%2BsgprpQegn0KAVbzQ5fbEXitThTiSvNmRIyXcHmKHfO4Si6WLV0DBUvrWzi%2BCcQ0NIVslrKrelV6T1cwAEsYNr8q0emMNDGBJHX06f%2BTI9DS2GQdSkBOn6QUtw0%2FsoWZEM6Ekg6sxxE1TTrkGXCZKA8WAZ%2FvR%2B5Nt7EQdN1m417WwNaXGjMjBD5VNLrLOHxRl0zmqxBZ1a8uqimgUGuC3kgwxqj5MMEWLGn%2FgXcz1u9VvihOoI1dH6asVf16NVs7o7yHDLPGvsHxIUwLmq%2FbWRlcnoMSzoYlYvu0%2Fia8gIcHBbKxRzy6QLxs7I9RJ9ltkD23ap%2FLs5bnpIF%2F1aGMeJBylP2FtvpYbs87UiMCLU8pmEK%2B9gy01VMMG3%2F9IGOqUBjLUtahIb5jOv0LYe5EbNjl3IR1W3zNdOun0E2q%2FxXCyquNdw5GbKlH2uHy%2BmnHRRTy9Mgkjp80PfE%2B0UKKArvoeHQqMKEo%2FFPTrWdQX%2FepnjgXlXXm%2FjbTmyW%2FgYy6Jas%2FvHXM0mzIaEhPXzZSyeEowsmoeg6hl%2BIhSXEhHhJf0QgFOhrG9seMK31lQ5cMFiwG3GDOhhJv3kEutvujjcZMh4Z%2FI7&X-Amz-Signature=66ab31c929d0deaf39226096d48eccc6fcbbea20c7a921356a441db4ebc9cfa1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

斜杠后方就是你所要去映射的一个地址。这个地址我们来看一下。我们目前要去映射，我们映射到我们可以映射到fooding，或者我们映射到这里，映射到 images 之下，也就是把这个 images 我们做一个映射，拷贝一下，写过来。也就是在 workspace 再来一个image，映射到这里就行了。因为后面的一些参数我们是可以通过字符串拼接去进行访问的就可以了。在这个后方其实也能再去加上一个斜杠，可以加上一个注释，这是映射本地静态资源去进行一个映射。映射完毕之后， images 下方所有的一些内容我们都可以去访问到。好，现在我们就可以去进行一个重启。好，重启成功之后，我们打开浏览器，在浏览器里面我们在这边写一下，在这边我们就可以直接通过访问。80，应该是 8088 对吧。


斜杠我们的映射资源的地址，现在我们是映射到了 image 的下方，所以在后面我们只需要加上 image 下方的一些内容，我们是映射到哪里，就从哪个目录下去进行一个设置，在这里写上一个foodie。在斜杠再加上它的一个目录名称。忘记了，重新再来看一下。


其实应该是从负底网上面一直一步一步的去写，直接写这个地址就可以了。我们把这个地址直接拷贝它的路径拷贝一下贴过来，在我们做一个精简。这样子就其实是 OK 了。也就是从 foodie 到faces，再到我们的一个 user ID，再到我们的一个图片，我们可以来一个 enter 回车看一下。当我们按回收了以后，这张图片就可以在我们的浏览器里面访问到了。OK。这个其实就是一个静态资源文件的映射，一定要注意它的一个开头。这个开头 fully 是从我们映射文件的下一个子目录开始的，也就是从 image 下方去进行一个访问的。因为这一段路径是被映射了。


映射完了之后是可以通过我们的一个location，也就是我们的一个服务器的域名，现在我们还没有域名，如果有域名是通过域名谁让 food 去访问？现在我们没有域名，通过 location 冒号 8088 去进行访问的。OK，大家在课后可以去根据这样的一种方式去实现一下就 OK 了。

我们可以再来看一下我们的 smart two，这是我们 swag two 的一个地址，来看一下。刷新一下以后你会发现他会访问是404。主要是因为其实 swag two 它所有的接口，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/c0a6d098-fb9f-4892-a55a-93f56a2b75b6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHVD73OL%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224726Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDC7iTC06Gz6jYU6kiq9vnPIEQptMXPMUL57y1LCAeeVQIgPX6GV860oVxp1xYMaEI%2BXA%2FZSwdIp93shjPkK%2BgXNbkqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDHx97TMHh9QzI3qLTircA5Nm2KT3cRjP0f%2BnxLP4b5jaZlUnTkN1uc4kQVLvzL950e7yTXLWVAmDcvIWNBQH04zdsPBWLy9sGbSuxQ2VxQhF7wIfBpBO45MfSAKeIrgNroOg7%2B2UKAtahMQlBAV3LRJOwDn%2BZ3zLQfNSiJJEXwGjOzr76AJnoVKzHfE5H2lfM5xxshjyxx5MoDyjdalk5Xikf7J8fSv3DG05F2Zmz9hKTFinJH4FElgfapg4KPoEM2NVl%2B7Atqaa%2B2rw05ZIRH1fjw%2BsgprpQegn0KAVbzQ5fbEXitThTiSvNmRIyXcHmKHfO4Si6WLV0DBUvrWzi%2BCcQ0NIVslrKrelV6T1cwAEsYNr8q0emMNDGBJHX06f%2BTI9DS2GQdSkBOn6QUtw0%2FsoWZEM6Ekg6sxxE1TTrkGXCZKA8WAZ%2FvR%2B5Nt7EQdN1m417WwNaXGjMjBD5VNLrLOHxRl0zmqxBZ1a8uqimgUGuC3kgwxqj5MMEWLGn%2FgXcz1u9VvihOoI1dH6asVf16NVs7o7yHDLPGvsHxIUwLmq%2FbWRlcnoMSzoYlYvu0%2Fia8gIcHBbKxRzy6QLxs7I9RJ9ltkD23ap%2FLs5bnpIF%2F1aGMeJBylP2FtvpYbs87UiMCLU8pmEK%2B9gy01VMMG3%2F9IGOqUBjLUtahIb5jOv0LYe5EbNjl3IR1W3zNdOun0E2q%2FxXCyquNdw5GbKlH2uHy%2BmnHRRTy9Mgkjp80PfE%2B0UKKArvoeHQqMKEo%2FFPTrWdQX%2FepnjgXlXXm%2FjbTmyW%2FgYy6Jas%2FvHXM0mzIaEhPXzZSyeEowsmoeg6hl%2BIhSXEhHhJf0QgFOhrG9seMK31lQ5cMFiwG3GDOhhJv3kEutvujjcZMh4Z%2FI7&X-Amz-Signature=806e650cc332b4a71f6b5eb6cbad07dc60ce4740f35e5e573be53d960fdd35e6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

它的文档，它生成之后，它其实也是一个的HTML。这种静态页面。由于我们现在是配置了一个静态资源的映射，但是我们却没有为 spark to 去进行配置，所以它才会出现这种问情况。我们之前没有配置的情况下，它默认是会帮我们去做到映射的。所以在这里我们应该要重新的为 step two 相关的一些文件去映射一下。OK，好，所以我们可以回到我们的配置内。


在这里我们可以再来添加一个 swag two。它所有的一个地址，它其实是映射到哈斯 pass 之下的形象 plus pass 冒号。这个地址我就直接去写了。它是在 Meta info 之下的，它会有一个resources，它会放在目录之下的。大家注意一下。后面还是一样。我加上一个。我加上一个注释映射， swag two。好，我们再来重启一下。好，重启成功。


重启成功之后，我们到页面里面，我们重新去刷新一下。刷新以后你会发现我们的 swag two 接口，我们又可以重新的去访问了。另外我们的图片刷新一下也没有问题，OK？至于这两个不同的精彩资源，一个是页面，其实页面它间接的就包含了 JS 以及是CSS。另外对于我们的一个图片也已经是映射， OK 了。

```java
package com.imooc.config;

import org.springframework.boot.web.client.RestTemplateBuilder;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.client.RestTemplate;
import org.springframework.web.servlet.config.annotation.ResourceHandlerRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

/**
 * <h1>构建一个restTemplate让订单创建接口发送MerchantOrderBO数据传输给订单支付系统</h1>
 */
@SuppressWarnings("all")
@Configuration
public class WebMvcConfig implements WebMvcConfigurer {


    /**
     * implements WebMvcConfigure 实现 WebMvcConfigure 用来做静态资源的网络映射
     */
    @Override
    public void addResourceHandlers(ResourceHandlerRegistry registry) {
        registry.addResourceHandler("/**")
                .addResourceLocations("classpath:/META-INF/resources/") // swagger2的接口文档是静态资源，所以我们需要为他做静态资源网页映射
                .addResourceLocations("file:/Users/guojun/workspaces/workspace/review-base-java/mac-foodie/foodie-dev-image/"); // 映射本地静态资源
    }

    @Bean
    public RestTemplate restTemplate(RestTemplateBuilder builder) {
        return builder.build();
    }

}
```


---
title: 1-4 用户中心 - 使用Hibernate验证用户信息
---

# 1-4 用户中心 - 使用Hibernate验证用户信息

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/ee2904df-8551-4fdb-853a-5d5291221e28/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663X3TTKKI%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224723Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD9gaqAaUrHR7nn%2BYEGkE2yjWHvePRQMlGGokb6TOSzMQIgVczDoldEGGzRVOoDv3xkqSHH0g6HVA60WoeOnoFzMnAqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ7F%2BMRpHzboroMCJSrcA9s9AmyNj0ZTdFnsU9OXLQkPWOa2L23xGeFi0Sx5arHv%2BFhGecMmY4Wy07qfYUBKxd77aJaKIdgYm8ulO87Xyl0i87xAP7rpTNXYt6MU1NZzF%2FC9FEP7xMutMZVXVLlmbLvF9y4kRqT%2FWlnBCpjSNw3TZxIIm5phvn%2FOv4R6S90EFgJXjRpFjqzZg5rBi0cAl1k2ycbCK0IXltpPEfp0%2BBWgkvZwai1zKIqKj1rCpJZ4fs1nQQhomejpD4UuIusgf0CBjGqp1zUXR5ekMf4uvLdPK0GE1cpgl3XoNAkmrZCsDhlJynWNUH6ywcjf2tHiuORKzmSB2Lj%2FE2eUdWOA4Tk3Kt%2FczqPSRKcjoo4YmB6%2FiRhfLd4zRLTtyt3ppb1fehWq7GZrbhugigFJUt%2BJ92duDONTTmXgwPYTRFvs5LvS4M%2BWJApzbObjDpJQFzQd%2FPXKmMnZjPPybESsvyyOnQKwje0%2FixjJOOAwOxGHvjZqbghQ0c0Wlz8dP4QuCv3sJL5lh0%2FYpZb6GZoZ1X7O8QsSVFXHlti5Fx6hdi6MOjsKBQ%2FPyhezHXZu7zlFAaTLFVp6fGNsLBn0%2B4tPsi7srELnXV61Ov5sCfvVcTFYy%2FUAZAv%2Ba8CUreKH6xONMN23%2F9IGOqUBsozCjlHz%2BPSvjUu6kfRV8sAmpCUEmMuQae0ZtUSmcfo1oZCY0z5qZEfCy9qRdBRlQyaSiw12zTF3nCVk336RrF%2F5L8iobTV7RVD6iITZXqD7kBI5xeaKLcdDO%2BRgTJJTpsEbv7ZSTa99sVOI9Vg9oq40hrOR05I7d0pMeytgNROI3fuGGZ9oSdux9yYVP1mSBhf%2Fv9qVDjBZ%2FXf1uS3GNe%2BOcLIe&X-Amz-Signature=6babe83fb8847af3fe613dbf8bc7bf04083a5c8c750dd084a54988ce19b28a3e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

上节我们是完成了用户信息的修改，它本身在前端我们就包含了一些验证，这个是写在前端的。其实不仅是在前端要有这些验证，在我们的后端其实也应该有，但是我们后端暂时先没有写。如果按照之前在天天吃货门户端所对应的后台接口里面，我们可能会在这里把 Bo 里面一些属性参数都拿出来一个去做验证，做判断。如果判断某一个字段有错有问题，我们就可以 return 一个。


error message。四种方式在这里其实会不太好，因为我们在这里 UserBO 里面所涉及到的属性实在是太多了。在我们这里去一个做判断，做验证，它的一个代码量会相当的多，而且有一部分都是一些重复性的代码，所以在这里我们不使用这种方式。在我们的项目里面，其实在最一开始我们的一个 POM 里面，我们依赖了一些价包，遇见了以后，它其实就包含了一个 Hibernate，它所带有的一个验证器，我们可以来先看一下。先来看一下我们所有的libraries，在这里面我们可以往下面去找一下。找一个 Hibernate ，可以看到会有一个 Hibernate validator ，这个是从哪里来的，其实我们没有主动的去引入。我们来看一下。我们打开聚合工程的Pom，把文件双击一下打开，我们在这个文件里面可以右键，右键 maven show dependencies。点一下以后会出来一张所有的依赖的

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/06274050-65ff-4d90-b418-17e1f91fa3ea/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663X3TTKKI%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224723Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD9gaqAaUrHR7nn%2BYEGkE2yjWHvePRQMlGGokb6TOSzMQIgVczDoldEGGzRVOoDv3xkqSHH0g6HVA60WoeOnoFzMnAqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ7F%2BMRpHzboroMCJSrcA9s9AmyNj0ZTdFnsU9OXLQkPWOa2L23xGeFi0Sx5arHv%2BFhGecMmY4Wy07qfYUBKxd77aJaKIdgYm8ulO87Xyl0i87xAP7rpTNXYt6MU1NZzF%2FC9FEP7xMutMZVXVLlmbLvF9y4kRqT%2FWlnBCpjSNw3TZxIIm5phvn%2FOv4R6S90EFgJXjRpFjqzZg5rBi0cAl1k2ycbCK0IXltpPEfp0%2BBWgkvZwai1zKIqKj1rCpJZ4fs1nQQhomejpD4UuIusgf0CBjGqp1zUXR5ekMf4uvLdPK0GE1cpgl3XoNAkmrZCsDhlJynWNUH6ywcjf2tHiuORKzmSB2Lj%2FE2eUdWOA4Tk3Kt%2FczqPSRKcjoo4YmB6%2FiRhfLd4zRLTtyt3ppb1fehWq7GZrbhugigFJUt%2BJ92duDONTTmXgwPYTRFvs5LvS4M%2BWJApzbObjDpJQFzQd%2FPXKmMnZjPPybESsvyyOnQKwje0%2FixjJOOAwOxGHvjZqbghQ0c0Wlz8dP4QuCv3sJL5lh0%2FYpZb6GZoZ1X7O8QsSVFXHlti5Fx6hdi6MOjsKBQ%2FPyhezHXZu7zlFAaTLFVp6fGNsLBn0%2B4tPsi7srELnXV61Ov5sCfvVcTFYy%2FUAZAv%2Ba8CUreKH6xONMN23%2F9IGOqUBsozCjlHz%2BPSvjUu6kfRV8sAmpCUEmMuQae0ZtUSmcfo1oZCY0z5qZEfCy9qRdBRlQyaSiw12zTF3nCVk336RrF%2F5L8iobTV7RVD6iITZXqD7kBI5xeaKLcdDO%2BRgTJJTpsEbv7ZSTa99sVOI9Vg9oq40hrOR05I7d0pMeytgNROI3fuGGZ9oSdux9yYVP1mSBhf%2Fv9qVDjBZ%2FXf1uS3GNe%2BOcLIe&X-Amz-Signature=50593fb87f93cc2c48d85e7b260baf68df4b673eb125e408a8a4eae58375fef8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/016d6189-cffb-4d3e-a18c-46323d6a3954/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663X3TTKKI%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224723Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD9gaqAaUrHR7nn%2BYEGkE2yjWHvePRQMlGGokb6TOSzMQIgVczDoldEGGzRVOoDv3xkqSHH0g6HVA60WoeOnoFzMnAqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ7F%2BMRpHzboroMCJSrcA9s9AmyNj0ZTdFnsU9OXLQkPWOa2L23xGeFi0Sx5arHv%2BFhGecMmY4Wy07qfYUBKxd77aJaKIdgYm8ulO87Xyl0i87xAP7rpTNXYt6MU1NZzF%2FC9FEP7xMutMZVXVLlmbLvF9y4kRqT%2FWlnBCpjSNw3TZxIIm5phvn%2FOv4R6S90EFgJXjRpFjqzZg5rBi0cAl1k2ycbCK0IXltpPEfp0%2BBWgkvZwai1zKIqKj1rCpJZ4fs1nQQhomejpD4UuIusgf0CBjGqp1zUXR5ekMf4uvLdPK0GE1cpgl3XoNAkmrZCsDhlJynWNUH6ywcjf2tHiuORKzmSB2Lj%2FE2eUdWOA4Tk3Kt%2FczqPSRKcjoo4YmB6%2FiRhfLd4zRLTtyt3ppb1fehWq7GZrbhugigFJUt%2BJ92duDONTTmXgwPYTRFvs5LvS4M%2BWJApzbObjDpJQFzQd%2FPXKmMnZjPPybESsvyyOnQKwje0%2FixjJOOAwOxGHvjZqbghQ0c0Wlz8dP4QuCv3sJL5lh0%2FYpZb6GZoZ1X7O8QsSVFXHlti5Fx6hdi6MOjsKBQ%2FPyhezHXZu7zlFAaTLFVp6fGNsLBn0%2B4tPsi7srELnXV61Ov5sCfvVcTFYy%2FUAZAv%2Ba8CUreKH6xONMN23%2F9IGOqUBsozCjlHz%2BPSvjUu6kfRV8sAmpCUEmMuQae0ZtUSmcfo1oZCY0z5qZEfCy9qRdBRlQyaSiw12zTF3nCVk336RrF%2F5L8iobTV7RVD6iITZXqD7kBI5xeaKLcdDO%2BRgTJJTpsEbv7ZSTa99sVOI9Vg9oq40hrOR05I7d0pMeytgNROI3fuGGZ9oSdux9yYVP1mSBhf%2Fv9qVDjBZ%2FXf1uS3GNe%2BOcLIe&X-Amz-Signature=b4dbce4cf3f1b9a076fce47f07cabe7dcb9d2464afdf22bb4acb9e9e394973c3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


其实我们在之前其实是讲日志的时候有看过，也是这样子去看的。我们在这里可以放大一下，放大一下，放大一下以后我们可以来看。在这里我们有一个 Foodie-dev ，这是我们的一个聚合工程，也就是我们的项目名称。在这里其实我们就可以来看了。往这边来看一下。在这边可以看到有一个 cabinet Validata 在这个地方，在这里它其实是基于某一个依赖的。我们来看下面的一条线，这一条线其实从这里往这边一直倒退，这条线我们可以一起看。在这里其实你会发现它是从我们的 spring boot web 模块里面来的，我们只要把 web 模块依赖了，它也就会帮我们把 Hibernate 它的验证器给依赖进来，所以我们在咱们的项目里面可以使用它的一个验证规则。如何去使用？我们来看一下。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/f5ac3bd1-f87d-4ba1-a694-7ed6ac2c2faf/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663X3TTKKI%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224723Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD9gaqAaUrHR7nn%2BYEGkE2yjWHvePRQMlGGokb6TOSzMQIgVczDoldEGGzRVOoDv3xkqSHH0g6HVA60WoeOnoFzMnAqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ7F%2BMRpHzboroMCJSrcA9s9AmyNj0ZTdFnsU9OXLQkPWOa2L23xGeFi0Sx5arHv%2BFhGecMmY4Wy07qfYUBKxd77aJaKIdgYm8ulO87Xyl0i87xAP7rpTNXYt6MU1NZzF%2FC9FEP7xMutMZVXVLlmbLvF9y4kRqT%2FWlnBCpjSNw3TZxIIm5phvn%2FOv4R6S90EFgJXjRpFjqzZg5rBi0cAl1k2ycbCK0IXltpPEfp0%2BBWgkvZwai1zKIqKj1rCpJZ4fs1nQQhomejpD4UuIusgf0CBjGqp1zUXR5ekMf4uvLdPK0GE1cpgl3XoNAkmrZCsDhlJynWNUH6ywcjf2tHiuORKzmSB2Lj%2FE2eUdWOA4Tk3Kt%2FczqPSRKcjoo4YmB6%2FiRhfLd4zRLTtyt3ppb1fehWq7GZrbhugigFJUt%2BJ92duDONTTmXgwPYTRFvs5LvS4M%2BWJApzbObjDpJQFzQd%2FPXKmMnZjPPybESsvyyOnQKwje0%2FixjJOOAwOxGHvjZqbghQ0c0Wlz8dP4QuCv3sJL5lh0%2FYpZb6GZoZ1X7O8QsSVFXHlti5Fx6hdi6MOjsKBQ%2FPyhezHXZu7zlFAaTLFVp6fGNsLBn0%2B4tPsi7srELnXV61Ov5sCfvVcTFYy%2FUAZAv%2Ba8CUreKH6xONMN23%2F9IGOqUBsozCjlHz%2BPSvjUu6kfRV8sAmpCUEmMuQae0ZtUSmcfo1oZCY0z5qZEfCy9qRdBRlQyaSiw12zTF3nCVk336RrF%2F5L8iobTV7RVD6iITZXqD7kBI5xeaKLcdDO%2BRgTJJTpsEbv7ZSTa99sVOI9Vg9oq40hrOR05I7d0pMeytgNROI3fuGGZ9oSdux9yYVP1mSBhf%2Fv9qVDjBZ%2FXf1uS3GNe%2BOcLIe&X-Amz-Signature=013abcad770af94e43cee67e5b424b7b41e408872dce77fcde668330e364f662&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

先打开 CenterUserBo，比方我们现在要针对昵称要去做一个相应的判断。我们可以这样子，比方昵称我们是必须要有值的，不能够为空。所以我们可以这样子。 @NotBlank，这个是代表属性的字段，我们要求它不能为空。如果为空，在这里我们可以加上一个message。 message 是什么意思？是指如果发生错误了，它所提示出来的一个消息是怎样的。写一下比方用户昵称不能为空。这样子我们就针对于尼克 name 做了一个判断。好，

我们可以再来详细一些。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/f4fcea06-e118-42b6-84f0-bf9fa7f608dc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663X3TTKKI%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224723Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD9gaqAaUrHR7nn%2BYEGkE2yjWHvePRQMlGGokb6TOSzMQIgVczDoldEGGzRVOoDv3xkqSHH0g6HVA60WoeOnoFzMnAqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ7F%2BMRpHzboroMCJSrcA9s9AmyNj0ZTdFnsU9OXLQkPWOa2L23xGeFi0Sx5arHv%2BFhGecMmY4Wy07qfYUBKxd77aJaKIdgYm8ulO87Xyl0i87xAP7rpTNXYt6MU1NZzF%2FC9FEP7xMutMZVXVLlmbLvF9y4kRqT%2FWlnBCpjSNw3TZxIIm5phvn%2FOv4R6S90EFgJXjRpFjqzZg5rBi0cAl1k2ycbCK0IXltpPEfp0%2BBWgkvZwai1zKIqKj1rCpJZ4fs1nQQhomejpD4UuIusgf0CBjGqp1zUXR5ekMf4uvLdPK0GE1cpgl3XoNAkmrZCsDhlJynWNUH6ywcjf2tHiuORKzmSB2Lj%2FE2eUdWOA4Tk3Kt%2FczqPSRKcjoo4YmB6%2FiRhfLd4zRLTtyt3ppb1fehWq7GZrbhugigFJUt%2BJ92duDONTTmXgwPYTRFvs5LvS4M%2BWJApzbObjDpJQFzQd%2FPXKmMnZjPPybESsvyyOnQKwje0%2FixjJOOAwOxGHvjZqbghQ0c0Wlz8dP4QuCv3sJL5lh0%2FYpZb6GZoZ1X7O8QsSVFXHlti5Fx6hdi6MOjsKBQ%2FPyhezHXZu7zlFAaTLFVp6fGNsLBn0%2B4tPsi7srELnXV61Ov5sCfvVcTFYy%2FUAZAv%2Ba8CUreKH6xONMN23%2F9IGOqUBsozCjlHz%2BPSvjUu6kfRV8sAmpCUEmMuQae0ZtUSmcfo1oZCY0z5qZEfCy9qRdBRlQyaSiw12zTF3nCVk336RrF%2F5L8iobTV7RVD6iITZXqD7kBI5xeaKLcdDO%2BRgTJJTpsEbv7ZSTa99sVOI9Vg9oq40hrOR05I7d0pMeytgNROI3fuGGZ9oSdux9yYVP1mSBhf%2Fv9qVDjBZ%2FXf1uS3GNe%2BOcLIe&X-Amz-Signature=3d67aa5771287ba8f6fe02e3e63824fca7aea3e77ca0d8ef54f64076f10c7fd7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

对于用户昵称，其实我们在前端也能够看得出来。在前端做判断的时候，首先它不能够为空，另外它也不能够太长，不能超过 12 位。另外对于我们的真实姓名也不能够超过 12 位。所以我们可以在这里去加上一个 lens 这样的注解。加上以后在这里它会有一个Max， Max 就是它的一个最长的长度。我们写上一个 12 就可以了，如果超过12，它就会报相应的 message 错误。可以写一下用户昵称，不能超过 12 位。同理，我们可以把拷贝到下方，是真实性，把这里改成用户真实姓名不能超过 12 位。


在这里他报了一个错，有一个红色的波浪线， Max 等于12， Max 等于12。其实是指的长度，它是一个整形，是一个整数。所以在这里你需要把双引号给去掉，这样子他就不会报错了。OK，这样子其实我们就很快速的写了两个验证。好，我们往下面继续。下面是一个手机号，手机号它其实是对应了一个正则表达式。正则表达式如何去选？我们可以写它。有一个叫做part，在这里面有一个叫做有属性，这个属性就是代表正则表达式。正则表达是如何去写？我们可以看一下前端，在前端其实在验证手机有效性的时候，在有一个 check mobile，这个是在 APP 点 JS 里面的，也就是这一段内容，它本身就包含了一段正则表达式，所以只需要把中间这一段表达式的内容拷贝一下就可以了。它的两端的斜杠不要拷贝，拷贝到我们后端的代码直接放到这个部位就可以了，拷贝过来，这样子它的一个正则表达式就已经是 OK 了。如果它不满足，正则表达式在后方，我们还是一样加上一个message，提示手机号格式不正确，OK。好，随后下面继续。


下方是一个邮箱地址，邮商地址，你可以使用自定义的一个验证规则，也是在我们的前端有可以使用 email 的一个格式。当然其实我们的后端也为我们提供了，可以来看一下它有一个 email 这样的注解，你使用这个注解就可以开启 email 的验证了，也是没有问题的。


好，随后再下一个。我们可以再来看一下性别，性别其实我们指明了它只能是012，要么是女，要么是男，要么是保密，你不可以去输入一些其他的，不可以是复数，不可以是超过2，也不能够是小数。另外它是一个整形，在这里如何去使用？我们可以加一个注解，来一个mean， mean 其实就是一个最小值，在这里我们最小值我们可以设置为0，如果在小于0，如果写了一个 0 以下的负数，我们就可以报一个错。性别选择不正确。好，除了一个最小值，还有一个最大值就是一个 Max value。在这里我们写上一个 2 就可以了。来一个 message 一样把拷贝一下，这样子我们的性别就 OK 了。其实现在我们已经是对于我们大多数大部分属性字段加上了一个验证的注解。随后其实我们就可以来测试一下我们的验证了，如何去针对这些内容去做验证的。信息的提示主要还是要回到咱们的 Ctrl 了。现在我们写了这些注解是不能够使用的。我们要在 center user Bo 前方我们加上一个。加一下这个就代表我要去做验证的意思。要去验证Bo。验证完了之后，它肯定会有一些错误的信息，也就是这里面所包含的一些message。这些 message 又放在哪里？它在下方，我们可以再加一个。


有一个叫做 bounding results。所有的一些错误信息其实都会在 result 里面的。好在这里我们就可以来做一个判断了。我们要判断 Bo 里面有没有错误，有没有错误，我们会从 result 里面去获取。写一下，写一个 result 点。有一个方法叫做 has Eris，它是指是否包含有错误，加个注释判断，帮你 result 是否包含错误的验证信息。如果有，则直接 return 就可以了。直接return，前端在接收到的时候就会包含它里面所提示的一些相应的错误消息了。OK，好，我们在下方。在这里下方我们写一个方法，这个方法专门是用于去处理这些错误的。


写一下，写一个 private 处理错误信息，我们就写一个map。一些错误信息我们都可以写在 map 里面，它是一个键值，对错误的一些属性我们是放在 key 里面。错误的一些消息 message 我们是放在 failure 里面。好，这是 return 的一个map。我们定一个方法，叫做 get Iris，传入进来的一个参数应该是 bounding results。把传进来在这个 result 里面，我们来看一下。


来看一下它会有一个 get failed errors。这是一个什么？它是一个 list 类型，它包含了很多的一个 failed error。 failed 其实就是代表它的一个 VO 中的某一个属性。如果有 2 个错误信息，这个 list 就会包含两个。OK，好，我们就可以来获取一下list。这是 failed error，定义一个名称叫做 error list。这个 list 包导入进来。好，拿到艾瑞尔 list 了。以后，在这里我们就可以去做一个 for 循环。做 for 循环。在这边写一下它是一个 failed error。从 error 里面我们就可以去拿一些相应的内容了，比方我们可以通过 error 去get，它有一个叫做failed，这个 failed 其实就是代表获得的某一个属性。加一下，这是发生验证错误所对应的某一个属性。在这里我们可以写一下 string error field。另外除了 fail 的以外，还会有相应的错误信息。错误信息在这里可以来看到，这里面有一个叫做 default 


message， message 就是错误的内容。加一下，这是验证错误的信息。好在前方我们可以定一下 string error message。拿到了以后，这两个内容其实我们就可以放到 map 里面去了，所以在外层我们可以来把 map 可以去声明一下，直接拷贝一个map，直接把它给遛出来，好在循环的过程中，只要发生错误，我们就一个一个的 map 点 put 就可以了。


第一个是 error field，第二个是 error message。OK，这样子 map 里面就有相应的错误内容了。最后我们直接把 map 给 return 出去就 OK 了。好在我们的前方。在这个地方就直接可以去调用 get 艾瑞斯，获得到的一些相应的参数内容。接收。我们也是以一个 map 去接收的。接收一下 era map。好在这里。只要进入到这个判断，就表示肯定有错误。既然有错误，我们就要在这里return。所以我们 return 一个 m result 点。需要注意。在这里面我们就不再会使用 error message 了，我们会使用到一个叫做 error map，双击一下，这个 error map 就是对应到我们现在所发生错误的map，它会包含很多的一些错误，它是一个错误集。好这样子，现在其实我们就已经是把这一段内容给做好了，我们验证都已经是 OK 了，我们可以去做一个测试了。在这里我们的 install 一下。


好， install 成功。随后我们再重启一下服务器。其实在我们前端它本身就包含了验证，对吧？所以我们在测试的时候，我们会使用 post man 来进行测试，因为 Postman 工具本身就非常不错，所以使用它来做测试也是没有问题的。在这里来看一下，我预先已经是把 post 方法。另外我们的 URL 已经是写好了， OK 参数这个是对应现在的一个 user 的ID。另外 body body 里面我传的是一个空的对象，空对象就是指我们现在在后端所接收到的读者，比如这里面的一些属性全部都是空值。所以我们就可以来做一个判断了。


OK，我们到前端，也就是在调用端在 postman 来点击 send 发送一下。这个时候来看一下发生了一个错误。这个错误就是一个 501 的错误。 501 是在我们后端所对应的一个 map 错误。看一下 error map，点进去看一下，如果发生错误，我们抛的就是一个501。其实我们在之前有提到过的，这边是501。 bin 看到是 b 验证错误。不管有多少错误，都以一个 map 的形式进行返回。好，继续。在这里我们就会返回一个nickname。用户昵称不能为空。 nickname 就是代表我们在之前定义 map 的时候所定义的一个failed。 OK message 就是错误信息。好，现在我们就已经是有了一个错误信息了。好，我们继续。在这里。现在我们就可以拿为它加上一个尼克name。尼克利姆加一下。比方，我们来取一个名字叫做慕课王。点击 send OK，可以看到现在我们是拿到的一个是成功的信息了。我们可以看一下数据库。来，我们刷新一下。刷新你会发现尼克利发生了一个更改了。好，我们继续下一个。我们来修改一下。


来看一下我们的 real name，真实姓名，真实姓名和 Nick name 它有一个共同的特点，就是它们的长度都不能够超过 12 位。所以我们在这里可以写一下。把 real name 属性拷贝到下方来。在这边我们就可以去写一下宇宙超级无敌在线教育网站。几个字246，八十十二，正好是 12 对吧。再加一个m。可我们来点击发送send。这个时候会报一个错，说 real name 出问题了，用户的真实姓名不能够超过 12 位。OK，这个错误好，现在已经是验证了。


好，再来看下一个是 mobile 手机号，拷贝一下，在下方。这个时候如果出现了一个错误，很显然，他在这个下方会以一个 map 的形式返回写一下。比方写一个123456，点击send。这个时候来看一下某贝尔手机号，格式不正确就已经是有了。在这里面它其实就是以一个对象的形式返还出来，它其实本身就是一个map，你可以把它看成是一个map，也可以把它看作是一个 JSON 对象，其实都是可以的。好，继续。下方是一个邮箱地址，里面邮箱地址我们在也可以这样子写，比方就写一个 a b c。好了。点击线的来看一下，里面这不是一个合法的电子邮箱地址，电子邮箱要合法，你是需要在它的后方一定要加上一个圈，比方 m . com，这个就是一个合格的邮箱的格式。


再点击 send 看一下，这个时候我们的email，它的验证格式就已经是通过了。OK，好。随后我们再下就是一个性别了。性别是012。这三个数字在我们前端在。其实也可以来写一下，sex，你写 0 来贬值 send 看一下，没有问题， 1 也没有问题， 2 也没有问题。这个时候我改成- 1 贬值线的，它会报错。性别选择不正确。如果是 3 超过 2 也是通过不了的。但是这个数字其实它会有一个小数点的问题。比方我们在这里写一个 2 点 92 点9，它是能够通过验证的。我们点一下，它是可以通过验证，但是你输入 2: 9，它会把 2 点 9 会当做是一个保密。因为我们在这里设置的是一个 Int 类型，只要是 Int 它，其实如果你在前端调用端传过来，是一个有带有小数点的小数，它会帮你强制转换成一个 Int 类型的，所以我们可以在这里我们可以来看一下。比方我们在来一个打印，把 Bo 直接给打印一下，我们再重启一下服务器。这个目的我们主要是为了前端所传过来的小数，看一下是不是能够进行一个强制转换。好，我们使用成功了。点击线的现在是 2 点 9 传到我们后端接收的时候，这个时候你会发现在这里下方有一个sex，它就会帮我们转换成耗了，对吧？所以如果你停两点 9 存到我们数据库，对应的保密零点几和一点几都分别会对应是 0 合 1 的。


现在这样子，其实我们就已经是完成了一个验证了，大家其实也可以在我们的一个课程里面使用这种哈密的它的一个验证器，去验证一下我们的一些相应的属性，都可以去做到的，但是这些属性你是必须要放在我们的一个entity，也就是放到 bill 里面去做的一个验证。另外我也是提供了一份文档，这份文档也是从我以前写的一个博客里面所摘录过来的。在这里来看一下，这是一个验证的。


b，其实在这里面会包含很多的注解，刚刚我们所使用的一些注解，其实也是其中的一些，大家都可以去看一下，根据自己以后的一些需求，不同的需求使用不同的注解去使用就可以了。多去试试，多去看看。这是一个验证的。b，在下方会包含一些相应的属性，上方是一些比较常用的验证的方式，下方是一个使用方式，在有一个message，这个 message 我使用的是一个属性资源的一种模式，也是可以的。下方是一个验证的 Ctrl 了，这 Ctrl 也是我们刚刚写的。需要注意的是，你要去做验证，你就要在前方加上一个valid。另外 bounding result 也是要去加的，加了以后在这边要去进行一个判断，如果没有通过在这边相应的一些信息，我们是需要去返回到前端的。OK。

```java
package com.imooc.pojo.center;

import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Data;
import org.hibernate.validator.constraints.Length;

import javax.validation.constraints.*;
import java.util.Date;

/**
 * <h1></h1>
 */
@SuppressWarnings("all")
@Data
@ApiModel(value = "用户信息BO", description = "从客户端，由用户传入的数据封装到此BO对象中")
public class CenterUserBO {

 @ApiModelProperty(value = "用户名", name = "username", example = "imooc", required = true)
 private String username;
 @ApiModelProperty(value = "密码", name = "password", example = "123456", required = true)
 private String password;
 @ApiModelProperty(value = "确认密码", name = "confirmPassword", example = "123456", required = false)
 private String confirmPassword;

 /**   从spring-boot-starter-web中自动依赖进来的 Hibernate 的字段验证注解，可以直接使用它来限制字段是否需要传数值，因为很多地方需要验证属性值是否需要传递，存在很多冗余代码  */
 @NotBlank(message = "用户昵称不能为空")
 @Length(max = 12, message = "用户昵称长度不能超过12位")
 @ApiModelProperty(value = "用户昵称", name = "nickName", example = "杰森", required = false)
 private String nickName;

 @Length(max = 12, message = "用户昵称长度不能超过12位")
 @ApiModelProperty(value = "真实姓名", name = "realName", example = "杰森", required = false)
 private String realName;

 @Pattern( regexp = "^(((13[0-9]{1})|(15[0-9]{1})|(18[0-9]{1}))+\\d{8})$", message = "手机号格式不正确")
 @ApiModelProperty(value = "手机号", name = "mobile", example = "13999999999", required = false)
 private String mobile;

 @Email
 @ApiModelProperty(value = "邮箱", name = "email", example = "123456@imooc.com", required = false)
 private String email;

 @Min(value = 0, message = "性别显示不正确")
 @Max(value = 2, message = "性别显示不正确")
 @ApiModelProperty(value = "性别", name = "sex", example = "0：女 1：男 2：保密", required = false)
 private String sex;


 @ApiModelProperty(value = "生日", name = "birthday", example = "1990-01-01", required = false)
 private Date birthday;

}
```


[file](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/4557201c-91f5-4959-8b6f-18a435a64c14/1-5_%E5%9B%BE%E6%96%87%E8%8A%82.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663X3TTKKI%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224723Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD9gaqAaUrHR7nn%2BYEGkE2yjWHvePRQMlGGokb6TOSzMQIgVczDoldEGGzRVOoDv3xkqSHH0g6HVA60WoeOnoFzMnAqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ7F%2BMRpHzboroMCJSrcA9s9AmyNj0ZTdFnsU9OXLQkPWOa2L23xGeFi0Sx5arHv%2BFhGecMmY4Wy07qfYUBKxd77aJaKIdgYm8ulO87Xyl0i87xAP7rpTNXYt6MU1NZzF%2FC9FEP7xMutMZVXVLlmbLvF9y4kRqT%2FWlnBCpjSNw3TZxIIm5phvn%2FOv4R6S90EFgJXjRpFjqzZg5rBi0cAl1k2ycbCK0IXltpPEfp0%2BBWgkvZwai1zKIqKj1rCpJZ4fs1nQQhomejpD4UuIusgf0CBjGqp1zUXR5ekMf4uvLdPK0GE1cpgl3XoNAkmrZCsDhlJynWNUH6ywcjf2tHiuORKzmSB2Lj%2FE2eUdWOA4Tk3Kt%2FczqPSRKcjoo4YmB6%2FiRhfLd4zRLTtyt3ppb1fehWq7GZrbhugigFJUt%2BJ92duDONTTmXgwPYTRFvs5LvS4M%2BWJApzbObjDpJQFzQd%2FPXKmMnZjPPybESsvyyOnQKwje0%2FixjJOOAwOxGHvjZqbghQ0c0Wlz8dP4QuCv3sJL5lh0%2FYpZb6GZoZ1X7O8QsSVFXHlti5Fx6hdi6MOjsKBQ%2FPyhezHXZu7zlFAaTLFVp6fGNsLBn0%2B4tPsi7srELnXV61Ov5sCfvVcTFYy%2FUAZAv%2Ba8CUreKH6xONMN23%2F9IGOqUBsozCjlHz%2BPSvjUu6kfRV8sAmpCUEmMuQae0ZtUSmcfo1oZCY0z5qZEfCy9qRdBRlQyaSiw12zTF3nCVk336RrF%2F5L8iobTV7RVD6iITZXqD7kBI5xeaKLcdDO%2BRgTJJTpsEbv7ZSTa99sVOI9Vg9oq40hrOR05I7d0pMeytgNROI3fuGGZ9oSdux9yYVP1mSBhf%2Fv9qVDjBZ%2FXf1uS3GNe%2BOcLIe&X-Amz-Signature=ef7385e7d0a170edb8f3dc4b5251592553a3d7b5e95215e5ec124cab1bd94add&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/27d28241-4177-4047-8509-ee61ce8376cb/2020-09-17_205932.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663X3TTKKI%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224723Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQD9gaqAaUrHR7nn%2BYEGkE2yjWHvePRQMlGGokb6TOSzMQIgVczDoldEGGzRVOoDv3xkqSHH0g6HVA60WoeOnoFzMnAqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJ7F%2BMRpHzboroMCJSrcA9s9AmyNj0ZTdFnsU9OXLQkPWOa2L23xGeFi0Sx5arHv%2BFhGecMmY4Wy07qfYUBKxd77aJaKIdgYm8ulO87Xyl0i87xAP7rpTNXYt6MU1NZzF%2FC9FEP7xMutMZVXVLlmbLvF9y4kRqT%2FWlnBCpjSNw3TZxIIm5phvn%2FOv4R6S90EFgJXjRpFjqzZg5rBi0cAl1k2ycbCK0IXltpPEfp0%2BBWgkvZwai1zKIqKj1rCpJZ4fs1nQQhomejpD4UuIusgf0CBjGqp1zUXR5ekMf4uvLdPK0GE1cpgl3XoNAkmrZCsDhlJynWNUH6ywcjf2tHiuORKzmSB2Lj%2FE2eUdWOA4Tk3Kt%2FczqPSRKcjoo4YmB6%2FiRhfLd4zRLTtyt3ppb1fehWq7GZrbhugigFJUt%2BJ92duDONTTmXgwPYTRFvs5LvS4M%2BWJApzbObjDpJQFzQd%2FPXKmMnZjPPybESsvyyOnQKwje0%2FixjJOOAwOxGHvjZqbghQ0c0Wlz8dP4QuCv3sJL5lh0%2FYpZb6GZoZ1X7O8QsSVFXHlti5Fx6hdi6MOjsKBQ%2FPyhezHXZu7zlFAaTLFVp6fGNsLBn0%2B4tPsi7srELnXV61Ov5sCfvVcTFYy%2FUAZAv%2Ba8CUreKH6xONMN23%2F9IGOqUBsozCjlHz%2BPSvjUu6kfRV8sAmpCUEmMuQae0ZtUSmcfo1oZCY0z5qZEfCy9qRdBRlQyaSiw12zTF3nCVk336RrF%2F5L8iobTV7RVD6iITZXqD7kBI5xeaKLcdDO%2BRgTJJTpsEbv7ZSTa99sVOI9Vg9oq40hrOR05I7d0pMeytgNROI3fuGGZ9oSdux9yYVP1mSBhf%2Fv9qVDjBZ%2FXf1uS3GNe%2BOcLIe&X-Amz-Signature=854c02bd601143f7378dca263d0e91f75451a037477124a4d4a842d274d535b9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)




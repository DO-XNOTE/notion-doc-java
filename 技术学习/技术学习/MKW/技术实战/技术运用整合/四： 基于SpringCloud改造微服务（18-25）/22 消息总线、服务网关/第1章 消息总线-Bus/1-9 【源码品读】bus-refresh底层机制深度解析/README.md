---
title: 1-9 【源码品读】bus-refresh底层机制深度解析
---

# 1-9 【源码品读】bus-refresh底层机制深度解析


[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/da02f316-8dbc-4559-b355-8b084f2ef8e0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R6RBMZOL%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225726Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICKhLsZHnOI1wbfhu1orSlUA2HdNYstXSV1NpZv%2B4XRfAiAntHS569Nog9Vg4B0l2g0QI5FdlIEyE1ZMUFSoOVFfxCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMwMsWIOh4MMuStTiXKtwDR%2Bnhpakdu5bGxgb%2B8ZxMeqUF2%2FQIM8TQH7saXq9EPUWHW1zRrYWdDZxYQIobXTvEH%2FIO2n8FiMokyzqL30oMEAIyv14HDNEtzmlCvlQuqxLbOca4%2BvZZKp8ZHoJe2bCWs1QDuC%2Fe1Fkvf8V1fdxwyaJRvox8CxyEajzQs%2BrI%2B%2B1ce5jEcc9HR57Y2EcoNmAOOmrklZsFPt%2BOglMrcljTh1Qj1W43RrtsdEVlvVY60wzZDXOU0dcU31DeQ9dIpMtDhzUP6E7EQE7UNsn0QpxLiMhpXEuVxFhlRFP7IIH5TDjUR3R0OlqdUk0SRjhaawHutj%2BTFjUgeWpwZdOeLSYCmNxdaMXnJtWBt0kXACnk3zW8fpbWq4IkdFb5tN%2Fqj0itzb9C5%2FlCldVvQOjxV3y%2BsQ272QGe%2BkbsAXV%2BsmqZLMcUKyCZFxFlfJJolfP6rn1nkm9ItraQ5OWxv9EW7crcJBwKEL6kH7trI3BBdlS9eNMH2qzACps3pNUSVZbWrmjtmaaS3HtppPmLjBTv2EeUQ8exwCxm8IroCtbpxJ6Ovzd9EyLkZodnMZU5RNFNO9wVW20zrnmxQcy4l6g8sx5hdVGFVd1P%2FGAopYNeZzX6FHtJRrgUcevEpi8te%2FQwg7f%2F0gY6pgFkJ6GS1LuS%2BQa8pp41MRyfM4y2Kb2XqcIUPO1BsCOqJG9NNPMbZI7VOcMJ61C2j4fnebU9OX3DkDsjDMRCkdxTkYcmcZRaD8JBlIsP9iBpwhADATgcPZwFbdUmuOivhHxWxZkoiBLrO3V4OZzDybfX9TkmcD5hy2%2F4Io2jDW7dpdixzlFh4bo3WYdcLoZt841e20YANbKLUeou3Gb%2BH9sP8W9eRZHt&X-Amz-Signature=17a91c543483fe2eaea75230a11d04ebf7150b3d5dd5e8b4cf4c79444cf8b89e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/0609cf11-1dbc-4300-856e-1a700c1c5d5d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R6RBMZOL%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225726Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICKhLsZHnOI1wbfhu1orSlUA2HdNYstXSV1NpZv%2B4XRfAiAntHS569Nog9Vg4B0l2g0QI5FdlIEyE1ZMUFSoOVFfxCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMwMsWIOh4MMuStTiXKtwDR%2Bnhpakdu5bGxgb%2B8ZxMeqUF2%2FQIM8TQH7saXq9EPUWHW1zRrYWdDZxYQIobXTvEH%2FIO2n8FiMokyzqL30oMEAIyv14HDNEtzmlCvlQuqxLbOca4%2BvZZKp8ZHoJe2bCWs1QDuC%2Fe1Fkvf8V1fdxwyaJRvox8CxyEajzQs%2BrI%2B%2B1ce5jEcc9HR57Y2EcoNmAOOmrklZsFPt%2BOglMrcljTh1Qj1W43RrtsdEVlvVY60wzZDXOU0dcU31DeQ9dIpMtDhzUP6E7EQE7UNsn0QpxLiMhpXEuVxFhlRFP7IIH5TDjUR3R0OlqdUk0SRjhaawHutj%2BTFjUgeWpwZdOeLSYCmNxdaMXnJtWBt0kXACnk3zW8fpbWq4IkdFb5tN%2Fqj0itzb9C5%2FlCldVvQOjxV3y%2BsQ272QGe%2BkbsAXV%2BsmqZLMcUKyCZFxFlfJJolfP6rn1nkm9ItraQ5OWxv9EW7crcJBwKEL6kH7trI3BBdlS9eNMH2qzACps3pNUSVZbWrmjtmaaS3HtppPmLjBTv2EeUQ8exwCxm8IroCtbpxJ6Ovzd9EyLkZodnMZU5RNFNO9wVW20zrnmxQcy4l6g8sx5hdVGFVd1P%2FGAopYNeZzX6FHtJRrgUcevEpi8te%2FQwg7f%2F0gY6pgFkJ6GS1LuS%2BQa8pp41MRyfM4y2Kb2XqcIUPO1BsCOqJG9NNPMbZI7VOcMJ61C2j4fnebU9OX3DkDsjDMRCkdxTkYcmcZRaD8JBlIsP9iBpwhADATgcPZwFbdUmuOivhHxWxZkoiBLrO3V4OZzDybfX9TkmcD5hy2%2F4Io2jDW7dpdixzlFh4bo3WYdcLoZt841e20YANbKLUeou3Gb%2BH9sP8W9eRZHt&X-Amz-Signature=13f024a0461982cca61f35e03334b432fef0e0d9742748643ffe1b175f8c55d5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/be3336cc-4893-41aa-a524-3da7772ec3a5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R6RBMZOL%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225726Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICKhLsZHnOI1wbfhu1orSlUA2HdNYstXSV1NpZv%2B4XRfAiAntHS569Nog9Vg4B0l2g0QI5FdlIEyE1ZMUFSoOVFfxCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMwMsWIOh4MMuStTiXKtwDR%2Bnhpakdu5bGxgb%2B8ZxMeqUF2%2FQIM8TQH7saXq9EPUWHW1zRrYWdDZxYQIobXTvEH%2FIO2n8FiMokyzqL30oMEAIyv14HDNEtzmlCvlQuqxLbOca4%2BvZZKp8ZHoJe2bCWs1QDuC%2Fe1Fkvf8V1fdxwyaJRvox8CxyEajzQs%2BrI%2B%2B1ce5jEcc9HR57Y2EcoNmAOOmrklZsFPt%2BOglMrcljTh1Qj1W43RrtsdEVlvVY60wzZDXOU0dcU31DeQ9dIpMtDhzUP6E7EQE7UNsn0QpxLiMhpXEuVxFhlRFP7IIH5TDjUR3R0OlqdUk0SRjhaawHutj%2BTFjUgeWpwZdOeLSYCmNxdaMXnJtWBt0kXACnk3zW8fpbWq4IkdFb5tN%2Fqj0itzb9C5%2FlCldVvQOjxV3y%2BsQ272QGe%2BkbsAXV%2BsmqZLMcUKyCZFxFlfJJolfP6rn1nkm9ItraQ5OWxv9EW7crcJBwKEL6kH7trI3BBdlS9eNMH2qzACps3pNUSVZbWrmjtmaaS3HtppPmLjBTv2EeUQ8exwCxm8IroCtbpxJ6Ovzd9EyLkZodnMZU5RNFNO9wVW20zrnmxQcy4l6g8sx5hdVGFVd1P%2FGAopYNeZzX6FHtJRrgUcevEpi8te%2FQwg7f%2F0gY6pgFkJ6GS1LuS%2BQa8pp41MRyfM4y2Kb2XqcIUPO1BsCOqJG9NNPMbZI7VOcMJ61C2j4fnebU9OX3DkDsjDMRCkdxTkYcmcZRaD8JBlIsP9iBpwhADATgcPZwFbdUmuOivhHxWxZkoiBLrO3V4OZzDybfX9TkmcD5hy2%2F4Io2jDW7dpdixzlFh4bo3WYdcLoZt841e20YANbKLUeou3Gb%2BH9sP8W9eRZHt&X-Amz-Signature=a6bf7f0ce93ddb1c6dd059f6ee2c2a7436324280daaa825e142a27dba1bad7dd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/494671f5-48f7-47cc-9d77-7b6f9a51f213/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R6RBMZOL%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225726Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICKhLsZHnOI1wbfhu1orSlUA2HdNYstXSV1NpZv%2B4XRfAiAntHS569Nog9Vg4B0l2g0QI5FdlIEyE1ZMUFSoOVFfxCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMwMsWIOh4MMuStTiXKtwDR%2Bnhpakdu5bGxgb%2B8ZxMeqUF2%2FQIM8TQH7saXq9EPUWHW1zRrYWdDZxYQIobXTvEH%2FIO2n8FiMokyzqL30oMEAIyv14HDNEtzmlCvlQuqxLbOca4%2BvZZKp8ZHoJe2bCWs1QDuC%2Fe1Fkvf8V1fdxwyaJRvox8CxyEajzQs%2BrI%2B%2B1ce5jEcc9HR57Y2EcoNmAOOmrklZsFPt%2BOglMrcljTh1Qj1W43RrtsdEVlvVY60wzZDXOU0dcU31DeQ9dIpMtDhzUP6E7EQE7UNsn0QpxLiMhpXEuVxFhlRFP7IIH5TDjUR3R0OlqdUk0SRjhaawHutj%2BTFjUgeWpwZdOeLSYCmNxdaMXnJtWBt0kXACnk3zW8fpbWq4IkdFb5tN%2Fqj0itzb9C5%2FlCldVvQOjxV3y%2BsQ272QGe%2BkbsAXV%2BsmqZLMcUKyCZFxFlfJJolfP6rn1nkm9ItraQ5OWxv9EW7crcJBwKEL6kH7trI3BBdlS9eNMH2qzACps3pNUSVZbWrmjtmaaS3HtppPmLjBTv2EeUQ8exwCxm8IroCtbpxJ6Ovzd9EyLkZodnMZU5RNFNO9wVW20zrnmxQcy4l6g8sx5hdVGFVd1P%2FGAopYNeZzX6FHtJRrgUcevEpi8te%2FQwg7f%2F0gY6pgFkJ6GS1LuS%2BQa8pp41MRyfM4y2Kb2XqcIUPO1BsCOqJG9NNPMbZI7VOcMJ61C2j4fnebU9OX3DkDsjDMRCkdxTkYcmcZRaD8JBlIsP9iBpwhADATgcPZwFbdUmuOivhHxWxZkoiBLrO3V4OZzDybfX9TkmcD5hy2%2F4Io2jDW7dpdixzlFh4bo3WYdcLoZt841e20YANbKLUeou3Gb%2BH9sP8W9eRZHt&X-Amz-Signature=9e42598e56f851f176a332a4f63421db8212bedb375dfba147cf122b341ae2c6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

嗨慕课网的各位同学们，大家好，咱这里到了本章 bus 章节里为艺术源码阅读环节，咱读什么内容呢？这里主要有两个部分。第一部分我们看一下内置的事件结构，也就是 bus 组件，在推送批量刷新的时候，它会使用一个 refresh remote application event 我们来看一看这个事件它长什么样子。

看完了这个事件以后，咱要把整个流程给它梳理起来。所以接下来我们来看一下刷新事件的发送端，也就是 refresh bus and point 这一个 accurate 端点是如何发布一个事件的。当然了有发布自然会有接收。所以我们也要去看一下我们每个 client 服务端是如何消费这样一个消息的。 OK 同学们准备好的话跟我一起 debug 模式走起编程是我快乐 996 是我的福报。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/a9163de9-e911-435a-acca-b60b684ec4e6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R6RBMZOL%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225726Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICKhLsZHnOI1wbfhu1orSlUA2HdNYstXSV1NpZv%2B4XRfAiAntHS569Nog9Vg4B0l2g0QI5FdlIEyE1ZMUFSoOVFfxCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMwMsWIOh4MMuStTiXKtwDR%2Bnhpakdu5bGxgb%2B8ZxMeqUF2%2FQIM8TQH7saXq9EPUWHW1zRrYWdDZxYQIobXTvEH%2FIO2n8FiMokyzqL30oMEAIyv14HDNEtzmlCvlQuqxLbOca4%2BvZZKp8ZHoJe2bCWs1QDuC%2Fe1Fkvf8V1fdxwyaJRvox8CxyEajzQs%2BrI%2B%2B1ce5jEcc9HR57Y2EcoNmAOOmrklZsFPt%2BOglMrcljTh1Qj1W43RrtsdEVlvVY60wzZDXOU0dcU31DeQ9dIpMtDhzUP6E7EQE7UNsn0QpxLiMhpXEuVxFhlRFP7IIH5TDjUR3R0OlqdUk0SRjhaawHutj%2BTFjUgeWpwZdOeLSYCmNxdaMXnJtWBt0kXACnk3zW8fpbWq4IkdFb5tN%2Fqj0itzb9C5%2FlCldVvQOjxV3y%2BsQ272QGe%2BkbsAXV%2BsmqZLMcUKyCZFxFlfJJolfP6rn1nkm9ItraQ5OWxv9EW7crcJBwKEL6kH7trI3BBdlS9eNMH2qzACps3pNUSVZbWrmjtmaaS3HtppPmLjBTv2EeUQ8exwCxm8IroCtbpxJ6Ovzd9EyLkZodnMZU5RNFNO9wVW20zrnmxQcy4l6g8sx5hdVGFVd1P%2FGAopYNeZzX6FHtJRrgUcevEpi8te%2FQwg7f%2F0gY6pgFkJ6GS1LuS%2BQa8pp41MRyfM4y2Kb2XqcIUPO1BsCOqJG9NNPMbZI7VOcMJ61C2j4fnebU9OX3DkDsjDMRCkdxTkYcmcZRaD8JBlIsP9iBpwhADATgcPZwFbdUmuOivhHxWxZkoiBLrO3V4OZzDybfX9TkmcD5hy2%2F4Io2jDW7dpdixzlFh4bo3WYdcLoZt841e20YANbKLUeou3Gb%2BH9sP8W9eRZHt&X-Amz-Signature=b10270bf89f7ea3d7da78a877624b0abec33910c13d5ae8a760a6f8d89e9637d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那咱今天又来享受福报啦。我们的故事从这个类说起，refresh remote application event 它是整个 bus 组件发送的批量刷新事件。那咱看到其实它并没有包含多少代码，那它主要的核心业务都在哪里？在它的 super 也就是负类的构造器当中。 OK 咱先别着急着点进去，看一看都有哪些类用到了它 bus 组件真的非常简单。所以我们查看一下这个类的引用很容易找到了两个上下游的关联类，分别叫什么呢？一个叫 refresh bus and point 另一个叫 refresh 


listener 这个名字就不打自招了。对不对？其中一个是消息发布者，另一个就是消息的接收者了，非常的直观。 OK 那我们何不打开 debug 模式，从消息发送者开始，沿着这个轨迹，从上到下撸一遍，就像平时撸串一样。 OK 那咱先把消息的发布者打开。叫 refresh bus and point 好，他已在门外恭候多时了，我们把它打开。好在这里大家有没有看到一个非常熟悉的门牌号？叫什么叫 bus refresh 他通过哪一个 annotation 进行修饰的这个 end point 大家知道它出自哪吗？它正是出自 activator 这个组件中。所以同学们如果以后想要扩展一个新的 act reader 端点怎么做呢？咱也说明一个类使用 end point 修饰这个类，然后在后面添加一个 ID 那么大家在打开 X rate 页面的时候也会看到这样一个端点暴露出来。


OK 那我们往下看，他这里提供了两个方法，大家是不是还记得在前一章当中，我们打开 X rate 端点的时候，发现在 buzz refresh 服务的 UR L 的末尾还有一个 destination 参数。那这个 destination 参数就是这个方法接收到的 selector 参数了。在这里咱可以指定某一台或者某几台带有同样特征量的机器进行这个刷新动作。那我这里先在巴斯 refresh 这个方法上打上一个断点咱不看这个 destination 只看这个默认的原始方法。那因为我这里已经使用 debug 模式启动了所有项目，我跟大家说一下有哪些项目需要启动。


第一个项目是 eureka server 我们要把它启动起来。第二个就是咱前面创建好的这个 config bus server 这个 config bus server 咱只用通过 run 形式把它跑起来就行了，不用使用 debug 但是接下来咱要使用 debug 模式开启这个项目叫 config bus client 我们把它用 debug 模式开起来，然后在这里打上一个断碟，接下来就去 postman 里发送一个请求，postman走起，打开 postman 常向 config client 发送请求也就是端点号为 61,002 的 client 它可不是配置中心，同样的也是往 activator 的 bus refresh 端点发送一个 post 请求，321发射。


好，大家看这个断点已经到这里了，我们收集小桌板来看一下这个 application event 里面藏了个什么鬼，到了这个 event 当中。好，我们跟进负类的方法，看它在负类方法有什么幺蛾子。 OK 负类方法中还有一个负类方法，咱这里就先不跟进去了，直接点进去瞄一眼就可以了。其实到了这里，它无非就是 set 一个 time step 那这个 super 方法实际上里面并没有什么内容，它这只是初始化一个 source 属性，我们不用管他。好回退回来往下开始一步步走啦。


original 是谁？他其实就是 instance ID 如果我们打开 expression 面板去看一下它的内容，它是以 config 杠 bus 再一个横杠 client 开头，加上端点后面跟了一串字符串的 instance ID 也就是一个唯一的 idok 那么接下来这个 if 条件，如果你的 destination service 没有指定它给你默认两个星号，两个星号是什么意思啊？它算是一个通配符，也就是说会对所有的节点生效。那么再往后的逻辑，如果它并不是对所有节点的生效，要对它做一系列的处理流程了，这里我们就不深入进去看了，同学们有兴趣的话可以自己研究一下，就是如何来指定 destination 使当前的这个刷新请求只对特定的机器生效。


好，我们再往下走。剩下的两步平淡无奇，没有什么逻辑，分别是把 destination 塞入进去。那最后一个属性就是一个简单的 UUID 它其实是作为整个 event 也就是消息体的 ID 好从这里我们可以看出，这个 remote application event 主要就做了一件事，什么事呢？也就是确定 destination 对于咱来说 destination 就是通配所有服务。 OK 那我把这个断点往上返回一层，再往上返回一层。那这个 refresh remote application 对象就已经创建好了，咱创建好这个 event 以后，要把它给推送出去对不对？所以这里有个 publish 方法，我们点进去。


好，到了这里我们就要把这个 event 发送出去，大家可以看到它是在哪里发送的。在这个 context 的上下文，大家不要以为这个 context 是 buzz 中的组件。实际上这个类 application invan publisher 它其实是 sprint 下面的一个通用组件，专门用来发布上下文中的消息的，大家在很多开源项目中都可以看到他的身影。 OK 那他是具体怎么样发布这个消息的呢？我们点进去。好，我们再点进去。


publish eventok 到了主体的逻辑，咱来看它的入参这个入参第一个参数就是我要正儿八经发布的消息体，那第二个参数实际上咱没有指定还是空。 OK 那他这里开始做数据验证了。你不能假传圣旨，你这个 event 要有，如果你没有消息的话，那我要给你报错，那么再往下走，他开始判断你的 event 类型。如果你的 event 类型是 application event 那他这里会做一个强制转换，把它强制转换成了 application event 以后往下走。


OK 到了这里大家止步，又是一个看似不起眼的方法，但是背后暗藏玄机。这里我将要发布事件了，怎么说，咱进去看一眼呗，点进这个 multi K cast invent 方法。好，这边打上一个断点走。你好，进来了对不对？接着往下走一步，咱们抛开繁文缛节，不入眼的小知县根本不看好这个 get application listeners 那他将获得三个对象，我们把它叫三板斧。其中有一个对象跟 consumer 息息相关，叫什么 refresh listener 他就是会 consumer 也就是消费咱发布的这个事件的监听器。


好，我们不妨先在这个监听器当中打上一个断点，就是你了 refresh listener 在这打上一个断点以后，前面这个 for 循环就不用管它了，直接把断点放掉。 Ok. 断点放掉以后，就来到了我们的 refresh listen 当中。这个方法只有一行不有两行，其中一行还是 log 那咱看一下这个主体方法 context refresher 这个类中的 refresh 方法，它做了什么事儿？我们点进来，断点走进来。
紧接着第一个 refresh environment 方法，再走进来。 OK 往下走一步，看它这个名字叫 before 


这个 before 相当于老的对象，也就是在变更以前的这些属性。这一行的方法咱就不进去看了。为什么？你看看这个方法写的纷繁复杂，看了大家也看不懂这里这个 for 循环 if if else 条件就像一层爬楼梯一样，这个其实是编码中的一个大忌，它就像一个公司的组织架构一样。如果你这个公司组织架构层级非常非常复杂，它效率一定不会高的，而且看起来也让人很心烦。我觉得四层已经算是极限了，不要再多了，尽量把它保持层级比较单一一些分支逻辑如果太复杂了，就把它抽取出来。 OK 那咱这个方法的名称就说明了他要做的一件事情，add configuration files to environment 把配置文件加入到环境当中，咱不去看。
经过这一段猛如虎的操作，咱的属性结构发生了变化，我们进到 changes 这个项目当中。好在 changes 里面，它有两个入参，分别是 before 和 after 那很明白的，这个 before 就是变更之前的属性。 after 就是我需要变更到的属性。这里声明了一个 result 实际上它更像是一个 merge 操作。如果一个变量只在 before 或者 after 中的其中一个属性当中存在，那么我们会把它加到返回的结果里。如果一个变量在 before 和 up 的中同时存在，我们以 after 为准。 OK 那知道了这个流程，咱直接回退到上一层就好了。



回退到上一层以后，大家看这里。接下来它又会发送一个 event 叫 environment change event 这里我们就不具体深入进去介绍了。因为这个 event 的发布将触发一系列的连锁反应，我们把断点放掉，静观其变，好似乎什么都没有发生。那就对了，因为我没有在相应的蕾丝那处打断点，我们直接把这个方法先返回。
好在这里又是一个平淡无奇的 refresh all 方法，但是这里面似有玄机，我们点进去看一下。首先它进入了自毁程序，直接调用了 destroy 销毁方法。但是咱们看上面的这个 manage 的 operation 里面有一句说明，他说在这个 scope 当中，我们要清空所有病中的当前的 instance 然后强制的做一个 refreshok 那我们来看它怎么做这个refresh ，它也是通过 publish invent 方法来做的 publish 哪个 invent refresh scope refresh 的 invent 像一个顺口溜一样。 OK 我们这里把断点放掉，看它会到哪里。我已经提前在那边埋伏好，打了。好断点走。


OK 那我们这里看到它进到了 eureka discovery client configuration 这里，为什么它进到这里呢？因为大家看到这里，它有一个 annotation 叫 conditional on class 这里面的属性是谁呢？是不是刚才咱发布的这个 event 呢？所以他这里相当于一个 listener 获得了响应。那么接下来他会做一件什么事儿？很简单。


我们看，他这里提到了一句 register in case metadata change 也就是说如果你的 metadata 元数据有所改变，那我要怎么样？我要把 outer registration 先给 stop 一下，然后再 start 我们看一下它的 log 它应该是在 debug 的端口页面报了。
你看，它的 service status 这里已经被写成了标记成了 down 我们把 log 往下移，看到这里有一行 log unregistering application 然后把这个服务的 status 设置成了 doneok 我们把 log 再清空一下，看它下一步操作做什么，像发神经一样先把它 stop 掉，然后再重新 start 好，这里看到 registering application 好，又把它重新做了一个 up 注册。讲到这里，咱这一节的 demo 内容就结束了，我来跟大家总结一下。


在这一节当中，我们首先看了 bus 发送的 refresh remote application event 它是触发整个批量刷新的事件类。然后我们进到了 refresh bus and point 这个类当中，它是通过 activator 暴露出来的一个 bus refresh 接口，然后来发布这一个批量刷新的事件的。


与发布端相对应的，我们还带大家看了另外一个叫 refresh listener 的类，它会监听 refresh 事件。当事件发生的时候它会刷新本地的配置，并且由于源数据发生了变更，所以它会发送一个新的事件，这个事件最终将要传递到 eureka discovery client 这个类当中做服务的 unregistry 并且再重新做注册。
OK 整个行为全是通过 invent 追问我们叫事件驱动，那其实这是一种非常好的编程解耦的模式，可以对你程序中的各个模块之间划分清晰的界限，同学们倒是可以借鉴 bus 的这种 invent 追问的思想，把它应用在自己的项目中，对于可以异步执行的消息驱动场景非常非常的好用。 OK 到这里本节的内容就结束了。在下一节当中，我来跟大家一起探讨一下如何使用 git 的一个功能叫 webhook 自动推送属性文件的变更。那同学我们下一节再见。





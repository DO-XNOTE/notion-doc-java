---
title: 3-2 SpringBoot  Admin监控数据可视化
---

# 3-2 SpringBoot  Admin监控数据可视化

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/0a9782ff-6cf2-4338-8b2c-bf22609ac8b6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R6RBMZOL%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230100Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICKhLsZHnOI1wbfhu1orSlUA2HdNYstXSV1NpZv%2B4XRfAiAntHS569Nog9Vg4B0l2g0QI5FdlIEyE1ZMUFSoOVFfxCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMwMsWIOh4MMuStTiXKtwDR%2Bnhpakdu5bGxgb%2B8ZxMeqUF2%2FQIM8TQH7saXq9EPUWHW1zRrYWdDZxYQIobXTvEH%2FIO2n8FiMokyzqL30oMEAIyv14HDNEtzmlCvlQuqxLbOca4%2BvZZKp8ZHoJe2bCWs1QDuC%2Fe1Fkvf8V1fdxwyaJRvox8CxyEajzQs%2BrI%2B%2B1ce5jEcc9HR57Y2EcoNmAOOmrklZsFPt%2BOglMrcljTh1Qj1W43RrtsdEVlvVY60wzZDXOU0dcU31DeQ9dIpMtDhzUP6E7EQE7UNsn0QpxLiMhpXEuVxFhlRFP7IIH5TDjUR3R0OlqdUk0SRjhaawHutj%2BTFjUgeWpwZdOeLSYCmNxdaMXnJtWBt0kXACnk3zW8fpbWq4IkdFb5tN%2Fqj0itzb9C5%2FlCldVvQOjxV3y%2BsQ272QGe%2BkbsAXV%2BsmqZLMcUKyCZFxFlfJJolfP6rn1nkm9ItraQ5OWxv9EW7crcJBwKEL6kH7trI3BBdlS9eNMH2qzACps3pNUSVZbWrmjtmaaS3HtppPmLjBTv2EeUQ8exwCxm8IroCtbpxJ6Ovzd9EyLkZodnMZU5RNFNO9wVW20zrnmxQcy4l6g8sx5hdVGFVd1P%2FGAopYNeZzX6FHtJRrgUcevEpi8te%2FQwg7f%2F0gY6pgFkJ6GS1LuS%2BQa8pp41MRyfM4y2Kb2XqcIUPO1BsCOqJG9NNPMbZI7VOcMJ61C2j4fnebU9OX3DkDsjDMRCkdxTkYcmcZRaD8JBlIsP9iBpwhADATgcPZwFbdUmuOivhHxWxZkoiBLrO3V4OZzDybfX9TkmcD5hy2%2F4Io2jDW7dpdixzlFh4bo3WYdcLoZt841e20YANbKLUeou3Gb%2BH9sP8W9eRZHt&X-Amz-Signature=8378b67f3339fc6397d082150d2a608a3de2fbffa0ce6581ad9d6e6f46fa117c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/2dbbc8b4-bcc9-437e-a419-73f341aac238/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R6RBMZOL%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230100Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICKhLsZHnOI1wbfhu1orSlUA2HdNYstXSV1NpZv%2B4XRfAiAntHS569Nog9Vg4B0l2g0QI5FdlIEyE1ZMUFSoOVFfxCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMwMsWIOh4MMuStTiXKtwDR%2Bnhpakdu5bGxgb%2B8ZxMeqUF2%2FQIM8TQH7saXq9EPUWHW1zRrYWdDZxYQIobXTvEH%2FIO2n8FiMokyzqL30oMEAIyv14HDNEtzmlCvlQuqxLbOca4%2BvZZKp8ZHoJe2bCWs1QDuC%2Fe1Fkvf8V1fdxwyaJRvox8CxyEajzQs%2BrI%2B%2B1ce5jEcc9HR57Y2EcoNmAOOmrklZsFPt%2BOglMrcljTh1Qj1W43RrtsdEVlvVY60wzZDXOU0dcU31DeQ9dIpMtDhzUP6E7EQE7UNsn0QpxLiMhpXEuVxFhlRFP7IIH5TDjUR3R0OlqdUk0SRjhaawHutj%2BTFjUgeWpwZdOeLSYCmNxdaMXnJtWBt0kXACnk3zW8fpbWq4IkdFb5tN%2Fqj0itzb9C5%2FlCldVvQOjxV3y%2BsQ272QGe%2BkbsAXV%2BsmqZLMcUKyCZFxFlfJJolfP6rn1nkm9ItraQ5OWxv9EW7crcJBwKEL6kH7trI3BBdlS9eNMH2qzACps3pNUSVZbWrmjtmaaS3HtppPmLjBTv2EeUQ8exwCxm8IroCtbpxJ6Ovzd9EyLkZodnMZU5RNFNO9wVW20zrnmxQcy4l6g8sx5hdVGFVd1P%2FGAopYNeZzX6FHtJRrgUcevEpi8te%2FQwg7f%2F0gY6pgFkJ6GS1LuS%2BQa8pp41MRyfM4y2Kb2XqcIUPO1BsCOqJG9NNPMbZI7VOcMJ61C2j4fnebU9OX3DkDsjDMRCkdxTkYcmcZRaD8JBlIsP9iBpwhADATgcPZwFbdUmuOivhHxWxZkoiBLrO3V4OZzDybfX9TkmcD5hy2%2F4Io2jDW7dpdixzlFh4bo3WYdcLoZt841e20YANbKLUeou3Gb%2BH9sP8W9eRZHt&X-Amz-Signature=5f2063a093d1ad00ad185ed8a0bf7e35a3b8afed439307b7d2691134213d01b5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/9ed3b51b-e411-4a99-9ef0-19d6be37a1bb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R6RBMZOL%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230100Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICKhLsZHnOI1wbfhu1orSlUA2HdNYstXSV1NpZv%2B4XRfAiAntHS569Nog9Vg4B0l2g0QI5FdlIEyE1ZMUFSoOVFfxCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMwMsWIOh4MMuStTiXKtwDR%2Bnhpakdu5bGxgb%2B8ZxMeqUF2%2FQIM8TQH7saXq9EPUWHW1zRrYWdDZxYQIobXTvEH%2FIO2n8FiMokyzqL30oMEAIyv14HDNEtzmlCvlQuqxLbOca4%2BvZZKp8ZHoJe2bCWs1QDuC%2Fe1Fkvf8V1fdxwyaJRvox8CxyEajzQs%2BrI%2B%2B1ce5jEcc9HR57Y2EcoNmAOOmrklZsFPt%2BOglMrcljTh1Qj1W43RrtsdEVlvVY60wzZDXOU0dcU31DeQ9dIpMtDhzUP6E7EQE7UNsn0QpxLiMhpXEuVxFhlRFP7IIH5TDjUR3R0OlqdUk0SRjhaawHutj%2BTFjUgeWpwZdOeLSYCmNxdaMXnJtWBt0kXACnk3zW8fpbWq4IkdFb5tN%2Fqj0itzb9C5%2FlCldVvQOjxV3y%2BsQ272QGe%2BkbsAXV%2BsmqZLMcUKyCZFxFlfJJolfP6rn1nkm9ItraQ5OWxv9EW7crcJBwKEL6kH7trI3BBdlS9eNMH2qzACps3pNUSVZbWrmjtmaaS3HtppPmLjBTv2EeUQ8exwCxm8IroCtbpxJ6Ovzd9EyLkZodnMZU5RNFNO9wVW20zrnmxQcy4l6g8sx5hdVGFVd1P%2FGAopYNeZzX6FHtJRrgUcevEpi8te%2FQwg7f%2F0gY6pgFkJ6GS1LuS%2BQa8pp41MRyfM4y2Kb2XqcIUPO1BsCOqJG9NNPMbZI7VOcMJ61C2j4fnebU9OX3DkDsjDMRCkdxTkYcmcZRaD8JBlIsP9iBpwhADATgcPZwFbdUmuOivhHxWxZkoiBLrO3V4OZzDybfX9TkmcD5hy2%2F4Io2jDW7dpdixzlFh4bo3WYdcLoZt841e20YANbKLUeou3Gb%2BH9sP8W9eRZHt&X-Amz-Signature=deb98297dba0d1bad3793ad1a6b913ae14a00fa7d43db6d20774d6a27d8bae2b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[https://micrometer.io/docs](https://micrometer.io/docs)

这节课来探讨如何将 spring boot activator 的监控数据可视化。要想实现这个目标，有非常多的选择，例如Atlas、Datalog、刚莉娅等等等等，有小 20 种选择。同学们如果感兴趣，可以点击地址阅读相关的文档。目前在这个领域最被业界认可也最流行的工具是 spring boot admin。也有一些企业选择使用 prime Hues 加上 Grafana 这两款软件组合，实现数据可视化。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/71208d3e-ad65-40e8-963b-0db9248ee2c7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R6RBMZOL%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230101Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICKhLsZHnOI1wbfhu1orSlUA2HdNYstXSV1NpZv%2B4XRfAiAntHS569Nog9Vg4B0l2g0QI5FdlIEyE1ZMUFSoOVFfxCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMwMsWIOh4MMuStTiXKtwDR%2Bnhpakdu5bGxgb%2B8ZxMeqUF2%2FQIM8TQH7saXq9EPUWHW1zRrYWdDZxYQIobXTvEH%2FIO2n8FiMokyzqL30oMEAIyv14HDNEtzmlCvlQuqxLbOca4%2BvZZKp8ZHoJe2bCWs1QDuC%2Fe1Fkvf8V1fdxwyaJRvox8CxyEajzQs%2BrI%2B%2B1ce5jEcc9HR57Y2EcoNmAOOmrklZsFPt%2BOglMrcljTh1Qj1W43RrtsdEVlvVY60wzZDXOU0dcU31DeQ9dIpMtDhzUP6E7EQE7UNsn0QpxLiMhpXEuVxFhlRFP7IIH5TDjUR3R0OlqdUk0SRjhaawHutj%2BTFjUgeWpwZdOeLSYCmNxdaMXnJtWBt0kXACnk3zW8fpbWq4IkdFb5tN%2Fqj0itzb9C5%2FlCldVvQOjxV3y%2BsQ272QGe%2BkbsAXV%2BsmqZLMcUKyCZFxFlfJJolfP6rn1nkm9ItraQ5OWxv9EW7crcJBwKEL6kH7trI3BBdlS9eNMH2qzACps3pNUSVZbWrmjtmaaS3HtppPmLjBTv2EeUQ8exwCxm8IroCtbpxJ6Ovzd9EyLkZodnMZU5RNFNO9wVW20zrnmxQcy4l6g8sx5hdVGFVd1P%2FGAopYNeZzX6FHtJRrgUcevEpi8te%2FQwg7f%2F0gY6pgFkJ6GS1LuS%2BQa8pp41MRyfM4y2Kb2XqcIUPO1BsCOqJG9NNPMbZI7VOcMJ61C2j4fnebU9OX3DkDsjDMRCkdxTkYcmcZRaD8JBlIsP9iBpwhADATgcPZwFbdUmuOivhHxWxZkoiBLrO3V4OZzDybfX9TkmcD5hy2%2F4Io2jDW7dpdixzlFh4bo3WYdcLoZt841e20YANbKLUeou3Gb%2BH9sP8W9eRZHt&X-Amz-Signature=20c39314e59825318ef8ba8df70f8379e9460ed0e7f827b953052197ea4f2bc4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

课上这两种最流行的方案都会探讨到，毕竟咱们这是一套面向实战的课程对吧？企业里面流行什么咱们就讲什么，至于不流行的，课上咱们就不展开了。感兴趣的同学可以点击地址了解一下。回到正题，先来探讨如何使用 spring boot admin 实现监控数据可视化 spring boot admin 是一个为 spring boot 量身打造的简单易用的监控数据管理工具。它的 Github 地址在这里，官方文档在这里，感兴趣的同学也可以了解一下。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/1c33e5bb-4f95-412f-89c0-97254c595a84/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R6RBMZOL%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230100Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICKhLsZHnOI1wbfhu1orSlUA2HdNYstXSV1NpZv%2B4XRfAiAntHS569Nog9Vg4B0l2g0QI5FdlIEyE1ZMUFSoOVFfxCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMwMsWIOh4MMuStTiXKtwDR%2Bnhpakdu5bGxgb%2B8ZxMeqUF2%2FQIM8TQH7saXq9EPUWHW1zRrYWdDZxYQIobXTvEH%2FIO2n8FiMokyzqL30oMEAIyv14HDNEtzmlCvlQuqxLbOca4%2BvZZKp8ZHoJe2bCWs1QDuC%2Fe1Fkvf8V1fdxwyaJRvox8CxyEajzQs%2BrI%2B%2B1ce5jEcc9HR57Y2EcoNmAOOmrklZsFPt%2BOglMrcljTh1Qj1W43RrtsdEVlvVY60wzZDXOU0dcU31DeQ9dIpMtDhzUP6E7EQE7UNsn0QpxLiMhpXEuVxFhlRFP7IIH5TDjUR3R0OlqdUk0SRjhaawHutj%2BTFjUgeWpwZdOeLSYCmNxdaMXnJtWBt0kXACnk3zW8fpbWq4IkdFb5tN%2Fqj0itzb9C5%2FlCldVvQOjxV3y%2BsQ272QGe%2BkbsAXV%2BsmqZLMcUKyCZFxFlfJJolfP6rn1nkm9ItraQ5OWxv9EW7crcJBwKEL6kH7trI3BBdlS9eNMH2qzACps3pNUSVZbWrmjtmaaS3HtppPmLjBTv2EeUQ8exwCxm8IroCtbpxJ6Ovzd9EyLkZodnMZU5RNFNO9wVW20zrnmxQcy4l6g8sx5hdVGFVd1P%2FGAopYNeZzX6FHtJRrgUcevEpi8te%2FQwg7f%2F0gY6pgFkJ6GS1LuS%2BQa8pp41MRyfM4y2Kb2XqcIUPO1BsCOqJG9NNPMbZI7VOcMJ61C2j4fnebU9OX3DkDsjDMRCkdxTkYcmcZRaD8JBlIsP9iBpwhADATgcPZwFbdUmuOivhHxWxZkoiBLrO3V4OZzDybfX9TkmcD5hy2%2F4Io2jDW7dpdixzlFh4bo3WYdcLoZt841e20YANbKLUeou3Gb%2BH9sP8W9eRZHt&X-Amz-Signature=dba60f4bde8b41c1c06fa75b49e73dadadec1a10455319853373104dd20a188d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

好，下面我们就来使用 springboot admin 实现监控数据可视化。


spring boot admin 总体来说有两种模式，第一种模式是基于 spring boot admin client 的模式，这种模式下每个微服务都需要集成 admin client， admin client 会把微服务的 i p 端口等等信息注册到 admin server 上面，这样的 admin server 就可以找到每个微服务的 ip 地址和端口了。再去拼接上 actuator 杠星星这样的地址，定时的请求，就可以拿到每个微服务的 x urator 监控信息了，好来写代码，现在编写。
Is rainbow the enemy server file new projects?

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e08dc30b-1e3e-4ed4-84fc-ef40952635a0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R6RBMZOL%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230101Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCICKhLsZHnOI1wbfhu1orSlUA2HdNYstXSV1NpZv%2B4XRfAiAntHS569Nog9Vg4B0l2g0QI5FdlIEyE1ZMUFSoOVFfxCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMwMsWIOh4MMuStTiXKtwDR%2Bnhpakdu5bGxgb%2B8ZxMeqUF2%2FQIM8TQH7saXq9EPUWHW1zRrYWdDZxYQIobXTvEH%2FIO2n8FiMokyzqL30oMEAIyv14HDNEtzmlCvlQuqxLbOca4%2BvZZKp8ZHoJe2bCWs1QDuC%2Fe1Fkvf8V1fdxwyaJRvox8CxyEajzQs%2BrI%2B%2B1ce5jEcc9HR57Y2EcoNmAOOmrklZsFPt%2BOglMrcljTh1Qj1W43RrtsdEVlvVY60wzZDXOU0dcU31DeQ9dIpMtDhzUP6E7EQE7UNsn0QpxLiMhpXEuVxFhlRFP7IIH5TDjUR3R0OlqdUk0SRjhaawHutj%2BTFjUgeWpwZdOeLSYCmNxdaMXnJtWBt0kXACnk3zW8fpbWq4IkdFb5tN%2Fqj0itzb9C5%2FlCldVvQOjxV3y%2BsQ272QGe%2BkbsAXV%2BsmqZLMcUKyCZFxFlfJJolfP6rn1nkm9ItraQ5OWxv9EW7crcJBwKEL6kH7trI3BBdlS9eNMH2qzACps3pNUSVZbWrmjtmaaS3HtppPmLjBTv2EeUQ8exwCxm8IroCtbpxJ6Ovzd9EyLkZodnMZU5RNFNO9wVW20zrnmxQcy4l6g8sx5hdVGFVd1P%2FGAopYNeZzX6FHtJRrgUcevEpi8te%2FQwg7f%2F0gY6pgFkJ6GS1LuS%2BQa8pp41MRyfM4y2Kb2XqcIUPO1BsCOqJG9NNPMbZI7VOcMJ61C2j4fnebU9OX3DkDsjDMRCkdxTkYcmcZRaD8JBlIsP9iBpwhADATgcPZwFbdUmuOivhHxWxZkoiBLrO3V4OZzDybfX9TkmcD5hy2%2F4Io2jDW7dpdixzlFh4bo3WYdcLoZt841e20YANbKLUeou3Gb%2BH9sP8W9eRZHt&X-Amz-Signature=27d9665cff750d23c337eec297998ee62ad6496ce3c816930c038d294125d0f8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

使用 spring initializer 快速创建项目 next terror group。
Id you shall come there? Any much carry artifact? Daddy? Just rain boots. Admin server next. 选择 spring boot 版本，比如 2 点一点十一，输入admin，选择 admin server next 选择项目创建的位置，我们就放在这里了，给你 import 一下。项目创建好了，打开 palm x mail，我们来分析一下。依赖。可以发现 spring boot initializer 自动规模添加了这样一段依赖，叫做 spring boot admin start server。除此以外，还给我们添加了这么一段。还记得在 spring cloud 相关章节，我们为项目整合 spring cloud 的时候，也有添加类似的这么一段。这一段表达的是什么意思？表示整合。 Spring boot, enemy! 的添加。
Spring boot element you like?


的时候就不用自己指定版本了，否则的话，我们就得在这里指定 spring boot admin 的版本。第二步，打开启动类，在上面添加一个注解，叫做 enable admin server。第三步写配置。我们把 application practice 删掉，创建一个文件，叫做 application 点 one 秒，指定 time cat 端口，比如叫8988， spring boot admin server 就已经写好了。


启动， host 8988，可以看到能够正常访问 Springboard enemy server。目前的 Springboard enemy server 监控了 0 个微服务回答PPT。下面我们来为富地 DV 项目整合 admin client 打开负 d v API，打开 pump x mail。首先为项目整合 spring boot admin， copy dependency management 这么一段。粘贴。 copy Springboard admin 的版本，粘贴。 import 一下，整合 Springboard admin 之后添加依赖，叫做 spring boot enemy starter clutch。 import 一下添加完依赖之后，找到项目的 application Watermail 文件。
添加配置。首先添加 spring boot client URL，把它配置成 admin server 的地址 HTTP local host 8988。如果你的 admin server 有多个实例，以逗号的形式分割就可以了。除此以外，还需要添加 instance name 来配置成 foodie DV。这个配置的意思是注册到 admin server 的微服名称。


启动项目。可以看到，虽然我们没有刷新浏览器，但是这边已经注册了一个微服务，叫做富力DV。点击会放大，再次点击就会看到详情。如果你对前面讲解的 spring boot actuator 比较熟悉，看到这个界面你一定也不会陌生。像这里的info，这是我们 application Watermail 里面配置的info，这里的 health 恰恰是我们的health。


单点。 the threads 则是 extrator 的thread。 dump 端点左边有很多的菜单，挑一两个玩一玩。比如matrix，其实是 spring boot actuator 的 matrix 端点， spring boot admin 自动展示了所有的子端点，只要点击 add 就可以实时监控了，以此类推。 environment 则是 executor 的 ENV 单点，展示应用的环境变量。


边还有一个 lovers 端点，点击会展示当前应用所有包的日志级别，它本质上是 sprint activated 的 loggers 端点， spring boot admin 除了可以查看日志级别以外，也可以动态修改。比如有一天我们的项目发生了问题，我们想要定位，于是我们想把一些包的日志级别设成debug。比如我们现在直接把 root 设成debug，实时生效。可以看到项目现在打印了很多的 debug 日志，我们去排错。


排完错之后，我们再来到 spring board admin 上面把日志级别设回成info。整个过程不需要重启项目，非常的方便。其他的菜单同学们也可以玩一玩，比较的简单。回答PPT。 spring boot admin 还有第二种模式，这种模式基于服务发现组件。在这种模式下，微服务不需要集成client，只需要注册到服务发现组件上面。比如 Eureka admin server 需要集成 Eureka 的 client element， server 会自动从服务发现组件上面找到微服务的 actuator 的相关端点，并定时拉取信息来写代码。


先来编写一个Eurocarver。还记得 Eurocarver 怎么写吗？一起来复习一下。 found new project spring utilizer next， terrorgroup ID come 点 IP match artifact ID Euroka server。选择 Springboard 版本。 2 点一点十一输入 Eureka server。Finish。项目创建好了，您泡了一下。打开 palm XML，可以看到 spring initializer 已经为我们添加了 Euroka server 的相关依赖。


接着我们找到启动类，在启动类上添加 enable your Caserver 的注解。最后来写配置，把 application properties 删掉，创建一个新的文件，叫做application。点完秒， server 点 pot 指定 Eurika server 的端口8761。
True Eureka client service Yaya before the zone, as you did.


TB local host 8761 erica 还记得后面的小尾巴不能少，加上 fetch registry 设成 false 以及。 Register with Eureka. Shouldn't force. 还记得这两个配置是什么意思吗？ fetch registry 表示是否要从其他 Eurika server 实例上获取数据，默认的是 true Eurock 默认是集群模式的。


register with Euroka 表示是否要注册到其他 Euroka server 上，启动 Uri Caserver 系统。好了，下面来改造福地 DV 这个项目。首先打开泡沫Xmail。由于在这种模式下，每个微服务只要注册到服务发现组件就 OK 了，它不再需要集成 admin client，所以我们把 spring boot admin 相关的依赖全部注释掉。


Imports. 来整合 spring cloud， spring cloud 的依赖管理器，到负 DV 这个项目粘贴。把 spring cloud 的版本也 copy 过来，粘贴。 import 一下，加上 Eureka client 的依赖。


Spring cloud starter Netflix Eureka client. In Paris. Okay. Application one meal. 首先把 spring boot admin 相关的配置给注释掉，在指定 Euroka 的相关配置， the father zone， HTTP locker host 8761 erica。再指定 spring application name 表示注册到 Eurika 上面的微服名称自立 DV 重启项目，下了爸问 logo host 8761，可以看到富地 Dev 这个项目已经成功地注册到 Ureka 上面了。左边这半部分我们已经实现完成了。下面 like the admin server 打开泡面， x 面，添加 spring cloud 的依赖管理器，puppy，粘贴， copy sprinkle out of 版本，粘贴硬泡了一下，添加 spring cloud starter Netflix Euroka client 你判了一下，打开 play k 西瓜妙，也是一样。添加于卡的相关配置。 HTTP local host 8761 erica spring application name 叫 admin server，双击项目，下了刷新 Urica 可以看到 UUKA 


server 上面已经注册来人名 server 已经负DV。刷新 spring boot admin server 可以看到现在 admin server 上面已经可以看到富地 DV 这个项目，以及 admin server 自己点击富力DV，它会放大。再次点击就可以看到详情。我们会发现在这种模式下达到的效果和第一种模式没有区别。返回点击 admin server，点击进去，我们会发现里面没有数据。这是因为 Springboard admin server 的 x Ray 的端点没有添加配置，目前只暴露了 


pairs 单点以及 info 单点。我们可以配一下。 web exposure include 把它设成新，并且泰尔斯单点也秀一下。第一条把它设成二位子。重启项目。刷新可以看到，现在 activator 已经展示了所有的监控单点。访问 springboard admin 的首页可以发现，现在只监控了富帝 DV 这个项目。 spring put admin server 过了一会才会监控到，这是为什么？还记得 Eureka client 本地是维护着一个缓存的，缓存默认 30 秒才会刷新一次，所以这里会有延迟。点击进去可以看到，现在已经能够展示详情了。好，回到PPT，简单总结一下。这节课我们探讨了如何使用 springboot admin 实现 spring boot activator 的数据可视化。课上探讨了两种模式，第一种模式微服务集成 admin client，由 admin client 把微服的信息注册到 admin


 server，定时的拉取每个微服的 x a 的监控信息。第二种模式，每个微服务只要注册到服务发现组件， admin server 也注册到服务发件组件，然后 admin server 通过服务发现组件找到微服务的 activator 相关单点，并定时拉取，从而获得各个微服的 x a 的监控数据。这两种模式都可以用在生产，并且都很流行，个人相对更加喜欢第二种模式，主要是它对微服的代码没有侵入性，而且比较的自动化。好，这节课就到这里，谢谢大家。





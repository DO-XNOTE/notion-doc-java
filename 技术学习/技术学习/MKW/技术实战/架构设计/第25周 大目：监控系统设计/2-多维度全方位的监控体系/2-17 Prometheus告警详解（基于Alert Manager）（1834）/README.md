---
title: 2-17 Prometheus告警详解（基于Alert Manager）（1834）
---

# 2-17 Prometheus告警详解（基于Alert Manager）（1834）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/001fdabd-495c-47b1-b697-e7172cc0815a/SCR-20240803-ghbd.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5A5VRUI%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231626Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDT4zG%2FH9ulxQ3ry4Hs424I3ffc8P6%2BjPF2ogCyaYbmzwIhAJMi3UZ%2BnVU08%2F4lgjRKbQktbx1l0xLObi0K%2BsaO%2BHTCKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzjsyCwZxlqkFKxpaYq3AM%2FqaKQiD5HQYkGphHm6Hy%2BmedQ1mmVSoRB3QGTbb02jhUTbJktWHnOIyQQsCJYm%2BlWqO6JYDxvZmK2GxulqMqdCDh9LoKWUXmc58zRUF4o4MFtsn5IyCoG8JA9UOtjjD1UvkfLsvV43CtHExIGRswrZ0PRMVqx47qoebdJXHkaeQDRy8AeVdewg60hcI8e2kOQO0WGY0gwQ2%2F%2BiKH2M6S65xi1E0kwaYRY90T4eTEFCJtP2j13XPM5FgLaiSZAvXOSG7MJfPdRmpiVolTR94QMUjSWS9%2B1%2FpKb9%2FXlgk7lyRm7H3U8jSjSdmasskSLHog7m%2BlGQSR1f9am6abiLlUK4BwZX6d3cVCz6U1cHJpIahAh0AjRiaMFQTtq%2BFIMu1joy1YTUFZD7x5KlpMJuXoXBRP%2BHLIGLJXV6kLWWpjkZxLQYs1qWTjjH9Q7TsreHZ4cQnPSCwy6eQ8Qs%2B%2FNmuqCXXG8klK9ZJcaCcKpxjTQFL4Ie0vKyX1ZW36jOkw8FeFWBehaOJJmnaXEfmqRri%2FWaZgWGTOQBytkairXZ3n6fuQ3L840pfjNQ88wXx17I47CMuEgi1Z87%2F4WzsKw5hw6jva%2FXukkZ8kRlByopFFk2vwbx7KWpW1h3QzruDDBt%2F%2FSBjqkAW%2BO6Elh%2BpPSqeiB2MBMLl%2FQ7AZ6XaTHAjTWcS%2BMt8iY8NrJx1dcwi2leitly3wwgRM6L8vrlNV8vCIwfrJEbx3ruiSdsVo6bVjUzgQxOIGxv3Yxe4xFZyxnGpJ6kBuUUwEfV9R9zU%2Fgxhq72BdLv%2BMQo4DiW9LudelaHaL9%2F32onQXywZ%2FGQ430kwZOePJSP%2FqycH6EWfgl5PbmLqJh%2Fp5vwLT3&X-Amz-Signature=fb13f28aa75a8f48e0b407b57a6fbf4cb20ebef4efdf37aa0c8dc8a05afafd89&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/0522e31e-630a-4116-b891-eba38d8a13dd/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5A5VRUI%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231626Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDT4zG%2FH9ulxQ3ry4Hs424I3ffc8P6%2BjPF2ogCyaYbmzwIhAJMi3UZ%2BnVU08%2F4lgjRKbQktbx1l0xLObi0K%2BsaO%2BHTCKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzjsyCwZxlqkFKxpaYq3AM%2FqaKQiD5HQYkGphHm6Hy%2BmedQ1mmVSoRB3QGTbb02jhUTbJktWHnOIyQQsCJYm%2BlWqO6JYDxvZmK2GxulqMqdCDh9LoKWUXmc58zRUF4o4MFtsn5IyCoG8JA9UOtjjD1UvkfLsvV43CtHExIGRswrZ0PRMVqx47qoebdJXHkaeQDRy8AeVdewg60hcI8e2kOQO0WGY0gwQ2%2F%2BiKH2M6S65xi1E0kwaYRY90T4eTEFCJtP2j13XPM5FgLaiSZAvXOSG7MJfPdRmpiVolTR94QMUjSWS9%2B1%2FpKb9%2FXlgk7lyRm7H3U8jSjSdmasskSLHog7m%2BlGQSR1f9am6abiLlUK4BwZX6d3cVCz6U1cHJpIahAh0AjRiaMFQTtq%2BFIMu1joy1YTUFZD7x5KlpMJuXoXBRP%2BHLIGLJXV6kLWWpjkZxLQYs1qWTjjH9Q7TsreHZ4cQnPSCwy6eQ8Qs%2B%2FNmuqCXXG8klK9ZJcaCcKpxjTQFL4Ie0vKyX1ZW36jOkw8FeFWBehaOJJmnaXEfmqRri%2FWaZgWGTOQBytkairXZ3n6fuQ3L840pfjNQ88wXx17I47CMuEgi1Z87%2F4WzsKw5hw6jva%2FXukkZ8kRlByopFFk2vwbx7KWpW1h3QzruDDBt%2F%2FSBjqkAW%2BO6Elh%2BpPSqeiB2MBMLl%2FQ7AZ6XaTHAjTWcS%2BMt8iY8NrJx1dcwi2leitly3wwgRM6L8vrlNV8vCIwfrJEbx3ruiSdsVo6bVjUzgQxOIGxv3Yxe4xFZyxnGpJ6kBuUUwEfV9R9zU%2Fgxhq72BdLv%2BMQo4DiW9LudelaHaL9%2F32onQXywZ%2FGQ430kwZOePJSP%2FqycH6EWfgl5PbmLqJh%2Fp5vwLT3&X-Amz-Signature=514d7d9a8449761739dd13b900f3b4401bd1cebf651a6464c73287d3c75f2bb8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/cf2cd5c1-e28d-4555-836c-724e5e76dd56/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5A5VRUI%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231626Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDT4zG%2FH9ulxQ3ry4Hs424I3ffc8P6%2BjPF2ogCyaYbmzwIhAJMi3UZ%2BnVU08%2F4lgjRKbQktbx1l0xLObi0K%2BsaO%2BHTCKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzjsyCwZxlqkFKxpaYq3AM%2FqaKQiD5HQYkGphHm6Hy%2BmedQ1mmVSoRB3QGTbb02jhUTbJktWHnOIyQQsCJYm%2BlWqO6JYDxvZmK2GxulqMqdCDh9LoKWUXmc58zRUF4o4MFtsn5IyCoG8JA9UOtjjD1UvkfLsvV43CtHExIGRswrZ0PRMVqx47qoebdJXHkaeQDRy8AeVdewg60hcI8e2kOQO0WGY0gwQ2%2F%2BiKH2M6S65xi1E0kwaYRY90T4eTEFCJtP2j13XPM5FgLaiSZAvXOSG7MJfPdRmpiVolTR94QMUjSWS9%2B1%2FpKb9%2FXlgk7lyRm7H3U8jSjSdmasskSLHog7m%2BlGQSR1f9am6abiLlUK4BwZX6d3cVCz6U1cHJpIahAh0AjRiaMFQTtq%2BFIMu1joy1YTUFZD7x5KlpMJuXoXBRP%2BHLIGLJXV6kLWWpjkZxLQYs1qWTjjH9Q7TsreHZ4cQnPSCwy6eQ8Qs%2B%2FNmuqCXXG8klK9ZJcaCcKpxjTQFL4Ie0vKyX1ZW36jOkw8FeFWBehaOJJmnaXEfmqRri%2FWaZgWGTOQBytkairXZ3n6fuQ3L840pfjNQ88wXx17I47CMuEgi1Z87%2F4WzsKw5hw6jva%2FXukkZ8kRlByopFFk2vwbx7KWpW1h3QzruDDBt%2F%2FSBjqkAW%2BO6Elh%2BpPSqeiB2MBMLl%2FQ7AZ6XaTHAjTWcS%2BMt8iY8NrJx1dcwi2leitly3wwgRM6L8vrlNV8vCIwfrJEbx3ruiSdsVo6bVjUzgQxOIGxv3Yxe4xFZyxnGpJ6kBuUUwEfV9R9zU%2Fgxhq72BdLv%2BMQo4DiW9LudelaHaL9%2F32onQXywZ%2FGQ430kwZOePJSP%2FqycH6EWfgl5PbmLqJh%2Fp5vwLT3&X-Amz-Signature=56b6f73e50b5e3a661b027179b79e3677727551e2d81f820f59f2fbfdf047eac&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

大家好，我是大木。前面我们已经用 prometheus 实现了各种维度的监控，**但是如果监控指标不正常，该如何实现告警？**还记得在告警系统综述这一章里面，已经说明了告警的重要性，**以及实际项目中针对告警的 5 大诉求。**这节课我们就来实现前面的这 5 大诉求。首先， prometheus 本身提供了告警能力，我们不妨参考官方文档去定义一个告警规则。官方文档在这里，

[https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/](https://prometheus.io/docs/prometheus/latest/configuration/alerting_rules/)

 copy，粘贴 到 prometheus 的根目录创建一个新的文件 touch 比方， my-alerts，点 yaml ，用 idea 打开粘贴。

```shell
groups:
  # 告警组的名称
  - name: example
    # 告警规则
    rules:
    # 告警规则的名称
    - alert: HighRequestLatency
      # 基于 promQL 计算时候又时间序列满足警告条件
      expr: job:request_latency_seconds:mean5m{job="myjob"} > 0.5
      # 评估的等待时间（可选参数）表示当 expr 的条件持续为 true 一段时间之后才出发告警
      for: 10m
      # 用来自定义标签
      labels:
        severity: page
      # 用来制定一组附加信息， 比如描述的告警的详细文字等等
      # 会发哦那个给 Alert Manager
      annotations:
        # value 支持模版
        summary: High request latency
```

好，下面来分析一下 yaml 的意思。首先， 

name 是说告警组的名称，多个告警规则会形成一个组。OK，这个组的名称叫 example 

rules，表示告警规则。 

alerts 是告警规则的名称。 

expr 表示基于 prometheus 计算是否有时间序列满足告警条件。表达式计算出来的结果是true，就触发告警。 

for 是评估的等待时间，这是一个可选参数。它表示当 expr 的条件，持续为 true，一段时间之后才触发告警。比方这里，就是这个 

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/dd52ac80-0825-4026-bf56-d8ba6fc218fa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5A5VRUI%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231626Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDT4zG%2FH9ulxQ3ry4Hs424I3ffc8P6%2BjPF2ogCyaYbmzwIhAJMi3UZ%2BnVU08%2F4lgjRKbQktbx1l0xLObi0K%2BsaO%2BHTCKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzjsyCwZxlqkFKxpaYq3AM%2FqaKQiD5HQYkGphHm6Hy%2BmedQ1mmVSoRB3QGTbb02jhUTbJktWHnOIyQQsCJYm%2BlWqO6JYDxvZmK2GxulqMqdCDh9LoKWUXmc58zRUF4o4MFtsn5IyCoG8JA9UOtjjD1UvkfLsvV43CtHExIGRswrZ0PRMVqx47qoebdJXHkaeQDRy8AeVdewg60hcI8e2kOQO0WGY0gwQ2%2F%2BiKH2M6S65xi1E0kwaYRY90T4eTEFCJtP2j13XPM5FgLaiSZAvXOSG7MJfPdRmpiVolTR94QMUjSWS9%2B1%2FpKb9%2FXlgk7lyRm7H3U8jSjSdmasskSLHog7m%2BlGQSR1f9am6abiLlUK4BwZX6d3cVCz6U1cHJpIahAh0AjRiaMFQTtq%2BFIMu1joy1YTUFZD7x5KlpMJuXoXBRP%2BHLIGLJXV6kLWWpjkZxLQYs1qWTjjH9Q7TsreHZ4cQnPSCwy6eQ8Qs%2B%2FNmuqCXXG8klK9ZJcaCcKpxjTQFL4Ie0vKyX1ZW36jOkw8FeFWBehaOJJmnaXEfmqRri%2FWaZgWGTOQBytkairXZ3n6fuQ3L840pfjNQ88wXx17I47CMuEgi1Z87%2F4WzsKw5hw6jva%2FXukkZ8kRlByopFFk2vwbx7KWpW1h3QzruDDBt%2F%2FSBjqkAW%2BO6Elh%2BpPSqeiB2MBMLl%2FQ7AZ6XaTHAjTWcS%2BMt8iY8NrJx1dcwi2leitly3wwgRM6L8vrlNV8vCIwfrJEbx3ruiSdsVo6bVjUzgQxOIGxv3Yxe4xFZyxnGpJ6kBuUUwEfV9R9zU%2Fgxhq72BdLv%2BMQo4DiW9LudelaHaL9%2F32onQXywZ%2FGQ430kwZOePJSP%2FqycH6EWfgl5PbmLqJh%2Fp5vwLT3&X-Amz-Signature=cc93292c3275f59749bfd3a7b6764f1f9ea911c661d495ce102f1e4a894de846&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

PromQL 的结果等于true，要持续 10 分钟才触发告警。 

label 用来自定义标签，用来对这一个告警打上标签，这样我们可以更加方便的筛选告警。

Annotation，用来指定一组附加信息，比方，描述告警的详细文字等等。 annotation 的内容会在告警产生的时候一同发送给 AlertManager，annotation，里面的数据以 ke-value 的形式就 OK 了。这个 value 可以支持模板，通过模板可以让告警信息更加灵活。

语法大张是这样的,大括号

```shell
# To insert a firing element's label values:
{{ $labels.<labelname> }}
# To insert the numeric expression value of the firing element:
{{ $value }}
```

， $labels 点儿 labelname。用这种方式可以读取指定标签的值。 $value 可以读取当前 PromQL 表达式所计算的值。ok


下面我们不妨来写一个告警规则。告警规则的名称，比方叫 SystemCpuTooHigh。操作系统的 CPU 占用过高了。表达式写上 system cpu Usage 大于。由于我们要触发告警，所以我们故意把告警阈值设的特别小。0.00001,  for 10 秒 当 CPU 持续超过阈值达到 10 秒，就推送告警标签随便写一个，比方叫 imooc：good， annotation下的 summary。我们可以写上告警的概要信息，比如 CPU 占用过高，用大括号， $labels.instance。读取是哪一个实例的 CPU 占用过高。我们还可以写上description， description 表示告警的详情。只是，实力，唱一下。的。系统 CPU 占用过高，并持续了 10 秒。用大括号， $value。CPU，占用是这么大。

```shell
groups:
  # 告警组的名称
  - name: example
    # 告警规则
    rules:
    # 告警规则的名称
    - alert: SystemCpuTooHigh
      # 基于 promQL 计算时候又时间序列满足警告条件
      expr: system_cpu_usage > 0.00001
      # 评估的等待时间（可选参数）表示当 expr 的条件持续为 true 一段时间之后才出发告警
      for: 10s
      # 用来自定义标签
      labels:
        imooc: good
      # 用来制定一组附加信息， 比如描述的告警的详细文字等等
      # 会发哦那个给 Alert Manager
      annotations:
        # value 支持模版
        summary: CPU 占用过高:{{ $labels.instance }}
        description: "实例{{ $labels.instance}}的系统 CPU 占用过高并持续了 10s，cpu占用是：{{ $value }}"
```


OK，现在告警规则已经编写完成了。之后修改 prometheus.yaml ，找到 rule files，指定刚刚的挖妙叫 my-alert.yaml，然后，启动prometheus，访问 localhost:9090，点击 alert ，可以看到。在上面就可以展示我们刚刚定义的告警规则了。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/78dd5e10-5e89-414d-84f7-e5bb7574ba9a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5A5VRUI%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231626Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDT4zG%2FH9ulxQ3ry4Hs424I3ffc8P6%2BjPF2ogCyaYbmzwIhAJMi3UZ%2BnVU08%2F4lgjRKbQktbx1l0xLObi0K%2BsaO%2BHTCKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzjsyCwZxlqkFKxpaYq3AM%2FqaKQiD5HQYkGphHm6Hy%2BmedQ1mmVSoRB3QGTbb02jhUTbJktWHnOIyQQsCJYm%2BlWqO6JYDxvZmK2GxulqMqdCDh9LoKWUXmc58zRUF4o4MFtsn5IyCoG8JA9UOtjjD1UvkfLsvV43CtHExIGRswrZ0PRMVqx47qoebdJXHkaeQDRy8AeVdewg60hcI8e2kOQO0WGY0gwQ2%2F%2BiKH2M6S65xi1E0kwaYRY90T4eTEFCJtP2j13XPM5FgLaiSZAvXOSG7MJfPdRmpiVolTR94QMUjSWS9%2B1%2FpKb9%2FXlgk7lyRm7H3U8jSjSdmasskSLHog7m%2BlGQSR1f9am6abiLlUK4BwZX6d3cVCz6U1cHJpIahAh0AjRiaMFQTtq%2BFIMu1joy1YTUFZD7x5KlpMJuXoXBRP%2BHLIGLJXV6kLWWpjkZxLQYs1qWTjjH9Q7TsreHZ4cQnPSCwy6eQ8Qs%2B%2FNmuqCXXG8klK9ZJcaCcKpxjTQFL4Ie0vKyX1ZW36jOkw8FeFWBehaOJJmnaXEfmqRri%2FWaZgWGTOQBytkairXZ3n6fuQ3L840pfjNQ88wXx17I47CMuEgi1Z87%2F4WzsKw5hw6jva%2FXukkZ8kRlByopFFk2vwbx7KWpW1h3QzruDDBt%2F%2FSBjqkAW%2BO6Elh%2BpPSqeiB2MBMLl%2FQ7AZ6XaTHAjTWcS%2BMt8iY8NrJx1dcwi2leitly3wwgRM6L8vrlNV8vCIwfrJEbx3ruiSdsVo6bVjUzgQxOIGxv3Yxe4xFZyxnGpJ6kBuUUwEfV9R9zU%2Fgxhq72BdLv%2BMQo4DiW9LudelaHaL9%2F32onQXywZ%2FGQ430kwZOePJSP%2FqycH6EWfgl5PbmLqJh%2Fp5vwLT3&X-Amz-Signature=7ff405bfacd10a02e304e151d759c05c00a62961f5e586073a3ea67d661ac901&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

目前告警规则的状态是 inactive，刷新状态变成了 pending，并且在 labels 里面还可以看到刚刚我们自定义的标签，等待一会儿之后再刷新，状态又变成了ferry。这是什么意思？

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/06b88454-747e-4ed6-9364-3056cf6bebc6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5A5VRUI%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231626Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDT4zG%2FH9ulxQ3ry4Hs424I3ffc8P6%2BjPF2ogCyaYbmzwIhAJMi3UZ%2BnVU08%2F4lgjRKbQktbx1l0xLObi0K%2BsaO%2BHTCKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzjsyCwZxlqkFKxpaYq3AM%2FqaKQiD5HQYkGphHm6Hy%2BmedQ1mmVSoRB3QGTbb02jhUTbJktWHnOIyQQsCJYm%2BlWqO6JYDxvZmK2GxulqMqdCDh9LoKWUXmc58zRUF4o4MFtsn5IyCoG8JA9UOtjjD1UvkfLsvV43CtHExIGRswrZ0PRMVqx47qoebdJXHkaeQDRy8AeVdewg60hcI8e2kOQO0WGY0gwQ2%2F%2BiKH2M6S65xi1E0kwaYRY90T4eTEFCJtP2j13XPM5FgLaiSZAvXOSG7MJfPdRmpiVolTR94QMUjSWS9%2B1%2FpKb9%2FXlgk7lyRm7H3U8jSjSdmasskSLHog7m%2BlGQSR1f9am6abiLlUK4BwZX6d3cVCz6U1cHJpIahAh0AjRiaMFQTtq%2BFIMu1joy1YTUFZD7x5KlpMJuXoXBRP%2BHLIGLJXV6kLWWpjkZxLQYs1qWTjjH9Q7TsreHZ4cQnPSCwy6eQ8Qs%2B%2FNmuqCXXG8klK9ZJcaCcKpxjTQFL4Ie0vKyX1ZW36jOkw8FeFWBehaOJJmnaXEfmqRri%2FWaZgWGTOQBytkairXZ3n6fuQ3L840pfjNQ88wXx17I47CMuEgi1Z87%2F4WzsKw5hw6jva%2FXukkZ8kRlByopFFk2vwbx7KWpW1h3QzruDDBt%2F%2FSBjqkAW%2BO6Elh%2BpPSqeiB2MBMLl%2FQ7AZ6XaTHAjTWcS%2BMt8iY8NrJx1dcwi2leitly3wwgRM6L8vrlNV8vCIwfrJEbx3ruiSdsVo6bVjUzgQxOIGxv3Yxe4xFZyxnGpJ6kBuUUwEfV9R9zU%2Fgxhq72BdLv%2BMQo4DiW9LudelaHaL9%2F32onQXywZ%2FGQ430kwZOePJSP%2FqycH6EWfgl5PbmLqJh%2Fp5vwLT3&X-Amz-Signature=7b3d07939c38dcb607202b841a095e0f2bc05dd9a31387200476787ba920dd16&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

是这样的，在一开始规则还没有加载或者表达式计算出来结果是false，这个时候状态是inactive，最后进攻计算表达式是 true 了，于是状态就会切换成pending。再之后，表达式持续之处已经持续 10 秒了，这个时候 prometheus 就会触发告警，状态变成 firing。OK，现在告警规则的状态已经变成了 firing 了，说明 permission 已经触发了告警。但是我们发现 prometheus 的告警能力实在是太弱了，仅靠这么点东西用来生产肯定是不够的，**而且它也不满足前面我们对告警的 5 大诉求。**


要想搭建满足生产环境的告警体系，我们需要使用 AlertManager。 prometheus server 和 AlertManager 之间的关系是这样的,

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/cc4de9e2-06b2-4da4-848c-7029b20f2277/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5A5VRUI%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231626Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDT4zG%2FH9ulxQ3ry4Hs424I3ffc8P6%2BjPF2ogCyaYbmzwIhAJMi3UZ%2BnVU08%2F4lgjRKbQktbx1l0xLObi0K%2BsaO%2BHTCKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzjsyCwZxlqkFKxpaYq3AM%2FqaKQiD5HQYkGphHm6Hy%2BmedQ1mmVSoRB3QGTbb02jhUTbJktWHnOIyQQsCJYm%2BlWqO6JYDxvZmK2GxulqMqdCDh9LoKWUXmc58zRUF4o4MFtsn5IyCoG8JA9UOtjjD1UvkfLsvV43CtHExIGRswrZ0PRMVqx47qoebdJXHkaeQDRy8AeVdewg60hcI8e2kOQO0WGY0gwQ2%2F%2BiKH2M6S65xi1E0kwaYRY90T4eTEFCJtP2j13XPM5FgLaiSZAvXOSG7MJfPdRmpiVolTR94QMUjSWS9%2B1%2FpKb9%2FXlgk7lyRm7H3U8jSjSdmasskSLHog7m%2BlGQSR1f9am6abiLlUK4BwZX6d3cVCz6U1cHJpIahAh0AjRiaMFQTtq%2BFIMu1joy1YTUFZD7x5KlpMJuXoXBRP%2BHLIGLJXV6kLWWpjkZxLQYs1qWTjjH9Q7TsreHZ4cQnPSCwy6eQ8Qs%2B%2FNmuqCXXG8klK9ZJcaCcKpxjTQFL4Ie0vKyX1ZW36jOkw8FeFWBehaOJJmnaXEfmqRri%2FWaZgWGTOQBytkairXZ3n6fuQ3L840pfjNQ88wXx17I47CMuEgi1Z87%2F4WzsKw5hw6jva%2FXukkZ8kRlByopFFk2vwbx7KWpW1h3QzruDDBt%2F%2FSBjqkAW%2BO6Elh%2BpPSqeiB2MBMLl%2FQ7AZ6XaTHAjTWcS%2BMt8iY8NrJx1dcwi2leitly3wwgRM6L8vrlNV8vCIwfrJEbx3ruiSdsVo6bVjUzgQxOIGxv3Yxe4xFZyxnGpJ6kBuUUwEfV9R9zU%2Fgxhq72BdLv%2BMQo4DiW9LudelaHaL9%2F32onQXywZ%2FGQ430kwZOePJSP%2FqycH6EWfgl5PbmLqJh%2Fp5vwLT3&X-Amz-Signature=edda0f19aba169531ad10652cf41b251e63f8c14a7b11a1b0bea361beacc2fb0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

在 prometheus server 端定义告警规则，然后 prometheus server 会针对告警规则进行计算。如果满足告警规则的触发条件，会向 AlertManager 发送告警信息。 AlertManager 收到告警之后，可以做进一步的处理，比方推送告警、静默告警等等。


OK，下面我们来用 AlertManager 实现邮件告警的推送。首先下载 alerta manager 官方下载地址在这里，

[https://github.com/prometheus/alertmanager/releases/tag/v0.25.0](https://github.com/prometheus/alertmanager/releases/tag/v0.25.0)

根据自己的操作系统下载就 OK 了。对于网络不好的同学可以到这里下载。需要注意， AlertManager 我把它上传到了 resource2 这个仓库，而不是前面的 resource 仓库。这是因为 resource 仓库已经达到了容量的上限，慕课网对单个仓库的容量上限是1G。 ok 下载之后解压，加完成。


打开 AlertManager.yaml。 AlertManager 该怎么配置？文档在这里，

[https://prometheus.io/docs/alerting/latest/configuration/#email_config](https://prometheus.io/docs/alerting/latest/configuration/#email_config)

我们是想要配置邮箱告警推送，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/96c709d3-a1dc-42bd-a048-07a6e1f2aaf2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5A5VRUI%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231626Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDT4zG%2FH9ulxQ3ry4Hs424I3ffc8P6%2BjPF2ogCyaYbmzwIhAJMi3UZ%2BnVU08%2F4lgjRKbQktbx1l0xLObi0K%2BsaO%2BHTCKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzjsyCwZxlqkFKxpaYq3AM%2FqaKQiD5HQYkGphHm6Hy%2BmedQ1mmVSoRB3QGTbb02jhUTbJktWHnOIyQQsCJYm%2BlWqO6JYDxvZmK2GxulqMqdCDh9LoKWUXmc58zRUF4o4MFtsn5IyCoG8JA9UOtjjD1UvkfLsvV43CtHExIGRswrZ0PRMVqx47qoebdJXHkaeQDRy8AeVdewg60hcI8e2kOQO0WGY0gwQ2%2F%2BiKH2M6S65xi1E0kwaYRY90T4eTEFCJtP2j13XPM5FgLaiSZAvXOSG7MJfPdRmpiVolTR94QMUjSWS9%2B1%2FpKb9%2FXlgk7lyRm7H3U8jSjSdmasskSLHog7m%2BlGQSR1f9am6abiLlUK4BwZX6d3cVCz6U1cHJpIahAh0AjRiaMFQTtq%2BFIMu1joy1YTUFZD7x5KlpMJuXoXBRP%2BHLIGLJXV6kLWWpjkZxLQYs1qWTjjH9Q7TsreHZ4cQnPSCwy6eQ8Qs%2B%2FNmuqCXXG8klK9ZJcaCcKpxjTQFL4Ie0vKyX1ZW36jOkw8FeFWBehaOJJmnaXEfmqRri%2FWaZgWGTOQBytkairXZ3n6fuQ3L840pfjNQ88wXx17I47CMuEgi1Z87%2F4WzsKw5hw6jva%2FXukkZ8kRlByopFFk2vwbx7KWpW1h3QzruDDBt%2F%2FSBjqkAW%2BO6Elh%2BpPSqeiB2MBMLl%2FQ7AZ6XaTHAjTWcS%2BMt8iY8NrJx1dcwi2leitly3wwgRM6L8vrlNV8vCIwfrJEbx3ruiSdsVo6bVjUzgQxOIGxv3Yxe4xFZyxnGpJ6kBuUUwEfV9R9zU%2Fgxhq72BdLv%2BMQo4DiW9LudelaHaL9%2F32onQXywZ%2FGQ430kwZOePJSP%2FqycH6EWfgl5PbmLqJh%2Fp5vwLT3&X-Amz-Signature=70e8ec75f4a3fd846c6db1bbd3836203728b88e8c7c9ae0bedbaea0076d1d42a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

所以可以找到这里的 receiver。在 receiver 里面有一个 email configs，我们再点一下 email config，在 email config 里面就可以看到该怎么配置了。收信人发信人 smtp 的地址等等。好，我们来配一下。prometheus.yaml 中找到receivers，然后，定义一个新的 receiver name，是比方email，写上 email confics， two 指定收件人的地址， from 指定发件人的地址。

smarthost，指定发件人的 SMTP。地址。


端口可以用不安全的端口25，也可以使用安全端口465。我们使用安全端口。

US  username ，指定发件人的用户名。 password。指定发件人的密码。需要注意，这里的密码对于 126 邮箱，password，并不是登录密码，而是开启 smtp 服务时候的授权码。 OK 填入我的授权码。


require_tls，把它设成false，配置。在使用 465 端口的时候，必须设置成false，否则无法成功发送邮件。OK， OK 最后还修改 route 里面的receiver。就目前来说，我们的 receiver 是 web hook，它表示当 AlertManager 收到告警之后，会自动请求这个地址，我们需要把它修改成email。

```shell
route:
  group_by: ['alertname']
  group_wait: 30s
  group_interval: 5m
  repeat_interval: 1h
  receiver: 'email'
receivers:
  - name: 'web.hook'
    webhook_configs:
      - url: 'http://127.0.0.1:5001/'
  - name: 'emial'
    email_configs:
    - to: '1101403286@qq.com'
      from: 'bdjob001@126.com'
      smarthost: 'smtp.126.com:465' 
      auth_usernam: bdjob001
      # 126邮箱： password 并不是登录密码，而是开启 smtp 服务时候的授权码
      auth_password: FOGVODLUWERBAMTGO
      # 在使用 465 的时候必须设置成 false ，否则成功发送邮件
      require_tls: false     
inhibit_rules:
  - source_match:
      severity: 'critical'
    target_match:
      severity: 'warning'
    equal: ['alertname', 'dev', 'instance']
```


好 AlertManager 配置完毕。再目录切换到 AlertManager，执行点儿杠 AlertManager，启动 AlertManager 访问 localhost:9093，这样就可以看到 AlertManager 的界面了。点击 status 可以看到 AlertManager 的状态，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/aee5022a-9f74-466c-8dd8-2812d6768d8e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5A5VRUI%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231626Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDT4zG%2FH9ulxQ3ry4Hs424I3ffc8P6%2BjPF2ogCyaYbmzwIhAJMi3UZ%2BnVU08%2F4lgjRKbQktbx1l0xLObi0K%2BsaO%2BHTCKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzjsyCwZxlqkFKxpaYq3AM%2FqaKQiD5HQYkGphHm6Hy%2BmedQ1mmVSoRB3QGTbb02jhUTbJktWHnOIyQQsCJYm%2BlWqO6JYDxvZmK2GxulqMqdCDh9LoKWUXmc58zRUF4o4MFtsn5IyCoG8JA9UOtjjD1UvkfLsvV43CtHExIGRswrZ0PRMVqx47qoebdJXHkaeQDRy8AeVdewg60hcI8e2kOQO0WGY0gwQ2%2F%2BiKH2M6S65xi1E0kwaYRY90T4eTEFCJtP2j13XPM5FgLaiSZAvXOSG7MJfPdRmpiVolTR94QMUjSWS9%2B1%2FpKb9%2FXlgk7lyRm7H3U8jSjSdmasskSLHog7m%2BlGQSR1f9am6abiLlUK4BwZX6d3cVCz6U1cHJpIahAh0AjRiaMFQTtq%2BFIMu1joy1YTUFZD7x5KlpMJuXoXBRP%2BHLIGLJXV6kLWWpjkZxLQYs1qWTjjH9Q7TsreHZ4cQnPSCwy6eQ8Qs%2B%2FNmuqCXXG8klK9ZJcaCcKpxjTQFL4Ie0vKyX1ZW36jOkw8FeFWBehaOJJmnaXEfmqRri%2FWaZgWGTOQBytkairXZ3n6fuQ3L840pfjNQ88wXx17I47CMuEgi1Z87%2F4WzsKw5hw6jva%2FXukkZ8kRlByopFFk2vwbx7KWpW1h3QzruDDBt%2F%2FSBjqkAW%2BO6Elh%2BpPSqeiB2MBMLl%2FQ7AZ6XaTHAjTWcS%2BMt8iY8NrJx1dcwi2leitly3wwgRM6L8vrlNV8vCIwfrJEbx3ruiSdsVo6bVjUzgQxOIGxv3Yxe4xFZyxnGpJ6kBuUUwEfV9R9zU%2Fgxhq72BdLv%2BMQo4DiW9LudelaHaL9%2F32onQXywZ%2FGQ430kwZOePJSP%2FqycH6EWfgl5PbmLqJh%2Fp5vwLT3&X-Amz-Signature=e093f12eb10da4ebb7764f035f8c4fbdc34d33009d772bf6c2b7179f3c5d55dd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

下面还会展示出 AlertManager 的配置。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/8a36b551-be88-497b-ab94-e143fee374a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5A5VRUI%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231626Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDT4zG%2FH9ulxQ3ry4Hs424I3ffc8P6%2BjPF2ogCyaYbmzwIhAJMi3UZ%2BnVU08%2F4lgjRKbQktbx1l0xLObi0K%2BsaO%2BHTCKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzjsyCwZxlqkFKxpaYq3AM%2FqaKQiD5HQYkGphHm6Hy%2BmedQ1mmVSoRB3QGTbb02jhUTbJktWHnOIyQQsCJYm%2BlWqO6JYDxvZmK2GxulqMqdCDh9LoKWUXmc58zRUF4o4MFtsn5IyCoG8JA9UOtjjD1UvkfLsvV43CtHExIGRswrZ0PRMVqx47qoebdJXHkaeQDRy8AeVdewg60hcI8e2kOQO0WGY0gwQ2%2F%2BiKH2M6S65xi1E0kwaYRY90T4eTEFCJtP2j13XPM5FgLaiSZAvXOSG7MJfPdRmpiVolTR94QMUjSWS9%2B1%2FpKb9%2FXlgk7lyRm7H3U8jSjSdmasskSLHog7m%2BlGQSR1f9am6abiLlUK4BwZX6d3cVCz6U1cHJpIahAh0AjRiaMFQTtq%2BFIMu1joy1YTUFZD7x5KlpMJuXoXBRP%2BHLIGLJXV6kLWWpjkZxLQYs1qWTjjH9Q7TsreHZ4cQnPSCwy6eQ8Qs%2B%2FNmuqCXXG8klK9ZJcaCcKpxjTQFL4Ie0vKyX1ZW36jOkw8FeFWBehaOJJmnaXEfmqRri%2FWaZgWGTOQBytkairXZ3n6fuQ3L840pfjNQ88wXx17I47CMuEgi1Z87%2F4WzsKw5hw6jva%2FXukkZ8kRlByopFFk2vwbx7KWpW1h3QzruDDBt%2F%2FSBjqkAW%2BO6Elh%2BpPSqeiB2MBMLl%2FQ7AZ6XaTHAjTWcS%2BMt8iY8NrJx1dcwi2leitly3wwgRM6L8vrlNV8vCIwfrJEbx3ruiSdsVo6bVjUzgQxOIGxv3Yxe4xFZyxnGpJ6kBuUUwEfV9R9zU%2Fgxhq72BdLv%2BMQo4DiW9LudelaHaL9%2F32onQXywZ%2FGQ430kwZOePJSP%2FqycH6EWfgl5PbmLqJh%2Fp5vwLT3&X-Amz-Signature=acbd1ff03db6aca4f4d243693aee24a7c74bf2e13d48ec82429025c7e28a630e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

之后，我们还需要修改 prometheus.yaml ，找到 alerting 叉叉叉targets，修改成 localhost:9093。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/6083c144-10cb-45bb-8ca8-85a89d06ac46/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5A5VRUI%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231626Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDT4zG%2FH9ulxQ3ry4Hs424I3ffc8P6%2BjPF2ogCyaYbmzwIhAJMi3UZ%2BnVU08%2F4lgjRKbQktbx1l0xLObi0K%2BsaO%2BHTCKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzjsyCwZxlqkFKxpaYq3AM%2FqaKQiD5HQYkGphHm6Hy%2BmedQ1mmVSoRB3QGTbb02jhUTbJktWHnOIyQQsCJYm%2BlWqO6JYDxvZmK2GxulqMqdCDh9LoKWUXmc58zRUF4o4MFtsn5IyCoG8JA9UOtjjD1UvkfLsvV43CtHExIGRswrZ0PRMVqx47qoebdJXHkaeQDRy8AeVdewg60hcI8e2kOQO0WGY0gwQ2%2F%2BiKH2M6S65xi1E0kwaYRY90T4eTEFCJtP2j13XPM5FgLaiSZAvXOSG7MJfPdRmpiVolTR94QMUjSWS9%2B1%2FpKb9%2FXlgk7lyRm7H3U8jSjSdmasskSLHog7m%2BlGQSR1f9am6abiLlUK4BwZX6d3cVCz6U1cHJpIahAh0AjRiaMFQTtq%2BFIMu1joy1YTUFZD7x5KlpMJuXoXBRP%2BHLIGLJXV6kLWWpjkZxLQYs1qWTjjH9Q7TsreHZ4cQnPSCwy6eQ8Qs%2B%2FNmuqCXXG8klK9ZJcaCcKpxjTQFL4Ie0vKyX1ZW36jOkw8FeFWBehaOJJmnaXEfmqRri%2FWaZgWGTOQBytkairXZ3n6fuQ3L840pfjNQ88wXx17I47CMuEgi1Z87%2F4WzsKw5hw6jva%2FXukkZ8kRlByopFFk2vwbx7KWpW1h3QzruDDBt%2F%2FSBjqkAW%2BO6Elh%2BpPSqeiB2MBMLl%2FQ7AZ6XaTHAjTWcS%2BMt8iY8NrJx1dcwi2leitly3wwgRM6L8vrlNV8vCIwfrJEbx3ruiSdsVo6bVjUzgQxOIGxv3Yxe4xFZyxnGpJ6kBuUUwEfV9R9zU%2Fgxhq72BdLv%2BMQo4DiW9LudelaHaL9%2F32onQXywZ%2FGQ430kwZOePJSP%2FqycH6EWfgl5PbmLqJh%2Fp5vwLT3&X-Amz-Signature=33858971f3c63d30770b10d1399779fcf73b1b7c5c8c663a6e6d256686ab6dac&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

它表示当 prometheus 告警规则满足，想要触发告警的时候，就会自动请求这个地址。把告警推送给 AlertManager。好， 重启 prometheus 。接着来的 prometheus server 刷新，目前是pending，我们稍等片刻。好，现在已经变成了 firing，

说明告警已经推送了。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/fa97051a-12bc-417a-ace1-5b4204cc4114/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5A5VRUI%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231626Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDT4zG%2FH9ulxQ3ry4Hs424I3ffc8P6%2BjPF2ogCyaYbmzwIhAJMi3UZ%2BnVU08%2F4lgjRKbQktbx1l0xLObi0K%2BsaO%2BHTCKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzjsyCwZxlqkFKxpaYq3AM%2FqaKQiD5HQYkGphHm6Hy%2BmedQ1mmVSoRB3QGTbb02jhUTbJktWHnOIyQQsCJYm%2BlWqO6JYDxvZmK2GxulqMqdCDh9LoKWUXmc58zRUF4o4MFtsn5IyCoG8JA9UOtjjD1UvkfLsvV43CtHExIGRswrZ0PRMVqx47qoebdJXHkaeQDRy8AeVdewg60hcI8e2kOQO0WGY0gwQ2%2F%2BiKH2M6S65xi1E0kwaYRY90T4eTEFCJtP2j13XPM5FgLaiSZAvXOSG7MJfPdRmpiVolTR94QMUjSWS9%2B1%2FpKb9%2FXlgk7lyRm7H3U8jSjSdmasskSLHog7m%2BlGQSR1f9am6abiLlUK4BwZX6d3cVCz6U1cHJpIahAh0AjRiaMFQTtq%2BFIMu1joy1YTUFZD7x5KlpMJuXoXBRP%2BHLIGLJXV6kLWWpjkZxLQYs1qWTjjH9Q7TsreHZ4cQnPSCwy6eQ8Qs%2B%2FNmuqCXXG8klK9ZJcaCcKpxjTQFL4Ie0vKyX1ZW36jOkw8FeFWBehaOJJmnaXEfmqRri%2FWaZgWGTOQBytkairXZ3n6fuQ3L840pfjNQ88wXx17I47CMuEgi1Z87%2F4WzsKw5hw6jva%2FXukkZ8kRlByopFFk2vwbx7KWpW1h3QzruDDBt%2F%2FSBjqkAW%2BO6Elh%2BpPSqeiB2MBMLl%2FQ7AZ6XaTHAjTWcS%2BMt8iY8NrJx1dcwi2leitly3wwgRM6L8vrlNV8vCIwfrJEbx3ruiSdsVo6bVjUzgQxOIGxv3Yxe4xFZyxnGpJ6kBuUUwEfV9R9zU%2Fgxhq72BdLv%2BMQo4DiW9LudelaHaL9%2F32onQXywZ%2FGQ430kwZOePJSP%2FqycH6EWfgl5PbmLqJh%2Fp5vwLT3&X-Amz-Signature=3258e4a1cb4abd4ad024c4764b00d1b999648ec185c075d23a4b5339e5ccaf99&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


gain Ji a lot manager alerts，可以看到 AlertManager

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/361d1fbe-fa2b-4784-89b1-9b3b6fb4551e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5A5VRUI%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231626Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDT4zG%2FH9ulxQ3ry4Hs424I3ffc8P6%2BjPF2ogCyaYbmzwIhAJMi3UZ%2BnVU08%2F4lgjRKbQktbx1l0xLObi0K%2BsaO%2BHTCKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzjsyCwZxlqkFKxpaYq3AM%2FqaKQiD5HQYkGphHm6Hy%2BmedQ1mmVSoRB3QGTbb02jhUTbJktWHnOIyQQsCJYm%2BlWqO6JYDxvZmK2GxulqMqdCDh9LoKWUXmc58zRUF4o4MFtsn5IyCoG8JA9UOtjjD1UvkfLsvV43CtHExIGRswrZ0PRMVqx47qoebdJXHkaeQDRy8AeVdewg60hcI8e2kOQO0WGY0gwQ2%2F%2BiKH2M6S65xi1E0kwaYRY90T4eTEFCJtP2j13XPM5FgLaiSZAvXOSG7MJfPdRmpiVolTR94QMUjSWS9%2B1%2FpKb9%2FXlgk7lyRm7H3U8jSjSdmasskSLHog7m%2BlGQSR1f9am6abiLlUK4BwZX6d3cVCz6U1cHJpIahAh0AjRiaMFQTtq%2BFIMu1joy1YTUFZD7x5KlpMJuXoXBRP%2BHLIGLJXV6kLWWpjkZxLQYs1qWTjjH9Q7TsreHZ4cQnPSCwy6eQ8Qs%2B%2FNmuqCXXG8klK9ZJcaCcKpxjTQFL4Ie0vKyX1ZW36jOkw8FeFWBehaOJJmnaXEfmqRri%2FWaZgWGTOQBytkairXZ3n6fuQ3L840pfjNQ88wXx17I47CMuEgi1Z87%2F4WzsKw5hw6jva%2FXukkZ8kRlByopFFk2vwbx7KWpW1h3QzruDDBt%2F%2FSBjqkAW%2BO6Elh%2BpPSqeiB2MBMLl%2FQ7AZ6XaTHAjTWcS%2BMt8iY8NrJx1dcwi2leitly3wwgRM6L8vrlNV8vCIwfrJEbx3ruiSdsVo6bVjUzgQxOIGxv3Yxe4xFZyxnGpJ6kBuUUwEfV9R9zU%2Fgxhq72BdLv%2BMQo4DiW9LudelaHaL9%2F32onQXywZ%2FGQ430kwZOePJSP%2FqycH6EWfgl5PbmLqJh%2Fp5vwLT3&X-Amz-Signature=3b5955f8061bb24876ebae00e2966bdf279c651f9c92a670be9e00679d9f27c4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

已经收到了这条告警。前往我的邮箱刷新

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/09328450-bd59-4839-9c4b-6c79206ce4ad/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5A5VRUI%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231626Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDT4zG%2FH9ulxQ3ry4Hs424I3ffc8P6%2BjPF2ogCyaYbmzwIhAJMi3UZ%2BnVU08%2F4lgjRKbQktbx1l0xLObi0K%2BsaO%2BHTCKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzjsyCwZxlqkFKxpaYq3AM%2FqaKQiD5HQYkGphHm6Hy%2BmedQ1mmVSoRB3QGTbb02jhUTbJktWHnOIyQQsCJYm%2BlWqO6JYDxvZmK2GxulqMqdCDh9LoKWUXmc58zRUF4o4MFtsn5IyCoG8JA9UOtjjD1UvkfLsvV43CtHExIGRswrZ0PRMVqx47qoebdJXHkaeQDRy8AeVdewg60hcI8e2kOQO0WGY0gwQ2%2F%2BiKH2M6S65xi1E0kwaYRY90T4eTEFCJtP2j13XPM5FgLaiSZAvXOSG7MJfPdRmpiVolTR94QMUjSWS9%2B1%2FpKb9%2FXlgk7lyRm7H3U8jSjSdmasskSLHog7m%2BlGQSR1f9am6abiLlUK4BwZX6d3cVCz6U1cHJpIahAh0AjRiaMFQTtq%2BFIMu1joy1YTUFZD7x5KlpMJuXoXBRP%2BHLIGLJXV6kLWWpjkZxLQYs1qWTjjH9Q7TsreHZ4cQnPSCwy6eQ8Qs%2B%2FNmuqCXXG8klK9ZJcaCcKpxjTQFL4Ie0vKyX1ZW36jOkw8FeFWBehaOJJmnaXEfmqRri%2FWaZgWGTOQBytkairXZ3n6fuQ3L840pfjNQ88wXx17I47CMuEgi1Z87%2F4WzsKw5hw6jva%2FXukkZ8kRlByopFFk2vwbx7KWpW1h3QzruDDBt%2F%2FSBjqkAW%2BO6Elh%2BpPSqeiB2MBMLl%2FQ7AZ6XaTHAjTWcS%2BMt8iY8NrJx1dcwi2leitly3wwgRM6L8vrlNV8vCIwfrJEbx3ruiSdsVo6bVjUzgQxOIGxv3Yxe4xFZyxnGpJ6kBuUUwEfV9R9zU%2Fgxhq72BdLv%2BMQo4DiW9LudelaHaL9%2F32onQXywZ%2FGQ430kwZOePJSP%2FqycH6EWfgl5PbmLqJh%2Fp5vwLT3&X-Amz-Signature=969622a7aedc17f04e79320784d7e724de75d9d2579c45c5feba06240f842407&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

，可以看到发信箱里面已经有了这样的一个告警，并且把 annotation 里面的模板给填充了。ok。通过刚刚的讲解，我们不难发现， prometheus server 可以灵活的去配置告警规则，说满足什么样的条件才推送告警。而 AlertManager 它提供了丰富的告警渠道，可以把告警推送到各个地方，比方邮箱。


另外，我们还可以针对指定的告警设置静默。点击 silence，选择想要静默的时间。静默 4 小时creator，写上我的名字，写上备注。告警太频繁，正在解决中。静默 4 小时crates，这样在 4 小时之内，我们就不会收到重复的告警了。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/fdda2413-be90-441d-8d30-4ce8928059c7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5A5VRUI%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231626Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDT4zG%2FH9ulxQ3ry4Hs424I3ffc8P6%2BjPF2ogCyaYbmzwIhAJMi3UZ%2BnVU08%2F4lgjRKbQktbx1l0xLObi0K%2BsaO%2BHTCKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzjsyCwZxlqkFKxpaYq3AM%2FqaKQiD5HQYkGphHm6Hy%2BmedQ1mmVSoRB3QGTbb02jhUTbJktWHnOIyQQsCJYm%2BlWqO6JYDxvZmK2GxulqMqdCDh9LoKWUXmc58zRUF4o4MFtsn5IyCoG8JA9UOtjjD1UvkfLsvV43CtHExIGRswrZ0PRMVqx47qoebdJXHkaeQDRy8AeVdewg60hcI8e2kOQO0WGY0gwQ2%2F%2BiKH2M6S65xi1E0kwaYRY90T4eTEFCJtP2j13XPM5FgLaiSZAvXOSG7MJfPdRmpiVolTR94QMUjSWS9%2B1%2FpKb9%2FXlgk7lyRm7H3U8jSjSdmasskSLHog7m%2BlGQSR1f9am6abiLlUK4BwZX6d3cVCz6U1cHJpIahAh0AjRiaMFQTtq%2BFIMu1joy1YTUFZD7x5KlpMJuXoXBRP%2BHLIGLJXV6kLWWpjkZxLQYs1qWTjjH9Q7TsreHZ4cQnPSCwy6eQ8Qs%2B%2FNmuqCXXG8klK9ZJcaCcKpxjTQFL4Ie0vKyX1ZW36jOkw8FeFWBehaOJJmnaXEfmqRri%2FWaZgWGTOQBytkairXZ3n6fuQ3L840pfjNQ88wXx17I47CMuEgi1Z87%2F4WzsKw5hw6jva%2FXukkZ8kRlByopFFk2vwbx7KWpW1h3QzruDDBt%2F%2FSBjqkAW%2BO6Elh%2BpPSqeiB2MBMLl%2FQ7AZ6XaTHAjTWcS%2BMt8iY8NrJx1dcwi2leitly3wwgRM6L8vrlNV8vCIwfrJEbx3ruiSdsVo6bVjUzgQxOIGxv3Yxe4xFZyxnGpJ6kBuUUwEfV9R9zU%2Fgxhq72BdLv%2BMQo4DiW9LudelaHaL9%2F32onQXywZ%2FGQ430kwZOePJSP%2FqycH6EWfgl5PbmLqJh%2Fp5vwLT3&X-Amz-Signature=1ae448834a48526e889c6e2192a6ccf121d90e5261af10dc20390ee542199c3b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


OK，这是 prometheus 的告警，利用 prometheus 以及 AlertManager 这个组合拳，就可以实现非常灵活的告警了。采用这样的搭配，可以满足我们绝大多数项目的需求。但是如果我们的告警需求特别的苛刻，连 AlertManager 也无法实现的话，该怎么办？不要忘记 AlertManager 它支持基于 Webhook 的 receiver，我们可以把 receiver 配置成 Webhook，自己去实现 URL 对应的API

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/8eaa5253-2e60-491d-be6f-8899cf7c039b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5A5VRUI%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231626Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDT4zG%2FH9ulxQ3ry4Hs424I3ffc8P6%2BjPF2ogCyaYbmzwIhAJMi3UZ%2BnVU08%2F4lgjRKbQktbx1l0xLObi0K%2BsaO%2BHTCKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzjsyCwZxlqkFKxpaYq3AM%2FqaKQiD5HQYkGphHm6Hy%2BmedQ1mmVSoRB3QGTbb02jhUTbJktWHnOIyQQsCJYm%2BlWqO6JYDxvZmK2GxulqMqdCDh9LoKWUXmc58zRUF4o4MFtsn5IyCoG8JA9UOtjjD1UvkfLsvV43CtHExIGRswrZ0PRMVqx47qoebdJXHkaeQDRy8AeVdewg60hcI8e2kOQO0WGY0gwQ2%2F%2BiKH2M6S65xi1E0kwaYRY90T4eTEFCJtP2j13XPM5FgLaiSZAvXOSG7MJfPdRmpiVolTR94QMUjSWS9%2B1%2FpKb9%2FXlgk7lyRm7H3U8jSjSdmasskSLHog7m%2BlGQSR1f9am6abiLlUK4BwZX6d3cVCz6U1cHJpIahAh0AjRiaMFQTtq%2BFIMu1joy1YTUFZD7x5KlpMJuXoXBRP%2BHLIGLJXV6kLWWpjkZxLQYs1qWTjjH9Q7TsreHZ4cQnPSCwy6eQ8Qs%2B%2FNmuqCXXG8klK9ZJcaCcKpxjTQFL4Ie0vKyX1ZW36jOkw8FeFWBehaOJJmnaXEfmqRri%2FWaZgWGTOQBytkairXZ3n6fuQ3L840pfjNQ88wXx17I47CMuEgi1Z87%2F4WzsKw5hw6jva%2FXukkZ8kRlByopFFk2vwbx7KWpW1h3QzruDDBt%2F%2FSBjqkAW%2BO6Elh%2BpPSqeiB2MBMLl%2FQ7AZ6XaTHAjTWcS%2BMt8iY8NrJx1dcwi2leitly3wwgRM6L8vrlNV8vCIwfrJEbx3ruiSdsVo6bVjUzgQxOIGxv3Yxe4xFZyxnGpJ6kBuUUwEfV9R9zU%2Fgxhq72BdLv%2BMQo4DiW9LudelaHaL9%2F32onQXywZ%2FGQ430kwZOePJSP%2FqycH6EWfgl5PbmLqJh%2Fp5vwLT3&X-Amz-Signature=fcd9ba435b71b032eb7140402f73e756eb08e659d8bfd9932e16f3ea1e7d7525&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

在 API 里面，我们可以完全按照告警需求去实现。不管是什么样的告警需求，我们都能够满足了。OK，这节课就到这里，谢谢大家。



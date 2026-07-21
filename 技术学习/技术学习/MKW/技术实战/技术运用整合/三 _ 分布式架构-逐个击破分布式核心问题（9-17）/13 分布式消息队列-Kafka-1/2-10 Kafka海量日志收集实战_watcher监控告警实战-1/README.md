---
title: 2-10 Kafka海量日志收集实战_watcher监控告警实战-1
---

# 2-10 Kafka海量日志收集实战_watcher监控告警实战-1

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/48bf846d-c863-4602-97fa-baa61ab67e42/SCR-20240807-hmgj.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663EFJUKNK%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCVog4afe8KSvFm4m16q2U2By2xf0NpXt8SwcXgeZFoWAIgalRgJKSHvlx3yvL%2FaivYpB6R8VpJCXS51ylzDzp8SkcqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGMj6ZofZccPjfyTiSrcA8dWLF9Co4mKkMn%2B529nU%2B9yrg9f32sUaEENJ33W4ypicksI2uTL%2BN6Q5KVJEYDbQw6NtZHJasFC2GVVz4VO3bbVOlJKEpZ6AKHCdQUW2T%2B44i%2BPWwY0USNJgVcV8NGfYAIUQG4pwZ0Ny53tODtM4cUofascxYOZSszv507jjHdUiB4rgY71OFCdLWZjCp73ToeZ1zqZxpyOPZqWBmaWz9IdirZTStLu%2FVoBiObHkVAElupLlr%2BHwXFPhUhfj05JEIW2SsGapJxsmHQJr5eBEPB%2FRSsvhZJF%2BbCYwHWmRiWpulsJtP7gwJhVlOz3IwFCu1bXtiyfhhtiaGwZipiLRiRzhQdrG%2BetBDenqE8%2BGywh0TMg3z6rYWirUzn4qJU3LH44myv9GD8Y9LgQuUfubMdhB2XJLvEa3dEmrEeaxiUGwulrbaDmiPE4eFbkcNpfCDZHHiW4nShXWLbH1o%2BKiN%2B32xlvHbiymeAywt518GEnwtftxvYsK2FSwtv16Uez5DYozrSLHdFn93iT2lGF1XYgBVynrDkbenWXaZYR9jb5%2B3n3SrtRVEx9tlz9eWM8A8F%2BPLmmdSKrJcFN00bZjrqxxQFi2F7yMdLm9wA4qSr8rV8L9AdUMUklUp3%2FMI66%2F9IGOqUBfUfzYU%2Fljem1pxWB1FWiRLaL0zXsreHv68f8rD3GYY5CNnx%2B1Pq7TCOQtddtkjW0ISDZ6NIBN94G202Wt8mq4ma8S%2FsBJPOPhmRV70cEPOdqQUUmbokxizenYCfRNICqM1BuNE8Qgb84DLBrQRYlsrbeMfQ7FbXBBdHDshlK4kwWFB%2B9PKEq3fG6FC7CpYeM0Pi6pdcDJok2N8Grx3q3y%2BAFYdE8&X-Amz-Signature=630570f39e863d49e08698e55ef78dbcea26c7134f12b30db83b941cad04c2c1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/68deca4b-0d20-4585-a9ca-9bb5fccfac7c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663EFJUKNK%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCVog4afe8KSvFm4m16q2U2By2xf0NpXt8SwcXgeZFoWAIgalRgJKSHvlx3yvL%2FaivYpB6R8VpJCXS51ylzDzp8SkcqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGMj6ZofZccPjfyTiSrcA8dWLF9Co4mKkMn%2B529nU%2B9yrg9f32sUaEENJ33W4ypicksI2uTL%2BN6Q5KVJEYDbQw6NtZHJasFC2GVVz4VO3bbVOlJKEpZ6AKHCdQUW2T%2B44i%2BPWwY0USNJgVcV8NGfYAIUQG4pwZ0Ny53tODtM4cUofascxYOZSszv507jjHdUiB4rgY71OFCdLWZjCp73ToeZ1zqZxpyOPZqWBmaWz9IdirZTStLu%2FVoBiObHkVAElupLlr%2BHwXFPhUhfj05JEIW2SsGapJxsmHQJr5eBEPB%2FRSsvhZJF%2BbCYwHWmRiWpulsJtP7gwJhVlOz3IwFCu1bXtiyfhhtiaGwZipiLRiRzhQdrG%2BetBDenqE8%2BGywh0TMg3z6rYWirUzn4qJU3LH44myv9GD8Y9LgQuUfubMdhB2XJLvEa3dEmrEeaxiUGwulrbaDmiPE4eFbkcNpfCDZHHiW4nShXWLbH1o%2BKiN%2B32xlvHbiymeAywt518GEnwtftxvYsK2FSwtv16Uez5DYozrSLHdFn93iT2lGF1XYgBVynrDkbenWXaZYR9jb5%2B3n3SrtRVEx9tlz9eWM8A8F%2BPLmmdSKrJcFN00bZjrqxxQFi2F7yMdLm9wA4qSr8rV8L9AdUMUklUp3%2FMI66%2F9IGOqUBfUfzYU%2Fljem1pxWB1FWiRLaL0zXsreHv68f8rD3GYY5CNnx%2B1Pq7TCOQtddtkjW0ISDZ6NIBN94G202Wt8mq4ma8S%2FsBJPOPhmRV70cEPOdqQUUmbokxizenYCfRNICqM1BuNE8Qgb84DLBrQRYlsrbeMfQ7FbXBBdHDshlK4kwWFB%2B9PKEq3fG6FC7CpYeM0Pi6pdcDJok2N8Grx3q3y%2BAFYdE8&X-Amz-Signature=827989080ec5e7a28b7571d042458fc268f8b60616f2e0b7296009169a0d3d95&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

OK 小伙伴们大家好，那这节课我们继续往下去讲。上节课我们已经把数据存储到了 elastic search 中。那这节课我们来看一看如何去做监控告警。说白了就是说我们要 error 日志级别以上的数据，我们要推送告警，最终推送到我们自己的这个用户的手里。所以说老师把整个的流程和思路梳理清楚，然后一些细节大家就可以自己去做了。


OK 那现在我们先把对应着的左侧这个菜单，我们先去点开我们的这个 DEV tools av 兔子里边。大家可以看到老师已经写好了一段最简单的脚本，这个脚本就是我们的 watcher 脚本。那对于 water 这个东西它是干什么用的？我在具体的这个文档里边已经给大家描述了，所以说大家就可以去看我给你们提供的文图资料，你看完了之后再回来听我这课。Ok.那他能做什么事情，他就能够去抓取某一个索引里边关键的一些数据信息，然后抓取出来做告警的。所以说 wash 这个东西说白了就是 elastic search 集成起来了，然后可以去做一些日志的这么一些告警。但我们在这里看一下，我现在不是每隔 10 分钟，我现在再把它最大化一下，我现在是每隔 5 秒钟。


我说我看一下 input 里的数据， input 就是我创建一个 watcher 那 watcher API 老师在文档里都说了，我就是杠 X pack watcher 然后对于这个 watcher 我给它起个名字叫做 aerolog 杠 watcher error log watcher 就我给它起个名字，然后我要做什么事情呢？你看我要做的事情其实你可以写得好一点，就是你可以这样去做 aerolock 杠 collector 杠 watcher 就是说你可以见名之意说这个是 L log 错误日志，然后什么服务就是 collector 这个服务里面的什么 watcher 那这个 wash 干什么？首先看第一点，这里边有个 trigger 触发器，触发器里边有个 schedule 这什么意思？就是说我轮询着每五秒钟我要做一下这个事情。你可以理解为就是一个定时任务，然后定时任务干什么呢？ input 就是输入项，这里面好多括号，大家千万别懵逼。每 5 秒钟做的事情很简单，就是去查 ES 的指定的索引。

```java

=====在 kibana 的[开发工具]上 执行此 watcher API =====================
## 创建一个watcher,比如定义一个trigger 每个10s钟看一下input里的数据
## 创建一个watcher,比如定义一个trigger 每个5s钟看一下input里的数据

PUT _xpack/watcher/watch/error_log_collector_watcher
{
  "trigger": {
    "schedule": {
      "interval": "5s"
    }
  },
  "input": {
    "search": {
      "request": {
        "indices": ["<error_log_collector-{now+8h/d}>"],
        "body": {
          "size": 0,
          "query": {
            "bool": {
              "must": [
                  {
                    "term": {"level": "ERROR"}
                  }
              ],
              "filter": {
                "range": {
                    "currentDateTime": {
                    "gt": "now-30s" , "lt": "now"
                  }
                }
              } 
            }
          }
        }
      }
    }
  },

  "condition": {
    "compare": {
      "ctx.payload.hits.total": {
        "gt": 0
      }
    }
  },

  "transform": {
    "search": {
      "request": {
        "indices": ["<error-log-collector-{now+8h/d}>"],
        "body": {
          "size": 1,
          "query": {
            "bool": {
              "must": [
                  {
                    "term": {"level": "ERROR"}
                  }
              ],
              "filter": {
                "range": {
                    "currentDateTime": {
                    "gt": "now-30s" , "lt": "now"
                  }
                }
              } 
            }
          },
          "sort": [
            {
                "currentDateTime": {
                    "order": "desc"
                }
            }
          ]
        }
      }
    }
  },
  "actions": {
    "test_error": {
      "webhook" : {
        "method" : "POST",
        "url" : "http://192.168.11.31:8001/accurateWatch",
        "body" : "{\"title\": \"异常错误告警\", \"applicationName\": \"{{#ctx.payload.hits.hits}}{{_source.applicationName}}{{/ctx.payload.hits.hits}}\", \"level\":\"告警级别P1\", \"body\": \"{{#ctx.payload.hits.hits}}{{_source.messageInfo}}{{/ctx.payload.hits.hits}}\", \"executionTime\": \"{{#ctx.payload.hits.hits}}{{_source.currentDateTime}}{{/ctx.payload.hits.hits}}\"}"
      }
    }
 }
}



=====================================================操作命令==================================
# 查看一个watcher
# 
GET _xpack/watcher/watch/error_log_collector_watcher


#删除一个watcher
DELETE _xpack/watcher/watch/error_log_collector_watcher

#执行watcher
# POST _xpack/watcher/watch/error_log_collector_watcher/_execute

#查看执行结果
GET /.watcher-history*/_search?pretty
{
  "sort" : [
    { "result.execution_time" : "desc" }
  ],
  "query": {
    "match": {
      "watch_id": "error_log_collector_watcher"
    }
  }
}

GET error-log-collector-2019.09.18/_search?size=10
{

  "query": {
    "match": {
      "level": "ERROR"
    }
  }
  ,
  "sort": [
    {
        "currentDateTime": {
            "order": "desc"
        }
    }
  ] 
}


GET error-log-collector-2019.09.18/_search?size=10
{

  "query": {
    "match": {
      "level": "ERROR"
    }
  }
  ,
  "sort": [
    {
        "currentDateTime": {
            "order": "desc"
        }
    }
  ] 
}
```


这个索引是什么？是 error log 杠 collector 后面是你看我这里面写的是 no 加上 8 小时，然后杠 D 代表什么意思？因为我们是东八区还是那个问题，所以说我们要加 8 小时才能是北京时间，因为它比我们北京时间慢 8 小时，然后 body size 这里面是0，我们不查数据，我们就去 query 里边具体内容 turn 匹配 error 的日志，就是你的日级别是 error 的话，我就会给你抓取出来怎么抓取？说 range 这里边有一个过滤当前的这个 current 对 time 我只抓取当前时间减去 30 秒，就是说当前时间减去 30 秒，到当前时间就是提前 30 秒。 30 秒以内的日志输出的。如果是 L 的，那我给你抓出来就是做这个事情。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/1d1ca772-c534-4bc2-b750-40c28aa5d8b0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663EFJUKNK%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCVog4afe8KSvFm4m16q2U2By2xf0NpXt8SwcXgeZFoWAIgalRgJKSHvlx3yvL%2FaivYpB6R8VpJCXS51ylzDzp8SkcqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGMj6ZofZccPjfyTiSrcA8dWLF9Co4mKkMn%2B529nU%2B9yrg9f32sUaEENJ33W4ypicksI2uTL%2BN6Q5KVJEYDbQw6NtZHJasFC2GVVz4VO3bbVOlJKEpZ6AKHCdQUW2T%2B44i%2BPWwY0USNJgVcV8NGfYAIUQG4pwZ0Ny53tODtM4cUofascxYOZSszv507jjHdUiB4rgY71OFCdLWZjCp73ToeZ1zqZxpyOPZqWBmaWz9IdirZTStLu%2FVoBiObHkVAElupLlr%2BHwXFPhUhfj05JEIW2SsGapJxsmHQJr5eBEPB%2FRSsvhZJF%2BbCYwHWmRiWpulsJtP7gwJhVlOz3IwFCu1bXtiyfhhtiaGwZipiLRiRzhQdrG%2BetBDenqE8%2BGywh0TMg3z6rYWirUzn4qJU3LH44myv9GD8Y9LgQuUfubMdhB2XJLvEa3dEmrEeaxiUGwulrbaDmiPE4eFbkcNpfCDZHHiW4nShXWLbH1o%2BKiN%2B32xlvHbiymeAywt518GEnwtftxvYsK2FSwtv16Uez5DYozrSLHdFn93iT2lGF1XYgBVynrDkbenWXaZYR9jb5%2B3n3SrtRVEx9tlz9eWM8A8F%2BPLmmdSKrJcFN00bZjrqxxQFi2F7yMdLm9wA4qSr8rV8L9AdUMUklUp3%2FMI66%2F9IGOqUBfUfzYU%2Fljem1pxWB1FWiRLaL0zXsreHv68f8rD3GYY5CNnx%2B1Pq7TCOQtddtkjW0ISDZ6NIBN94G202Wt8mq4ma8S%2FsBJPOPhmRV70cEPOdqQUUmbokxizenYCfRNICqM1BuNE8Qgb84DLBrQRYlsrbeMfQ7FbXBBdHDshlK4kwWFB%2B9PKEq3fG6FC7CpYeM0Pi6pdcDJok2N8Grx3q3y%2BAFYdE8&X-Amz-Signature=c02f817367db2f9c3411cbedf5f9dc9202e8b96c3b5da8404de075c87ea5cb5b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/476ced7f-44ef-418a-a1f6-36565d3bdae6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663EFJUKNK%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCVog4afe8KSvFm4m16q2U2By2xf0NpXt8SwcXgeZFoWAIgalRgJKSHvlx3yvL%2FaivYpB6R8VpJCXS51ylzDzp8SkcqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGMj6ZofZccPjfyTiSrcA8dWLF9Co4mKkMn%2B529nU%2B9yrg9f32sUaEENJ33W4ypicksI2uTL%2BN6Q5KVJEYDbQw6NtZHJasFC2GVVz4VO3bbVOlJKEpZ6AKHCdQUW2T%2B44i%2BPWwY0USNJgVcV8NGfYAIUQG4pwZ0Ny53tODtM4cUofascxYOZSszv507jjHdUiB4rgY71OFCdLWZjCp73ToeZ1zqZxpyOPZqWBmaWz9IdirZTStLu%2FVoBiObHkVAElupLlr%2BHwXFPhUhfj05JEIW2SsGapJxsmHQJr5eBEPB%2FRSsvhZJF%2BbCYwHWmRiWpulsJtP7gwJhVlOz3IwFCu1bXtiyfhhtiaGwZipiLRiRzhQdrG%2BetBDenqE8%2BGywh0TMg3z6rYWirUzn4qJU3LH44myv9GD8Y9LgQuUfubMdhB2XJLvEa3dEmrEeaxiUGwulrbaDmiPE4eFbkcNpfCDZHHiW4nShXWLbH1o%2BKiN%2B32xlvHbiymeAywt518GEnwtftxvYsK2FSwtv16Uez5DYozrSLHdFn93iT2lGF1XYgBVynrDkbenWXaZYR9jb5%2B3n3SrtRVEx9tlz9eWM8A8F%2BPLmmdSKrJcFN00bZjrqxxQFi2F7yMdLm9wA4qSr8rV8L9AdUMUklUp3%2FMI66%2F9IGOqUBfUfzYU%2Fljem1pxWB1FWiRLaL0zXsreHv68f8rD3GYY5CNnx%2B1Pq7TCOQtddtkjW0ISDZ6NIBN94G202Wt8mq4ma8S%2FsBJPOPhmRV70cEPOdqQUUmbokxizenYCfRNICqM1BuNE8Qgb84DLBrQRYlsrbeMfQ7FbXBBdHDshlK4kwWFB%2B9PKEq3fG6FC7CpYeM0Pi6pdcDJok2N8Grx3q3y%2BAFYdE8&X-Amz-Signature=d14420a6de3ef91f3e2ef6421c47461831d40d174e53ed657e86fe364aa87782&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

当然这个事情做完了之后，然后接下来有个 condition 看见了这个就是 hits 就表示你 hits 斯命中了。这个 G T 表示大于0，只要是大于 0 条，那我就帮你去做 his 就是已经命中了。然后下面这个 transfer 其实就是做一个这个排序，可以做一些细粒度的。其实这个代码这块的脚本跟上面脚本差不多，但是你必须要写，就是你可以去上面这块只是做一个查询，有没有命命中。下面这块 transfer 是真正把数据查出来，把数据查出来之后是 L 的你看这个有条件都是一样的，就重写一遍，然后做了一个排序，这上面还是没有排序的。


然后下面这个 transfer 相当于把数据真正查出来之后干什么事情呢？这里边有一个 action 这个 action 就是具体做的事情，我具体做的事情。对于这个 watcher 它可以做很多事情，比如说发邮件，比如说推手机短信，或者做一些其他的事情都可以。那我们在这里我是把抓取出来的数据给他发送 POS 请求到这个地址看见了吗？我抓取出来的数据发送到31。这个服务器其实 31 是哪个服务器？ 31 就是我们刚才写的那个应用程序，我再给它发回去，然后访问这个地址看见了吗？ body 内容是什么？ body 内容里面有这个语法，我们在对应着 watch 里边老师已经讲过了，我直接就说 application name 就是你的应用服务名称是什么，然后以及你的 level 你的级别是什么。这个级别其实可以动态的，比如说有些关键的内容，我可以指定这个级别是 p1p2 p3 告警级别。 body 就是你具体什么样的错误？我把 master info 拿出来，然后以及这个 excuse 的 time 是什么。 excuse time 就是我们的 parent day time 就是当前这个告警在我们日志里打的时间，就是出现这个问题的当前时间是什么时间点。那这样的话它就相当于告警抓取出来数据，会向这个服务器的这个地址去发送请求，然后把数据发过去，就是做这个事情。小伙伴们这回应该听懂了吧。


好，听懂了之后，那接下来我们要做的事情很简单是什么呢？就是要开发这一块小程序了，我们这里边叫做 culture water 这个 API 好，那其实我们就搞一个 pose 请求，然后去从这个里边去写一个这个 spring MVC 的小程序就可以了，然后把这个实体定义一下。那在这里打开我们自己的工具，然后我在这里起一个 class 我们这个 class 就叫做 watcher controller 吧。


 watcher controller 让小伙伴们看到这个效果。 water controller 里边我们其实很简单，我们在这里边写好了 request mapping 这个 request mapping 的 value 是什么呢？ value 就是刚才老师给你看到的这个杠，它这个地址的值跟我们的这个里边的值一定是相匹配的，端口也匹配。
8001。 Ok. 然后接下来我们再做其他的事情，比如说 rest controller 然后接下来我们来写这个方法，我说 public 然后 string 返回是 string 无所谓的。然后 watch 就给它起个名字，watch这个 watcher 里边要传什么样的数据呢？同学们请看这个 watcher 里面传的数据。我这里面 body 里面已经封装好了，它就是有 title application name level 以及 body 这几个字段，还有什么？还有 execute time 这几个字段。就说我们干脆搞一个对象就好了，搞一个对象，这个对象我就不在这里写了，我直接把它 copy 过来，然后我们一起快速的去看到这个效果。比如说老师在这里去创建一个 entity 然后把它粘过来。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/a61abac7-9dc6-4137-b8fd-8a4269212a06/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663EFJUKNK%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCVog4afe8KSvFm4m16q2U2By2xf0NpXt8SwcXgeZFoWAIgalRgJKSHvlx3yvL%2FaivYpB6R8VpJCXS51ylzDzp8SkcqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGMj6ZofZccPjfyTiSrcA8dWLF9Co4mKkMn%2B529nU%2B9yrg9f32sUaEENJ33W4ypicksI2uTL%2BN6Q5KVJEYDbQw6NtZHJasFC2GVVz4VO3bbVOlJKEpZ6AKHCdQUW2T%2B44i%2BPWwY0USNJgVcV8NGfYAIUQG4pwZ0Ny53tODtM4cUofascxYOZSszv507jjHdUiB4rgY71OFCdLWZjCp73ToeZ1zqZxpyOPZqWBmaWz9IdirZTStLu%2FVoBiObHkVAElupLlr%2BHwXFPhUhfj05JEIW2SsGapJxsmHQJr5eBEPB%2FRSsvhZJF%2BbCYwHWmRiWpulsJtP7gwJhVlOz3IwFCu1bXtiyfhhtiaGwZipiLRiRzhQdrG%2BetBDenqE8%2BGywh0TMg3z6rYWirUzn4qJU3LH44myv9GD8Y9LgQuUfubMdhB2XJLvEa3dEmrEeaxiUGwulrbaDmiPE4eFbkcNpfCDZHHiW4nShXWLbH1o%2BKiN%2B32xlvHbiymeAywt518GEnwtftxvYsK2FSwtv16Uez5DYozrSLHdFn93iT2lGF1XYgBVynrDkbenWXaZYR9jb5%2B3n3SrtRVEx9tlz9eWM8A8F%2BPLmmdSKrJcFN00bZjrqxxQFi2F7yMdLm9wA4qSr8rV8L9AdUMUklUp3%2FMI66%2F9IGOqUBfUfzYU%2Fljem1pxWB1FWiRLaL0zXsreHv68f8rD3GYY5CNnx%2B1Pq7TCOQtddtkjW0ISDZ6NIBN94G202Wt8mq4ma8S%2FsBJPOPhmRV70cEPOdqQUUmbokxizenYCfRNICqM1BuNE8Qgb84DLBrQRYlsrbeMfQ7FbXBBdHDshlK4kwWFB%2B9PKEq3fG6FC7CpYeM0Pi6pdcDJok2N8Grx3q3y%2BAFYdE8&X-Amz-Signature=caa04d3bba8986eacafb4b6df0dab1e67bb916df1e102b992933e5dca9f74379&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

好同学们请看就这几个字段有 title 有 execute time 执行时间，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/10df4d0a-aa20-4590-8d7d-204fa352c126/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663EFJUKNK%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCVog4afe8KSvFm4m16q2U2By2xf0NpXt8SwcXgeZFoWAIgalRgJKSHvlx3yvL%2FaivYpB6R8VpJCXS51ylzDzp8SkcqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGMj6ZofZccPjfyTiSrcA8dWLF9Co4mKkMn%2B529nU%2B9yrg9f32sUaEENJ33W4ypicksI2uTL%2BN6Q5KVJEYDbQw6NtZHJasFC2GVVz4VO3bbVOlJKEpZ6AKHCdQUW2T%2B44i%2BPWwY0USNJgVcV8NGfYAIUQG4pwZ0Ny53tODtM4cUofascxYOZSszv507jjHdUiB4rgY71OFCdLWZjCp73ToeZ1zqZxpyOPZqWBmaWz9IdirZTStLu%2FVoBiObHkVAElupLlr%2BHwXFPhUhfj05JEIW2SsGapJxsmHQJr5eBEPB%2FRSsvhZJF%2BbCYwHWmRiWpulsJtP7gwJhVlOz3IwFCu1bXtiyfhhtiaGwZipiLRiRzhQdrG%2BetBDenqE8%2BGywh0TMg3z6rYWirUzn4qJU3LH44myv9GD8Y9LgQuUfubMdhB2XJLvEa3dEmrEeaxiUGwulrbaDmiPE4eFbkcNpfCDZHHiW4nShXWLbH1o%2BKiN%2B32xlvHbiymeAywt518GEnwtftxvYsK2FSwtv16Uez5DYozrSLHdFn93iT2lGF1XYgBVynrDkbenWXaZYR9jb5%2B3n3SrtRVEx9tlz9eWM8A8F%2BPLmmdSKrJcFN00bZjrqxxQFi2F7yMdLm9wA4qSr8rV8L9AdUMUklUp3%2FMI66%2F9IGOqUBfUfzYU%2Fljem1pxWB1FWiRLaL0zXsreHv68f8rD3GYY5CNnx%2B1Pq7TCOQtddtkjW0ISDZ6NIBN94G202Wt8mq4ma8S%2FsBJPOPhmRV70cEPOdqQUUmbokxizenYCfRNICqM1BuNE8Qgb84DLBrQRYlsrbeMfQ7FbXBBdHDshlK4kwWFB%2B9PKEq3fG6FC7CpYeM0Pi6pdcDJok2N8Grx3q3y%2BAFYdE8&X-Amz-Signature=de02cfd35fe84781707b1d144c2dbbe0cc64e306ad65e82e3f7081822cdb568b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

包括你的应用服务的名称以及告警的 level 以及你告警内容是什么。有了这个对象以后，我们可以通过它直接搞一个什么呢？ Response request body. 直接搞一个 request body 就可以了，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/85540196-3884-4bfb-98e8-9e8aec097ed8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663EFJUKNK%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCVog4afe8KSvFm4m16q2U2By2xf0NpXt8SwcXgeZFoWAIgalRgJKSHvlx3yvL%2FaivYpB6R8VpJCXS51ylzDzp8SkcqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGMj6ZofZccPjfyTiSrcA8dWLF9Co4mKkMn%2B529nU%2B9yrg9f32sUaEENJ33W4ypicksI2uTL%2BN6Q5KVJEYDbQw6NtZHJasFC2GVVz4VO3bbVOlJKEpZ6AKHCdQUW2T%2B44i%2BPWwY0USNJgVcV8NGfYAIUQG4pwZ0Ny53tODtM4cUofascxYOZSszv507jjHdUiB4rgY71OFCdLWZjCp73ToeZ1zqZxpyOPZqWBmaWz9IdirZTStLu%2FVoBiObHkVAElupLlr%2BHwXFPhUhfj05JEIW2SsGapJxsmHQJr5eBEPB%2FRSsvhZJF%2BbCYwHWmRiWpulsJtP7gwJhVlOz3IwFCu1bXtiyfhhtiaGwZipiLRiRzhQdrG%2BetBDenqE8%2BGywh0TMg3z6rYWirUzn4qJU3LH44myv9GD8Y9LgQuUfubMdhB2XJLvEa3dEmrEeaxiUGwulrbaDmiPE4eFbkcNpfCDZHHiW4nShXWLbH1o%2BKiN%2B32xlvHbiymeAywt518GEnwtftxvYsK2FSwtv16Uez5DYozrSLHdFn93iT2lGF1XYgBVynrDkbenWXaZYR9jb5%2B3n3SrtRVEx9tlz9eWM8A8F%2BPLmmdSKrJcFN00bZjrqxxQFi2F7yMdLm9wA4qSr8rV8L9AdUMUklUp3%2FMI66%2F9IGOqUBfUfzYU%2Fljem1pxWB1FWiRLaL0zXsreHv68f8rD3GYY5CNnx%2B1Pq7TCOQtddtkjW0ISDZ6NIBN94G202Wt8mq4ma8S%2FsBJPOPhmRV70cEPOdqQUUmbokxizenYCfRNICqM1BuNE8Qgb84DLBrQRYlsrbeMfQ7FbXBBdHDshlK4kwWFB%2B9PKEq3fG6FC7CpYeM0Pi6pdcDJok2N8Grx3q3y%2BAFYdE8&X-Amz-Signature=49e3ad6e3d557f0b70cd8a403acc60cb0aa7b627ce6f955fdbef679145a8f847&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

我们直接来写一个 request bodyrequest body 就是我们对应的刚才这个对象。然后我们写好了这个对象这里边返回什么值，这个就无所谓了。


我们直接返回一个 is water 好吧， is water 的，然后加上我们具体的一个内容，这个内容我们就叫做 ret 好我们用一个字符串 ret 去接收一下我们对应的内容。这个内容我们直接他过来，我们把它打成一个 JSON 可不可以 [json.to](http://json.to/) string 把一个 object 内容给它打成一个 Jason 然后用 it 接收一下，最后打印一下。
好，同学们，请看，现在我的代码其实已经开发完了，非常非常简单。看见了吧。 OK 那这样的话我们有了这个回调地址。那一会儿我们收到的这个访问如果有 error 的话，然后把它打出来，然后请求到这里边。如果打印了这句话，在控制台上说明什么呢？说明就真的帮我们去做告警了。其实这个 RE 不 return 其实倒无所谓。我们其实再打印一句话，在这里边在 system.out 打印一句话耶，这个我们说告警内容，我把它放到这里。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/4cac0885-cf52-4248-a992-af0a699f3a1f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663EFJUKNK%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCVog4afe8KSvFm4m16q2U2By2xf0NpXt8SwcXgeZFoWAIgalRgJKSHvlx3yvL%2FaivYpB6R8VpJCXS51ylzDzp8SkcqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGMj6ZofZccPjfyTiSrcA8dWLF9Co4mKkMn%2B529nU%2B9yrg9f32sUaEENJ33W4ypicksI2uTL%2BN6Q5KVJEYDbQw6NtZHJasFC2GVVz4VO3bbVOlJKEpZ6AKHCdQUW2T%2B44i%2BPWwY0USNJgVcV8NGfYAIUQG4pwZ0Ny53tODtM4cUofascxYOZSszv507jjHdUiB4rgY71OFCdLWZjCp73ToeZ1zqZxpyOPZqWBmaWz9IdirZTStLu%2FVoBiObHkVAElupLlr%2BHwXFPhUhfj05JEIW2SsGapJxsmHQJr5eBEPB%2FRSsvhZJF%2BbCYwHWmRiWpulsJtP7gwJhVlOz3IwFCu1bXtiyfhhtiaGwZipiLRiRzhQdrG%2BetBDenqE8%2BGywh0TMg3z6rYWirUzn4qJU3LH44myv9GD8Y9LgQuUfubMdhB2XJLvEa3dEmrEeaxiUGwulrbaDmiPE4eFbkcNpfCDZHHiW4nShXWLbH1o%2BKiN%2B32xlvHbiymeAywt518GEnwtftxvYsK2FSwtv16Uez5DYozrSLHdFn93iT2lGF1XYgBVynrDkbenWXaZYR9jb5%2B3n3SrtRVEx9tlz9eWM8A8F%2BPLmmdSKrJcFN00bZjrqxxQFi2F7yMdLm9wA4qSr8rV8L9AdUMUklUp3%2FMI66%2F9IGOqUBfUfzYU%2Fljem1pxWB1FWiRLaL0zXsreHv68f8rD3GYY5CNnx%2B1Pq7TCOQtddtkjW0ISDZ6NIBN94G202Wt8mq4ma8S%2FsBJPOPhmRV70cEPOdqQUUmbokxizenYCfRNICqM1BuNE8Qgb84DLBrQRYlsrbeMfQ7FbXBBdHDshlK4kwWFB%2B9PKEq3fG6FC7CpYeM0Pi6pdcDJok2N8Grx3q3y%2BAFYdE8&X-Amz-Signature=5e50ddd4f1ebc7d04cbdc4ef178c940521243923ef25200ea7be5ec8b967757e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

告警内容是什么？我们来一个冒号，然后加上我们自己的 NT 因为只要你打出来的话，控制台肯定才会输出。好了，那我们现在大功告成，接下来的事情是什么呢？我们把它重新 clean 掉，然后再打个包，然后我们再打个包，我们去 miss 跳。好，那等他打高了，我们先做一下这个其他的剩余的一些操作。比如说现在你要做什么事情，现在你肯定要把所有的服务都停掉，因为你重新发应用服务了。好啦，其实你不停也可以，就是你看我现在卡夫卡不停，然后三四这个服务我也不停，我只停自己的 feel meet 我也不想停，没问题。


好，我现在就 GPS 杠 L 然后我去把谁 Q 掉，把凯莱克这个服务杠 Q 杠9， (或者 netstat -apn | grep 8001===》 kiil -9 [进程号])

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b82f42e2-d6c9-48d9-803f-dc6faac24bf1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663EFJUKNK%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCVog4afe8KSvFm4m16q2U2By2xf0NpXt8SwcXgeZFoWAIgalRgJKSHvlx3yvL%2FaivYpB6R8VpJCXS51ylzDzp8SkcqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGMj6ZofZccPjfyTiSrcA8dWLF9Co4mKkMn%2B529nU%2B9yrg9f32sUaEENJ33W4ypicksI2uTL%2BN6Q5KVJEYDbQw6NtZHJasFC2GVVz4VO3bbVOlJKEpZ6AKHCdQUW2T%2B44i%2BPWwY0USNJgVcV8NGfYAIUQG4pwZ0Ny53tODtM4cUofascxYOZSszv507jjHdUiB4rgY71OFCdLWZjCp73ToeZ1zqZxpyOPZqWBmaWz9IdirZTStLu%2FVoBiObHkVAElupLlr%2BHwXFPhUhfj05JEIW2SsGapJxsmHQJr5eBEPB%2FRSsvhZJF%2BbCYwHWmRiWpulsJtP7gwJhVlOz3IwFCu1bXtiyfhhtiaGwZipiLRiRzhQdrG%2BetBDenqE8%2BGywh0TMg3z6rYWirUzn4qJU3LH44myv9GD8Y9LgQuUfubMdhB2XJLvEa3dEmrEeaxiUGwulrbaDmiPE4eFbkcNpfCDZHHiW4nShXWLbH1o%2BKiN%2B32xlvHbiymeAywt518GEnwtftxvYsK2FSwtv16Uez5DYozrSLHdFn93iT2lGF1XYgBVynrDkbenWXaZYR9jb5%2B3n3SrtRVEx9tlz9eWM8A8F%2BPLmmdSKrJcFN00bZjrqxxQFi2F7yMdLm9wA4qSr8rV8L9AdUMUklUp3%2FMI66%2F9IGOqUBfUfzYU%2Fljem1pxWB1FWiRLaL0zXsreHv68f8rD3GYY5CNnx%2B1Pq7TCOQtddtkjW0ISDZ6NIBN94G202Wt8mq4ma8S%2FsBJPOPhmRV70cEPOdqQUUmbokxizenYCfRNICqM1BuNE8Qgb84DLBrQRYlsrbeMfQ7FbXBBdHDshlK4kwWFB%2B9PKEq3fG6FC7CpYeM0Pi6pdcDJok2N8Grx3q3y%2BAFYdE8&X-Amz-Signature=54655cdbf396edd236d1635f533c1c4f8bb802311ed4b93c88ecaf1a7b82b33f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

叫做30，然后 137 把它。干掉了之后我去把它删掉，rm杠 RF collector 的炸删掉。注意，我现在 fail beat 停没停，我 PS 杠 EF grape cell beat philbit 没有提供，是不是那个文件还在吗？只不过没有输出。所以说其实你是可以你重新发服务，你只需要去对服务进行一个重新替换就可以，其他的无所谓。


好了，那现在我们来观察一下我们对应的服务已经 success 导航包了。那就 OK 我们现在把新包放到桌面上，我们去刷新一下，然后放到桌面上，然后再把它传到我们的服务器里边，传到我们的服务器里边。 31 没问题，我把它停一下。好了，我又起来了，这个是一个 Excel 的小 bug 把这个 Excel 重新开一下就好了。所以说一会我还得重新起一遍。我刚才把这个 Excel 重新又关掉，打开一下就好了，然后我去来看一下，然后我们再把新打的这个包我给它扔到这个对应的我的 31 上。
好，扔上来之后我们来看一看首先我是不是把 fail beat 起来了，我们来检查一下我们 PS 杠 EF graph fail beat 这个 fail beat 现在是起来的。然后我们看一看三四节点上的这个三四节点上是一个 log stash 我们 GPS 一下，我的 logstash 现在是起着的，我的 logstash 起着了之后，那证明没问题，或者说我没问题是吧。 OK 那我们再看我们三个这个 el K 这个平台，这都是没问题的。然后 51 节点卡夫卡刚才我也起来了，没问题。好，现在我们要做的一个事情就是我们把我们自己刚才的这个 connect 包重新再启动一下 Java 杠架。然后 connector 然后 a and 宇会说把它骑起来好了，把它骑起来。这个服务如果能正常启动，那其实就可以完成我们刚才的一个小的案例了，就是做一个告警。


好了，琪琪来了。起来了之后，小伙伴们请注意，现在我开始真正的去操作了。看所以说这些步骤都是比较繁琐的，因为 elk 其实得相关的去有一些专业的运维同学去做，这样才是比较好的。 OK 然后现在我现在对应的这个告警信息，对应的 watch 我把它创建一下，大家请看我去对应的去给它创建一下。老师在这里也提供一个 watch 的 API 大家可以看这个到时候我也把它放到我们的项目中，跟着大家一起把这个 watch API 这这个里边的信息同步一下。


你可以看到这个里边它有一些简单的 water 操作，比如说查看一个 water 这个叫做 collect 杠 water 好，因为后面给到你的时候咱们两个应该保持一致，这个叫做 collector 杠 water 然后这个是 L log watch ，这个就不是了，你可以执行一个 watch 我那个名字叫什么？我那名字叫做 L log collector watcher 你想执行，它可以直接粘过来，它可以直接执行，包括你也可以查询你查询的 water 是什么？

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/d15758eb-e502-452a-a502-3bc2fd8141c9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663EFJUKNK%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCVog4afe8KSvFm4m16q2U2By2xf0NpXt8SwcXgeZFoWAIgalRgJKSHvlx3yvL%2FaivYpB6R8VpJCXS51ylzDzp8SkcqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGMj6ZofZccPjfyTiSrcA8dWLF9Co4mKkMn%2B529nU%2B9yrg9f32sUaEENJ33W4ypicksI2uTL%2BN6Q5KVJEYDbQw6NtZHJasFC2GVVz4VO3bbVOlJKEpZ6AKHCdQUW2T%2B44i%2BPWwY0USNJgVcV8NGfYAIUQG4pwZ0Ny53tODtM4cUofascxYOZSszv507jjHdUiB4rgY71OFCdLWZjCp73ToeZ1zqZxpyOPZqWBmaWz9IdirZTStLu%2FVoBiObHkVAElupLlr%2BHwXFPhUhfj05JEIW2SsGapJxsmHQJr5eBEPB%2FRSsvhZJF%2BbCYwHWmRiWpulsJtP7gwJhVlOz3IwFCu1bXtiyfhhtiaGwZipiLRiRzhQdrG%2BetBDenqE8%2BGywh0TMg3z6rYWirUzn4qJU3LH44myv9GD8Y9LgQuUfubMdhB2XJLvEa3dEmrEeaxiUGwulrbaDmiPE4eFbkcNpfCDZHHiW4nShXWLbH1o%2BKiN%2B32xlvHbiymeAywt518GEnwtftxvYsK2FSwtv16Uez5DYozrSLHdFn93iT2lGF1XYgBVynrDkbenWXaZYR9jb5%2B3n3SrtRVEx9tlz9eWM8A8F%2BPLmmdSKrJcFN00bZjrqxxQFi2F7yMdLm9wA4qSr8rV8L9AdUMUklUp3%2FMI66%2F9IGOqUBfUfzYU%2Fljem1pxWB1FWiRLaL0zXsreHv68f8rD3GYY5CNnx%2B1Pq7TCOQtddtkjW0ISDZ6NIBN94G202Wt8mq4ma8S%2FsBJPOPhmRV70cEPOdqQUUmbokxizenYCfRNICqM1BuNE8Qgb84DLBrQRYlsrbeMfQ7FbXBBdHDshlK4kwWFB%2B9PKEq3fG6FC7CpYeM0Pi6pdcDJok2N8Grx3q3y%2BAFYdE8&X-Amz-Signature=ac55220829d7854f61f72a594cf149abba9301dcbff1919017e398527c2dfb8b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

 L log 杠 collect water 这是没问题的。 OK 我把它保存。然后现在就开始去通过控制台运行它一下，执行好它已经成功了。创建成功了之后，他就会帮我们去每 5 秒钟去扫一下这个索引，看一看里边到底有没有 L 那其实你可以通过哪去看很简单，你通过老师刚才给你的这个文档你可以去看。比如说你说查看这个 water 有没有运行或者怎么样，你可以直接通过命令去敲走着，你看当前 sound 当前它是 trueok 这是没问题的。就是说我们证明我们这个告警是对的。然后还有哪呢？在这个 management 里边如果你集成了 expect 的话，你会看到它除了有 index pattern 它后面还有一个什么 water 看见了这个 water 里边我们点开你可以自己创建 water 或者我们之前已经创建过了，你看老师之前是在 7 个月，两个月之前创建过好多的 watch 那我们新创建的 water 在这里。


fail 你看这里面有个时间说你是 20:45 创建的，我们直接点开点进去，我在 f5 刷新一下，你会看到，它已经执行了多少次了，说白了就是说 46 秒看见了吗？它每五秒钟会扫一下刚才我们所关注的那个索引，每五秒钟扫一下。比如说 last 24 小时或者 last 1 小时，你看 46 分 11 秒，我们再刷一下再看一下。其实你点回去就行了。 water 丝然后再点进来，你看 11 秒，16秒，21秒，就是说每 5 秒钟他都会帮我去扫一次。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/98b53863-b24b-443a-8258-3b1f2d17dd65/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663EFJUKNK%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCVog4afe8KSvFm4m16q2U2By2xf0NpXt8SwcXgeZFoWAIgalRgJKSHvlx3yvL%2FaivYpB6R8VpJCXS51ylzDzp8SkcqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGMj6ZofZccPjfyTiSrcA8dWLF9Co4mKkMn%2B529nU%2B9yrg9f32sUaEENJ33W4ypicksI2uTL%2BN6Q5KVJEYDbQw6NtZHJasFC2GVVz4VO3bbVOlJKEpZ6AKHCdQUW2T%2B44i%2BPWwY0USNJgVcV8NGfYAIUQG4pwZ0Ny53tODtM4cUofascxYOZSszv507jjHdUiB4rgY71OFCdLWZjCp73ToeZ1zqZxpyOPZqWBmaWz9IdirZTStLu%2FVoBiObHkVAElupLlr%2BHwXFPhUhfj05JEIW2SsGapJxsmHQJr5eBEPB%2FRSsvhZJF%2BbCYwHWmRiWpulsJtP7gwJhVlOz3IwFCu1bXtiyfhhtiaGwZipiLRiRzhQdrG%2BetBDenqE8%2BGywh0TMg3z6rYWirUzn4qJU3LH44myv9GD8Y9LgQuUfubMdhB2XJLvEa3dEmrEeaxiUGwulrbaDmiPE4eFbkcNpfCDZHHiW4nShXWLbH1o%2BKiN%2B32xlvHbiymeAywt518GEnwtftxvYsK2FSwtv16Uez5DYozrSLHdFn93iT2lGF1XYgBVynrDkbenWXaZYR9jb5%2B3n3SrtRVEx9tlz9eWM8A8F%2BPLmmdSKrJcFN00bZjrqxxQFi2F7yMdLm9wA4qSr8rV8L9AdUMUklUp3%2FMI66%2F9IGOqUBfUfzYU%2Fljem1pxWB1FWiRLaL0zXsreHv68f8rD3GYY5CNnx%2B1Pq7TCOQtddtkjW0ISDZ6NIBN94G202Wt8mq4ma8S%2FsBJPOPhmRV70cEPOdqQUUmbokxizenYCfRNICqM1BuNE8Qgb84DLBrQRYlsrbeMfQ7FbXBBdHDshlK4kwWFB%2B9PKEq3fG6FC7CpYeM0Pi6pdcDJok2N8Grx3q3y%2BAFYdE8&X-Amz-Signature=9cfa3260dbc3a5794cdc5a502fee9ed354cceef6ec243b1f4918e36a4131c544&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

好，那对应这个 wash 我已经解释得很清楚了，因为你没有数据就没有告警，什么时候我们能让他去看呢？告警很简单，来，我们现在就来做一下这个事情，我们去访问一下 error 就好了。注意 ER RO 然后先不要着急去敲这回车，我们想看到效果，你应该看到 31 的控制台，我把它可丽尔一下。然后现在我去刷新访问了一次。同学们请看这个日志是不是已经打印了错误的日志对不对？错误的是打印了之后，接下来其实你应该看到看一看这个告警触没触发，那怎么办？还是回到控制台我们来刷新一下这个告警有没有处罚？同学们请看这个告警现在还没有处罚。


那你现在可以看一个问题，就是说我们先去 discover 里边，我们去看看有没有这个日志，包括我们自己的那个服务器里边没有去打印那句告警内容。那其实就是有问题了，就是你哪块做的不对了，我们先简单跟一下来看一看。首先你怎么去排查这种问题，那你要逐步的去排查。首先看我们的三四这个服务器。 34 的服务器是我们的 GPS 看见了吗？ 34 服务器是我们的什么是我们的 logstash 那 logstash 是不是就没有把这条日志上报上去呢？刚才其实我明明看到这个 logstash 服务启动了，但是现在为什么又没了呢？可能刚才我操作的是有问题的。


总之现在我已经上报了一条告警信息了，那我现在可以把它骑起来吗？因为我卡夫卡里有数据，但是我的 lost 里肯定没有消费，所以说我现在再重新去起一下我的 log 赛事，重新旗下。那这条数据肯定会被 log 赛事筹备，我们的卡夫卡里边也是肯定有数据，因为卡夫卡它一直是起的状态。但是有一个问题，这个告警不一定能够推送成功。同学们想一想是不是这样的，为什么呢？因为你已经超过了我们的时间限制。那我这里边 water 只是每 5 秒钟去扫当前时间，减去前 30 秒的我并不能确定什么呢？我并不能确定你超过了那么长时间我也会给你推。所以说我们看一下这个 dv tools 我们对应的这个 water 是怎么去写的，就是当前，然后减去 30 秒，在当前时间减 30 秒。这个时间段内里边 error 并且它的 hit 大于0，我才会帮你去推告警，只有这种情况我才会帮你推高警。那所以说现在早已经过了 30 秒，就算你的 elk 能够采集到数据，能够抓到这个异常。那么我的我们再打开一下。我的这个 kibana 上，也就是说我的 elastic search 上是肯定是有的。这个告警我可以搜一下。就是 L log 。我们来看一看 last 15 分钟。就是在我们 20:47 这个时间点，我们已经有了一个错误，它的级别是 L 它是算数异常对吧？这是刚才我们访问的，这是对战信息都会有。但是我们来看一看我们的服务器上 31 这个节点，它并没有推靠井，他有没有推告警？其实你看这个还是看 management 里边那个 watch 如果处罚了他会有一个小喇叭，就是表示他已经处罚告警了。


好了，那我们再次再刷一下，看看有没有。好，我又访问了一次，同学们请看我这回访问了一次，我再刷新一下一会数据收集上来。在 20:51 的时候已经收集下来了。然后我们可以去刷新一下这个 water 来看一看它到底有没有这回看一看他有没有去帮你去有这个 L 然后我们来看一看对应的这个堆栈信息。 31 这个节点上。小伙伴们现在我们所看到的这个问题就是说我们刚才写了一个方法，他们也没给我回调没有回调，我的日志通过这个劳斯菜市已经传到了我们的 elk 平台上。那为什么我们这次告警没有处罚呢？这是一个小问题。那接下来我们就来排查一下他。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/c3ad0d47-ec03-4b93-b12f-f07c50d17f9a/2020-09-17_173152.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663EFJUKNK%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225332Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCVog4afe8KSvFm4m16q2U2By2xf0NpXt8SwcXgeZFoWAIgalRgJKSHvlx3yvL%2FaivYpB6R8VpJCXS51ylzDzp8SkcqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGMj6ZofZccPjfyTiSrcA8dWLF9Co4mKkMn%2B529nU%2B9yrg9f32sUaEENJ33W4ypicksI2uTL%2BN6Q5KVJEYDbQw6NtZHJasFC2GVVz4VO3bbVOlJKEpZ6AKHCdQUW2T%2B44i%2BPWwY0USNJgVcV8NGfYAIUQG4pwZ0Ny53tODtM4cUofascxYOZSszv507jjHdUiB4rgY71OFCdLWZjCp73ToeZ1zqZxpyOPZqWBmaWz9IdirZTStLu%2FVoBiObHkVAElupLlr%2BHwXFPhUhfj05JEIW2SsGapJxsmHQJr5eBEPB%2FRSsvhZJF%2BbCYwHWmRiWpulsJtP7gwJhVlOz3IwFCu1bXtiyfhhtiaGwZipiLRiRzhQdrG%2BetBDenqE8%2BGywh0TMg3z6rYWirUzn4qJU3LH44myv9GD8Y9LgQuUfubMdhB2XJLvEa3dEmrEeaxiUGwulrbaDmiPE4eFbkcNpfCDZHHiW4nShXWLbH1o%2BKiN%2B32xlvHbiymeAywt518GEnwtftxvYsK2FSwtv16Uez5DYozrSLHdFn93iT2lGF1XYgBVynrDkbenWXaZYR9jb5%2B3n3SrtRVEx9tlz9eWM8A8F%2BPLmmdSKrJcFN00bZjrqxxQFi2F7yMdLm9wA4qSr8rV8L9AdUMUklUp3%2FMI66%2F9IGOqUBfUfzYU%2Fljem1pxWB1FWiRLaL0zXsreHv68f8rD3GYY5CNnx%2B1Pq7TCOQtddtkjW0ISDZ6NIBN94G202Wt8mq4ma8S%2FsBJPOPhmRV70cEPOdqQUUmbokxizenYCfRNICqM1BuNE8Qgb84DLBrQRYlsrbeMfQ7FbXBBdHDshlK4kwWFB%2B9PKEq3fG6FC7CpYeM0Pi6pdcDJok2N8Grx3q3y%2BAFYdE8&X-Amz-Signature=7a75e416d250770ddd94c8dec2390b74710868357dfcaf8961ff1d82e37b204d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





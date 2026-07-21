---
title: 2-12 watcher 语法
---

# 2-12 watcher 语法

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/a61c78b6-1747-4e19-b343-7679e62948a3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663TD5TR6M%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225333Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDqCm6urCsrb5GQ8G5C%2FydugKOsGg%2Bmb5KjXJL4hJhjyQIgA5eDdWb%2BZBdi7iWCVIN40Bvx%2BsuiRZM6RGh4jpAI%2B1oqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOLaqxzX64LHldZu2SrcA60oCpIhVE%2FqomxGuwtcxCs9f8eN3tvnpYsrhh2xPopfg3gFIRAd9aVoaSIlYr0y49xkyMALCcEcssgyY9JCcUi%2FkGZveJ7l4zWoyZ7udFu97re5sYXsOQk2k%2BasL6vl%2B%2Fku5Xg1cnLM%2BNB8dcgfGUkoiEMLUjxZ%2FhT%2Fogxzx8UNjbaVaOLwB2CP4ZMX3NhCl0jZnW8oCuxV0qwGDJJKKG3uo3YX55QL6thws1osVP%2B1TGaTtfYUjww2n%2FGuqgK2p7ycLY0oR%2BpiU0EbNE3DFJ5r18NtkHQka37fWIgFtfxAs9TUlQh6EwxZ609EnXv2TnG55ctKkirownutYjw0MtLhPHmfZ7TNb61%2FgA%2BmKl6Hco4wijZLgi7OIwCPSfGZba9ceziY3%2BmZYPltZrdJk%2BbylBbovc7cYa5PJc%2FeURsjnX7cv7p9xhjZGhU5Bir8N8RroaDBwlu0Wuy2kY9pBgvNRRDYHbi3zADwqXH4wHZ3Gash%2F9kWoE0ecUUTXubPakaVHLKfLFVw77oQUURLBTJCUxXNNlaEpCMG0z3LGdscaFHSMDDh2pw0RB5QZuz7tX2tN%2FOoKJ9PN3vQaTjZXBdfvkMB68dfhcIF8FZ1BVYkF21AQccaGorT%2FrRBMIK4%2F9IGOqUBoHdz4An%2B7dU2BMbpn2L5TLq%2B3CcIVUWZ7bmamqAS97EkV%2FC5%2BFDJXwRJQuju19a%2FiyPOl4gq7zNMlDNqpwCop8zSQ0UEztTtNpWtdPp%2BoEmz76EDMyh7qgRK0d57yCYfonztXU2LSoXFhjiEgJoL6PDDRNydRkxWsf%2FvW%2FfSDBVxAdY4VeBaNnibjb7XL5x5BHxDVQzDcOHPmqt1CFBJRjSOdaoN&X-Amz-Signature=6133630c1e8664080ef3934779337602c71c33e2735ee188f39d3e0ba00701f6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[https://www.cnblogs.com/wjx6270/p/13431087.html](https://www.cnblogs.com/wjx6270/p/13431087.html)

```java
##
创建一个watcher, 比如定义一个trigger 每个10s钟看一下input里的数据
PUT _xpack / watcher / watch / school_watcher {
		"trigger": {
			"schedule": {
				"interval": "10s"
			}
		},
		##查看任务信息 "input": {
			"search": {
				"request": {##
					监控具体索引 "indices": ["school*"],
					##body里面具体些搜索语句 "body": {
						"size": 0,
						"query": {
							"match": {##
								比如索引里面name 有 hello 则进行报警 "name": "hello"
							}
						}
					}
				}
			}
		},
		##对于上面的查询结果进行比较： "condition": {##
			compare进行比较 "compare": {##
				上面的query查询的结果会放入到ctx.payload中：## 比如获取 ctx.payload.hits.total ctx.payload._shards.total 等等 "ctx.payload.hits.total": {
					"gt": 0
				}
			}
		},
		##transform作用： 重新查询出文档内容赋值给ctx.payload "transform": {
			"search": {
				"request": {
					"indices": ["school*"],
					"body": {
						"size": 10,
						"query": {
							"match": {
								"name": "hello"
							}
						}
					}
				}
			}
```



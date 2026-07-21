---
title: 1-11 【Demo】Sleuth集成ELK实现日志检索-1
---

# 1-11 【Demo】Sleuth集成ELK实现日志检索-1

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/1365b64f-a61e-4910-9ff5-d6aa742fec87/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662M7YJSPF%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225803Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID9C05CUuFFehuWxZABqY%2FN%2BhYb12rdB9qizvW%2FkFZp0AiEAik81m6Ou6ORrryf5989RaDvuSA33%2Fh3D4a0VsjVmt3AqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBdJpv%2F61xy2wWG1GircA0ykpCWHKQ3iRZeUzHb%2Fd7vqXD8yC2nKT911LnyN3heUq6sSMm6jO5pmLJMD9We5ayIPf0B1iwljPxrVRO%2FqnaROgaBrEso8hKMjFR%2FLtiufKVKUbCIMj1ax8PZ1CU4bYzVuMdf9DMhWQPvkk0yRiJx6yeau6qIi01ali5pTn97zYSk8%2BwVB%2FirVkId4EWYDiwxqITEJ%2FiDPxso5jauVasGK81ZdXF2aUsYojkgyPbP%2BT8mPAsEloeP4VQ2v8gJ9mgEtDasI%2Ff2lQFmEM%2BIDBupcCKUU7e3u5UeYijNsn0VYCunbV2ghAkrPifK1r0Yn5C%2FQbbxrMnka6iwch8SbUDHKEyGNLC1KrcIEKIvZNLv63sJvyzAOg3%2BcT9rw4bbC9anuCJPcI44SBgaVLjcgi0Cs%2FHqaPI6sUjIqN8JtKf%2FPH7QU8d0%2Bb%2F4j0hRasUgpj3Xpa0mBDhnBkdGCIZvVVNvaRX8fqZNw1cK%2BkJFjv8mgT3n7Wn5XinYnHvjyE5rNFWnC5h2%2BXTkkkYTHSdGanmNkVusYQbcSkyol9thBLgmJRCjqMqoqG9AwXKZ8ggt4pW2xVbp8S3tEhicLqaC5I9bzYNUt%2F3etAuYzYxmoCw%2F749EGB0OI71cNubDzMN23%2F9IGOqUB2H7dno17Fj0hZUHiy0vqhjd3dK7bPdUnSqX3%2BvJzb8OhxianD1sBZwkefnA%2BQki2xnIq1Tcttl%2F5smqIc3prvu%2Bqy6kKntGTx3XHJOA%2BrDxqArKipx1BXQVJe5wvcF4LQy1aPgLVrsY1mVWgDiVT9jFqI0wq%2BoAxJY0RvB7UbNiVd3DiXPZrKjQZ67cXfp4lgj3CVrzqDl2Ih74bR2YmE516i1Pj&X-Amz-Signature=bc76480da1f9efc999267502caf42ebdfcef71ef72ff2fe0a5bce07f7ac6dd54&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/ec61daf3-eb98-4715-a1d1-7e4f50df5b8f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662M7YJSPF%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225803Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID9C05CUuFFehuWxZABqY%2FN%2BhYb12rdB9qizvW%2FkFZp0AiEAik81m6Ou6ORrryf5989RaDvuSA33%2Fh3D4a0VsjVmt3AqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBdJpv%2F61xy2wWG1GircA0ykpCWHKQ3iRZeUzHb%2Fd7vqXD8yC2nKT911LnyN3heUq6sSMm6jO5pmLJMD9We5ayIPf0B1iwljPxrVRO%2FqnaROgaBrEso8hKMjFR%2FLtiufKVKUbCIMj1ax8PZ1CU4bYzVuMdf9DMhWQPvkk0yRiJx6yeau6qIi01ali5pTn97zYSk8%2BwVB%2FirVkId4EWYDiwxqITEJ%2FiDPxso5jauVasGK81ZdXF2aUsYojkgyPbP%2BT8mPAsEloeP4VQ2v8gJ9mgEtDasI%2Ff2lQFmEM%2BIDBupcCKUU7e3u5UeYijNsn0VYCunbV2ghAkrPifK1r0Yn5C%2FQbbxrMnka6iwch8SbUDHKEyGNLC1KrcIEKIvZNLv63sJvyzAOg3%2BcT9rw4bbC9anuCJPcI44SBgaVLjcgi0Cs%2FHqaPI6sUjIqN8JtKf%2FPH7QU8d0%2Bb%2F4j0hRasUgpj3Xpa0mBDhnBkdGCIZvVVNvaRX8fqZNw1cK%2BkJFjv8mgT3n7Wn5XinYnHvjyE5rNFWnC5h2%2BXTkkkYTHSdGanmNkVusYQbcSkyol9thBLgmJRCjqMqoqG9AwXKZ8ggt4pW2xVbp8S3tEhicLqaC5I9bzYNUt%2F3etAuYzYxmoCw%2F749EGB0OI71cNubDzMN23%2F9IGOqUB2H7dno17Fj0hZUHiy0vqhjd3dK7bPdUnSqX3%2BvJzb8OhxianD1sBZwkefnA%2BQki2xnIq1Tcttl%2F5smqIc3prvu%2Bqy6kKntGTx3XHJOA%2BrDxqArKipx1BXQVJe5wvcF4LQy1aPgLVrsY1mVWgDiVT9jFqI0wq%2BoAxJY0RvB7UbNiVd3DiXPZrKjQZ67cXfp4lgj3CVrzqDl2Ih74bR2YmE516i1Pj&X-Amz-Signature=6b45ca69f826e3adf74eaa8ba6ac6b282e5d9c123054bf871988ef60999e6339&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/20da1940-405a-43b2-9078-5b2d245cfe67/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662M7YJSPF%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225803Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID9C05CUuFFehuWxZABqY%2FN%2BhYb12rdB9qizvW%2FkFZp0AiEAik81m6Ou6ORrryf5989RaDvuSA33%2Fh3D4a0VsjVmt3AqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBdJpv%2F61xy2wWG1GircA0ykpCWHKQ3iRZeUzHb%2Fd7vqXD8yC2nKT911LnyN3heUq6sSMm6jO5pmLJMD9We5ayIPf0B1iwljPxrVRO%2FqnaROgaBrEso8hKMjFR%2FLtiufKVKUbCIMj1ax8PZ1CU4bYzVuMdf9DMhWQPvkk0yRiJx6yeau6qIi01ali5pTn97zYSk8%2BwVB%2FirVkId4EWYDiwxqITEJ%2FiDPxso5jauVasGK81ZdXF2aUsYojkgyPbP%2BT8mPAsEloeP4VQ2v8gJ9mgEtDasI%2Ff2lQFmEM%2BIDBupcCKUU7e3u5UeYijNsn0VYCunbV2ghAkrPifK1r0Yn5C%2FQbbxrMnka6iwch8SbUDHKEyGNLC1KrcIEKIvZNLv63sJvyzAOg3%2BcT9rw4bbC9anuCJPcI44SBgaVLjcgi0Cs%2FHqaPI6sUjIqN8JtKf%2FPH7QU8d0%2Bb%2F4j0hRasUgpj3Xpa0mBDhnBkdGCIZvVVNvaRX8fqZNw1cK%2BkJFjv8mgT3n7Wn5XinYnHvjyE5rNFWnC5h2%2BXTkkkYTHSdGanmNkVusYQbcSkyol9thBLgmJRCjqMqoqG9AwXKZ8ggt4pW2xVbp8S3tEhicLqaC5I9bzYNUt%2F3etAuYzYxmoCw%2F749EGB0OI71cNubDzMN23%2F9IGOqUB2H7dno17Fj0hZUHiy0vqhjd3dK7bPdUnSqX3%2BvJzb8OhxianD1sBZwkefnA%2BQki2xnIq1Tcttl%2F5smqIc3prvu%2Bqy6kKntGTx3XHJOA%2BrDxqArKipx1BXQVJe5wvcF4LQy1aPgLVrsY1mVWgDiVT9jFqI0wq%2BoAxJY0RvB7UbNiVd3DiXPZrKjQZ67cXfp4lgj3CVrzqDl2Ih74bR2YmE516i1Pj&X-Amz-Signature=11321984724295655188a6b029947d4834e50c214b50975c20bfe067871e14c8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

hello 慕课网的各位同学们，大家好，这一节当中我们将引入一个新的处理日志以及搜索日志的组件，叫 elk 那前面的章节大家应该对 elK 有过一个全面的了解，咱这一节就把他的介绍部分轻描淡写的一笔带过。不过咱这一节当中搭建 el K 的方式非常非常省力。大家如果在分布式章节觉得搭建这三个服务太过麻烦的话，在这个章节我来教大家用一个 Docker 全部搞定。 OK 同学们跟我一起进入这一章的学习。


下一页在开始之前，我先来跟大家简单的回顾 elk 是什么，这个 E 就是 elastic search 它是用来做搜索和数据 indexing 的组件，那 L 是 logstash 通过名字就可以知道它跟 log 是息息相关的，用来做 log 的收集以及过滤等等。


那最后一个 k 是咱 elk 组合的颜值担当，不是说它的图标很漂亮，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/f3e20a5a-38d9-4710-ac84-445012815547/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662M7YJSPF%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225803Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID9C05CUuFFehuWxZABqY%2FN%2BhYb12rdB9qizvW%2FkFZp0AiEAik81m6Ou6ORrryf5989RaDvuSA33%2Fh3D4a0VsjVmt3AqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBdJpv%2F61xy2wWG1GircA0ykpCWHKQ3iRZeUzHb%2Fd7vqXD8yC2nKT911LnyN3heUq6sSMm6jO5pmLJMD9We5ayIPf0B1iwljPxrVRO%2FqnaROgaBrEso8hKMjFR%2FLtiufKVKUbCIMj1ax8PZ1CU4bYzVuMdf9DMhWQPvkk0yRiJx6yeau6qIi01ali5pTn97zYSk8%2BwVB%2FirVkId4EWYDiwxqITEJ%2FiDPxso5jauVasGK81ZdXF2aUsYojkgyPbP%2BT8mPAsEloeP4VQ2v8gJ9mgEtDasI%2Ff2lQFmEM%2BIDBupcCKUU7e3u5UeYijNsn0VYCunbV2ghAkrPifK1r0Yn5C%2FQbbxrMnka6iwch8SbUDHKEyGNLC1KrcIEKIvZNLv63sJvyzAOg3%2BcT9rw4bbC9anuCJPcI44SBgaVLjcgi0Cs%2FHqaPI6sUjIqN8JtKf%2FPH7QU8d0%2Bb%2F4j0hRasUgpj3Xpa0mBDhnBkdGCIZvVVNvaRX8fqZNw1cK%2BkJFjv8mgT3n7Wn5XinYnHvjyE5rNFWnC5h2%2BXTkkkYTHSdGanmNkVusYQbcSkyol9thBLgmJRCjqMqoqG9AwXKZ8ggt4pW2xVbp8S3tEhicLqaC5I9bzYNUt%2F3etAuYzYxmoCw%2F749EGB0OI71cNubDzMN23%2F9IGOqUB2H7dno17Fj0hZUHiy0vqhjd3dK7bPdUnSqX3%2BvJzb8OhxianD1sBZwkefnA%2BQki2xnIq1Tcttl%2F5smqIc3prvu%2Bqy6kKntGTx3XHJOA%2BrDxqArKipx1BXQVJe5wvcF4LQy1aPgLVrsY1mVWgDiVT9jFqI0wq%2BoAxJY0RvB7UbNiVd3DiXPZrKjQZ67cXfp4lgj3CVrzqDl2Ih74bR2YmE516i1Pj&X-Amz-Signature=015a82b3a6cc3f29b3388d8cf53ba79ab92e62f5d25fb7c8d1a930cb1f3ba53f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

而是它的界面很漂亮。它提供了一个非常酷炫的 UI 界面，让大家可以在前端去搜索 log 然后产生一些数据报表。要么说这三个家伙是一个组合吗？看这个图标都差不多，花花绿绿跟跳广场舞大妈似的。那咱看看 el K 可以做什么样的工作，这个组合搭配起来法力无边，它能做的最主要的工作是日志的收集和过滤。那除此以外，还有日志信息的化。这个持久化的部分就是放在 elastic search 里面，供后面的组件来搜索调用。


如果从我们日常开发或者在生产环境做 troubleshooting 的经验来说，它还有一个重要的功能是根据关键字来查找 log 比方说咱要查一个订单，通过 order ID 做查询，或者在后台拿到 sleuth 的 trace ID 用来查询整个调用链路上的 log 信息。最后就是它的报表功能了，可以汇总分期 log 然后提供重要的数据支持。咱知道 elk 组合能干什么以后，咱还要知道他是怎么来分工协作的。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/faecfade-f69f-43f1-b14f-795259b397c6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662M7YJSPF%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225803Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID9C05CUuFFehuWxZABqY%2FN%2BhYb12rdB9qizvW%2FkFZp0AiEAik81m6Ou6ORrryf5989RaDvuSA33%2Fh3D4a0VsjVmt3AqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBdJpv%2F61xy2wWG1GircA0ykpCWHKQ3iRZeUzHb%2Fd7vqXD8yC2nKT911LnyN3heUq6sSMm6jO5pmLJMD9We5ayIPf0B1iwljPxrVRO%2FqnaROgaBrEso8hKMjFR%2FLtiufKVKUbCIMj1ax8PZ1CU4bYzVuMdf9DMhWQPvkk0yRiJx6yeau6qIi01ali5pTn97zYSk8%2BwVB%2FirVkId4EWYDiwxqITEJ%2FiDPxso5jauVasGK81ZdXF2aUsYojkgyPbP%2BT8mPAsEloeP4VQ2v8gJ9mgEtDasI%2Ff2lQFmEM%2BIDBupcCKUU7e3u5UeYijNsn0VYCunbV2ghAkrPifK1r0Yn5C%2FQbbxrMnka6iwch8SbUDHKEyGNLC1KrcIEKIvZNLv63sJvyzAOg3%2BcT9rw4bbC9anuCJPcI44SBgaVLjcgi0Cs%2FHqaPI6sUjIqN8JtKf%2FPH7QU8d0%2Bb%2F4j0hRasUgpj3Xpa0mBDhnBkdGCIZvVVNvaRX8fqZNw1cK%2BkJFjv8mgT3n7Wn5XinYnHvjyE5rNFWnC5h2%2BXTkkkYTHSdGanmNkVusYQbcSkyol9thBLgmJRCjqMqoqG9AwXKZ8ggt4pW2xVbp8S3tEhicLqaC5I9bzYNUt%2F3etAuYzYxmoCw%2F749EGB0OI71cNubDzMN23%2F9IGOqUB2H7dno17Fj0hZUHiy0vqhjd3dK7bPdUnSqX3%2BvJzb8OhxianD1sBZwkefnA%2BQki2xnIq1Tcttl%2F5smqIc3prvu%2Bqy6kKntGTx3XHJOA%2BrDxqArKipx1BXQVJe5wvcF4LQy1aPgLVrsY1mVWgDiVT9jFqI0wq%2BoAxJY0RvB7UbNiVd3DiXPZrKjQZ67cXfp4lgj3CVrzqDl2Ih74bR2YmE516i1Pj&X-Amz-Signature=d8d6d812f5c68ab645d4b2403bed232ce70423f84f343c402fe4c357312d41a9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

在整个环节里，首当其冲的带头大哥其实是logstash ，它是用来在最前端在第一个步骤中收集 log 信息，然后做一些必要的过滤。那接下来它把过滤后的 log 信息传递给 elastic searchelastic search 把 log 信息做好持久化，然后提供搜索必要的 indexing 支持。


最后一步才是交由我们的 kibana 由 kibana 通过 UI 界面将用户的搜索请求转化为查询语句，从 elastic search 中捞到数据，展现给前端的用户。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/312c49a8-73ef-433b-9b4a-a036a68679d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662M7YJSPF%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225803Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID9C05CUuFFehuWxZABqY%2FN%2BhYb12rdB9qizvW%2FkFZp0AiEAik81m6Ou6ORrryf5989RaDvuSA33%2Fh3D4a0VsjVmt3AqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBdJpv%2F61xy2wWG1GircA0ykpCWHKQ3iRZeUzHb%2Fd7vqXD8yC2nKT911LnyN3heUq6sSMm6jO5pmLJMD9We5ayIPf0B1iwljPxrVRO%2FqnaROgaBrEso8hKMjFR%2FLtiufKVKUbCIMj1ax8PZ1CU4bYzVuMdf9DMhWQPvkk0yRiJx6yeau6qIi01ali5pTn97zYSk8%2BwVB%2FirVkId4EWYDiwxqITEJ%2FiDPxso5jauVasGK81ZdXF2aUsYojkgyPbP%2BT8mPAsEloeP4VQ2v8gJ9mgEtDasI%2Ff2lQFmEM%2BIDBupcCKUU7e3u5UeYijNsn0VYCunbV2ghAkrPifK1r0Yn5C%2FQbbxrMnka6iwch8SbUDHKEyGNLC1KrcIEKIvZNLv63sJvyzAOg3%2BcT9rw4bbC9anuCJPcI44SBgaVLjcgi0Cs%2FHqaPI6sUjIqN8JtKf%2FPH7QU8d0%2Bb%2F4j0hRasUgpj3Xpa0mBDhnBkdGCIZvVVNvaRX8fqZNw1cK%2BkJFjv8mgT3n7Wn5XinYnHvjyE5rNFWnC5h2%2BXTkkkYTHSdGanmNkVusYQbcSkyol9thBLgmJRCjqMqoqG9AwXKZ8ggt4pW2xVbp8S3tEhicLqaC5I9bzYNUt%2F3etAuYzYxmoCw%2F749EGB0OI71cNubDzMN23%2F9IGOqUB2H7dno17Fj0hZUHiy0vqhjd3dK7bPdUnSqX3%2BvJzb8OhxianD1sBZwkefnA%2BQki2xnIq1Tcttl%2F5smqIc3prvu%2Bqy6kKntGTx3XHJOA%2BrDxqArKipx1BXQVJe5wvcF4LQy1aPgLVrsY1mVWgDiVT9jFqI0wq%2BoAxJY0RvB7UbNiVd3DiXPZrKjQZ67cXfp4lgj3CVrzqDl2Ih74bR2YmE516i1Pj&X-Amz-Signature=bf8ae9eb9877c81a8a947db7334648df444eb9052c2e93aa58b5b5cb027b39b9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

 OK 那我们刚才对 elk 组合做了一个句型回顾，相信大家应该或多或少的能想起来在分布式章节中学到的那些知识点了。 OK 那接下来我们还要做一个动手的练习是什么呢？那就是做准备工作，下载 elk 的镜像。咱前面提到过，这一节是一个非常简单的傻瓜式的编程题，他不会让大家手把手的分别搭建 elk 然后组合在一起，那样太麻烦了。老师这里直接通过一个镜像让大家来下载 elk 这样的话就可以通过一个命令直接把 E LK 启动起来。 OK 那我们先来看这一节的步骤都有哪些。


第一步，通过 Docker 安装 elk 镜像，如果同学们有使用 Docker 的经验的话，那可以直接跑下面的这个命令，用红字标出来的命令，大家一定要记住，它是使用 Docker 命令来拉取一个镜像的。但是在拉取镜像的过程中，我劝同学们一定要保持耐心，一定要能耐得住寂寞，因为这个镜像真的非常难拉取。我尝试从本地的网络拉，实在是速度太慢，后来翻墙发现速度也不行，最后只好怎么样跑到公司用美国的专线才把他拉下来的。所以同学们如果没有翻墙工具是在家里用普通网络拉的话，一定要稍加耐心一下，早上出门把命令打上，然后上完班回到家可能就会拉好了。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/1aad1fd7-e1f7-4684-bd9d-338ed0832de4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662M7YJSPF%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225803Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID9C05CUuFFehuWxZABqY%2FN%2BhYb12rdB9qizvW%2FkFZp0AiEAik81m6Ou6ORrryf5989RaDvuSA33%2Fh3D4a0VsjVmt3AqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBdJpv%2F61xy2wWG1GircA0ykpCWHKQ3iRZeUzHb%2Fd7vqXD8yC2nKT911LnyN3heUq6sSMm6jO5pmLJMD9We5ayIPf0B1iwljPxrVRO%2FqnaROgaBrEso8hKMjFR%2FLtiufKVKUbCIMj1ax8PZ1CU4bYzVuMdf9DMhWQPvkk0yRiJx6yeau6qIi01ali5pTn97zYSk8%2BwVB%2FirVkId4EWYDiwxqITEJ%2FiDPxso5jauVasGK81ZdXF2aUsYojkgyPbP%2BT8mPAsEloeP4VQ2v8gJ9mgEtDasI%2Ff2lQFmEM%2BIDBupcCKUU7e3u5UeYijNsn0VYCunbV2ghAkrPifK1r0Yn5C%2FQbbxrMnka6iwch8SbUDHKEyGNLC1KrcIEKIvZNLv63sJvyzAOg3%2BcT9rw4bbC9anuCJPcI44SBgaVLjcgi0Cs%2FHqaPI6sUjIqN8JtKf%2FPH7QU8d0%2Bb%2F4j0hRasUgpj3Xpa0mBDhnBkdGCIZvVVNvaRX8fqZNw1cK%2BkJFjv8mgT3n7Wn5XinYnHvjyE5rNFWnC5h2%2BXTkkkYTHSdGanmNkVusYQbcSkyol9thBLgmJRCjqMqoqG9AwXKZ8ggt4pW2xVbp8S3tEhicLqaC5I9bzYNUt%2F3etAuYzYxmoCw%2F749EGB0OI71cNubDzMN23%2F9IGOqUB2H7dno17Fj0hZUHiy0vqhjd3dK7bPdUnSqX3%2BvJzb8OhxianD1sBZwkefnA%2BQki2xnIq1Tcttl%2F5smqIc3prvu%2Bqy6kKntGTx3XHJOA%2BrDxqArKipx1BXQVJe5wvcF4LQy1aPgLVrsY1mVWgDiVT9jFqI0wq%2BoAxJY0RvB7UbNiVd3DiXPZrKjQZ67cXfp4lgj3CVrzqDl2Ih74bR2YmE516i1Pj&X-Amz-Signature=afc5735ed547c3805e58b65efc17d06cc1f416eac8cc6a0390c664533d2bfc9c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

OK 那如果大家在平时的工作中并不常用到 Docker 而且对 Docker 的命令也不熟悉，这里也可以等待咱学到分布式章节。学过 Docker 的基本操作以后再回来做这个内容都是可以的。不过没有 Docker 知识，也不用太过担心，跟着老师一步一步做没什么问题的。


OK 接下来第二个步骤就是创建 Docker 容器，咱给这个 Docker 容器取名为 elk 在启动 elk 镜像的时候，要分别给这三个组件指定端口号。 OK 那最后一步就是修改 logstash 接收日志的方式，这一步需要在 darker 中完成。那我这里会把整个步骤需要用到的命令都添加到项目中，通过注释的方式添加到项目文件里，大家可以去 github 上面拉取。 OK 那同学们准备好的话就跟我一起进入动手环节。同学们老师把所有的 Docker 命令就是本节中需要用到的这些命令都添加到了一个 TXT 文件夹里。这个文件夹大家可以在 slow 的 Tracy 的 resources 目录下面找到它的名称叫 elk 然后下划线 comment okay 那我先跟着命令一个一个往下做。

[file](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/2e6a61a6-3d28-4396-9ca5-9f921e6df42e/elk_commands.txt?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662M7YJSPF%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225803Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID9C05CUuFFehuWxZABqY%2FN%2BhYb12rdB9qizvW%2FkFZp0AiEAik81m6Ou6ORrryf5989RaDvuSA33%2Fh3D4a0VsjVmt3AqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBdJpv%2F61xy2wWG1GircA0ykpCWHKQ3iRZeUzHb%2Fd7vqXD8yC2nKT911LnyN3heUq6sSMm6jO5pmLJMD9We5ayIPf0B1iwljPxrVRO%2FqnaROgaBrEso8hKMjFR%2FLtiufKVKUbCIMj1ax8PZ1CU4bYzVuMdf9DMhWQPvkk0yRiJx6yeau6qIi01ali5pTn97zYSk8%2BwVB%2FirVkId4EWYDiwxqITEJ%2FiDPxso5jauVasGK81ZdXF2aUsYojkgyPbP%2BT8mPAsEloeP4VQ2v8gJ9mgEtDasI%2Ff2lQFmEM%2BIDBupcCKUU7e3u5UeYijNsn0VYCunbV2ghAkrPifK1r0Yn5C%2FQbbxrMnka6iwch8SbUDHKEyGNLC1KrcIEKIvZNLv63sJvyzAOg3%2BcT9rw4bbC9anuCJPcI44SBgaVLjcgi0Cs%2FHqaPI6sUjIqN8JtKf%2FPH7QU8d0%2Bb%2F4j0hRasUgpj3Xpa0mBDhnBkdGCIZvVVNvaRX8fqZNw1cK%2BkJFjv8mgT3n7Wn5XinYnHvjyE5rNFWnC5h2%2BXTkkkYTHSdGanmNkVusYQbcSkyol9thBLgmJRCjqMqoqG9AwXKZ8ggt4pW2xVbp8S3tEhicLqaC5I9bzYNUt%2F3etAuYzYxmoCw%2F749EGB0OI71cNubDzMN23%2F9IGOqUB2H7dno17Fj0hZUHiy0vqhjd3dK7bPdUnSqX3%2BvJzb8OhxianD1sBZwkefnA%2BQki2xnIq1Tcttl%2F5smqIc3prvu%2Bqy6kKntGTx3XHJOA%2BrDxqArKipx1BXQVJe5wvcF4LQy1aPgLVrsY1mVWgDiVT9jFqI0wq%2BoAxJY0RvB7UbNiVd3DiXPZrKjQZ67cXfp4lgj3CVrzqDl2Ih74bR2YmE516i1Pj&X-Amz-Signature=54f30615518993056ec4400fc65f611c50668bbb4b89de78d0b6f1f1f23f4e9c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


```java
1. 下载镜像（时间很久，耐心要足）：
docker pull sebp/elk

2. 创建Docker容器（只用在第一次使用的时候才创建）
docker run --restart=always -p 5601:5601 -p 9200:9200 -p 5044:5044 -e ES_MIN_MEM=128m  -e ES_MAX_MEM=1024m -it --name elk sebp/elk

docker run  -p 5601:5601 -p 9200:9200 -p 5044:5044 -e ES_MIN_MEM=128m  -e ES_MAX_MEM=1024m -it --name elk sebp/elk


docker run --restart=always -p 5601:5601 -p 9200:9200 -p 5044:5044 -e ES_MIN_MEM=128m  -e ES_MAX_MEM=1024m --name elk sebp/elk

3. 进入docker容器：
docker exec -it elk /bin/bash

4. 修改配置文件
配置文件的位置：/etc/logstash/conf.d/02-beats-input.conf
将其中的内容都删掉，替换成下面的配置
input {
    tcp {
        port => 5044
        codec => json_lines

    }

}
output{
    elasticsearch {
    hosts => ["localhost:9200"]

    }

}

5.	重启docker容器（大概等5-10分钟，等待服务重启）
docker restart elk

6. 访问Kibana
http://localhost:5601/
```


第一个是使用 Docker pull 一个镜像，那这个镜像其实非常大了，同学们先把这一步给准备好，我来先看一下它的大小。在命令行通过 Docker images 我看这里是排在第一个的，就是他的镜像大概有 1.93 个 G 说大不大说小不小。 OK 那假设第一步咱们大家都完成了镜像拉到了，那我们接下来去 copy 第二个步骤。


第二步的名称非常长，我来跟大家说一下它是什么意思。它这里其实是创建一个 Docker 容器，只不过咱这个容器只用创建一次。当下次大家在用的时候，只要启动当前这个容器就好了，不用再重新创建。所以这条命令同学们只要执行一次就好。它这里创建了一个容器，分别给 kibana elastic search 还有 logstash 指定了它的端口号，并且指定了部分内存运行期的大小。


同学们注意看，这后面有两个参数比较重要，其中第一个参数， elk 是咱创建的这个容器的名称，这个容器的名称是大家在创建的时候可以自己修改的。 OK 后面的这个其实是咱第一步拉取下来的镜像的名称，这个可不能修改，大家不要改错了。 OK 那我们这里把这整条命令给它 copy 下来，然后走到 terminal 里面，把命令行清一下，然后把这行命令打上。 OK 它这里会执行一段时间，大概有 5 分钟左右。那如果机器 8g 内存稍微性能差，那么一点可能会执行个十几分钟。从这个 log 里面看，它现在首先去启动了 elastic searchok 那我们稍等片刻，一炷香的功夫以后，咱再回来。 OK 一炷香的功夫回来了，咱大家可以看到这 log 里面已经提示出 logstash started 然后正在 starting kibanaok 那咱再等待一炷香的时间。好，勒。一炷香的时间到了咱这里，看到它的整个服务都已经启动起来了。
好，我们接下来进入后面的步骤回到 intelligi 里面。第三步是进入 Docker 容器。咱刚才创建的这个容器叫 elk 那就执行这个命令，进入到 Docker 容器里面，修改部分文件内容。我们这里新加一个窗口，重新打开一个窗口，然后在这个窗口中把刚才的命令复制下来。同学们要注意，这个命令只有你在 Docker 启动的时候才能执行。如果你这个 container 它并没有启动起来，那是会报错的。
OK 咱执行这个命令现在就进入了 Docker 环境当中。紧接着咱看需要修改哪个文件呢？这里给出了修改配置文件的位置这个是 logstash 的配置文件，咱把它 copy 一下。 OK 再回来，我们把这个文件通过 wim 指令给它修改一下。 OK 想看到这是文件的默认内容我们要现在把它替换过来，点击一下 I 然后进入 instead 模式。替换之前咱先把所有内容删掉。 OK 删干净了以后，咱回到银泰利 J 里面，从这 13 行到 27 行一字不差，把这几行复制下来。


这几行的改动很简单，比方说 input 是 logstash 的接收端，它会开放一个端口，5044专门接收 lock 请求。这里的 log 格式是 JSON 格式。 OK 咱们再看它的 outputoutput 是指 log stash 会把接收到的 log 信息传送给谁传送给 elastic search ，那这里就是 elastic search 的端口号。 OK 咱们把这段文字给它 copy 下来，然后到命令行中粘贴上来。那接下来就直接保存 wq 直接保存下来。保存完了以后，咱接下来看攻略上面怎么说，要重启 Doc 容器对不对？他这边说了大概等 5 到 10 分钟。好，咱把这行命令复制下来，再回到 terminal 里面把它打上。


先要退出 Docker 容器，再打这个命令。如果你在 Docker 容器里面是不好打的。 OK 咱们退出了 Docker 容器，接着打 restartelk 大家看到刚才启动好的项目，现在在一行退出，走到这里已经退出完毕了，说明这个容器当前已经停止运行了。那接下来我们在后台等它静默重启完，然后再来访问 UI 页面。


OK 咱接着回到攻略，那最后一步是访问 K 班，咱们把这个地址给它复制过来，因为现在整个容器还在重启，所以大家如果尝试着访问 Chrome 打开一个新的 tab 咱进行访问的时候可能会发现这个页面在不停地转，那说明他在后台的重启还没有全部完成，我们再稍等一炷香的时间，然后回来再看。这是重启了三分钟以后的结果。他说 kibana service not ready yet 那说明他还在充气，我们再过半炷香的时间，再回来看一下。好半炷香的时间又过去了，我们重启了足足有五分钟了。
打开 K 班的页面，哇真是桃园仙境。好多功能，好多按钮，一时眼花缭乱，怎么办呢？我们点击这一个，这是咱最常用的搜索 log 的按钮。 OK 那这里看到他让大家 create index 的 pattern 我们怎么来创建呢？大家看这个小滑鼠，把它给它点开。点开之后我们先来定义一个 index pattern 它下面有一些必要的注释，大家可以去参考一下。那咱这里直接用通配符匹配所有的 pattern 然后直接点击 next step 在这里它需要选一个 time filter 那我们直接选第一个 at time step 如果咱不选时间，那在搜索界面是无法根据时间来搜索的。

[http://172.16.136.203:5601/app/management/kibana/indexPatterns](http://172.16.136.203:5601/app/management/kibana/indexPatterns)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/37f72cef-f0e0-4bbb-9636-9a091ba9c3e3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662M7YJSPF%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225803Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID9C05CUuFFehuWxZABqY%2FN%2BhYb12rdB9qizvW%2FkFZp0AiEAik81m6Ou6ORrryf5989RaDvuSA33%2Fh3D4a0VsjVmt3AqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBdJpv%2F61xy2wWG1GircA0ykpCWHKQ3iRZeUzHb%2Fd7vqXD8yC2nKT911LnyN3heUq6sSMm6jO5pmLJMD9We5ayIPf0B1iwljPxrVRO%2FqnaROgaBrEso8hKMjFR%2FLtiufKVKUbCIMj1ax8PZ1CU4bYzVuMdf9DMhWQPvkk0yRiJx6yeau6qIi01ali5pTn97zYSk8%2BwVB%2FirVkId4EWYDiwxqITEJ%2FiDPxso5jauVasGK81ZdXF2aUsYojkgyPbP%2BT8mPAsEloeP4VQ2v8gJ9mgEtDasI%2Ff2lQFmEM%2BIDBupcCKUU7e3u5UeYijNsn0VYCunbV2ghAkrPifK1r0Yn5C%2FQbbxrMnka6iwch8SbUDHKEyGNLC1KrcIEKIvZNLv63sJvyzAOg3%2BcT9rw4bbC9anuCJPcI44SBgaVLjcgi0Cs%2FHqaPI6sUjIqN8JtKf%2FPH7QU8d0%2Bb%2F4j0hRasUgpj3Xpa0mBDhnBkdGCIZvVVNvaRX8fqZNw1cK%2BkJFjv8mgT3n7Wn5XinYnHvjyE5rNFWnC5h2%2BXTkkkYTHSdGanmNkVusYQbcSkyol9thBLgmJRCjqMqoqG9AwXKZ8ggt4pW2xVbp8S3tEhicLqaC5I9bzYNUt%2F3etAuYzYxmoCw%2F749EGB0OI71cNubDzMN23%2F9IGOqUB2H7dno17Fj0hZUHiy0vqhjd3dK7bPdUnSqX3%2BvJzb8OhxianD1sBZwkefnA%2BQki2xnIq1Tcttl%2F5smqIc3prvu%2Bqy6kKntGTx3XHJOA%2BrDxqArKipx1BXQVJe5wvcF4LQy1aPgLVrsY1mVWgDiVT9jFqI0wq%2BoAxJY0RvB7UbNiVd3DiXPZrKjQZ67cXfp4lgj3CVrzqDl2Ih74bR2YmE516i1Pj&X-Amz-Signature=50278c985c292a6b17873aa834170bab0b4cbd2b87b7db18b5fb64828d7f716c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

OK 那点击 create index step pattern 稍等片刻，等它创建整个索引。 OK 到这里说明索引已经创建好了。那接下来我们怎么做呢？同样的还是点击这个 discover 按钮。


这里大家就可以看到当前 kibana 的 log 了，因为我们还没有将斯鲁斯项目集成到 elk 当中，所以 elk 现在就像无源之水，没有数据流入。那么早在 K 班那上面看不到任何信息，同学们不用心急，咱先来一个中场休息。下半场我来带大家去从头到尾改造 sleuth 的应用，把 log 文件输出到 elk 组件里。

```shell
spring.application.name=sleuth-traceB
server.port=62001

eureka.client.service-url.defaultZone=http://localhost:20000/eureka/

logging.file=${spring.application.name}.log

# zipkin的地址
spring.zipkin.base-url=http://localhost:62100
# 采样率
spring.sleuth.sampler.probability=1

info.app.name=sleuth-traceB
info.app.description=test


management.security.enabled=false
management.endpoint.health.show-details=always
management.endpoints.web.exposure.include=*
```


OK 这一节的内容到这里就结束了，我们来稍微回顾一下。在这一节开始的时候，我们简单了解了 erk 组件它都包含哪些部分，然后它的功能是什么？每一部分他负责的内容又是什么。然后咱通过一系列的 Docker 指令创建了一个 elk 镜像，并且修改了配置文件，然后再启动起来的 kibana 项目当中，我们创建了一个 search index 接下来的事儿就交给下一张来处理了。同学们，我们下一张再见。




```shell
=================================logstash.conf============================
# 获取运用的日志 sluth+zipkin
input {
  tcp {
    port => 5044
    codec => json_lines
  } 
}

## 测试输出到控制台：
output {
  stdout { codec => rubydebug }
}


# 输出日志到 elasticsearch
output {
  elasticsearch {
    hosts => ["192.168.13.213:9200"]
    # 用户名密码      
    #user => "elastic"
    #password => "elastic"
    # 通过嗅探机制进行es集群负载均衡发日志消息
    sniffing => true
    index => "zipkin-log-%{index_time}%"
  }
}
```

```shell
<dependencies>
       <dependency>
           <groupId>io.zipkin.java</groupId>
           <artifactId>zipkin-server</artifactId>
           <version>2.8.4</version>
           <exclusions>
               <exclusion>
                   <groupId>org.apache.logging.log4j</groupId>
                   <artifactId>log4j-slf4j-impl</artifactId>
               </exclusion>
           </exclusions>
       </dependency>

       <dependency>
           <groupId>io.zipkin.java</groupId>
           <artifactId>zipkin-autoconfigure-ui</artifactId>
           <version>2.8.4</version>
           <exclusions>
               <exclusion>
                   <groupId>org.apache.logging.log4j</groupId>
                   <artifactId>log4j-slf4j-impl</artifactId>
               </exclusion>
           </exclusions>
       </dependency>

   </dependencies>
```




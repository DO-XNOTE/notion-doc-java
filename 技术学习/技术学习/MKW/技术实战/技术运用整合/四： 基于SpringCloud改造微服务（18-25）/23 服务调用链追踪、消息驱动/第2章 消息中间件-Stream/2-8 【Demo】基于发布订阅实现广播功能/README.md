---
title: 2-8 【Demo】基于发布订阅实现广播功能
---

# 2-8 【Demo】基于发布订阅实现广播功能

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/6250e4a4-e9c4-48e2-b9c5-b1cc83e17774/SCR-20240722-bchv.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YZHLJSGF%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225814Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD1hTFO6wg3kjAdn3%2FvlOT2qVi1tdXG7dB%2FjmykVcXMwwIhAIgg8TvEPEiI0a3RstQHTAjcIPbariuAo90%2FzkjUtBuCKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyYHKc5XyBFJqJkHcoq3APHmNO7QZQUNnheB2%2BKHpULg%2BDE0NHiYyjoH%2BeBpVtSng3AjBhFTVnTj6tY63lLCqIAt8IhSMO%2BSn0x5TYZGeDbHICwU9mv%2Bp3it6KnSi0aBmNKpEAI9j%2BbSsok%2Ba9fgoRRx0CdvCFtYRkUtRmy6ZP9VGsylApxx6LenHZI9cMZy0EvpvNGAMMqTk8dvj6IFlWeq5bGiEPZZySdNNeSfzc5D5tnwYBWRgrH0vaih8GOjIBPb2I0w9%2BGwi2ZgZ6W4zw5FoJJpuqgfrKXWqOkfnqog%2FCpAxiCm4NZpLHjRSCy8mEy33Ed6H2gfCU5mz4%2B7vikGcVYo6CQBHtH5lsikZdmUg2OoCPPDyLztj6De0BuZx%2FUyeuLa%2FaHYbNY6%2F7d5aSuVn5HjnHqhTb9%2FcUmEUAI76vS4gix1ONWYlh55ndPqsxUa1WH3zH37Y3qVUNvHD63ESWN5JnFGDLJwP0BFNdwpy2334QvGvJLh454Ed2cCNO%2BuaILx4TY88wrctqDXl4UYqGJ3x9bUYzRzuPSGtKPAqbGc9njhbTQ%2Bg%2BXJ%2Fgt8W99AdzD2to9qNOXn%2FdJ4FyCf%2FIqWBXa1UwdZ4tKIpsaL8L9uQjnETB%2B%2FpjQG1efGGIik8VuXxRvL6%2Bh9zDEuv%2FSBjqkAd29rbKGbaeG8Zo6qa%2BSK0GafCF%2BAwjkusw%2F2bdfj77eTBQC%2Fof%2FLu%2BMEo0h3wkynK%2B1pLBXmsG9W2r3Lzs1ozJSdRkcAkB5NBvcZky5%2BieE14%2BHFiDcMP%2BmRZyeVbI3YkEWx0aZ5U8sPMuxodrOM%2FZ6lsBkR2fwodZIvwrL%2FzrKH762vX4vhAvbeM2kHmjSsjLwUKTdMUuAuBxhL9W%2BUBBOklN6&X-Amz-Signature=9345f15356a107cac865cc31510d67d3fc6cb190780c8d264ba28bdac5331add&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/fe5246e1-6628-4b07-97d5-b518482b5072/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YZHLJSGF%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225814Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD1hTFO6wg3kjAdn3%2FvlOT2qVi1tdXG7dB%2FjmykVcXMwwIhAIgg8TvEPEiI0a3RstQHTAjcIPbariuAo90%2FzkjUtBuCKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyYHKc5XyBFJqJkHcoq3APHmNO7QZQUNnheB2%2BKHpULg%2BDE0NHiYyjoH%2BeBpVtSng3AjBhFTVnTj6tY63lLCqIAt8IhSMO%2BSn0x5TYZGeDbHICwU9mv%2Bp3it6KnSi0aBmNKpEAI9j%2BbSsok%2Ba9fgoRRx0CdvCFtYRkUtRmy6ZP9VGsylApxx6LenHZI9cMZy0EvpvNGAMMqTk8dvj6IFlWeq5bGiEPZZySdNNeSfzc5D5tnwYBWRgrH0vaih8GOjIBPb2I0w9%2BGwi2ZgZ6W4zw5FoJJpuqgfrKXWqOkfnqog%2FCpAxiCm4NZpLHjRSCy8mEy33Ed6H2gfCU5mz4%2B7vikGcVYo6CQBHtH5lsikZdmUg2OoCPPDyLztj6De0BuZx%2FUyeuLa%2FaHYbNY6%2F7d5aSuVn5HjnHqhTb9%2FcUmEUAI76vS4gix1ONWYlh55ndPqsxUa1WH3zH37Y3qVUNvHD63ESWN5JnFGDLJwP0BFNdwpy2334QvGvJLh454Ed2cCNO%2BuaILx4TY88wrctqDXl4UYqGJ3x9bUYzRzuPSGtKPAqbGc9njhbTQ%2Bg%2BXJ%2Fgt8W99AdzD2to9qNOXn%2FdJ4FyCf%2FIqWBXa1UwdZ4tKIpsaL8L9uQjnETB%2B%2FpjQG1efGGIik8VuXxRvL6%2Bh9zDEuv%2FSBjqkAd29rbKGbaeG8Zo6qa%2BSK0GafCF%2BAwjkusw%2F2bdfj77eTBQC%2Fof%2FLu%2BMEo0h3wkynK%2B1pLBXmsG9W2r3Lzs1ozJSdRkcAkB5NBvcZky5%2BieE14%2BHFiDcMP%2BmRZyeVbI3YkEWx0aZ5U8sPMuxodrOM%2FZ6lsBkR2fwodZIvwrL%2FzrKH762vX4vhAvbeM2kHmjSsjLwUKTdMUuAuBxhL9W%2BUBBOklN6&X-Amz-Signature=15e3a0213bba96d883d6ae7cc7a486073c2f8eb6582a3245e5991658f495bde4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/1edde8c5-0658-4174-9030-d9bcca3065e7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YZHLJSGF%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225814Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD1hTFO6wg3kjAdn3%2FvlOT2qVi1tdXG7dB%2FjmykVcXMwwIhAIgg8TvEPEiI0a3RstQHTAjcIPbariuAo90%2FzkjUtBuCKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyYHKc5XyBFJqJkHcoq3APHmNO7QZQUNnheB2%2BKHpULg%2BDE0NHiYyjoH%2BeBpVtSng3AjBhFTVnTj6tY63lLCqIAt8IhSMO%2BSn0x5TYZGeDbHICwU9mv%2Bp3it6KnSi0aBmNKpEAI9j%2BbSsok%2Ba9fgoRRx0CdvCFtYRkUtRmy6ZP9VGsylApxx6LenHZI9cMZy0EvpvNGAMMqTk8dvj6IFlWeq5bGiEPZZySdNNeSfzc5D5tnwYBWRgrH0vaih8GOjIBPb2I0w9%2BGwi2ZgZ6W4zw5FoJJpuqgfrKXWqOkfnqog%2FCpAxiCm4NZpLHjRSCy8mEy33Ed6H2gfCU5mz4%2B7vikGcVYo6CQBHtH5lsikZdmUg2OoCPPDyLztj6De0BuZx%2FUyeuLa%2FaHYbNY6%2F7d5aSuVn5HjnHqhTb9%2FcUmEUAI76vS4gix1ONWYlh55ndPqsxUa1WH3zH37Y3qVUNvHD63ESWN5JnFGDLJwP0BFNdwpy2334QvGvJLh454Ed2cCNO%2BuaILx4TY88wrctqDXl4UYqGJ3x9bUYzRzuPSGtKPAqbGc9njhbTQ%2Bg%2BXJ%2Fgt8W99AdzD2to9qNOXn%2FdJ4FyCf%2FIqWBXa1UwdZ4tKIpsaL8L9uQjnETB%2B%2FpjQG1efGGIik8VuXxRvL6%2Bh9zDEuv%2FSBjqkAd29rbKGbaeG8Zo6qa%2BSK0GafCF%2BAwjkusw%2F2bdfj77eTBQC%2Fof%2FLu%2BMEo0h3wkynK%2B1pLBXmsG9W2r3Lzs1ozJSdRkcAkB5NBvcZky5%2BieE14%2BHFiDcMP%2BmRZyeVbI3YkEWx0aZ5U8sPMuxodrOM%2FZ6lsBkR2fwodZIvwrL%2FzrKH762vX4vhAvbeM2kHmjSsjLwUKTdMUuAuBxhL9W%2BUBBOklN6&X-Amz-Signature=095221808d671c2753fdf57879bea8458fa017e03e57fcaf1b3f3436c2531360&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/f2e276d7-2ccf-4340-9ac8-652b510c476e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YZHLJSGF%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225814Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD1hTFO6wg3kjAdn3%2FvlOT2qVi1tdXG7dB%2FjmykVcXMwwIhAIgg8TvEPEiI0a3RstQHTAjcIPbariuAo90%2FzkjUtBuCKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyYHKc5XyBFJqJkHcoq3APHmNO7QZQUNnheB2%2BKHpULg%2BDE0NHiYyjoH%2BeBpVtSng3AjBhFTVnTj6tY63lLCqIAt8IhSMO%2BSn0x5TYZGeDbHICwU9mv%2Bp3it6KnSi0aBmNKpEAI9j%2BbSsok%2Ba9fgoRRx0CdvCFtYRkUtRmy6ZP9VGsylApxx6LenHZI9cMZy0EvpvNGAMMqTk8dvj6IFlWeq5bGiEPZZySdNNeSfzc5D5tnwYBWRgrH0vaih8GOjIBPb2I0w9%2BGwi2ZgZ6W4zw5FoJJpuqgfrKXWqOkfnqog%2FCpAxiCm4NZpLHjRSCy8mEy33Ed6H2gfCU5mz4%2B7vikGcVYo6CQBHtH5lsikZdmUg2OoCPPDyLztj6De0BuZx%2FUyeuLa%2FaHYbNY6%2F7d5aSuVn5HjnHqhTb9%2FcUmEUAI76vS4gix1ONWYlh55ndPqsxUa1WH3zH37Y3qVUNvHD63ESWN5JnFGDLJwP0BFNdwpy2334QvGvJLh454Ed2cCNO%2BuaILx4TY88wrctqDXl4UYqGJ3x9bUYzRzuPSGtKPAqbGc9njhbTQ%2Bg%2BXJ%2Fgt8W99AdzD2to9qNOXn%2FdJ4FyCf%2FIqWBXa1UwdZ4tKIpsaL8L9uQjnETB%2B%2FpjQG1efGGIik8VuXxRvL6%2Bh9zDEuv%2FSBjqkAd29rbKGbaeG8Zo6qa%2BSK0GafCF%2BAwjkusw%2F2bdfj77eTBQC%2Fof%2FLu%2BMEo0h3wkynK%2B1pLBXmsG9W2r3Lzs1ozJSdRkcAkB5NBvcZky5%2BieE14%2BHFiDcMP%2BmRZyeVbI3YkEWx0aZ5U8sPMuxodrOM%2FZ6lsBkR2fwodZIvwrL%2FzrKH762vX4vhAvbeM2kHmjSsjLwUKTdMUuAuBxhL9W%2BUBBOklN6&X-Amz-Signature=73c7ee6209669590b1b9e42d4cbd3f103d830cdc1d41ea3a9f9872a1e4c93acd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

hello 慕课网的各位同学们，大家好，在前面一个小节里，咱学习了如何创建一个 consumer 消费者，然后利用 stream 的标签从 rabbit MQ 中的 topic 里拉取消息。那在这个小街里，我们一起搭建一个生产者到消费者的完整链路，实现消息的广播功能。


我们先来看一下本小节的主要内容。第一部分我们要创建一个 producer 这个 producer 就是指消息的生产者，然后为 producer 配置消息的 topic 并且创建相应的 consumer 去监听这个主题。然后消费消息。紧接着咱启动多个 consumer 节点去测试消息的广播。这个测试用例就是先让 producer 发布一条消息到 rabbit MQ 然后看看所有的 consumer 是不是都可以消费这同一条消息。那最后一个内容就是我们大家一起去 rabbit MQ 的管理界面上看一看广播组它长什么样子。好。同学们抄起家伙跟我一起到 intelligj 里面。咱开工了编程使我快乐。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/597ac679-2b57-49c8-875a-a8d35a497e77/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YZHLJSGF%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225814Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD1hTFO6wg3kjAdn3%2FvlOT2qVi1tdXG7dB%2FjmykVcXMwwIhAIgg8TvEPEiI0a3RstQHTAjcIPbariuAo90%2FzkjUtBuCKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyYHKc5XyBFJqJkHcoq3APHmNO7QZQUNnheB2%2BKHpULg%2BDE0NHiYyjoH%2BeBpVtSng3AjBhFTVnTj6tY63lLCqIAt8IhSMO%2BSn0x5TYZGeDbHICwU9mv%2Bp3it6KnSi0aBmNKpEAI9j%2BbSsok%2Ba9fgoRRx0CdvCFtYRkUtRmy6ZP9VGsylApxx6LenHZI9cMZy0EvpvNGAMMqTk8dvj6IFlWeq5bGiEPZZySdNNeSfzc5D5tnwYBWRgrH0vaih8GOjIBPb2I0w9%2BGwi2ZgZ6W4zw5FoJJpuqgfrKXWqOkfnqog%2FCpAxiCm4NZpLHjRSCy8mEy33Ed6H2gfCU5mz4%2B7vikGcVYo6CQBHtH5lsikZdmUg2OoCPPDyLztj6De0BuZx%2FUyeuLa%2FaHYbNY6%2F7d5aSuVn5HjnHqhTb9%2FcUmEUAI76vS4gix1ONWYlh55ndPqsxUa1WH3zH37Y3qVUNvHD63ESWN5JnFGDLJwP0BFNdwpy2334QvGvJLh454Ed2cCNO%2BuaILx4TY88wrctqDXl4UYqGJ3x9bUYzRzuPSGtKPAqbGc9njhbTQ%2Bg%2BXJ%2Fgt8W99AdzD2to9qNOXn%2FdJ4FyCf%2FIqWBXa1UwdZ4tKIpsaL8L9uQjnETB%2B%2FpjQG1efGGIik8VuXxRvL6%2Bh9zDEuv%2FSBjqkAd29rbKGbaeG8Zo6qa%2BSK0GafCF%2BAwjkusw%2F2bdfj77eTBQC%2Fof%2FLu%2BMEo0h3wkynK%2B1pLBXmsG9W2r3Lzs1ozJSdRkcAkB5NBvcZky5%2BieE14%2BHFiDcMP%2BmRZyeVbI3YkEWx0aZ5U8sPMuxodrOM%2FZ6lsBkR2fwodZIvwrL%2FzrKH762vX4vhAvbeM2kHmjSsjLwUKTdMUuAuBxhL9W%2BUBBOklN6&X-Amz-Signature=40a95959405e08d325a078fc55e21782417edf7bb0c8c6b0edad3a5817d8f52f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

996 是我的福报，今天享受福报，先从 cosplay 开始。 cosplay 谁呢？你看咱这边定义了一个 listener 然后 listener 使用了默认的 stream 提供的接口 Sync 咱就 cosplay 它自己创建一个自定义的 topic 实现生产者和消费者的完整链路。


OK 咱回到项目里面，在 com IMock springcloud 下面再创建一个新的文件夹，给它起名叫 topics 以后所有的 topic 全都要放在这里。咱这只是刚开始定义第一个，后面多着呢，万事开头难，任重而道远。咱创建的第一个 topic 不宜太高调，名字起的低调一些，就叫 my topic 类型，这里要把它选成interface 。 OK 那好，这个类创建好了，咱接下来要怎么样定义一个 topic 的名称？ topic 的名称就叫 input 字段名叫 input 然后它的值我们给它叫做 my topic 保持低调的做派。


好，下面咱们 cosplay 一个 listener 那 listener 要是一个 subscriber channel subscriber 是什么意思就是那种可以被订阅的通信通道。 OK 这个方法咱也给它起名叫 input 好了，在 stream 的概念里， input 和 output 它的定义和咱常规理解有那么点不同，它的 input 指的是接收消息的那一段，也就是消费者。那 output 是指生产消息的那一段，也就是生产者很多同学可能会把关系搞反了，以为 input 是生产消息不对的，这里是消费消息。


OK 那咱这个 topic 的通信通道创建好了以后，给它来一个注解，应该是谁是 input 对不对？好，咱的 input 的名称也就是 topic 的名称，就是刚才创建的 my topicok 那咱自定义的 topic 创建好以后，我们走到 stream consumer 里，同样的把 consume 方法给它 copy 一下，然后复制这里给方法改一个名称叫 consume my messageokay 然后 log 也给它加一个不同的信息，叫 my message consumed successfully 但是这个 listener 的名称，咱也要把它变到自己的 topic 上面，我们把 my topic 引入进来，然后添加 input 好，这里就创建好了。那接下来还需要怎么样？还需要把这个信道绑定声明在方法的头上，给它声明叫 my topic.classok 到这里，一个自定义的消息的消费者就已经创建好了，接下来咱来创建这个生产者。


那咱把生产者定义在哪里呢？依然找到 my topic 方法，在这个方法里面，在这个类里定义一个新的生产者。那生产者的方法返回的这个类就不同了，它不是 subscriber channel 了，而是 message channel 这个 message channel 它在类的继承结构上实际上是 subscriber channel 的父类，我们可以点进 subscriber channel 看一下它的继承结构它是继承自 message channel 的。 OK 咱回退回来。那这里给 message channel 的方法名称定义为 output 同时在它上面加一个注解，还能是 input 吗？同学们不是啦，这里是 output 注解，这是一对 input 代表消费者， output 代表生产者。


那咱同样的也要给生产者指定一个 topic 对不对这里指定谁呢？同学们看咱的消费者是 my topic 那理所应当的生产者就应该是 my topic 了对吗？这个假设是正确的吗？同学们好，那我们不妨这样试验一下，因为在咱们的观念里面，一个消费者和生产者，他肯定 topic name 是相同的，所以我们不妨把他们两个也设置为相同。但是我这里要加一个标记，爆雷了，咱看待会这种配置会怎么样？爆雷，然后我们再回过头来把它修复好。


OK 那咱这个 topic 已经定义完成了。接下来要创建一个 controllercontroller 是做什么作用的呢？那就是通过一个 HTTP 调用， controller 会在底层调用它的生产者发送一条消息到 rabmq 当中。我们把这个 controller 同样也给定义在 Bits 文件夹下面。 business 文件夹下面给它起名就叫 controller 你看咱项目的起名都非常的朴实无华。 OK 那给 controller 的头顶上加一个 rest controller 的 annotation 同样的 sl four G 不要忘伤砸 log 可是非常重要的。那接下来我们定义一个方法，专门来接收 HDD B 的请求，调用 producer 它的方法名称，我们就给它起名叫 send messageok 那它接收什么参数呢？我们给它声明一个 string 类型的参数叫 body 这就是消息体 okay 给它用 request 包起来。那它的值 value 就是 body 实际上即使你不写这个 request parama 它也会默认使用 filter 的名称来作为 request param 的。但是咱这里建议还是把它写上，为什么？因为咱的属性名称可能会发生变动的，这样你一旦变动以后，方法属性名也跟着变动了，这样会给前端同学造成一定的麻烦。所以我们这里也就尽量都把 request param 给它加上。


好了，接下来咱要给这个方法指定一个路径，我们把它作为 post 方法指定 post mapping 然后它的路径咱就简单的写一个 send 好了。 OK 那紧接着我们要把生产者给它注释进来，那生产者我们注释的方式也非常简单，就使用 out wired 注释，谁进来 my topic 只要把它加进来就可以了，那我们给它起名叫 producer 那这个 my topic 只是一个接口，那它怎么来调用呢？同学们不用急，咱前面已经把信道绑定上了，它在上下文中已经被初始化好了，我们只用调用 producer 的什么方法 output 方法，然后直接发送一个 send 就可以了。


这个 sand 我们要把 string 类型转化成一个 messaging 的类型，怎么转化调用一个工具类，这个工具类的名称叫什么呢？叫 message builder 你看这里有很多个 message builder 咱是调用哪一个呢？咱调用这一个。大家看好这个包路径是 messaging 下面的 support 包下面的 message builder 不要调用错了，调用到其他的可能是会找不到方法的。调用 messaging 包下的，然后调用它的什么方法？ H with the payload 把咱的 body 传入进去，然后在后面调用一下它的 build 方法，这样的话我们的消息就可以发送出去了。


到这里似乎全部都配置好了，我们应该可以去尝试着启动下项目了。但是别忘了，咱这里好像还埋了一颗雷，在哪要爆雷了？我们看看它究竟会怎么个爆法。我们来到 stream application 这里，把项目启动起来，稍等半炷香的时间，到现在为止还一切正常。看到 spring 成功一半往下走，右还没走两步，就摔跤了。


什么意思呢？我们看它的报错，我把屏幕放大一些，你看它的报错信息 invalid bin definition with name my topic 它说咱刚才配置的 my topic 这个 bin 它的定义不合法。为什么呢？它下面有句解释， bin definition with this name already exist 当前这个命名的 bin 已经有一个相同名称的存在了。


为什么呢？我们再回头看一下，走到刚才爆雷的地方，大家看，实际上咱以为它是通道的名称，对不对？它是 topic 的名称，这样理解是没错的，只不过它这里还有一个其它的用途，也就是说它会把你传入的这个 topic 名称当成一个 bin 的 name 那咱这里一个 input 的标签和一个 output 标签相当于声明了两个 bin 那这两个 bin 都有了同样的 name 那是不是 spring 在启动的时候肯定要报错了，那怎么办呢？有一个解决办法，我们来看，咱给这个 input 和 output 起不同的名字，就可以完美的解决这个问题了。


我们现在给 output 起一个其他的名字 output 给它起名叫 my topic producer 同理这个 input 我们也给它起一个和下面遥相呼应的名字叫 my topic consumer 但是这样看下来似乎有点不对，哪里不对。


你这两个 topic 之间好像没有进行关联起来，你发你的消息，我消费我的消息，但是你发消息的地方和我消费消息的地方好像不在一块。那怎么办才好呢？山人自有妙记，咱把这两个不同的信道绑定在一起不就可以了吗？那同学问在哪绑定啊？那当然是在咱的配置文件里面绑定了。 OK 我们要大显身手了，流出一块空地闪开。闪开闪开。好，我们在这里开始发功了，怎么来绑定？我们使用两个配置属性，把两个信道绑定到同一个 topic 上来。那这个属性以 spring 开头，后面跟谁呢？ cloud 再后面跟 stream 然后 bundings 那接下来后面跟谁呢？我们跟这个咱把 topic 的名称给它 copy 下来。 OK 前面都是定制好的内容，到了后面，这里有咱要把自己的 topic 给它绑定过来，就是信道的名称，也就是说这个信道将要被重定向到一个哪里呢？一个 destination 后面在等号以后，那就是大家指定真正 topic 的地方了。

```docker
spring.application.name=stream-sample
server.port=63001

#RabbitMQ 连接字符串
spring.rabbitmq.host=172.16.136.217
spring.rabbitmq.port=5672
spring.rabbitmq.username=guest
spring.rabbitmq.password=guest

# 绑定不同的信道（channel）到 broadcast
spring.cloud.stream.bindings.myTopic-consumer.destination=broadcast
spring.cloud.stream.bindings.myTopic-producer.destination=broadcast


management.security.enabled=false
management.endpoint.health.show-details=always
management.endpoints.web.exposure.include=*

----------------------------------------------------------------------------------------

public interface MyTopic {

    String INPUT = "myTopic-consumer";

    String OUTPUT = "myTopic-producer";

    @Input(INPUT)
    SubscribableChannel input();

    @Output(OUTPUT)
    MessageChannel output();

}

----------------------------------------------------------------------------------------
@Slf4j
@EnableBinding( value = {
        Sink.class,
        MyTopic.class
}
)
public class StreamConsumer {

    @StreamListener(Sink.INPUT)
    public void consume(Object payload) {
       log.info("message consumed successfully,  payload = {} "  + payload);
    }

    @StreamListener(MyTopic.INPUT)
    public void consumeMessage(Object payload) {
        log.info("message consumed successfully,  payload = {} "  + payload);
    }
}


----------------------------------------------------------------------------------------
@RestController
@Slf4j
public class Controller {


    @Autowired
    private MyTopic producer;

    @PostMapping("send")
    public void sendMessage(@RequestParam(value = "body") String body) {
        producer.output().send(MessageBuilder.withPayload(body).build());
    }

}
```


我们把这个 topic 指定成 broadcast 广播的意思。好，那第一个信道已经被绑定到了 broadcast 接下来我们把第二个信道绑定好，第二个信道的名称是 my topic 杠 producerokay 那现在这两个信道都被绑定到了 broadcast 我们在这里加一个注释，方便大家回顾。因为接下来我们还要在下面添加很多很多不同的信道，我们的注释写绑定 channel 到 broadcast 把它复制过来。 OK 那通过这样的配置，我们就可以把不同的信道绑定到相同的 topic 当中。当生产者发送消息到指定的 topic 以后，我的 consumer 就可以去消费这条消息了。 OK 那咱这个配置好以后就可以去尝试启动项目了，咱在 stream application 里面把这个项目启动好。


接下来我们再回到配置文件里面干什么？改端口，我们把端口从 63,001 改成63,000，再启动一个实例。这样的话我们就有了两个 consumer 我们要验证的是什么呢？我们要验证。当你发送了一条消息以后，这个广播消息会不会被两个 consumer 同时消费？ OK 这里看到两个 instance 全部启动起来了，咱把 log 清空一下。


好嘞，我们到 postman 里对方法发起一个调用，这个方法会被发送到 local host63,000。然后它的路径是 send 也就是咱刚才配的 controller 里，它的 body 我们给它传入一串 payload 叫 helload broadcast frog the cast 广播。你好，现在开始广播好，发送这里显示200，那信息应该已经被生产者生产出来了。


我们看一下这两个 instance 是不是都有 log 打出。 OK 这个 instance 已经打出了 my message consumed successfully 证明它成功消费了一条消息。那另一个 instance 我们切换过去看一下。 OK 这里也已经打出了一条消息，完美通关，我们的广播测试到此结束。但是咱本小节的内容还没有结束，我们接下来要去 rabbit MQ 的界面看一下广播消息组它长什么样子。


好，我们来到 rabbit MQ 的界面，然后点击上面的 exchanges 这个 tab 下面我们看到有很多 exchange 都出现在这个列表里了，我们找谁呢？大家仔细盯好叫 broadcast 在哪里？在这了。在这你看它的类型这里有一个 type 它的类型是什么 topic 那就是我们刚才把信道绑定上的 topic 好，咱点进去往下走。 OK 在这里大家就可以看到它 bindings 的 to list 这里有两个 instance 那这两个 bindings 分别代表什么含义呢？实际上 exchange 和 Q 之间的绑定就是这个 binding 词。我们不妨点开一个 Q 的 tab 页面。


我们看到这里最上面的两个 broadcast 这两个 Q 的名称是不是和 exchange 下面的 bindings 中的名称一模一样？那在 bindings 这边出现的每一个 item 实际上都是对应的这里的一个 Q 那这个 Q 又对应着谁呢？我们不妨打开其中的一个 Q 来看一下。


我们滚到下面，往这个 Q 里发送一个 message 叫 Q test 好，我们 push 回去看看后台是哪个服务接收到了。这里有两个 stream 的服务。你看，其中只有一个服务接收到了。 OK 那是大家是不是猜到了一二了呢？这两个 Q 是对应谁，就是对应咱连上的这两个 consumer 了。那我们这里不妨打开另一个Q ，给它 push 一个 test to 走。你我们看一下另一个 Q 果然你看他说到了，所以这里每个 Q 实际上都对应了后台的一个监听队列。这样的话大家是不是就把 exchange 还有 Q 以及它们中间的这个 bindings 的关系理清楚了呢？ OK 同学们，那这一节的 demo 就到此结束了，我来带大家回顾一下今天的内容。


在这一节当中，我们创建了一个自己的 my topic 然后声明了 input 和 output 分别代表是消费者和生产者。在这里，大家需要给每一个声明的信道指定一个不同的名称，否则的话启动会报错。那如果大家想把两个不同的信道绑定到同一个 topic 当中，那就要借助于 stream 中的这行配置来完成信道的绑定。比如咱这里就把 producer 和 consumer 都绑定到了 broadcast 这一个 topic 上来，通过这种方式，我们就可以实现一个简单的广播功能。


OK 同学们，那这一节的内容到这里就结束了。在接下来我将要用图文课程跟大家做一个案例拓展，看一看在阿里新零售的业务中是如何利用广播这种场景来处理商品发布的。再往后一个小节，我将带大家去搭建一个轮询单播的示例。也就是说在整个集群范围内，一个生产者生产出来的消息有且仅有一个消费者会去处理它，这要借助于消费组的概念来完成了。那预知后事如何呢？且听下回分解。同学，我们下一节课程再见。





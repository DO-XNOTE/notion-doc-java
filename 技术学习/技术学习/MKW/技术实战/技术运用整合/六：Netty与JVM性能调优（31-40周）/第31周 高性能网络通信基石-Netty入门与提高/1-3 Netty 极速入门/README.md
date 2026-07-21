---
title: 1-3 Netty 极速入门
---

# 1-3 Netty 极速入门

1-3Netty急速入门
Netty急速入门
现在，我们开始编写一个最简单的Netty示例， 在这之前我们先熟悉一下最基本的编码实现步骤
Netty实现通信的步骤：   客户端与服务器端基本一致创建两个的NIO线程组，一个专门用于网络事件处理接受客户端的连接），另一个则进行网络通信读写。
创建一个ServerBootstrap对象，配置Netty的一系列参数，例如接受传出数据的缓存大小等等。
创建一个实际处理数据的类Channelnitializer，进行
初始化的准备工作，比如设置接受传出数据的字符
集、格式、已经实际处理数据的接口。
绑定端口，执行同步阻塞方法等待服务器端启动即
可。
Netty的使用非常简单，仅仅引入依赖即可快速开始
dependency>
<g roupd>ionetty</groupd>
<artifactd>netty-al</artifactd>
<version>4.1.12.Final</version>
</dependency
Netty Server
NettyServer端需要编写Server与ServerHandler两个核心类！
Server:
oackage combfxy·nettyquickstart
import io.nettybootstrap.ServerBootstrap
import io.netty.channel.ChannelFuture
import io.netty.channel.ChanneInitializer
import io.netty.channelChanneloption:
import io.netty.channelEventLoopGroup
import io.netty.channel.nio.NioEventLoopGroup
import io.netty.channel.ssocketSocketchanneL
import io.netty.channel. socket nio.NioServerSocketchanne
关  Server
author Alienware
米
/
oublic class Server
public static void main(Stringl args） throws
InterruptedException
//1创建两个线程组：一个用于进行网络连接接受的另一个用于我们的实际处理（网络通信的读写
EventLoopGroup bossGroup = new NioEventLoopGroup）:
EventLoopGroup workGroup=newNioEventLoopGroup）
//2通过辅助类去构造server/client
ServerBootstrap b = newServerBootstrap//3，进行NioServer的基础配置
[//3.1绑定两个线程组](https://3.xn--1-2p6asa278km29an5fbb0g/)
bgroup(bossGroup， workGroup
[//3.2因为是server端](https://3.xn--2server-f73kx65d058axyzc/)，所以需要配置Nioserversocketchanne
·channeL(NioServerSocketchanne.class）
[//3.3设置链接超时时间](https://3.xn--3-np5bl2ea1173alppc1chrvn6b/)
option(Channeoption.CONNECT TIMEOUT MI
LLIS,3000）
[//3.4设置TCPbacklog参数=sync队列+acce](https://3.xn--4tcpbacklog=sync+acce-pe98ap2vtx4is1vgq5uchuyc/)
pt队列
option(channeloption.SO_BACKLOG，1024）
[//3.5设置配置项通信不延](https://3.xn--5-ro6a91dk93amj2ba671tf5h5wcv40a/)
chidoption(channeloptionTCP NODELAY
true）
[//3.6设置配置项接收与发送缓存区大小](https://3.xn--6-to6am9nirap7sepdxpbz98aekd1w3gq2aa8802buqmewem89a/)
childoption(channeoptionSO_RCVBUF，1024*32）
chidOptionChanneoptionSO SNDBUF124*32）
[//3.7进行初始化Channelnitializer](https://3.xn--7channelnitializer-7b83ak6kgs8bd27stlkb/)，用于构建双向链表“pipeline”添加业务handler处理
childHandler(newi ChanneInitializer<Socketchannel>
override
protected void initchanne(SocketchanneL ch） throws Exception
[//3.8这里仅仅只是添加一个业务处理器serverHandler](https://3.xn--8serverhandler-566vum5iq3ha458qya743eo3pbipyu1f0mzbud8ac24mq2l/)（后面我们要针对他进行编码
chpipeineCaddLast(new ServerH
andler(））；
//4服务器端绑定端口并启动服务使用channe级
别的监听close端口阻塞的方式
ChannelFuture cf = b.bind(8765）sync）cfchanne）closeFuture）Sync）
//5释放资源
bossGroup shutdownGracefullyC）
workGroup ShutdownGracefuLlyC
ServerHandler
ackage com-bfxynetty.guickstart
import io.netty.buffer.ByteBuf
import io.nettykbufferUnpooled
import io.nettychannel.ChannelHandlercontextimport io.netty channe. ChanneInboundHandlerAdapter；
sServerHandter
大@author Alienware
/
oublic class SServerHander extends ChannelInbound
HandlerAdapter
channetActive
水  通道激活方法
/
override
public void channelActivechanneLHandlerconte
xt ctx）throwsEException t
Systemerrprintn“serverchanneactivechanneRead
米  读写数据核心方法
override
pubic void channelRead(ChanneHandlercontext
ctx，Object msg） throws Exception人
//1读取客户端的数据（缓存中去取并打印到控制台）
ByteBuf buf =（ByteBuf） msgi
byte reuest =new byteLbufreadableBytes(）；
buf.readBytes(request）
String requestBody = new SString(requestutf-8）；
Systemerrprint LnServer: +reguestBo
dy）:
//2返回响应数据
StringresponseBody=返回响应数据，”+requestBody
ctxwriteAndFushUnpooled copiedBufferr
esponseBody·getBytes）））
exceptioncaught
水  捕获异常方法
/
override
public void exceptionCaught(ChanneLHandlerCon
text ctxThrowable cause） throws Exception人
ctx.fireExceptionCaught(cause）
NettyClient
NettyClient端需要编写Client与ClientHandler两个核心类！
Client:
oackage combfxy·nettyquickstart
import io.netty.bootstrap.EBootstrap
import io.netty.buffer.Unpooled
import io.netty.channel.ChannelFuture；
import io.netty.channel.ChannelInitializer
import io.nettychannel.Channeloption
import io.netty.channel.EventLoopGroup
import io.nettychannel.nio.NioEventLoopGroup
import ionettychannel: socketSocketchanne
import io.netty.channel.socket nio.NioSocketchannel
$client
* @author Alienware
米
大
public class Cclient
public static void main(Stringl args） throws
InterruptedException t
//1创建两个线程组：只需要一个线程组用于我们的实际处理（网络通信的读写）
EventLoopGroup workGroup = new NioEventLo
opGroup）
//2通过辅助类去构造cient，然后进行配置响应的配置参数
Bootstrap k 三new Bootstrap）
b·groupworkGroup
channeL(NioSocketchanne. cass）
optionChanne LoptionCONNECTTIMEOUT MILLIS，3000）
option(channeloption.SO_RCVBUF，102432）
option(Channeloption.SO_SNDBUF，102432）
[//3.初始化channelInitializer](https://3.xn--channelinitializer-6b83ak6kgs8b/)
handler(new Channelnitializer<Socketchannel>（）
aoverride
protected void initchanne(Socketchan
nel ch） throws Exception t
[//3.1](https://3.0.0.1/)  添加客户端业务处理类
chpipeline）addLast(new CientH
andler(））；
//4服务器端绑定端口并启动服务；使用channe级别的监听close端口阻塞的方式
ChanneFuture cf = b.connect(127.0.0.18765）syncUninterruptibly
//5发送一条数据到服务器端
cfchannetCwriteAndFtushUnpooled copie
dBuffer(hello netty!getBytes(）））；
//6休眠一秒钟后再发送一条数据到服务端
Thread.sleep(1000）；
cf channetC·writeAndFushUnpooedcopie
dBuffer(hello netty again!.getBytes(）））
//7同步阻塞关闭监听并释放资源
cfchanne）·closeFuture·syncO
workGroupshutdownGracefully
ClientHandler
package com.bfxynettyquickstart
import com.bfxynetty.serialized. marshaling.Resp
onsei
import ionettychannel.ChanneHandlercontext
import io.netty channe. ChanneInboundHanderAdapter；
import ionettyutil.Referencecountutil
CtientHander
* dauthor Aienware
/
oublic class ClientHandler extends channenboundHandlerAdapter
水  channeActive
水  客户端通道激活
/
override
public void channelActive(channeLHandlerconte
xtctx）throwsException t
Systemerr-printinclient channe active大
channeRead
水  真正的数据最终会走到这个方法进行处理
/
Goverride
public void channelRead(channeHandlercontext
ctx，Object msg） throws Exception t
//固定模式的tryfinally
//在try代码片段处理逻辑，finaly进行释放缓存
资源，也就是Objectmsg（buffer）
tryt
Response resp = （Response） msg
Systemerrprintn(client:  +resp
getId(）+       respgetName）       + resp·getReponseMessage）
大finaly t
Referencecountutil. release(msg）
exceptioncaught
水  异常捕获方法
Goverride
public voidexceptioncaught(channeLHandlercontext ctx，Throwable cause  throws Exception tctx.fireExceptioncaught(cause）；
本节课程小结
到此为止，我们已经对Nctty有了一个初步的认知；期望没有接触
过Netty的小伙伴按照老师给出的示例代码能够快速的实现服务器与客户端的数据通信！

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/75792d62-c714-4656-a88c-cdce629ce319/2020-09-17_191742.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TWDBBDFO%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230004Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCOXupGz20Pnds9Jv5L3YUJKbBwWE8olPlwAv4jwkSISQIgEoHRJaJQMwOOqY630SvQt%2FsSLfl%2Fm0GikyNbimEFkNAqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAicX2Ztuv%2BPUeMbKCrcA28pBD6S4PooOIT58IoxMilCJR1XSG6VDMN4JRt0bZkd35FO%2FPoCBPhoqf%2BKObiPoV8ajniJKmLEGGLXuZtE6t3Ff%2BEJiOnhT6Bh9nRJTz%2B4jRd2H730eyQ2kvSB%2BzUVZ%2F3kreTsvtE22HEy8qOkjTX%2Bo3aSo6RNFqPWQd5OlLsr8cVlpSg0do%2Bt7yF1lBf0YL4jxV3t1Zi3AQQBPdk6CVrn0WrZJ2Dx0u1t4y7iHXxVG4jUmGZvztxkNNse5xNo8hfPRk%2BiA5LSwH0DEKMyVupmTMJi8ETYlIQeaG84535CzhN6osp3GFTG9uiYLgCNBWeMXjxYja%2BYfLsows%2F7TxJo2uHMXCTWxH%2FSOw7%2FUMQeF8LZsO%2Fl2JnW4%2FIXgujKsFVkrFdI%2BHLtcoNWTevFQ5MV9x5SoiVeDOlhkeVa8s86iZrkFtdyxivRkLFU9ZE%2BqMhUQn1FD98GnivOcdaQ0yri5shV2TBLCJQVDthc4XbZh%2FZ%2BuLG9vgiJwOQ7xeu5lkGiJs6wyzetWrFyasyDxbar6NvWWkWCSkul3CIPaS4MsHJDwAP6KTbljyGUBh9ASPmajTaVj9FhAqlYkCDIPaNVkzEcOzQaoMBSgdkVzRugp%2Fn7OdEUhrBNaphRMKy3%2F9IGOqUBnNohTbpNVsGUH2%2B6CAT%2Fuy1NfO56VI4BRl6wtEIIIbVX%2BeIg5XO4fdcXYgjRzhdXYRmpWGHynxYuTxegmz9SBabEjywxc5xG5Agzc9djH%2FOg7GqT33z%2Fv%2FfH7IZQEScq6jjXa784YrlkF1sJzkEoPGRZ1n%2FFitAqFC1Ik5ab7bkbOt96NSKo2a4PXVxVHX2SCR76vzf7rItNRvniWKjOE%2FB3dnk3&X-Amz-Signature=951fc06ee165bed127049f52b2f8cefe535dac52e15f1b71d7e27644d0a6b0d1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



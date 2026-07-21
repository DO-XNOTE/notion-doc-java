---
title: 3．请详述TCP三次握手的全过程，并且如果没有第三次握手会有什么问题？
---

# 3．请详述TCP三次握手的全过程，并且如果没有第三次握手会有什么问题？

TCP三次握手的全过程如下:

1. 客户端向服务器端发送一个SYN Segment,标志位置1,Sequence Number为x;
1. 服务器端收到SYN Segment后,需要对这个SYN Segment进行确认,向客户端发送一个SYN/ACK Segment,标志位SYN=1,ACK=1,Acknowledgment Number为x+1,Sequence Number为y;
1. 客户端收到服务器的SYN/ACK Segment后,需要进行确认,向服务器发送一个ACK Segment,标志位ACK=1,Acknowledgment Number为y+1。
到此,三次握手完成。

如果没有第三次握手,会出现以下问题:

1. 服务器端无法确认客户端是否正确收到了服务器的SYN/ACK Segment。服务器端会维持这个半开连接的状态,资源被占用但无法使用。
1. 客户端由于没有收到服务器的确认,会超时重传SYN Segment,服务器端会收到重复的SYN。
1. 导致双方都无法正常建立连接,陷入循环中。
所以,三次握手的第三步ACK是必需的,可以让双方都确认对方正确收到了對方的确认,完成TCP连接的建立。



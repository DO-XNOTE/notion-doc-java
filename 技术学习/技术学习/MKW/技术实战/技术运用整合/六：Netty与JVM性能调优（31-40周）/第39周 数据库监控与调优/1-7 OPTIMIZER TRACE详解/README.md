---
title: 1-7 OPTIMIZER TRACE详解
---

# 1-7 OPTIMIZER TRACE详解

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/4f6795df-e680-477e-8a77-c2ce5c08dfff/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MNRO6NA%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230209Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCBUqXZFHe3bI9aLlDXFUy3n9h65QOIbgFG2NYMDC3bMAIhAKbLsDn5W3nFgCDsqe2Cf%2Bf63NYx3X%2BtruZhuaxMPh51KogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz3yXCKFHJxoY9TPPQq3ANeoHUEG4OnqQiQjQimDUP3j2RWTnjM6Izc1HNUI8wpfjZClTL4WvZbKykAgE7KYXAgPKxy%2FHcsxFp2R6pFBqT2T%2BZ5zPxf4mJYpUe%2BSyTPHQaDNjDehykcn2Pc%2FFaOZrTIdpJgRryGIIRPPC9aU1jse9fHSLa%2FaRBUv4xaauQ58jzWjpKP7%2F2Z4gujOBBGZq6b%2F%2BShbT%2FRrQF3DPct9NjR%2Bivg2wBmmU%2B%2B%2B8QurzNf4PtoUXGbGFmueSZmiclMW2HXiqAwVrT758Whrf70Am8iQf86QacuLSs2OSnY1q1PNPVZzqj6lCx5UYoGroHDY2KvCvxLFbj9zTKzkdNxDLvisM3MbcUKa1YhFmXKBve90OVCtpSoR1%2FoQ8WZH%2FUw0KvNt0mlxF%2F2jpCM8TTDz5MpfKCw1Ik18dWLNNJPnw7QebA2Z2X9ArLSi6AutZbzZ4zVbGtmcoDemQPAyt6OIxJSbmG17ZwHdqUlwbWWCpOoIIjz3d7xq2SH0MFjhFhQNwhuKY%2FgobuCNw%2BkF5ICQqY6vEDDPGxyjmts8%2FNsir2kjfF5q6fbJVYoLHdpB442HUTuBPlM8PBJVLGunI2B8lZHnrHCj9QoOvGm7IOtOKr3aKM1j9LAbFO5L2qLZTDEuf%2FSBjqkAdiSYHC8G2nQVncMTQEOSjPPK2reyHCaWYk45LXQOh7wXLEWStIynAtsuFc%2Bv1WQ%2FGmvmFA8%2FmcVhmjOXOyHe1CIMoQz6H7%2BLm2wLopmSC2sycSR%2FoU7ZhnAPlNF5GWNfpWSpxW7XWi9YGKrOhnPAx%2Fy%2FfsCOjIk9Nf6rEqJn14h0aIIXGwIAY52Ekxn%2Fv1ML3x%2ByYik5a5ENac97QC7dYLu2rnQ&X-Amz-Signature=10a16865dfafc7e087094f70b2ea2f289bf7ad0d0b32b458de872c4dc9a74111&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/6369a9fd-58c1-4295-adb3-c6892b57c806/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MNRO6NA%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230209Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCBUqXZFHe3bI9aLlDXFUy3n9h65QOIbgFG2NYMDC3bMAIhAKbLsDn5W3nFgCDsqe2Cf%2Bf63NYx3X%2BtruZhuaxMPh51KogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz3yXCKFHJxoY9TPPQq3ANeoHUEG4OnqQiQjQimDUP3j2RWTnjM6Izc1HNUI8wpfjZClTL4WvZbKykAgE7KYXAgPKxy%2FHcsxFp2R6pFBqT2T%2BZ5zPxf4mJYpUe%2BSyTPHQaDNjDehykcn2Pc%2FFaOZrTIdpJgRryGIIRPPC9aU1jse9fHSLa%2FaRBUv4xaauQ58jzWjpKP7%2F2Z4gujOBBGZq6b%2F%2BShbT%2FRrQF3DPct9NjR%2Bivg2wBmmU%2B%2B%2B8QurzNf4PtoUXGbGFmueSZmiclMW2HXiqAwVrT758Whrf70Am8iQf86QacuLSs2OSnY1q1PNPVZzqj6lCx5UYoGroHDY2KvCvxLFbj9zTKzkdNxDLvisM3MbcUKa1YhFmXKBve90OVCtpSoR1%2FoQ8WZH%2FUw0KvNt0mlxF%2F2jpCM8TTDz5MpfKCw1Ik18dWLNNJPnw7QebA2Z2X9ArLSi6AutZbzZ4zVbGtmcoDemQPAyt6OIxJSbmG17ZwHdqUlwbWWCpOoIIjz3d7xq2SH0MFjhFhQNwhuKY%2FgobuCNw%2BkF5ICQqY6vEDDPGxyjmts8%2FNsir2kjfF5q6fbJVYoLHdpB442HUTuBPlM8PBJVLGunI2B8lZHnrHCj9QoOvGm7IOtOKr3aKM1j9LAbFO5L2qLZTDEuf%2FSBjqkAdiSYHC8G2nQVncMTQEOSjPPK2reyHCaWYk45LXQOh7wXLEWStIynAtsuFc%2Bv1WQ%2FGmvmFA8%2FmcVhmjOXOyHe1CIMoQz6H7%2BLm2wLopmSC2sycSR%2FoU7ZhnAPlNF5GWNfpWSpxW7XWi9YGKrOhnPAx%2Fy%2FfsCOjIk9Nf6rEqJn14h0aIIXGwIAY52Ekxn%2Fv1ML3x%2ByYik5a5ENac97QC7dYLu2rnQ&X-Amz-Signature=22c5c4986e6730bf7e2222925e165bd24fbbad6e126c1e912fdc403311928197&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/fcf20cc0-d446-472f-b946-dfb0bdda6f00/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MNRO6NA%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230209Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCBUqXZFHe3bI9aLlDXFUy3n9h65QOIbgFG2NYMDC3bMAIhAKbLsDn5W3nFgCDsqe2Cf%2Bf63NYx3X%2BtruZhuaxMPh51KogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz3yXCKFHJxoY9TPPQq3ANeoHUEG4OnqQiQjQimDUP3j2RWTnjM6Izc1HNUI8wpfjZClTL4WvZbKykAgE7KYXAgPKxy%2FHcsxFp2R6pFBqT2T%2BZ5zPxf4mJYpUe%2BSyTPHQaDNjDehykcn2Pc%2FFaOZrTIdpJgRryGIIRPPC9aU1jse9fHSLa%2FaRBUv4xaauQ58jzWjpKP7%2F2Z4gujOBBGZq6b%2F%2BShbT%2FRrQF3DPct9NjR%2Bivg2wBmmU%2B%2B%2B8QurzNf4PtoUXGbGFmueSZmiclMW2HXiqAwVrT758Whrf70Am8iQf86QacuLSs2OSnY1q1PNPVZzqj6lCx5UYoGroHDY2KvCvxLFbj9zTKzkdNxDLvisM3MbcUKa1YhFmXKBve90OVCtpSoR1%2FoQ8WZH%2FUw0KvNt0mlxF%2F2jpCM8TTDz5MpfKCw1Ik18dWLNNJPnw7QebA2Z2X9ArLSi6AutZbzZ4zVbGtmcoDemQPAyt6OIxJSbmG17ZwHdqUlwbWWCpOoIIjz3d7xq2SH0MFjhFhQNwhuKY%2FgobuCNw%2BkF5ICQqY6vEDDPGxyjmts8%2FNsir2kjfF5q6fbJVYoLHdpB442HUTuBPlM8PBJVLGunI2B8lZHnrHCj9QoOvGm7IOtOKr3aKM1j9LAbFO5L2qLZTDEuf%2FSBjqkAdiSYHC8G2nQVncMTQEOSjPPK2reyHCaWYk45LXQOh7wXLEWStIynAtsuFc%2Bv1WQ%2FGmvmFA8%2FmcVhmjOXOyHe1CIMoQz6H7%2BLm2wLopmSC2sycSR%2FoU7ZhnAPlNF5GWNfpWSpxW7XWi9YGKrOhnPAx%2Fy%2FfsCOjIk9Nf6rEqJn14h0aIIXGwIAY52Ekxn%2Fv1ML3x%2ByYik5a5ENac97QC7dYLu2rnQ&X-Amz-Signature=5724ac374daf3e8d8980bff38dff9827aad494aef401811fecbd4b3ce390c342&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

大家好，我是大木。这节课来看到分析 SQL 的又一款神器，叫做 optimizer trees，发一阵中文叫做优化剂跟踪，它可以跟踪优化剂做出的各种决策，让我们了解优化器的执行细节，进而帮助我们理解 SQL 的执行过程，并去优化SQL。关于 optimized trees，我也写了一篇手记来看一下。首先， optimize treats 是 MySQL 5. 6 才引入的一项功能，对于早期的 MySQL 是没有办法使用的。一旦开启 optimizer trees 之后，可以分析这些SQL。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/758af57e-4a32-4395-9dd5-2ebdb2256272/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MNRO6NA%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230209Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCBUqXZFHe3bI9aLlDXFUy3n9h65QOIbgFG2NYMDC3bMAIhAKbLsDn5W3nFgCDsqe2Cf%2Bf63NYx3X%2BtruZhuaxMPh51KogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz3yXCKFHJxoY9TPPQq3ANeoHUEG4OnqQiQjQimDUP3j2RWTnjM6Izc1HNUI8wpfjZClTL4WvZbKykAgE7KYXAgPKxy%2FHcsxFp2R6pFBqT2T%2BZ5zPxf4mJYpUe%2BSyTPHQaDNjDehykcn2Pc%2FFaOZrTIdpJgRryGIIRPPC9aU1jse9fHSLa%2FaRBUv4xaauQ58jzWjpKP7%2F2Z4gujOBBGZq6b%2F%2BShbT%2FRrQF3DPct9NjR%2Bivg2wBmmU%2B%2B%2B8QurzNf4PtoUXGbGFmueSZmiclMW2HXiqAwVrT758Whrf70Am8iQf86QacuLSs2OSnY1q1PNPVZzqj6lCx5UYoGroHDY2KvCvxLFbj9zTKzkdNxDLvisM3MbcUKa1YhFmXKBve90OVCtpSoR1%2FoQ8WZH%2FUw0KvNt0mlxF%2F2jpCM8TTDz5MpfKCw1Ik18dWLNNJPnw7QebA2Z2X9ArLSi6AutZbzZ4zVbGtmcoDemQPAyt6OIxJSbmG17ZwHdqUlwbWWCpOoIIjz3d7xq2SH0MFjhFhQNwhuKY%2FgobuCNw%2BkF5ICQqY6vEDDPGxyjmts8%2FNsir2kjfF5q6fbJVYoLHdpB442HUTuBPlM8PBJVLGunI2B8lZHnrHCj9QoOvGm7IOtOKr3aKM1j9LAbFO5L2qLZTDEuf%2FSBjqkAdiSYHC8G2nQVncMTQEOSjPPK2reyHCaWYk45LXQOh7wXLEWStIynAtsuFc%2Bv1WQ%2FGmvmFA8%2FmcVhmjOXOyHe1CIMoQz6H7%2BLm2wLopmSC2sycSR%2FoU7ZhnAPlNF5GWNfpWSpxW7XWi9YGKrOhnPAx%2Fy%2FfsCOjIk9Nf6rEqJn14h0aIIXGwIAY52Ekxn%2Fv1ML3x%2ByYik5a5ENac97QC7dYLu2rnQ&X-Amz-Signature=2396b02f4e990ca146e91fe7ad066c3992413a071dc86c9e062962e188054ead&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

optimizer trees 的参数有这么几个，来看一下。首先是 optimizer trees，这是一个总开关，默认情况是关闭的。第二是 optimized trees features，这是 optimizer trees 的细粒度开关，可以分别针对 Grady search range， optimizer dynamic range 等等分别设置是否要开启？ optimizer trees limit 用来控制 optimizer trees 的展示结果，显示多少条 optimizer trees makes memory size，又来指定 optimizer trees 允许使用的最大内存。 optimized trace offset 用来设置第一个要展示的 optimized trace 的偏移量。目前大家可能不理解这是什么意思，一会就知道了。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/edff1d52-de75-4c47-afd0-efebf3107957/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MNRO6NA%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230209Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCBUqXZFHe3bI9aLlDXFUy3n9h65QOIbgFG2NYMDC3bMAIhAKbLsDn5W3nFgCDsqe2Cf%2Bf63NYx3X%2BtruZhuaxMPh51KogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz3yXCKFHJxoY9TPPQq3ANeoHUEG4OnqQiQjQimDUP3j2RWTnjM6Izc1HNUI8wpfjZClTL4WvZbKykAgE7KYXAgPKxy%2FHcsxFp2R6pFBqT2T%2BZ5zPxf4mJYpUe%2BSyTPHQaDNjDehykcn2Pc%2FFaOZrTIdpJgRryGIIRPPC9aU1jse9fHSLa%2FaRBUv4xaauQ58jzWjpKP7%2F2Z4gujOBBGZq6b%2F%2BShbT%2FRrQF3DPct9NjR%2Bivg2wBmmU%2B%2B%2B8QurzNf4PtoUXGbGFmueSZmiclMW2HXiqAwVrT758Whrf70Am8iQf86QacuLSs2OSnY1q1PNPVZzqj6lCx5UYoGroHDY2KvCvxLFbj9zTKzkdNxDLvisM3MbcUKa1YhFmXKBve90OVCtpSoR1%2FoQ8WZH%2FUw0KvNt0mlxF%2F2jpCM8TTDz5MpfKCw1Ik18dWLNNJPnw7QebA2Z2X9ArLSi6AutZbzZ4zVbGtmcoDemQPAyt6OIxJSbmG17ZwHdqUlwbWWCpOoIIjz3d7xq2SH0MFjhFhQNwhuKY%2FgobuCNw%2BkF5ICQqY6vEDDPGxyjmts8%2FNsir2kjfF5q6fbJVYoLHdpB442HUTuBPlM8PBJVLGunI2B8lZHnrHCj9QoOvGm7IOtOKr3aKM1j9LAbFO5L2qLZTDEuf%2FSBjqkAdiSYHC8G2nQVncMTQEOSjPPK2reyHCaWYk45LXQOh7wXLEWStIynAtsuFc%2Bv1WQ%2FGmvmFA8%2FmcVhmjOXOyHe1CIMoQz6H7%2BLm2wLopmSC2sycSR%2FoU7ZhnAPlNF5GWNfpWSpxW7XWi9YGKrOhnPAx%2Fy%2FfsCOjIk9Nf6rEqJn14h0aIIXGwIAY52Ekxn%2Fv1ML3x%2ByYik5a5ENac97QC7dYLu2rnQ&X-Amz-Signature=72ddded25fcac0dffd04800ed90f333f01c7890ac4ba3e5e0c6b43a04e089970&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

最后， end markers in JSON 这个参数的作用是 optimizer trees 的结果是一个JSON。如果开启了 end markers in JSON，就会在一段 JSON 结束之后加上这样的一个注释，表示这一段已经结束了。方便阅读的。OK。回来想要设置这些参数的值的时候，只需要使用 set 语句就 OK 了，你也可以使用 set global 去全局设置。但是即使全局设置，也不能跨 session 跟踪，你没有办法监控其他 session 发送的 SQL 语句。再一个，这些参数里面比较有意思的是 optimizer trace limit 和 optimizer trace upset 这两个参数，它们经常配合使用。比方，你可以这样设置这两个参数配合使用的时候，有点类似于 MySQL 里面的 limit 语句。


默认情况下， optimizer trace offset 是-1， optimizer trace limit 是一。其中 optimizer trace offset 等于-1，表示记录最近的一条 SQL 语句。 optimizer trees limit 等于inner，表示每次只展示一条数据。说的更通俗一点的话，默认情况下只监控上一条 SQL 语句，对吧？而如果你把它设置成 optimizer trace offset 等于-2， optimizer trace limit 等于 1 的话，那么就表示每次只记录倒数第二条 4 个语句。如果把它改成set， optimizer trees 等于far， optimized trees 的 limit 等于 2 的话，这表示总是记录最近两条 SQL 语句。现在大家应该知道 optimized trace offset 是什么意思了。


好，下面我们来玩一下 optimized trace 吧。首先开启 optimize the trees copy 粘贴执行。接着设置一下 optimize trace offset 以及 optimized trace limit。这里 offset 设成- 30 limit 设置成30，表示总是记录最近 30 条词刻语句。 copy 粘贴执行，就可以发送你想要分析的 SQL 语句了。


copy 粘贴，执行一下，之后，可以使用 selection from information schema optimizer trees limit 30，可以查看 optimized trace 的结果。运行。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/8765c1f3-07e8-47eb-a510-590ced9c3ddc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MNRO6NA%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230209Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCBUqXZFHe3bI9aLlDXFUy3n9h65QOIbgFG2NYMDC3bMAIhAKbLsDn5W3nFgCDsqe2Cf%2Bf63NYx3X%2BtruZhuaxMPh51KogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz3yXCKFHJxoY9TPPQq3ANeoHUEG4OnqQiQjQimDUP3j2RWTnjM6Izc1HNUI8wpfjZClTL4WvZbKykAgE7KYXAgPKxy%2FHcsxFp2R6pFBqT2T%2BZ5zPxf4mJYpUe%2BSyTPHQaDNjDehykcn2Pc%2FFaOZrTIdpJgRryGIIRPPC9aU1jse9fHSLa%2FaRBUv4xaauQ58jzWjpKP7%2F2Z4gujOBBGZq6b%2F%2BShbT%2FRrQF3DPct9NjR%2Bivg2wBmmU%2B%2B%2B8QurzNf4PtoUXGbGFmueSZmiclMW2HXiqAwVrT758Whrf70Am8iQf86QacuLSs2OSnY1q1PNPVZzqj6lCx5UYoGroHDY2KvCvxLFbj9zTKzkdNxDLvisM3MbcUKa1YhFmXKBve90OVCtpSoR1%2FoQ8WZH%2FUw0KvNt0mlxF%2F2jpCM8TTDz5MpfKCw1Ik18dWLNNJPnw7QebA2Z2X9ArLSi6AutZbzZ4zVbGtmcoDemQPAyt6OIxJSbmG17ZwHdqUlwbWWCpOoIIjz3d7xq2SH0MFjhFhQNwhuKY%2FgobuCNw%2BkF5ICQqY6vEDDPGxyjmts8%2FNsir2kjfF5q6fbJVYoLHdpB442HUTuBPlM8PBJVLGunI2B8lZHnrHCj9QoOvGm7IOtOKr3aKM1j9LAbFO5L2qLZTDEuf%2FSBjqkAdiSYHC8G2nQVncMTQEOSjPPK2reyHCaWYk45LXQOh7wXLEWStIynAtsuFc%2Bv1WQ%2FGmvmFA8%2FmcVhmjOXOyHe1CIMoQz6H7%2BLm2wLopmSC2sycSR%2FoU7ZhnAPlNF5GWNfpWSpxW7XWi9YGKrOhnPAx%2Fy%2FfsCOjIk9Nf6rEqJn14h0aIIXGwIAY52Ekxn%2Fv1ML3x%2ByYik5a5ENac97QC7dYLu2rnQ&X-Amz-Signature=b6b4a8dd051397f8b17c00aa8ac8384545a42738a2037184edb81380f8cc2070&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

这一列会展示出执行的 circle 是什么。可以看到，在这里， trace 则是 optimize trace 的结果。它是一段很长的JSON。我们可以把结果 copy 出来，创建一个文件 new file，比如 OPT measure chase，点JSON，然后粘贴过来。


从结果可以看到，整个结果包括了三大部分准备阶段、优化阶段以及执行阶段。由于内容非常的长，因此课上就不逐个展开了。同学们可以对照弹幕的手机看一下。每一段表示什么含义。我都写了，注释还是比较清晰的。这里面最重要的步骤有


两个，一是 **rose estimation，**这个步骤分析了操作某一张表的**各种执行方案的成**本。比如使用表扫描成本是这样子的需要扫描这么多行，成本是这么大，使用索引需要扫描这么多行，成本是这么大等等等。这个步骤对于分析单表查询非常的有用。

```sql


 {
  "steps": [
    {
      "join_preparation": {
        "select#": 1,
        "steps": [
          {
            "expanded_query": "/* select#1 */ select `salaries`.`emp_no` AS `emp_no`,`salaries`.`salary` AS `salary`,`salaries`.`from_date` AS `from_date`,`salaries`.`to_date` AS `to_date` from `salaries` where ((`salaries`.`from_date` = '1986-06-26') and (`salaries`.`to_date` = '1987-06-26'))"
          }
        ] /* steps */
      } /* join_preparation */
    },
    {
      "join_optimization": {
        "select#": 1,
        "steps": [
          {
            "condition_processing": {
              "condition": "WHERE",
              "original_condition": "((`salaries`.`from_date` = '1986-06-26') and (`salaries`.`to_date` = '1987-06-26'))",
              "steps": [
                {
                  "transformation": "equality_propagation",
                  "resulting_condition": "(multiple equal('1986-06-26', `salaries`.`from_date`) and multiple equal('1987-06-26', `salaries`.`to_date`))"
                },
                {
                  "transformation": "constant_propagation",
                  "resulting_condition": "(multiple equal('1986-06-26', `salaries`.`from_date`) and multiple equal('1987-06-26', `salaries`.`to_date`))"
                },
                {
                  "transformation": "trivial_condition_removal",
                  "resulting_condition": "(multiple equal(DATE'1986-06-26', `salaries`.`from_date`) and multiple equal(DATE'1987-06-26', `salaries`.`to_date`))"
                }
              ] /* steps */
            } /* condition_processing */
          },
          {
            "substitute_generated_columns": {
            } /* substitute_generated_columns */
          },
          {
            "table_dependencies": [
              {
                "table": "`salaries`",
                "row_may_be_null": false,
                "map_bit": 0,
                "depends_on_map_bits": [
                ] /* depends_on_map_bits */
              }
            ] /* table_dependencies */
          },
          {
            "ref_optimizer_key_uses": [
            ] /* ref_optimizer_key_uses */
          },
          {
            "rows_estimation": [
              {
                "table": "`salaries`",
                "table_scan": {
                  "rows": 2838426,
                  "cost": 1530
                } /* table_scan */
              }
            ] /* rows_estimation */
          },
          {
            "considered_execution_plans": [
              {
                "plan_prefix": [
                ] /* plan_prefix */,
                "table": "`salaries`",
                "best_access_path": {
                  "considered_access_paths": [
                    {
                      "rows_to_scan": 2838426,
                      "access_type": "scan",
                      "resulting_rows": 2.83843e+06,
                      "cost": 285373,
                      "chosen": true
                    }
                  ] /* considered_access_paths */
                } /* best_access_path */,
                "condition_filtering_pct": 100,
                "rows_for_plan": 2.83843e+06,
                "cost_for_plan": 285373,
                "chosen": true
              }
            ] /* considered_execution_plans */
          },
          {
            "attaching_conditions_to_tables": {
              "original_condition": "((`salaries`.`to_date` = DATE'1987-06-26') and (`salaries`.`from_date` = DATE'1986-06-26'))",
              "attached_conditions_computation": [
              ] /* attached_conditions_computation */,
              "attached_conditions_summary": [
                {
                  "table": "`salaries`",
                  "attached": "((`salaries`.`to_date` = DATE'1987-06-26') and (`salaries`.`from_date` = DATE'1986-06-26'))"
                }
              ] /* attached_conditions_summary */
            } /* attaching_conditions_to_tables */
          },
          {
            "finalizing_table_conditions": [
              {
                "table": "`salaries`",
                "original_table_condition": "((`salaries`.`to_date` = DATE'1987-06-26') and (`salaries`.`from_date` = DATE'1986-06-26'))",
                "final_table_condition   ": "((`salaries`.`to_date` = DATE'1987-06-26') and (`salaries`.`from_date` = DATE'1986-06-26'))"
              }
            ] /* finalizing_table_conditions */
          },
          {
            "refine_plan": [
              {
                "table": "`salaries`"
              }
            ] /* refine_plan */
          }
        ] /* steps */
      } /* join_optimization */
    },
    {
      "join_execution": {
        "select#": 1,
        "steps": [
        ] /* steps */
      } /* join_execution */
    }
  ] /* steps */
}
```


**第二是 consider 的 execution plans**。这个步骤会显明各种访问方式的开销。比方使用 ref 这种访问方式，开销是这样子的使用 range 访问方式使用的水印是什么， MySQL 没有选择它，所以没有展示开销。**这个步骤对于分析多表查询比较有用**。其他的步骤同学们可以通读一下。
好。经过实验之后，不难发现 optimizer trees 的强大，它可以剖析 sql 的直径细节，并且会告诉我们各种开销。今后同学们在做 sql 调优的时候，如果想要深入到优化器内部，就可以使用 optimizer trace 了。这节课就到这里，谢谢大家。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/9374dd31-5620-481e-8ce6-f15ffd72acf2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MNRO6NA%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230209Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCBUqXZFHe3bI9aLlDXFUy3n9h65QOIbgFG2NYMDC3bMAIhAKbLsDn5W3nFgCDsqe2Cf%2Bf63NYx3X%2BtruZhuaxMPh51KogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz3yXCKFHJxoY9TPPQq3ANeoHUEG4OnqQiQjQimDUP3j2RWTnjM6Izc1HNUI8wpfjZClTL4WvZbKykAgE7KYXAgPKxy%2FHcsxFp2R6pFBqT2T%2BZ5zPxf4mJYpUe%2BSyTPHQaDNjDehykcn2Pc%2FFaOZrTIdpJgRryGIIRPPC9aU1jse9fHSLa%2FaRBUv4xaauQ58jzWjpKP7%2F2Z4gujOBBGZq6b%2F%2BShbT%2FRrQF3DPct9NjR%2Bivg2wBmmU%2B%2B%2B8QurzNf4PtoUXGbGFmueSZmiclMW2HXiqAwVrT758Whrf70Am8iQf86QacuLSs2OSnY1q1PNPVZzqj6lCx5UYoGroHDY2KvCvxLFbj9zTKzkdNxDLvisM3MbcUKa1YhFmXKBve90OVCtpSoR1%2FoQ8WZH%2FUw0KvNt0mlxF%2F2jpCM8TTDz5MpfKCw1Ik18dWLNNJPnw7QebA2Z2X9ArLSi6AutZbzZ4zVbGtmcoDemQPAyt6OIxJSbmG17ZwHdqUlwbWWCpOoIIjz3d7xq2SH0MFjhFhQNwhuKY%2FgobuCNw%2BkF5ICQqY6vEDDPGxyjmts8%2FNsir2kjfF5q6fbJVYoLHdpB442HUTuBPlM8PBJVLGunI2B8lZHnrHCj9QoOvGm7IOtOKr3aKM1j9LAbFO5L2qLZTDEuf%2FSBjqkAdiSYHC8G2nQVncMTQEOSjPPK2reyHCaWYk45LXQOh7wXLEWStIynAtsuFc%2Bv1WQ%2FGmvmFA8%2FmcVhmjOXOyHe1CIMoQz6H7%2BLm2wLopmSC2sycSR%2FoU7ZhnAPlNF5GWNfpWSpxW7XWi9YGKrOhnPAx%2Fy%2FfsCOjIk9Nf6rEqJn14h0aIIXGwIAY52Ekxn%2Fv1ML3x%2ByYik5a5ENac97QC7dYLu2rnQ&X-Amz-Signature=94a69183f435da9853a2319cf0523d11a23aad54189561ebc90983854b6d057c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e1a88cc5-0982-491b-9a63-d06f740fd299/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MNRO6NA%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230209Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCBUqXZFHe3bI9aLlDXFUy3n9h65QOIbgFG2NYMDC3bMAIhAKbLsDn5W3nFgCDsqe2Cf%2Bf63NYx3X%2BtruZhuaxMPh51KogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz3yXCKFHJxoY9TPPQq3ANeoHUEG4OnqQiQjQimDUP3j2RWTnjM6Izc1HNUI8wpfjZClTL4WvZbKykAgE7KYXAgPKxy%2FHcsxFp2R6pFBqT2T%2BZ5zPxf4mJYpUe%2BSyTPHQaDNjDehykcn2Pc%2FFaOZrTIdpJgRryGIIRPPC9aU1jse9fHSLa%2FaRBUv4xaauQ58jzWjpKP7%2F2Z4gujOBBGZq6b%2F%2BShbT%2FRrQF3DPct9NjR%2Bivg2wBmmU%2B%2B%2B8QurzNf4PtoUXGbGFmueSZmiclMW2HXiqAwVrT758Whrf70Am8iQf86QacuLSs2OSnY1q1PNPVZzqj6lCx5UYoGroHDY2KvCvxLFbj9zTKzkdNxDLvisM3MbcUKa1YhFmXKBve90OVCtpSoR1%2FoQ8WZH%2FUw0KvNt0mlxF%2F2jpCM8TTDz5MpfKCw1Ik18dWLNNJPnw7QebA2Z2X9ArLSi6AutZbzZ4zVbGtmcoDemQPAyt6OIxJSbmG17ZwHdqUlwbWWCpOoIIjz3d7xq2SH0MFjhFhQNwhuKY%2FgobuCNw%2BkF5ICQqY6vEDDPGxyjmts8%2FNsir2kjfF5q6fbJVYoLHdpB442HUTuBPlM8PBJVLGunI2B8lZHnrHCj9QoOvGm7IOtOKr3aKM1j9LAbFO5L2qLZTDEuf%2FSBjqkAdiSYHC8G2nQVncMTQEOSjPPK2reyHCaWYk45LXQOh7wXLEWStIynAtsuFc%2Bv1WQ%2FGmvmFA8%2FmcVhmjOXOyHe1CIMoQz6H7%2BLm2wLopmSC2sycSR%2FoU7ZhnAPlNF5GWNfpWSpxW7XWi9YGKrOhnPAx%2Fy%2FfsCOjIk9Nf6rEqJn14h0aIIXGwIAY52Ekxn%2Fv1ML3x%2ByYik5a5ENac97QC7dYLu2rnQ&X-Amz-Signature=c5a77145c7fbb1752c440113d0ce4833c984a0ae044d4c49fda18d6038c1e342&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/5ec78147-cc34-44cd-9978-77f82d71c7a4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4664MNRO6NA%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230209Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCBUqXZFHe3bI9aLlDXFUy3n9h65QOIbgFG2NYMDC3bMAIhAKbLsDn5W3nFgCDsqe2Cf%2Bf63NYx3X%2BtruZhuaxMPh51KogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igz3yXCKFHJxoY9TPPQq3ANeoHUEG4OnqQiQjQimDUP3j2RWTnjM6Izc1HNUI8wpfjZClTL4WvZbKykAgE7KYXAgPKxy%2FHcsxFp2R6pFBqT2T%2BZ5zPxf4mJYpUe%2BSyTPHQaDNjDehykcn2Pc%2FFaOZrTIdpJgRryGIIRPPC9aU1jse9fHSLa%2FaRBUv4xaauQ58jzWjpKP7%2F2Z4gujOBBGZq6b%2F%2BShbT%2FRrQF3DPct9NjR%2Bivg2wBmmU%2B%2B%2B8QurzNf4PtoUXGbGFmueSZmiclMW2HXiqAwVrT758Whrf70Am8iQf86QacuLSs2OSnY1q1PNPVZzqj6lCx5UYoGroHDY2KvCvxLFbj9zTKzkdNxDLvisM3MbcUKa1YhFmXKBve90OVCtpSoR1%2FoQ8WZH%2FUw0KvNt0mlxF%2F2jpCM8TTDz5MpfKCw1Ik18dWLNNJPnw7QebA2Z2X9ArLSi6AutZbzZ4zVbGtmcoDemQPAyt6OIxJSbmG17ZwHdqUlwbWWCpOoIIjz3d7xq2SH0MFjhFhQNwhuKY%2FgobuCNw%2BkF5ICQqY6vEDDPGxyjmts8%2FNsir2kjfF5q6fbJVYoLHdpB442HUTuBPlM8PBJVLGunI2B8lZHnrHCj9QoOvGm7IOtOKr3aKM1j9LAbFO5L2qLZTDEuf%2FSBjqkAdiSYHC8G2nQVncMTQEOSjPPK2reyHCaWYk45LXQOh7wXLEWStIynAtsuFc%2Bv1WQ%2FGmvmFA8%2FmcVhmjOXOyHe1CIMoQz6H7%2BLm2wLopmSC2sycSR%2FoU7ZhnAPlNF5GWNfpWSpxW7XWi9YGKrOhnPAx%2Fy%2FfsCOjIk9Nf6rEqJn14h0aIIXGwIAY52Ekxn%2Fv1ML3x%2ByYik5a5ENac97QC7dYLu2rnQ&X-Amz-Signature=c4b5a3ebb5b9eb50b96ae2794a9b241d4c6b63f5586b38792bd9f5b038bcfb04&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)









---
title: 2-6 线程池调优实战
---

# 2-6 线程池调优实战

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/a1aeb9c3-132e-4d68-bc57-c704918f50bb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655PXHHT5%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCJS7N%2BUnfwpmp6u%2BSFBRdX3NcFEmNP1cJ4vmvFZmXsmQIhAKiojXCDexJ5VpQFH8V015V4UsrBJK3fMdDLR6TwURO0KogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzfEzsfpZ1A6C%2FDfGkq3AP%2BkbuB5Lv7limPWXdkvSEZo5p42ArGFuMeCL7ngyTPK6XSzgf01EXFuvoIDyfCqbXgD0wGNpD8w7KJs1oGyNvjK0A%2FtSrEzmJFYK2wIJEq1A6SatJJhfZEjfbd3ybkdtDL2wk1Uo0dfuAxlgws6ylr1erGCQzL%2BYkrvTsKT8%2FLgr4e6Fr7F%2F%2B%2Bg%2FuNk9ERmsUKxXUNwq6iQC698G3qaNTl3VS81C6M%2Fft6UkpCrdWst8jVl2pR%2Bv4wUGu5XzbrRy8arUFT7x7hCY%2FfAotappv09agOrG0y27QMHHLQSKeOMkio218AO3hxqTRcWF5qIwXokqoChLwAvBMeRc2fy3xGOW4k%2Fk%2FunD%2FAgtpar0z8O3J1S%2B3WU%2FTrdAkD1OQyqcv51CssuyaJcUefeyOOLe05DGtoa5QcnmXWs6wottJgiG4KmB6v86jv2RxXj0LDWKZvwRjKSP2Qb410GFKV52TeT5Vyvf5E%2FN4mJ22iRvfhgcW60h31GL4bymbg%2FxFz9sWEytbcDYwYhAuGOGBAef3mhh%2BUv6JCAzzsx82AeSF09ouqJSbCju3sH5e4qSyakC164ocJXUp8MyRSg92S569%2FGSChiqlD4TJeVWQC8Uz0lvUswLPhheV5Xu3wbDCCu%2F%2FSBjqkAZj9v92N3LgVwpaoGf3Jr2jIhX10YuRbwbu%2BC0Tg1eB5tCnpBgzjdI0HSaKrFSx0sn2DShO5dIm7vbB6YdQeE4zyMIIamHdCR7%2B2eOLfEltvw6uhJJcFgXXbx%2B0IQIOn8i0A6wFnIj1r57ozSLIU9jAKwkNkoE3zm%2FqAbc3crXmKY%2BVfmgF%2B9RRxFEIi0LGcTUi5P15rBDPUriUnpC%2BwKJwK3blq&X-Amz-Signature=e79c668b32316ac34c52b1fc20bc316b11b88ef3b442e24d03c434b96c1cb2e1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e451b58c-e8b6-4dca-91f3-c986d7a51298/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655PXHHT5%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCJS7N%2BUnfwpmp6u%2BSFBRdX3NcFEmNP1cJ4vmvFZmXsmQIhAKiojXCDexJ5VpQFH8V015V4UsrBJK3fMdDLR6TwURO0KogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzfEzsfpZ1A6C%2FDfGkq3AP%2BkbuB5Lv7limPWXdkvSEZo5p42ArGFuMeCL7ngyTPK6XSzgf01EXFuvoIDyfCqbXgD0wGNpD8w7KJs1oGyNvjK0A%2FtSrEzmJFYK2wIJEq1A6SatJJhfZEjfbd3ybkdtDL2wk1Uo0dfuAxlgws6ylr1erGCQzL%2BYkrvTsKT8%2FLgr4e6Fr7F%2F%2B%2Bg%2FuNk9ERmsUKxXUNwq6iQC698G3qaNTl3VS81C6M%2Fft6UkpCrdWst8jVl2pR%2Bv4wUGu5XzbrRy8arUFT7x7hCY%2FfAotappv09agOrG0y27QMHHLQSKeOMkio218AO3hxqTRcWF5qIwXokqoChLwAvBMeRc2fy3xGOW4k%2Fk%2FunD%2FAgtpar0z8O3J1S%2B3WU%2FTrdAkD1OQyqcv51CssuyaJcUefeyOOLe05DGtoa5QcnmXWs6wottJgiG4KmB6v86jv2RxXj0LDWKZvwRjKSP2Qb410GFKV52TeT5Vyvf5E%2FN4mJ22iRvfhgcW60h31GL4bymbg%2FxFz9sWEytbcDYwYhAuGOGBAef3mhh%2BUv6JCAzzsx82AeSF09ouqJSbCju3sH5e4qSyakC164ocJXUp8MyRSg92S569%2FGSChiqlD4TJeVWQC8Uz0lvUswLPhheV5Xu3wbDCCu%2F%2FSBjqkAZj9v92N3LgVwpaoGf3Jr2jIhX10YuRbwbu%2BC0Tg1eB5tCnpBgzjdI0HSaKrFSx0sn2DShO5dIm7vbB6YdQeE4zyMIIamHdCR7%2B2eOLfEltvw6uhJJcFgXXbx%2B0IQIOn8i0A6wFnIj1r57ozSLIU9jAKwkNkoE3zm%2FqAbc3crXmKY%2BVfmgF%2B9RRxFEIi0LGcTUi5P15rBDPUriUnpC%2BwKJwK3blq&X-Amz-Signature=344d03643ea0c82fd9b88e3b0c479a11bb213d10a86d7b91759e667c7a25acc6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/42e08528-423f-4ae1-a2e0-365f2184a8d3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655PXHHT5%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCJS7N%2BUnfwpmp6u%2BSFBRdX3NcFEmNP1cJ4vmvFZmXsmQIhAKiojXCDexJ5VpQFH8V015V4UsrBJK3fMdDLR6TwURO0KogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzfEzsfpZ1A6C%2FDfGkq3AP%2BkbuB5Lv7limPWXdkvSEZo5p42ArGFuMeCL7ngyTPK6XSzgf01EXFuvoIDyfCqbXgD0wGNpD8w7KJs1oGyNvjK0A%2FtSrEzmJFYK2wIJEq1A6SatJJhfZEjfbd3ybkdtDL2wk1Uo0dfuAxlgws6ylr1erGCQzL%2BYkrvTsKT8%2FLgr4e6Fr7F%2F%2B%2Bg%2FuNk9ERmsUKxXUNwq6iQC698G3qaNTl3VS81C6M%2Fft6UkpCrdWst8jVl2pR%2Bv4wUGu5XzbrRy8arUFT7x7hCY%2FfAotappv09agOrG0y27QMHHLQSKeOMkio218AO3hxqTRcWF5qIwXokqoChLwAvBMeRc2fy3xGOW4k%2Fk%2FunD%2FAgtpar0z8O3J1S%2B3WU%2FTrdAkD1OQyqcv51CssuyaJcUefeyOOLe05DGtoa5QcnmXWs6wottJgiG4KmB6v86jv2RxXj0LDWKZvwRjKSP2Qb410GFKV52TeT5Vyvf5E%2FN4mJ22iRvfhgcW60h31GL4bymbg%2FxFz9sWEytbcDYwYhAuGOGBAef3mhh%2BUv6JCAzzsx82AeSF09ouqJSbCju3sH5e4qSyakC164ocJXUp8MyRSg92S569%2FGSChiqlD4TJeVWQC8Uz0lvUswLPhheV5Xu3wbDCCu%2F%2FSBjqkAZj9v92N3LgVwpaoGf3Jr2jIhX10YuRbwbu%2BC0Tg1eB5tCnpBgzjdI0HSaKrFSx0sn2DShO5dIm7vbB6YdQeE4zyMIIamHdCR7%2B2eOLfEltvw6uhJJcFgXXbx%2B0IQIOn8i0A6wFnIj1r57ozSLIU9jAKwkNkoE3zm%2FqAbc3crXmKY%2BVfmgF%2B9RRxFEIi0LGcTUi5P15rBDPUriUnpC%2BwKJwK3blq&X-Amz-Signature=c2982b2606ed670b170435291cd4d14d78d77581c13469f5f84b30aac7dce950&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e192f4cd-041a-4b78-83a6-5d71ed0de655/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655PXHHT5%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCJS7N%2BUnfwpmp6u%2BSFBRdX3NcFEmNP1cJ4vmvFZmXsmQIhAKiojXCDexJ5VpQFH8V015V4UsrBJK3fMdDLR6TwURO0KogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzfEzsfpZ1A6C%2FDfGkq3AP%2BkbuB5Lv7limPWXdkvSEZo5p42ArGFuMeCL7ngyTPK6XSzgf01EXFuvoIDyfCqbXgD0wGNpD8w7KJs1oGyNvjK0A%2FtSrEzmJFYK2wIJEq1A6SatJJhfZEjfbd3ybkdtDL2wk1Uo0dfuAxlgws6ylr1erGCQzL%2BYkrvTsKT8%2FLgr4e6Fr7F%2F%2B%2Bg%2FuNk9ERmsUKxXUNwq6iQC698G3qaNTl3VS81C6M%2Fft6UkpCrdWst8jVl2pR%2Bv4wUGu5XzbrRy8arUFT7x7hCY%2FfAotappv09agOrG0y27QMHHLQSKeOMkio218AO3hxqTRcWF5qIwXokqoChLwAvBMeRc2fy3xGOW4k%2Fk%2FunD%2FAgtpar0z8O3J1S%2B3WU%2FTrdAkD1OQyqcv51CssuyaJcUefeyOOLe05DGtoa5QcnmXWs6wottJgiG4KmB6v86jv2RxXj0LDWKZvwRjKSP2Qb410GFKV52TeT5Vyvf5E%2FN4mJ22iRvfhgcW60h31GL4bymbg%2FxFz9sWEytbcDYwYhAuGOGBAef3mhh%2BUv6JCAzzsx82AeSF09ouqJSbCju3sH5e4qSyakC164ocJXUp8MyRSg92S569%2FGSChiqlD4TJeVWQC8Uz0lvUswLPhheV5Xu3wbDCCu%2F%2FSBjqkAZj9v92N3LgVwpaoGf3Jr2jIhX10YuRbwbu%2BC0Tg1eB5tCnpBgzjdI0HSaKrFSx0sn2DShO5dIm7vbB6YdQeE4zyMIIamHdCR7%2B2eOLfEltvw6uhJJcFgXXbx%2B0IQIOn8i0A6wFnIj1r57ozSLIU9jAKwkNkoE3zm%2FqAbc3crXmKY%2BVfmgF%2B9RRxFEIi0LGcTUi5P15rBDPUriUnpC%2BwKJwK3blq&X-Amz-Signature=0e97257bd4f95488f7feda118e976189662a3e729a9f075754df0a7576f9d44e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

大家好，我是大木。前面在讲解 blocking queue 的时候，已经简单提及了线程池优化的注意点。这一节我们来系统探讨如何优化线程池，并来做一个限制式优化的实战。线程值调优主要包括两方面，第一是线程数的调优，第二是 blocking queue 的调优。先来探讨线程数的调优。实际项目中，调优线程数是比较麻烦的一件事儿，因为线程数量过多，就会导致线程之间竞争激烈，从而降低性能。而设置的太少又会导致无法充分利用计算机的资源，造成资源浪费。并且由于环境是不断变化的，因为线程池里面跑的任务在变化，而不同的任务所花费的时间以及计算资源往往都不一样，所以即使是同一个线程池，在不同时间的最优线程数也可能会有差异。好在一般来说，可以根据实际的操作因素，计算出一个相对合理的线程数。


目前业界一般把任务分为以下几种。第一种是 CPU 密集型任务。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/bbc4a65e-5d3b-42be-ac62-e9c9a43a5f0f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655PXHHT5%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCJS7N%2BUnfwpmp6u%2BSFBRdX3NcFEmNP1cJ4vmvFZmXsmQIhAKiojXCDexJ5VpQFH8V015V4UsrBJK3fMdDLR6TwURO0KogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzfEzsfpZ1A6C%2FDfGkq3AP%2BkbuB5Lv7limPWXdkvSEZo5p42ArGFuMeCL7ngyTPK6XSzgf01EXFuvoIDyfCqbXgD0wGNpD8w7KJs1oGyNvjK0A%2FtSrEzmJFYK2wIJEq1A6SatJJhfZEjfbd3ybkdtDL2wk1Uo0dfuAxlgws6ylr1erGCQzL%2BYkrvTsKT8%2FLgr4e6Fr7F%2F%2B%2Bg%2FuNk9ERmsUKxXUNwq6iQC698G3qaNTl3VS81C6M%2Fft6UkpCrdWst8jVl2pR%2Bv4wUGu5XzbrRy8arUFT7x7hCY%2FfAotappv09agOrG0y27QMHHLQSKeOMkio218AO3hxqTRcWF5qIwXokqoChLwAvBMeRc2fy3xGOW4k%2Fk%2FunD%2FAgtpar0z8O3J1S%2B3WU%2FTrdAkD1OQyqcv51CssuyaJcUefeyOOLe05DGtoa5QcnmXWs6wottJgiG4KmB6v86jv2RxXj0LDWKZvwRjKSP2Qb410GFKV52TeT5Vyvf5E%2FN4mJ22iRvfhgcW60h31GL4bymbg%2FxFz9sWEytbcDYwYhAuGOGBAef3mhh%2BUv6JCAzzsx82AeSF09ouqJSbCju3sH5e4qSyakC164ocJXUp8MyRSg92S569%2FGSChiqlD4TJeVWQC8Uz0lvUswLPhheV5Xu3wbDCCu%2F%2FSBjqkAZj9v92N3LgVwpaoGf3Jr2jIhX10YuRbwbu%2BC0Tg1eB5tCnpBgzjdI0HSaKrFSx0sn2DShO5dIm7vbB6YdQeE4zyMIIamHdCR7%2B2eOLfEltvw6uhJJcFgXXbx%2B0IQIOn8i0A6wFnIj1r57ozSLIU9jAKwkNkoE3zm%2FqAbc3crXmKY%2BVfmgF%2B9RRxFEIi0LGcTUi5P15rBDPUriUnpC%2BwKJwK3blq&X-Amz-Signature=d6c68ba6209a1e5416931942cd533fc1616df89e481730a851c67a5d185c27ee&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

所谓 CPU 密集型任务，任务大部分时间都在用 CPU 进行计算，像数字计算、排序等等都是由 CPU 完成的对吧？ CPU 密集型任务一般世界大型的复杂的计算型任务，比方挖矿就是一种非常复杂的计算型任务。只不过挖矿一般都不会用 CPU 去挖矿，更多的使用 GPU 去挖矿对吧？


第二种是 IO 密集型任务。 IO 密集型任务指的是大部分时间都在和 IO 交互，比方我们有一个 service 方法，它操作了 5 次数据库，操作数据库的过程就是i、 o 的过程。


第三是混合型任务。混合型任务比较好理解，c、p、 o 和i、 o 都需要占用一定的时间，实际项目中更多的是混合型任务。不过有一个经验，增删改闸类型的项目一般都更偏向于i、 o 密集型的任务。好。下面我们来针对这 3 种类型的任务，谈谈怎么样优化线程的数量。


首先， CPU 密集型的任务该怎么调优？一般来说，可以把线人数设置为 n 加1。 n 指的是 CPU 核心的数量，c、b、 u 核心数可以这样计算创建一个类叫 thread poor core test，

创建变方法。 Own runtime they are get the wrong time. They are available processors.

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/eec41c47-9705-4664-91b0-b60a07467793/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655PXHHT5%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCJS7N%2BUnfwpmp6u%2BSFBRdX3NcFEmNP1cJ4vmvFZmXsmQIhAKiojXCDexJ5VpQFH8V015V4UsrBJK3fMdDLR6TwURO0KogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzfEzsfpZ1A6C%2FDfGkq3AP%2BkbuB5Lv7limPWXdkvSEZo5p42ArGFuMeCL7ngyTPK6XSzgf01EXFuvoIDyfCqbXgD0wGNpD8w7KJs1oGyNvjK0A%2FtSrEzmJFYK2wIJEq1A6SatJJhfZEjfbd3ybkdtDL2wk1Uo0dfuAxlgws6ylr1erGCQzL%2BYkrvTsKT8%2FLgr4e6Fr7F%2F%2B%2Bg%2FuNk9ERmsUKxXUNwq6iQC698G3qaNTl3VS81C6M%2Fft6UkpCrdWst8jVl2pR%2Bv4wUGu5XzbrRy8arUFT7x7hCY%2FfAotappv09agOrG0y27QMHHLQSKeOMkio218AO3hxqTRcWF5qIwXokqoChLwAvBMeRc2fy3xGOW4k%2Fk%2FunD%2FAgtpar0z8O3J1S%2B3WU%2FTrdAkD1OQyqcv51CssuyaJcUefeyOOLe05DGtoa5QcnmXWs6wottJgiG4KmB6v86jv2RxXj0LDWKZvwRjKSP2Qb410GFKV52TeT5Vyvf5E%2FN4mJ22iRvfhgcW60h31GL4bymbg%2FxFz9sWEytbcDYwYhAuGOGBAef3mhh%2BUv6JCAzzsx82AeSF09ouqJSbCju3sH5e4qSyakC164ocJXUp8MyRSg92S569%2FGSChiqlD4TJeVWQC8Uz0lvUswLPhheV5Xu3wbDCCu%2F%2FSBjqkAZj9v92N3LgVwpaoGf3Jr2jIhX10YuRbwbu%2BC0Tg1eB5tCnpBgzjdI0HSaKrFSx0sn2DShO5dIm7vbB6YdQeE4zyMIIamHdCR7%2B2eOLfEltvw6uhJJcFgXXbx%2B0IQIOn8i0A6wFnIj1r57ozSLIU9jAKwkNkoE3zm%2FqAbc3crXmKY%2BVfmgF%2B9RRxFEIi0LGcTUi5P15rBDPUriUnpC%2BwKJwK3blq&X-Amz-Signature=4f3ca7cc790c8cf613f4be0e2d29bc32827dfb41ee3fb7f0388aa337f201bd3d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/99c70531-c73b-4078-af65-d697d66414b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655PXHHT5%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCJS7N%2BUnfwpmp6u%2BSFBRdX3NcFEmNP1cJ4vmvFZmXsmQIhAKiojXCDexJ5VpQFH8V015V4UsrBJK3fMdDLR6TwURO0KogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzfEzsfpZ1A6C%2FDfGkq3AP%2BkbuB5Lv7limPWXdkvSEZo5p42ArGFuMeCL7ngyTPK6XSzgf01EXFuvoIDyfCqbXgD0wGNpD8w7KJs1oGyNvjK0A%2FtSrEzmJFYK2wIJEq1A6SatJJhfZEjfbd3ybkdtDL2wk1Uo0dfuAxlgws6ylr1erGCQzL%2BYkrvTsKT8%2FLgr4e6Fr7F%2F%2B%2Bg%2FuNk9ERmsUKxXUNwq6iQC698G3qaNTl3VS81C6M%2Fft6UkpCrdWst8jVl2pR%2Bv4wUGu5XzbrRy8arUFT7x7hCY%2FfAotappv09agOrG0y27QMHHLQSKeOMkio218AO3hxqTRcWF5qIwXokqoChLwAvBMeRc2fy3xGOW4k%2Fk%2FunD%2FAgtpar0z8O3J1S%2B3WU%2FTrdAkD1OQyqcv51CssuyaJcUefeyOOLe05DGtoa5QcnmXWs6wottJgiG4KmB6v86jv2RxXj0LDWKZvwRjKSP2Qb410GFKV52TeT5Vyvf5E%2FN4mJ22iRvfhgcW60h31GL4bymbg%2FxFz9sWEytbcDYwYhAuGOGBAef3mhh%2BUv6JCAzzsx82AeSF09ouqJSbCju3sH5e4qSyakC164ocJXUp8MyRSg92S569%2FGSChiqlD4TJeVWQC8Uz0lvUswLPhheV5Xu3wbDCCu%2F%2FSBjqkAZj9v92N3LgVwpaoGf3Jr2jIhX10YuRbwbu%2BC0Tg1eB5tCnpBgzjdI0HSaKrFSx0sn2DShO5dIm7vbB6YdQeE4zyMIIamHdCR7%2B2eOLfEltvw6uhJJcFgXXbx%2B0IQIOn8i0A6wFnIj1r57ozSLIU9jAKwkNkoE3zm%2FqAbc3crXmKY%2BVfmgF%2B9RRxFEIi0LGcTUi5P15rBDPUriUnpC%2BwKJwK3blq&X-Amz-Signature=0e89aca0b5a82ef432e1faca81b6fd5a47af766a8bf2be57e4d3e95a7c2359af&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

这样就可以拿到 CPU 的核心数了。如果我们的线程池运行的是一个 CPU 密集型的任务，就可以把线程的数量设置为9。大家想为什么要把它设置为 CPU 的核心数加1。理论上把它设置为 CPU 核心数性能是最优的，因为没有任何线程切换的开销，同时又可以让每一个 CPU 的核心都忙起来，没有任何的资源浪费。这样想当然没什么问题。但问题是，如果某一个线程突然出现暂停或者中断，c、b、 o 就会有一个核心处于空闲状态了。所以我们一般会设置为 n 加1。这样多出来的一个线程就可以用来充分利用 CPU 的空闲时间。这就像是踢足球弄了一个候补队员对吧。


对于 IO 密集型的任务，由于大部分时间是在处理 IO 的，而线程处理 IO 的过程是不需要占用 CPU 的，所以处理 IO 的这段时间，这个线程的 CPU 资源就可以交给其他线程去使用。因此 IO 密集器的任务可以多配置一些线程。业界比较认可的经验值是2N，对于我的机器就可以配置成 16 对吧。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/52854dfa-28f7-462e-a846-3573c5750980/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655PXHHT5%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCJS7N%2BUnfwpmp6u%2BSFBRdX3NcFEmNP1cJ4vmvFZmXsmQIhAKiojXCDexJ5VpQFH8V015V4UsrBJK3fMdDLR6TwURO0KogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzfEzsfpZ1A6C%2FDfGkq3AP%2BkbuB5Lv7limPWXdkvSEZo5p42ArGFuMeCL7ngyTPK6XSzgf01EXFuvoIDyfCqbXgD0wGNpD8w7KJs1oGyNvjK0A%2FtSrEzmJFYK2wIJEq1A6SatJJhfZEjfbd3ybkdtDL2wk1Uo0dfuAxlgws6ylr1erGCQzL%2BYkrvTsKT8%2FLgr4e6Fr7F%2F%2B%2Bg%2FuNk9ERmsUKxXUNwq6iQC698G3qaNTl3VS81C6M%2Fft6UkpCrdWst8jVl2pR%2Bv4wUGu5XzbrRy8arUFT7x7hCY%2FfAotappv09agOrG0y27QMHHLQSKeOMkio218AO3hxqTRcWF5qIwXokqoChLwAvBMeRc2fy3xGOW4k%2Fk%2FunD%2FAgtpar0z8O3J1S%2B3WU%2FTrdAkD1OQyqcv51CssuyaJcUefeyOOLe05DGtoa5QcnmXWs6wottJgiG4KmB6v86jv2RxXj0LDWKZvwRjKSP2Qb410GFKV52TeT5Vyvf5E%2FN4mJ22iRvfhgcW60h31GL4bymbg%2FxFz9sWEytbcDYwYhAuGOGBAef3mhh%2BUv6JCAzzsx82AeSF09ouqJSbCju3sH5e4qSyakC164ocJXUp8MyRSg92S569%2FGSChiqlD4TJeVWQC8Uz0lvUswLPhheV5Xu3wbDCCu%2F%2FSBjqkAZj9v92N3LgVwpaoGf3Jr2jIhX10YuRbwbu%2BC0Tg1eB5tCnpBgzjdI0HSaKrFSx0sn2DShO5dIm7vbB6YdQeE4zyMIIamHdCR7%2B2eOLfEltvw6uhJJcFgXXbx%2B0IQIOn8i0A6wFnIj1r57ozSLIU9jAKwkNkoE3zm%2FqAbc3crXmKY%2BVfmgF%2B9RRxFEIi0LGcTUi5P15rBDPUriUnpC%2BwKJwK3blq&X-Amz-Signature=05cb94c2be70b7dae2cca40564412543f15f216c5031e7624e91004e96921a71&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

可以发现，对于c、p、 u 密集型的任务以及i、 o 密集型的任务，线程池数量的调优还是比较简单的。但实际项目中，纯粹的c、 b o 秘籍或者i、 o 秘籍型的任务其实很难遇到，更多的是混合性的任务。这个时候又该如何设置线程的数量呢？这里普及一个估算线程的计算公式，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/fb67aca4-5307-4908-a6da-a9b429dabe7f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655PXHHT5%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCJS7N%2BUnfwpmp6u%2BSFBRdX3NcFEmNP1cJ4vmvFZmXsmQIhAKiojXCDexJ5VpQFH8V015V4UsrBJK3fMdDLR6TwURO0KogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzfEzsfpZ1A6C%2FDfGkq3AP%2BkbuB5Lv7limPWXdkvSEZo5p42ArGFuMeCL7ngyTPK6XSzgf01EXFuvoIDyfCqbXgD0wGNpD8w7KJs1oGyNvjK0A%2FtSrEzmJFYK2wIJEq1A6SatJJhfZEjfbd3ybkdtDL2wk1Uo0dfuAxlgws6ylr1erGCQzL%2BYkrvTsKT8%2FLgr4e6Fr7F%2F%2B%2Bg%2FuNk9ERmsUKxXUNwq6iQC698G3qaNTl3VS81C6M%2Fft6UkpCrdWst8jVl2pR%2Bv4wUGu5XzbrRy8arUFT7x7hCY%2FfAotappv09agOrG0y27QMHHLQSKeOMkio218AO3hxqTRcWF5qIwXokqoChLwAvBMeRc2fy3xGOW4k%2Fk%2FunD%2FAgtpar0z8O3J1S%2B3WU%2FTrdAkD1OQyqcv51CssuyaJcUefeyOOLe05DGtoa5QcnmXWs6wottJgiG4KmB6v86jv2RxXj0LDWKZvwRjKSP2Qb410GFKV52TeT5Vyvf5E%2FN4mJ22iRvfhgcW60h31GL4bymbg%2FxFz9sWEytbcDYwYhAuGOGBAef3mhh%2BUv6JCAzzsx82AeSF09ouqJSbCju3sH5e4qSyakC164ocJXUp8MyRSg92S569%2FGSChiqlD4TJeVWQC8Uz0lvUswLPhheV5Xu3wbDCCu%2F%2FSBjqkAZj9v92N3LgVwpaoGf3Jr2jIhX10YuRbwbu%2BC0Tg1eB5tCnpBgzjdI0HSaKrFSx0sn2DShO5dIm7vbB6YdQeE4zyMIIamHdCR7%2B2eOLfEltvw6uhJJcFgXXbx%2B0IQIOn8i0A6wFnIj1r57ozSLIU9jAKwkNkoE3zm%2FqAbc3crXmKY%2BVfmgF%2B9RRxFEIi0LGcTUi5P15rBDPUriUnpC%2BwKJwK3blq&X-Amz-Signature=7b7422e77bebc8ff80d26a64ba4c7be90c51b54aa95bdb8e4ad2e5de7751b523&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

叫 n 乘 u 乘以 1 加 w t 除以 s t。这里的指的是 c p o 的核心数， u 指的是你希望 c p o 的利用率达到多少。 w t 指的是线程等待的时间， s t 指的是线程运行的时间。在公式里面， n 最好获取，又是我们的期待，也非常好设置。比较难的是 w t 以及 s t 该怎么获取。


这里我们可以普及一个技巧，你可以运行一个项目，比如我们的负 d v 项目。打开终端，使用 j v 选 v m， j v m 是 j t k 自带的一个多合一的工具，在课程后面会详细讲。这里我们先使用一下enter，这样就可以启动 j v QVM 了。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/ea50f67d-6a38-4021-a010-1a0bdafe92bf/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655PXHHT5%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCJS7N%2BUnfwpmp6u%2BSFBRdX3NcFEmNP1cJ4vmvFZmXsmQIhAKiojXCDexJ5VpQFH8V015V4UsrBJK3fMdDLR6TwURO0KogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzfEzsfpZ1A6C%2FDfGkq3AP%2BkbuB5Lv7limPWXdkvSEZo5p42ArGFuMeCL7ngyTPK6XSzgf01EXFuvoIDyfCqbXgD0wGNpD8w7KJs1oGyNvjK0A%2FtSrEzmJFYK2wIJEq1A6SatJJhfZEjfbd3ybkdtDL2wk1Uo0dfuAxlgws6ylr1erGCQzL%2BYkrvTsKT8%2FLgr4e6Fr7F%2F%2B%2Bg%2FuNk9ERmsUKxXUNwq6iQC698G3qaNTl3VS81C6M%2Fft6UkpCrdWst8jVl2pR%2Bv4wUGu5XzbrRy8arUFT7x7hCY%2FfAotappv09agOrG0y27QMHHLQSKeOMkio218AO3hxqTRcWF5qIwXokqoChLwAvBMeRc2fy3xGOW4k%2Fk%2FunD%2FAgtpar0z8O3J1S%2B3WU%2FTrdAkD1OQyqcv51CssuyaJcUefeyOOLe05DGtoa5QcnmXWs6wottJgiG4KmB6v86jv2RxXj0LDWKZvwRjKSP2Qb410GFKV52TeT5Vyvf5E%2FN4mJ22iRvfhgcW60h31GL4bymbg%2FxFz9sWEytbcDYwYhAuGOGBAef3mhh%2BUv6JCAzzsx82AeSF09ouqJSbCju3sH5e4qSyakC164ocJXUp8MyRSg92S569%2FGSChiqlD4TJeVWQC8Uz0lvUswLPhheV5Xu3wbDCCu%2F%2FSBjqkAZj9v92N3LgVwpaoGf3Jr2jIhX10YuRbwbu%2BC0Tg1eB5tCnpBgzjdI0HSaKrFSx0sn2DShO5dIm7vbB6YdQeE4zyMIIamHdCR7%2B2eOLfEltvw6uhJJcFgXXbx%2B0IQIOn8i0A6wFnIj1r57ozSLIU9jAKwkNkoE3zm%2FqAbc3crXmKY%2BVfmgF%2B9RRxFEIi0LGcTUi5P15rBDPUriUnpC%2BwKJwK3blq&X-Amz-Signature=7dbeb4c0c3574e814846b768f89096cca2cf495c9e45462a504427a21024b160&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

点击我们刚刚启动的项目，点击profile，点击CPU。这样 j v m 就会进行一段时间的性能分析，需要一定的时间，我们稍等一下好分析好了。这里的自用时间指的是线程的运行时间，也就是公式里面的 s t 总时间。减去自用时间，得到的就是 w t。计算一下就可以得到结果了。好，现在课上已经普及了 3 个公式，帮助我们去计算线程数的参考值。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/3b402d44-f0b8-433c-909f-3c19c65d6ad3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655PXHHT5%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCJS7N%2BUnfwpmp6u%2BSFBRdX3NcFEmNP1cJ4vmvFZmXsmQIhAKiojXCDexJ5VpQFH8V015V4UsrBJK3fMdDLR6TwURO0KogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzfEzsfpZ1A6C%2FDfGkq3AP%2BkbuB5Lv7limPWXdkvSEZo5p42ArGFuMeCL7ngyTPK6XSzgf01EXFuvoIDyfCqbXgD0wGNpD8w7KJs1oGyNvjK0A%2FtSrEzmJFYK2wIJEq1A6SatJJhfZEjfbd3ybkdtDL2wk1Uo0dfuAxlgws6ylr1erGCQzL%2BYkrvTsKT8%2FLgr4e6Fr7F%2F%2B%2Bg%2FuNk9ERmsUKxXUNwq6iQC698G3qaNTl3VS81C6M%2Fft6UkpCrdWst8jVl2pR%2Bv4wUGu5XzbrRy8arUFT7x7hCY%2FfAotappv09agOrG0y27QMHHLQSKeOMkio218AO3hxqTRcWF5qIwXokqoChLwAvBMeRc2fy3xGOW4k%2Fk%2FunD%2FAgtpar0z8O3J1S%2B3WU%2FTrdAkD1OQyqcv51CssuyaJcUefeyOOLe05DGtoa5QcnmXWs6wottJgiG4KmB6v86jv2RxXj0LDWKZvwRjKSP2Qb410GFKV52TeT5Vyvf5E%2FN4mJ22iRvfhgcW60h31GL4bymbg%2FxFz9sWEytbcDYwYhAuGOGBAef3mhh%2BUv6JCAzzsx82AeSF09ouqJSbCju3sH5e4qSyakC164ocJXUp8MyRSg92S569%2FGSChiqlD4TJeVWQC8Uz0lvUswLPhheV5Xu3wbDCCu%2F%2FSBjqkAZj9v92N3LgVwpaoGf3Jr2jIhX10YuRbwbu%2BC0Tg1eB5tCnpBgzjdI0HSaKrFSx0sn2DShO5dIm7vbB6YdQeE4zyMIIamHdCR7%2B2eOLfEltvw6uhJJcFgXXbx%2B0IQIOn8i0A6wFnIj1r57ozSLIU9jAKwkNkoE3zm%2FqAbc3crXmKY%2BVfmgF%2B9RRxFEIi0LGcTUi5P15rBDPUriUnpC%2BwKJwK3blq&X-Amz-Signature=252c66244587ba3cda152bf036205db1edd1b315975b2a86d58b0b9a66d1c793&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

blockingQueue 该怎么调优？

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/aa4d78c2-430b-4bc6-80e2-e547c9fa42d1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655PXHHT5%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCJS7N%2BUnfwpmp6u%2BSFBRdX3NcFEmNP1cJ4vmvFZmXsmQIhAKiojXCDexJ5VpQFH8V015V4UsrBJK3fMdDLR6TwURO0KogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzfEzsfpZ1A6C%2FDfGkq3AP%2BkbuB5Lv7limPWXdkvSEZo5p42ArGFuMeCL7ngyTPK6XSzgf01EXFuvoIDyfCqbXgD0wGNpD8w7KJs1oGyNvjK0A%2FtSrEzmJFYK2wIJEq1A6SatJJhfZEjfbd3ybkdtDL2wk1Uo0dfuAxlgws6ylr1erGCQzL%2BYkrvTsKT8%2FLgr4e6Fr7F%2F%2B%2Bg%2FuNk9ERmsUKxXUNwq6iQC698G3qaNTl3VS81C6M%2Fft6UkpCrdWst8jVl2pR%2Bv4wUGu5XzbrRy8arUFT7x7hCY%2FfAotappv09agOrG0y27QMHHLQSKeOMkio218AO3hxqTRcWF5qIwXokqoChLwAvBMeRc2fy3xGOW4k%2Fk%2FunD%2FAgtpar0z8O3J1S%2B3WU%2FTrdAkD1OQyqcv51CssuyaJcUefeyOOLe05DGtoa5QcnmXWs6wottJgiG4KmB6v86jv2RxXj0LDWKZvwRjKSP2Qb410GFKV52TeT5Vyvf5E%2FN4mJ22iRvfhgcW60h31GL4bymbg%2FxFz9sWEytbcDYwYhAuGOGBAef3mhh%2BUv6JCAzzsx82AeSF09ouqJSbCju3sH5e4qSyakC164ocJXUp8MyRSg92S569%2FGSChiqlD4TJeVWQC8Uz0lvUswLPhheV5Xu3wbDCCu%2F%2FSBjqkAZj9v92N3LgVwpaoGf3Jr2jIhX10YuRbwbu%2BC0Tg1eB5tCnpBgzjdI0HSaKrFSx0sn2DShO5dIm7vbB6YdQeE4zyMIIamHdCR7%2B2eOLfEltvw6uhJJcFgXXbx%2B0IQIOn8i0A6wFnIj1r57ozSLIU9jAKwkNkoE3zm%2FqAbc3crXmKY%2BVfmgF%2B9RRxFEIi0LGcTUi5P15rBDPUriUnpC%2BwKJwK3blq&X-Amz-Signature=6d2b77002b2612b17f82eeaedf28de1f7f24a721f64498418020838384881c40&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

你可以估算一下你的线程池每一个任务预计要花多少内存，你的线程池你希望它总共花费多少内存？这样算一下就可以得到 block q 的大小了。可以发现，实际项目中，对于混合型的任务限制值的调优还是比较麻烦的。你需要做一堆的计算才能知道线程的数量。在做一堆的估算才能得到 blocking q 该设置多大。因此，在这里，大木**提供一个懒人工具类，用来帮助你迅速优化线程池**。地址在这里。一起来看一下。

[file](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/d46b78f5-234b-4a1e-ac18-173b095fd742/PoolSizeCalculator.java?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655PXHHT5%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCJS7N%2BUnfwpmp6u%2BSFBRdX3NcFEmNP1cJ4vmvFZmXsmQIhAKiojXCDexJ5VpQFH8V015V4UsrBJK3fMdDLR6TwURO0KogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzfEzsfpZ1A6C%2FDfGkq3AP%2BkbuB5Lv7limPWXdkvSEZo5p42ArGFuMeCL7ngyTPK6XSzgf01EXFuvoIDyfCqbXgD0wGNpD8w7KJs1oGyNvjK0A%2FtSrEzmJFYK2wIJEq1A6SatJJhfZEjfbd3ybkdtDL2wk1Uo0dfuAxlgws6ylr1erGCQzL%2BYkrvTsKT8%2FLgr4e6Fr7F%2F%2B%2Bg%2FuNk9ERmsUKxXUNwq6iQC698G3qaNTl3VS81C6M%2Fft6UkpCrdWst8jVl2pR%2Bv4wUGu5XzbrRy8arUFT7x7hCY%2FfAotappv09agOrG0y27QMHHLQSKeOMkio218AO3hxqTRcWF5qIwXokqoChLwAvBMeRc2fy3xGOW4k%2Fk%2FunD%2FAgtpar0z8O3J1S%2B3WU%2FTrdAkD1OQyqcv51CssuyaJcUefeyOOLe05DGtoa5QcnmXWs6wottJgiG4KmB6v86jv2RxXj0LDWKZvwRjKSP2Qb410GFKV52TeT5Vyvf5E%2FN4mJ22iRvfhgcW60h31GL4bymbg%2FxFz9sWEytbcDYwYhAuGOGBAef3mhh%2BUv6JCAzzsx82AeSF09ouqJSbCju3sH5e4qSyakC164ocJXUp8MyRSg92S569%2FGSChiqlD4TJeVWQC8Uz0lvUswLPhheV5Xu3wbDCCu%2F%2FSBjqkAZj9v92N3LgVwpaoGf3Jr2jIhX10YuRbwbu%2BC0Tg1eB5tCnpBgzjdI0HSaKrFSx0sn2DShO5dIm7vbB6YdQeE4zyMIIamHdCR7%2B2eOLfEltvw6uhJJcFgXXbx%2B0IQIOn8i0A6wFnIj1r57ozSLIU9jAKwkNkoE3zm%2FqAbc3crXmKY%2BVfmgF%2B9RRxFEIi0LGcTUi5P15rBDPUriUnpC%2BwKJwK3blq&X-Amz-Signature=d3e8114d72de79c1752e13fa450e1647de5c860e480ad5c06e6d6acb0cb5cf43&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```java
package com.imooc.jvm.threadpool;

import java.math.BigDecimal;
import java.math.RoundingMode;
import java.util.Timer;
import java.util.TimerTask;
import java.util.concurrent.BlockingQueue;

/**

 * A class that calculates the optimal thread pool boundaries. It takes the desired target utilization and the desired
 * work queue memory consumption as input and retuns thread count and work queue capacity.
 * 
 * @author Niklas Schlimm
 * */
   public abstract class PoolSizeCalculator {

 /**

  * The sample queue size to calculate the size of a single {@link Runnable} element.
    */
     private final int SAMPLE_QUEUE_SIZE = 1000;

 /**

  * Accuracy of test run. It must finish within 20ms of the testTime otherwise we retry the test. This could be
  * configurable.
    */
     private final int EPSYLON = 20;

 /**

  * Control variable for the CPU time investigation.
    */
     private volatile boolean expired;

 /**

  * Time (millis) of the test run in the CPU time calculation.
    */
     private final long testtime = 3000;

 /**

  * Calculates the boundaries of a thread pool for a given {@link Runnable}.
  * 
  * @param targetUtilization
  * the desired utilization of the CPUs (0 <= targetUtilization <= 1)
  * @param targetQueueSizeBytes
  * the desired maximum work queue size of the thread pool (bytes)
      */
     protected void calculateBoundaries(BigDecimal targetUtilization, BigDecimal targetQueueSizeBytes) {
      calculateOptimalCapacity(targetQueueSizeBytes);
      Runnable task = creatTask();
      start(task);
      start(task); // warm up phase
      long cputime = getCurrentThreadCPUTime();
      start(task); // test intervall
      cputime = getCurrentThreadCPUTime() - cputime;
      long waittime = (testtime * 1000000) - cputime;
      calculateOptimalThreadCount(cputime, waittime, targetUtilization);
     }

 private void calculateOptimalCapacity(BigDecimal targetQueueSizeBytes) {
  long mem = calculateMemoryUsage();
  BigDecimal queueCapacity = targetQueueSizeBytes.divide(new BigDecimal(mem), RoundingMode.HALF_UP);
  System.out.println("Target queue memory usage (bytes): " + targetQueueSizeBytes);
  System.out.println("createTask() produced " + creatTask().getClass().getName() + " which took " + mem
    + " bytes in a queue");
  System.out.println("Formula: " + targetQueueSizeBytes + " / " + mem);
  System.out.println("* Recommended queue capacity (bytes): " + queueCapacity);
 }

 /**

  * Brian Goetz' optimal thread count formula, see 'Java Concurrency in Practice' (chapter 8.2)
  * 
  * @param cpu
  * cpu time consumed by considered task
  * @param wait
  * wait time of considered task
  * @param targetUtilization
  * target utilization of the system
      */
     private void calculateOptimalThreadCount(long cpu, long wait, BigDecimal targetUtilization) {
      BigDecimal waitTime = new BigDecimal(wait);
      BigDecimal computeTime = new BigDecimal(cpu);
      BigDecimal numberOfCPU = new BigDecimal(Runtime.getRuntime().availableProcessors());
      BigDecimal optimalthreadcount = numberOfCPU.multiply(targetUtilization).multiply(
    new BigDecimal(1).add(waitTime.divide(computeTime, RoundingMode.HALF_UP)));
      System.out.println("Number of CPU: " + numberOfCPU);
      System.out.println("Target utilization: " + targetUtilization);
      System.out.println("Elapsed time (nanos): " + (testtime * 1000000));
      System.out.println("Compute time (nanos): " + cpu);
      System.out.println("Wait time (nanos): " + wait);
      System.out.println("Formula: " + numberOfCPU + " * " + targetUtilization + " * (1 + " + waitTime + " / "
    + computeTime + ")");
      System.out.println("* Optimal thread count: " + optimalthreadcount);
       }

 /**

  * Runs the {@link Runnable} over a period defined in {@link #testtime}. Based on Heinz Kabbutz' ideas
  * (http://www.javaspecialists.eu/archive/Issue124.html).
  * 
  * @param task
  * the runnable under investigation
      */
     public void start(Runnable task) {
      long start = 0;
      int runs = 0;
      do {
       if (++runs > 5) {
    throw new IllegalStateException("Test not accurate");
       }
       expired = false;
       start = System.currentTimeMillis();
       Timer timer = new Timer();
       timer.schedule(new TimerTask() {
    public void run() {
     expired = true;
    }
       }, testtime);
       while (!expired) {
    task.run();
       }
       start = System.currentTimeMillis() - start;
       timer.cancel();
      } while (Math.abs(start - testtime) > EPSYLON);
      collectGarbage(3);
     }

 private void collectGarbage(int times) {
  for (int i = 0; i < times; i++) {
   System.gc();
   try {
    Thread.sleep(10);
   } catch (InterruptedException e) {
    Thread.currentThread().interrupt();
    break;
   }
  }
 }

 /**

  * Calculates the memory usage of a single element in a work queue. Based on Heinz Kabbutz' ideas
  * (http://www.javaspecialists.eu/archive/Issue029.html).
  * 
  * @return memory usage of a single {@link Runnable} element in the thread pools work queue
    */
     public long calculateMemoryUsage() {
      BlockingQueue<Runnable> queue = createWorkQueue();
      for (int i = 0; i < SAMPLE_QUEUE_SIZE; i++) {
       queue.add(creatTask());
      }
      long mem0 = Runtime.getRuntime().totalMemory() - Runtime.getRuntime().freeMemory();
      long mem1 = Runtime.getRuntime().totalMemory() - Runtime.getRuntime().freeMemory();
      queue = null;
      collectGarbage(15);
      mem0 = Runtime.getRuntime().totalMemory() - Runtime.getRuntime().freeMemory();
      queue = createWorkQueue();
      for (int i = 0; i < SAMPLE_QUEUE_SIZE; i++) {
       queue.add(creatTask());
      }
      collectGarbage(15);
      mem1 = Runtime.getRuntime().totalMemory() - Runtime.getRuntime().freeMemory();
      return (mem1 - mem0) / SAMPLE_QUEUE_SIZE;
     }

 /**

  * Create your runnable task here.
  * 
  * @return an instance of your runnable task under investigation
    */
     protected abstract Runnable creatTask();

 /**

  * Return an instance of the queue used in the thread pool.
  * 
  * @return queue instance
    */
     protected abstract BlockingQueue<Runnable> createWorkQueue();

 /**

  * Calculate current cpu time. Various frameworks may be used here, depending on the operating system in use. (e.g.
  * http://www.hyperic.com/products/sigar). The more accurate the CPU time measurement, the more accurate the results
  * for thread count boundaries.
  * 
  * @return current cpu time of current thread
    */
     protected abstract long getCurrentThreadCPUTime();

}
```

这篇文章写的通俗易懂，文章的标题是宪政的故事，怎么让宪政时更加的鲁棒呢？文章写得很棒，同学们可以看看。如果英文不好，可以借助谷歌翻译，翻译的质量还是不错的。当然了，文章中的知识点，课上都有覆盖的。好，我们回到英文状态。在这个地方有一个工具类，利用这个工具类就可以帮助我们迅速地调优线程池了。我们 copy 过来，粘贴，打包。


好了。这是一个抽象类，它里面有几个抽象方法，要想使用，只需要继承抽象类，实现一下里面的抽象方法就 OK 了。文章里面也有示例，我们来抄一下。粘贴。这个示例类里面有点问题，我们需要调整一下，否则编译不会通过。


这里的异常，不需要了。好，这里的 runable 指的就是我们实际项目里面需要运行的任务，由它来给你估算运行这些任务的线程数应该配多大， blocking queue 应该配置多大。所以我们需要写一个class，叫 a singness task，实现一下runable。这个任务我们简单一点，就让他打印一下当前的现成的名称。好吧，参数我们也不要了，这样代码就写好了。这里的参数每一个是什么意思？你可以点到源码里面去看一下。注释写得非常详细，我们这里也加一下注释。 0 指的是 c p u 目标利用率，相当于前面我们公式里面的you。 1.


第二个参数指的是 blocking queue，占用的内存大小，单位是 byte get current thread。 c b u time 指的是当前线程占用的总时间。 create a task 非常好理解，表示创建任务让 process calculator 进行计算你的线程池应该配置多大。 blocking queue 也比较好理解，在这里创建一个 blocking queue，交给 process calculator，这样 process calculator 就会根据你 blocking queue 的内存大小，计算出一个 blocking q 的大小。


运行一下。运行好了，他告诉你说我们的机器 CPU 核心数是8，我们期望的 CPU 占用率是百分之百。在测试的过程中，已经过去了这么多纳秒，线程运行了这么多纳秒，等待了这么多纳秒。最后他使用我们前面讲的公式进行了一个计算出来，建议线程数配置成8。 blocking queue 的大小。工具类也可以帮助我们计算出来。我们可以把这里的打印给去掉。


再次运行。可以看到它估算出来一个任务需要花费 40 byte，它用我们传入的 10 万 byte 除了一下，它说建议 kill 的 size 设成2500。好。有了工具类之后，相信同学们就可以非常方便的进行线程池的调优了。通过这个结果，假设我们的线程池运行的是这里的 asynchness task，我们的线程池就可以这样创建。拷贝一下前面的 thread pull executor 就可以这么玩。 corporal size 设成8， maxim 破 size 也设成8，这样可以降低线程创建的开销。


keep a lifetime 可以根据你的实际需要去设置。 block and queue 设成 2500 third factory 以及 aboard policy 也可以根据你的需要去设置。我们的调优过程被大幅度的简化了，但是需要注意课上介绍的几个公式，不管是 n 加 e 也好， RN 也好，还是公式也好，都仅仅是目前业界比较认可的经验值公式，并不是按照这些公式一定能够达到最优。实际项目中一定要结合自己的实际情况去调优。你可以按照这样的步骤去操作。


首先可以对自己的线程池做一个业务上的评估，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b4236790-32e7-4a1a-a8ce-4b51c1e00962/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46655PXHHT5%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230117Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCJS7N%2BUnfwpmp6u%2BSFBRdX3NcFEmNP1cJ4vmvFZmXsmQIhAKiojXCDexJ5VpQFH8V015V4UsrBJK3fMdDLR6TwURO0KogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzfEzsfpZ1A6C%2FDfGkq3AP%2BkbuB5Lv7limPWXdkvSEZo5p42ArGFuMeCL7ngyTPK6XSzgf01EXFuvoIDyfCqbXgD0wGNpD8w7KJs1oGyNvjK0A%2FtSrEzmJFYK2wIJEq1A6SatJJhfZEjfbd3ybkdtDL2wk1Uo0dfuAxlgws6ylr1erGCQzL%2BYkrvTsKT8%2FLgr4e6Fr7F%2F%2B%2Bg%2FuNk9ERmsUKxXUNwq6iQC698G3qaNTl3VS81C6M%2Fft6UkpCrdWst8jVl2pR%2Bv4wUGu5XzbrRy8arUFT7x7hCY%2FfAotappv09agOrG0y27QMHHLQSKeOMkio218AO3hxqTRcWF5qIwXokqoChLwAvBMeRc2fy3xGOW4k%2Fk%2FunD%2FAgtpar0z8O3J1S%2B3WU%2FTrdAkD1OQyqcv51CssuyaJcUefeyOOLe05DGtoa5QcnmXWs6wottJgiG4KmB6v86jv2RxXj0LDWKZvwRjKSP2Qb410GFKV52TeT5Vyvf5E%2FN4mJ22iRvfhgcW60h31GL4bymbg%2FxFz9sWEytbcDYwYhAuGOGBAef3mhh%2BUv6JCAzzsx82AeSF09ouqJSbCju3sH5e4qSyakC164ocJXUp8MyRSg92S569%2FGSChiqlD4TJeVWQC8Uz0lvUswLPhheV5Xu3wbDCCu%2F%2FSBjqkAZj9v92N3LgVwpaoGf3Jr2jIhX10YuRbwbu%2BC0Tg1eB5tCnpBgzjdI0HSaKrFSx0sn2DShO5dIm7vbB6YdQeE4zyMIIamHdCR7%2B2eOLfEltvw6uhJJcFgXXbx%2B0IQIOn8i0A6wFnIj1r57ozSLIU9jAKwkNkoE3zm%2FqAbc3crXmKY%2BVfmgF%2B9RRxFEIi0LGcTUi5P15rBDPUriUnpC%2BwKJwK3blq&X-Amz-Signature=92f13a67b57619586eba1e9597ebb35758ee21d7f73a5836877c31a245683bc7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

其中的任务是c、b、 u 密集型的、i、 o 密集型的或者是混合型的。可以利用公式去计算出一个建议的线程数，并且也可以评估出一个 blocking queue 的容量。第二，可以多次压测，并且去逐步调整线程池的大小。比方，把公式计算出来的线程数目加 1 + 2- 1- 2，在公式计算出来的数值周边进行滑动，多次对比，最终评估出一个表现最好的值，这样才能作为你线程池最终所使用的参数。好，这节课就到这里，谢谢大家。



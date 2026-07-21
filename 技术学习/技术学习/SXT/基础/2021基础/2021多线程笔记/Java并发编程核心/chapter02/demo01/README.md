---
title: demo01
---

# demo01

[file](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/35c69bc5-8210-4fa5-aa17-b6ae321cdbca/TryConcurrency01.java?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKYU4UFX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHBaPbz70rEMbxYugeqcmePzJXih7%2BR8B%2BqYo0qQJ6ApAiEA8LDZ5Gi08dwbWHYoy1GcSor11SkVpbkgJEl%2FuBpIqt4qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNFqz5QUsGOEtk6tcircA6WFMgYYcnyeOcz6mWZioggVTgzRc8ATQV2f7mBLcznNqhqC1bePcjR9l%2B%2BDnhH9TbFUikycSGq2hzf8Q5XBlxLdRzEP1Oneg557LAB9ltrebIFXcPkDiVlpc2NovAHNxDUXAFny353AfrM0%2BYTy3hUboEM4EGOHOCJLuLHsWrlqsdbod36Fc1ZduoqYHeopql57ljPF1p1G%2BLv4vEJWy8Ast5er%2BZ8UMOwLrsjqh9Mbp186NBsi9OgNHxqwN5p7%2BiY3uuAVRT3kb2rgVJRKcyfDuLUnKOK%2B5IKsc%2BQENIGa8jAOSGQFnWguqPelmnSQBjeeWmSabcpZusUlVu8Clf5eFpz%2BpbHHRXikdZlJz6nqcp4kAvV%2FSK%2BjbjKJDJKgHGB5uxpZJygtkEnppbVR8%2FcF9ahuR3sFlETGl5ma3EOHMnx8lwDPKSYoBLzo5HOb3qPEqrmLExkJJpnHYKyV8ReumwOhwgyLtNdiNKXk6G7vxS3NqCTWJF8raJPoIQUFgTDF2TWWbztK7gEF%2B3205DWQ00HujeUkUedrTryGTKQ66UGzFMlnpNpCQEWLeNIgL7ZTHznBct6NZVGDXLvnfI716JAVRbjuWIuF28rhT9wRoBbOttQQDaGlYjpVMLi4%2F9IGOqUB19stOzvcFdwZ1wPalYHBvS4yoqY8gvSiXs%2FkyBagJe61N1Pr4wdJV%2BXoF2Ny0sqpXInhrCY8A9IdWCPIGl1UhnfynYkewi9tkkuSXEkcQuRlNEe%2BZV0eIijsRP8HDHkWTUzuMjU%2FsT2pOQ2y7sSjfdLQh%2FITOVp38%2FFYy%2BASuscMZbfyelFTlv7Zn4i3GsdZVZp1qU9RqtCKjX2lz81%2FPEpINIVi&X-Amz-Signature=e7ca4e3a4e7a894a736cdd3d031e5371c62c9c8f9c4874402ebc4eb9ade5da4a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[file](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/a56ef722-0f06-49a6-82ac-ae592646698b/TryConcurrency02.java?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RKYU4UFX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232548Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIHBaPbz70rEMbxYugeqcmePzJXih7%2BR8B%2BqYo0qQJ6ApAiEA8LDZ5Gi08dwbWHYoy1GcSor11SkVpbkgJEl%2FuBpIqt4qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNFqz5QUsGOEtk6tcircA6WFMgYYcnyeOcz6mWZioggVTgzRc8ATQV2f7mBLcznNqhqC1bePcjR9l%2B%2BDnhH9TbFUikycSGq2hzf8Q5XBlxLdRzEP1Oneg557LAB9ltrebIFXcPkDiVlpc2NovAHNxDUXAFny353AfrM0%2BYTy3hUboEM4EGOHOCJLuLHsWrlqsdbod36Fc1ZduoqYHeopql57ljPF1p1G%2BLv4vEJWy8Ast5er%2BZ8UMOwLrsjqh9Mbp186NBsi9OgNHxqwN5p7%2BiY3uuAVRT3kb2rgVJRKcyfDuLUnKOK%2B5IKsc%2BQENIGa8jAOSGQFnWguqPelmnSQBjeeWmSabcpZusUlVu8Clf5eFpz%2BpbHHRXikdZlJz6nqcp4kAvV%2FSK%2BjbjKJDJKgHGB5uxpZJygtkEnppbVR8%2FcF9ahuR3sFlETGl5ma3EOHMnx8lwDPKSYoBLzo5HOb3qPEqrmLExkJJpnHYKyV8ReumwOhwgyLtNdiNKXk6G7vxS3NqCTWJF8raJPoIQUFgTDF2TWWbztK7gEF%2B3205DWQ00HujeUkUedrTryGTKQ66UGzFMlnpNpCQEWLeNIgL7ZTHznBct6NZVGDXLvnfI716JAVRbjuWIuF28rhT9wRoBbOttQQDaGlYjpVMLi4%2F9IGOqUB19stOzvcFdwZ1wPalYHBvS4yoqY8gvSiXs%2FkyBagJe61N1Pr4wdJV%2BXoF2Ny0sqpXInhrCY8A9IdWCPIGl1UhnfynYkewi9tkkuSXEkcQuRlNEe%2BZV0eIijsRP8HDHkWTUzuMjU%2FsT2pOQ2y7sSjfdLQh%2FITOVp38%2FFYy%2BASuscMZbfyelFTlv7Zn4i3GsdZVZp1qU9RqtCKjX2lz81%2FPEpINIVi&X-Amz-Signature=a9d3f1d9426646be099d24e33ddb8f4bf0ef9d83339a9ce50bc46f885369ebe2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


```java
package com.bjsxt.chapter02.demo01;

public class TryConcurrency01 {

    public static void main(String[] args) {
        browseNews();
        enjoyMusic();
    }

    // 浏览新闻
    private static void browseNews() {
        while (true) {
            System.out.println("The good news.");
            try {
                Thread.sleep(1000L);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

    // 欣赏音乐
    private static void enjoyMusic() {
        while (true) {
            System.out.println("The nice music.");
            try {
                Thread.sleep(1000L);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

}
```

```java
package com.bjsxt.chapter02.demo01;

public class TryConcurrency02 {

    public static void main(String[] args) {
        // JDK 1.8 之前匿名内部类
        Thread t = new Thread("BrowseNews") {
            @Override
            public void run() {
                browseNews();
            }
        };
        t.start();

        // JDK 1.8 Lambda 编码方式
        // new Thread(TryConcurrency02::browseNews).start();
        enjoyMusic();
    }

    // 浏览新闻
    private static void browseNews() {
        while (true) {
            System.out.println("The good news.");
            try {
                Thread.sleep(1000L);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

    // 欣赏音乐
    private static void enjoyMusic() {
        while (true) {
            System.out.println("The nice music.");
            try {
                Thread.sleep(1000L);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

}
```


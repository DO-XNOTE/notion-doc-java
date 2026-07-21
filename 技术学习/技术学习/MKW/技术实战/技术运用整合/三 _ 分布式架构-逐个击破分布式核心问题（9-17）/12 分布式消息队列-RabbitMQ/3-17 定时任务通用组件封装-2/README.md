---
title: 3-17 定时任务通用组件封装-2
---

# 3-17 定时任务通用组件封装-2

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/3bfb7c00-0e90-46b9-bd6c-43fd434a7e5a/SCR-20240806-sxbr.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQ2H5XWG%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCx3UPx8ol6%2BSjnREH2mOLO95cnaRAK9wpRNGxK5CgvEQIhAKGnBGjSkpB7BL1ojKiw3NDoTCiweNgahqEjQd4OqOY6KogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx1IZJVZLrx%2F832ajkq3ANSqM6%2F%2BP1F4a0ZnSs39pjUeMXeCuyGj5k9oX9%2B92lfWMCa23FjOa49yQjld2Tft0OXFp5kyj8fhyJ0o8w%2FRrZnMhNRZ61Y0W2YncGj45gFXG%2F5s8uT5cvE5WPRtQ%2Fy9G%2BUAA%2BNjY8T3xnjqvvaQeHZ5IZppT4QcaR258BZcRN%2BPwoXyvvQeD%2BlfLpVeIK60pU3jk7fsP4G2Zbfk85%2BfEE9RuXwSS181zSCTIDWVtGGIe%2F3PNW1x9r6WQu964mSBBzqNuJop0XJY8jUV8ye%2ByCUw0bPBpHLNmQMxbKtwUzazqEjVb3ezm6lyxZ5Oj8e7i2I2VG76v9HtRg%2BD0FyueSYThEHry5YPiAaSdEAj2sF5I9NzLlDQz5oIvsW2ohi7GXEVFzZeE7idzT4ruvoifaGt6EQZxc5C723SihdyoqKo2w34Mo62qdJJXCYy8KthpQcAer%2Fu8lRXEhhkBuxvSJqoDT4Ni3fGz74%2FgVocw8O3JqQFXyjISPHKupTlDWErIuaJs%2FMdSiX62wKAjDZfxwNdjg%2FzMG9erTGG%2BvoL%2FQlHYqgedkQXpslI%2BJJT8l%2FnV5D5JGDXUCix8%2BBFRkrWDyKPt%2B9K6SYYHrW%2BO%2BJz8DHPoIljee2dB9TDLUCJzDXuf%2FSBjqkAeWAy1wadipBmBzpyJwMfGTVG4GOspQXzOQLEkMvwf%2F55NdxfbhfFrp2UeR5%2BNhgQ0kMiCNpTJ%2F8%2Bl1b3B6BnlIiB%2F%2FpjIpz%2BOHYaJMKH6YiG5TyywIor28qdsvGbn6Z4DiLJwdkCCM2343PgICY%2BcfPSPMDwmQwQrzIAxXCdr%2B53l6RSp4ASIW6LXb9rtUn6UZAj7AWzqb3fqswcWgfOqqM71Qn&X-Amz-Signature=59f20a56631be2f4fdc0793531e97f2fcd8e5ebf1af20eff06bcd589ed82e290&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/5f48f9a3-07e4-4045-85de-30cfccdf9f81/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQ2H5XWG%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCx3UPx8ol6%2BSjnREH2mOLO95cnaRAK9wpRNGxK5CgvEQIhAKGnBGjSkpB7BL1ojKiw3NDoTCiweNgahqEjQd4OqOY6KogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx1IZJVZLrx%2F832ajkq3ANSqM6%2F%2BP1F4a0ZnSs39pjUeMXeCuyGj5k9oX9%2B92lfWMCa23FjOa49yQjld2Tft0OXFp5kyj8fhyJ0o8w%2FRrZnMhNRZ61Y0W2YncGj45gFXG%2F5s8uT5cvE5WPRtQ%2Fy9G%2BUAA%2BNjY8T3xnjqvvaQeHZ5IZppT4QcaR258BZcRN%2BPwoXyvvQeD%2BlfLpVeIK60pU3jk7fsP4G2Zbfk85%2BfEE9RuXwSS181zSCTIDWVtGGIe%2F3PNW1x9r6WQu964mSBBzqNuJop0XJY8jUV8ye%2ByCUw0bPBpHLNmQMxbKtwUzazqEjVb3ezm6lyxZ5Oj8e7i2I2VG76v9HtRg%2BD0FyueSYThEHry5YPiAaSdEAj2sF5I9NzLlDQz5oIvsW2ohi7GXEVFzZeE7idzT4ruvoifaGt6EQZxc5C723SihdyoqKo2w34Mo62qdJJXCYy8KthpQcAer%2Fu8lRXEhhkBuxvSJqoDT4Ni3fGz74%2FgVocw8O3JqQFXyjISPHKupTlDWErIuaJs%2FMdSiX62wKAjDZfxwNdjg%2FzMG9erTGG%2BvoL%2FQlHYqgedkQXpslI%2BJJT8l%2FnV5D5JGDXUCix8%2BBFRkrWDyKPt%2B9K6SYYHrW%2BO%2BJz8DHPoIljee2dB9TDLUCJzDXuf%2FSBjqkAeWAy1wadipBmBzpyJwMfGTVG4GOspQXzOQLEkMvwf%2F55NdxfbhfFrp2UeR5%2BNhgQ0kMiCNpTJ%2F8%2Bl1b3B6BnlIiB%2F%2FpjIpz%2BOHYaJMKH6YiG5TyywIor28qdsvGbn6Z4DiLJwdkCCM2343PgICY%2BcfPSPMDwmQwQrzIAxXCdr%2B53l6RSp4ASIW6LXb9rtUn6UZAj7AWzqb3fqswcWgfOqqM71Qn&X-Amz-Signature=bd39fdd3670df3e68a609d84475bb3803aafc7bf6eb7d058c23f4dd0b0250c6e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

我现在把 ZK 都已经搞定了，那第二件事情我们要做的是什么呢？是模块装配，模块装配意味着我要有一个什么enable，什么什么的，这个时候它才启动，要不然它就不启动。所以说在这里来看一看。比如说我在这里边来建一个新的包，我们叫做annotation。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/0f430fce-7b34-4e1a-b8b8-4642423b506d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQ2H5XWG%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCx3UPx8ol6%2BSjnREH2mOLO95cnaRAK9wpRNGxK5CgvEQIhAKGnBGjSkpB7BL1ojKiw3NDoTCiweNgahqEjQd4OqOY6KogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx1IZJVZLrx%2F832ajkq3ANSqM6%2F%2BP1F4a0ZnSs39pjUeMXeCuyGj5k9oX9%2B92lfWMCa23FjOa49yQjld2Tft0OXFp5kyj8fhyJ0o8w%2FRrZnMhNRZ61Y0W2YncGj45gFXG%2F5s8uT5cvE5WPRtQ%2Fy9G%2BUAA%2BNjY8T3xnjqvvaQeHZ5IZppT4QcaR258BZcRN%2BPwoXyvvQeD%2BlfLpVeIK60pU3jk7fsP4G2Zbfk85%2BfEE9RuXwSS181zSCTIDWVtGGIe%2F3PNW1x9r6WQu964mSBBzqNuJop0XJY8jUV8ye%2ByCUw0bPBpHLNmQMxbKtwUzazqEjVb3ezm6lyxZ5Oj8e7i2I2VG76v9HtRg%2BD0FyueSYThEHry5YPiAaSdEAj2sF5I9NzLlDQz5oIvsW2ohi7GXEVFzZeE7idzT4ruvoifaGt6EQZxc5C723SihdyoqKo2w34Mo62qdJJXCYy8KthpQcAer%2Fu8lRXEhhkBuxvSJqoDT4Ni3fGz74%2FgVocw8O3JqQFXyjISPHKupTlDWErIuaJs%2FMdSiX62wKAjDZfxwNdjg%2FzMG9erTGG%2BvoL%2FQlHYqgedkQXpslI%2BJJT8l%2FnV5D5JGDXUCix8%2BBFRkrWDyKPt%2B9K6SYYHrW%2BO%2BJz8DHPoIljee2dB9TDLUCJzDXuf%2FSBjqkAeWAy1wadipBmBzpyJwMfGTVG4GOspQXzOQLEkMvwf%2F55NdxfbhfFrp2UeR5%2BNhgQ0kMiCNpTJ%2F8%2Bl1b3B6BnlIiB%2F%2FpjIpz%2BOHYaJMKH6YiG5TyywIor28qdsvGbn6Z4DiLJwdkCCM2343PgICY%2BcfPSPMDwmQwQrzIAxXCdr%2B53l6RSp4ASIW6LXb9rtUn6UZAj7AWzqb3fqswcWgfOqqM71Qn&X-Amz-Signature=d81f2337a9cc0d9a143b9118975eb91fa9957315c50ed5e70bb42488ba319a1f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

好，这个 annotation 我们来先写第一个注解，这个叫做elected，或者叫做enable，我们的 elastic job，这个 job 好了搞定。嗯， able elastic job，那它作为一个注解，首先它有一个非常关键的属性，就是我们的什么 n type，然后还有它的这个 rate OK，这里边它就是 runtime proxy return box，点 runtime 在运行时起到作用。然后比如说他有其他属性 document 是不是？或者他是不是可以被继承的？就是说 in Harry，Harry。好了，这是作为一个注解最基本的 4 个属性。然后接下来如果你想要做这种事，什么enable，像 MBC enable，那应该怎么去做**？其实大家如果你不太清楚的话，那其实你可以去看一下unable，这是刚才我去写的，就是叫做 unable elected job，还有什么 unable a single， unable 等等 unable catching，还有 unable im been export。**

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/37a58d4b-128c-425a-b19f-9c6d603c3542/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQ2H5XWG%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCx3UPx8ol6%2BSjnREH2mOLO95cnaRAK9wpRNGxK5CgvEQIhAKGnBGjSkpB7BL1ojKiw3NDoTCiweNgahqEjQd4OqOY6KogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx1IZJVZLrx%2F832ajkq3ANSqM6%2F%2BP1F4a0ZnSs39pjUeMXeCuyGj5k9oX9%2B92lfWMCa23FjOa49yQjld2Tft0OXFp5kyj8fhyJ0o8w%2FRrZnMhNRZ61Y0W2YncGj45gFXG%2F5s8uT5cvE5WPRtQ%2Fy9G%2BUAA%2BNjY8T3xnjqvvaQeHZ5IZppT4QcaR258BZcRN%2BPwoXyvvQeD%2BlfLpVeIK60pU3jk7fsP4G2Zbfk85%2BfEE9RuXwSS181zSCTIDWVtGGIe%2F3PNW1x9r6WQu964mSBBzqNuJop0XJY8jUV8ye%2ByCUw0bPBpHLNmQMxbKtwUzazqEjVb3ezm6lyxZ5Oj8e7i2I2VG76v9HtRg%2BD0FyueSYThEHry5YPiAaSdEAj2sF5I9NzLlDQz5oIvsW2ohi7GXEVFzZeE7idzT4ruvoifaGt6EQZxc5C723SihdyoqKo2w34Mo62qdJJXCYy8KthpQcAer%2Fu8lRXEhhkBuxvSJqoDT4Ni3fGz74%2FgVocw8O3JqQFXyjISPHKupTlDWErIuaJs%2FMdSiX62wKAjDZfxwNdjg%2FzMG9erTGG%2BvoL%2FQlHYqgedkQXpslI%2BJJT8l%2FnV5D5JGDXUCix8%2BBFRkrWDyKPt%2B9K6SYYHrW%2BO%2BJz8DHPoIljee2dB9TDLUCJzDXuf%2FSBjqkAeWAy1wadipBmBzpyJwMfGTVG4GOspQXzOQLEkMvwf%2F55NdxfbhfFrp2UeR5%2BNhgQ0kMiCNpTJ%2F8%2Bl1b3B6BnlIiB%2F%2FpjIpz%2BOHYaJMKH6YiG5TyywIor28qdsvGbn6Z4DiLJwdkCCM2343PgICY%2BcfPSPMDwmQwQrzIAxXCdr%2B53l6RSp4ASIW6LXb9rtUn6UZAj7AWzqb3fqswcWgfOqqM71Qn&X-Amz-Signature=d3a8a1f01b372d91845b6ac086e4484cb272cfe46391ef689bf77a1924d9545f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

**当然我在这里边还有 enable schedule 的定时任务启动的，对吧？那这些都是属于什么呀？属于模块方式的装配，那包括 enable MVC 也是一样的，我们点进去看他怎么去做的，你看他怎么去做的。他除了有几个这个注解必须要有的圆注解以外，他还多了一个什么import，所以说我们就依葫芦画瓢，有一个import，然后 import 里边是一个什么configuration，然后一个bin，对不对？那我们就照这种方式去做就好了。那既然官方或者是说 spring 的这个都是这么去做，那我们也这样去做吧，搞一个 import 就好了。**

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/46899190-0ad8-4784-8d61-4baf950f3e08/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQ2H5XWG%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCx3UPx8ol6%2BSjnREH2mOLO95cnaRAK9wpRNGxK5CgvEQIhAKGnBGjSkpB7BL1ojKiw3NDoTCiweNgahqEjQd4OqOY6KogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx1IZJVZLrx%2F832ajkq3ANSqM6%2F%2BP1F4a0ZnSs39pjUeMXeCuyGj5k9oX9%2B92lfWMCa23FjOa49yQjld2Tft0OXFp5kyj8fhyJ0o8w%2FRrZnMhNRZ61Y0W2YncGj45gFXG%2F5s8uT5cvE5WPRtQ%2Fy9G%2BUAA%2BNjY8T3xnjqvvaQeHZ5IZppT4QcaR258BZcRN%2BPwoXyvvQeD%2BlfLpVeIK60pU3jk7fsP4G2Zbfk85%2BfEE9RuXwSS181zSCTIDWVtGGIe%2F3PNW1x9r6WQu964mSBBzqNuJop0XJY8jUV8ye%2ByCUw0bPBpHLNmQMxbKtwUzazqEjVb3ezm6lyxZ5Oj8e7i2I2VG76v9HtRg%2BD0FyueSYThEHry5YPiAaSdEAj2sF5I9NzLlDQz5oIvsW2ohi7GXEVFzZeE7idzT4ruvoifaGt6EQZxc5C723SihdyoqKo2w34Mo62qdJJXCYy8KthpQcAer%2Fu8lRXEhhkBuxvSJqoDT4Ni3fGz74%2FgVocw8O3JqQFXyjISPHKupTlDWErIuaJs%2FMdSiX62wKAjDZfxwNdjg%2FzMG9erTGG%2BvoL%2FQlHYqgedkQXpslI%2BJJT8l%2FnV5D5JGDXUCix8%2BBFRkrWDyKPt%2B9K6SYYHrW%2BO%2BJz8DHPoIljee2dB9TDLUCJzDXuf%2FSBjqkAeWAy1wadipBmBzpyJwMfGTVG4GOspQXzOQLEkMvwf%2F55NdxfbhfFrp2UeR5%2BNhgQ0kMiCNpTJ%2F8%2Bl1b3B6BnlIiB%2F%2FpjIpz%2BOHYaJMKH6YiG5TyywIor28qdsvGbn6Z4DiLJwdkCCM2343PgICY%2BcfPSPMDwmQwQrzIAxXCdr%2B53l6RSp4ASIW6LXb9rtUn6UZAj7AWzqb3fqswcWgfOqqM71Qn&X-Amz-Signature=76b33f1195fea2f29def97ec7239a4a3c1f5e9c71caf118777bb1a08365f6abf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

**import？我们 import 什么类呢？我们就是只要说加这个注解启动的时候，我们才把它引进来嘛，所以说我们在这里 import delay，就是我们自己刚才所定义的这个 pass auto configuration plus 好了，就 import 它，那这个注解就行好了，相当于你自己去用的时候，你必须要做这个引用，叫做import。必须要做这个启用，你不启用是不好使的，只有启用我才会去加载，就这么一个事情。**


[file](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/82cf6c41-108f-4390-987e-09e8e55cdda0/RabbitMQ%E6%B6%88%E6%81%AF%E6%9C%8D%E5%8A%A1%E7%94%A8%E6%88%B7%E6%89%8B%E5%86%8C.docx?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQ2H5XWG%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225309Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCx3UPx8ol6%2BSjnREH2mOLO95cnaRAK9wpRNGxK5CgvEQIhAKGnBGjSkpB7BL1ojKiw3NDoTCiweNgahqEjQd4OqOY6KogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx1IZJVZLrx%2F832ajkq3ANSqM6%2F%2BP1F4a0ZnSs39pjUeMXeCuyGj5k9oX9%2B92lfWMCa23FjOa49yQjld2Tft0OXFp5kyj8fhyJ0o8w%2FRrZnMhNRZ61Y0W2YncGj45gFXG%2F5s8uT5cvE5WPRtQ%2Fy9G%2BUAA%2BNjY8T3xnjqvvaQeHZ5IZppT4QcaR258BZcRN%2BPwoXyvvQeD%2BlfLpVeIK60pU3jk7fsP4G2Zbfk85%2BfEE9RuXwSS181zSCTIDWVtGGIe%2F3PNW1x9r6WQu964mSBBzqNuJop0XJY8jUV8ye%2ByCUw0bPBpHLNmQMxbKtwUzazqEjVb3ezm6lyxZ5Oj8e7i2I2VG76v9HtRg%2BD0FyueSYThEHry5YPiAaSdEAj2sF5I9NzLlDQz5oIvsW2ohi7GXEVFzZeE7idzT4ruvoifaGt6EQZxc5C723SihdyoqKo2w34Mo62qdJJXCYy8KthpQcAer%2Fu8lRXEhhkBuxvSJqoDT4Ni3fGz74%2FgVocw8O3JqQFXyjISPHKupTlDWErIuaJs%2FMdSiX62wKAjDZfxwNdjg%2FzMG9erTGG%2BvoL%2FQlHYqgedkQXpslI%2BJJT8l%2FnV5D5JGDXUCix8%2BBFRkrWDyKPt%2B9K6SYYHrW%2BO%2BJz8DHPoIljee2dB9TDLUCJzDXuf%2FSBjqkAeWAy1wadipBmBzpyJwMfGTVG4GOspQXzOQLEkMvwf%2F55NdxfbhfFrp2UeR5%2BNhgQ0kMiCNpTJ%2F8%2Bl1b3B6BnlIiB%2F%2FpjIpz%2BOHYaJMKH6YiG5TyywIor28qdsvGbn6Z4DiLJwdkCCM2343PgICY%2BcfPSPMDwmQwQrzIAxXCdr%2B53l6RSp4ASIW6LXb9rtUn6UZAj7AWzqb3fqswcWgfOqqM71Qn&X-Amz-Signature=a866b43658295d33d344c90007f3727928b92547e3a3ff7754a00b00586c5699&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

OK，好了， import 这个事情搞定了，接下来我们想一想，除了这一个住址之外够不够呢？很明显是不够的，为什么呢？因为我们可能还需要有多一的配置。哪些配置？就是关于我们 ES job 的一些配置，这些配置都在哪呢？其实都在，我们所看到的这些东西就是你的 simple job，起码你这个 job 应该有个名字，有一个 cran 表达式，包括你的分片的总数是多少，你分片的item，包括你的 fail over，你的 monitor execution，包括 monitor port 等等。


‘这些配置可能我们都需要用，那这些配置从哪来？就是从官方文档来，就是说我们现在不要做那种代码级别的模板，不是说我自己新加一个job，我就把这个代码就这么去写了，将近小 100 行代码，那每一个 job 我都得写 100 行代码，我能不能用这种注解的方式，配置的方式去做呢？这是可以的，所以说我们在这里提供一个注解，同学们请看，在这里我提供一个注解，它的名字叫什么？叫做 ES job config。可以，好，allotation，我们叫做 elastic job config，就是 ES job config。那这个 ES job config 里面它都有哪些东西？先不着急，我们先把它最关键的，其实你写一个注解，比较关键的就是 target 跟这个return，那这个里边我们 element type 就等于 type 吧，就是表示在方法上，在类上，在哪都可以用。然后这个 run time 没什么说的， ATM box 点 run time 好搞定。这里边的配置项就是你自己想写一个照本，那你就按照我的配置项给它加到一个类上，我就能够帮你去解析，帮你动态的去生成。我们之前 ES job 里边我们要写的这一坨，就是这一堆的代码，我写一遍就够了。好，他都有哪些配置的？配置太多了去了，对不对？我们来看一看，就是他的作业的配置项。

首先 job name， crown 表达式，还有什么，就是sharding，items，param，还有等等fareover，还有这个 Mr 就是否开启错过任务重新执行。 


description 描述这个作业描述信息。 job practice，我们浏览一下，包括这里边这些东西可能都是我们需要，在这个注解里面我们需要做配置的东西，我们需要定义的一些属性，就是这些可能都需要，包括下面这些有一些东西我们可能都需要。那接下来老师一个一个的领着小伙伴们去写，然后加以说明。


首先我们对应的我们可以说 string name 对不对？就这样去写了，表示什么呢？相当于我们的 elses job 的奴字名称。然后怎么去迅速去想这个就是 crime 表达式默认go，默认就是call，可以吧？那其实我说为什么默认空这个确认值，这不就是空吗？然后有的确认值是什么 false 是 true 什么的，你就按照这个来就好了。然后这个 C20 todo count 它默认是什么？它默认值，分片作业的分片总数，它默认值。其实那你想想你的定时任务，你分片，你既然跑定时任务了，你的 default 不能是0，最好是一个 1 好了，还有哪些属性，还有什么 sharing item 对不对？就拿过来，它也是一个 string 类型，默认是一个公职， default 就是公职。


好，除了有这几个以外还有什么呀？斯特类型的 job parameter，如果你自己特殊，有些参数的话，你可以传进来。OK，其实我现在也是帮着大家去熟悉API，还有什么呢？还有 sell over 失败就是开启失败转移对不对？如果当前这个任务执行失败了，执行的过程中宕机了，那他会把这个任务未完成给他在另一件上去做，重做，重新再补偿执行了。其实你在自己封装的时候，就我为什么说就是在基础架构组去做事情会比较有意思的原因是你会对它的开源框架，或者你自己自研的一些框架，你会对它的这个 API 了解得非常清楚，不要不然的话你自己了解不清楚，那你怎么去给别人封装这个东西，然后让别人去用呢？这个默认是 true 哈，错过执行、重新执行和默认是处的。


所以说小伙伴们，你自己在工作中去学一个东西的时候，除非什么呢？除非说你们公司这个技术非常非常的重要，不然的话你只是说简单的会去使用而已，那这个你是没有深度的，说白了说你深度是不够的，你必须要深度，要非常的够，然后再去考虑广度好了。然后还有哪些呢？其实它有很多很多，比如说这个叫做 job practice，这个 job practice 就是说定义配置的这个做异常的这个，我们后面再去做这个就没必要了。然后再往下看什么 job config process 没什么可说的，这个 monitor 相关的这些配置一会我们也都需要配一下。还有哪些就比较关键的，当然我不可能说把所有的配置都写了，肯定不会说特别特别全在这，但是我尽量把我们常用的跟大家一起封装一下override，对不对？事物覆盖默认是boss。


然后接下来那个 streaming word 类型的streaming，就是如果你是流计算的话，会有这么一个，这个对不对？ streaming process 这个大写 default 是false，然后除了它还有什么呀？还有很多，比如说其实你可以看还有这个就是我们的 ESL 一共有三种类型，第一种类型就是我们的简单job，第二种类型是我们的这种流式的job。第三种就是脚本，如果你是脚本的话，那它也是有一个 script command line 干什么？这就是脚本型作业的执行命令。

```java
package com.bfxy.rabbit.task.annotation;

import com.bfxy.rabbit.task.autoconfiguration.JobParserAutoConfigution;
import org.springframework.context.annotation.Import;

import java.lang.annotation.*;

/**
 * <h1></h1>
 */
@Target(ElementType.TYPE)
@Retention(RetentionPolicy.RUNTIME)
@Documented
@Inherited
@Import(JobParserAutoConfigution.class)
public @interface EnableElasticJob {

    String name();  // 	作业名称

    String cron() default ""; //  	CRON 表达式，用于控制作业触发时间

    int shardingTotalCount() default 1; // 作业分片总数

    String shardingItemParameters() default ""; // 个性化分片参数

    String jobParameter() default ""; // 作业自定义参数

    boolean failover() default false; // 	是否开启任务执行失效转移

    boolean misfire() default true; // 是否开启错过任务重新执行

    String description(); // 作业描述信息

    boolean overwrite() default false; // 本地配置是否可覆盖注册中心配置

    boolean streamingProcess() default false; // 是否进行流失处理， 如果进行流失处理，则 fetchData 不返回空结果将继续执行作业，如果飞流失处理，则处理完成后作业结束

    String  scriptCommandLine()  default ""; // 脚本作业执行命令行

    boolean monitorExecution() default false; // 监控作业运行状态，每次执行时间和检核时间均非常短的情况，建议不监控作业的运行状态以提升效率

    public int monitorPort() default -1;	//must

    public int maxTimeDiffSeconds() default -1;	//must

    public String jobShardingStrategyClass() default "";	//must

    public int reconcileIntervalMinutes() default 10;	//must

    public String eventTraceRdbDataSource() default "";	//must

    public String listener() default "";	//must

    public boolean disabled() default false;	//must

    public String distributedListener() default "";

    public long startedTimeoutMilliseconds() default Long.MAX_VALUE;	//must

    public long completedTimeoutMilliseconds() default Long.MAX_VALUE;		//must

    public String jobExceptionHandler() default "com.dangdang.ddframe.job.executor.handler.impl.DefaultJobExceptionHandler";

    public String executorServiceHandler() default "com.dangdang.ddframe.job.executor.handler.impl.DefaultExecutorServiceHandler";

}
```

这个其实你想封装也可以把它封装进来，其实我在这里实际工作中用的并不是很多，大家一起封装进来就好，好慢的烂，对吧？它默认什么呢？既然是脚本的话， default 肯定是一个cover，是一个string。接下来我们看一看那些monitarm，就是刚才所看到的那些监控什么的，再往上走一点，就在这，它里边有什么？有模拟听execution，它是一个布尔类型的，我现在定义这么多东西为它干什么呀？就是为了后面我去实现，在用的时候我只需要对这个注解做一个配置就好了，然后还有哪些比如说 monitor point 等等，在这呢，老师就不去一个个写了，因为这个比较浪费时间。小伙伴们应该能理解老师的意思，就是说我把它按照我的这个官方的API，然后自己去把我想要的属性加到我对应的这个配置里， elite job config 里边，这就可以了。OK，那在这里老师把剩余的直接都粘过来，然后跟大家简单来看一下你这些配置，我浪费半小时，我写的没有意义了。


好，我们来看一下这里边有 monitoring 相关的对不对？还有什么？还有比如说你的 job selling city，就是你的 job 的这个策略，就是 sharing 策略，还有一些listener，还有一些分布式的listener，还有启动完成的一些时间，超时时间、 time out 时间，包括异常的时候 job exception handler 以及 executor service handler 等等。那这是当网默认的类，你可以通过官方文档，就是官方文档，你自己都可以去找得到，都可以看得到。

好，这一步我们就已经完成了，相当于我们对于什么呢？我们对于我们自己实现的这个 elastic job config 这个注解，它里边规定了这么多属性，已经搞定了。接下来我们来看我们要做什么事情，其实现在 2 个注解已经写完了，那接下来我们肯定就是要解析这个注解呀，注解写完了，接下来你就解析这个注解就可以了。OK，那在这里呢，我们稍微暂停一下这节课，我们先讲到这下节课呢，我们来对于这个注解进行一个解析，看看怎么去跟我们斯科人进行一个整合。好了，感谢小伙伴们收看。


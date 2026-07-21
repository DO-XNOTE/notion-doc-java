---
title: 2-7 上传头像-大小限制，以及自定义捕获异常
---

# 2-7 上传头像-大小限制，以及自定义捕获异常

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/f55ae725-a89f-4804-8792-ec2cb093480b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662LPEGZP6%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224728Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCZmRB9HtgII%2F32fCz2tHhBfThNlZSQ5x%2BJnY%2B7JXDvIAIgGqFpXuUzrccSfZO1RAq13oM0ahBEdAR8XJd97C74ReQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLzLjZ7Pe0bKuB7jayrcAxSi7YBQnlhRHO3vrbMRYs0pM4XxS9PKx3VndjCjK0ueR6lnGNMCHSYqQRQ%2BrQi8qJOvTG5KePhqI3IxDCBUC9FJQS%2BBg7uKswDZHePCpBRZSsXFq4Gkh5WV25SbunUA%2FwGG1Nj6pW27OBifRMhntxxLybOfJ%2B6uaW3OoyopasV92YdqECIQSirwDVJ2Ws%2B0SdUyHOxkKzc7eENHa7vGkkViS7u54DMIPczzNhfzbooDI3ueI53i7TtRLpbMMfGxnxA4q51OgMPXtIbk6ipKgUNjuEQqb6TVm7oIAzTfPigKDpGe9xAOm7O1mJTgx4kwsbdIWCN7cMIRi3s3QD73cv04BdAQA3MFH3%2BP1lyLuoIyIwD3KCk3sLALXZXnp3bOCY7yG8xkCgtFZu3DlZoiBy%2FBfG6CTDubdtAvZYh3A%2Bhx%2F8BrdKiAh6QxYfzcVBfIoorgOdzxmcJHgPjdR%2Fcs41QmzsWs31M0VFvbH66PwZ7gEHdes98uFYQiLsL%2BW5sAs%2FaDaVHWnCfXC9wg9%2BAKFtloP0cyGPRPCP%2F%2BoMlieZs3ZsEiP4c0WUkQGc3wYcNxSCh7otUeFALRxrUKFL2O%2ByF7qI0PLkvRf0lL3azi6z%2FWo9bzvOUypGVvvp0GMLS3%2F9IGOqUBH99MGAfFcocoZSKD6IEwonhaKPI%2B%2BXNBT0pzDQ1DcN%2B5RmLj%2FeKAnZQnQXoU4w5vXFvW1nRbSUBWFS0YZ%2Fb2awxorpOwOJTI9kF2SGhW2DlnR3cl6GG0EVATmpGMGbCZrxZq9xgtObBJ66ci8fXE06mz%2F6QAlk1tw93FS9HOdYYRCOHGeM6v4t7IS0gBWPf7D7b%2BtLEDlbHUOWaji%2FNzTtz6wECm&X-Amz-Signature=d938c0567819330a643fe65c46152038118f47df0506196fc1e5fac80287ba1c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

图片上传接口其实我们现在就已经是 OK 了，上一节我们也是完善了一下图片格式的限制，这一节我们还是接着来看一下图片上传。在我们做图片上传的时候，其实我们可以到这里来看一下，之前我们所上传的一些图片，其实它的大小其实都并不是很大，来看一下 face 1 和 face 2，它们就只有是 50K 和91K。如果我现在有一张是 500 多 k 的图片，能不能够去上传，甚至于我现在有一个 1 兆的， 10 兆的， 20 兆的图片，我们这些能不能上传，其实我们都应该要限制掉。


其实往往在我们涉及到一些图片上层的时候，我们的图片大小大多会限制在 200K 以内，或者是 500K 以内，都会有各种情况的限制，对于这种限制，现在我们的一个项目里面其实并没有加。如果我现在去上传一张 500K 的图片，也是没有问题的，可以来看一下。在我们头像上传的地方，我直接选择一下这一张 500K 的图片，双击一下你就可以发现图片是上传。 OK 是可以成功的。OK，它没有问题，但是图片太大了，我们应该要限制。如何去做到一个限制。


我们回到开发工具，在咱们的代码里面找到application，点 YAML 文件，双击，在这里面会有一个 spring 节点，我们来看一下。在 spring 下有一个叫做servlet。再来往下面看，这里面会有一个叫做 Max file size，这是一个最大文件的大小，它默认是 1 兆。随后下方还有一个叫做 Max request size，这是一个最大的请求。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/30dc815e-6bd2-4c9e-bc52-b909376b6568/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662LPEGZP6%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224728Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCZmRB9HtgII%2F32fCz2tHhBfThNlZSQ5x%2BJnY%2B7JXDvIAIgGqFpXuUzrccSfZO1RAq13oM0ahBEdAR8XJd97C74ReQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLzLjZ7Pe0bKuB7jayrcAxSi7YBQnlhRHO3vrbMRYs0pM4XxS9PKx3VndjCjK0ueR6lnGNMCHSYqQRQ%2BrQi8qJOvTG5KePhqI3IxDCBUC9FJQS%2BBg7uKswDZHePCpBRZSsXFq4Gkh5WV25SbunUA%2FwGG1Nj6pW27OBifRMhntxxLybOfJ%2B6uaW3OoyopasV92YdqECIQSirwDVJ2Ws%2B0SdUyHOxkKzc7eENHa7vGkkViS7u54DMIPczzNhfzbooDI3ueI53i7TtRLpbMMfGxnxA4q51OgMPXtIbk6ipKgUNjuEQqb6TVm7oIAzTfPigKDpGe9xAOm7O1mJTgx4kwsbdIWCN7cMIRi3s3QD73cv04BdAQA3MFH3%2BP1lyLuoIyIwD3KCk3sLALXZXnp3bOCY7yG8xkCgtFZu3DlZoiBy%2FBfG6CTDubdtAvZYh3A%2Bhx%2F8BrdKiAh6QxYfzcVBfIoorgOdzxmcJHgPjdR%2Fcs41QmzsWs31M0VFvbH66PwZ7gEHdes98uFYQiLsL%2BW5sAs%2FaDaVHWnCfXC9wg9%2BAKFtloP0cyGPRPCP%2F%2BoMlieZs3ZsEiP4c0WUkQGc3wYcNxSCh7otUeFALRxrUKFL2O%2ByF7qI0PLkvRf0lL3azi6z%2FWo9bzvOUypGVvvp0GMLS3%2F9IGOqUBH99MGAfFcocoZSKD6IEwonhaKPI%2B%2BXNBT0pzDQ1DcN%2B5RmLj%2FeKAnZQnQXoU4w5vXFvW1nRbSUBWFS0YZ%2Fb2awxorpOwOJTI9kF2SGhW2DlnR3cl6GG0EVATmpGMGbCZrxZq9xgtObBJ66ci8fXE06mz%2F6QAlk1tw93FS9HOdYYRCOHGeM6v4t7IS0gBWPf7D7b%2BtLEDlbHUOWaji%2FNzTtz6wECm&X-Amz-Signature=75a74b597cad36bc9df136baa8a8c0411e2d33414d7a0350b7ec6cbc6beca1c5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

的大小是实兆。很显然，其实这 1 兆和 10 兆其实太大了。我们应该要做一个限制，我们在这里就可以把它们限制为500K。我们分别都可以来进行一个添加。 500K 其实就应该是 5 乘以 1024 对吧。其实相应的应该是五一二零零零对吧？这是 500 12K。好，这是一个大小限制，一下，加一个注释文件上传大小限制为 500 k b 下。还有是一个Max，有 quest size，这是一个最大请求，我们也来加一下，这是最大请求，请求大小限制为 500 KB。这样子就可以限制我们文件的一个上传的大小。好，重启一下服务器。

```yaml
############################################################
spring:
  profiles:
    active: dev          # 多环境配置激活 spring.profiles.active
  datasource:                                         # 数据源的相关配置
    type: com.zaxxer.hikari.HikariDataSource          # 数据源类型：HikariCP
    driver-class-name: com.mysql.cj.jdbc.Driver        # mysql驱动
#    url: jdbc:mysql://localhost:3306/foodie-shop-dev?useUnicode=true&characterEncoding=UTF-8&autoReconnect=true
    username: root
#    password: guojun12
    hikari:
      connection-timeout: 30000       # 等待连接池分配连接的最大时长（毫秒），超过这个时长还没可用的连接则发生SQLException， 默认:30秒
      minimum-idle: 5                 # 最小连接数
      maximum-pool-size: 20           # 最大连接数
      auto-commit: true               # 自动提交
      idle-timeout: 600000            # 连接超时的最大时长（毫秒），超时则被释放（retired），默认:10分钟
      pool-name: DataSourceHikariCP     # 连接池名字
      max-lifetime: 1800000           # 连接的生命时长（毫秒），超时而且没被使用则被释放（retired），默认:30分钟 1800000ms
      connection-test-query: SELECT 1
  servlet:
    multipart:
      max-file-size: 512000     # 文件上传大小限制为500kb
      max-request-size: 512000  # 请求大小限制为500kb
```

好，重启成功。再回到咱们的前端，在这里先刷新一下，我们再来，这个时候我们来选择一下500K，再来我们直接双击一下，这个时候双击以后在我们的页面上没有发生任何的效果。很显然在我们的后端应该是报错了吧。我们回到后端，把控制台打开，在这里可以看到会报了一个错，会提示这里有一个 file upload，有一个请求被驳回了，因为它的大小是这么大，但是我们配置的是一个 500K 对吧？超过了我们的预设值，所以就会报一个错。相应的在我们的前端其实就没有任何的响应了。异常的确是抛出了，但是异常抛出了以后，其实我们应该要 catch 一下，我们应该要把它以一个合适的形式去返回到前端，要提示用户，你现在上传的一个文件，它太大了，你应该要去做一个压缩对吧？你应该要降低一下图片的质量。所以我们应该要去把 Max upload size exception 异常要去捕获一下，去进行一个处理，再把相应的信息更加人性化的再反馈给用户。所以我们在这里先把拷贝一下。

```java
/**
 * <h1>文件上传异常捕获</h1>
 */
@SuppressWarnings("all")
@RestControllerAdvice
public class CustomExceptionHandler {

    // 上传文件不能超过500k
    @ExceptionHandler(MaxUploadSizeExceededException.class)
    public IMOOCJSONResult handlerMapUploadFile(MaxUploadSizeExceededException exception) {
        return IMOOCJSONResult.errorMsg("文件上传大小不能超过500k,请压缩文件大小");
    }

}
------------------------------------------------------------------------------------------
/*
 * Copyright 2002-2017 the original author or authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      https://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package org.springframework.web.multipart;

import org.springframework.lang.Nullable;

/**
 * MultipartException subclass thrown when an upload exceeds the
 * maximum upload size allowed.
 *
 * @author Juergen Hoeller
 * @since 1.0.1
 */
@SuppressWarnings("serial")
public class MaxUploadSizeExceededException extends MultipartException {

	private final long maxUploadSize;


	/**
	 * Constructor for MaxUploadSizeExceededException.
	 * @param maxUploadSize the maximum upload size allowed,
	 * or -1 if the size limit isn't known
	 */
	public MaxUploadSizeExceededException(long maxUploadSize) {
		this(maxUploadSize, null);
	}

	/**
	 * Constructor for MaxUploadSizeExceededException.
	 * @param maxUploadSize the maximum upload size allowed,
	 * or -1 if the size limit isn't known
	 * @param ex root cause from multipart parsing API in use
	 */
	public MaxUploadSizeExceededException(long maxUploadSize, @Nullable Throwable ex) {
		super("Maximum upload size " + (maxUploadSize >= 0 ? "of " + maxUploadSize + " bytes " : "") + "exceeded", ex);
		this.maxUploadSize = maxUploadSize;
	}


	/**
	 * Return the maximum upload size allowed,
	 * or -1 if the size limit isn't known.
	 */
	public long getMaxUploadSize() {
		return this.maxUploadSize;
	}

}

```


以后，现在我们就要去捕获咱们的一个异常了。好在我们的项目里面。在这里我们可以去新创建一个包，创建一个包，取一个名字叫做exception。好，创建了一个包了。以后，在我们再创建一个类，这个类取一个名字叫做， custom exception handle 了，就是自定义的一个异常助手类。在这里面我们就可以去捕获一下这个异常了，写一下捕获，就叫做异常。对于我们的一个思喷容器来讲，既然它是一个助手类，所以我们在这里应该要去增加一个注解，叫做 rest control。使用注解，我们的容器会扫描。在这里面我们要去捕获。捕获还写一个叫做public。由于捕获到信息，我们要一个 JSON result，一个结果及返回，所以我们返回可以使用 imock JS result。


在这里写一个方法名，我们取的名字叫做 handle Max Upload file。就在这里去写这样的一个方法。其中在这里面我们是需要去传进来一个相应的异常，异常，其实异常刚刚在我们后台报的异常，它是捕获，它是会捕获到的。你一个 EX 传入，传入进来以后，直接我们在这里可以做一个 return 了，也称 m 可杰森 result 点 error message。在这里做一个消息的提示。我们在这边写一下文件，上传大小不能超过500K，请压缩图片或者降低图片质量。在上传。OK，这就是我们的一个错误的信息。这个方法写完了以后，在这里你还要去追加一个注解，叫做 exception handle，为我们的异常提供一个助手。在这里我们直接只需要把当前你要去捕获的异常的类给放进去就可以了，也就是当前异常点 plus 这样子去放进去，他就可以去捕获了。我们在这边去加一个注释，上传文件，超过 500K 捕获异常，捕获异常。


OK，好，现在我们就可以做一个测试了，在这里直接重启一下服务器，好，启动成功。回到咱们的一个页面，刷新一下。在这里还是一样，我选择这一张 500K 的图片，直接双击上传。好，OK。提示了一个错误的信息，文件上传大小不能够超过500K，请压缩图片质量，或者降低图片的质量再上传。


OK。现在我们就已经是成功的捕获到相应的异常了，这样子我们的一个错误信息也能够更加的一个人性化的反馈给用户，让用户知道你现在图片的一个大小是需要去做一个更改的。OK。而且图片的一个大小其实是在很多的一些互联网的网站，绝大多数其实都会寻到，你不能够收集的太大。极端情况下，其实我遇到过最大的一个图片是不能够超过50K，这个其实是真的是太小。一般来说我们自己设定为200K、300K、 500K 就可以了。千万不要超过500K，一方面太大了，另外一方面也会导致你的一个文件，它会占用你的一个绝大多数的硬盘容量。这一点去注意一下。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/230b86d9-916a-431e-a17a-e813839cb9c6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662LPEGZP6%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224728Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCZmRB9HtgII%2F32fCz2tHhBfThNlZSQ5x%2BJnY%2B7JXDvIAIgGqFpXuUzrccSfZO1RAq13oM0ahBEdAR8XJd97C74ReQqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLzLjZ7Pe0bKuB7jayrcAxSi7YBQnlhRHO3vrbMRYs0pM4XxS9PKx3VndjCjK0ueR6lnGNMCHSYqQRQ%2BrQi8qJOvTG5KePhqI3IxDCBUC9FJQS%2BBg7uKswDZHePCpBRZSsXFq4Gkh5WV25SbunUA%2FwGG1Nj6pW27OBifRMhntxxLybOfJ%2B6uaW3OoyopasV92YdqECIQSirwDVJ2Ws%2B0SdUyHOxkKzc7eENHa7vGkkViS7u54DMIPczzNhfzbooDI3ueI53i7TtRLpbMMfGxnxA4q51OgMPXtIbk6ipKgUNjuEQqb6TVm7oIAzTfPigKDpGe9xAOm7O1mJTgx4kwsbdIWCN7cMIRi3s3QD73cv04BdAQA3MFH3%2BP1lyLuoIyIwD3KCk3sLALXZXnp3bOCY7yG8xkCgtFZu3DlZoiBy%2FBfG6CTDubdtAvZYh3A%2Bhx%2F8BrdKiAh6QxYfzcVBfIoorgOdzxmcJHgPjdR%2Fcs41QmzsWs31M0VFvbH66PwZ7gEHdes98uFYQiLsL%2BW5sAs%2FaDaVHWnCfXC9wg9%2BAKFtloP0cyGPRPCP%2F%2BoMlieZs3ZsEiP4c0WUkQGc3wYcNxSCh7otUeFALRxrUKFL2O%2ByF7qI0PLkvRf0lL3azi6z%2FWo9bzvOUypGVvvp0GMLS3%2F9IGOqUBH99MGAfFcocoZSKD6IEwonhaKPI%2B%2BXNBT0pzDQ1DcN%2B5RmLj%2FeKAnZQnQXoU4w5vXFvW1nRbSUBWFS0YZ%2Fb2awxorpOwOJTI9kF2SGhW2DlnR3cl6GG0EVATmpGMGbCZrxZq9xgtObBJ66ci8fXE06mz%2F6QAlk1tw93FS9HOdYYRCOHGeM6v4t7IS0gBWPf7D7b%2BtLEDlbHUOWaji%2FNzTtz6wECm&X-Amz-Signature=7ce3006d289f6d040898a1ac7414b3911012cc12df3a1426a2f16fb16fa31c57&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


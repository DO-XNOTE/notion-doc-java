---
title: 3-6 整合Swagger2文档api
---

# 3-6 整合Swagger2文档api

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/1f38b97d-5dd6-4f69-a40b-6a6bfeb7e728/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TAAJKNXU%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224626Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEfEPK7JbdRs4ZImHFfuJCeq9x7sy2eMdWefVlGOyq6eAiBuODiXUXSwm%2F1dw%2Bv3e5fCybWYq%2BxJAkxfwM5%2FSp70UyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMaXnNY5Lh7as5tlMZKtwDpFZ6KAPw6iolrXjK%2F8JrfCNhHxCT0qwiaj8I3d2P5Te2jdVOhvrOOVBLKZCIEUULZeVkmKNLRiyM6wHjDLhRXdfsP2oKDi1NShI95g1ReoQp%2FeNE%2FVKaK16sG2yI%2BS5fR5Rly%2FMVVFp9wDQx8Z6VlUp9d3WVnu3vNVLvDwQyMdjR0C3nKNF0CaU5PPX1udeP%2FFljepE6iJdLunp1HkpHj9do0eAuRjJNiyCSX9dE%2FFM11OPRZUk4EBaiW2UhleOPL%2B2h%2FWv3UhBX0BE7Nl%2FXQbQBRS9Zg%2BEuUfd1iZDxel3Dwda5B1xp55q%2BcNO%2B%2F0CD%2B9ZTOH8D06f4HaBdInDUTzst3%2BHJKlxYTwquHh28aG6q0NhfnNOXIpdm1if1Bzj4lNUYa4KID3ro%2B%2FlgiMlYctWtMItfXLRFKjtgophPCTBo8xIQaXsXc2mnzgKDSzTfjI8YTwz6JJyfvjlCXJB%2F05gXCUh1UENQU7A2g%2FYf%2BE%2B3tAGN3CQeC8ePneje1%2BhwG3DJwAmL7DTtU2Z2MryH1xgIL7eJX1CbIIWJY0sK7goDDGA8%2FjE3juKE1KXJ505311%2Fh3p8rry68efbcwr72ZF4EmRwrEmlJmw7JWcasya0inHb0dWDqI0ZFBR4whbv%2F0gY6pgEesgongaWeRG%2FuKOjYGADpeYieRM5XOgar6DSmQtjgZh0QJy18sql%2FJ60OY8jj2JjN88Tk%2B7BvCGEF12yMqkjchq6f8T2LrbVsdQhn6nku%2FGck4ILVji3fJWO9ChnMzoWsNpxXDqGiH48hplIR%2B%2F91B%2FIEj6eqWnpyQdO6FfcBUb77WuXQX%2F6t8iqrIDcnKTiKPC0pMzyQLckuaxll7CNk0U604Vgn&X-Amz-Signature=f377b2260721c34828e56476d0aabea445087f93ff9c944292aaead1117b9bda&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[file](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/df647218-aa46-43b7-ba25-cb6eded03e31/3-7_%E5%9B%BE%E6%96%87%E8%8A%82.pdf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TAAJKNXU%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224626Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEfEPK7JbdRs4ZImHFfuJCeq9x7sy2eMdWefVlGOyq6eAiBuODiXUXSwm%2F1dw%2Bv3e5fCybWYq%2BxJAkxfwM5%2FSp70UyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMaXnNY5Lh7as5tlMZKtwDpFZ6KAPw6iolrXjK%2F8JrfCNhHxCT0qwiaj8I3d2P5Te2jdVOhvrOOVBLKZCIEUULZeVkmKNLRiyM6wHjDLhRXdfsP2oKDi1NShI95g1ReoQp%2FeNE%2FVKaK16sG2yI%2BS5fR5Rly%2FMVVFp9wDQx8Z6VlUp9d3WVnu3vNVLvDwQyMdjR0C3nKNF0CaU5PPX1udeP%2FFljepE6iJdLunp1HkpHj9do0eAuRjJNiyCSX9dE%2FFM11OPRZUk4EBaiW2UhleOPL%2B2h%2FWv3UhBX0BE7Nl%2FXQbQBRS9Zg%2BEuUfd1iZDxel3Dwda5B1xp55q%2BcNO%2B%2F0CD%2B9ZTOH8D06f4HaBdInDUTzst3%2BHJKlxYTwquHh28aG6q0NhfnNOXIpdm1if1Bzj4lNUYa4KID3ro%2B%2FlgiMlYctWtMItfXLRFKjtgophPCTBo8xIQaXsXc2mnzgKDSzTfjI8YTwz6JJyfvjlCXJB%2F05gXCUh1UENQU7A2g%2FYf%2BE%2B3tAGN3CQeC8ePneje1%2BhwG3DJwAmL7DTtU2Z2MryH1xgIL7eJX1CbIIWJY0sK7goDDGA8%2FjE3juKE1KXJ505311%2Fh3p8rry68efbcwr72ZF4EmRwrEmlJmw7JWcasya0inHb0dWDqI0ZFBR4whbv%2F0gY6pgEesgongaWeRG%2FuKOjYGADpeYieRM5XOgar6DSmQtjgZh0QJy18sql%2FJ60OY8jj2JjN88Tk%2B7BvCGEF12yMqkjchq6f8T2LrbVsdQhn6nku%2FGck4ILVji3fJWO9ChnMzoWsNpxXDqGiH48hplIR%2B%2F91B%2FIEj6eqWnpyQdO6FfcBUb77WuXQX%2F6t8iqrIDcnKTiKPC0pMzyQLckuaxll7CNk0U604Vgn&X-Amz-Signature=49a243f0a322ceb6b3a0a21db24ac97c757a013017c062be64a116a6c0d056ac&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

这一节我们一起来看一下 Swagger2 这样的一个文档API。现在其实对于我们来讲，我们已经是开发完毕两个接口，一个是注册，一个是判断用户名是否存在这两个接口。并且我们其实也通过 Postman 进行了一个测试，这个其实是属于后端开发人员的一个自测。假设现在我们要和前端人员去进行对接，我们必须要提供一份文档，这份文档就是由编写相应接口的开发人员去编写的。假设你现在开发了1万个接口，你就必须要在一个文档里面写上这1万个接口，所需要去传递的一些参数，URL、地址，说明信息等等的内容你都要去写。其实对于程序员来讲，他们其实比较懒，不是很喜欢写文档，所以就应运而生了。这样的一个文档API，这样的一个开源的插件，我们可以来一起看一下。


为了减少程序员编写文档，提高生产力， Swagger2 就应用摇身了。使用 Swagger2，其实我们可以减少编写过多的文档，生产力可以顿时提高很多。你不需要再花费大量的时间去编写文档了，只需要通过一些简单的代码就能够生成 API 文档，并且是在线的，提供给前端人员去对接，是非常的方便的。


随后，既然是一个开源的插件，所以我们就必须要引入这一段相应的依赖，引入到我们的项目里面去。所以把这一段内容直接拷贝一下，贴到我们项目的在肤底 DEV 这里面看一下聚合工程他自己的 pom 里面，我们把刚刚的内容直接给贴过来，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b3e8fdd7-a2b1-43cf-bd71-0ea23455aa6d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TAAJKNXU%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224626Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIEfEPK7JbdRs4ZImHFfuJCeq9x7sy2eMdWefVlGOyq6eAiBuODiXUXSwm%2F1dw%2Bv3e5fCybWYq%2BxJAkxfwM5%2FSp70UyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMaXnNY5Lh7as5tlMZKtwDpFZ6KAPw6iolrXjK%2F8JrfCNhHxCT0qwiaj8I3d2P5Te2jdVOhvrOOVBLKZCIEUULZeVkmKNLRiyM6wHjDLhRXdfsP2oKDi1NShI95g1ReoQp%2FeNE%2FVKaK16sG2yI%2BS5fR5Rly%2FMVVFp9wDQx8Z6VlUp9d3WVnu3vNVLvDwQyMdjR0C3nKNF0CaU5PPX1udeP%2FFljepE6iJdLunp1HkpHj9do0eAuRjJNiyCSX9dE%2FFM11OPRZUk4EBaiW2UhleOPL%2B2h%2FWv3UhBX0BE7Nl%2FXQbQBRS9Zg%2BEuUfd1iZDxel3Dwda5B1xp55q%2BcNO%2B%2F0CD%2B9ZTOH8D06f4HaBdInDUTzst3%2BHJKlxYTwquHh28aG6q0NhfnNOXIpdm1if1Bzj4lNUYa4KID3ro%2B%2FlgiMlYctWtMItfXLRFKjtgophPCTBo8xIQaXsXc2mnzgKDSzTfjI8YTwz6JJyfvjlCXJB%2F05gXCUh1UENQU7A2g%2FYf%2BE%2B3tAGN3CQeC8ePneje1%2BhwG3DJwAmL7DTtU2Z2MryH1xgIL7eJX1CbIIWJY0sK7goDDGA8%2FjE3juKE1KXJ505311%2Fh3p8rry68efbcwr72ZF4EmRwrEmlJmw7JWcasya0inHb0dWDqI0ZFBR4whbv%2F0gY6pgEesgongaWeRG%2FuKOjYGADpeYieRM5XOgar6DSmQtjgZh0QJy18sql%2FJ60OY8jj2JjN88Tk%2B7BvCGEF12yMqkjchq6f8T2LrbVsdQhn6nku%2FGck4ILVji3fJWO9ChnMzoWsNpxXDqGiH48hplIR%2B%2F91B%2FIEj6eqWnpyQdO6FfcBUb77WuXQX%2F6t8iqrIDcnKTiKPC0pMzyQLckuaxll7CNk0U604Vgn&X-Amz-Signature=57bd04a368dc5fd117cba639cfd9bccb5deb826be665373c98cd1d9371c5c4a5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

一起看一下。 import chance 首先第一个是 springfox SEC two，这个是它的核心的内容，核心内容都是在依赖里面。随后下一个是 select UI，它要以一个怎样的形式展现出来，其实它是要生成一些相应的内容的。这两个其实都是由官方所提供的，从它的 group ID 也可以看得出来，都是在 springfox 下面。另外还会有一个额外的，这个是我自己添加的，它非常好用。它是什么？它也是一个 swag UI，只不过是由其他的开发人员所发布的。这两种 UI 我们都会一起来看一下。


的。好依赖引入了以后，我们就需要去编写相应的 API 配置了，怎么去配？我们来看一下，展开我们的 API 这样的一个子工程，把它全部展开。在这里面我们可以去创建一个新的包package，取一个名字叫做config。在这里我们再去创建一个甲板类，取个名字叫做 Swagger2。这个其实就是我们 Swagger2 的一些相应的配置了。首先第一个，我们既然要去使用相应的配置，这个配置是应该要让我们的 spin boot 要让容器去扫拿到的，所以我们应该要在它的上方去加上一个configuration，加上了以后它才会被扫描到。


随后第二个，第二个，我们应该要开启 11 个 to page，也就是 enable step two 把加进来，我们这是两个添加在这个类上方的两个注解。随后下一个我们就应该要去配置它的 swagger to 的核心配置。 swagger to 核心配置，这个核心配置其实称之为是docket，叫做这个东西。我们就来写一下 pubalic docket。在这里是在 springfox，它是一个web，是一个plugins，是插件。好，我们取一个名字叫做 create rest a p i。随后我们在里面我们就要去 return 一个内容，我们这样子return，你有一个docket，这是你有出来的。在这里面我们是需要去指定我们所使用的是哪一种文档的类型，点进去看一下。文档类型有一个叫做 documation document Asian type，点进去看一下。在这边可以看到其实是有 3 种类型，这三种类型分别对应是 swag 一、二。其实不是 swag 12，是 1. 2 这个版本。还有是 swag two，我们所需要去使用的。还有一个就是 spring web，这个是 1. 0 的，我们使用的是 2 点零web，所以我们会使用。在这个地方怎么去写？写上一个 documents documentation，点一个 swagger to 加入进来。在后方我们可以去加上一个注释，这是指定 a p i 类型为 swag to。好，这是第一个，随后第二个，第二个我们来通过点它，其实是一种响应式的编程风格。


点 a p i 音for。这个 API info 是什么？我们可以来写一下。这个是指用于定义 API 文档，汇总信息这些内容，我们再把配置类配置完毕并且运行以后，我们会通过一个网页去进行打开。现在我们在编写代码的时候可能会有一些闷，但是没有关系的，我们跟着步骤一步一步去把代码停进去就可以了，因为这毕竟是一个配置。在这个里面我们要来你有一个东西，你有一个什么，你有一个 API info，其实我们在这边可以额外的再去创建一个新的方法也就可以了。


我们可以点进去看一下 API info 是一个什么东西，在这里它是一个类，再点一下你会发现这个类的里面包含了相应的属性，比方版本号，标题描述，URL，地址，还有是授权的，像一些 license 还有是开发人员的联系方式都有。所以这些信息我们会在这个地方我们再去重新的去创建一个新的方法。

```java
package com.imooc.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import springfox.documentation.builders.ApiInfoBuilder;
import springfox.documentation.builders.PathSelectors;
import springfox.documentation.builders.RequestHandlerSelectors;
import springfox.documentation.service.ApiInfo;
import springfox.documentation.service.Contact;
import springfox.documentation.spi.DocumentationType;
import springfox.documentation.spring.web.plugins.Docket;
import springfox.documentation.swagger2.annotations.EnableSwagger2;

/**
 * <h1></h1>
 */
@SuppressWarnings("all")
@Configuration
@EnableSwagger2
public class Swagger2 {

    // 原路径： http://localhost:8088/swagger-ui.html
    // 优化页面： http://localhost:8088/doc.html
    @Bean
    public Docket cresteApi() {
        return new Docket(DocumentationType.SWAGGER_2) // api类型
                .apiInfo(apiInfo())
                .select()
                .apis(RequestHandlerSelectors.basePackage("com.imooc.controller"))
                .paths(PathSelectors.any())
                .build();
    }

    private ApiInfo apiInfo() {
        return new ApiInfoBuilder()
                .title("天天吃货 电商平台api接口")
                .contact(new Contact("imooc", "https://imooc.com","abc@imooc"))
                .description("转为天天吃货提供的api文档")
                .version("1.0.1")
                .termsOfServiceUrl("https://www.imooc.com")
                .build();
    }

}

/** http://localhost:8088/swagger-ui.html  访问
```

我们在当前类就叫做 private API info，我们会 return 出去 API info，在这里面直接去return。这个我们就可以直接通过 new 一个 API in for new，我们可以使用 API in for 有一个build，使用去构建。这里面我们直接点回车。


第一个是一个title，很明显是文档的标题，注释写在后面，文档页标题。比方我们当前的 API 文档就可以直接去取一个名字了。天天吃货电商平台接口API。最后第二个我们就可以使用一个content，这就是我们的一个联系人，或者称之为是文档的创建人，也可以有一个 contact 使用下面过时了，是直接提供了一个字符串，是谁肯，这样它的内容会比较多。你有一个contact，这里面有name，还有是 email 进他的源码。看一下。


这三个其实就分别对应的是一个开发人员的姓名，你自己的博客的地址或者你网站的地址。另外还有是你的联系的饮料联系方式。在这里面我们直接就把这三项内容传进去就可以了。第一个我们可以比方叫做m。第二个网站地址 h t t p s 冒号斜杠是 3W 点 m . com，这是我们的网站。随后下一个内容比较多，比较长，我们就直接换行，看的可以更加的清晰一些。下一个联系的 email 地址，比方 ABC 艾特 m . com。当然这是一个假的，并没有加上注释，联系人信息。好，下一个。应该是有一个方法叫做比斯科皮。这是详细的描述。写一下专为天天吃货提供的 API 文档。当然这个信息可以写很多，我们就写这一点也就够了。好，OK，加上注释，详细信息。


好，下一个。应该要来写一下我们网站的一些版本号，或者是我们文档的版本号。因为文档会经常去变动，所以版本号你也可以在这里面去写。比方我们初始的为一点零点一版本都行。写一下文档版本号。好。随后再来我们再来一个URL， URL 使用这个其实就是我们网站的一个URL，也就是把木孔网的地址给贴过来写一下，这是网站地址。好，这些基本的信息构建完毕以后，我们直接可以通过点 build 来进行构建。这个构建它就会把一个 API info 给返回出去。返回到哪里？返回到这里，我们在这里去使用就行了。我们在这里只要把这个方法写过来就 OK 了。相应的信息都会放到我们的 DOC 的核心配置里面去就行了。

好，下一个。下一个我们就应该要去配置一下咱们的扫描包所在的地址。什么叫扫描包？也就是我们现有的所有的 Ctrl 的所在的地址。我们的 Ctrl 在哪里？来看一下。目前我们所有的 Ctrl 了都是在这里。我们所需要去生成的那些文档要根据哪些 Ctrl 了来，他们的源头又是在哪个包？都在这个包下面。这下面所有的 Ctrl 了都要为我们所提供相应的接口。所以我们只需要把拷贝一下，把路径直接放到我们的里面去就可以了。


怎么去解？来一个select，我们把放大一些 select 用去选择，也就是它的一个选择器。随后写一个 a p i s a p s，里面可以看到它就是一个 request handler，就是一个选择器。双击一下。 select 是个什么东西？它是一个 request handler selectors，它有一个叫做点 base packages。基础的那些包名你需要在这边是需要去写的。我们只需要把 COM 点 m 点 Ctrl 了写过来就可以了。这个比较长对吧？我们在这里回车一下。在这边我们也进行一个回车，这样子看的可以更加的清楚。扫描啃错了，你要说是指定，我们严谨一些。指定 Ctrl 的包。好，随后下一个。


指定了这个包以后，我们还有一个配置，它会有一个pass。这个 pass 又是什么意思？这个 pass 就是指在这个包下方，我们是要把所有的 controller 了，都是需要去选择的，所以 pass 又有一个叫做 pass selectors。点any，其实就是任何的意思。我们把所有的全部都加进去就可以了。我们在最后通过build，这样子我们的核心配置就已经是构建好了。加上一个注释，所有选错了。好，OK，这个配置配完了以后，千万不要忘记，我们在它的上方是需要去加上一个 bin 的，加上了以后 spring 才知道它是一个病。


好，接下来我们如何去访问我们的文档？其实配置文件内容也并不是很多，我们来看一下。要访问这个文档所在的地址，它其实会提供一个官方的地址，叫做斜杠 swag 杠 UI 点HTML。这样的一个地址，我们写全一点，是 HTTP 冒号斜杠，加上我们的 local host 冒号端口号，假设是8080，现在其实我们是 8088 了。


再来一个后方我们没有上下文的一个项目名，所以我们通过斜杠就可以直接拒绝访问了。这个是原目的，我们可以先把拷贝我们来测试一下。运行之前我们先install，好，已经是可以运行了。打开咱们的浏览器，在浏览器里面，我们把地址贴过来，按一下回车，很明显运行不了，因为我们并没有去启动对吧，所以我们再启动一下。好，启动好了。随后我们刷新一下咱们的页面，这个时候可以发现我们页面是可以访问了。比较明显现在这一段内容。


这一段内容其实就是我们所设置的 API info。我们来看一下在咱们的配置里面，这个部位像title，联系方式，一些详情，还有是版本号， UR 地址等等，全部都在我们浏览器。在我们页面的部分全部都显示的。所以我们在编写配置的时候可能会有一些闷，但是一旦我们的页面展现出来以后，还是比较丰富，页面也是比较好看的。


随后当你去和相应的人员去对接了以后，对方那些开发人员只要根据我们所提供的这些 controller 的就可以去配了。现在其实我们有这么多的 controller 了，这些我们都是可以去提供开放出来的，比方hello。还有我们之前用于去测试 c r u d 的一个 s t u，它的一个 controller l。另外对于我们的一个网站里面真正所使用到的 passport 很重要，都有。比方我们可以来使用一下 user name is exist。可不可以直接点击，点击之后它是会有一个上下滑动的效果。


在这边可以看到它会有一个参数，这个参数就是一个 user name，比方我们来一个m，随后在这边会有一个 try it out，点击一下你会发现接口是调用成功的，用户名已经存在。也就是我们其实也能通过咱们的文档来实现。咱们的一个自测功能也是没有问题的。这也是一石二鸟，一举两得，也是非常方便的。好。这个是他的一个官方自带的皮肤，我们来做一个换肤。换肤其实也是我们之前在依赖里面所提到的，它是使用了bootstrap，也就是前端的一个 CSS 框架。它要去访问的时候，它所在的地址路径在哪里，我们把也写一下。敲甲，这个地址其实跟这个是有一定的区别的。在这里原来是 swag 杠，如 i 对吧。它比较简单简洁，它是一个Doc，点 HTML 就可以了。


随后我们在我们来修改一下，我们把改为g、 o c，其实就是 document 的简写。回车一下，你会发现这个时候我们的页面其实风格发生了一个变化，它分为了左右左半部分，其实就相当于是一个导航，右半部分就是我们的一个信息。针对于我们的文档信息，其实就是我们的一个首页。 API info 都在这里进行了一个展示，其实也是非常的不错的。像 hello controller 了， passport controller 等等相应的内容，相应的 controller 了，全部都在这里有了相应的展示了。


大家在运行完毕以后可以去测试一下它的效果。其实和它原先的一个皮肤来比，我个人倾向于使用这样的皮肤，更加符合我们的使用习惯。如果相应的接口比较多，全部会在左侧进行列出的测试。其实也是一样，比方我们就拿刚刚的一个接口，在我们使用 m 可来进行测试，点击发送，随后下方会有一个响应的内容，在这里全部都有一定的展示。OK，现在其实我们就整合 strike two 就已经是成功了。






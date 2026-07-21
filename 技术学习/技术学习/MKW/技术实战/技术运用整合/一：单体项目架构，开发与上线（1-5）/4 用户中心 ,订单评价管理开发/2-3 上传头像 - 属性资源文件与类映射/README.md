---
title: 2-3 上传头像 - 属性资源文件与类映射
---

# 2-3 上传头像 - 属性资源文件与类映射

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/4ea00edf-c89e-4f23-aa38-73967646bbf3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662LU2I6AV%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224725Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDPp6VBqIbaROIp%2BGOVE7Pj7G4c9Ed77QmcDCS2qJxIigIgU50PKGtQHFj6k9BcEaork8yIcTFCrHDuxJS7aDShPJAqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNRydjt1s3%2BTcIqjCSrcA%2FMbwbgp7gjfuWIBbk8ot7u2E2XkPehAbPHVx1zR6rX7rA9OIzMbMZo%2BEeNOIYdqVVL%2B9Eqiv4HS5gIrCl8D9C2PAfP4ujX6CuDB6T6b3a79tOun7lQnvD7mKxp5BmaRi6CKb%2BP%2Fa3OcTt7l1ej9M2sICjnlZqL0labJfyfT990C241%2FTXgbDIMtNQyhb8NZwZ1%2F04Y4Z%2BuVDxj3VgNvl1PumQl%2FyKigu%2FYBKXU9rkDK5C88HKZ0%2BD3HGjhynybbx3xlcXFHAa4eXTV2Hv2jY9aHGeyyI6Y9dZzir32iBj0MMtEtjQcV%2FXRsEsThUSK4WCYrfqiIQ0oGvMnXBJpAZaiKd2xQycIeu%2Fpd2ZQ%2BLg6NSpvOwgQqt2VSAFuRq%2Bz0jSX2UCCfo9GrrQYsHXA8ITIwPxDBo93JAECeHIV9hwQuO51dqQc68VluTtPa1d82NoagApgkEytIrqYzKDcwxkw0ASo1%2BxgrlgSwHwEvpkVeZ3gTIBPAQJmPGT0OX0la2ZlzE6RnSaCAf2fs6dG0ODAoGcApO0GOQZsq7BNB9h1NOFCz8ONBjJIq%2BZaeBoJjvR0LmOxLce6zdBk0H1kT2LBqo7zxT%2F0qCYmcZKBqwTIA0W5a6Sls1TbklFPDMKG6%2F9IGOqUB3I37xKwH1W5FKwyqa8cWHYrjTllmgohYtdLEIBddjzQ4KC1j1aqqpiIfic1%2BbUDo9ee7NMmSlPm1Nk2X571R1NC6AMv3wbFo2%2Bv7Vb1ycvrQYr3jauf5hMKdm%2BQz%2Bmk1LGjcorxCApvDRXfFbI3LPj1zgwew6agNT62xVG0FcRB%2BUZ429QVcLRHTxFj8KtabhmmZkOp0qL6KBQXNDesRnRbNRdO%2B&X-Amz-Signature=e1826f6462206ea36d0b09ff9218aabca03b11d05e76a7118907fa557c8b045d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

上一节我们已经是完成了头上的上传，已经是上传成功了。这一节我们来看一下。有一个地方我们是需要去进行一个穴位的优化，也就是我们定义的一个头像保存的地址，也就是在目录之下。目录配置我们是写在了 base Ctrl 里面，只要去继承它，我们就可以去进行使用。但是路径写在这里会有一个小问题。在我们以后，如果我们会有测试环境，预发布环境以及是生产环境的时候，在这里其实我们会把写成 4 份，只有一份是打开的，其他 4 份都是注释掉的。当然这仅仅只是一个属性的配置，如果我们会有多个，我们一旦切换环境，就会来回的去进行一个注释，这样子显然并不是很好，有没有一种更好的方式来替代？这种方式其实是有的，在我们的支付中心里面，其实我们的一些配置使用的这种方式，也就是通过一些资源文件的配置来去实现的。


好，这一节我们就来写一下。在我们的位置，在 resource 的里面，我们可以来创建一个文件，你有一个 file 文件，取一个名字，在这里就叫做 file upload。再来一个杠 d v 点practice，好POP，注意不要拼错。

[file](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/f03e6dd3-147c-4377-a01e-c8b409772036/file-upload-dev.properties?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662LU2I6AV%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224725Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDPp6VBqIbaROIp%2BGOVE7Pj7G4c9Ed77QmcDCS2qJxIigIgU50PKGtQHFj6k9BcEaork8yIcTFCrHDuxJS7aDShPJAqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNRydjt1s3%2BTcIqjCSrcA%2FMbwbgp7gjfuWIBbk8ot7u2E2XkPehAbPHVx1zR6rX7rA9OIzMbMZo%2BEeNOIYdqVVL%2B9Eqiv4HS5gIrCl8D9C2PAfP4ujX6CuDB6T6b3a79tOun7lQnvD7mKxp5BmaRi6CKb%2BP%2Fa3OcTt7l1ej9M2sICjnlZqL0labJfyfT990C241%2FTXgbDIMtNQyhb8NZwZ1%2F04Y4Z%2BuVDxj3VgNvl1PumQl%2FyKigu%2FYBKXU9rkDK5C88HKZ0%2BD3HGjhynybbx3xlcXFHAa4eXTV2Hv2jY9aHGeyyI6Y9dZzir32iBj0MMtEtjQcV%2FXRsEsThUSK4WCYrfqiIQ0oGvMnXBJpAZaiKd2xQycIeu%2Fpd2ZQ%2BLg6NSpvOwgQqt2VSAFuRq%2Bz0jSX2UCCfo9GrrQYsHXA8ITIwPxDBo93JAECeHIV9hwQuO51dqQc68VluTtPa1d82NoagApgkEytIrqYzKDcwxkw0ASo1%2BxgrlgSwHwEvpkVeZ3gTIBPAQJmPGT0OX0la2ZlzE6RnSaCAf2fs6dG0ODAoGcApO0GOQZsq7BNB9h1NOFCz8ONBjJIq%2BZaeBoJjvR0LmOxLce6zdBk0H1kT2LBqo7zxT%2F0qCYmcZKBqwTIA0W5a6Sls1TbklFPDMKG6%2F9IGOqUB3I37xKwH1W5FKwyqa8cWHYrjTllmgohYtdLEIBddjzQ4KC1j1aqqpiIfic1%2BbUDo9ee7NMmSlPm1Nk2X571R1NC6AMv3wbFo2%2Bv7Vb1ycvrQYr3jauf5hMKdm%2BQz%2Bmk1LGjcorxCApvDRXfFbI3LPj1zgwew6agNT62xVG0FcRB%2BUZ429QVcLRHTxFj8KtabhmmZkOp0qL6KBQXNDesRnRbNRdO%2B&X-Amz-Signature=6ce024202b59eca871eb6da4cdde68ac1eca28dcac4d85059120a03b1f03b73c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[file](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/716c15e7-018b-4131-a94c-3272d8656835/file-upload-prod.properties?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662LU2I6AV%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224725Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDPp6VBqIbaROIp%2BGOVE7Pj7G4c9Ed77QmcDCS2qJxIigIgU50PKGtQHFj6k9BcEaork8yIcTFCrHDuxJS7aDShPJAqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNRydjt1s3%2BTcIqjCSrcA%2FMbwbgp7gjfuWIBbk8ot7u2E2XkPehAbPHVx1zR6rX7rA9OIzMbMZo%2BEeNOIYdqVVL%2B9Eqiv4HS5gIrCl8D9C2PAfP4ujX6CuDB6T6b3a79tOun7lQnvD7mKxp5BmaRi6CKb%2BP%2Fa3OcTt7l1ej9M2sICjnlZqL0labJfyfT990C241%2FTXgbDIMtNQyhb8NZwZ1%2F04Y4Z%2BuVDxj3VgNvl1PumQl%2FyKigu%2FYBKXU9rkDK5C88HKZ0%2BD3HGjhynybbx3xlcXFHAa4eXTV2Hv2jY9aHGeyyI6Y9dZzir32iBj0MMtEtjQcV%2FXRsEsThUSK4WCYrfqiIQ0oGvMnXBJpAZaiKd2xQycIeu%2Fpd2ZQ%2BLg6NSpvOwgQqt2VSAFuRq%2Bz0jSX2UCCfo9GrrQYsHXA8ITIwPxDBo93JAECeHIV9hwQuO51dqQc68VluTtPa1d82NoagApgkEytIrqYzKDcwxkw0ASo1%2BxgrlgSwHwEvpkVeZ3gTIBPAQJmPGT0OX0la2ZlzE6RnSaCAf2fs6dG0ODAoGcApO0GOQZsq7BNB9h1NOFCz8ONBjJIq%2BZaeBoJjvR0LmOxLce6zdBk0H1kT2LBqo7zxT%2F0qCYmcZKBqwTIA0W5a6Sls1TbklFPDMKG6%2F9IGOqUB3I37xKwH1W5FKwyqa8cWHYrjTllmgohYtdLEIBddjzQ4KC1j1aqqpiIfic1%2BbUDo9ee7NMmSlPm1Nk2X571R1NC6AMv3wbFo2%2Bv7Vb1ycvrQYr3jauf5hMKdm%2BQz%2Bmk1LGjcorxCApvDRXfFbI3LPj1zgwew6agNT62xVG0FcRB%2BUZ429QVcLRHTxFj8KtabhmmZkOp0qL6KBQXNDesRnRbNRdO%2B&X-Amz-Signature=c275acd647fbb6e9e5c68f113bedb11ae7dc296318ab0323fce816ac9a1329f4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


在这里面我们就可以去把一些相应的资源的属性都可以写到这里面去。写到这里面去了之后，我们只需要在调用的时候从这里面去取就可以了，非常的方便，而且也是非常的直观。因为我们的一些文件直接都是写在 resource 下方的，我们不要把一些什么测试生产开发环境的一些参数配置到我们 man 夹把包里面去，尽量的放到我们的 resource 里面，这样子其实是会更好，也是更加直观。


在这里面我们就可以去定义了，比方我们可以来定一个叫做 file 点，后方其实是前缀，后方是它的一个属性的名称，属性的名称我们就可以以这个为例。把拷贝过来，我们就可以把它叫做是 image user face location，叫做一个地址后方。后方我们要写上一个等于号，而不是一个冒号。写了一个等于号了以后，你要把具体的值写进去。


在这里我们现在具体的值其实是这一段内容，这一段内容其实它是一个 Java 代码，因为我们会使用到 file 点separate，这个东西在我们的资源文件里面是不能够去使用的，所以现在我们要去使用，我们还是只能方式使用这种方式来替代。写到这个位置，这样子就 OK 了。所以大家如果要使用 properties 的时候，涉及到路径一定要去注意。我现在使用的是一个正斜杠，如果是 windows 系统，要在这里把它改为两个反斜杠，也一定要注意，因为不同的操作系统它的斜杠是不一样的。所以这就是我们使用甲板币和使用资源文件定义的两种不同的方式，要去注意一下它们的区别。


在这里这一段代码其实我就不去注释了，我就放着在这边。其实我们当前文件我们就已经是写好了，我们再来把文件，我们可以再来拷贝一份拷贝一下。在这边我们可以定义为叫做 prod，其实就是 product，代表是生产环境的意思。当然你也可以再加一个test，就是代表测试环境。这样子。其实我们两份文件里面的内容目前都是一模一样。在这里文件我们先暂时的把这一块内容删除留空。我们只使用 DV 文件。好，有了属性资源文件了以后，我们是需要去使用这里面的 d 的目录值如何去使用？我们在包里面我们可以再去创建一个比方，我们在这边我们再去额外的去创建一个叫做 resource 的包，创建一个resource，这个 resource 在这里我们可以在我们去创建一个类，创建一个 java 类，这个夹巴类的名称就叫做FileUpload。这个 dev 我们就不需要了，直接取名叫 fileupload。在这里面就有了这样的一个类。

```java
package com.imooc.resource;

import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.context.annotation.PropertySource;
import org.springframework.stereotype.Component;

/**
 * <h1>文件上传优化，不要直接定义在BasController中了， 不同的环境有不同的未见存放地址，所以需要动态的</h1>
 *
 * 文件放在classpath下面，使用@PropertySource注解来取值（文件存放位置）
 */
@SuppressWarnings("all")
@Component
@ConfigurationProperties(prefix = "file")  // 获取文件中的内容的定义名称的前缀
@PropertySource("classpath:file-upload-dev.properties") // 获取文件
public class FileUpload {

    private String imageUserFaceLocation;

    private String imageServerUrl; // 图片存放在服务中地址

    public String getImageServerUrl() {
        return imageServerUrl;
    }

    public void setImageServerUrl(String imageServerUrl) {
        this.imageServerUrl = imageServerUrl;
    }

    public String getImageUserFaceLocation() {
        return imageUserFaceLocation;
    }

    public void setImageUserFaceLocation(String imageUserFaceLocation) {
        this.imageUserFaceLocation = imageUserFaceLocation;
    }
}
```

这个类其实我们要和资源文件要进行一个关联。如何去进行一个关联？首先我们先来写一下，写有一个叫做 property source，这个意思是指我们的一个属性咨询文件所在的一个地址在哪里。现在我们其实是把文件放在了 resources 下方，一旦我们在项目打包了以后，其实这里面的所有的文件都是在我们的 class pass 下方。所以在这里我们就直接可以去写一个 class pass，加上一个冒号，代表他所在的一个地址，在这里你只需要去把文件名去拷贝一下，直接把肯德西拷贝，拷贝了以后贴过来，贴到这个位置。它的一个 source 地址配置好了。


配置好了以后，在这里你还需要去配置它的一个前缀。它的前缀其实我们从文件里面，从它的这里面就能够看得出来，它会有一个 file 点，这个 file 点就是它的一个前缀。或者你可以来一个 file 点， face 也可以作为它的一个前缀，都是没问题。因为它的一个真实的属性是下方的，这一个内容才是我们要去定义的一个内容。我们可以在内部去使用，比方我们来一个string， private string。把这个属性名称贴过来以后，你再去生成一下它的 get 和 set 方法，这样子就生成了。好，所以你要在这个地方去加上它的前缀。它的前缀我们是需要配置一个叫做 config 瑞幸practice，也就是属性资源文件的一个配置。在这里面它会有一个叫做 prefix ，它默认是为空的。在这边我们直接把 file 给加进去，贴过来， file 就会作为属性的一个前缀了。


好，我们在这里还是需要去再加上一个component。加上一个component，因为它会作为一个组件，让我们的 spring mode 容器去进行一个扫描，扫描到了以后，这个文件你才可以去使用。现在我们就已经是定义好了。随后我们应该要去使用一下如何去使用。我们把这个类直接拿到我们的 Ctrl 里面，在这边做一个注入就可以了。 private 把这个类拿过来，上方加上一个 all to wide，好 fireupload 就可以去使用了。在这边我们把这行代码我就注释掉，我不去删除。通过 file upload 点 get 就可以获得目录的一个属性值了。所以在前面我们再做一个赋值。这样子 file space 等于 file upload。


Can get image user face location.

这样子也可以去获取的。随后我们再来重新的去启动一下，我们 install 一下。还是如果所写的代码量比较多，还是建议去 install 一下，这是一个比较好的习惯。好，我们再来一个重启。好，重启成功。我们回到页面，刷新一下，选择某一张图片。当前我们选择刚刚选择的是，现在选择 face to。点击打开好头像，上传成功了。我们到目录里面去看一下。可以看到这张图片就已经是上传成功了。只不过我们在之前也说了，我们是一个覆盖式的一种形式，你加了一个时间，它就是一个增量式的。好，这一节就是我们所讲的一个使用的这种资源文件的方式，映射到我们的一个 Java 类里面去，这样子就可以实现我们的一些属性的公用化。如果以后要做发布，我们只要在这个位置把 DV 改成一个 Pro d product，其实就OK。



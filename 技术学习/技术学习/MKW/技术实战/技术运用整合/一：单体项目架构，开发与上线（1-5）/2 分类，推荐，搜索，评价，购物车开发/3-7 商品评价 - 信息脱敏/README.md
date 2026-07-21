---
title: 3-7 商品评价 - 信息脱敏
---

# 3-7 商品评价 - 信息脱敏

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/5802bf3d-eca7-48ba-9541-1b3e2ffd9dd2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665UGHB6EG%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224647Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDlEgfenuTFR2MMLe%2BEB3ZanaimvJKnCv9woAnrLzYkvgIgNqULGiqM59g00aJHJdOBaPCCU8YunvZlwbb4xbJszaMqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEwkk2PCUkMP%2BpHHRyrcA84k0rSZGGojhsIGhnCk5fScCNuRdG%2BbWBxjIuqo9QAhFzixsZjFjOSXVqmXnh%2FDm9rGViAc2A%2BG0pMEUCylVrFqnDG5MHkGrx5LvMgUlyKyKHFSOVnqtTvyrtUXe7dtRa3KuUJuPQw64997VJ8mPTonkHmD61VEohjjOUBF7ypV1YzeikU0aTEQcNot0VtHKuCUHtJ%2FY0qsEVPaFVU441%2Fs3Ec5xsko23%2Bvk7g1Xn25stTtknu32q0w%2FxymU2nbaRdQka%2FqemO5WJGQZpEcbwbb3P%2BdD7ajaUn6wzIoO992bsso%2FzLAKM8dAzInsgGaR7B20%2FdWvrqHz6wG0CXt9RiOPrX9%2FJUHaiNGRp753WjnvOKxG1wpXVIUk6306YNh45L8i5Bb9fLe3TakZ7szZ9eu%2Fdm12cWsBdcqn2tpS8LEoouQfV0qhuoxN8yppaP3Svqu4%2BigMi23chAId%2FCvzUlzzTyxcjtpNO0U%2Fjbz0xjcpQQhiOrN%2BLPVfguJGkCNAJ1rnL2CXsIyPPYXGjxYQg0TsDARCxGwcsQp2ilVnkhtGVoByrDP%2BOToIZ%2BIN4rHj8BIz%2FE9N4UaOU8xWClxLZ9F8dFFC6fRPMHH4mufWOx41FVudTFbeS6R%2FmSLMJu6%2F9IGOqUBah8lKp3%2BP52t%2BOB5srN7PcTI8aAu4u%2Fo3c7lMmTIAWzgjItYq4SA1pQCoewziCD%2BQ3XJgVY3T3m0dSxD5LC00djH05fD8s8FX1Gt1pfBZFHWqFeaeADR8Krjuel84N0VPKB%2BPQ2MSYyEnjCQScgr5Odha2rcP4%2Fv3SBs4JC5EjWBfztdFT4ak7R8SQDR%2FMCO8ioZ178VCz8rDxaloI3v0smd767q&X-Amz-Signature=7ef37fe50e558668473860b47ae39b1bf98ef8a975d5302c0e8f6727ce97cc12&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

前面几节我们是把商品的评价进行了一个开发，现在联调也已经是成功了，并且我们也是带上了分页功能，也是没有问题。接下来我们先来看一下头像以及是他的用户名，在这里我们没有展示，这主要是咱们的数据库的一个问题。之前评论这张表以及是用户表其实并没有对应，我们只需要去做一个修改就可以了。在这里面这些数据其实都是从生产上我全部都拿过来的，我把拷贝一下，把本地找 m 可把用户的 ID 覆盖掉，打个勾。现在我们再可以到页面里面去刷新一下，刷新可以看到用户的头像和昵称现在都已经是有了，有一个小的问题我们要去解决一下。


之前我们在讲这个需求的时候，其实我们的用户的昵称我们是应该要做一个脱敏的，可以看到用户在这里会有很多的心，用心来替代。其实我们也是为大家提供了一个脱敏的工具类，我们是可以去实现一个脱敏的。我们来看一下。在项目里面，其实我们也预先为大家准备了这样的一个脱敏的工具类，叫做 d c n c t zation，有跳双击。打开一下来看一下。这个工具类就是通用的脱敏工具类，它可以是用于像用户名，手机号，邮箱地址等等你都可以去使用。在这边是定义了两个值，一个是size，一个是星号。星号就是你自己要去使用的一个符号，你可以去替换掉的，你使用比方像常用的星号，井号都可以，另外 size 是6，也就是最长是6。我们可以先来测试一下比方，在这里我提写了一个像姓名，是手机号，还有是邮箱和住址都可以。右键先来运行一下。可以看到在这里相应的内容都已经是打印出来。如果你的姓名比较短，它中间它会用一个心去进行代替的。如果你的一个值，你的字符串比较长，它最长就只有是 6 位6。在我们刚刚在这里所提到的size，你可以自己去替换，你要长一些，你使用 8 也没有问题。这个就是一个脱敏，把一些敏感信息使用一些特殊的字符串去进行一个隐藏去替换掉。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/4287093e-f710-4120-89b1-9951c3e12aa3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665UGHB6EG%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224647Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDlEgfenuTFR2MMLe%2BEB3ZanaimvJKnCv9woAnrLzYkvgIgNqULGiqM59g00aJHJdOBaPCCU8YunvZlwbb4xbJszaMqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEwkk2PCUkMP%2BpHHRyrcA84k0rSZGGojhsIGhnCk5fScCNuRdG%2BbWBxjIuqo9QAhFzixsZjFjOSXVqmXnh%2FDm9rGViAc2A%2BG0pMEUCylVrFqnDG5MHkGrx5LvMgUlyKyKHFSOVnqtTvyrtUXe7dtRa3KuUJuPQw64997VJ8mPTonkHmD61VEohjjOUBF7ypV1YzeikU0aTEQcNot0VtHKuCUHtJ%2FY0qsEVPaFVU441%2Fs3Ec5xsko23%2Bvk7g1Xn25stTtknu32q0w%2FxymU2nbaRdQka%2FqemO5WJGQZpEcbwbb3P%2BdD7ajaUn6wzIoO992bsso%2FzLAKM8dAzInsgGaR7B20%2FdWvrqHz6wG0CXt9RiOPrX9%2FJUHaiNGRp753WjnvOKxG1wpXVIUk6306YNh45L8i5Bb9fLe3TakZ7szZ9eu%2Fdm12cWsBdcqn2tpS8LEoouQfV0qhuoxN8yppaP3Svqu4%2BigMi23chAId%2FCvzUlzzTyxcjtpNO0U%2Fjbz0xjcpQQhiOrN%2BLPVfguJGkCNAJ1rnL2CXsIyPPYXGjxYQg0TsDARCxGwcsQp2ilVnkhtGVoByrDP%2BOToIZ%2BIN4rHj8BIz%2FE9N4UaOU8xWClxLZ9F8dFFC6fRPMHH4mufWOx41FVudTFbeS6R%2FmSLMJu6%2F9IGOqUBah8lKp3%2BP52t%2BOB5srN7PcTI8aAu4u%2Fo3c7lMmTIAWzgjItYq4SA1pQCoewziCD%2BQ3XJgVY3T3m0dSxD5LC00djH05fD8s8FX1Gt1pfBZFHWqFeaeADR8Krjuel84N0VPKB%2BPQ2MSYyEnjCQScgr5Odha2rcP4%2Fv3SBs4JC5EjWBfztdFT4ak7R8SQDR%2FMCO8ioZ178VCz8rDxaloI3v0smd767q&X-Amz-Signature=350de945586d84ea67a526eba38bb6214a45b35dbef62d41639d2dca4a9dd582&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


在我们代码里面，我们也可以这样子去做，把这个类拷贝一下，找到我们刚刚的service，这个 service 是在这里，这是我们查询的评论，其中有一个用户的昵称。在这里我们可以来一个 for 循环。负循环我们是循环的list，所以我们在写一下。在这边我们来一个，就叫做feel。好。这个其实也是一个 for 循环，我们可以不需要再去定义一个变量 i 的，也是可以去使用的。来一个VO， VO 就是 list 里面每一个循环时候所拿到的一个元素。一个item。好通过 v o 点 set 来一个user，它是一个nickname。在里面我们就可以使用这个了。使用脱敏的工具类，先把包引入进来，点它有一个 common display，也就是通用的一个使用方式，再把 FIO 点 get Nick name 给拿出来。也是拿出来以后进行脱敏，再重新的进行一个set。这个步骤就可以实现脱敏。我们来 install 一下。好， install 成功。再重启。


服务器，是被刚刚的类给替换掉了，我们在这里运行一下咱们的启动类就可以了。好，运行成功。现在我们可以来刷新一下。刷新页面。刷新页面以后再来看一下咱们的评价。这个时候就可以看到我们的m，可其实中间的一些字符串就已经是被脱敏了。OK，这个就是我们脱敏的工具类的使用。

```java
package com.imooc.utils;

/**
 * 通用脱敏工具类
 * 可用于：
 *      用户名
 *      手机号
 *      邮箱
 *      地址等
 */
public class DesensitizationUtil {

    private static final int SIZE = 6;
    private static final String SYMBOL = "*";

    public static void main(String[] args) {
        String name = commonDisplay("慕课网");
        String mobile = commonDisplay("13900000000");
        String mail = commonDisplay("admin@imooc.com");
        String address = commonDisplay("北京大运河东路888号");

        System.out.println(name);
        System.out.println(mobile);
        System.out.println(mail);
        System.out.println(address);
    }

    /**
     * 通用脱敏方法
     * @param value
     * @return
     */
    public static String commonDisplay(String value) {
        if (null == value || "".equals(value)) {
            return value;
        }
        int len = value.length();
        int pamaone = len / 2;
        int pamatwo = pamaone - 1;
        int pamathree = len % 2;
        StringBuilder stringBuilder = new StringBuilder();
        if (len <= 2) {
            if (pamathree == 1) {
                return SYMBOL;
            }
            stringBuilder.append(SYMBOL);
            stringBuilder.append(value.charAt(len - 1));
        } else {
            if (pamatwo <= 0) {
                stringBuilder.append(value.substring(0, 1));
                stringBuilder.append(SYMBOL);
                stringBuilder.append(value.substring(len - 1, len));

            } else if (pamatwo >= SIZE / 2 && SIZE + 1 != len) {
                int pamafive = (len - SIZE) / 2;
                stringBuilder.append(value.substring(0, pamafive));
                for (int i = 0; i < SIZE; i++) {
                    stringBuilder.append(SYMBOL);
                }
                if ((pamathree == 0 && SIZE / 2 == 0) || (pamathree != 0 && SIZE % 2 != 0)) {
                    stringBuilder.append(value.substring(len - pamafive, len));
                } else {
                    stringBuilder.append(value.substring(len - (pamafive + 1), len));
                }
            } else {
                int pamafour = len - 2;
                stringBuilder.append(value.substring(0, 1));
                for (int i = 0; i < pamafour; i++) {
                    stringBuilder.append(SYMBOL);
                }
                stringBuilder.append(value.substring(len - 1, len));
            }
        }
        return stringBuilder.toString();
    }

}
```






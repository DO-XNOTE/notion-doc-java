---
title: 2-11 Sentinel整合Apollo sentinel-dashboard扩展实现-2
---

# 2-11 Sentinel整合Apollo sentinel-dashboard扩展实现-2

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b086668b-30b1-47c9-8d5d-62f7b242eb48/SCR-20240723-dcit.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XTSUWJTB%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225847Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCiEcX%2BWw0CYm7csq33pKuZcgLde9Ajn5HT5SYK1d5IowIgC6TvnCYWZstfkhz1eq50r2Hhp85mTR0t%2BPO9aRm58bwqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFS1hr7OQEezACsbnSrcA2DVeqTUFXKKB9l%2BXYKu3FXCadXWD%2BuReO8Af3RaZACm13AVppKqv6kIuvbDWz6iQYnKgoLHXgBo9I0ee4aRFMH2z%2F8gbSiHh3LG1mVAN3aukNqI1LiPoJdMvGjEEjRtevaliUtXw7v98v3dTZKYowN4%2BU0opWnqxNipD97j0tPTwQwxG7GzDKoP%2FCtheoTNsBv70QUNj9FWbl4Ktw7K0F5XPaufQmtIJuCCWBC7JbK6Vr7WCwHr2jL6XpTTBrlKN%2BX8oKKTNAC265%2FJY2hIOAg8UsgsZ5iYtmkN2aUkxVvn%2FGKjx3OAy%2B4Ojh3OutOzLGv%2B6ZjdC1%2Ff0oeP5x0PJVGOl3KTlObPgtregppd8vyyhg8NB6WpyVtnZGIDQT2XlinxC2YlKPPktnWB3jitA8gCxjUnmm5XKQhPWZm7wzHGDwYkX3odR7VRR%2BXQifmw3DzLqeLA48xXh%2BKxsmWSYv%2F8Fs%2Bn%2FCFwQepGbZ0dbM8vuWSwOZAaGX5h6UwGDZKewL1M9vIQUCe48XzmfJXzIjOvZMXOfzhbz4iV1lOW%2BCWo8GIzhmgpYVKMC6z7Q4kFFgp4gGpgHfMnDuHbZNHt3rdigdcFNOqM7flXmzfEOYcq8JKZYEwnNUHpIiJ8MLW3%2F9IGOqUBXh47CuTGQyqYJW2wI8eotYzNIL9zTPiE8a52GjY5kVnDsIybh%2Bw63xZe8NggdUdAZrRk23E%2FeVALIv2CzD6Nw8xLguiSf31E1Xsu60P%2BBsOZkY1RPVjw1a%2FiajuMVJ91Js%2BBKlLBLYJuZmS2IXx39Isu9JyrEgnFC%2FbmCp3OHng3HsjsL0Kl%2BGLdFC1vXPuH%2FKVlaji6v1roUiRzUpUdKu8YUBA4&X-Amz-Signature=7321449bab1c1d123f9ac294bf61806db07190ff9775c28e6a3f6cc34195a3bc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/feccc4c5-dd93-40ee-962c-5182f966e863/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XTSUWJTB%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225847Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCiEcX%2BWw0CYm7csq33pKuZcgLde9Ajn5HT5SYK1d5IowIgC6TvnCYWZstfkhz1eq50r2Hhp85mTR0t%2BPO9aRm58bwqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFS1hr7OQEezACsbnSrcA2DVeqTUFXKKB9l%2BXYKu3FXCadXWD%2BuReO8Af3RaZACm13AVppKqv6kIuvbDWz6iQYnKgoLHXgBo9I0ee4aRFMH2z%2F8gbSiHh3LG1mVAN3aukNqI1LiPoJdMvGjEEjRtevaliUtXw7v98v3dTZKYowN4%2BU0opWnqxNipD97j0tPTwQwxG7GzDKoP%2FCtheoTNsBv70QUNj9FWbl4Ktw7K0F5XPaufQmtIJuCCWBC7JbK6Vr7WCwHr2jL6XpTTBrlKN%2BX8oKKTNAC265%2FJY2hIOAg8UsgsZ5iYtmkN2aUkxVvn%2FGKjx3OAy%2B4Ojh3OutOzLGv%2B6ZjdC1%2Ff0oeP5x0PJVGOl3KTlObPgtregppd8vyyhg8NB6WpyVtnZGIDQT2XlinxC2YlKPPktnWB3jitA8gCxjUnmm5XKQhPWZm7wzHGDwYkX3odR7VRR%2BXQifmw3DzLqeLA48xXh%2BKxsmWSYv%2F8Fs%2Bn%2FCFwQepGbZ0dbM8vuWSwOZAaGX5h6UwGDZKewL1M9vIQUCe48XzmfJXzIjOvZMXOfzhbz4iV1lOW%2BCWo8GIzhmgpYVKMC6z7Q4kFFgp4gGpgHfMnDuHbZNHt3rdigdcFNOqM7flXmzfEOYcq8JKZYEwnNUHpIiJ8MLW3%2F9IGOqUBXh47CuTGQyqYJW2wI8eotYzNIL9zTPiE8a52GjY5kVnDsIybh%2Bw63xZe8NggdUdAZrRk23E%2FeVALIv2CzD6Nw8xLguiSf31E1Xsu60P%2BBsOZkY1RPVjw1a%2FiajuMVJ91Js%2BBKlLBLYJuZmS2IXx39Isu9JyrEgnFC%2FbmCp3OHng3HsjsL0Kl%2BGLdFC1vXPuH%2FKVlaji6v1roUiRzUpUdKu8YUBA4&X-Amz-Signature=72f7855245457d0e1493989364c3d6ecd07b7f9cf65440133cd52312bdac7ba6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/fcbcdfa8-839f-4f55-a615-30960ae689d8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XTSUWJTB%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225847Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCiEcX%2BWw0CYm7csq33pKuZcgLde9Ajn5HT5SYK1d5IowIgC6TvnCYWZstfkhz1eq50r2Hhp85mTR0t%2BPO9aRm58bwqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFS1hr7OQEezACsbnSrcA2DVeqTUFXKKB9l%2BXYKu3FXCadXWD%2BuReO8Af3RaZACm13AVppKqv6kIuvbDWz6iQYnKgoLHXgBo9I0ee4aRFMH2z%2F8gbSiHh3LG1mVAN3aukNqI1LiPoJdMvGjEEjRtevaliUtXw7v98v3dTZKYowN4%2BU0opWnqxNipD97j0tPTwQwxG7GzDKoP%2FCtheoTNsBv70QUNj9FWbl4Ktw7K0F5XPaufQmtIJuCCWBC7JbK6Vr7WCwHr2jL6XpTTBrlKN%2BX8oKKTNAC265%2FJY2hIOAg8UsgsZ5iYtmkN2aUkxVvn%2FGKjx3OAy%2B4Ojh3OutOzLGv%2B6ZjdC1%2Ff0oeP5x0PJVGOl3KTlObPgtregppd8vyyhg8NB6WpyVtnZGIDQT2XlinxC2YlKPPktnWB3jitA8gCxjUnmm5XKQhPWZm7wzHGDwYkX3odR7VRR%2BXQifmw3DzLqeLA48xXh%2BKxsmWSYv%2F8Fs%2Bn%2FCFwQepGbZ0dbM8vuWSwOZAaGX5h6UwGDZKewL1M9vIQUCe48XzmfJXzIjOvZMXOfzhbz4iV1lOW%2BCWo8GIzhmgpYVKMC6z7Q4kFFgp4gGpgHfMnDuHbZNHt3rdigdcFNOqM7flXmzfEOYcq8JKZYEwnNUHpIiJ8MLW3%2F9IGOqUBXh47CuTGQyqYJW2wI8eotYzNIL9zTPiE8a52GjY5kVnDsIybh%2Bw63xZe8NggdUdAZrRk23E%2FeVALIv2CzD6Nw8xLguiSf31E1Xsu60P%2BBsOZkY1RPVjw1a%2FiajuMVJ91Js%2BBKlLBLYJuZmS2IXx39Isu9JyrEgnFC%2FbmCp3OHng3HsjsL0Kl%2BGLdFC1vXPuH%2FKVlaji6v1roUiRzUpUdKu8YUBA4&X-Amz-Signature=c3b999f0efbed8d22c960bf105f08dc44bc7c10048e676f0cc86d44a63dfc2ff&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

创建一个新的类叫做 follow ruler 还是阿波罗的什么？ publish 对不对？好搞定。那这个 publish 我们怎么去用呢？很简单，也是你要实现一个接口，那个接口叫做什么呢？叫做 implements dynamic 现在我们要做的是 publisher 然后它的接口里面也是一样的。对还是要存储一个 list 然后里边叫做 follow ruler entity 我们要一个 list 是 Java uter 的 list 里边存储的是 follow ruler entity 好，然后重写它的一个方法，这个就是发布的方法，当然它一定要被 spring 管理起来。我们写一个 component 注解，然后把这个名字粘过来，然后把它换成小写。


好。那接下来我们看一看这个 publish 方法我们该怎么去做整理。那个坎沃特还需要用一下，坎沃特在这里边我们还需要拿过来，因为它也需要进行转换，来看一看这个坎沃特拿过来。那接下来我们看一看这个东西应该怎么去做。 publisher 就表示发布。发布里面给我传了两个属性，一个是对应的 App 内幕是什么，还有我们可以把这写好一点。还有就是你发布它肯定发布新的规则新的规则是什么？那我们可以判断说，如果你发布的 ruler 丝为空的话，我就不需要发布了。所以我说 if 如果你的 ruler 丝等于 none 的话，我就直接 return 就好了。直接啥也不管 return 不等于空的情况下我才去发布。然后还是我先要获取 client 不管怎么样我都需要获取这个 client 因为我们就是 dashboard 操作， Open API 操作 open PI 必须要得到 client 这个 client 判断它等不等于空，它不等于空的时候我们再做对应的处理。


我们来看一下 if 如果它不等于 none 的时候，然后我们做处理 else 的情况下，我们就不做处理了，是不是或者是打一个 error 老师在这里直接用 sense out 说什么呢？ client 意思 none 就好了，然后发布失败， publisher failed 好了搞定。


那接下来我们就看一看它不等于空的时候，我们应该怎么去发布发布这个动作其实有两个动作。第一个就是先提交一下，提交完了之后再去进行发布。然后我们来看一下这个东西应该首先怎么去做。首先第一点你不可避免而要获取一些你要用的一些东西，比如说之前我们在这里去取的这个 follow date 还有 App 我们把这两个直接 copy 过来，这些你肯定得需要用。所以说老师在这里就不写了。


有了这两个东西之后，然后我们要发布，要发布你肯定得去发布一个对象，就是把你的这个规则这些东西都封装成一个对象。哪个对象我们之前知道，其实它最终是一个叫做 open item D to O 是一个项发布项。所以说我们在这里一定要把它搞出来，我们发布的一个的项就是这个东西 open item T to 然后我们叫做 DTO 等于 new 一个 open item T to 好，它发布哪些内容呢？我们看一看，它发布的时候要 set 一个 key 这是最重要的。


打开浏览器，我们之前发布的一个 key 就比如 time out 还有这个 new key 这些都是 key 现在我们要发布的 key 是什么呢？现在我们要发布的 key 不就是这个 follow date ID ，我说这个 follow date ID 就是我们这么去拼的，以项目名称加上后面的这个杠 follow rules 这个后缀成为一个 key 所以说我们要发布的 key 就是这个东西。


好了，那我们现在直接放进去，然后还要设置哪些内容？第二， set 我们的这个 value 发布的内容是什么？发布内容无非就是一个 JSON 串，JSON串就是我用它 convert 可以去取到第二 converter 我们之前这个是一个 Jason 格式的 ruler 那我们是不是可以直接转过来？这是 conwater 我们直接把 ruler 词放进来，把 ruler 词放进来是不行的。那我们应该变一下，因为什么，之前是我们把一个 string 转成对象，现在我们应该变成这个 convert 应该这样去写，应该是把一个集合转成一个字符串。然后这回在 convert 的时候你给我一个集合，我帮你返回 convert 一个字符串，这是我要发布的 date 然后接下来有了数据之后剩下的东西，我们就可以随便去写了。
其实这些东西无所谓了，比如说 set 备注，备注我们就可以写叫做 modify 我们可以加上一个时间戳。这个时间戳我们可以去搞一个format ，这里有没有。 Fast data format.有，我们就用它就行了。


fast data format 然后我们定义它是一个 private static 的，它我用大写的等于点 get instance 我们就把这个东西取到这个style 。然后这个年月日时分秒，我们就随便写 YY YY 四个 ymmdd 大写的 hh 小写的 MM SS 可以吧。这是年月日时分秒 get instance pattern 。 OK 这是我们想要做的 pattern 好了，有了它之后我们直接拿过来，当天时间我们直接是不是可以转过来，就是我们的 data 然后 format 那我们可以在上面，它点 format 我们 new 一个 date 就可以了，是不是 Java util 的 date 然后转成一个字符串，就是我们自己的 format 叫做 data format 那这个字符串就是当前时间，我们就直接可以 copy 出来。


这是描述吗？我就说我修改的这个描述时间是什么？然后接下来我们来看一看，比如说修改人是谁？是不是 set 我们的 change modify by date change last modify by 最后修改人是谁呢？那我们修改人肯定是我们自己的这个用户管理员用户，我们用过阿波罗 config user ID 是不就可以？这是最后修改人是谁？然后还有什么？比如说 data create 这里面还有一些属性，有些属性你不填它是不通过的，所以说你必须要都填上。比如说 create by create by 是谁就是也是当前这个人，就是把修改人跟那个这两个都设置一下。


最后这个对象搞定了之后，我们就可以去对这个对象进行操作了。那还是谁通过我们具体的 client 去发起操作，点儿 create or update item 然后传的参数就是 App ID 我们这里面直接有了 ENV 我们是通过 config ENV 取出来的，然后 close to name 在这回戳一下。


close to name 就是它点 close name 取到的，然后 name space 也是一样的，它点 name says 最后那个 DTO 我要发布的内容就是我们刚才所填充的这个 DTO 好，那到这一步为止。其实你现在刚刚的去掉了一个更新的动作，你现在为止刚刚的是比如说现在不是 80 吗？我改成800，你现在点提交只是做了这个动作，只是做了修改的这个动作，但是你还没有点发布，你真正点发布的时候它才生效。所以说对应的我们的这个 Java 代码里边。


第一步它叫做修改操作，然后预发布，然后你接下来还要真正的进行发布，这样的话你的阿波罗的一个配置才真正的更新感知到了。所以说第二件事情我们要做的是真正的发布。真正的发布它有一个对象叫做 publish 这个才是真正的发布动作，它需要 App ID 然后还有以及后面的这个三个参数都需要。然后还有一个 release DTO 那这个 release DTO 是我们需要再重新把它弄出来的，你看这个 release DTO 那我们把它重新弄出来，它叫做 name space name space release DTO ，就它我们给它起个名字叫做 release T to O ，然后等于 new 出来一个 release T to 然后它里边必须要填充的几个属性有哪些？首先你是否要进行发布？它有一个 set 这个东西你必须要设置成 true 这才好使这才叫真正的发布。然后还有你要发布的描述是什么？发布的描述我们就写 modify 就是我就写这个东西了，加一个 configuration 或者加一个content ，做一个区别。


好，然后有了这两个之后，还有就是对应的你发布的人是谁、发布的一些标签儿是什么？这些都是我们之前必须要去加的。比如说点儿 set release title 发布的就是表示发布新属性可以吧，然后我再加个时间，这是发布新属性的时间。然后发布的人是谁？点 set release by 是不是发布的人就是我们当前这个用户。第二 user ID 发布人是谁？好，我们把我们想要填充的东西，填充好了之后，最后再调我们的这个 publish namespace 就可以了，这样的话就真正的发布成功了，这写一个分号。

```java
package com.alibaba.csp.sentinel.dashboard.rule.apollo;

import com.alibaba.csp.sentinel.dashboard.datasource.entity.rule.FlowRuleEntity;
import com.alibaba.csp.sentinel.dashboard.rule.DynamicRulePublisher;
import com.alibaba.csp.sentinel.datasource.Converter;
import com.ctrip.framework.apollo.openapi.client.ApolloOpenApiClient;
import com.ctrip.framework.apollo.openapi.dto.NamespaceReleaseDTO;
import com.ctrip.framework.apollo.openapi.dto.OpenItemDTO;
import org.apache.commons.lang.time.FastDateFormat;
import org.springframework.beans.factory.annotation.Autowired;

import java.util.Date;
import java.util.List;

/**
 * <h1></h1>
 */
public class FlowRuleApolloPublisher implements DynamicRulePublisher<List<FlowRuleEntity>> {


    private static FastDateFormat FASTDATAFORMATE = FastDateFormat.getDateInstance("yyyyMMddHHmmss");

    @Autowired
    private Converter<List<FlowRuleEntity>, String> converter;

    /**
     * Publish rules to remote rule configuration center for given application name.
     *
     * @param app   app name
     * @param rules list of rules to push
     * @throws Exception if some error occurs
     */
    @Override
    public void publish(String appName, List<FlowRuleEntity> rules) throws Exception {

        if (rules == null) {
            return;
        }

        ApolloOpenApiClient client = ApolloConfigUtil.createApolloOpenApiClient(appName);
        String dataFormate = FASTDATAFORMATE.format(new Date());

        if (client != null) {
            // 具体流控的规则 ID
            String flowDataId = ApolloConfigUtil.getFlowDataId(appName);
            // apollo 的运用服务 id
            String appId = ApolloConfigUtil.getAppIdWithAppName(appName);

            OpenItemDTO dto = new OpenItemDTO();
            dto.setKey(flowDataId);
            dto.setValue(converter.convert(rules));
            dto.setComment("modify: " + dataFormate);
            dto.setDataChangeCreatedBy(ApolloConfig.USERID);
            dto.setDataChangeCreatedBy(ApolloConfig.USERID);

            // 1:修改操作，未发布
            client.createOrUpdateItem(appId, ApolloConfig.ENV, ApolloConfig.CLUSTERNAME, ApolloConfig.NAMESPACE, dto);

            // 2：真正发布
            NamespaceReleaseDTO releaseDTO = new NamespaceReleaseDTO();
            releaseDTO.setEmergencyPublish(true);
            releaseDTO.setReleaseComment("modify comment : " + dataFormate);
            releaseDTO.setReleaseTitle("发布新属性：" + dataFormate);
            releaseDTO.setReleasedBy(ApolloConfig.USERID);

            client.publishNamespace(appId, ApolloConfig.ENV, ApolloConfig.CLUSTERNAME, ApolloConfig.NAMESPACE, releaseDTO);

        } else {
            System.out.println("client is null, publish failed !!");
        }
    }
}
```


好了，现在我们真正的把我们自己实现的这个阿波罗的两个扩展搞定了，一个是 provider 一个是 publisher 搞定了之后，这个东西都是我们把它放到我们的这个持久化的这个 spring 中了就相当于把它注入到 spring 中了。然后我们就用这两个东西去修改我们之前最开始的时候注释掉的那个 sentence API client 就可以了。


好，那我们来一起来看一看这个怎么去修改。我们之前把它注释掉了对不对？但是我们还要把我们刚才引进来的这个两个东西加进来。就 O to where ，然后 O to where 它有一个 query fair 就是名字叫什么？名字一个叫做 provider 是吧叫做它。然后我们定义他这是引进来。第一个还有一个奥特维尔的哈克里菲尔是什么？这个是我们的 publisher 对不对？好，然后 private 然后把它引进来。好，现在我们已经把这两个东西引进来了，那接下来我们来看一看怎么去做修改。


第一个， ruler S 这个地方我们第一步就要对它做修改。 ruler S 我们最开始的时候调的是什么呢？走到这儿的时候我们调的是 fetch rulers of machine 通过 dashboard 直接访问的这个具体的那个 client 然后知道 client 的那个 IPU 端口号，还有它的 App name 然后获取的 rules 现在我们就不应该这么去玩了，现在我们直接把它删掉，我们怎么去做怎么去获取这个 rulers 是不是获取 rulers 就是用 provider 就可以了，等于点 get rules 把 App name 传进去就好啦。


这个前面它就是 ap name 然后最终返回的还是这个 list ruler follow ruler entity 这么一个集合，然后最后 save 保存，然后展示。所以说这一件事情已经搞定了。接下来我们往下去找。比如说我们保存的时候我们怎么去做的？看到这是我们之前打的断点是不是保存的时候我们是直接 save 了， save 完了之后然后做的这个动作。那这里边我们不需要再做这个动作了，我们直接把它注释掉。但是你还要做一个 publish 的动作，就是你现在是保存的一个规则。保存规则之后，然后你的做法是通过 HD 请求再通知 client 让它更新。但是现在这事不需要你做了，所以你要把它注释掉，那你把它注释掉就是相当于老师现在把它给它注释掉了。


现在你的 publish 的动作所有的 publish 都是去对我们的阿波罗进行一个操作，所以说你在这里你这样去写，你自己再重新写一个 private wide 就可以了。一个发布的动作也叫做publish 。当然在这里边我们只需要传一个什么，一个 string App name 就可以了。然后 throws 我们的 exeption 首先这句话我们可能还是需要的，因为它是从内存里去找到 rules 之后，后面下面这块调这个 HTTP 的，我们换成操作阿波罗就好了。


我们操作阿波罗用哪个？我们就用刚才的这个 follow ruler 阿波罗 publish 调它的发布动作就可以了。是不是？然后发布的 App 就是他当然这个叫做 find by 某信我们叫 find all Ya PP ，然后直接把 App name 扔进来就可以了。好了，这种方式就搞定了。那我们下面所有的这种 publish 方法是不是都改我们自己最新的就可以了。那我们来看看怎么去改，我们先从最上面这个去改，就把这个注释掉是吧。然后我们把自己的那个逻辑拿过来，然后做一个发布就可以了，直接调一下这个方法，然后把这个 App App 怎么去取过来，就它 entity 里面肯定会有的。


第 2 get App 就可以了，然后这里边 try catch 一下，如果出现异常了怎么办？我们 catch 完了之后打一个日志，打一个 arrow 然后把它返回 error 就 failed return 。 return result 点儿 or failed 然后就等于负 1 吧，然后就是一点儿 get message 可以吧。好，这就是发布失败的时候，我们打一个日志。当然这个日志好像这个类里边应该有吧，这里边有 logo 对象。拿过来我们写的好一点叫做什么呢？叫做 failed to add followerrulers 可以吧。然后这个 E 放到这儿，因为什么呢？因为现在你是什么？你是 save 保存方法对不对？你是去添加规则，所以说你在这里改一下就好了。


然后再往下还有两个地方用到了，那我们直接把这个 copy 过来放下去就好了，什么都不需要改，很简单。我们先看这儿，不管怎么样，我就把它注释掉，把我们自己的逻辑放进来就可以了。然后还有最后一个，这是 delete 删除规则的时候也是把它注释掉，把我们自己的加进来，我看一看，它是一个上下文逻辑，这有一个 old entity 是不是什么叫通过 old entity 去取到了吗？删除吗？本身来讲就是我把以前的规则删除，但是我这里边在删除之前这是 delay 塔。删除之前我还有个引用，我引用拿出来，然后 get App ID 然后去发布过去，这就可以了。那基本上来讲我们的代码在这儿就已经改造完了。


然后这里边这是 test 这个后面是官方给你的一些发布规则。他这个包名都跟我保持一致了。那既然我跟他名字冲突了，我说他怎么报个错，可以直接删掉了，我不要他那无所谓了，我直接给他干掉 delay 掉好了，这样就更简单。反正就是我们现在用我们自己的规则，我们不用他自己官方 DE demo 写的很简单，我把这个 test 包下面这个东西完全都删掉，现在我们完全用自己加的这个规则搞定。


搞定了以后，现在我们就来做一下测试。怎么去做测试呢？我们现在先启动我们现在的这个 dashboard 我们已经改了面目全非的这个 dashboard 我们先启一下试一试，先右键 run as springbot application 启动一下，看看能不能起来。同学们，请看这是可以起来的，起来了以后然后我们现在还要做什么？我说我现在用的不是这个阿波罗 test 吗？我是不是也可以把它骑起来？但是现在我骑它没有用，因为它里边还没有任何的流控规则，它里边只是一个最基本的 hello word 还没有流控规则。


那现在我们刚才已经能够正常的把 dashboard 骑起来了，就证明起码我们应用程序能运行起来，我们现在已经扩展 OK 了，接下来的步骤就是我们自己写代码去验证的步骤了。好了，那基本上这节课我们就先讲到这下节课我们继续做一个验证。感谢小伙伴们收看。




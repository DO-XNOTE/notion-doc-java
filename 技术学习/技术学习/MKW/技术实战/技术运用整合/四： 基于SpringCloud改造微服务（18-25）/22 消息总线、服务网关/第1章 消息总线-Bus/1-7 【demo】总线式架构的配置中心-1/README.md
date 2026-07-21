---
title: 1-7 【demo】总线式架构的配置中心-1
---

# 1-7 【demo】总线式架构的配置中心-1

1-7 【demo】总线式架构的配置中心-1

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/6154c437-5e4c-4025-8533-e666e626b291/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SC7G4PLU%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225724Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAgTB7N7CrubmKa%2BI3Fv0cIgiA5xqk5WhNfT%2BNX%2BudrJAiEAteXFlucibbY5KMPCbl0N0JTV5sVtFeUXA9hSTAfacrgqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOS4UNg0Oz3%2B4%2BJHeircAyOp1B109ayYD4FasNwSRKnVWHGr6WPSvWGGidnkqba9RQ9aLkZXCBhBBZ2Q5EyxgczJg0%2Btm1nrvQeWUK3BRsdG5PcBfWtXtjRRdcf4i2wPH2CFnosvu1ehUcurakZp4Kn36%2BXZj1LnmMSABf0gDHnQYZuoupfGYYDVc%2FZRYY4hXqaMt%2BDOT3YdM0tX5XSzbBgk27pf4%2BsevWMVRCYaY4j%2BYOQF37%2BtW5tIfFGOWKK4703L9apXEtymg%2Fa09WFHiwbUq9AGWxxL%2F5TG3yK%2BguhVr8NNYWz3IqVmrUVP00bvqYBLmCIhMPrLxLtPQ0h9RYxFxDAFNia7dGFm77tMB%2B7uB07zmRZx1rbcREBtHmsPABEJ0cpurF1uFFI0P5hXV8wHBR%2B2qrTsv38PQtQOWnSwJZ6EQSL2ch6tdrtCR5xcoMCtCTSzRZz1MuFDniJA4XxhMMSWVANjj8cu4Z7Xef4iepRiaRftXxsX%2B6YJePOid1viQCUbTRpDaH91zyXpqF8wxrVxsMjh%2BxR7bCPQrPrOl5IlA%2BlJz1jY3AsOZwrvo2ZJqB5iCadYLoSg817TwskmV2mgebUsROuvuzyprZlfHVUWNzedVdXW0v8H3M7SVDBO5tc5EavpnnJnMIS5%2F9IGOqUBo3A%2F5Oo%2F9GleS6tR6xl8c%2Ffj1jbl3xrbDShpLqMmgclUdTHe%2F%2BrH2iv69%2FYeUS6aFjpjfNFPkDNxUwgRWq%2BX9lBRyeK2hymZFZHbTDhlmCTkgMaxrcOfBvxK0LruBXBPFQ5aYFELN7%2FwDXRrLF03YEJX4jYhkeWRBR1gdptAcDil8OfYtUeT0Ig0WONM3rltmIDIHt%2BF4ewfdFkcIbHiWr%2BP58Wu&X-Amz-Signature=ebc119b7997021e631377f4abbf846118d0fd8e1bcba83f0c9ea72ba6e6e6ccb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/90c205ea-f911-4949-8fed-ab888c7bb34e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SC7G4PLU%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225724Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAgTB7N7CrubmKa%2BI3Fv0cIgiA5xqk5WhNfT%2BNX%2BudrJAiEAteXFlucibbY5KMPCbl0N0JTV5sVtFeUXA9hSTAfacrgqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOS4UNg0Oz3%2B4%2BJHeircAyOp1B109ayYD4FasNwSRKnVWHGr6WPSvWGGidnkqba9RQ9aLkZXCBhBBZ2Q5EyxgczJg0%2Btm1nrvQeWUK3BRsdG5PcBfWtXtjRRdcf4i2wPH2CFnosvu1ehUcurakZp4Kn36%2BXZj1LnmMSABf0gDHnQYZuoupfGYYDVc%2FZRYY4hXqaMt%2BDOT3YdM0tX5XSzbBgk27pf4%2BsevWMVRCYaY4j%2BYOQF37%2BtW5tIfFGOWKK4703L9apXEtymg%2Fa09WFHiwbUq9AGWxxL%2F5TG3yK%2BguhVr8NNYWz3IqVmrUVP00bvqYBLmCIhMPrLxLtPQ0h9RYxFxDAFNia7dGFm77tMB%2B7uB07zmRZx1rbcREBtHmsPABEJ0cpurF1uFFI0P5hXV8wHBR%2B2qrTsv38PQtQOWnSwJZ6EQSL2ch6tdrtCR5xcoMCtCTSzRZz1MuFDniJA4XxhMMSWVANjj8cu4Z7Xef4iepRiaRftXxsX%2B6YJePOid1viQCUbTRpDaH91zyXpqF8wxrVxsMjh%2BxR7bCPQrPrOl5IlA%2BlJz1jY3AsOZwrvo2ZJqB5iCadYLoSg817TwskmV2mgebUsROuvuzyprZlfHVUWNzedVdXW0v8H3M7SVDBO5tc5EavpnnJnMIS5%2F9IGOqUBo3A%2F5Oo%2F9GleS6tR6xl8c%2Ffj1jbl3xrbDShpLqMmgclUdTHe%2F%2BrH2iv69%2FYeUS6aFjpjfNFPkDNxUwgRWq%2BX9lBRyeK2hymZFZHbTDhlmCTkgMaxrcOfBvxK0LruBXBPFQ5aYFELN7%2FwDXRrLF03YEJX4jYhkeWRBR1gdptAcDil8OfYtUeT0Ig0WONM3rltmIDIHt%2BF4ewfdFkcIbHiWr%2BP58Wu&X-Amz-Signature=2e6c7173772a97cb2c511eeffdbe554eefdb77b27ed39d2a2b46872f9efef103&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/31cd834d-6d23-4e9e-b066-769601a15eb9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SC7G4PLU%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225724Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAgTB7N7CrubmKa%2BI3Fv0cIgiA5xqk5WhNfT%2BNX%2BudrJAiEAteXFlucibbY5KMPCbl0N0JTV5sVtFeUXA9hSTAfacrgqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOS4UNg0Oz3%2B4%2BJHeircAyOp1B109ayYD4FasNwSRKnVWHGr6WPSvWGGidnkqba9RQ9aLkZXCBhBBZ2Q5EyxgczJg0%2Btm1nrvQeWUK3BRsdG5PcBfWtXtjRRdcf4i2wPH2CFnosvu1ehUcurakZp4Kn36%2BXZj1LnmMSABf0gDHnQYZuoupfGYYDVc%2FZRYY4hXqaMt%2BDOT3YdM0tX5XSzbBgk27pf4%2BsevWMVRCYaY4j%2BYOQF37%2BtW5tIfFGOWKK4703L9apXEtymg%2Fa09WFHiwbUq9AGWxxL%2F5TG3yK%2BguhVr8NNYWz3IqVmrUVP00bvqYBLmCIhMPrLxLtPQ0h9RYxFxDAFNia7dGFm77tMB%2B7uB07zmRZx1rbcREBtHmsPABEJ0cpurF1uFFI0P5hXV8wHBR%2B2qrTsv38PQtQOWnSwJZ6EQSL2ch6tdrtCR5xcoMCtCTSzRZz1MuFDniJA4XxhMMSWVANjj8cu4Z7Xef4iepRiaRftXxsX%2B6YJePOid1viQCUbTRpDaH91zyXpqF8wxrVxsMjh%2BxR7bCPQrPrOl5IlA%2BlJz1jY3AsOZwrvo2ZJqB5iCadYLoSg817TwskmV2mgebUsROuvuzyprZlfHVUWNzedVdXW0v8H3M7SVDBO5tc5EavpnnJnMIS5%2F9IGOqUBo3A%2F5Oo%2F9GleS6tR6xl8c%2Ffj1jbl3xrbDShpLqMmgclUdTHe%2F%2BrH2iv69%2FYeUS6aFjpjfNFPkDNxUwgRWq%2BX9lBRyeK2hymZFZHbTDhlmCTkgMaxrcOfBvxK0LruBXBPFQ5aYFELN7%2FwDXRrLF03YEJX4jYhkeWRBR1gdptAcDil8OfYtUeT0Ig0WONM3rltmIDIHt%2BF4ewfdFkcIbHiWr%2BP58Wu&X-Amz-Signature=77f88324acf65f71d35b47a2554523e06c0e5196b5455befc2740bb70c29e0fd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/a4df6326-426b-4b04-87e4-b0eb9edadd92/SCR-20240721-bhwu.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SC7G4PLU%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225724Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAgTB7N7CrubmKa%2BI3Fv0cIgiA5xqk5WhNfT%2BNX%2BudrJAiEAteXFlucibbY5KMPCbl0N0JTV5sVtFeUXA9hSTAfacrgqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOS4UNg0Oz3%2B4%2BJHeircAyOp1B109ayYD4FasNwSRKnVWHGr6WPSvWGGidnkqba9RQ9aLkZXCBhBBZ2Q5EyxgczJg0%2Btm1nrvQeWUK3BRsdG5PcBfWtXtjRRdcf4i2wPH2CFnosvu1ehUcurakZp4Kn36%2BXZj1LnmMSABf0gDHnQYZuoupfGYYDVc%2FZRYY4hXqaMt%2BDOT3YdM0tX5XSzbBgk27pf4%2BsevWMVRCYaY4j%2BYOQF37%2BtW5tIfFGOWKK4703L9apXEtymg%2Fa09WFHiwbUq9AGWxxL%2F5TG3yK%2BguhVr8NNYWz3IqVmrUVP00bvqYBLmCIhMPrLxLtPQ0h9RYxFxDAFNia7dGFm77tMB%2B7uB07zmRZx1rbcREBtHmsPABEJ0cpurF1uFFI0P5hXV8wHBR%2B2qrTsv38PQtQOWnSwJZ6EQSL2ch6tdrtCR5xcoMCtCTSzRZz1MuFDniJA4XxhMMSWVANjj8cu4Z7Xef4iepRiaRftXxsX%2B6YJePOid1viQCUbTRpDaH91zyXpqF8wxrVxsMjh%2BxR7bCPQrPrOl5IlA%2BlJz1jY3AsOZwrvo2ZJqB5iCadYLoSg817TwskmV2mgebUsROuvuzyprZlfHVUWNzedVdXW0v8H3M7SVDBO5tc5EavpnnJnMIS5%2F9IGOqUBo3A%2F5Oo%2F9GleS6tR6xl8c%2Ffj1jbl3xrbDShpLqMmgclUdTHe%2F%2BrH2iv69%2FYeUS6aFjpjfNFPkDNxUwgRWq%2BX9lBRyeK2hymZFZHbTDhlmCTkgMaxrcOfBvxK0LruBXBPFQ5aYFELN7%2FwDXRrLF03YEJX4jYhkeWRBR1gdptAcDil8OfYtUeT0Ig0WONM3rltmIDIHt%2BF4ewfdFkcIbHiWr%2BP58Wu&X-Amz-Signature=150e082f8ab75bf82d7825e6ccdf925e9ac5fe087a4160a42cb2a1d7cf505460&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

hello 慕课网的各位同学们，大家好，作为整个 bus 章节中唯一一个需要大家实操的 demo 环节，这节我带大家一起去实现一个基于总线式架构的配置中心。这一节主要包含三个部分的内容。第一部分咱要创建两个全新的毛九，分别是 config bus server 和 config bus consumer 从名字中就可以看出，它分别是集成了 bus 的配置中心以及集成了 bus 的 consumer 节点。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/4315f3de-b892-4f0d-a69f-81b69b78ccb4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SC7G4PLU%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225724Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAgTB7N7CrubmKa%2BI3Fv0cIgiA5xqk5WhNfT%2BNX%2BudrJAiEAteXFlucibbY5KMPCbl0N0JTV5sVtFeUXA9hSTAfacrgqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOS4UNg0Oz3%2B4%2BJHeircAyOp1B109ayYD4FasNwSRKnVWHGr6WPSvWGGidnkqba9RQ9aLkZXCBhBBZ2Q5EyxgczJg0%2Btm1nrvQeWUK3BRsdG5PcBfWtXtjRRdcf4i2wPH2CFnosvu1ehUcurakZp4Kn36%2BXZj1LnmMSABf0gDHnQYZuoupfGYYDVc%2FZRYY4hXqaMt%2BDOT3YdM0tX5XSzbBgk27pf4%2BsevWMVRCYaY4j%2BYOQF37%2BtW5tIfFGOWKK4703L9apXEtymg%2Fa09WFHiwbUq9AGWxxL%2F5TG3yK%2BguhVr8NNYWz3IqVmrUVP00bvqYBLmCIhMPrLxLtPQ0h9RYxFxDAFNia7dGFm77tMB%2B7uB07zmRZx1rbcREBtHmsPABEJ0cpurF1uFFI0P5hXV8wHBR%2B2qrTsv38PQtQOWnSwJZ6EQSL2ch6tdrtCR5xcoMCtCTSzRZz1MuFDniJA4XxhMMSWVANjj8cu4Z7Xef4iepRiaRftXxsX%2B6YJePOid1viQCUbTRpDaH91zyXpqF8wxrVxsMjh%2BxR7bCPQrPrOl5IlA%2BlJz1jY3AsOZwrvo2ZJqB5iCadYLoSg817TwskmV2mgebUsROuvuzyprZlfHVUWNzedVdXW0v8H3M7SVDBO5tc5EavpnnJnMIS5%2F9IGOqUBo3A%2F5Oo%2F9GleS6tR6xl8c%2Ffj1jbl3xrbDShpLqMmgclUdTHe%2F%2BrH2iv69%2FYeUS6aFjpjfNFPkDNxUwgRWq%2BX9lBRyeK2hymZFZHbTDhlmCTkgMaxrcOfBvxK0LruBXBPFQ5aYFELN7%2FwDXRrLF03YEJX4jYhkeWRBR1gdptAcDil8OfYtUeT0Ig0WONM3rltmIDIHt%2BF4ewfdFkcIbHiWr%2BP58Wu&X-Amz-Signature=1749713512628dfe99738d4ad0dbe08fdab83e89f024b66f9ca6c9b41aae4e53&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

OK 在创建好这两个应用以后，我们要启动 rabbit MQ 相信大家在前面的分布式章节中已经学习了 rabbit MQ 的细致的用法。那这里咱就不深入 rabbit MQ 的知识点讲解了，直接把它启动起来，然后修改一下 demo 的配置属性，将 rab 的 MQ 集成到上面咱写好的两个项目当中。


好，这一步完成以后，我们要使用 X rate 服务推送 bus 变更。大家还记得在 config 章节中，咱使用的是 accurator 的 refresh 端点，这里我们将使用一个不同的 endpoint 来推送属性的变更消息。 OK 大家准备好的话，我们一块去 intelligj 里面开工。编程是我快乐 996 是我的福报，又到了享受福报的时候了，咱先创建一个 directory 叫 bus 开启一个新的章节，先要有一个新的文件夹，在这个 buzz 下面，我们来创建一个新的毛九。


第一步，咱先创建 config server 好了，OK这个 config server 起名叫 config bus server 这是它的 artifact ID 保存一下，然后 module name 和 artifact 保持一致。项目的路径就是咱前面创建的 bus 文件夹下面点击 finish 321 出。 OK 这个 palm 咱就不一行手打了，直接到前面创建的 config server 有瑞卡这个项目里面，咱来去偷师学艺，把这个项目从头到尾的 dependency 全部 copy 下来，也就两个。


OK copy 到这个 bus 咱创建的 bus server 这里好，可是就这两个 dependency 也不够，咱耍大刀，我们要加两个分别是谁。 OK 那咱先来加 bus 的 dependency 好了，bus the dependency group ID 依然是 org and sprint framework and cloud OK 它的 artifact ID 是 sprint 杠 cloud 杠 starter 杠 bus 然后后面跟的是 amqp 咱如果使用 rabbit MQ 引入这个依赖就可以了，我们不妨先点进去这个 rk fact ID ，看一看里面有什么门道好往下移哟看到吗？同学们这里还偷偷的藏着一个 spring cloud stream 的组件。所以就像咱前面说的 bus 就是一个空壳子了，它底层跟消息中间件通信实际上是借助的。谁？ spring cloud stream 组件对不对？所以这里引入了 stream 组件下的 rabbit 适配层。


OK 那咱再回退回来。好，现在有三个 dependency 了，那还需要一个是 activator 咱从其他的地方随便找一个有 actuator 的复制过来就可以了。 config client 好像这里有，果然咱把它复制一下放到 config bus server 这里。 OK 顺手给他的 packaging 类型指定成价。那到这里整个 pum 文件就创建好了。

```java
       <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-config-server</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-netflix-eureka-client</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-bus-amqp</artifactId>
        </dependency>

        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-actuator</artifactId>
        </dependency>
```


咱接下来创建一个，启动类的话跟前面咱创建好的 config server 没有什么不同，这里可以直接 copy 过来，我们先把 come.imock spring cloud 这一个路径给它创建好，然后再到 config server eurika 这里去偷尸了这个闷方法，config server application 启动类直接给压回寨中名字，要不咱稍微改一下，把它改成 config bus server application 类上面的三顶大帽子，咱一顶不多一顶不少原样不动放在这，不需要额外的配置。记得咱前面章节中说过的 config 和 buzz 集成是无缝集成，你甚至都感知不到 bus 的存在，对咱的代码一点影响都没有。


好，那我们这个康菲克创建好了以后，接下来要创建配置文件了，配置文件也不用一行手打，我们还是可以向 config server eureka 这个毛主借鉴先进经验，我们把它下面的 application 和 boot strap 都 copy 过来。


这个 boot strap 它是 encrepe 的 key 保持原样不动。但是 application 这里我们需要动点手脚。第一个要改动的地方就是 application name 咱把 config server eureka 改成 config 杠 bus 杠 serverok 这一步改完了。接下来还有两处改动，这第二处改动就跟 rabbit MQ 相关了。我们看这里要在 spring 节点下面配置 rabbit MQ 的连接字符串，我们来配置 rabbit MQ 节点，这里打上 rabbit MQ 全都是小写，这个 MQ 的 M 不会是大写，大家不要打错了二倍 MQ 接下来是 host host 我们就使用默认的 local host 就可以了。然后咱要指定 rabbit MQ 的 pot 这个 pot 我们就采用默认的5672。如果大家在安装 rabbit MQ 的时候没有更改端口。那么这里使用默认的端口，如果有更改端口，那这里要改成大家更改后的那个端口。 OK 那接下来我们要给出 username username 还有 password 这两个要根据大家自己本地安装的 rabbit MQ 做调整了。因为老师这里没有做任何的定制，所以一切都使用的默认账号，那他的默认账号是叫 guest 同样它的 password 也是叫guest。

```java
---------------application.yml--------------------------------------------------------------------------------

spring:
  application:
    name: config-bus-server
  rabbitmq:
    host: 172.16.136.223
#    host: 172.16.136.226  两个都可以用
    port: 5672
    username: admin
    password: 123456
  cloud:
    config:
      server:
        git:
          uri: https://github.com/DO-XNOTE/config-repo.git
          force-pull: true  # 强制拉去文件
#          search-paths:  有多个项目的配置文件可以使用 search-path来指定
#            -
#          username:    现在是 public 的， 如果是线上的就需要把他们填上了
#          password:

eureka:
  client:
    service-url:
      defaultZone: http://peer1:20000/eureka


management:
  security:
    enabled: false
  endpoints:
    web:
      exposure:
        include: "*"
  endpoint:
    health:
      show-details: always


server:
  port: 60002

-----------bootstrap.yml----------------------------------------------------------------------

encrypt:
  key: 20051001
```


Ok. 配置好 rabbit MQ 以后咱还有一个配置要做。大家记得前面咋引入了 activator 对不对啊？那我这里需要把 actuator 的所有的 endpoints 全部开放出来。那我这里从其他项目中 copy 这一段逻辑，就从 config client 这里把它 copy 过来。好了，找到这个 management 节点，把 activator 的所有 endpoint 统统给它开放出来。好，复制这里粘贴。 OK acterator 改好以后，咱再改一下这个 server port 前面的 config server 是使用的60,001，那咱这里把它改成60,002。好了，OK这里把它保存好了以后，那这个项目就改造完成了，我们试着把它启动一下。咱这里总共要启动三个服务，排好队一个个来。


第一个服务是谁？是 eurika 的 server 我们把 eurika server 找到，然后慢函数启动起来。好在启动 eureka server 的同时，我们要确保 rabbit MQ 是处于开启状态的。我这里到命令行直接把 rabbit MQ 使用这个 rabbit MQ 杠 server 命令启动起来。因为我已经把 rabmq 加到了 Mac 系统中的 bash profile 文件。所以我这边直接使用这个命令把 rabbit MQ 给启动起来，正在启动它这里已经提示完成了，并且加载了 6 个 plugin 那我们到页面上面看一下，验证一下 rabmq 是不是启动成功了，打造它的默认管理界面。


好，这已经加载起来了。那瑞贝 fq 这边没有什么问题，我们再回到银泰 dj 里面，看到 eureka 也已经启动完成了，把 log 清一下。然后咱回到 config bus server 这里，直接把咱刚才创建的 bus server 启动起来，不用用 debug 直接 run 就好了，看到 spring 标签成功一半。 OK 他这边看到已经连接上了 message channel 那说明这个 rabbi MQ 也已经连接成功了，往下它显示 started 那我们先使用 postman 来试一下，看它能不能拉取到 github 的文件，这样保证咱的配置不出错。 postman 里发送到端口60,002，然后拉取 config consumer production 的文件，以 JSON 格式返回。


好，看到文件内容已经完整的返回了。那接下来咱要到浏览器上验证 X read 是不是配置正确。我们打开 local host 然后端口号是60,002，加上一个斜杠，后面的路径叫 activator 点击回车。好，大家看到这里开放了很多 end points ，咱要找哪个 endpoints 咱要找 refreshok 那这里我们可以看到两个 refresh endpoints 一个 refresh 是谁呢？是咱前面 config 组件中使用的刷新接口，对不对？它叫 extraterrefresh 那么另一个 endpoint 是谁啊？在这里 accurator bus refresh 这就是我们待会将要使用的 endpoint 我们会发送一条消息给他，然后触发整个集群的批量刷新。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/eada0493-caf9-4517-b0c0-492e73ce6916/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SC7G4PLU%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225724Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIAgTB7N7CrubmKa%2BI3Fv0cIgiA5xqk5WhNfT%2BNX%2BudrJAiEAteXFlucibbY5KMPCbl0N0JTV5sVtFeUXA9hSTAfacrgqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDOS4UNg0Oz3%2B4%2BJHeircAyOp1B109ayYD4FasNwSRKnVWHGr6WPSvWGGidnkqba9RQ9aLkZXCBhBBZ2Q5EyxgczJg0%2Btm1nrvQeWUK3BRsdG5PcBfWtXtjRRdcf4i2wPH2CFnosvu1ehUcurakZp4Kn36%2BXZj1LnmMSABf0gDHnQYZuoupfGYYDVc%2FZRYY4hXqaMt%2BDOT3YdM0tX5XSzbBgk27pf4%2BsevWMVRCYaY4j%2BYOQF37%2BtW5tIfFGOWKK4703L9apXEtymg%2Fa09WFHiwbUq9AGWxxL%2F5TG3yK%2BguhVr8NNYWz3IqVmrUVP00bvqYBLmCIhMPrLxLtPQ0h9RYxFxDAFNia7dGFm77tMB%2B7uB07zmRZx1rbcREBtHmsPABEJ0cpurF1uFFI0P5hXV8wHBR%2B2qrTsv38PQtQOWnSwJZ6EQSL2ch6tdrtCR5xcoMCtCTSzRZz1MuFDniJA4XxhMMSWVANjj8cu4Z7Xef4iepRiaRftXxsX%2B6YJePOid1viQCUbTRpDaH91zyXpqF8wxrVxsMjh%2BxR7bCPQrPrOl5IlA%2BlJz1jY3AsOZwrvo2ZJqB5iCadYLoSg817TwskmV2mgebUsROuvuzyprZlfHVUWNzedVdXW0v8H3M7SVDBO5tc5EavpnnJnMIS5%2F9IGOqUBo3A%2F5Oo%2F9GleS6tR6xl8c%2Ffj1jbl3xrbDShpLqMmgclUdTHe%2F%2BrH2iv69%2FYeUS6aFjpjfNFPkDNxUwgRWq%2BX9lBRyeK2hymZFZHbTDhlmCTkgMaxrcOfBvxK0LruBXBPFQ5aYFELN7%2FwDXRrLF03YEJX4jYhkeWRBR1gdptAcDil8OfYtUeT0Ig0WONM3rltmIDIHt%2BF4ewfdFkcIbHiWr%2BP58Wu&X-Amz-Signature=1d57e9d44ff3c1dd87a2fae5482c997d9f2ad659822ca4eb318af550c308de14&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

大家看到这里还有一个 destination 的参数，那它是什么含义呢？而上一章中咱使用的 refresh endpoint 是没有这个参数的。为什么？因为上一节当中的 actuator refresh 是针对单节点的刷新，所以在你发送刷新请求的时候，这个机器名其实已经指定好了。它每次刷新实际上刷新的机器就是前面的这个 local host 60,002，也就是咱前面提供的 IP 地址。但是对于 bus refresh 来讲它可不一样，它每次刷新是刷新所有已经订阅了这个消息的服务。那假如说我不想让这个服务集群中的所有机器全部刷新，我想指定某些特征量，也就是具备这些特征的机器才进行刷新。那怎么办。这里就可以用到后面的 destination 通过这个属性，我们可以做一些手脚，只对某些特定的服务器触发这个属性刷新的动作。


OK 那到这里我们上半场就要结束了。在上半场当中，我们配置了 config bus server 它跟上一张 config 章节当中有这么几点不同，分别是 palm 文件，我们多加了两个依赖，一个是 bus 的依赖，另一个是 activator 然后我们又将它所有的 activator 端口全部暴露了出来，并且在 application YAML 当中配置了一串 rabbit MQ 的连接字符串。那么配置上的不同之处也就只有 palm 和 application YAML 了，对于代码层面没有做任何的改动。所以说这个 bus 的继承对于咱的业务代码来说是完全无感知的。 OK 那这一节就到这里结束了。下一节当中我将带大家一起创建另外一个应用 config bus client 然后通过 bus 组件批量的通知所有节点，进行属性文件的更新。同学们，那我们下一节课程再见




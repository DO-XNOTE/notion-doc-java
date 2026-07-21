---
title: 2-8 Sentinel整合Apollo配置文件解析与ApolloOpenApiClient创建-1
---

# 2-8 Sentinel整合Apollo配置文件解析与ApolloOpenApiClient创建-1

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/28136e7a-302d-4f2a-92bf-a0fd72dd88c6/SCR-20240723-coqj.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662AEAW2IP%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGIyBchkhWbjf%2B4pDgeWoCzM8Yy5wXi9pwAsVrZaRE4YAiEA%2F0FBXCmaXtPGaKvOV6stv%2F5e6meb%2FzR1b7g%2Bqw5PHhUqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGf6kE5i0gdF3f8NJircA4ZGhidl4bQxbx4BAEHMhSZZhvBKSd2jkGXePQt6iJ97uT80Kx3r%2FPvvglIpRnzamjE39LDh7dChJaTwToL6EMEh4G0KYRBqYasHGoGsX7KfrIlsh4XhBJklW5ZPI4tAki9jXT3AApf3xwOrSMchnISBB3ExUSdbl0ldnZaHnRWjGUFVUIqJw4UDhuVFPcCxSfZVKu9IHIOFduy6dq7V1gJyOzvbbAs5FeHDfh8%2BeP3U2vs%2BPxI2f5Ezq4HHIXTYtyPVsMYtrJ95myt9bS7m1Xp6cDiEg8jyfibcBd7mGwtKNSPZBj7FWyjbF5EPlOVAOrBXt6lC28lb6m57ezg17s2pF6H6BObUW%2B7uzzQmurwrocvwN%2FPsdZkK3UjyEzEyenyk9tg2tD4QwMm%2BkCZRpCZOLoCfoLTrHx1QB7zQHtQAdVtfgQnLCxIuF99Ex4VYAqrk%2BK5Z0Kk7K2woDg%2B3qxcHMrzFUSa8dDyVxQ0ehtqNKSIr8qxdbd%2Bylhkxw4I9ZmH7yx9HvFCVMDGHgmorGwi2h%2BttkluwTKEt51MxrkG8gXjaaNVrhhJA%2BRy2b64aEX7S9fnFdBzm%2BDdmygEGsAPii8EBpfXrMiIwcGnmUmQjGd9x6QCor5ghNXslMPK3%2F9IGOqUBiv94agjdOpLQn0xQic%2FTEE2iSqdmyL43Y5xvOziBlpcTl6rOL27E09dZvgHvI72xGnC%2F0oNXzTXAzue2yLUksFoA%2B3tvTtuwgdIWccNLkaJi%2FTiWqyYVkw5GGO5Iyqq2tTfZ5ni%2BgLgldFcaFLLlOraR0qOz8QpmKw38ePktQED7HQedGAW5r0nSjOIkWa63mmuk5bxyEn%2BVlF%2FBSktSBJd%2B0wjE&X-Amz-Signature=498d934480469c6ce0db7908f4bf59d11e22e4f4987c0490720b0650f3f7e5a7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/3ba13d42-0060-4dda-9f4d-8f95ce2fc033/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662AEAW2IP%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGIyBchkhWbjf%2B4pDgeWoCzM8Yy5wXi9pwAsVrZaRE4YAiEA%2F0FBXCmaXtPGaKvOV6stv%2F5e6meb%2FzR1b7g%2Bqw5PHhUqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGf6kE5i0gdF3f8NJircA4ZGhidl4bQxbx4BAEHMhSZZhvBKSd2jkGXePQt6iJ97uT80Kx3r%2FPvvglIpRnzamjE39LDh7dChJaTwToL6EMEh4G0KYRBqYasHGoGsX7KfrIlsh4XhBJklW5ZPI4tAki9jXT3AApf3xwOrSMchnISBB3ExUSdbl0ldnZaHnRWjGUFVUIqJw4UDhuVFPcCxSfZVKu9IHIOFduy6dq7V1gJyOzvbbAs5FeHDfh8%2BeP3U2vs%2BPxI2f5Ezq4HHIXTYtyPVsMYtrJ95myt9bS7m1Xp6cDiEg8jyfibcBd7mGwtKNSPZBj7FWyjbF5EPlOVAOrBXt6lC28lb6m57ezg17s2pF6H6BObUW%2B7uzzQmurwrocvwN%2FPsdZkK3UjyEzEyenyk9tg2tD4QwMm%2BkCZRpCZOLoCfoLTrHx1QB7zQHtQAdVtfgQnLCxIuF99Ex4VYAqrk%2BK5Z0Kk7K2woDg%2B3qxcHMrzFUSa8dDyVxQ0ehtqNKSIr8qxdbd%2Bylhkxw4I9ZmH7yx9HvFCVMDGHgmorGwi2h%2BttkluwTKEt51MxrkG8gXjaaNVrhhJA%2BRy2b64aEX7S9fnFdBzm%2BDdmygEGsAPii8EBpfXrMiIwcGnmUmQjGd9x6QCor5ghNXslMPK3%2F9IGOqUBiv94agjdOpLQn0xQic%2FTEE2iSqdmyL43Y5xvOziBlpcTl6rOL27E09dZvgHvI72xGnC%2F0oNXzTXAzue2yLUksFoA%2B3tvTtuwgdIWccNLkaJi%2FTiWqyYVkw5GGO5Iyqq2tTfZ5ni%2BgLgldFcaFLLlOraR0qOz8QpmKw38ePktQED7HQedGAW5r0nSjOIkWa63mmuk5bxyEn%2BVlF%2FBSktSBJd%2B0wjE&X-Amz-Signature=2f7ace15c080443748b231cc0eb12a3e2555ce14ed16a756d20446413d2d4628&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/9d2aa5e1-6756-4e89-994d-e286f41c5fcd/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662AEAW2IP%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGIyBchkhWbjf%2B4pDgeWoCzM8Yy5wXi9pwAsVrZaRE4YAiEA%2F0FBXCmaXtPGaKvOV6stv%2F5e6meb%2FzR1b7g%2Bqw5PHhUqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGf6kE5i0gdF3f8NJircA4ZGhidl4bQxbx4BAEHMhSZZhvBKSd2jkGXePQt6iJ97uT80Kx3r%2FPvvglIpRnzamjE39LDh7dChJaTwToL6EMEh4G0KYRBqYasHGoGsX7KfrIlsh4XhBJklW5ZPI4tAki9jXT3AApf3xwOrSMchnISBB3ExUSdbl0ldnZaHnRWjGUFVUIqJw4UDhuVFPcCxSfZVKu9IHIOFduy6dq7V1gJyOzvbbAs5FeHDfh8%2BeP3U2vs%2BPxI2f5Ezq4HHIXTYtyPVsMYtrJ95myt9bS7m1Xp6cDiEg8jyfibcBd7mGwtKNSPZBj7FWyjbF5EPlOVAOrBXt6lC28lb6m57ezg17s2pF6H6BObUW%2B7uzzQmurwrocvwN%2FPsdZkK3UjyEzEyenyk9tg2tD4QwMm%2BkCZRpCZOLoCfoLTrHx1QB7zQHtQAdVtfgQnLCxIuF99Ex4VYAqrk%2BK5Z0Kk7K2woDg%2B3qxcHMrzFUSa8dDyVxQ0ehtqNKSIr8qxdbd%2Bylhkxw4I9ZmH7yx9HvFCVMDGHgmorGwi2h%2BttkluwTKEt51MxrkG8gXjaaNVrhhJA%2BRy2b64aEX7S9fnFdBzm%2BDdmygEGsAPii8EBpfXrMiIwcGnmUmQjGd9x6QCor5ghNXslMPK3%2F9IGOqUBiv94agjdOpLQn0xQic%2FTEE2iSqdmyL43Y5xvOziBlpcTl6rOL27E09dZvgHvI72xGnC%2F0oNXzTXAzue2yLUksFoA%2B3tvTtuwgdIWccNLkaJi%2FTiWqyYVkw5GGO5Iyqq2tTfZ5ni%2BgLgldFcaFLLlOraR0qOz8QpmKw38ePktQED7HQedGAW5r0nSjOIkWa63mmuk5bxyEn%2BVlF%2FBSktSBJd%2B0wjE&X-Amz-Signature=fe0fe9e65283004c54afcbabbbd18a553ced1b349bf82b66cf6b4c3368ff8c91&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/7f97c345-fa38-4281-94b5-52c0d1d8e3c3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662AEAW2IP%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGIyBchkhWbjf%2B4pDgeWoCzM8Yy5wXi9pwAsVrZaRE4YAiEA%2F0FBXCmaXtPGaKvOV6stv%2F5e6meb%2FzR1b7g%2Bqw5PHhUqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGf6kE5i0gdF3f8NJircA4ZGhidl4bQxbx4BAEHMhSZZhvBKSd2jkGXePQt6iJ97uT80Kx3r%2FPvvglIpRnzamjE39LDh7dChJaTwToL6EMEh4G0KYRBqYasHGoGsX7KfrIlsh4XhBJklW5ZPI4tAki9jXT3AApf3xwOrSMchnISBB3ExUSdbl0ldnZaHnRWjGUFVUIqJw4UDhuVFPcCxSfZVKu9IHIOFduy6dq7V1gJyOzvbbAs5FeHDfh8%2BeP3U2vs%2BPxI2f5Ezq4HHIXTYtyPVsMYtrJ95myt9bS7m1Xp6cDiEg8jyfibcBd7mGwtKNSPZBj7FWyjbF5EPlOVAOrBXt6lC28lb6m57ezg17s2pF6H6BObUW%2B7uzzQmurwrocvwN%2FPsdZkK3UjyEzEyenyk9tg2tD4QwMm%2BkCZRpCZOLoCfoLTrHx1QB7zQHtQAdVtfgQnLCxIuF99Ex4VYAqrk%2BK5Z0Kk7K2woDg%2B3qxcHMrzFUSa8dDyVxQ0ehtqNKSIr8qxdbd%2Bylhkxw4I9ZmH7yx9HvFCVMDGHgmorGwi2h%2BttkluwTKEt51MxrkG8gXjaaNVrhhJA%2BRy2b64aEX7S9fnFdBzm%2BDdmygEGsAPii8EBpfXrMiIwcGnmUmQjGd9x6QCor5ghNXslMPK3%2F9IGOqUBiv94agjdOpLQn0xQic%2FTEE2iSqdmyL43Y5xvOziBlpcTl6rOL27E09dZvgHvI72xGnC%2F0oNXzTXAzue2yLUksFoA%2B3tvTtuwgdIWccNLkaJi%2FTiWqyYVkw5GGO5Iyqq2tTfZ5ni%2BgLgldFcaFLLlOraR0qOz8QpmKw38ePktQED7HQedGAW5r0nSjOIkWa63mmuk5bxyEn%2BVlF%2FBSktSBJd%2B0wjE&X-Amz-Signature=2acb071c1aea00135df37c7a874722b722ef3f43861137733e608e03243aa2fd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

之前已经分析了我们怎么去做，无非就是把这个 dashboard 直接跟我们 client 端交互的这个 sentence App client 把它注释掉。然后把该用阿波罗持久化 service 地方我们用到阿波罗就好了，让我们所有操作都是直接操作阿波罗，而不是当他直接发 H 请求到我们自己的开单端。我们清楚这个事情之后，我们就一步步开始去做。怎么去做呢？首先我们先定义一些配置。为什么要定义配置呢？因为我们的 dashboard 服务以后要访问的是我们的阿波罗，也就是说我们会用到阿波罗的这个第三方的这个 Open API 所以说现在我们的 pom 文件里边第一件事情我们这里边已经有了我们阿波罗的 Open API 了，看见了，只不过它是 test 那其实我们打包的时候其实我们可以把它变成，把这个 test 去掉也可以，它有了阿波罗的 Open API 我们在这里就不用去引了，对不对？这是新版本里面直接带的一个 test 服务。 OK 那还有什么 knox 的都会有，那这样的话就可以了。我们现在在旧版本的时候，我们需要自己手工的去把这个阿波罗的 Open API 引进来。


好了，搞定这个事情之后，引入炸包，当然新版本有就不需要了，然后接下来我们要加一些配置项。首先我们在这里来看看这个配置我们应该怎么去改，我们还是要在这个 application.props 里面，因为它是一个死存部的工程，然后去加一些我们对阿波罗的一些配置，因为我们的 dashboard 访问阿波罗，你肯定有一些对应的配置要去做。


首先第一个配置是什么呢？就是你阿波罗的路径它的服务地址是什么？在这里就是阿波罗配置信息有哪些呢？第一个就是阿波罗服务地址，我们来看一看阿波罗服务地址，无非就是阿波罗的点儿 portal 我们要访问的是portal ，直接 portal 点儿 uil 等于什么呢？等于 HT DP 冒号儿杠 192 点儿 168 点儿 11 对不对？然后 8070 是不是这是我们的 portal 地址？那首先我们的 dashboard 要访问阿波罗，所以说一定要指定这个 portal 的地址是什么。然后接下来你要做的是一个比较复杂的对应关系。我为什么说它是比较复杂的对应关系呢？我们在这里起个名字，咱们叫做阿波罗点 portal 既然都叫 portal 我们都以及开头。点儿 App name config list config list 可以吧，然后它是一个 list 列表，我们可以说 list 0，然后这是代表什么意思？当然它是 u8 的，我们把它去掉，然后 save u8 就是说我们要配置一些规则，这个关系我在这儿先写好，让小伙伴们后面自己去看一下。就是说我们最开始有一个应用服务名称，然后我用冒号分隔，阿波罗的 token 是什么，然后再用冒号分隔，你看我自己的写法。然后接下来我说阿波罗的应用 ID 是什么？ App ID 是吧，然后还有什么阿波罗的色的ID 。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/89ec337f-3817-405d-8e42-aa1405a9c15c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662AEAW2IP%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGIyBchkhWbjf%2B4pDgeWoCzM8Yy5wXi9pwAsVrZaRE4YAiEA%2F0FBXCmaXtPGaKvOV6stv%2F5e6meb%2FzR1b7g%2Bqw5PHhUqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGf6kE5i0gdF3f8NJircA4ZGhidl4bQxbx4BAEHMhSZZhvBKSd2jkGXePQt6iJ97uT80Kx3r%2FPvvglIpRnzamjE39LDh7dChJaTwToL6EMEh4G0KYRBqYasHGoGsX7KfrIlsh4XhBJklW5ZPI4tAki9jXT3AApf3xwOrSMchnISBB3ExUSdbl0ldnZaHnRWjGUFVUIqJw4UDhuVFPcCxSfZVKu9IHIOFduy6dq7V1gJyOzvbbAs5FeHDfh8%2BeP3U2vs%2BPxI2f5Ezq4HHIXTYtyPVsMYtrJ95myt9bS7m1Xp6cDiEg8jyfibcBd7mGwtKNSPZBj7FWyjbF5EPlOVAOrBXt6lC28lb6m57ezg17s2pF6H6BObUW%2B7uzzQmurwrocvwN%2FPsdZkK3UjyEzEyenyk9tg2tD4QwMm%2BkCZRpCZOLoCfoLTrHx1QB7zQHtQAdVtfgQnLCxIuF99Ex4VYAqrk%2BK5Z0Kk7K2woDg%2B3qxcHMrzFUSa8dDyVxQ0ehtqNKSIr8qxdbd%2Bylhkxw4I9ZmH7yx9HvFCVMDGHgmorGwi2h%2BttkluwTKEt51MxrkG8gXjaaNVrhhJA%2BRy2b64aEX7S9fnFdBzm%2BDdmygEGsAPii8EBpfXrMiIwcGnmUmQjGd9x6QCor5ghNXslMPK3%2F9IGOqUBiv94agjdOpLQn0xQic%2FTEE2iSqdmyL43Y5xvOziBlpcTl6rOL27E09dZvgHvI72xGnC%2F0oNXzTXAzue2yLUksFoA%2B3tvTtuwgdIWccNLkaJi%2FTiWqyYVkw5GGO5Iyqq2tTfZ5ni%2BgLgldFcaFLLlOraR0qOz8QpmKw38ePktQED7HQedGAW5r0nSjOIkWa63mmuk5bxyEn%2BVlF%2FBSktSBJd%2B0wjE&X-Amz-Signature=b6cdf88f33260dbe913c28381252994ff110b10db6c119becd2a9eaf4722a005&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


当然自然 D 可能我们在这里面没有用上，不过我们也把它存起来，万一说后面会用就是第三方的 ID 我们现在就是这个 list 列表里边存的这个怎么 put 读取一个 release 很简单对吧？它要存的内容是什么呢？首先第一个就是应用服务的名称是什么？就是说我们被管理的我们的 dashboard 被管理哪个服务之前我们上节课已经做了授权了，但是我们那次授权的服务是谁呢？是这个叫做阿波罗 test 所以说对应着对不对？这个服务 run ADS 它要启动的时候肯定需要连我们的 dashboard 那我们现在把它简单去做一下，就之前我们是用 demo 去连的，然后现在我们改一下，把这个配置拿过来就好了，把这个配置 copy 过来，然后把它关掉。然后现在后面因为我们这个做授权了，所以说我们就用它 config 去改它的 config 配置就不是 demo 了，是这个 upload test 然后找到 arguments 然后 A 粘过来。


然后这个名字是阿波罗 test 对不对？我们写好阿波罗杠 test 然后端口号是个 8719 无所谓了。然后这个一定要是连阿波罗的地址 local house 杠巴拉巴拉你就可以找到，然后把它 play 好了，我们就不 run 了不启动。好。那我问你现在我们阿波罗 test 要跟 dashboard 做集成对不对？那我现在这个 App 应用名称是什么呢？ App 服务的英文名称不就是阿波罗杠test ，是不是就是我们当前这个服务对吧？然后我说我用冒号去分隔，接下来 token 是什么？ token 我们是不是已经申请好了。
第三方的 token 我们回到浏览器，因为我们之前授权的就是它我们第三方应用我们找到它，我们第三方应用名称叫做阿波罗，这个我能记住是不是。然后杠 test 杠 third 查询。那这个 token 都有这个 token ctrl C 粘过来放到后面。


第一个表示应用服务的名字，第二个表示它的阿波罗所对应的 token 第三个，它的 App ID 是什么？它的 App ID 也叫阿波罗杠 test 为什么呢？因为我们之前看到了在这里配置死了对不对？它的 App ID 跟项目名称保持一致，也叫阿波罗杠 test OK 然后最后一个它的色的 ID 是什么呢？色也是冒号风格的色 ID 我们都知道，刚才我们都记住了，就是 test 杠色的。 OK 保存好了，现在我们就以这个为组合，我们去当成一个服务列表。那以后比如说你的服务有了多个应用的配置，那你就可以配置多个，因为这是一个list 。接下来我们看一看还有哪些必须要配的东西。比如说它的环境是什么？环境就是我们自己的这个应用环境，默认我们都是用DEV ，就是所属环境默认就是 DEV 我其实不写它默认就是 DEV 我写什么阿波罗点 portal 第二 ENV 是不是默认 DEV 可以吧。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e1e156e7-46b8-40fe-886f-713408623d64/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662AEAW2IP%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGIyBchkhWbjf%2B4pDgeWoCzM8Yy5wXi9pwAsVrZaRE4YAiEA%2F0FBXCmaXtPGaKvOV6stv%2F5e6meb%2FzR1b7g%2Bqw5PHhUqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGf6kE5i0gdF3f8NJircA4ZGhidl4bQxbx4BAEHMhSZZhvBKSd2jkGXePQt6iJ97uT80Kx3r%2FPvvglIpRnzamjE39LDh7dChJaTwToL6EMEh4G0KYRBqYasHGoGsX7KfrIlsh4XhBJklW5ZPI4tAki9jXT3AApf3xwOrSMchnISBB3ExUSdbl0ldnZaHnRWjGUFVUIqJw4UDhuVFPcCxSfZVKu9IHIOFduy6dq7V1gJyOzvbbAs5FeHDfh8%2BeP3U2vs%2BPxI2f5Ezq4HHIXTYtyPVsMYtrJ95myt9bS7m1Xp6cDiEg8jyfibcBd7mGwtKNSPZBj7FWyjbF5EPlOVAOrBXt6lC28lb6m57ezg17s2pF6H6BObUW%2B7uzzQmurwrocvwN%2FPsdZkK3UjyEzEyenyk9tg2tD4QwMm%2BkCZRpCZOLoCfoLTrHx1QB7zQHtQAdVtfgQnLCxIuF99Ex4VYAqrk%2BK5Z0Kk7K2woDg%2B3qxcHMrzFUSa8dDyVxQ0ehtqNKSIr8qxdbd%2Bylhkxw4I9ZmH7yx9HvFCVMDGHgmorGwi2h%2BttkluwTKEt51MxrkG8gXjaaNVrhhJA%2BRy2b64aEX7S9fnFdBzm%2BDdmygEGsAPii8EBpfXrMiIwcGnmUmQjGd9x6QCor5ghNXslMPK3%2F9IGOqUBiv94agjdOpLQn0xQic%2FTEE2iSqdmyL43Y5xvOziBlpcTl6rOL27E09dZvgHvI72xGnC%2F0oNXzTXAzue2yLUksFoA%2B3tvTtuwgdIWccNLkaJi%2FTiWqyYVkw5GGO5Iyqq2tTfZ5ni%2BgLgldFcaFLLlOraR0qOz8QpmKw38ePktQED7HQedGAW5r0nSjOIkWa63mmuk5bxyEn%2BVlF%2FBSktSBJd%2B0wjE&X-Amz-Signature=b72c9e33855411913147f6886f9330bcc4a5cbc02296f52fe877c6b5f75e5034&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

好了，加完这个配置之后还有哪些？首先你阿波罗的管理员是什么角色？管理用户，可能你自己第三方应用的时候，你的管理用户你可以自己再申请一个，这都可以，但是我们现在没有申请它的 user ID 目前这些都是我自己定义的，目前就是叫阿波罗。然后这个密码其实你先不用添，然后接下来它的集群是什么？就是后面我们可以去做指定，比如说集群名称，阿波罗点儿 cluster namecluster name 是不是我们可以默认它默认官方默认它叫 default 好，然后还有配置。


好，我把这个就缩进一下，让大家能看清楚，就是有一些对应的配置我们都要配置好。还有就是它所属的 namespace 工作空间。 namespace 工作空间是什么？那就是阿波罗点儿 namespace 就可以了。当然你可以大写首字母大写，默认是什么？ namespace 默认就是application。


Ok. 好了，现在我已经把这个配置配置好了，唯一比较复杂的就是我们这个东西要对应上这么多，因为我要知道服务的名称，要知道它的 token 要知道什么 appid 还要知道 third ID 其实你有了这些配置，接下来的事情就是你自己要写一个 configuration 去解析这些配置，然后放到对应的集合中，你通过这几个配置我就能去创建我们自己的这个阿波罗的这个client 。说白了，阿波罗的 Open API 肯定也需要依赖于 client 因为它是 HTTP 请求。


好了，那我们来看看怎么去做这几个配置，我们现在有了。那接下来，因为我自己 fork 出来的分支，所以说我直接可以在这基础上去做修改。然后这里边有一个 ruler 是不是你看到这些 ruler 的规则， dynamic ruler 它是 interface 我们最后后面写的东西肯定是要实现这个接口，然后重写这个 publish 跟什么，跟这个 get rules 跟 publish 的方法就好了。


好了，那我们暂时在这块再起一个新的包，撸了点阿波罗可以吧，再起一个新的包对吧。这是关专门针对于阿波罗的。然后我们现在建一个普通的 Java 的 class 去解析这个配置叫做阿波罗config 。 OK 建立好了它以后，让我们怎么去写，我们来看一看这个东西的写法。


首先我们要把我们自己的这个数据什么的都要解析好。那第一件事情是要 at configuration 因为它是一个 spring boot 工程，你可以认为它是一个 spring 然后我们要解析的内容就是 configuration on properties ，有一个 configuration properties 在这里。那我们其实指定的去解析的就是 application.practice 了。然后我们指定一个 prefix prefix 就是我要把里边所有的以阿波罗点 portal portal 为前缀的属性我都要解析，因为我们之前所配置的都是阿波罗点 portal 那以这个前缀的后面的属性我都需要做一个解析。然后接下来我们去扫描一下，因为你又加了一个额外的扫描，所以说你要做一个 component scan 扫描指定的一个包。我们自己的包就是我们刚才所建的那个包，就是我把它复制出来 ctrl C 然后点星我要去扫描这个包下面所有的类，让它把它注入到 supreme 搞定完这个事情之后，我们来看一看我们接下来应该怎么去做。


接下来的做法无非就是我们要声明几个，要运用这个成员变量，用纯变量去接受一下。比如说 uil 因为这个 uil 其实说白了就是我们自己阿波罗点 portal.uil 我们看到了是不是阿波罗点 portal.uil 然后还有 application list 还有什么ENV ， user ID 还有 class name 包括 name space 。 OK 好，我们一个个去写。然后第二个是什么呢？Application. App list 是吧。 private 是 list 然后 string 然后在这里叫 AE PP 一定要保持一致，要不然它不解析。然后在这里你一定要事先把它拗出来，拗一个 release 搞定。


搞定完这个事情之后，接下来我们再看属性还有 user ID 什么的对吧。 privater string 类型的。比如说 user ID 因为我默认已经写好了，写死了他是阿波罗是吧。所以说其实我们可以有一些静态常量的配置，比如说我们给他一些静态的常量 public static string 比如说它的 user ID 默认我就你配置不配，是不是你就不配我默认也是阿波罗，我们在这里把它写得完善一点。好，你配置你不配，我默认也是给他，叫做等于阿波罗是吧。


还有什么呢？比如说环境，我们来写一下，我们都写上 ENV 默认的是 DEV 环境的。然后还有哪些？比如说 cluster name 默认是什么？是 default 还记得，cluster name 默认叫做 default 还有一个就是 namespace 默认是 application 对吧，static默认 name 是 pace 默认是 application 好啦，然后把这个东西转大写搞定，那我们来加一加。有了这个之后我们就可以加进来，我就懒得写了。 private 然后这个是 ENV 然后等于我们的 ENV 是吧，这是默认的，假设你配置里不配我给你，然后还有什么呢？还有 cluster name 是不是 cluster name 默认就是这个 default 然后还有 private string 的 name space 叫 name space namespace 默认也是叫做 application 你不配为给你。 OK 好了，这是我们最基本的几个属性搞定了。


接下来像我们这些最关键的就是这个 list 这个 list 我们应该怎么去解析呢？我们肯定是以，冒号去解析，我们应该怎么去存呢？在这里老师给出三组存放的规则，这个代码我就不写了，我直接粘过来，大家一起看，我们给出三个集合来存储 application config list 里面所对应的那个内容，我们直接粘过来，然后 ctrl CPO 倒进来。
好，我们来看一看，看看老师怎么做的，我说我声明成 volatile volletail 就是纪实感知。然后我说 App ID 就是你的 App ID 和色带 ID 做一组映射关系，一个 App ID 肯定对应着一个色带ID ，然后我用一个 map 把它存出来叫做 third map 它是一个 concard map 对吧？这是第一组，第二组就是你的应用服务名称 application nameapplication name 是什么呢？说白了， application name 就是我们最开始的这个阿波罗杠 test 因为它最开始就是表示应用服务名称，然后我们怎么去存储呢？我说 application name 一个 application name 也对应着一个 App ID 一个 application name 还对应一个 token 对吧，你的一个服务里边肯定有具体的一个 token 因为它的授权是一对一的关系。


好了，我现在用这个三个 map 来承装对应的键值。对，那接下来的事情就是我把它怎么去按照冒号分隔解析，然后放到这三个 map 里的事情了。很简单，怎么去做？我们接下来比如说先去让它这个类去实现一个接口，比如说实现一个 init Lisa bin 这样的话，在它初始化完了之后，我们就可以去调用它的方法我们直接实现这个叫做 after property site 这个方法。好，那我们来看看这个方法怎么去写，无非就是做一个解析。


首先阿波罗 config 里边这都是默认的参数，那我们怎么去做呢？静态的默认参数我们直接可以去点了，我说直接先赋值 ENV 默认值等于 ENV 是吧，这个我不知道小伙伴们能不能看懂。假设说我们最开始初始化的时候给他 ENV 是这个 ENV 但是你的 ENV 如果配置其他的是不是它这个属性就会被覆盖。


当然你要写一下这个 get set 方法，我们要写一下这个 get set 方法，把所有的除了静态的我们都给它加上 get set 方法。就是比如说这几个小写的加上 get set 方法。 Ok generate. 好了，保存一下 get set 方法都生成完了之后。然后对于它我们要重新设置一下。还有哪些呢？比如说这几个静态常量我们都要重新设置一下。比如 user ID 我们要重新给一个 user ID 你如果配置文件里配了那个 user ID 是什么，我再重新赋一下值。然后比如说 class name 也是一样的，等于对应的 class name 还有就是我们的 namespace 要重新配一下这个 namespace 还有就是 uil.uil uil 是没配吗？那我们少写了一个，也加上。因为后面我们可以通过静态的属性直接取到。那默认我给它一个空值，比如说 public static string 然后就叫做 UL 然后等于一个空，默认是空的对吧。 OK 好，它这个大小写肯定是区分的对不对？Java 。


那接下来我们有了这个 URL 之后，我们也要把这个 URL 赋一下值，就赋给对应的 URL 这样好了，搞定这几个配置是最基础的，都搞定了，剩下的就是比较复杂的。那你就直接取出来。比如说我们 days 点这个 list 然后点负一尺，当然你要判断它是否为空，那我在这里就不判断了取出来之后每一项是不是就是每一个 item 项，然后去做循环遍历，怎么去遍历呢？比如说取到我们用一个 item 思表示它是一个 string 的数组，陆续把它按照那个我们自己所规定的那个 split 按照冒号去分隔开。为什么它是一个集合？因为什么呢？因为它有多个，因为它是这个第两个，它还有第一个第二个。所以说我们就是把每一个长的字符串用冒号拼接的一个字符串，我去把它按照冒号再截出来，结束了。


取到这个 item 对吧，取到 item 我们直接可以知道 item 1 是什么。 item1 就是 application name 对吧，就等于 item 40，它是最开始的。然后我再 copy 两份三份四份一共 4 个。对不对？然后这是1，这是2，这是3。然后 2 应该就是我们的token 。我记得没错的话，3就是我们的 App id4 是色的 ID 是吧，我们来写一写色的 ID 好了，这几项我们都有了，然后无非就是往对应的 map 里面去装就好了。一个是 third map 一个是 App map 还有一个 token map 很简单，那我们就吃一个一个去装。我说跟这个 third map.put if set 如果存在就不 put 了。然后我要存什么内容？ third map 里边存的是我们的 App ID 跟 third ID 对吧，我们来看一眼 third map 就是第一个 App ID 跟 third ID 好了， App ID 对应的一个 third ID 扩得进去。然后还有什么？比如说 token map.put if set 然后这个里面存的是什么？存的是 token 吗？对应的就是 token 对不对？然后还有一个就是叫做这个 put if set 还有一个叫做 App map 。我记得是， App ID map 它是对应的是 application 以及 App ID 好了，那这个很简单，我们再加进来。第二 put if set upset 好，那这个就是我们对应的 application name 以及 App ID 所对应的一个集合。


好了，这样 put 完了之后就 OK 了，再加个判断，说如果 if 什么 items.lens 等于 4 的话才进来，万一那个搞错了，当然我在这里就不详细的去搞太复杂的这个太正规的认证了，因为大家都明白是吧，你等于 4 就证明确实你有三个冒号，然后去分隔的，然后再进来。剩下的其他情况，比如说你 else 你不等于4，你抛个异常或者怎么样都可以。
好了，现在我已经搞定了，相当于已经解析完了我们对应的 practice 然后在这里老师再加一个额外的东西，我们直接放到这。好，粘过来之后 ctrl shift 加 O 然后我们用的是 convert 用的是谁用的是这个哨兵的convert 。好保存一下。


好，同学们，请看我现在做了什么事情，我现在加了好多个 bin 因为它是一个什么？它是一个 configuration 所以说我可以初始化 bin 其实我是想把一些规则序列化这些东西我都直接注入到这个 bin 里了。如果你是一个 follow ruler 这个 entity 就是一个流控的规则的集合实体，对不对？然后你怎么去转成Jason ，我就直接这么去转成 Jason 就是 Jason 跟我们的实体内的一个转换。当然这是流控的。


下面这里面还有认证的我们就先要流控的，这个认证的我们先去掉，然后这是什么？这是 degree 的降级的我们先留着，然后系统的我们选择要或者不要都会有，后面你自己去加就好了。我现在在这里只是跟大家把这个整个的内容搞定。我们先用两个，一个是对于流量控制的 entity 跟他的这个字符串的一个转换的一个 bin 还有他们相互转换的一个 bin 保留在这里一个 encoder 一个 decoder 然后降级的也是一个 encoder 一个 decoder 其他的先不加。好了，OK现在我关于这个 config 这个类已经完全搞定了，然后其他的不要的。 ctrl 是不是叫 O 保存一下。



```java
package com.alibaba.csp.sentinel.dashboard.rule.apollo;

import com.alibaba.csp.sentinel.dashboard.datasource.entity.rule.*;
import com.alibaba.csp.sentinel.datasource.Converter;
import com.alibaba.fastjson.JSON;
import org.springframework.beans.factory.BeanFactoryAware;
import org.springframework.beans.factory.InitializingBean;
import org.springframework.boot.context.properties.ConfigurationProperties;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ConcurrentHashMap;

/**
 * <h1></h1>
 */
@Configuration
@ConfigurationProperties(prefix = "apollo.portal")
@ComponentScan("com.alibaba.csp.sentinel.dashboard.rule.apollo")
public class ApolloConfig implements InitializingBean {
    // 如果不配置我就给你一些默认的就行了
    public static String USERID = "apollo";

    public static String ENV = "DEV";

    public static String CLUSTERNAME = "default";

    public static String NAMESPACE = "application";

    private static String URL = "";

    private String url;

    private List<String> appNameConfigList = new ArrayList<>();

    private String userId;

    private String env = ENV;

    private String clusterName = CLUSTERNAME;

    private String nameSpace = NAMESPACE;

    private static volatile ConcurrentHashMap<String /** appId */, String /** thirdId */> thirdIdMap = new ConcurrentHashMap<>();

    private static volatile ConcurrentHashMap<String /** applicationName */, String /** appId */> appIdMap = new ConcurrentHashMap<>();

    private static volatile ConcurrentHashMap<String /** applicationName */, String /** token */> tokenMap = new ConcurrentHashMap<>();


    /**
     * Invoked by the containing {@code BeanFactory} after it has set all bean properties
     * and satisfied {@link BeanFactoryAware}, {@code ApplicationContextAware} etc.
     * <p>This method allows the bean instance to perform validation of its overall
     * configuration and final initialization when all bean properties have been set.
     *
     * @throws Exception in the event of misconfiguration (such as failure to set an
     *                   essential property) or if initialization fails for any other reason
     */
    @Override
    public void afterPropertiesSet() throws Exception {
        ApolloConfig.ENV = env;
        ApolloConfig.USERID = userId;
        ApolloConfig.CLUSTERNAME = clusterName;
        ApolloConfig.NAMESPACE = nameSpace;
        ApolloConfig.URL = url;

        this.appNameConfigList.forEach(item -> {
            String[] items = item.split(":");
            String applicationName = items[0];
            if (items.length == 4) {
                String token = items[1];
                String appId = items[2];
                String thirdId = items[3];

                thirdIdMap.putIfAbsent(appId, thirdId);
                tokenMap.putIfAbsent(applicationName, token);
                appIdMap.putIfAbsent(applicationName, appId);
            }
        });
    }

    @Bean
    public Converter<List<FlowRuleEntity>, String> flowRuleEntityEncoder() {
        return JSON :: toJSONString;
    }

    @Bean
    public Converter< String, List<FlowRuleEntity>> flowRuleEntityDecoder() {
        return s -> JSON.parseArray(s, FlowRuleEntity.class);
    }

    @Bean
    public Converter<List<AuthorityRuleEntity>, String> authorityRuleEntityDecoder() {
        return JSON :: toJSONString;
    }


    @Bean
    public Converter<String, List<AuthorityRuleEntity>> authorityRuleEntityEncoder() {
        return s -> JSON.parseArray(s, AuthorityRuleEntity.class);
    }

    @Bean
    public Converter<List<DegradeRuleEntity>, String> degradeRuleEntityDecoder() {
        return JSON :: toJSONString;
    }

    @Bean
    public Converter<String, List<DegradeRuleEntity>> degradeRuleEntityEncoder() {
        return s -> JSON.parseArray(s, DegradeRuleEntity.class);
    }


    @Bean
    public Converter<List<SystemRuleEntity> ,String> systemRuleEntityDecode() {
        return JSON :: toJSONString;
    }

    @Bean
    public Converter<String ,List<SystemRuleEntity>> systemRuleEntityEncode() {
        return s -> JSON.parseArray(s, SystemRuleEntity.class);
    }
    @Bean
    public Converter<List<ParamFlowRuleEntity>, String> ParamFlowRuleEntityDecode() {
        return JSON :: toJSONString;
    }

    @Bean
    public Converter<String, List<ParamFlowRuleEntity>> ParamFlowRuleEntityEncode() {
        return s -> JSON.parseArray(s, ParamFlowRuleEntity.class);
    }

    public String getURL() {
        return URL;
    }

    public void setURL(String URL) {
        this.URL = URL;
    }

    public static String getUSERID() {
        return USERID;
    }

    public static void setUSERID(String USERID) {
        ApolloConfig.USERID = USERID;
    }

    public static String getENV() {
        return ENV;
    }

    public static void setENV(String ENV) {
        ApolloConfig.ENV = ENV;
    }

    public static String getCLUSTERNAME() {
        return CLUSTERNAME;
    }

    public static void setCLUSTERNAME(String CLUSTERNAME) {
        ApolloConfig.CLUSTERNAME = CLUSTERNAME;
    }

    public static String getNAMESPACE() {
        return NAMESPACE;
    }

    public static void setNAMESPACE(String NAMESPACE) {
        ApolloConfig.NAMESPACE = NAMESPACE;
    }

    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }

    public List<String> getAppNameConfigList() {
        return appNameConfigList;
    }

    public void setAppNameConfigList(List<String> appNameConfigList) {
        this.appNameConfigList = appNameConfigList;
    }

    public String getUserId() {
        return userId;
    }

    public void setUserId(String userId) {
        this.userId = userId;
    }

    public String getEnv() {
        return env;
    }

    public void setEnv(String env) {
        this.env = env;
    }

    public String getClusterName() {
        return clusterName;
    }

    public void setClusterName(String clusterName) {
        this.clusterName = clusterName;
    }

    public String getNameSpace() {
        return nameSpace;
    }

    public void setNameSpace(String nameSpace) {
        this.nameSpace = nameSpace;
    }

    public static ConcurrentHashMap<String, String> getThirdIdMap() {
        return thirdIdMap;
    }

    public static void setThirdIdMap(ConcurrentHashMap<String, String> thirdIdMap) {
        ApolloConfig.thirdIdMap = thirdIdMap;
    }

    public static ConcurrentHashMap<String, String> getAppIdMap() {
        return appIdMap;
    }

    public static void setAppIdMap(ConcurrentHashMap<String, String> appIdMap) {
        ApolloConfig.appIdMap = appIdMap;
    }

    public static ConcurrentHashMap<String, String> getTokenMap() {
        return tokenMap;
    }

    public static void setTokenMap(ConcurrentHashMap<String, String> tokenMap) {
        ApolloConfig.tokenMap = tokenMap;
    }
}
```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/6215c549-f96b-4a5c-a1e8-0a6d8b5435ff/AwesomeScreenshot-www-apolloconfig--2023-04-16_6_01_part1.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662AEAW2IP%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGIyBchkhWbjf%2B4pDgeWoCzM8Yy5wXi9pwAsVrZaRE4YAiEA%2F0FBXCmaXtPGaKvOV6stv%2F5e6meb%2FzR1b7g%2Bqw5PHhUqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGf6kE5i0gdF3f8NJircA4ZGhidl4bQxbx4BAEHMhSZZhvBKSd2jkGXePQt6iJ97uT80Kx3r%2FPvvglIpRnzamjE39LDh7dChJaTwToL6EMEh4G0KYRBqYasHGoGsX7KfrIlsh4XhBJklW5ZPI4tAki9jXT3AApf3xwOrSMchnISBB3ExUSdbl0ldnZaHnRWjGUFVUIqJw4UDhuVFPcCxSfZVKu9IHIOFduy6dq7V1gJyOzvbbAs5FeHDfh8%2BeP3U2vs%2BPxI2f5Ezq4HHIXTYtyPVsMYtrJ95myt9bS7m1Xp6cDiEg8jyfibcBd7mGwtKNSPZBj7FWyjbF5EPlOVAOrBXt6lC28lb6m57ezg17s2pF6H6BObUW%2B7uzzQmurwrocvwN%2FPsdZkK3UjyEzEyenyk9tg2tD4QwMm%2BkCZRpCZOLoCfoLTrHx1QB7zQHtQAdVtfgQnLCxIuF99Ex4VYAqrk%2BK5Z0Kk7K2woDg%2B3qxcHMrzFUSa8dDyVxQ0ehtqNKSIr8qxdbd%2Bylhkxw4I9ZmH7yx9HvFCVMDGHgmorGwi2h%2BttkluwTKEt51MxrkG8gXjaaNVrhhJA%2BRy2b64aEX7S9fnFdBzm%2BDdmygEGsAPii8EBpfXrMiIwcGnmUmQjGd9x6QCor5ghNXslMPK3%2F9IGOqUBiv94agjdOpLQn0xQic%2FTEE2iSqdmyL43Y5xvOziBlpcTl6rOL27E09dZvgHvI72xGnC%2F0oNXzTXAzue2yLUksFoA%2B3tvTtuwgdIWccNLkaJi%2FTiWqyYVkw5GGO5Iyqq2tTfZ5ni%2BgLgldFcaFLLlOraR0qOz8QpmKw38ePktQED7HQedGAW5r0nSjOIkWa63mmuk5bxyEn%2BVlF%2FBSktSBJd%2B0wjE&X-Amz-Signature=95b749c35b6b31bbbd2248ec034507a9fe720c84dd6c9549d956070bdb8f00ff&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/90e5a598-8a3e-439c-acc0-c4908f8238da/AwesomeScreenshot-www-apolloconfig--2023-04-16_6_01_part2.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4662AEAW2IP%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225845Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGIyBchkhWbjf%2B4pDgeWoCzM8Yy5wXi9pwAsVrZaRE4YAiEA%2F0FBXCmaXtPGaKvOV6stv%2F5e6meb%2FzR1b7g%2Bqw5PHhUqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGf6kE5i0gdF3f8NJircA4ZGhidl4bQxbx4BAEHMhSZZhvBKSd2jkGXePQt6iJ97uT80Kx3r%2FPvvglIpRnzamjE39LDh7dChJaTwToL6EMEh4G0KYRBqYasHGoGsX7KfrIlsh4XhBJklW5ZPI4tAki9jXT3AApf3xwOrSMchnISBB3ExUSdbl0ldnZaHnRWjGUFVUIqJw4UDhuVFPcCxSfZVKu9IHIOFduy6dq7V1gJyOzvbbAs5FeHDfh8%2BeP3U2vs%2BPxI2f5Ezq4HHIXTYtyPVsMYtrJ95myt9bS7m1Xp6cDiEg8jyfibcBd7mGwtKNSPZBj7FWyjbF5EPlOVAOrBXt6lC28lb6m57ezg17s2pF6H6BObUW%2B7uzzQmurwrocvwN%2FPsdZkK3UjyEzEyenyk9tg2tD4QwMm%2BkCZRpCZOLoCfoLTrHx1QB7zQHtQAdVtfgQnLCxIuF99Ex4VYAqrk%2BK5Z0Kk7K2woDg%2B3qxcHMrzFUSa8dDyVxQ0ehtqNKSIr8qxdbd%2Bylhkxw4I9ZmH7yx9HvFCVMDGHgmorGwi2h%2BttkluwTKEt51MxrkG8gXjaaNVrhhJA%2BRy2b64aEX7S9fnFdBzm%2BDdmygEGsAPii8EBpfXrMiIwcGnmUmQjGd9x6QCor5ghNXslMPK3%2F9IGOqUBiv94agjdOpLQn0xQic%2FTEE2iSqdmyL43Y5xvOziBlpcTl6rOL27E09dZvgHvI72xGnC%2F0oNXzTXAzue2yLUksFoA%2B3tvTtuwgdIWccNLkaJi%2FTiWqyYVkw5GGO5Iyqq2tTfZ5ni%2BgLgldFcaFLLlOraR0qOz8QpmKw38ePktQED7HQedGAW5r0nSjOIkWa63mmuk5bxyEn%2BVlF%2FBSktSBJd%2B0wjE&X-Amz-Signature=bc0ed89edaf65f39b07f280ef65b7534986860d249776c8766c4b89eecfd9243&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)







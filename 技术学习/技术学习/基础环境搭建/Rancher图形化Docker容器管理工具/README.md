---
title: Rancher图形化Docker容器管理工具
---

# Rancher图形化Docker容器管理工具

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/beb36a04-c0ea-4c36-a04c-629fae8eeb41/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XTSUWJTB%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCiEcX%2BWw0CYm7csq33pKuZcgLde9Ajn5HT5SYK1d5IowIgC6TvnCYWZstfkhz1eq50r2Hhp85mTR0t%2BPO9aRm58bwqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFS1hr7OQEezACsbnSrcA2DVeqTUFXKKB9l%2BXYKu3FXCadXWD%2BuReO8Af3RaZACm13AVppKqv6kIuvbDWz6iQYnKgoLHXgBo9I0ee4aRFMH2z%2F8gbSiHh3LG1mVAN3aukNqI1LiPoJdMvGjEEjRtevaliUtXw7v98v3dTZKYowN4%2BU0opWnqxNipD97j0tPTwQwxG7GzDKoP%2FCtheoTNsBv70QUNj9FWbl4Ktw7K0F5XPaufQmtIJuCCWBC7JbK6Vr7WCwHr2jL6XpTTBrlKN%2BX8oKKTNAC265%2FJY2hIOAg8UsgsZ5iYtmkN2aUkxVvn%2FGKjx3OAy%2B4Ojh3OutOzLGv%2B6ZjdC1%2Ff0oeP5x0PJVGOl3KTlObPgtregppd8vyyhg8NB6WpyVtnZGIDQT2XlinxC2YlKPPktnWB3jitA8gCxjUnmm5XKQhPWZm7wzHGDwYkX3odR7VRR%2BXQifmw3DzLqeLA48xXh%2BKxsmWSYv%2F8Fs%2Bn%2FCFwQepGbZ0dbM8vuWSwOZAaGX5h6UwGDZKewL1M9vIQUCe48XzmfJXzIjOvZMXOfzhbz4iV1lOW%2BCWo8GIzhmgpYVKMC6z7Q4kFFgp4gGpgHfMnDuHbZNHt3rdigdcFNOqM7flXmzfEOYcq8JKZYEwnNUHpIiJ8MLW3%2F9IGOqUBXh47CuTGQyqYJW2wI8eotYzNIL9zTPiE8a52GjY5kVnDsIybh%2Bw63xZe8NggdUdAZrRk23E%2FeVALIv2CzD6Nw8xLguiSf31E1Xsu60P%2BBsOZkY1RPVjw1a%2FiajuMVJ91Js%2BBKlLBLYJuZmS2IXx39Isu9JyrEgnFC%2FbmCp3OHng3HsjsL0Kl%2BGLdFC1vXPuH%2FKVlaji6v1roUiRzUpUdKu8YUBA4&X-Amz-Signature=ecf82651d1cb3648167a43dcb4577074c194e7199b6c8a601b5ad2254e1f70fd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/6e15f8d2-b1fa-4874-b712-f9d950ddf31c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XTSUWJTB%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCiEcX%2BWw0CYm7csq33pKuZcgLde9Ajn5HT5SYK1d5IowIgC6TvnCYWZstfkhz1eq50r2Hhp85mTR0t%2BPO9aRm58bwqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFS1hr7OQEezACsbnSrcA2DVeqTUFXKKB9l%2BXYKu3FXCadXWD%2BuReO8Af3RaZACm13AVppKqv6kIuvbDWz6iQYnKgoLHXgBo9I0ee4aRFMH2z%2F8gbSiHh3LG1mVAN3aukNqI1LiPoJdMvGjEEjRtevaliUtXw7v98v3dTZKYowN4%2BU0opWnqxNipD97j0tPTwQwxG7GzDKoP%2FCtheoTNsBv70QUNj9FWbl4Ktw7K0F5XPaufQmtIJuCCWBC7JbK6Vr7WCwHr2jL6XpTTBrlKN%2BX8oKKTNAC265%2FJY2hIOAg8UsgsZ5iYtmkN2aUkxVvn%2FGKjx3OAy%2B4Ojh3OutOzLGv%2B6ZjdC1%2Ff0oeP5x0PJVGOl3KTlObPgtregppd8vyyhg8NB6WpyVtnZGIDQT2XlinxC2YlKPPktnWB3jitA8gCxjUnmm5XKQhPWZm7wzHGDwYkX3odR7VRR%2BXQifmw3DzLqeLA48xXh%2BKxsmWSYv%2F8Fs%2Bn%2FCFwQepGbZ0dbM8vuWSwOZAaGX5h6UwGDZKewL1M9vIQUCe48XzmfJXzIjOvZMXOfzhbz4iV1lOW%2BCWo8GIzhmgpYVKMC6z7Q4kFFgp4gGpgHfMnDuHbZNHt3rdigdcFNOqM7flXmzfEOYcq8JKZYEwnNUHpIiJ8MLW3%2F9IGOqUBXh47CuTGQyqYJW2wI8eotYzNIL9zTPiE8a52GjY5kVnDsIybh%2Bw63xZe8NggdUdAZrRk23E%2FeVALIv2CzD6Nw8xLguiSf31E1Xsu60P%2BBsOZkY1RPVjw1a%2FiajuMVJ91Js%2BBKlLBLYJuZmS2IXx39Isu9JyrEgnFC%2FbmCp3OHng3HsjsL0Kl%2BGLdFC1vXPuH%2FKVlaji6v1roUiRzUpUdKu8YUBA4&X-Amz-Signature=4e88e1af6bd29c238e066ccdb54d03cd4300dd783eac74b200e20d83563d55af&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


[https://www.rancher.com/quick-start](https://www.rancher.com/quick-start)

docker pull rancher/rancher:2.4.8-rc2-linux-arm64

[https://docs.rancher.cn/rancher2/](https://docs.rancher.cn/rancher2/)

```markdown
## 到 Dockerhub上去找  https://hub.docker.com/r/rancher/rancher/tags?page=4

K8S 1.2.4版本---------------->必须使用Rancher:v2.6.7的版本
docker pull rancher/rancher:v2.7-0229213f3a2074d2b842acdb609bc63428ab0fb9-linux-arm64
docker pull rancher/rancher:2.4.8-rc2-linux-arm64
## 
## 启动docker：systemctl start docker 
## 直接创建容器的方式

# docker run -di --restart=unless-stopped --restart=always --privileged -p 443:443 -p 8070:80 -v ~/rancher_home:/var/lib/rancher -v ~/rancher_home/auditlog:/var/log/auditlog --name=AveryRancher rancher/rancher:v2.7-0229213f3a2074d2b842acdb609bc63428ab0fb9-linux-arm64


# docker run -di --privileged --restart=always --name=rancher -p 9100:443 rancher/rancher:v2.6.7
 

 使用 rancher 创建 k8s 集群的举例
https://juejin.cn/post/6909720966134235143?searchId=2023111207015463CA726DF704AD4A86A7


然后根据提示执行获取临时密码的操作进去就可以活设置密码了
# docker logs  容器ID  2>&1 | grep "Bootstrap Password:"
# 访问地址： https://172.16.136.226:4444
# 用户名: admin. 密码：bNUzr6dGIIEbs5DM

# docker exec -ti <container_id> reset-password 设置查看密码（2.5.15版本不需要设置）
# 应该使用 https: + Ip + Port 会显示可以继续的提示 选择 “高级” 继续访问 登录进去了！！！！


2.4.5版本
# docker run -di --restart=unless-stopped --restart=always --privileged -p 2443:443 -p 2458:80 -v ~/rancher_home2.4.5:/var/lib/rancher -v ~/rancher_home2.4.5/auditlog:/var/log/auditlog --name=RancherServer rancher/rancher:v2.4.5
用户： admin   密码：admin
# https://172.16.136.226:2443


docker run -di --restart=unless-stopped --restart=always --privileged -p 1662:443 -p 1668:80 -v ~/rancher_home:/var/lib/rancher -v ~/rancher_home/auditlog:/var/log/auditlog --name=AveryRancher rancher/rancher:v1.6.21
```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/9ee9652b-eded-46de-b131-756f971d3f27/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XTSUWJTB%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCiEcX%2BWw0CYm7csq33pKuZcgLde9Ajn5HT5SYK1d5IowIgC6TvnCYWZstfkhz1eq50r2Hhp85mTR0t%2BPO9aRm58bwqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFS1hr7OQEezACsbnSrcA2DVeqTUFXKKB9l%2BXYKu3FXCadXWD%2BuReO8Af3RaZACm13AVppKqv6kIuvbDWz6iQYnKgoLHXgBo9I0ee4aRFMH2z%2F8gbSiHh3LG1mVAN3aukNqI1LiPoJdMvGjEEjRtevaliUtXw7v98v3dTZKYowN4%2BU0opWnqxNipD97j0tPTwQwxG7GzDKoP%2FCtheoTNsBv70QUNj9FWbl4Ktw7K0F5XPaufQmtIJuCCWBC7JbK6Vr7WCwHr2jL6XpTTBrlKN%2BX8oKKTNAC265%2FJY2hIOAg8UsgsZ5iYtmkN2aUkxVvn%2FGKjx3OAy%2B4Ojh3OutOzLGv%2B6ZjdC1%2Ff0oeP5x0PJVGOl3KTlObPgtregppd8vyyhg8NB6WpyVtnZGIDQT2XlinxC2YlKPPktnWB3jitA8gCxjUnmm5XKQhPWZm7wzHGDwYkX3odR7VRR%2BXQifmw3DzLqeLA48xXh%2BKxsmWSYv%2F8Fs%2Bn%2FCFwQepGbZ0dbM8vuWSwOZAaGX5h6UwGDZKewL1M9vIQUCe48XzmfJXzIjOvZMXOfzhbz4iV1lOW%2BCWo8GIzhmgpYVKMC6z7Q4kFFgp4gGpgHfMnDuHbZNHt3rdigdcFNOqM7flXmzfEOYcq8JKZYEwnNUHpIiJ8MLW3%2F9IGOqUBXh47CuTGQyqYJW2wI8eotYzNIL9zTPiE8a52GjY5kVnDsIybh%2Bw63xZe8NggdUdAZrRk23E%2FeVALIv2CzD6Nw8xLguiSf31E1Xsu60P%2BBsOZkY1RPVjw1a%2FiajuMVJ91Js%2BBKlLBLYJuZmS2IXx39Isu9JyrEgnFC%2FbmCp3OHng3HsjsL0Kl%2BGLdFC1vXPuH%2FKVlaji6v1roUiRzUpUdKu8YUBA4&X-Amz-Signature=5bcbdea2fdd7dd58d4765b068663b39733199974dba3a5e17b3b8da13db1ce5e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

> 💡 2.4.5版本的Rancher 用户名：admin    密码设置的是：admin
[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/04e34c0b-d752-4095-87a0-75649dfcdc93/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XTSUWJTB%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCiEcX%2BWw0CYm7csq33pKuZcgLde9Ajn5HT5SYK1d5IowIgC6TvnCYWZstfkhz1eq50r2Hhp85mTR0t%2BPO9aRm58bwqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFS1hr7OQEezACsbnSrcA2DVeqTUFXKKB9l%2BXYKu3FXCadXWD%2BuReO8Af3RaZACm13AVppKqv6kIuvbDWz6iQYnKgoLHXgBo9I0ee4aRFMH2z%2F8gbSiHh3LG1mVAN3aukNqI1LiPoJdMvGjEEjRtevaliUtXw7v98v3dTZKYowN4%2BU0opWnqxNipD97j0tPTwQwxG7GzDKoP%2FCtheoTNsBv70QUNj9FWbl4Ktw7K0F5XPaufQmtIJuCCWBC7JbK6Vr7WCwHr2jL6XpTTBrlKN%2BX8oKKTNAC265%2FJY2hIOAg8UsgsZ5iYtmkN2aUkxVvn%2FGKjx3OAy%2B4Ojh3OutOzLGv%2B6ZjdC1%2Ff0oeP5x0PJVGOl3KTlObPgtregppd8vyyhg8NB6WpyVtnZGIDQT2XlinxC2YlKPPktnWB3jitA8gCxjUnmm5XKQhPWZm7wzHGDwYkX3odR7VRR%2BXQifmw3DzLqeLA48xXh%2BKxsmWSYv%2F8Fs%2Bn%2FCFwQepGbZ0dbM8vuWSwOZAaGX5h6UwGDZKewL1M9vIQUCe48XzmfJXzIjOvZMXOfzhbz4iV1lOW%2BCWo8GIzhmgpYVKMC6z7Q4kFFgp4gGpgHfMnDuHbZNHt3rdigdcFNOqM7flXmzfEOYcq8JKZYEwnNUHpIiJ8MLW3%2F9IGOqUBXh47CuTGQyqYJW2wI8eotYzNIL9zTPiE8a52GjY5kVnDsIybh%2Bw63xZe8NggdUdAZrRk23E%2FeVALIv2CzD6Nw8xLguiSf31E1Xsu60P%2BBsOZkY1RPVjw1a%2FiajuMVJ91Js%2BBKlLBLYJuZmS2IXx39Isu9JyrEgnFC%2FbmCp3OHng3HsjsL0Kl%2BGLdFC1vXPuH%2FKVlaji6v1roUiRzUpUdKu8YUBA4&X-Amz-Signature=32e0df089b5faaf8111c96a035a9ce7e2d4747be3d63b347dac5e1b8181ba786&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

# 初始化-添加环境

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b3a2459e-5024-446c-830d-f3815ee80880/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XTSUWJTB%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCiEcX%2BWw0CYm7csq33pKuZcgLde9Ajn5HT5SYK1d5IowIgC6TvnCYWZstfkhz1eq50r2Hhp85mTR0t%2BPO9aRm58bwqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFS1hr7OQEezACsbnSrcA2DVeqTUFXKKB9l%2BXYKu3FXCadXWD%2BuReO8Af3RaZACm13AVppKqv6kIuvbDWz6iQYnKgoLHXgBo9I0ee4aRFMH2z%2F8gbSiHh3LG1mVAN3aukNqI1LiPoJdMvGjEEjRtevaliUtXw7v98v3dTZKYowN4%2BU0opWnqxNipD97j0tPTwQwxG7GzDKoP%2FCtheoTNsBv70QUNj9FWbl4Ktw7K0F5XPaufQmtIJuCCWBC7JbK6Vr7WCwHr2jL6XpTTBrlKN%2BX8oKKTNAC265%2FJY2hIOAg8UsgsZ5iYtmkN2aUkxVvn%2FGKjx3OAy%2B4Ojh3OutOzLGv%2B6ZjdC1%2Ff0oeP5x0PJVGOl3KTlObPgtregppd8vyyhg8NB6WpyVtnZGIDQT2XlinxC2YlKPPktnWB3jitA8gCxjUnmm5XKQhPWZm7wzHGDwYkX3odR7VRR%2BXQifmw3DzLqeLA48xXh%2BKxsmWSYv%2F8Fs%2Bn%2FCFwQepGbZ0dbM8vuWSwOZAaGX5h6UwGDZKewL1M9vIQUCe48XzmfJXzIjOvZMXOfzhbz4iV1lOW%2BCWo8GIzhmgpYVKMC6z7Q4kFFgp4gGpgHfMnDuHbZNHt3rdigdcFNOqM7flXmzfEOYcq8JKZYEwnNUHpIiJ8MLW3%2F9IGOqUBXh47CuTGQyqYJW2wI8eotYzNIL9zTPiE8a52GjY5kVnDsIybh%2Bw63xZe8NggdUdAZrRk23E%2FeVALIv2CzD6Nw8xLguiSf31E1Xsu60P%2BBsOZkY1RPVjw1a%2FiajuMVJ91Js%2BBKlLBLYJuZmS2IXx39Isu9JyrEgnFC%2FbmCp3OHng3HsjsL0Kl%2BGLdFC1vXPuH%2FKVlaji6v1roUiRzUpUdKu8YUBA4&X-Amz-Signature=1df25f4447ea17f7796ebd24d2a25bb4f4273f91b1da1ddff16508ae0184c8b8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```markdown
# 开发， 正式环境的添加后是能隔离开的

# 官放文档： https://docs.ranchermanager.rancher.io/
# 切换到中文文档：https://docs.ranchermanager.rancher.io/zh/pages-for-subheaders/deploy-rancher-manager

```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b2dd7ced-9ace-4a84-b74d-53144bf1906b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XTSUWJTB%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCiEcX%2BWw0CYm7csq33pKuZcgLde9Ajn5HT5SYK1d5IowIgC6TvnCYWZstfkhz1eq50r2Hhp85mTR0t%2BPO9aRm58bwqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFS1hr7OQEezACsbnSrcA2DVeqTUFXKKB9l%2BXYKu3FXCadXWD%2BuReO8Af3RaZACm13AVppKqv6kIuvbDWz6iQYnKgoLHXgBo9I0ee4aRFMH2z%2F8gbSiHh3LG1mVAN3aukNqI1LiPoJdMvGjEEjRtevaliUtXw7v98v3dTZKYowN4%2BU0opWnqxNipD97j0tPTwQwxG7GzDKoP%2FCtheoTNsBv70QUNj9FWbl4Ktw7K0F5XPaufQmtIJuCCWBC7JbK6Vr7WCwHr2jL6XpTTBrlKN%2BX8oKKTNAC265%2FJY2hIOAg8UsgsZ5iYtmkN2aUkxVvn%2FGKjx3OAy%2B4Ojh3OutOzLGv%2B6ZjdC1%2Ff0oeP5x0PJVGOl3KTlObPgtregppd8vyyhg8NB6WpyVtnZGIDQT2XlinxC2YlKPPktnWB3jitA8gCxjUnmm5XKQhPWZm7wzHGDwYkX3odR7VRR%2BXQifmw3DzLqeLA48xXh%2BKxsmWSYv%2F8Fs%2Bn%2FCFwQepGbZ0dbM8vuWSwOZAaGX5h6UwGDZKewL1M9vIQUCe48XzmfJXzIjOvZMXOfzhbz4iV1lOW%2BCWo8GIzhmgpYVKMC6z7Q4kFFgp4gGpgHfMnDuHbZNHt3rdigdcFNOqM7flXmzfEOYcq8JKZYEwnNUHpIiJ8MLW3%2F9IGOqUBXh47CuTGQyqYJW2wI8eotYzNIL9zTPiE8a52GjY5kVnDsIybh%2Bw63xZe8NggdUdAZrRk23E%2FeVALIv2CzD6Nw8xLguiSf31E1Xsu60P%2BBsOZkY1RPVjw1a%2FiajuMVJ91Js%2BBKlLBLYJuZmS2IXx39Isu9JyrEgnFC%2FbmCp3OHng3HsjsL0Kl%2BGLdFC1vXPuH%2FKVlaji6v1roUiRzUpUdKu8YUBA4&X-Amz-Signature=0998c069b276d5c60111ec978cbf8197addb89023bf2a7311f746b4a1d4c7e5c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/4ac25137-e1d2-4f79-a378-b099094ac227/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XTSUWJTB%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCiEcX%2BWw0CYm7csq33pKuZcgLde9Ajn5HT5SYK1d5IowIgC6TvnCYWZstfkhz1eq50r2Hhp85mTR0t%2BPO9aRm58bwqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFS1hr7OQEezACsbnSrcA2DVeqTUFXKKB9l%2BXYKu3FXCadXWD%2BuReO8Af3RaZACm13AVppKqv6kIuvbDWz6iQYnKgoLHXgBo9I0ee4aRFMH2z%2F8gbSiHh3LG1mVAN3aukNqI1LiPoJdMvGjEEjRtevaliUtXw7v98v3dTZKYowN4%2BU0opWnqxNipD97j0tPTwQwxG7GzDKoP%2FCtheoTNsBv70QUNj9FWbl4Ktw7K0F5XPaufQmtIJuCCWBC7JbK6Vr7WCwHr2jL6XpTTBrlKN%2BX8oKKTNAC265%2FJY2hIOAg8UsgsZ5iYtmkN2aUkxVvn%2FGKjx3OAy%2B4Ojh3OutOzLGv%2B6ZjdC1%2Ff0oeP5x0PJVGOl3KTlObPgtregppd8vyyhg8NB6WpyVtnZGIDQT2XlinxC2YlKPPktnWB3jitA8gCxjUnmm5XKQhPWZm7wzHGDwYkX3odR7VRR%2BXQifmw3DzLqeLA48xXh%2BKxsmWSYv%2F8Fs%2Bn%2FCFwQepGbZ0dbM8vuWSwOZAaGX5h6UwGDZKewL1M9vIQUCe48XzmfJXzIjOvZMXOfzhbz4iV1lOW%2BCWo8GIzhmgpYVKMC6z7Q4kFFgp4gGpgHfMnDuHbZNHt3rdigdcFNOqM7flXmzfEOYcq8JKZYEwnNUHpIiJ8MLW3%2F9IGOqUBXh47CuTGQyqYJW2wI8eotYzNIL9zTPiE8a52GjY5kVnDsIybh%2Bw63xZe8NggdUdAZrRk23E%2FeVALIv2CzD6Nw8xLguiSf31E1Xsu60P%2BBsOZkY1RPVjw1a%2FiajuMVJ91Js%2BBKlLBLYJuZmS2IXx39Isu9JyrEgnFC%2FbmCp3OHng3HsjsL0Kl%2BGLdFC1vXPuH%2FKVlaji6v1roUiRzUpUdKu8YUBA4&X-Amz-Signature=54773662e5ba2cc92aef117d0d4283abd3c0bfe78ee9a93fe3ba793b06a21d29&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


# Rancher部署微服务

```markdown
#1: 搭建私有仓库 registry 端口 5000
```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/278c809b-88e1-4cb4-a07a-fe8c75837960/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XTSUWJTB%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCiEcX%2BWw0CYm7csq33pKuZcgLde9Ajn5HT5SYK1d5IowIgC6TvnCYWZstfkhz1eq50r2Hhp85mTR0t%2BPO9aRm58bwqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFS1hr7OQEezACsbnSrcA2DVeqTUFXKKB9l%2BXYKu3FXCadXWD%2BuReO8Af3RaZACm13AVppKqv6kIuvbDWz6iQYnKgoLHXgBo9I0ee4aRFMH2z%2F8gbSiHh3LG1mVAN3aukNqI1LiPoJdMvGjEEjRtevaliUtXw7v98v3dTZKYowN4%2BU0opWnqxNipD97j0tPTwQwxG7GzDKoP%2FCtheoTNsBv70QUNj9FWbl4Ktw7K0F5XPaufQmtIJuCCWBC7JbK6Vr7WCwHr2jL6XpTTBrlKN%2BX8oKKTNAC265%2FJY2hIOAg8UsgsZ5iYtmkN2aUkxVvn%2FGKjx3OAy%2B4Ojh3OutOzLGv%2B6ZjdC1%2Ff0oeP5x0PJVGOl3KTlObPgtregppd8vyyhg8NB6WpyVtnZGIDQT2XlinxC2YlKPPktnWB3jitA8gCxjUnmm5XKQhPWZm7wzHGDwYkX3odR7VRR%2BXQifmw3DzLqeLA48xXh%2BKxsmWSYv%2F8Fs%2Bn%2FCFwQepGbZ0dbM8vuWSwOZAaGX5h6UwGDZKewL1M9vIQUCe48XzmfJXzIjOvZMXOfzhbz4iV1lOW%2BCWo8GIzhmgpYVKMC6z7Q4kFFgp4gGpgHfMnDuHbZNHt3rdigdcFNOqM7flXmzfEOYcq8JKZYEwnNUHpIiJ8MLW3%2F9IGOqUBXh47CuTGQyqYJW2wI8eotYzNIL9zTPiE8a52GjY5kVnDsIybh%2Bw63xZe8NggdUdAZrRk23E%2FeVALIv2CzD6Nw8xLguiSf31E1Xsu60P%2BBsOZkY1RPVjw1a%2FiajuMVJ91Js%2BBKlLBLYJuZmS2IXx39Isu9JyrEgnFC%2FbmCp3OHng3HsjsL0Kl%2BGLdFC1vXPuH%2FKVlaji6v1roUiRzUpUdKu8YUBA4&X-Amz-Signature=dbb002046463fb644917398de553d7e131777cb4cfec97acf99d70f49b4d17d8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/bf025151-d38d-47d2-8e02-3da9d04c2559/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XTSUWJTB%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCiEcX%2BWw0CYm7csq33pKuZcgLde9Ajn5HT5SYK1d5IowIgC6TvnCYWZstfkhz1eq50r2Hhp85mTR0t%2BPO9aRm58bwqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFS1hr7OQEezACsbnSrcA2DVeqTUFXKKB9l%2BXYKu3FXCadXWD%2BuReO8Af3RaZACm13AVppKqv6kIuvbDWz6iQYnKgoLHXgBo9I0ee4aRFMH2z%2F8gbSiHh3LG1mVAN3aukNqI1LiPoJdMvGjEEjRtevaliUtXw7v98v3dTZKYowN4%2BU0opWnqxNipD97j0tPTwQwxG7GzDKoP%2FCtheoTNsBv70QUNj9FWbl4Ktw7K0F5XPaufQmtIJuCCWBC7JbK6Vr7WCwHr2jL6XpTTBrlKN%2BX8oKKTNAC265%2FJY2hIOAg8UsgsZ5iYtmkN2aUkxVvn%2FGKjx3OAy%2B4Ojh3OutOzLGv%2B6ZjdC1%2Ff0oeP5x0PJVGOl3KTlObPgtregppd8vyyhg8NB6WpyVtnZGIDQT2XlinxC2YlKPPktnWB3jitA8gCxjUnmm5XKQhPWZm7wzHGDwYkX3odR7VRR%2BXQifmw3DzLqeLA48xXh%2BKxsmWSYv%2F8Fs%2Bn%2FCFwQepGbZ0dbM8vuWSwOZAaGX5h6UwGDZKewL1M9vIQUCe48XzmfJXzIjOvZMXOfzhbz4iV1lOW%2BCWo8GIzhmgpYVKMC6z7Q4kFFgp4gGpgHfMnDuHbZNHt3rdigdcFNOqM7flXmzfEOYcq8JKZYEwnNUHpIiJ8MLW3%2F9IGOqUBXh47CuTGQyqYJW2wI8eotYzNIL9zTPiE8a52GjY5kVnDsIybh%2Bw63xZe8NggdUdAZrRk23E%2FeVALIv2CzD6Nw8xLguiSf31E1Xsu60P%2BBsOZkY1RPVjw1a%2FiajuMVJ91Js%2BBKlLBLYJuZmS2IXx39Isu9JyrEgnFC%2FbmCp3OHng3HsjsL0Kl%2BGLdFC1vXPuH%2FKVlaji6v1roUiRzUpUdKu8YUBA4&X-Amz-Signature=874573896fa7c43d279583a5501497e9ba9a90f03a7322ce7089bcb8a6828f46&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```markdown
# 修改 docker服务配置：
# vi /lib/systemd/system/docker.service
# 加上 ExecStart=后面加
-H tcp://0.0.0.0:2375 -H unix:///var/run/docker.sock
#systemctl daemon-reload
#systemctl restart docker
#systemctl enable docker
#systemctl start registry 
#systemctl enable registry 
```

```markdown
# 部署微服务
由于这里我的rancher没有使用，是直接手动创建mysql的镜像作为生产环境的镜像
# docker run -di --name=AveryProMysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=guojun12 --restart=unless-stoped --restart=always  mysql


# 创建jdk1.8的（基于cnetos7）的镜像，搭建一个私有仓库，用于存放微服务运用的镜像



# 项目微服务中pom加入docker的mavne插件

<!-- Docker的Mavne插件： https://github.com/spotify/docker-maven-plugin#specify-build-info-in-the-pom   -->
<plugin>
    <groupId>com.spotify</groupId>
    <artifactId>docker-maven-plugin</artifactId>
    <version>0.4.14</version>
    <configuration>
 #       <imageName>172.16.136.222:5000/${project.artifactId}:${project.version}</imageName>
 #       <baseImage>jdk1.8</baseImage> 
        <entryPoint>["java", "-jar", "/${project.build.finalName}.jar"]</entryPoint>
        <!-- copy the service's jar file from target into the root directory of the image -->
        <resources>
            <resource>
                <targetPath>/</targetPath>
                <directory>${project.build.directory}</directory>
                <include>${project.build.finalName}.jar</include>
            </resource>
        </resources>
 #       <dockerHost>http://172.16.136.222:2375</dockerHost>
    </configuration>
</plugin>

# 需要配置github的仓库地址下载插件可能需要翻墙


# 然后 maven 执行命令，将允许用打包并上传为 docker 的进项
IDEA中执行
# mvn clean package docker:build -DpushImage
DpushImage : push推送的意思

执行成功后，使用Rancher管理容器，并配置端口，然后访问测试（端口配置9001）
```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b4f0bf1c-caf9-4ccd-b8a7-1d052d5c41d2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XTSUWJTB%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCiEcX%2BWw0CYm7csq33pKuZcgLde9Ajn5HT5SYK1d5IowIgC6TvnCYWZstfkhz1eq50r2Hhp85mTR0t%2BPO9aRm58bwqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFS1hr7OQEezACsbnSrcA2DVeqTUFXKKB9l%2BXYKu3FXCadXWD%2BuReO8Af3RaZACm13AVppKqv6kIuvbDWz6iQYnKgoLHXgBo9I0ee4aRFMH2z%2F8gbSiHh3LG1mVAN3aukNqI1LiPoJdMvGjEEjRtevaliUtXw7v98v3dTZKYowN4%2BU0opWnqxNipD97j0tPTwQwxG7GzDKoP%2FCtheoTNsBv70QUNj9FWbl4Ktw7K0F5XPaufQmtIJuCCWBC7JbK6Vr7WCwHr2jL6XpTTBrlKN%2BX8oKKTNAC265%2FJY2hIOAg8UsgsZ5iYtmkN2aUkxVvn%2FGKjx3OAy%2B4Ojh3OutOzLGv%2B6ZjdC1%2Ff0oeP5x0PJVGOl3KTlObPgtregppd8vyyhg8NB6WpyVtnZGIDQT2XlinxC2YlKPPktnWB3jitA8gCxjUnmm5XKQhPWZm7wzHGDwYkX3odR7VRR%2BXQifmw3DzLqeLA48xXh%2BKxsmWSYv%2F8Fs%2Bn%2FCFwQepGbZ0dbM8vuWSwOZAaGX5h6UwGDZKewL1M9vIQUCe48XzmfJXzIjOvZMXOfzhbz4iV1lOW%2BCWo8GIzhmgpYVKMC6z7Q4kFFgp4gGpgHfMnDuHbZNHt3rdigdcFNOqM7flXmzfEOYcq8JKZYEwnNUHpIiJ8MLW3%2F9IGOqUBXh47CuTGQyqYJW2wI8eotYzNIL9zTPiE8a52GjY5kVnDsIybh%2Bw63xZe8NggdUdAZrRk23E%2FeVALIv2CzD6Nw8xLguiSf31E1Xsu60P%2BBsOZkY1RPVjw1a%2FiajuMVJ91Js%2BBKlLBLYJuZmS2IXx39Isu9JyrEgnFC%2FbmCp3OHng3HsjsL0Kl%2BGLdFC1vXPuH%2FKVlaji6v1roUiRzUpUdKu8YUBA4&X-Amz-Signature=55da666c406b62b9ea4cb462dd89a7a47d13808c66e89c44a43315fa91099297&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/a44f9c84-9877-44d3-8ceb-4b5ddf5ff666/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XTSUWJTB%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234338Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCiEcX%2BWw0CYm7csq33pKuZcgLde9Ajn5HT5SYK1d5IowIgC6TvnCYWZstfkhz1eq50r2Hhp85mTR0t%2BPO9aRm58bwqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFS1hr7OQEezACsbnSrcA2DVeqTUFXKKB9l%2BXYKu3FXCadXWD%2BuReO8Af3RaZACm13AVppKqv6kIuvbDWz6iQYnKgoLHXgBo9I0ee4aRFMH2z%2F8gbSiHh3LG1mVAN3aukNqI1LiPoJdMvGjEEjRtevaliUtXw7v98v3dTZKYowN4%2BU0opWnqxNipD97j0tPTwQwxG7GzDKoP%2FCtheoTNsBv70QUNj9FWbl4Ktw7K0F5XPaufQmtIJuCCWBC7JbK6Vr7WCwHr2jL6XpTTBrlKN%2BX8oKKTNAC265%2FJY2hIOAg8UsgsZ5iYtmkN2aUkxVvn%2FGKjx3OAy%2B4Ojh3OutOzLGv%2B6ZjdC1%2Ff0oeP5x0PJVGOl3KTlObPgtregppd8vyyhg8NB6WpyVtnZGIDQT2XlinxC2YlKPPktnWB3jitA8gCxjUnmm5XKQhPWZm7wzHGDwYkX3odR7VRR%2BXQifmw3DzLqeLA48xXh%2BKxsmWSYv%2F8Fs%2Bn%2FCFwQepGbZ0dbM8vuWSwOZAaGX5h6UwGDZKewL1M9vIQUCe48XzmfJXzIjOvZMXOfzhbz4iV1lOW%2BCWo8GIzhmgpYVKMC6z7Q4kFFgp4gGpgHfMnDuHbZNHt3rdigdcFNOqM7flXmzfEOYcq8JKZYEwnNUHpIiJ8MLW3%2F9IGOqUBXh47CuTGQyqYJW2wI8eotYzNIL9zTPiE8a52GjY5kVnDsIybh%2Bw63xZe8NggdUdAZrRk23E%2FeVALIv2CzD6Nw8xLguiSf31E1Xsu60P%2BBsOZkY1RPVjw1a%2FiajuMVJ91Js%2BBKlLBLYJuZmS2IXx39Isu9JyrEgnFC%2FbmCp3OHng3HsjsL0Kl%2BGLdFC1vXPuH%2FKVlaji6v1roUiRzUpUdKu8YUBA4&X-Amz-Signature=b9b9784405aebacb5d50c5b8c68bbb9686059c482a478b77b08af904662d46e0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/61d54baf-e81d-4dec-947b-0d104b3b25ae/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XTSUWJTB%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCiEcX%2BWw0CYm7csq33pKuZcgLde9Ajn5HT5SYK1d5IowIgC6TvnCYWZstfkhz1eq50r2Hhp85mTR0t%2BPO9aRm58bwqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFS1hr7OQEezACsbnSrcA2DVeqTUFXKKB9l%2BXYKu3FXCadXWD%2BuReO8Af3RaZACm13AVppKqv6kIuvbDWz6iQYnKgoLHXgBo9I0ee4aRFMH2z%2F8gbSiHh3LG1mVAN3aukNqI1LiPoJdMvGjEEjRtevaliUtXw7v98v3dTZKYowN4%2BU0opWnqxNipD97j0tPTwQwxG7GzDKoP%2FCtheoTNsBv70QUNj9FWbl4Ktw7K0F5XPaufQmtIJuCCWBC7JbK6Vr7WCwHr2jL6XpTTBrlKN%2BX8oKKTNAC265%2FJY2hIOAg8UsgsZ5iYtmkN2aUkxVvn%2FGKjx3OAy%2B4Ojh3OutOzLGv%2B6ZjdC1%2Ff0oeP5x0PJVGOl3KTlObPgtregppd8vyyhg8NB6WpyVtnZGIDQT2XlinxC2YlKPPktnWB3jitA8gCxjUnmm5XKQhPWZm7wzHGDwYkX3odR7VRR%2BXQifmw3DzLqeLA48xXh%2BKxsmWSYv%2F8Fs%2Bn%2FCFwQepGbZ0dbM8vuWSwOZAaGX5h6UwGDZKewL1M9vIQUCe48XzmfJXzIjOvZMXOfzhbz4iV1lOW%2BCWo8GIzhmgpYVKMC6z7Q4kFFgp4gGpgHfMnDuHbZNHt3rdigdcFNOqM7flXmzfEOYcq8JKZYEwnNUHpIiJ8MLW3%2F9IGOqUBXh47CuTGQyqYJW2wI8eotYzNIL9zTPiE8a52GjY5kVnDsIybh%2Bw63xZe8NggdUdAZrRk23E%2FeVALIv2CzD6Nw8xLguiSf31E1Xsu60P%2BBsOZkY1RPVjw1a%2FiajuMVJ91Js%2BBKlLBLYJuZmS2IXx39Isu9JyrEgnFC%2FbmCp3OHng3HsjsL0Kl%2BGLdFC1vXPuH%2FKVlaji6v1roUiRzUpUdKu8YUBA4&X-Amz-Signature=04ae145e6d3e78f6d6b0ed0a9340f456eec03ee652efb3bed74bf0580458f7bf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b5ee4720-ca0e-4fcb-b499-2b0c59cc0dbe/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XTSUWJTB%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCiEcX%2BWw0CYm7csq33pKuZcgLde9Ajn5HT5SYK1d5IowIgC6TvnCYWZstfkhz1eq50r2Hhp85mTR0t%2BPO9aRm58bwqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFS1hr7OQEezACsbnSrcA2DVeqTUFXKKB9l%2BXYKu3FXCadXWD%2BuReO8Af3RaZACm13AVppKqv6kIuvbDWz6iQYnKgoLHXgBo9I0ee4aRFMH2z%2F8gbSiHh3LG1mVAN3aukNqI1LiPoJdMvGjEEjRtevaliUtXw7v98v3dTZKYowN4%2BU0opWnqxNipD97j0tPTwQwxG7GzDKoP%2FCtheoTNsBv70QUNj9FWbl4Ktw7K0F5XPaufQmtIJuCCWBC7JbK6Vr7WCwHr2jL6XpTTBrlKN%2BX8oKKTNAC265%2FJY2hIOAg8UsgsZ5iYtmkN2aUkxVvn%2FGKjx3OAy%2B4Ojh3OutOzLGv%2B6ZjdC1%2Ff0oeP5x0PJVGOl3KTlObPgtregppd8vyyhg8NB6WpyVtnZGIDQT2XlinxC2YlKPPktnWB3jitA8gCxjUnmm5XKQhPWZm7wzHGDwYkX3odR7VRR%2BXQifmw3DzLqeLA48xXh%2BKxsmWSYv%2F8Fs%2Bn%2FCFwQepGbZ0dbM8vuWSwOZAaGX5h6UwGDZKewL1M9vIQUCe48XzmfJXzIjOvZMXOfzhbz4iV1lOW%2BCWo8GIzhmgpYVKMC6z7Q4kFFgp4gGpgHfMnDuHbZNHt3rdigdcFNOqM7flXmzfEOYcq8JKZYEwnNUHpIiJ8MLW3%2F9IGOqUBXh47CuTGQyqYJW2wI8eotYzNIL9zTPiE8a52GjY5kVnDsIybh%2Bw63xZe8NggdUdAZrRk23E%2FeVALIv2CzD6Nw8xLguiSf31E1Xsu60P%2BBsOZkY1RPVjw1a%2FiajuMVJ91Js%2BBKlLBLYJuZmS2IXx39Isu9JyrEgnFC%2FbmCp3OHng3HsjsL0Kl%2BGLdFC1vXPuH%2FKVlaji6v1roUiRzUpUdKu8YUBA4&X-Amz-Signature=8e196b18797a4ddef8cfea3ec6bca2a284acda835996cb6acfeac47ccc4b268b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```markdown
# 触发地址：只需要通过 post 请求，就会触发上面的配置扩容现象
```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e5360082-9343-47c6-a132-e949f8c203f8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XTSUWJTB%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCiEcX%2BWw0CYm7csq33pKuZcgLde9Ajn5HT5SYK1d5IowIgC6TvnCYWZstfkhz1eq50r2Hhp85mTR0t%2BPO9aRm58bwqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFS1hr7OQEezACsbnSrcA2DVeqTUFXKKB9l%2BXYKu3FXCadXWD%2BuReO8Af3RaZACm13AVppKqv6kIuvbDWz6iQYnKgoLHXgBo9I0ee4aRFMH2z%2F8gbSiHh3LG1mVAN3aukNqI1LiPoJdMvGjEEjRtevaliUtXw7v98v3dTZKYowN4%2BU0opWnqxNipD97j0tPTwQwxG7GzDKoP%2FCtheoTNsBv70QUNj9FWbl4Ktw7K0F5XPaufQmtIJuCCWBC7JbK6Vr7WCwHr2jL6XpTTBrlKN%2BX8oKKTNAC265%2FJY2hIOAg8UsgsZ5iYtmkN2aUkxVvn%2FGKjx3OAy%2B4Ojh3OutOzLGv%2B6ZjdC1%2Ff0oeP5x0PJVGOl3KTlObPgtregppd8vyyhg8NB6WpyVtnZGIDQT2XlinxC2YlKPPktnWB3jitA8gCxjUnmm5XKQhPWZm7wzHGDwYkX3odR7VRR%2BXQifmw3DzLqeLA48xXh%2BKxsmWSYv%2F8Fs%2Bn%2FCFwQepGbZ0dbM8vuWSwOZAaGX5h6UwGDZKewL1M9vIQUCe48XzmfJXzIjOvZMXOfzhbz4iV1lOW%2BCWo8GIzhmgpYVKMC6z7Q4kFFgp4gGpgHfMnDuHbZNHt3rdigdcFNOqM7flXmzfEOYcq8JKZYEwnNUHpIiJ8MLW3%2F9IGOqUBXh47CuTGQyqYJW2wI8eotYzNIL9zTPiE8a52GjY5kVnDsIybh%2Bw63xZe8NggdUdAZrRk23E%2FeVALIv2CzD6Nw8xLguiSf31E1Xsu60P%2BBsOZkY1RPVjw1a%2FiajuMVJ91Js%2BBKlLBLYJuZmS2IXx39Isu9JyrEgnFC%2FbmCp3OHng3HsjsL0Kl%2BGLdFC1vXPuH%2FKVlaji6v1roUiRzUpUdKu8YUBA4&X-Amz-Signature=777f8b26027b78d8aeb06295f619ae6cf6020b2ccb67d8d41519576bdc9f852f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```markdown
# 容器从1个变成了3个但是却没有端口映射---------------> 负载均衡

```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/730df8c3-b40b-4c72-aa52-2e97e58d36ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XTSUWJTB%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCiEcX%2BWw0CYm7csq33pKuZcgLde9Ajn5HT5SYK1d5IowIgC6TvnCYWZstfkhz1eq50r2Hhp85mTR0t%2BPO9aRm58bwqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFS1hr7OQEezACsbnSrcA2DVeqTUFXKKB9l%2BXYKu3FXCadXWD%2BuReO8Af3RaZACm13AVppKqv6kIuvbDWz6iQYnKgoLHXgBo9I0ee4aRFMH2z%2F8gbSiHh3LG1mVAN3aukNqI1LiPoJdMvGjEEjRtevaliUtXw7v98v3dTZKYowN4%2BU0opWnqxNipD97j0tPTwQwxG7GzDKoP%2FCtheoTNsBv70QUNj9FWbl4Ktw7K0F5XPaufQmtIJuCCWBC7JbK6Vr7WCwHr2jL6XpTTBrlKN%2BX8oKKTNAC265%2FJY2hIOAg8UsgsZ5iYtmkN2aUkxVvn%2FGKjx3OAy%2B4Ojh3OutOzLGv%2B6ZjdC1%2Ff0oeP5x0PJVGOl3KTlObPgtregppd8vyyhg8NB6WpyVtnZGIDQT2XlinxC2YlKPPktnWB3jitA8gCxjUnmm5XKQhPWZm7wzHGDwYkX3odR7VRR%2BXQifmw3DzLqeLA48xXh%2BKxsmWSYv%2F8Fs%2Bn%2FCFwQepGbZ0dbM8vuWSwOZAaGX5h6UwGDZKewL1M9vIQUCe48XzmfJXzIjOvZMXOfzhbz4iV1lOW%2BCWo8GIzhmgpYVKMC6z7Q4kFFgp4gGpgHfMnDuHbZNHt3rdigdcFNOqM7flXmzfEOYcq8JKZYEwnNUHpIiJ8MLW3%2F9IGOqUBXh47CuTGQyqYJW2wI8eotYzNIL9zTPiE8a52GjY5kVnDsIybh%2Bw63xZe8NggdUdAZrRk23E%2FeVALIv2CzD6Nw8xLguiSf31E1Xsu60P%2BBsOZkY1RPVjw1a%2FiajuMVJ91Js%2BBKlLBLYJuZmS2IXx39Isu9JyrEgnFC%2FbmCp3OHng3HsjsL0Kl%2BGLdFC1vXPuH%2FKVlaji6v1roUiRzUpUdKu8YUBA4&X-Amz-Signature=e08cc16cf2bcfd378f6ae9b194e6a012aab79068a547eb8439c1909a0cae5a51&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```markdown
# 添加负载均衡的服务就可以访问扩容后的服务（轮训）
```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/ec7925a5-77c8-4405-85d8-dd374dd587e7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XTSUWJTB%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234339Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCiEcX%2BWw0CYm7csq33pKuZcgLde9Ajn5HT5SYK1d5IowIgC6TvnCYWZstfkhz1eq50r2Hhp85mTR0t%2BPO9aRm58bwqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFS1hr7OQEezACsbnSrcA2DVeqTUFXKKB9l%2BXYKu3FXCadXWD%2BuReO8Af3RaZACm13AVppKqv6kIuvbDWz6iQYnKgoLHXgBo9I0ee4aRFMH2z%2F8gbSiHh3LG1mVAN3aukNqI1LiPoJdMvGjEEjRtevaliUtXw7v98v3dTZKYowN4%2BU0opWnqxNipD97j0tPTwQwxG7GzDKoP%2FCtheoTNsBv70QUNj9FWbl4Ktw7K0F5XPaufQmtIJuCCWBC7JbK6Vr7WCwHr2jL6XpTTBrlKN%2BX8oKKTNAC265%2FJY2hIOAg8UsgsZ5iYtmkN2aUkxVvn%2FGKjx3OAy%2B4Ojh3OutOzLGv%2B6ZjdC1%2Ff0oeP5x0PJVGOl3KTlObPgtregppd8vyyhg8NB6WpyVtnZGIDQT2XlinxC2YlKPPktnWB3jitA8gCxjUnmm5XKQhPWZm7wzHGDwYkX3odR7VRR%2BXQifmw3DzLqeLA48xXh%2BKxsmWSYv%2F8Fs%2Bn%2FCFwQepGbZ0dbM8vuWSwOZAaGX5h6UwGDZKewL1M9vIQUCe48XzmfJXzIjOvZMXOfzhbz4iV1lOW%2BCWo8GIzhmgpYVKMC6z7Q4kFFgp4gGpgHfMnDuHbZNHt3rdigdcFNOqM7flXmzfEOYcq8JKZYEwnNUHpIiJ8MLW3%2F9IGOqUBXh47CuTGQyqYJW2wI8eotYzNIL9zTPiE8a52GjY5kVnDsIybh%2Bw63xZe8NggdUdAZrRk23E%2FeVALIv2CzD6Nw8xLguiSf31E1Xsu60P%2BBsOZkY1RPVjw1a%2FiajuMVJ91Js%2BBKlLBLYJuZmS2IXx39Isu9JyrEgnFC%2FbmCp3OHng3HsjsL0Kl%2BGLdFC1vXPuH%2FKVlaji6v1roUiRzUpUdKu8YUBA4&X-Amz-Signature=1cb18222fb4e40eb0d1b8692fdea6d358b01cde6d081e439af3513944c0a5eed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)











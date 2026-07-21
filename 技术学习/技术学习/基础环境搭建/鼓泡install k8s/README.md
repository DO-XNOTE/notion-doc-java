---
title: 鼓泡install k8s
---

# 鼓泡install k8s


# 沽泡安装

## 虚拟机的环境配置

[file](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b3c81e42-eb3f-47cc-a0a3-a721f6c255ff/%E5%AD%A6%E5%91%98-%E5%85%B5%E5%85%B5-%E6%95%B4%E7%90%86%E4%BC%98%E5%8C%96%E7%9A%84%E6%AD%A5%E9%AA%A4%E5%A4%A7%E5%AE%B6%E4%B9%9F%E5%8F%AF%E4%BB%A5%E4%BD%9C%E4%B8%BA%E5%8F%82%E8%80%83.md?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y7YCOZDA%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCDa3y%2FLe5Iy%2BqDP3jHDcv5BgofJ6e6%2FFd7gnLc45wCYgIgI8q4v9PitvWy1s%2BkDvE%2Bc5WNyCPH0vdkOCH1Duxg1x8qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLNwKtt5LmMk5UdVjyrcA4s9MHnpiDvR9CyVhWga2U1SOH0IT4t03M1q0ERbEpFF69r5Cag6CXZZLjPfHhHlD1cFXx6GCvmR2N6LVL4vFLft4ANEaI4AOZknW1Fk48EnGrzBddUfYFl7PSrpMFgJAOhzFGNV2YYlhTlI9O%2F1NwU2R0tpXqtg05dEeEwpXoC1yJgHSllK8Y0qRrbbdATtakNwc4D2NaFndX6W0LJFg7zmW%2FMzlL7EQWqdqdWBB5OcBK3760IyXTm0okns8YOy7C08ALsu93mx63jaZXFqcvuggIGBVA5IpO1mjMdAiDLzaiQoP1t2wVtesr9FQbkifH9dCpTXXBP3mJ7ybGHT8tFiFlrGj82VF%2BKl8ZXN8oK6QandtaMhKGjcDFfRfx9TMdz0O9au1FcYrgwTCigylkXfT4ScRgdO%2B2g9zt3j1lVGRCT9ayaFknnX64QIUDPeaBSyW15uBrtHgzbG2t%2BitGpCR0x71hTFFmuzrBv%2Fow1JJtV4m23Y4JnZa2tWIhFJRXNXAqtTxRjnGt9cDVCDPfE0iF%2FoGAYFjaiJB4gaK4TNhz0VCQix%2Fvb1XtcVW1jEQPFYeYWfeeTrLlOp8aA0y553PzNX57ysFwzBCa7m4Db3EQ%2FgwFidDx%2FJYD4fMIa3%2F9IGOqUBF6HnLH7ZOWGGlpUcR6KgiOgGGU%2FfVQgaC2W3fvIwJHyJOPWlFe5hWGUjQnc8x0dVEm0Gcmwupwwg0ExGRA2aAaTfnMMlFHNVIJMyM3sqhK1ywCLQaDxHVonsO474bpkcbnTDsATfJzEhyFo3PrakdH2T3cz1RN58QANsL2XLiRunfPXRrmYh7rH4eDjL%2FWCtr3Q4tKfWdGOHZ%2BOIy%2Fe4vnhCMOEo&X-Amz-Signature=15a5551e40da97a9a1e1c6aad0c737336563dbd8601fbc7f5d86bda5f5685ace&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[file](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/3148aa57-94b7-40e8-b22c-41d2f399859d/%E5%B7%A5%E6%AC%B2%E5%96%84%E5%85%B6%E4%BA%8B%E5%BF%85%E5%85%88%E5%88%A9%E5%85%B6%E5%99%A8%E8%AF%BE%E7%A8%8B%E7%AC%94%E8%AE%B0.md?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y7YCOZDA%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCDa3y%2FLe5Iy%2BqDP3jHDcv5BgofJ6e6%2FFd7gnLc45wCYgIgI8q4v9PitvWy1s%2BkDvE%2Bc5WNyCPH0vdkOCH1Duxg1x8qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLNwKtt5LmMk5UdVjyrcA4s9MHnpiDvR9CyVhWga2U1SOH0IT4t03M1q0ERbEpFF69r5Cag6CXZZLjPfHhHlD1cFXx6GCvmR2N6LVL4vFLft4ANEaI4AOZknW1Fk48EnGrzBddUfYFl7PSrpMFgJAOhzFGNV2YYlhTlI9O%2F1NwU2R0tpXqtg05dEeEwpXoC1yJgHSllK8Y0qRrbbdATtakNwc4D2NaFndX6W0LJFg7zmW%2FMzlL7EQWqdqdWBB5OcBK3760IyXTm0okns8YOy7C08ALsu93mx63jaZXFqcvuggIGBVA5IpO1mjMdAiDLzaiQoP1t2wVtesr9FQbkifH9dCpTXXBP3mJ7ybGHT8tFiFlrGj82VF%2BKl8ZXN8oK6QandtaMhKGjcDFfRfx9TMdz0O9au1FcYrgwTCigylkXfT4ScRgdO%2B2g9zt3j1lVGRCT9ayaFknnX64QIUDPeaBSyW15uBrtHgzbG2t%2BitGpCR0x71hTFFmuzrBv%2Fow1JJtV4m23Y4JnZa2tWIhFJRXNXAqtTxRjnGt9cDVCDPfE0iF%2FoGAYFjaiJB4gaK4TNhz0VCQix%2Fvb1XtcVW1jEQPFYeYWfeeTrLlOp8aA0y553PzNX57ysFwzBCa7m4Db3EQ%2FgwFidDx%2FJYD4fMIa3%2F9IGOqUBF6HnLH7ZOWGGlpUcR6KgiOgGGU%2FfVQgaC2W3fvIwJHyJOPWlFe5hWGUjQnc8x0dVEm0Gcmwupwwg0ExGRA2aAaTfnMMlFHNVIJMyM3sqhK1ywCLQaDxHVonsO474bpkcbnTDsATfJzEhyFo3PrakdH2T3cz1RN58QANsL2XLiRunfPXRrmYh7rH4eDjL%2FWCtr3Q4tKfWdGOHZ%2BOIy%2Fe4vnhCMOEo&X-Amz-Signature=6e9c677eb305c354f31c2ba0c009c18fbbb03d17eb3e8e8404e8931f8c24c5f9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/cfd19a37-4f0a-4553-a7f7-3ddfaf99f66e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y7YCOZDA%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCDa3y%2FLe5Iy%2BqDP3jHDcv5BgofJ6e6%2FFd7gnLc45wCYgIgI8q4v9PitvWy1s%2BkDvE%2Bc5WNyCPH0vdkOCH1Duxg1x8qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLNwKtt5LmMk5UdVjyrcA4s9MHnpiDvR9CyVhWga2U1SOH0IT4t03M1q0ERbEpFF69r5Cag6CXZZLjPfHhHlD1cFXx6GCvmR2N6LVL4vFLft4ANEaI4AOZknW1Fk48EnGrzBddUfYFl7PSrpMFgJAOhzFGNV2YYlhTlI9O%2F1NwU2R0tpXqtg05dEeEwpXoC1yJgHSllK8Y0qRrbbdATtakNwc4D2NaFndX6W0LJFg7zmW%2FMzlL7EQWqdqdWBB5OcBK3760IyXTm0okns8YOy7C08ALsu93mx63jaZXFqcvuggIGBVA5IpO1mjMdAiDLzaiQoP1t2wVtesr9FQbkifH9dCpTXXBP3mJ7ybGHT8tFiFlrGj82VF%2BKl8ZXN8oK6QandtaMhKGjcDFfRfx9TMdz0O9au1FcYrgwTCigylkXfT4ScRgdO%2B2g9zt3j1lVGRCT9ayaFknnX64QIUDPeaBSyW15uBrtHgzbG2t%2BitGpCR0x71hTFFmuzrBv%2Fow1JJtV4m23Y4JnZa2tWIhFJRXNXAqtTxRjnGt9cDVCDPfE0iF%2FoGAYFjaiJB4gaK4TNhz0VCQix%2Fvb1XtcVW1jEQPFYeYWfeeTrLlOp8aA0y553PzNX57ysFwzBCa7m4Db3EQ%2FgwFidDx%2FJYD4fMIa3%2F9IGOqUBF6HnLH7ZOWGGlpUcR6KgiOgGGU%2FfVQgaC2W3fvIwJHyJOPWlFe5hWGUjQnc8x0dVEm0Gcmwupwwg0ExGRA2aAaTfnMMlFHNVIJMyM3sqhK1ywCLQaDxHVonsO474bpkcbnTDsATfJzEhyFo3PrakdH2T3cz1RN58QANsL2XLiRunfPXRrmYh7rH4eDjL%2FWCtr3Q4tKfWdGOHZ%2BOIy%2Fe4vnhCMOEo&X-Amz-Signature=ba98fd77727d794ec7944beb35d6ea005b235822eef7387e9b0b4765821e7780&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```markdown
根据以上鼓泡文件下载
# 直接安装 否则会导致下载缺少一些需要高版本的依赖包，直接下载可以安装可以卸载的其他版本的
# error：Requires: kubernetes-cni = 0.7.5 Available: kubernetes-cni-0.5.1-0.aarch64 (kubernetes) 版本低了
# yum install -y kubelet kubeadm kubectl 可直接下载

启动报错：
1:/etc/kubernetes/manifests
```

```markdown
# 设置 每台机器的 hosts
并设置机器的名称  sudo hostnamectl set-hostname m
并设置机器的名称  sudo hostnamectl set-hostname n1
并设置机器的名称  sudo hostnamectl set-hostname n2
172.16.136.227 m     
172.16.136.228 n1    
172.16.136.229 n2    
```

```markdown
# 写错了： 是 kubectl
```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/815c4350-f828-425e-b2c2-b02bb7d8fede/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y7YCOZDA%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCDa3y%2FLe5Iy%2BqDP3jHDcv5BgofJ6e6%2FFd7gnLc45wCYgIgI8q4v9PitvWy1s%2BkDvE%2Bc5WNyCPH0vdkOCH1Duxg1x8qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLNwKtt5LmMk5UdVjyrcA4s9MHnpiDvR9CyVhWga2U1SOH0IT4t03M1q0ERbEpFF69r5Cag6CXZZLjPfHhHlD1cFXx6GCvmR2N6LVL4vFLft4ANEaI4AOZknW1Fk48EnGrzBddUfYFl7PSrpMFgJAOhzFGNV2YYlhTlI9O%2F1NwU2R0tpXqtg05dEeEwpXoC1yJgHSllK8Y0qRrbbdATtakNwc4D2NaFndX6W0LJFg7zmW%2FMzlL7EQWqdqdWBB5OcBK3760IyXTm0okns8YOy7C08ALsu93mx63jaZXFqcvuggIGBVA5IpO1mjMdAiDLzaiQoP1t2wVtesr9FQbkifH9dCpTXXBP3mJ7ybGHT8tFiFlrGj82VF%2BKl8ZXN8oK6QandtaMhKGjcDFfRfx9TMdz0O9au1FcYrgwTCigylkXfT4ScRgdO%2B2g9zt3j1lVGRCT9ayaFknnX64QIUDPeaBSyW15uBrtHgzbG2t%2BitGpCR0x71hTFFmuzrBv%2Fow1JJtV4m23Y4JnZa2tWIhFJRXNXAqtTxRjnGt9cDVCDPfE0iF%2FoGAYFjaiJB4gaK4TNhz0VCQix%2Fvb1XtcVW1jEQPFYeYWfeeTrLlOp8aA0y553PzNX57ysFwzBCa7m4Db3EQ%2FgwFidDx%2FJYD4fMIa3%2F9IGOqUBF6HnLH7ZOWGGlpUcR6KgiOgGGU%2FfVQgaC2W3fvIwJHyJOPWlFe5hWGUjQnc8x0dVEm0Gcmwupwwg0ExGRA2aAaTfnMMlFHNVIJMyM3sqhK1ywCLQaDxHVonsO474bpkcbnTDsATfJzEhyFo3PrakdH2T3cz1RN58QANsL2XLiRunfPXRrmYh7rH4eDjL%2FWCtr3Q4tKfWdGOHZ%2BOIy%2Fe4vnhCMOEo&X-Amz-Signature=5297077103a4f426e78e75b5171f1b500e4f4e36903eb9a155c5e5569151492c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```markdown
# yum install -y kubeadm-1.21.14-0 kubelet-1.21.14-0 kubectl-1.21.14-0 安装提升一个次版本就可以

# kebeadm  kebuctl kubelet 安装完成后后，
需要安装的组件查询使用的命令
# kubeadm config images list 可以打印出来，（版本最好就是要对应，不要安装太多版本的）


[root@localhost ~]# kubeadm config images list
I1027 07:34:14.128782    3753 version.go:254] remote version is much newer: v1.25.3; falling back to: stable-1.21
k8s.gcr.io/kube-apiserver:v1.21.14
k8s.gcr.io/kube-controller-manager:v1.21.14
k8s.gcr.io/kube-scheduler:v1.21.14
k8s.gcr.io/kube-proxy:v1.21.14
k8s.gcr.io/pause:3.4.1
k8s.gcr.io/etcd:3.4.13-0
k8s.gcr.io/coredns/coredns:v1.8.0z
# ---------------------------------------------------------------
#!/bin/bash
set -e

KUBE_VERSION=v1.21.14
KUBE_PAUSE_VERSION=3.4.1
ETCD_VERSION=3.4.13-0
CORE_DNS_VERSION=1.8.0

GCR_URL=k8s.gcr.io
ALIYUN_URL=registry.cn-hangzhou.aliyuncs.com/google_containers

images=(kube-proxy:${KUBE_VERSION}
kube-scheduler:${KUBE_VERSION}
kube-controller-manager:${KUBE_VERSION}
kube-apiserver:${KUBE_VERSION}
pause:${KUBE_PAUSE_VERSION}
etcd:${ETCD_VERSION}
coredns:${CORE_DNS_VERSION})

for imageName in ${images[@]} ; do
  docker pull $ALIYUN_URL/$imageName
  docker tag  $ALIYUN_URL/$imageName $GCR_URL/$imageName
  docker rmi $ALIYUN_URL/$imageName
done
# ---------------------------------------------------------------

---------------------------------
#执行脚本：    sh ./kubeadm.sh 
拉取需要的版本
```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/4af283b5-37cc-4659-bfbe-fd067dae9355/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y7YCOZDA%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCDa3y%2FLe5Iy%2BqDP3jHDcv5BgofJ6e6%2FFd7gnLc45wCYgIgI8q4v9PitvWy1s%2BkDvE%2Bc5WNyCPH0vdkOCH1Duxg1x8qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLNwKtt5LmMk5UdVjyrcA4s9MHnpiDvR9CyVhWga2U1SOH0IT4t03M1q0ERbEpFF69r5Cag6CXZZLjPfHhHlD1cFXx6GCvmR2N6LVL4vFLft4ANEaI4AOZknW1Fk48EnGrzBddUfYFl7PSrpMFgJAOhzFGNV2YYlhTlI9O%2F1NwU2R0tpXqtg05dEeEwpXoC1yJgHSllK8Y0qRrbbdATtakNwc4D2NaFndX6W0LJFg7zmW%2FMzlL7EQWqdqdWBB5OcBK3760IyXTm0okns8YOy7C08ALsu93mx63jaZXFqcvuggIGBVA5IpO1mjMdAiDLzaiQoP1t2wVtesr9FQbkifH9dCpTXXBP3mJ7ybGHT8tFiFlrGj82VF%2BKl8ZXN8oK6QandtaMhKGjcDFfRfx9TMdz0O9au1FcYrgwTCigylkXfT4ScRgdO%2B2g9zt3j1lVGRCT9ayaFknnX64QIUDPeaBSyW15uBrtHgzbG2t%2BitGpCR0x71hTFFmuzrBv%2Fow1JJtV4m23Y4JnZa2tWIhFJRXNXAqtTxRjnGt9cDVCDPfE0iF%2FoGAYFjaiJB4gaK4TNhz0VCQix%2Fvb1XtcVW1jEQPFYeYWfeeTrLlOp8aA0y553PzNX57ysFwzBCa7m4Db3EQ%2FgwFidDx%2FJYD4fMIa3%2F9IGOqUBF6HnLH7ZOWGGlpUcR6KgiOgGGU%2FfVQgaC2W3fvIwJHyJOPWlFe5hWGUjQnc8x0dVEm0Gcmwupwwg0ExGRA2aAaTfnMMlFHNVIJMyM3sqhK1ywCLQaDxHVonsO474bpkcbnTDsATfJzEhyFo3PrakdH2T3cz1RN58QANsL2XLiRunfPXRrmYh7rH4eDjL%2FWCtr3Q4tKfWdGOHZ%2BOIy%2Fe4vnhCMOEo&X-Amz-Signature=0086b6c74f75a525abaeaeb44c54614202408d9c11bc9e82bf83cb750b5dec0e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```markdown

```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/ab5fba32-e045-4188-88a9-c1252866d439/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y7YCOZDA%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCDa3y%2FLe5Iy%2BqDP3jHDcv5BgofJ6e6%2FFd7gnLc45wCYgIgI8q4v9PitvWy1s%2BkDvE%2Bc5WNyCPH0vdkOCH1Duxg1x8qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLNwKtt5LmMk5UdVjyrcA4s9MHnpiDvR9CyVhWga2U1SOH0IT4t03M1q0ERbEpFF69r5Cag6CXZZLjPfHhHlD1cFXx6GCvmR2N6LVL4vFLft4ANEaI4AOZknW1Fk48EnGrzBddUfYFl7PSrpMFgJAOhzFGNV2YYlhTlI9O%2F1NwU2R0tpXqtg05dEeEwpXoC1yJgHSllK8Y0qRrbbdATtakNwc4D2NaFndX6W0LJFg7zmW%2FMzlL7EQWqdqdWBB5OcBK3760IyXTm0okns8YOy7C08ALsu93mx63jaZXFqcvuggIGBVA5IpO1mjMdAiDLzaiQoP1t2wVtesr9FQbkifH9dCpTXXBP3mJ7ybGHT8tFiFlrGj82VF%2BKl8ZXN8oK6QandtaMhKGjcDFfRfx9TMdz0O9au1FcYrgwTCigylkXfT4ScRgdO%2B2g9zt3j1lVGRCT9ayaFknnX64QIUDPeaBSyW15uBrtHgzbG2t%2BitGpCR0x71hTFFmuzrBv%2Fow1JJtV4m23Y4JnZa2tWIhFJRXNXAqtTxRjnGt9cDVCDPfE0iF%2FoGAYFjaiJB4gaK4TNhz0VCQix%2Fvb1XtcVW1jEQPFYeYWfeeTrLlOp8aA0y553PzNX57ysFwzBCa7m4Db3EQ%2FgwFidDx%2FJYD4fMIa3%2F9IGOqUBF6HnLH7ZOWGGlpUcR6KgiOgGGU%2FfVQgaC2W3fvIwJHyJOPWlFe5hWGUjQnc8x0dVEm0Gcmwupwwg0ExGRA2aAaTfnMMlFHNVIJMyM3sqhK1ywCLQaDxHVonsO474bpkcbnTDsATfJzEhyFo3PrakdH2T3cz1RN58QANsL2XLiRunfPXRrmYh7rH4eDjL%2FWCtr3Q4tKfWdGOHZ%2BOIy%2Fe4vnhCMOEo&X-Amz-Signature=50c0c5fa70d4d6a41398d84d4f3a6978f3128a7a17afacf08daba39c9bd6c37a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/87643276-793e-424b-80bf-6b7285f65c57/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y7YCOZDA%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCDa3y%2FLe5Iy%2BqDP3jHDcv5BgofJ6e6%2FFd7gnLc45wCYgIgI8q4v9PitvWy1s%2BkDvE%2Bc5WNyCPH0vdkOCH1Duxg1x8qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLNwKtt5LmMk5UdVjyrcA4s9MHnpiDvR9CyVhWga2U1SOH0IT4t03M1q0ERbEpFF69r5Cag6CXZZLjPfHhHlD1cFXx6GCvmR2N6LVL4vFLft4ANEaI4AOZknW1Fk48EnGrzBddUfYFl7PSrpMFgJAOhzFGNV2YYlhTlI9O%2F1NwU2R0tpXqtg05dEeEwpXoC1yJgHSllK8Y0qRrbbdATtakNwc4D2NaFndX6W0LJFg7zmW%2FMzlL7EQWqdqdWBB5OcBK3760IyXTm0okns8YOy7C08ALsu93mx63jaZXFqcvuggIGBVA5IpO1mjMdAiDLzaiQoP1t2wVtesr9FQbkifH9dCpTXXBP3mJ7ybGHT8tFiFlrGj82VF%2BKl8ZXN8oK6QandtaMhKGjcDFfRfx9TMdz0O9au1FcYrgwTCigylkXfT4ScRgdO%2B2g9zt3j1lVGRCT9ayaFknnX64QIUDPeaBSyW15uBrtHgzbG2t%2BitGpCR0x71hTFFmuzrBv%2Fow1JJtV4m23Y4JnZa2tWIhFJRXNXAqtTxRjnGt9cDVCDPfE0iF%2FoGAYFjaiJB4gaK4TNhz0VCQix%2Fvb1XtcVW1jEQPFYeYWfeeTrLlOp8aA0y553PzNX57ysFwzBCa7m4Db3EQ%2FgwFidDx%2FJYD4fMIa3%2F9IGOqUBF6HnLH7ZOWGGlpUcR6KgiOgGGU%2FfVQgaC2W3fvIwJHyJOPWlFe5hWGUjQnc8x0dVEm0Gcmwupwwg0ExGRA2aAaTfnMMlFHNVIJMyM3sqhK1ywCLQaDxHVonsO474bpkcbnTDsATfJzEhyFo3PrakdH2T3cz1RN58QANsL2XLiRunfPXRrmYh7rH4eDjL%2FWCtr3Q4tKfWdGOHZ%2BOIy%2Fe4vnhCMOEo&X-Amz-Signature=4cc993f13d42f6bd30d2e5e45109df90132dfd49d96fcd6673bcb22b2af20555&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```markdown
## 可以租用香港的云服务，拉取国外的镜像，放在自己的仓库上


docker images 查看到我们的镜像

[root@n2 software]# docker images
REPOSITORY                           TAG                 IMAGE ID            CREATED             SIZE
k8s.gcr.io/kube-apiserver            v1.21.14            151ba3c9f102        4 months ago        117MB
k8s.gcr.io/kube-proxy                v1.21.14            e8e1a1b5feef        4 months ago        97.3MB
k8s.gcr.io/kube-controller-manager   v1.21.14            11f8a2457a62        4 months ago        112MB
k8s.gcr.io/kube-scheduler            v1.21.14            64286b3112ed        4 months ago        47.6MB
k8s.gcr.io/pause                     3.4.1               d055819ed991        21 months ago       484kB
k8s.gcr.io/coredns                   1.8.0               1a1f05a2cd7c        2 years ago         39.3MB
k8s.gcr.io/etcd                      3.4.13-0            05b738aa1bc6        2 years ago         312MB
```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/45402456-bba5-479e-9977-b805d0a08ed8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y7YCOZDA%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCDa3y%2FLe5Iy%2BqDP3jHDcv5BgofJ6e6%2FFd7gnLc45wCYgIgI8q4v9PitvWy1s%2BkDvE%2Bc5WNyCPH0vdkOCH1Duxg1x8qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLNwKtt5LmMk5UdVjyrcA4s9MHnpiDvR9CyVhWga2U1SOH0IT4t03M1q0ERbEpFF69r5Cag6CXZZLjPfHhHlD1cFXx6GCvmR2N6LVL4vFLft4ANEaI4AOZknW1Fk48EnGrzBddUfYFl7PSrpMFgJAOhzFGNV2YYlhTlI9O%2F1NwU2R0tpXqtg05dEeEwpXoC1yJgHSllK8Y0qRrbbdATtakNwc4D2NaFndX6W0LJFg7zmW%2FMzlL7EQWqdqdWBB5OcBK3760IyXTm0okns8YOy7C08ALsu93mx63jaZXFqcvuggIGBVA5IpO1mjMdAiDLzaiQoP1t2wVtesr9FQbkifH9dCpTXXBP3mJ7ybGHT8tFiFlrGj82VF%2BKl8ZXN8oK6QandtaMhKGjcDFfRfx9TMdz0O9au1FcYrgwTCigylkXfT4ScRgdO%2B2g9zt3j1lVGRCT9ayaFknnX64QIUDPeaBSyW15uBrtHgzbG2t%2BitGpCR0x71hTFFmuzrBv%2Fow1JJtV4m23Y4JnZa2tWIhFJRXNXAqtTxRjnGt9cDVCDPfE0iF%2FoGAYFjaiJB4gaK4TNhz0VCQix%2Fvb1XtcVW1jEQPFYeYWfeeTrLlOp8aA0y553PzNX57ysFwzBCa7m4Db3EQ%2FgwFidDx%2FJYD4fMIa3%2F9IGOqUBF6HnLH7ZOWGGlpUcR6KgiOgGGU%2FfVQgaC2W3fvIwJHyJOPWlFe5hWGUjQnc8x0dVEm0Gcmwupwwg0ExGRA2aAaTfnMMlFHNVIJMyM3sqhK1ywCLQaDxHVonsO474bpkcbnTDsATfJzEhyFo3PrakdH2T3cz1RN58QANsL2XLiRunfPXRrmYh7rH4eDjL%2FWCtr3Q4tKfWdGOHZ%2BOIy%2Fe4vnhCMOEo&X-Amz-Signature=e46f9153d23e77593bf7dced065c8346715f75c8bcf8e2a7f7f28f6413a71ddb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

### 进行初始化操作

```markdown
# 主节点上执行 初始化操作 我的是 230 节点

# kubeadm init --image-repository registry.aliyuncs.com/google_containers --apiserver-advertise-address=172.16.136.230 --kubernetes-version=v1.21.4 --pod-network-cidr=10.244.0.0/16 --service-cidr=10.1.0.0/16
kubeadm init --apiserver-advertise-address=172.16.136.230 --kubernetes-version=v1.21.4 --pod-network-cidr=10.244.0.0/16 --service-cidr=10.1.0.0/16

# 关机去设置 内存 调整大一点 超过2g最好， 如果 并设置这些组件卡机启动
```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/a714b600-ed5d-4f4d-9fe9-7ac911271a69/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y7YCOZDA%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCDa3y%2FLe5Iy%2BqDP3jHDcv5BgofJ6e6%2FFd7gnLc45wCYgIgI8q4v9PitvWy1s%2BkDvE%2Bc5WNyCPH0vdkOCH1Duxg1x8qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLNwKtt5LmMk5UdVjyrcA4s9MHnpiDvR9CyVhWga2U1SOH0IT4t03M1q0ERbEpFF69r5Cag6CXZZLjPfHhHlD1cFXx6GCvmR2N6LVL4vFLft4ANEaI4AOZknW1Fk48EnGrzBddUfYFl7PSrpMFgJAOhzFGNV2YYlhTlI9O%2F1NwU2R0tpXqtg05dEeEwpXoC1yJgHSllK8Y0qRrbbdATtakNwc4D2NaFndX6W0LJFg7zmW%2FMzlL7EQWqdqdWBB5OcBK3760IyXTm0okns8YOy7C08ALsu93mx63jaZXFqcvuggIGBVA5IpO1mjMdAiDLzaiQoP1t2wVtesr9FQbkifH9dCpTXXBP3mJ7ybGHT8tFiFlrGj82VF%2BKl8ZXN8oK6QandtaMhKGjcDFfRfx9TMdz0O9au1FcYrgwTCigylkXfT4ScRgdO%2B2g9zt3j1lVGRCT9ayaFknnX64QIUDPeaBSyW15uBrtHgzbG2t%2BitGpCR0x71hTFFmuzrBv%2Fow1JJtV4m23Y4JnZa2tWIhFJRXNXAqtTxRjnGt9cDVCDPfE0iF%2FoGAYFjaiJB4gaK4TNhz0VCQix%2Fvb1XtcVW1jEQPFYeYWfeeTrLlOp8aA0y553PzNX57ysFwzBCa7m4Db3EQ%2FgwFidDx%2FJYD4fMIa3%2F9IGOqUBF6HnLH7ZOWGGlpUcR6KgiOgGGU%2FfVQgaC2W3fvIwJHyJOPWlFe5hWGUjQnc8x0dVEm0Gcmwupwwg0ExGRA2aAaTfnMMlFHNVIJMyM3sqhK1ywCLQaDxHVonsO474bpkcbnTDsATfJzEhyFo3PrakdH2T3cz1RN58QANsL2XLiRunfPXRrmYh7rH4eDjL%2FWCtr3Q4tKfWdGOHZ%2BOIy%2Fe4vnhCMOEo&X-Amz-Signature=215d238d26bc1c1860e863bb947dd38ff04c544fabb882719fde331f7e0916e3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```markdown
==================上面的初始化语句方式不行=======================================

# 初始化使用这个：
# s

#-----------------------------------初始化成功的重要信息---------------------------------------

Then you can join any number of worker nodes by running the following on each as root:
kubeadm join 172.16.136.234:6443 --token xjm293.hfpup1c4ni3pro7u \
        --discovery-token-ca-cert-hash sha256:e2a7c83ce93ebf7c590682b94d260325a32bd2a372bfdd779dcd910d6c9a319e

#-------------------------------------------------------------------------

To start using your cluster, you need to run the following as a regular user:

#  mkdir -p $HOME/.kube
  sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
  sudo chown $(id -u):$(id -g) $HOME/.kube/config

Alternatively, if you are the root user, you can run:

  export KUBECONFIG=/etc/kubernetes/admin.conf


```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/a198d0d0-2bb4-4d68-a7da-3ca10b794ed3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y7YCOZDA%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCDa3y%2FLe5Iy%2BqDP3jHDcv5BgofJ6e6%2FFd7gnLc45wCYgIgI8q4v9PitvWy1s%2BkDvE%2Bc5WNyCPH0vdkOCH1Duxg1x8qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLNwKtt5LmMk5UdVjyrcA4s9MHnpiDvR9CyVhWga2U1SOH0IT4t03M1q0ERbEpFF69r5Cag6CXZZLjPfHhHlD1cFXx6GCvmR2N6LVL4vFLft4ANEaI4AOZknW1Fk48EnGrzBddUfYFl7PSrpMFgJAOhzFGNV2YYlhTlI9O%2F1NwU2R0tpXqtg05dEeEwpXoC1yJgHSllK8Y0qRrbbdATtakNwc4D2NaFndX6W0LJFg7zmW%2FMzlL7EQWqdqdWBB5OcBK3760IyXTm0okns8YOy7C08ALsu93mx63jaZXFqcvuggIGBVA5IpO1mjMdAiDLzaiQoP1t2wVtesr9FQbkifH9dCpTXXBP3mJ7ybGHT8tFiFlrGj82VF%2BKl8ZXN8oK6QandtaMhKGjcDFfRfx9TMdz0O9au1FcYrgwTCigylkXfT4ScRgdO%2B2g9zt3j1lVGRCT9ayaFknnX64QIUDPeaBSyW15uBrtHgzbG2t%2BitGpCR0x71hTFFmuzrBv%2Fow1JJtV4m23Y4JnZa2tWIhFJRXNXAqtTxRjnGt9cDVCDPfE0iF%2FoGAYFjaiJB4gaK4TNhz0VCQix%2Fvb1XtcVW1jEQPFYeYWfeeTrLlOp8aA0y553PzNX57ysFwzBCa7m4Db3EQ%2FgwFidDx%2FJYD4fMIa3%2F9IGOqUBF6HnLH7ZOWGGlpUcR6KgiOgGGU%2FfVQgaC2W3fvIwJHyJOPWlFe5hWGUjQnc8x0dVEm0Gcmwupwwg0ExGRA2aAaTfnMMlFHNVIJMyM3sqhK1ywCLQaDxHVonsO474bpkcbnTDsATfJzEhyFo3PrakdH2T3cz1RN58QANsL2XLiRunfPXRrmYh7rH4eDjL%2FWCtr3Q4tKfWdGOHZ%2BOIy%2Fe4vnhCMOEo&X-Amz-Signature=4cc39643254c8da5cbbe455b9d042eb00113a13c238d818a355f7cc430f55a3c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```markdown
查看 pod
# kubectl get pods
[root@m kubernetes]# kubectl get pods
No resources found in default namespace.
查看默认的命名空间
#kubectl get pods -n kub-system 存在没有运行的 pending，原因是没有网络插件

# 安装flannel网络插件(CNI)
#创建文件夹
mkdir flannel && cd flannel
#下载文件
curl -O https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml
# kube-flannel.yml里需要下载镜像,我这里提前先下载
docker pull quay.io/coreos/flannel:v0.14.0-rc1
#创建flannel网络插件
kubectl apply -f kube-flannel.yml

#过一会查看k8s集群节点,变成Ready状态了
# kubectl get nodes
NAME         STATUS   ROLES    AGE     VERSION
k8s-master   Ready    master   9m39s   v1.19.3
```


[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/36b14fe3-b705-4334-9888-9d783ae7d93c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y7YCOZDA%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCDa3y%2FLe5Iy%2BqDP3jHDcv5BgofJ6e6%2FFd7gnLc45wCYgIgI8q4v9PitvWy1s%2BkDvE%2Bc5WNyCPH0vdkOCH1Duxg1x8qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLNwKtt5LmMk5UdVjyrcA4s9MHnpiDvR9CyVhWga2U1SOH0IT4t03M1q0ERbEpFF69r5Cag6CXZZLjPfHhHlD1cFXx6GCvmR2N6LVL4vFLft4ANEaI4AOZknW1Fk48EnGrzBddUfYFl7PSrpMFgJAOhzFGNV2YYlhTlI9O%2F1NwU2R0tpXqtg05dEeEwpXoC1yJgHSllK8Y0qRrbbdATtakNwc4D2NaFndX6W0LJFg7zmW%2FMzlL7EQWqdqdWBB5OcBK3760IyXTm0okns8YOy7C08ALsu93mx63jaZXFqcvuggIGBVA5IpO1mjMdAiDLzaiQoP1t2wVtesr9FQbkifH9dCpTXXBP3mJ7ybGHT8tFiFlrGj82VF%2BKl8ZXN8oK6QandtaMhKGjcDFfRfx9TMdz0O9au1FcYrgwTCigylkXfT4ScRgdO%2B2g9zt3j1lVGRCT9ayaFknnX64QIUDPeaBSyW15uBrtHgzbG2t%2BitGpCR0x71hTFFmuzrBv%2Fow1JJtV4m23Y4JnZa2tWIhFJRXNXAqtTxRjnGt9cDVCDPfE0iF%2FoGAYFjaiJB4gaK4TNhz0VCQix%2Fvb1XtcVW1jEQPFYeYWfeeTrLlOp8aA0y553PzNX57ysFwzBCa7m4Db3EQ%2FgwFidDx%2FJYD4fMIa3%2F9IGOqUBF6HnLH7ZOWGGlpUcR6KgiOgGGU%2FfVQgaC2W3fvIwJHyJOPWlFe5hWGUjQnc8x0dVEm0Gcmwupwwg0ExGRA2aAaTfnMMlFHNVIJMyM3sqhK1ywCLQaDxHVonsO474bpkcbnTDsATfJzEhyFo3PrakdH2T3cz1RN58QANsL2XLiRunfPXRrmYh7rH4eDjL%2FWCtr3Q4tKfWdGOHZ%2BOIy%2Fe4vnhCMOEo&X-Amz-Signature=aa0060d81f1b08c6584539f67ada70cc34cff1a41c74678ee6161f289ac82bec&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```markdown
# 容器在多机上的通讯
```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/98120f21-99f2-4e70-a0b8-cb5d3ac9777f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y7YCOZDA%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCDa3y%2FLe5Iy%2BqDP3jHDcv5BgofJ6e6%2FFd7gnLc45wCYgIgI8q4v9PitvWy1s%2BkDvE%2Bc5WNyCPH0vdkOCH1Duxg1x8qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLNwKtt5LmMk5UdVjyrcA4s9MHnpiDvR9CyVhWga2U1SOH0IT4t03M1q0ERbEpFF69r5Cag6CXZZLjPfHhHlD1cFXx6GCvmR2N6LVL4vFLft4ANEaI4AOZknW1Fk48EnGrzBddUfYFl7PSrpMFgJAOhzFGNV2YYlhTlI9O%2F1NwU2R0tpXqtg05dEeEwpXoC1yJgHSllK8Y0qRrbbdATtakNwc4D2NaFndX6W0LJFg7zmW%2FMzlL7EQWqdqdWBB5OcBK3760IyXTm0okns8YOy7C08ALsu93mx63jaZXFqcvuggIGBVA5IpO1mjMdAiDLzaiQoP1t2wVtesr9FQbkifH9dCpTXXBP3mJ7ybGHT8tFiFlrGj82VF%2BKl8ZXN8oK6QandtaMhKGjcDFfRfx9TMdz0O9au1FcYrgwTCigylkXfT4ScRgdO%2B2g9zt3j1lVGRCT9ayaFknnX64QIUDPeaBSyW15uBrtHgzbG2t%2BitGpCR0x71hTFFmuzrBv%2Fow1JJtV4m23Y4JnZa2tWIhFJRXNXAqtTxRjnGt9cDVCDPfE0iF%2FoGAYFjaiJB4gaK4TNhz0VCQix%2Fvb1XtcVW1jEQPFYeYWfeeTrLlOp8aA0y553PzNX57ysFwzBCa7m4Db3EQ%2FgwFidDx%2FJYD4fMIa3%2F9IGOqUBF6HnLH7ZOWGGlpUcR6KgiOgGGU%2FfVQgaC2W3fvIwJHyJOPWlFe5hWGUjQnc8x0dVEm0Gcmwupwwg0ExGRA2aAaTfnMMlFHNVIJMyM3sqhK1ywCLQaDxHVonsO474bpkcbnTDsATfJzEhyFo3PrakdH2T3cz1RN58QANsL2XLiRunfPXRrmYh7rH4eDjL%2FWCtr3Q4tKfWdGOHZ%2BOIy%2Fe4vnhCMOEo&X-Amz-Signature=1cd28d935ead2182a3e8f233b5024eedb17dd5dfe62b82469c382bad0ce688da&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



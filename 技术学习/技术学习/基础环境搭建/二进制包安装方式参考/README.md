---
title: 二进制包安装方式参考
---

# 二进制包安装方式参考


[https://www.likecs.com/show-203610256.html](https://www.likecs.com/show-203610256.html)

```markdown
之前尝试了使用kubeadm工具来安装k8s集群，非常简单，傻瓜也会。那么，其中肯定有诈。
所以就花了些时间使用二进制文件方式来安装k8s集群。说白了 ，二进制文件就是可直接执行的底层代码，
这样的安装方式无非就是自己手动把kubeadm工具所做的事情做了。废话够多了，开始下一步吧。


# 组织架构

master：192.168.10.21    控制节点    安装etcd,kube-apiserver,kube-controller-manager,kube-scheduler

node1:    192.168.10.22    计算节点1  安装kube-proxy,kubelet

node2:    192.168.10.23   计算节点2  安装kube-proxy,kubelet

无论是master或者node，都需要提前安装好docker

# master 节点的安装
1.下载etcd二进制包

wget https://github.com/etcd-io/etcd/releases/download/v3.3.9/etcd-v3.3.9-linux-amd64.tar.gz

2.解压etcd

tar -zxvf etcd-v3.3.9-linux-amd64.tar.gz & cd etcd-v3.3.9-linux-amd64

3.将二进制包etcd,etcdctl复制到/usr/bin目录

cp etcd etcdctl /usr/bin

4.设置systemd服务文件/usr/lib/systemd/system/etcd.service

[Unit]
Description=Etcd Server
After=network.target

[Service]
Type=simple
WorkingDirectory=/var/lib/etcd/    #etcd数据保存的目录
EnvironmentFile=-/etc/etcd/etcd.conf
ExecStart=/usr/bin/etcd

[Install]
WantedBy=multi-user.target

5.增加一下etcd的存放目录，默认不存在

mkdir /var/lib/etcd

6.配置完成后，通过systemctl start 命令启动etcd服务

systemctl daemon-reload

systemctl enable etcd.service

systemctl start etcd.service

通过执行 etcdctl cluster-health 验证etcd 是否正确启动

etcdctl cluster-health

## 二.安装kube-apiserver服务
1.首先到kubernetes官网找到相应的二进制包

cd /usr/local/src/

wget https://dl.k8s.io/v1.11.0/kubernetes-server-linux-amd64.tar.gz

2.解压kubernetes-server-linux-amd64.tar.gz

tar -zxvf kubernetes-server-linux-amd64.tar.gz

cd kubernetes/server/bin & ls
```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/3b925f6a-24f7-4091-b144-52d755d6161a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SI3KBPCM%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234356Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB5Kuq5QqgWjOnoSK%2BZqViyv%2BXJaBSdJzK9w5py7rBvFAiBNxnQalikf31VZ6d%2BRPa1LEOSrAc5ul3TtdsFGN6BkaCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMV0y6R5wDSc28KKLVKtwDMenGMn0atyMbUL9Kau6tqSFZY0wzjpTl3%2BD6VYLTKDdwfbUa27HkfzVm%2FIUqaSZP3fvmsCkRdpCZOdBgFAbJSrsiaTJvz90rbnqHd3SbXOj7z87u8AeALUz3XoiKIJcYmwR3h9vo0m%2FFr9FNZg6HM8h1vqnnepIPqUkUaEr4p8iaPsi7RM%2BKad7N6%2Fsm7Gr15DfLhW36FCiroF7DHMmyMoyX%2B2kpAV7c484jiEkGbCEK3V43auQqXGokuviTu0YBMHynbbdW1QjW6YG8F1wpomayCvwGzU%2Fj9DjxR%2BHwDdyQ0y1gaDHRMQwf8vbNA4RzcS%2B8MU%2Fz8H3MBbthmIxmCjpbLXLTZPa8MS4KLxu9uXGTGIMnOIWvIuvtZ9XNr0nXUyIW%2BfQpS6CtCxfmjCXRKQWE3y6WA1cuQVjRASnJ77yTMp1sqCZKXbvKzzwFV8F1J6QJVnGj9SNI2AseLY%2BxuHiOYI2F3p%2FRXUIOEfNhgrkvkfku2eT1cuR9aoajU9EJGoh8iGblGsLdn3ZScvEM%2BjdA%2FCViuDz5rpqgiv5r7HEHXuhHu0xP4R6E%2FdhwdSZ13JXkxqYUPoqyQNmDMGw2lPshKqFy1ZfnSN5cLqiIdMPubBY9%2BcuujV7Pz4Iwu7j%2F0gY6pgEgvReu9UBnVa%2Fw0Rw7n1ia0Dwczdxtc4zaPpILDnAfNlLFBBPpXCSovE5e6pcUVG1aKX2ekyxYfW9AvCDW7dM1NOOCeT%2BBG5aRixKCtRiFNeAEb3XvD%2BJzHn5wiEovYt%2Fxt8Y7Ba%2FaB71sgPlToDBp5LjbqP50N9VHvitE%2FXu4cQ8b8oyIfmvfT5OJH7uLJjaY7lNSN9%2FXY%2FxFfI8iHTiUf2h2CWS8&X-Amz-Signature=90da4771033f6998463a0062468e8e781f9963286981bbef093be2373efe0a27&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```markdown
3.将kube-apiserver,kube-controller-manager,kube-scheduler复制到/usr/bin

cp kube-apiserver kube-controller-manager kube-scheduler /usr/bin

4.设置systemd服务文件/usr/lib/systemd/system/kube-apiserver.service

[[email protected] system]# vim kube-apiserver.service

[Unit]
Description=Kubernetes API Server
Documentation=https://github.com/kubernetes/kubernetes
After=etcd.service
Wants=etcd.service

[Service]
EnvironmentFile=/etc/kubernetes/apiserver
ExecStart=/usr/bin/kube-apiserver $KUBE_API_ARGS
Restart=on-failure
Type=notify

[Install]
WantedBy=multi-user.target

5.编辑/etc/kubernetes/apiserver

KUBE_API_ARGS="--storage-backend=etcd3 --etcd-servers=http://127.0.0.1:2379  --insecure-bind-address=0.0.0.0  --insecure-port=8080 --service-cluster-ip-range=10.10.10.0/24 --service-node-port-range=1-65535 --admission-control=NamespaceLifecycle,NamespaceExists,LimitRanger,DefaultStorageClass,ResourceQuota --logtostderr=true --log-dir=/var/log/kubernetes --v=2"


## 三.安装kube-controller-manager
1.设置systemd服务文件/usr/lib/systemd/system/kube-controller-manager.service服务

[Unit]
Description=Kubernetes Controller Manager
Documentation=https://github.com/GoogleCloudPlatform/kubernetes
After=kube-apiserver.service
Requires=kube-apiserver.service

[Service]
EnvironmentFile=-/etc/kubernetes/controller-manager
ExecStart=/usr/bin/kube-controller-manager $KUBE_CONTROLLER_MANAGER_ARGS
Restart=on-failure
LimitNOFILE=65536

[Install]
WantedBy=multi-user.target

2.编辑配置文件/etc/kubernetes/controller-manager

KUBE_CONTROLLER_MANAGER_ARGS="--master=http://192.168.10.21:8080 --logtostderr=true --log-dir=/var/log/kubernetes --v=2"

##四.安装kube-scheduler
1.设置systemd服务文件/usr/lib/systemd/system/kube-scheduler.service服务

[Unit]
Description=Kubernetes Scheduler
Documentation=https://github.com/GoogleCloudPlatform/kubernetes
After=kube-apiserver.service
Requires=kube-apiserver.service

[Service]
EnvironmentFile=-/etc/kubernetes/scheduler
ExecStart=/usr/bin/kube-scheduler $KUBE_SCHEDULER_ARGS
Restart=on-failure
LimitNOFILE=65536

[Install]
WantedBy=multi-user.target

2.编辑配置文件/etc/kubernetes/scheduler

KUBE_SCHEDULER_ARGS="--master=http://192.168.10.21:8080 --logtostderr=true --log-dir=/var/log/kubernetes --v=2"

五.启动master各个服务

systemctl daemon-reload

systemctl enable kube-apiserver.service

systemctl start kube-apiserver.service

systemctl enable kube-controller-manager.service

systemctl start kube-controller-manager.service

systemctl enable kube-scheduler

systemctl start kube-scheduler

## node节点安装
1.下载kubernetes二进制包，将里面的kubectl，kube-proxy复制到/usr/bin

cp /usr/local/src/kubernetes/server/bin/kubelet /usr/bin

cp /usr/local/src/kubernetes/server/bin/kube-proxy /usr/bin

2.配置/usr/lib/systemd/system/kubelet.service

[Unit]
Description=Kubernetes Kubelet Server
Documentation=https://github.com/GoogleCloudPlatform/kubernetes
After=docker.service
Requires=docker.service

[Service]
WorkingDirectory=/var/lib/kubelet
EnvironmentFile=-/etc/kubernetes/kubelet
ExecStart=/usr/bin/kubelet $KUBELET_ARGS
Restart=on-failure
KillMode=process

[Install]
WantedBy=multi-user.target

#3.添加参数文件/etc/kubernetes/kubelet

KUBELET_ARGS="--address=192.168.10.22 --port=10250 --cgroup-driver=systemd --hostname-override=192.168.10.22 --allow-privileged=false --kubeconfig=/etc/kubernetes/kubelet.kubeconfig --cluster-dns=10.10.10.2 --cluster-domain=cluster.local --fail-swap-on=false --logtostderr=true --log-dir=/var/log/kubernetes --v=4"

4.设置kubeconfig

cat /etc/kubernetes/kubelet.kubeconfig

apiVersion: v1
kind: Config
clusters:
  - cluster:
      server: http://192.168.10.21:8080
    name: local
contexts:
  - context:
      cluster: local
    name: local
current-context: local

5.kube-proxy服务/usr/lib/systemd/system/kube-proxy.service

[Unit]
Description=Kubernetes Kube-proxy Server
Documentation=https://github.com/GoogleCloudPlatform/kubernetes
After=network.service
Requires=network.service

[Service]
EnvironmentFile=/etc/kubernetes/proxy
ExecStart=/usr/bin/kube-proxy $KUBE_PROXY_ARGS
Restart=on-failure
LimitNOFILE=65536
KillMode=process

[Install]
WantedBy=multi-user.target

6.配置文件/etc/kubernetes/proxy

KUBE_PROXY_ARGS="--master=http://192.168.10.21:8080 --hostname-override=192.168.10.22 --logtostderr=true --log-dir=/var/log/kubernetes --v=4"

7.通过systemctl start 启动kubelet和kube-proxy服务

systemctl daemon-reload

systemctl enable kubelet.service

systemctl start kubelet.service

systemctl enable kube-proxy

systemctl start kube-proxy

8. 在master上测试node是否成功安装

kubectl get nodes
```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/7731c5c6-986e-4873-a4d0-7767d9af3b67/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SI3KBPCM%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234355Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIB5Kuq5QqgWjOnoSK%2BZqViyv%2BXJaBSdJzK9w5py7rBvFAiBNxnQalikf31VZ6d%2BRPa1LEOSrAc5ul3TtdsFGN6BkaCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMV0y6R5wDSc28KKLVKtwDMenGMn0atyMbUL9Kau6tqSFZY0wzjpTl3%2BD6VYLTKDdwfbUa27HkfzVm%2FIUqaSZP3fvmsCkRdpCZOdBgFAbJSrsiaTJvz90rbnqHd3SbXOj7z87u8AeALUz3XoiKIJcYmwR3h9vo0m%2FFr9FNZg6HM8h1vqnnepIPqUkUaEr4p8iaPsi7RM%2BKad7N6%2Fsm7Gr15DfLhW36FCiroF7DHMmyMoyX%2B2kpAV7c484jiEkGbCEK3V43auQqXGokuviTu0YBMHynbbdW1QjW6YG8F1wpomayCvwGzU%2Fj9DjxR%2BHwDdyQ0y1gaDHRMQwf8vbNA4RzcS%2B8MU%2Fz8H3MBbthmIxmCjpbLXLTZPa8MS4KLxu9uXGTGIMnOIWvIuvtZ9XNr0nXUyIW%2BfQpS6CtCxfmjCXRKQWE3y6WA1cuQVjRASnJ77yTMp1sqCZKXbvKzzwFV8F1J6QJVnGj9SNI2AseLY%2BxuHiOYI2F3p%2FRXUIOEfNhgrkvkfku2eT1cuR9aoajU9EJGoh8iGblGsLdn3ZScvEM%2BjdA%2FCViuDz5rpqgiv5r7HEHXuhHu0xP4R6E%2FdhwdSZ13JXkxqYUPoqyQNmDMGw2lPshKqFy1ZfnSN5cLqiIdMPubBY9%2BcuujV7Pz4Iwu7j%2F0gY6pgEgvReu9UBnVa%2Fw0Rw7n1ia0Dwczdxtc4zaPpILDnAfNlLFBBPpXCSovE5e6pcUVG1aKX2ekyxYfW9AvCDW7dM1NOOCeT%2BBG5aRixKCtRiFNeAEb3XvD%2BJzHn5wiEovYt%2Fxt8Y7Ba%2FaB71sgPlToDBp5LjbqP50N9VHvitE%2FXu4cQ8b8oyIfmvfT5OJH7uLJjaY7lNSN9%2FXY%2FxFfI8iHTiUf2h2CWS8&X-Amz-Signature=063ea553d4689c27d58a678e035bd2b5e64e3cf8373bff82320ac84f7aca75eb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


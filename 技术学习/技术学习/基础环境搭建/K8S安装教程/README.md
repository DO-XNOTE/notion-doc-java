---
title: K8S安装教程
---

# K8S安装教程

[file](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/d4702b2b-7541-4cbd-866e-5ddbc46fc1e8/K8S%E5%AE%89%E8%A3%85%E6%95%99%E7%A8%8B.md?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZDY32AI%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCMt4X%2FGhp3jbKlp%2FCw79iuYDFRPLCGKDC%2Bhw8pIcoEsAIgeu23%2B27pfcwcD3TVPrwx6XG%2FSiAXi1pk5F198dQ5iHkqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDKT9cWgu6Uwi%2B8suSrcAz%2FaKSVTrTFkG4Vnb%2B%2FXHcGlZboZ%2FmZQHJc%2B9uscFClfDV7YnLOKLzrU0mv9M%2BzpS7vyV9R3MW6xCF7M6UeLT%2FQA5i9JJNs%2Bvy96oBxQfTRvliPA0GPcj%2Fw53aLgh8vg1rpleMgFMvO0CFCmMla3KXQ9ylSxLIyTWDwkckYHxaWa59RU09sNO3cqNOaFRwvkYXg9dwy8ILhDJ0LjSUzTqqXzURJIF1UfSe4qgVNe%2FGOKcWNCzLT9MQhKlJmxtAuGyFWeCrtcpVm%2BgFZfP68G7yndT1MOhZ%2BQ0SXf33hhXnhrOqoKXbb42Fv4fDLnRgZAlMEZskBC28y5J6ZpAcA7wwZkeyR30WiLtKb1P%2FiC7%2B8IKy5IAnsDMQbHt1lUzI1jDm8FCeiVgMvoFAiU2ghZa%2BNoS8aG4lKNKB0wkmHDer%2BdjZrExfuNn73hqUZJx%2Bc4pX4BQ9XQtqqAgIsNADhIDkP6pGw8%2Bvk4qIZpWi7beyXqZ53ro%2F7Nvsybvh%2F9xyb4Ayt81lseb0lPTPeUGzLBFvDK2inynAT1%2BKNsuD8DkUWxZo%2B5K%2Bn7rNtYNNhTwZd9zwkX8XMnVMblKDxZQcoawEL14rA%2BgDhRaSNSLZWAaSF3pR0y42xd6Wi5t2dKMKK4%2F9IGOqUBNXN%2F6NCSO3BjER9z3z3FYudWACOQWjif3JSzRvBv7W8yS1mBanpmjaO1%2BaCnQII%2FK72CL2IaTsESkicR3VuIn60l3PWpX5u%2BuKGHXZR3gjfasTTu2W%2BHizuOe7zsyEbto2MsKxeHzPqB4Zygal0QS3FMH%2FNGhdBVaOL3kezymS07fYeG7KkGZ4o0icA%2BMS3D%2FX3TdBLYK2v6AiuHjnS%2ByFTzKJ1R&X-Amz-Signature=2fc9080f5053bdc50e7f01761f303c85f1cd8dc593fcb97d39105b14eab1fd78&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

法兰绒

[file](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/2b360c1b-9eab-47d8-890c-9e315d183581/kube-flannel.yml?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SZDY32AI%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234358Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCMt4X%2FGhp3jbKlp%2FCw79iuYDFRPLCGKDC%2Bhw8pIcoEsAIgeu23%2B27pfcwcD3TVPrwx6XG%2FSiAXi1pk5F198dQ5iHkqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDDKT9cWgu6Uwi%2B8suSrcAz%2FaKSVTrTFkG4Vnb%2B%2FXHcGlZboZ%2FmZQHJc%2B9uscFClfDV7YnLOKLzrU0mv9M%2BzpS7vyV9R3MW6xCF7M6UeLT%2FQA5i9JJNs%2Bvy96oBxQfTRvliPA0GPcj%2Fw53aLgh8vg1rpleMgFMvO0CFCmMla3KXQ9ylSxLIyTWDwkckYHxaWa59RU09sNO3cqNOaFRwvkYXg9dwy8ILhDJ0LjSUzTqqXzURJIF1UfSe4qgVNe%2FGOKcWNCzLT9MQhKlJmxtAuGyFWeCrtcpVm%2BgFZfP68G7yndT1MOhZ%2BQ0SXf33hhXnhrOqoKXbb42Fv4fDLnRgZAlMEZskBC28y5J6ZpAcA7wwZkeyR30WiLtKb1P%2FiC7%2B8IKy5IAnsDMQbHt1lUzI1jDm8FCeiVgMvoFAiU2ghZa%2BNoS8aG4lKNKB0wkmHDer%2BdjZrExfuNn73hqUZJx%2Bc4pX4BQ9XQtqqAgIsNADhIDkP6pGw8%2Bvk4qIZpWi7beyXqZ53ro%2F7Nvsybvh%2F9xyb4Ayt81lseb0lPTPeUGzLBFvDK2inynAT1%2BKNsuD8DkUWxZo%2B5K%2Bn7rNtYNNhTwZd9zwkX8XMnVMblKDxZQcoawEL14rA%2BgDhRaSNSLZWAaSF3pR0y42xd6Wi5t2dKMKK4%2F9IGOqUBNXN%2F6NCSO3BjER9z3z3FYudWACOQWjif3JSzRvBv7W8yS1mBanpmjaO1%2BaCnQII%2FK72CL2IaTsESkicR3VuIn60l3PWpX5u%2BuKGHXZR3gjfasTTu2W%2BHizuOe7zsyEbto2MsKxeHzPqB4Zygal0QS3FMH%2FNGhdBVaOL3kezymS07fYeG7KkGZ4o0icA%2BMS3D%2FX3TdBLYK2v6AiuHjnS%2ByFTzKJ1R&X-Amz-Signature=b001837e964cd507ba5595e4debe194e04282de1051e0d453808233fa2f0bc10&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```markdown
# 01 安装必要的依赖
sudo yum install -y yum-utils \
device-mapper-persistent-data \
lvm2




# 02 设置docker仓库
	sudo yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
	

#【设置要设置一下阿里云镜像加速器】

sudo mkdir -p /etc/docker

sudo tee /etc/docker/daemon.json <<-'EOF'
{  
 "registry-mirrors": ["https://registry.docker-cn.com"]
  "exec-opts": ["native.cgroupdriver=systemd"]
 }
EOF



sudo systemctl daemon-reload

#03 安装docker
yum install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
##sudo yum makecache fastç
##sudo yum -y install docker-ce

#04 启动docker
	sudo systemctl start docker && sudo systemctl enable docker
	
# 设置master的hostname，并且修改hosts文件
sudo hostnamectl set-hostname m
sudo hostnamectl set-hostname n1
sudo hostnamectl set-hostname n2

vi /etc/hosts
192.168.13.102 m
192.168.13.103 n1
192.168.13.104 n2	

# 设置worker01/02的hostname，并且修改hosts文件
sudo hostnamectl set-hostname w1
sudo hostnamectl set-hostname w2


# (1)关闭防火墙
systemctl stop firewalld && systemctl disable firewalld

# (2)关闭selinux
setenforce 0
sed -i 's/^SELINUX=enforcing$/SELINUX=permissive/' /etc/selinux/config

# (3)关闭swap
swapoff -a
sed -i '/swap/s/^\(.*\)$/#\1/g' /etc/fstab

# (4)配置iptables的ACCEPT规则
iptables -F && iptables -X && iptables -F -t nat && iptables -X -t nat && iptables -P FORWARD ACCEPT

# (5)设置系统参数
cat <<EOF >  /etc/sysctl.d/k8s.conf
net.bridge.bridge-nf-call-ip6tables = 1
net.bridge.bridge-nf-call-iptables = 1
EOF

sysctl --system


## Installing kubeadm, kubelet and kubectl
cat <<EOF > /etc/yum.repos.d/kubernetes.repo
[kubernetes]
name=Kubernetes
#baseurl=http://mirrors.aliyun.com/kubernetes/yum/repos/kubernetes-el7-x86_64
baseurl=https://mirrors.aliyun.com/kubernetes/yum/repos/kubernetes-el7-aarch64
enabled=1
gpgcheck=0
repo_gpgcheck=0
gpgkey=http://mirrors.aliyun.com/kubernetes/yum/doc/yum-key.gpg
       http://mirrors.aliyun.com/kubernetes/yum/doc/rpm-package-key.gpg
EOF


(2)安装kubeadm&kubelet&kubectl
yum install -y kubeadm-1.21.14-0 kubelet-1.21.14-0 kubectl-1.21.14-0
sudo yum install -y kubelet kubeadm kubectl

docker和k8s设置同一个cgroup
# docker
vi /etc/docker/daemon.json
   {{ "exec-opts": ["native.cgroupdriver=systemd"],}}
    
 # dockerhub 上
{
  "registry-mirrors": ["https://<my-docker-mirror-host>"]
 }
systemctl restart docker


# kubelet，这边如果发现输出 directory not exist，也说明是没问题的，大家继续往下进行即可
# (检验kubelet的cgroup的方式是否是systemd，如果不是就修改。是的话就继续-也就是正确的)
sed -i "s/cgroup-driver=systemd/cgroup-driver=cgroupfs/g" /etc/systemd/system/kubelet.service.d/10-kubeadm.conf


# kube init流程
01-进行一系列检查，以确定这台机器可以部署kubernetes

02-生成kubernetes对外提供服务所需要的各种证书可对应目录
/etc/kubernetes/pki/

03-为其他组件生成访问kube-ApiServer所需的配置文件
    ls /etc/kubernetes/
    admin.conf  controller-manager.conf  kubelet.conf  scheduler.conf
    
04-为 Master组件生成Pod配置文件。
    ls /etc/kubernetes/manifests/xxxx.yaml
    kube-apiserver.yaml 
    kube-controller-manager.yaml
    kube-scheduler.yaml
    
05-生成etcd的Pod YAML文件。
    ls /etc/kubernetes/manifests/xxxx.yaml
    kube-apiserver.yaml 
    kube-controller-manager.yaml
    kube-scheduler.yaml
	etcd.yaml
	
06-一旦这些 YAML 文件出现在被 kubelet 监视的/etc/kubernetes/manifests/目录下，kubelet就会自动创建这些yaml文件定义的pod，即master组件的容器。master容器启动后，kubeadm会通过检查localhost：6443/healthz这个master组件的健康状态检查URL，等待master组件完全运行起来

07-为集群生成一个bootstrap token

08-将ca.crt等 Master节点的重要信息，通过ConfigMap的方式保存在etcd中，工后续部署node节点使用

09-最后一步是安装默认插件，kubernetes默认kube-proxy和DNS两个插件是必须安装的

systemctl start kubelet & systemctl enable kubelet

# 本地有镜像
kubeadm init --image-repository registry.aliyuncs.com/google_containers --apiserver-advertise-address=172.16.53.107 --kubernetes-version=v1.29.3 --pod-network-cidr=10.244.0.0/16 --service-cidr=10.1.0.0/16

【若要重新初始化集群状态：kubeadm reset，然后再进行上述操作】

#创建文件夹
mkdir flannel && cd flannel
#下载文件
curl -O https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml
# kube-flannel.yml里需要下载镜像,我这里提前先下载
docker pull quay.io/coreos/flannel:v0.14.0-rc1
#创建flannel网络插件
kubectl apply -f kube-flannel.yml

#过一会查看k8s集群节点,变成Ready状态了
kubectl get nodes
NAME         STATUS   ROLES    AGE     VERSION
k8s-master   Ready    master   9m39s   v1.19.3

join其他节点到master


# 如果其他的节点没有准备好， 那可能是网路原因或者改节点上的 pod 没有运行起来
如果是网络问题需要下载网络的相关配置并与行 apply -f起来




kubeadm join 172.16.53.227:6443 --token 4vyigm.nq7vvy9ml38ydliv --discovery-token-ca-cert-hash sha256:69cd5fab6be5a2311549c111f24599a8073e449318644e59173470385a3aa161
```

卸载 k8s

[https://www.orchome.com/16614](https://www.orchome.com/16614)

## **CentOS / RHEL / Fedora**

`sudo yum remove -y kubeadm kubectl kubelet kubernetes-cni kube*   
sudo yum autoremove -y`

• autoremove：当使用yum install命令安装一枚软件包时，yum会将该软件包连同其所有依赖包一并安装到本机。但当我们使用yum remove命令卸载一枚已安装软件包时，yum默认只会移除你所指定的那枚软件包，并不会移除该包的相关依赖包。自从Fedora 18之后，可以使用yum autoremove命令来干净卸载软件包。

## **Systemd服务**

`systemctl stop kubelet
systemctl disable kubelet`

配置清理

```plain text
rm -rf /etc/systemd/system/kubelet.service
rm -rf /etc/systemd/system/kube*
```

**最后，手动清理kubernetes配置**

```plain text
sudo rm -rf ~/.kube
sudo rm -rf /etc/kubernetes/
sudo rm -rf /var/lib/kube*
```



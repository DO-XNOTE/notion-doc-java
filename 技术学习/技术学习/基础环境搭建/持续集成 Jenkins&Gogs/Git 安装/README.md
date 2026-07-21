---
title: Git 安装
---

# Git 安装

代码上传到服务器

```markdown
[root@instance-gvpb80ao ~]# yum install git -y

# 测试
[root@instance-gvpb80ao ~]# git --version

git version 1.8.3.1

# 基本配置
git config --global user.name "guojun"  #用户名
git config --global user.email "DO-XNOTE@Outlook.com"  #邮箱
git config --global user.password "guojun12"  # 密码

# 查看信息
[root@instance-gvpb80ao ~]# git config -l
user.name=guojun
user.email=DO-XNOTE@Outlook.com

[root@instance-gvpb80ao ~]# mkdir orginal_workspace
[root@instance-gvpb80ao ~]# cd orginal_workspace/
[root@instance-gvpb80ao test]# git init
# 初始化空的 Git 版本库于 /root/test/.git/
[root@instance-gvpb80ao test]# ll -a
total 0
drwxr-xr-x. 3 root root  18 Oct 21 18:22 .
drwxr-xr-x. 6 root root 102 Oct 21 18:21 ..
drwxr-xr-x. 7 root root 119 Oct 21 18:22 .git

# git可执行文件  which git    --->/usr/bin/git
```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/42f52bfa-f424-4d89-8123-586cf8faf0f9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XVOVVTJV%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDvqDWQHXiSBXUkYkcn96s62GCDKkc%2BHxH%2FP69mTCpNZAIhAJUMZweEPe3skVehSSO88stshdWZ7oXj2eNDDwYUzutnKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgzUHreIOU1ER6a2we8q3APbA3rWJ9sD%2Fm479BWRBpGTDliKnU25Occ4O7lTxLjLYEGq9DxzDLREK1Qw2T9T3%2B0NVJn%2BRXH8pc0NODAFE9QvozUrwtQyfn76skWPmULI7kLZEgxVuDyFZEEP%2F7oIg7k33vz0tCAUJAeB3O35oLaWpFTpNFR9fjn3mTpHxs9EVoaPG9xRzIzabRdjvOoR2p8Z5WwJ7Vxx6k6DGRduEDUUhYmXry8a8iSNBtWg%2FPKt%2BMt19wUyxaD5zPNx0uk6NQHl5z%2B3dZ6gGJFWgXWGX5zvsA3Keh21PsZMIrzAQRtsxwOW3uytSl8A7962DYbHTDgKjsJcBIiw8XAGtgEYpbALF2pAm0MXpXpZgHNsFeSo%2Bc%2BZTdSG%2F829ggVIve7DHsHgTylxNow1CvQwaRq5jugeCt3%2B8KR6fct4ZQrbNwJjhByTAigiZ3DzureVt1%2B%2F6DNZwjfGiS08iZJ3c6GiWCYylKosd6mTFxV%2FzTiID6sOU%2Bt6d%2FpM8IO3BN1QeN%2Fj7%2FrX9Aq%2BrqhVjCmZmtr8MdbwVnTqSa2Q95K0ZnNGbaKs0RssiQAUzQWBYVK5tSNgUYzPYfEgRLGfunWNBDLiYL9rrQOs83Lc0K6JFmom23pv5HRMK65okIOmVBPpnTCsuf%2FSBjqkATN%2BCxQR1wzuZadpBgIOzhlPT%2Fs6c6Z5gzbwOjBr4rrRVQ6hoHwkJwcCU0xCXRqrpA1F96midkZgFptVzL%2BMtB7pXJJlxu85w0f%2BRvNs%2Bu6bkzwFs4yM3VgwAu4cAs7CLO2CTLR9z%2Fn3y5OYScfP7jQwjMt3C891iH6KZbR9fwzfA%2B4QxFFunlDqP6yYFtUyzhXQ2EFXVYniIBone988Q6JU9lUX&X-Amz-Signature=1e8523b893e3121a009781d9f72a37757752c82627eeeaab7160faa4499f397e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



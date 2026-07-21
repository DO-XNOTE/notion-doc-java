---
title: homebrew
---

# homebrew

```markdown
https://zhuanlan.zhihu.com/p/90508170 

`Homebrew`是一款包管理工具，目前支持`macOS`和`linux`系统。
主要有四个部分组成: `brew`、`homebrew-core` 、`homebrew-cask`、`homebrew-bottles`。



## homebrew快速安装
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
执行此命令
```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b2759d9b-d7bc-49b4-a4fe-ca6f02cf2451/v2-c62ae8d13e72cb89e9e4770bb9a10b64_r.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SP2RFOUU%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234404Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDQjUH5oPVvaOVKVBmJKegdjRltJj%2F%2ByKbz2eDiYkW4wAiARhK8%2FDXDoVWm9RduUmVLGzkCaG5Mj8fupmf09q3GeCiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMd96cTMvvCtvYpRVXKtwDAcqzfoiJRDVn%2FtUI%2FwaDDdBIcx1kuAWxABqhmcYpX%2FvxOhEEnUmBRuGIU%2BPw300QHnQfRvdXlR%2Bzozpkqdlo3Au96J3i3nAE52wdR4RdwoRridSz32KD0djn75Es0%2FCu58EDgiBguyYB43L4%2Ffut4VC3GS5mzh9c%2BepNJK6bnyhxtRGBZMIkewzbYzlxeWI%2BrOoky3G3dTqGDFTfOWNM3gKIHkKnqXHS2m2H8rIiZrbsRlvWIrdlNxV6eDZa5yA91r4wm7Y9V0%2BMPdRI4yHX7oT5Gk8vzyBqZQG689qqf0x6AdlpML96rVVX4nRNIzNRXT1UsNgXVoXyFtd%2Fpy%2F0KhkPMSawGKqevUuG8muRdTg%2BnoONaIW%2FHrXpZnj37hxGMpbBGrkqCmTapgI75EWrEV7wkhj5PxJKOQGzS%2Bt8J%2BNdLkdzpp6H0GqO3cX8y76zMLQZngSgaeRKOnAvfsXacAI%2B59f80%2BCEpSK2C0Ipm%2BmZvncaGIBbpqWL4bLYQgMQocJ9OYRrfZKyOmD8bg4%2Bo4tawsOFAjOmTi4jbeLl0aA21D%2FUw10wqFdBJaRimk6vmQLF6uWdJgkR7MAJJhEXHteCcUWmkbBphW%2FAK%2FP8ibhnOYIQeJzCF3AEhYgw8Lr%2F0gY6pgHIFEA1589%2FxUWz8phFwL4sSF990YGa%2BOgCfYlmSJ6Tzw9QBNlnzNgHn3uLHG%2FhhDKBSNhclQHW6oGIIpVZ%2B9QX82o3xK2dPcoqkVkWoPhEofg29DuQDGWK%2FgDiG0swxpEVMhwkuo3N%2FBfDKankKqb8PJs6dfEhwGw7B6FjiV7uhcToRuHsaCaAlcS%2B%2FsBo6ZfYXl%2FdKT0slwJ0%2BBCOJ97pMZHz1ubL&X-Amz-Signature=b85a3d2247c81c104b06ed4a1ce08c385a174ae7ff363d1b0b3f53e98e54ef3e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```makefile
设置jdk的环境变量 

open -e .bash_profile 打开文件

JAVA_HOME="/Library/Java/JavaVirtualMachines/zulu-8.jdk/Content/Home"
PATH=$JAVA_HOME/bin:$PATH:.
CLASSPATH=$JAVA_HOME/lib/tools.jar:$JAVA_HOME/lib/dt.jar:.
export JAVA_HOME
export PATH
export CLASSPATH
JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk1.8.0_181.jdk/Contents/Home
CLASSPAHT=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar
PATH=$JAVA_HOME/bin:$PATH:
export JAVA_HOME
export CLASSPATH

$$maven

M3_HOME=/Applications/maven/apache-maven-3.8.4
export M3_HOME
export PATH=$MAVEN_HOME/bin:$PATH
```





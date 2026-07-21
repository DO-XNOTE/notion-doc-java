---
title: Mac安装iterm2 + oh-my-zsh + spaceship 主题
---

# Mac安装iterm2 + oh-my-zsh + spaceship 主题

1. 安装iterm2
```shell
下载安装包就可以 或者 使用 brew install iterm
```

1. brew 安装 zsh，并将其改成默认的shell
```shell
2.1 使用 brew 安装 zsh
# https://github.com/ohmyzsh/ohmyzsh/wiki/Installing-ZSH

2.2 将 ZSH 添加到 /etc/shells 文件：为了让 ZSH 成为一个有效的登录 shell，
你需要将其路径添加到 /etc/shells 文件中。可以使用以下命令来实现这一点：
echo $(which zsh) | sudo tee -a /etc/shells

2.2.1 如果实在centos平台需要将默认的bash改成zsh需要使用命令 chsh命令 ，如果找不到该命令需要安装
# sudo dnf install util-linux-user
# 然后使用  chsh -s $(which zsh) 
2.2.2 安装后若任然不可用则 
# sudo dnf update 更新
```

1. 下载插件
> 😛 github上下载 oh-my-zsh 插件  
1. 安装spaceship主题
```shell
github下载安装到.oh-my-zsh包的custom/plugins/
# https://github.com/spaceship-prompt/spaceship-prompt

配置相关的文件 ~/.config/shapcesip.zsh
# https://github.com/spaceship-prompt/spaceship-vi-mode/blob/main/README.md
# 提示设置参考： https://spaceship-prompt.sh/config/prompt/#Prompt-order
# 配置参考： https://spaceship-prompt.sh/config/intro/


安装 Fira 字体在使用 idea 的时候选择（要使用space主题的编辑显示需要安装相关字体--推荐Fira字体）
# 参考： 字体安装  https://github.com/tonsky/FiraCode/wiki
#                https://github.com/tonsky/FiraCode/wiki/Installing
# IDEA中使用参考：https://github.com/tonsky/FiraCode/wiki/Intellij-products-instructions

```

[https://github.com/tonsky/FiraCode/wiki/Intellij-products-instructions](https://github.com/tonsky/FiraCode/wiki/Intellij-products-instructions)

5.常用插件

```shell
自动提示， https://github.com/zsh-users/zsh-autosuggestions.git
高亮： https://github.com/zdharma-continuum/fast-syntax-highlighting
      https://github.com/zsh-users/zsh-syntax-highlighting.git

```

5.使其生效

```shell
vim .zshrc 加入插件， 加入主题 THEME

source ~/.zshrc



```



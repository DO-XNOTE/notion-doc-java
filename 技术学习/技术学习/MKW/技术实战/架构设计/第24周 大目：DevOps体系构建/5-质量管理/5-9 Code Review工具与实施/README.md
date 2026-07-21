---
title: 5-9 Code Review工具与实施
---

# 5-9 Code Review工具与实施

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/77f89e3a-3722-43c8-8afe-7186bf9f54f6/SCR-20240803-eaco.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665F7HJZI7%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231603Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC%2B8YISKrnsUCCcMBKz2fegKFGyVbzQmm0FumlGrD5s9AIhAOyb5G5HYKWOqbbtqKLK67K9PkAbyDMIMTe%2FYkZ%2BisUhKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwQa%2BRhylPROemCtEwq3APMU9i2DhlNbXTsbYjObOi7fO3RiJUmOJHh%2F%2BP7aScDSf8vc27nStfKt6LL1lCDXiQekxgAoHgbyPwUh5%2FEFLztC9a9byEAunTYz%2FvW4XI2qB7EcHtEnARAZCGVrRF%2BuHSYfEqC04RXxU9C3tlAD3kSsxoOH4b6P6tKOktY3FWHXb%2FZKRFW%2BK5%2F0DLOEarfX8Hs7ZB8GHTgn4BU9yBIKPBYPJfNEs6hpo4FZdpPR8pA%2Bh40HAzjTrBOi0Yu88plVqdu%2BFXzCUEu%2BHCfBnNLpQQxFoux%2FQ%2FkbowM5Ud3vb6OdEOdHCCgdMb4%2FNdfVDBKVYfCbvadSZmHVJbilvLCGYOu5pryBSpc0cOs%2Bpor4U0%2FhLP7bCngXS%2BokWwHN77mSTdw8oo6qs%2Bwqgoi3gZhXKPN%2FEkCZD%2BabnUuvzPw%2BP7blIv7gHekvq2vxlrElGA8Ei3UKxGBIQjP6yvtiybwTFmRzg%2BaS%2FIYK3p6MEBVVA%2BPhu5pDXWMFr5koyHCD%2FIlLkY2rjCh9yPSknIc12W2ItmjqsD2qgV6pscyC8jx6Ts9bSZ8E9pcb8vS8oKlVQpl7t7q0jGIcCKcwU%2Fs9lrnjKgT3ge1u97mxLFu3d0i%2BWTifHO4ooOhXUfycMCm9TCauv%2FSBjqkAe%2BWqSnNCnx322QSkE65dWN0nMT7VcjywH%2BLRWwnZhJJzhu%2Fugns%2FQuoVmjY8vnXCkF8HAn4s570N53RrolSMhgBy8JqNHOyRCsnQFc2FIco5nBmbO66dkRjLLm5PsKSLYytNAUfOiGPukZxrhDMEyj4Br1mmX8%2Far4SCn1XahIGq0KiqTICP5zNYWf9iEnWmqB8DYXoypIZ40ksnojz1MjS%2BuiA&X-Amz-Signature=93de7416c053aa8e9e1d9fc0306323277cd736c6b4215c833829f1630bdd3a53&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/70704549-f67d-4fc0-89dc-285a4aab7674/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665F7HJZI7%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231603Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC%2B8YISKrnsUCCcMBKz2fegKFGyVbzQmm0FumlGrD5s9AIhAOyb5G5HYKWOqbbtqKLK67K9PkAbyDMIMTe%2FYkZ%2BisUhKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwQa%2BRhylPROemCtEwq3APMU9i2DhlNbXTsbYjObOi7fO3RiJUmOJHh%2F%2BP7aScDSf8vc27nStfKt6LL1lCDXiQekxgAoHgbyPwUh5%2FEFLztC9a9byEAunTYz%2FvW4XI2qB7EcHtEnARAZCGVrRF%2BuHSYfEqC04RXxU9C3tlAD3kSsxoOH4b6P6tKOktY3FWHXb%2FZKRFW%2BK5%2F0DLOEarfX8Hs7ZB8GHTgn4BU9yBIKPBYPJfNEs6hpo4FZdpPR8pA%2Bh40HAzjTrBOi0Yu88plVqdu%2BFXzCUEu%2BHCfBnNLpQQxFoux%2FQ%2FkbowM5Ud3vb6OdEOdHCCgdMb4%2FNdfVDBKVYfCbvadSZmHVJbilvLCGYOu5pryBSpc0cOs%2Bpor4U0%2FhLP7bCngXS%2BokWwHN77mSTdw8oo6qs%2Bwqgoi3gZhXKPN%2FEkCZD%2BabnUuvzPw%2BP7blIv7gHekvq2vxlrElGA8Ei3UKxGBIQjP6yvtiybwTFmRzg%2BaS%2FIYK3p6MEBVVA%2BPhu5pDXWMFr5koyHCD%2FIlLkY2rjCh9yPSknIc12W2ItmjqsD2qgV6pscyC8jx6Ts9bSZ8E9pcb8vS8oKlVQpl7t7q0jGIcCKcwU%2Fs9lrnjKgT3ge1u97mxLFu3d0i%2BWTifHO4ooOhXUfycMCm9TCauv%2FSBjqkAe%2BWqSnNCnx322QSkE65dWN0nMT7VcjywH%2BLRWwnZhJJzhu%2Fugns%2FQuoVmjY8vnXCkF8HAn4s570N53RrolSMhgBy8JqNHOyRCsnQFc2FIco5nBmbO66dkRjLLm5PsKSLYytNAUfOiGPukZxrhDMEyj4Br1mmX8%2Far4SCn1XahIGq0KiqTICP5zNYWf9iEnWmqB8DYXoypIZ40ksnojz1MjS%2BuiA&X-Amz-Signature=29d19a42615f69ae09b8a4ee5a2d3caea3b6cb9c62c217fcf3abf0120a5e9e3f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

大家好，我是大木。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/27cfd6a6-b9b2-4968-bf42-65c9104ba18d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665F7HJZI7%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231603Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQC%2B8YISKrnsUCCcMBKz2fegKFGyVbzQmm0FumlGrD5s9AIhAOyb5G5HYKWOqbbtqKLK67K9PkAbyDMIMTe%2FYkZ%2BisUhKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgwQa%2BRhylPROemCtEwq3APMU9i2DhlNbXTsbYjObOi7fO3RiJUmOJHh%2F%2BP7aScDSf8vc27nStfKt6LL1lCDXiQekxgAoHgbyPwUh5%2FEFLztC9a9byEAunTYz%2FvW4XI2qB7EcHtEnARAZCGVrRF%2BuHSYfEqC04RXxU9C3tlAD3kSsxoOH4b6P6tKOktY3FWHXb%2FZKRFW%2BK5%2F0DLOEarfX8Hs7ZB8GHTgn4BU9yBIKPBYPJfNEs6hpo4FZdpPR8pA%2Bh40HAzjTrBOi0Yu88plVqdu%2BFXzCUEu%2BHCfBnNLpQQxFoux%2FQ%2FkbowM5Ud3vb6OdEOdHCCgdMb4%2FNdfVDBKVYfCbvadSZmHVJbilvLCGYOu5pryBSpc0cOs%2Bpor4U0%2FhLP7bCngXS%2BokWwHN77mSTdw8oo6qs%2Bwqgoi3gZhXKPN%2FEkCZD%2BabnUuvzPw%2BP7blIv7gHekvq2vxlrElGA8Ei3UKxGBIQjP6yvtiybwTFmRzg%2BaS%2FIYK3p6MEBVVA%2BPhu5pDXWMFr5koyHCD%2FIlLkY2rjCh9yPSknIc12W2ItmjqsD2qgV6pscyC8jx6Ts9bSZ8E9pcb8vS8oKlVQpl7t7q0jGIcCKcwU%2Fs9lrnjKgT3ge1u97mxLFu3d0i%2BWTifHO4ooOhXUfycMCm9TCauv%2FSBjqkAe%2BWqSnNCnx322QSkE65dWN0nMT7VcjywH%2BLRWwnZhJJzhu%2Fugns%2FQuoVmjY8vnXCkF8HAn4s570N53RrolSMhgBy8JqNHOyRCsnQFc2FIco5nBmbO66dkRjLLm5PsKSLYytNAUfOiGPukZxrhDMEyj4Br1mmX8%2Far4SCn1XahIGq0KiqTICP5zNYWf9iEnWmqB8DYXoypIZ40ksnojz1MjS%2BuiA&X-Amz-Signature=8b69b882a0f299f02e486b13f2064b22ce0974435ea54b29091ade2f898c8604&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

这几个来聊一聊 code review 的工具，以及利用这些工具如何去实施 code review。

[https://zhuanlan.zhihu.com/p/103592147](https://zhuanlan.zhihu.com/p/103592147)

目前 code review 的工具有很多，比方这篇文章里面分享了 16 款 code review 的工具，其中像 Gerrit、**Review Board** 等等都是非常专业的 code review 软件。


但是大木比较推崇利用 GitLab 去做 code review，在这篇文章里面写得非常详细，一起来看一下。

[https://cloud.tencent.com/developer/article/1592049](https://cloud.tencent.com/developer/article/1592049)

用 GitLab 去做 code review，步骤大概是这样的首先，创建分支。这篇文章是手动创建的，你也可以利用 Gitflow 之类的工具去创建。之后把release、 develop 以及 master 这三个分支设置成保护分支。保护分支只允许 maintainer 进行merge，而不允许直接push，而 develop 杠 1 则是非保护分支，它允许直接push。最后在开发的时候把代码提交到 develop 杠 1 分支，再去创建 merge requests，用 merge request 去做 code review。

创建 merge request 的时候，标题没有特殊要求，一般写上 merge request 的作用描述，可以提交一些描述信息，比方这个代码是用来做什么的。另外也可以描述一下 code review 的要点是什么，从而给帮助你 review 代码的人一个参考。


assign 表示 merge request 分配给谁，被分配的人将会收到邮件通知。 assign 逆和 merge 权限没有必然的关系，依然是项目的 maintainer 采用有 merge 权限。 milestone 里程碑 label 标签。这两个是可选项，比较好理解。 a previous 表示审批人必须是项目的所在组成员，如果选择了perverse，则表示这次 merge 必须经由 approvals 批准之后才能merge。最后， source branch 表示源分支， target branch 表示目标分支。意思是代码会从源分支 merge 到 target 分支之后提交 merge request。提交之后，大家就可以在 merge request 里面进行沟通了。审批人会指出这段代码存在什么问题写出来，而提交末接入 request 的人则进行修正。当改造大家都比较满意，达成一个共识的时候，就可以由 approvals 去批准并 merge 了。这样一次 code review 也就完成了。


利用 item lab 去做 code review 是比较简单的，而且非常的灵活，可以根据项目的需要进行设置。另外，由于大家对于 GitLab 普遍比较熟悉，所以学习成本也是非常低的。当然了，你也可以尝试用专门的 code review 工具去进行review。这里有 16 款，你可以尝试几款，看一看哪一款工具更加适合你们团队。总之，能够实现目的就 OK 了。小赵大楼陀螺对吧？又用 Git lab 去做 code review，实在是太简单了，所以课上我们就不去花时间演示了。


好，这节课就到这里，谢谢大家。



---
title: Best way to develop software applications
---

# Best way to develop software applications

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/72f9079e-e46f-487f-a40f-f5d8ef1d434c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466S7AD662C%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231505Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCYwaoGF7Ruqgl7zXKTQjbPlHVNq00bwBpjzQVk0LSjBAIgHIQK%2B3XwkKD7X2SsVfQV3FSioc8z80BMwkIun5wanAMqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDBVcAdeMLougHdRCpircAx4ekexcZPGrF48S8N67sg866T%2FBrbW9BTMpspw4pDyrXdb4xfwVp%2FIldopC7KL0jYlmoHK%2Bm1ANTlgcWABXGRxeoo6inN15aFBTRM%2BISD9BxPa%2FBgxarZPzoUMp%2BzBjTHCGy08G3zSUGn480H3ldPKxOWpcAMDZV0wdjJnUqTJFWszxZiJZcYy0GOxSfG4%2FpuYVKeHOpyAGMR9jEh6NvgvhkJ3Bsj59i%2BRvrTM%2F0wFpzuuKIbvxDLqwfP2two0Xu5WqFxD0C04vbpXPbvtG9OTtaHKISCU%2B%2FNSqGLE7BO5Aoy8DkthDujUtFCiInjeTuuDtCGw1yxFKIywWdTOGUsMqj%2FKDDyyILHuiFKPB%2Fj%2FWzhb0HquUKGuVtSU5Ef69YSAmy87NkEQRtN37E9WKZfhZBx5amkmLbEhQJ%2FVVioFeoiMgvMZ2y14olS036njeOxI8TxDTLfHTuvzJaNWOJSu5G1wti8BhgEAGnk2OqqMOI%2B3tvHfG1SAFtQcI6TURQP%2FgKKsQvw1kBxzWfAQnqMKZNDjzKx85%2BUXaO0DGdiJiieTZ2EE4ILXqS8Jbunm1mRuPlJBRNBiMKFg%2BZYjpT9FmPmEdA0G8FM9BgPcA2vCVKuMWcac73vpBFXwxMKa3%2F9IGOqUBddus7vFu2vBnppG%2BpE7lprT3xW7pPlp%2BEusQMfaoeSA4dVxELfPVjFmES3nAd0xZrMtsQKU5HsFLIelJRj5u6OgMA9QP5cHVOHngFn9OxoH68G1KfX66DRLMMrIqJMCEfQE0D%2FhwzrvUHxIuVv6q3F7heQZqDO7mfDBMYKahAPlT%2B95S%2F2aEMQElAP4qgwVF145Hluxmmzt8f4tvr5pTuFJjOklp&X-Amz-Signature=5314b917bf08409d42fa44a802b25e0e3f191818628c65a30f15de6e48e98af5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

all right so my last video where I just rambled and Drew diagrams did really
好吧，所以我的最后一个视频，我胡言乱语并画图，真的

well and got a lot of views so I'm going to do the exact same thing in this video
很好，并且获得了许多观看，因此我将在本视频中执行完全相同的事情

this video is kind of an extension on the last one I kind of show the process
此视频是对上一个视频的一种扩展，我展示了该过程

that I do at work kind of using a git flow approach to software development
我在工作中使用 git 流方法进行软件开发

but some people might see that and be like oh that's an old approach that's a
但有些人可能会看到这一点，并认为这是一种旧方法，这是一种

bad approach the gold standard for making software at least that's what
制作软件的糟糕方法，至少这就是

some people say is using something called trunk based development so I want
有些人说正在使用基于主干的开发，所以我想要

to kind of give you an overview of what chunk based development is and I want to
给您一个基于块的开发概述，我想

remind you as an engineer every approach has trade-offs right and it's your job
提醒您作为一名工程师，每种方法都有权衡利弊，而且这是您的工作

to decide what trade-offs work best for your team and your project that's why
决定哪种权衡最适合您的团队和项目，这就是为什么

some teams decide to use git flow it might give a little bit more stability
一些团队决定使用 git 流，它可能会提供更多稳定性

in the long run if your client is one of those people who like the moment you
从长远来看，如果你的客户是那种喜欢在您发布错误到生产环境时给您打电话并询问发生了什么事的人，那么

ship a bug to production they're calling you and asking what's going on then
也许一种工作流可能更适合您的团队，因此基于主干的开发

maybe one workflow might work better for your team so trunk based development
当您构建软件时，让我们实际讨论一下，您有多个

let's actually talk about it when you're building software you have multiple
正在尝试创建功能的开发人员，并

Developers who are trying to create features and
将它们运送到某个地方，这样您将拥有一个团队，也许该团队有六个人

ship them somewhere right so you'll have a team maybe that team has six people
也许您是一个独奏 div，也许您的项目有多个团队，所有

maybe you're a solo div maybe you have multiple teams on your project all
试图共同努力构建一个功能，现在要构建该功能，您

trying to work together to build out a feature now to build on the feature what
通常需要获取最新版本的代码，现在一个

you typically do is you need to grab the latest version of the code now one
许多人所做的约定是在 GitHub 上有一个主分支

convention that a lot of people do is on GitHub there is a main branch

so if I were to go ahead and just do like GitHub here
因此，如果我要继续并像 GitHub 一样进行操作

and say Main whenever you want to work on some code
并且在您想处理一些代码时说 Main

you're going to check off that main branch and you and your team of
您将签出该主分支，您和您的团队

developers are going to just start working on your feature now the main now
开发人员现在将开始处理您的功能，现在是主功能

the most important thing about trunk based development is that you don't have
基于主干的开发最重要的方面是您没有

a bunch of other branches you don't have like a Dev Branch you don't have like a
一堆其他分支，您没有像 Dev 分支，您没有像

staging branch is what I showed in the last video you really just work off of
暂存分支，这是我在上一个视频中展示的，您实际上只是在

this main branch and the idea is that every day you should be merging multiple
这个主分支上工作，并且这个想法是您每天都应该合并多个

PR's to Main as often as possible right you're trying
尽可能频繁地将 PR 合并到 Main，您正在尝试

to improve the continuous integration so that every piece of work that's being
改进持续集成，以便正在

worked on is continuously integrated multiple times a day now the main
现在每天持续集成多次，这是我一直在做的工作

benefits of doing this is that you get rapid feedback and you know that hey if
这样做的优点是，你可以得到快速反馈，并且你知道，嘿，如果

Dev over here is working on this feature but Dev over here is working on another
这里的开发人员正在处理此功能，但这里的开发人员正在处理另一个

feature and those features are actually having a ton of conflicts you're going
功能，并且这些功能实际上有很多冲突，你正在

to find out day one that hey maybe these two stories either need to be combined
在第一天发现，嘿，这两个故事可能需要合并

together or maybe one Dev needs to wait or maybe there's more coordination that
在一起，或者可能一个开发人员需要等待，或者可能需要更多的协调

needs to happen right so that's one of the main benefits of having trunk-based
需要立即发生，所以这是基于主干开发的主要优点之一

development is that you're continuously integrating so your March conflicts will
就是你正在持续集成，因此你的三月冲突将

happen much faster and let me kind of talk about the the other
发生得更快，让我谈谈其他

approach right if you have feature branches someone may pull a story and
方法，如果你有功能分支，有人可能会提取一个故事并

work on that for three to four weeks someone else is going to pull a story
在那上面工作三到四周，其他人会拉取一个故事

and work on it for three to four weeks and then when they're like oh my story's
并在这上面工作三到四周，然后当他们说我的故事

ready they're gonna go ahead and try to merge those changes together and you
准备好了，他们会继续尝试合并这些更改，而你

might get tons and tons of merge conflicts that's not always the case but
可能得到大量大量的合并冲突，情况并不总是如此，但

sometimes if the story was kind of really overlapping with another story it
有时如果故事与另一个故事有很大程度的重叠，它

can cause a lot of issues I'll say check off check out off Main and then I will
会导致很多问题，我会说签出主干，然后我将

just go ahead and say merge daily
继续说每天合并

so for merching daily that means that every day there's pull requests being
因此，对于每天合并，这意味着每天都有拉取请求被

opened and the team has to allocate more time another day to make sure that hey
打开，团队必须在另一天分配更多时间来确保嘿

those pull requests are getting reviewed you kind of have to prioritize reviewing
这些拉取请求正在得到审查，你必须优先审查

pull requests and merging them as often as possible otherwise you know you're
尽可能频繁地拉取请求并合并它们，否则你就会失去快速反馈和持续集成周期，因此另一个

losing that rapid feedback and continuous integration cycle so another
这确实促进的是知识共享，如果所有这些开发人员

thing this really promotes is knowledge sharing if all these developers are
基本上每天都必须审查代码并了解所有这些

basically having to review code daily and understanding what all these
每天都在更改的不同功能，有更多的知识

different features are being changed on the daily basis there's more knowledge
共享正在进行，因此一位开发人员对正在发生的变化有一个很好的了解

sharing going on so that one developer kind of has a good picture of what's
与功能分支方法相比，你可能看不到正在发生的变化

changing versus like a feature Branch approach you may not see what's being
改变，直到三周到一个月后，然后你将有一个

changed until three weeks to a month into the future and then you'll have a
拉取请求，就像 500 个文件那么长，有很多更改，让我们说实话

pull request that's like 500 files long has tons of changes and let's be honest
当一个拉取请求如此庞大时，没有人能够真正彻底地审查它，对吧

when a pull request is that big no one can actually thoroughly review it right

it's just too hard there's too much code it's too exhausting which is why another
实在太难了，代码太多，太让人筋疲力尽了，这就是为什么另一个

benefit of using trunk-based development is that your PRS are typically small you
使用基于 trunk 的开发的好处是，你的 PRS 通常很小，你可以

might have a couple of file changes you can review the pr link five minutes
可能有几个文件更改，你可以查看 pr 链接五分钟

leave a comment or just merge it if it seems good but let's kind of talk more
留下评论或如果看起来不错就合并它，但让我们更多地讨论

about the cons of this approach right if you're merging code daily into main what
关于这种方法的缺点，如果你每天将代码合并到主代码中，那么

could potentially happen is if you were to merge a bug like let's say you just
可能发生的情况是，如果你合并了一个 bug，比如你刚刚

have some bad code and you merge that to Main and then all nine year developers
有些错误的代码，你将它合并到主代码中，然后所有九年的开发者

let's say every morning they're supposed to pull main or multiple times a day
假设他们每天早上应该拉一次或多次

they pull in Maine to their side branch that bug is actually going to get merged
他们把 Maine 拉到他们的分支，那个 bug 实际上会被合并

to all of these developers right so potentially
对所有这些开发人员来说，这很有可能

you might just break work for everybody on your team
你可能只是破坏了你团队中每个人的工作

and it's kind of like a red alert situation where like okay who broke this
这就像一个红色警报的情况，比如谁破坏了这个

we got to go back and figure it out sometimes someone will have a fix and
我们必须回去弄清楚，有时有人会修复它

they'll talk about it other people might miss that message and they're just stuck
他们会谈论它，其他人可能会错过那个消息，他们只是卡住了

there for hours trying to figure out why their stuff doesn't work so
在那里花几个小时试图弄清楚为什么他们的东西不起作用

doing all these pull requests daily increases your chance of breaking stuff
每天进行所有这些拉取请求会增加你破坏东西的机会

and that's potentially bad or what if someone breaks something and goes off to
而且这可能很糟糕，或者如果有人破坏了某样东西并离开了怎么办

lunch or you know someone decides to push some code before they go on
午餐或你知道有人决定在他们继续之前推送一些代码

vacation and it breaks the entire project for everybody these are real
休假，它会破坏所有人的整个项目，这些都是真正的

issues in one circumvention of this is you have to write a lot of automated
规避此问题的一个问题是您必须编写大量的自动化

tests okay so before you're even allowed to push code into main you have tests
测试，好的，因此在您甚至被允许将代码推送到主代码之前，您就有测试

that run just go ahead and put like a little icon here
运行，继续前进，并在此处放置一个小的图标

so before you can actually merge the pr you have a bunch of tests right now the
因此，在您实际合并公关之前，您现在有一堆测试

first line of the fence is unit tests and this is one way to make sure that
围栏的第一行是单元测试，这是确保

the code you're writing is like proper I personally think integration tests are a
您编写的代码是正确的，我个人认为集成测试更有用，因此您可能还具有集成测试，因此让我们说

lot more useful so you might also have a integration test so let's say
集成测试套件，并且在该代码进入主代码之前，它必须

integration test Suite and again before this code can get into main it has to
通过单元测试集成测试，您可能已经设置了 linters

pass unit test integration test you might have a linters set up you might

have like a prettier formatter set up you might have Cypress into intest some
拥有一个更漂亮的格式化程序设置，您可能已经将 Cypress 导入 intest 中

people use playwright there's a lot of things that you could do in the pr level
人们使用 playwright，在 pr 级别有很多事情可以做

to verify that everything is good so that when you merge that PR and all
验证一切正常，以便在合并该 PR 和所有

those checks are green there's a lot lower chance that there's a breaking bug
那些检查是绿色的，出现破坏性错误的可能性很低

that makes it into all these developers now overall I say like for a smaller
这使得它进入所有这些开发人员现在总体来说，我所说的就像一个较小的

team or project this works perfectly fine right this is actually like
团队或项目，这工作得很好，这实际上就像

considered the gold standard by a lot of people because it just has a lot of
被很多人认为是黄金标准，因为它有很多

benefits and a lot of people in the industry have seen issues with just code
好处，并且业内很多人看到了仅代码的问题

that takes too long to get integrated with other code and it can cause a lot
这需要太长时间才能与其他代码集成，并且可能导致很多

of bugs and overhead now by the way is there anything I say wrong in these
错误和开销，顺便说一下，我在这些方面有什么说错的吗

videos feel free to leave a comment and call me out I'm okay with that sometimes
视频随时发表评论并叫我出来，我对此没问题，有时

I say stuff that's incorrect and we're all here to kind of learn together
我说一些不正确的话，我们都在这里一起学习

that's basically what trunk based development
这基本上是基于主干的开发

um encompasses it doesn't really talk much about the deployments although I am
um 涵盖了它，实际上并没有太多谈论部署，尽管我

going to talk about that because it's kind of important because your
会谈论它，因为它很重要，因为你的

deployment strategy kind of changes a little bit when you're doing this
部署策略在你执行此操作时会发生一些变化

approach so for anyone who's working on this community project I have this code
方法，因此对于从事此社区项目的任何人，我都有此代码

racer project this is kind of the approach that we're taking right so
赛车项目，这是我们正在采取的方法

people will make pull requests daily okay here's a bunch of pull requests
人们会每天提出请求，好的，这里有一堆请求

people kind of put images of like what changed before and after and then also
人们会放一些图片，比如前后发生了什么变化，然后还

we have a couple of checks that run we don't have testing set up yet we have
我们有一些检查正在运行，我们还没有设置测试，我们有

like linters and we try to build a project to make sure typescript works
比如 linter，我们尝试构建一个项目以确保 typescript 正常工作

fine but we've got three checks right now and when those checks are done we
很好，但我们现在有三个检查，当这些检查完成后，我们

can basically just merge that into Main and that gets deployed out to what we
基本上可以将它合并到 Main 中，然后将其部署到我们

say production let's talk about the deployment side of things so the moment
说生产，让我们谈谈事情的部署方面，所以那一刻

you merge code into main one approach that some teams and a lot of teams will
你将代码合并到主代码中，一些团队和许多团队将

do is that they will have a prod environment let's go ahead and say here
做的是他们将拥有一个 prod 环境，让我们继续说这里

do prod so what you should have is a bunch of like let's say GitHub actions
做 prod，所以你应该拥有一堆类似于 GitHub 操作的东西

I'll go like this you have a GitHub action or some teams will use Jenkins or
我会这样说，你有一个 GitHub 操作，或者一些团队将使用 Jenkins 或

Circle CI Travis CI doesn't doesn't really matter right but basically
Circle CI Travis CI 并不重要，但基本上

whenever you merge that PRN to main it's going to kick off a process that is
每当你将该 PRN 合并到主 PRN 时，它将启动一个进程

going to it that code deployed somewhere right so typically you do a build and
将代码部署到某个地方，所以通常你会进行构建，然后

then you do a deploy sometimes you could do a test in here if you think that you
然后你进行部署，有时如果你认为你

need more testing um so if you imagine this is the the
需要更多测试，嗯，所以如果你想象这是正在进行的工作，每次有人合并一个 PR，这东西就会启动

work that's being worked on every time someone merges a PR this thing kicks off
它构建你正在使用的包，比如 Docker，你可以构建一个 Docker 镜像

it builds your package you're using like Docker you could build a Docker image
并将其部署到 kubernetes 集群或类似的东西，或者你知道有很多方法可以部署你的东西，一般来说

and get that deployed to a kubernetes cluster or something like that or you
有一些可发布的东西，比如你有一个版本，这个版本有时会标记一个数字，或者你也可以像提交 Shaw 一样做

know there's tons of ways that you can deploy your stuff the general sense you
这将被推送到你的生产环境，好的，这可能就像一个网站，无论这是否是方法最简单

have some type of like releasable thing right you have like a release this is
这是你可以做到的，而且对于基于 trunk 的来说，这是一个巨大的胜利

tagged with a number sometimes or you can just do like a commit Shaw and that

is going to be pushed to your production environment okay so this could be like a

website whatever this is like the most simplest approach

that you can potentially do and again another huge win for trunk-based

development is that the workflow is super simple there's not a bunch of
开发是工作流程非常简单，没有一堆

branches you have to do there's not a bunch of back merging you have to do
分支，你必须在那里执行，没有一堆你必须执行的回退合并

there's not hot fixing that you have to do if you encounter a bug in prod you
如果在生产中遇到错误，则无需进行热修复

just do the same process you make a PR to fix the bug you get it deployed out
只需执行相同的流程，即可通过 PR 修复错误并将其部署出去

right and the idea is that this time to deployment
正确，并且想法是这次部署

should be low okay this is key here because when you
应该很低，因为当您

deploy your change if there's a bug you want to be able to fix that really
部署更改时，如果存在错误，您希望能够真正

really fast if possible if there is a feedback on a feature you want to be
尽可能快地修复它，如果对某个功能有反馈，您希望能够

able to fix that as fast as possible one example I'll give is that I actually
尽可能快地修复它，我举一个例子，我实际上

message a company and said hey it'd be really cool if your application had this
给一家公司发消息，并说嘿，如果您的应用程序具有此功能，那就太棒了

feature and within one hour they emailed me back and they said this is already
功能，在一个小时内，他们给我发了电子邮件，他们说这已经

deployed to prod we just we just implement it for you and we deployed it
部署到生产环境，我们刚刚为您实现并部署了它

that is the kind of Rapid feedback that you want to be able to achieve on your
这是您希望在您的

project when a client or customer asks for something you should be able to get
当客户要求某事时，你应该能够获得该项目

that deployed as fast as possible if needed
上实现的快速反馈类型，如果需要，可以尽快部署

right and there's a bunch of more overhead with like the project
没错，而且还有很多开销，比如项目

management side of things that like that kind of impede progress due to like
管理方面的事情，比如由于各种流程和内容而阻碍进度

various processes and stuff but that's like the gold standard right if someone
但那是黄金标准，如果有人

asks for a change or you get a bug like we should be able to get this over as
要求更改或您遇到错误，我们应该能够尽快解决，而不会破坏内容，现在有不同的方法

fast as possible without breaking stuff now there's different approaches for
部署以及一些人实际上会喜欢标记版本，所以只是

deployment as well some people will actually like tag releases so just
将内容合并到主内容中不会启动部署，有时他们实际上会

merging stuff into main won't kick off a deployment sometimes they'll actually

tag a release and that act of tagging in a new release might kick off a
标记一个版本，而标记新版本的行为可能会启动

deployment like that so that line kind of goes away
类似的部署，以便该行消失

and this is more of like a manual process sometimes you can automate it
并且这更像是一个手动过程，有时你可以自动化它

but overall the idea is the same right there's at some point you mark something
但总体而言，这个想法是相同的，在某个时刻你标记了一些东西

as this needs to go to production and then you deploy it so this potentially
因为这需要投入生产，然后你部署它，所以这可能

has a little bit of drawbacks right let's talk about some of the drawbacks
有点缺点，让我们谈谈一些缺点

if you are continuously pushing changes multiple times a day as often as
如果你每天多次持续推送更改，尽可能频繁

possible and those things are getting deployed to prod as fast and often as
并且这些东西会尽可能快且频繁地部署到生产环境中

possible and that means that you're going to have unfinished features
这意味着你将拥有未完成的功能

deploying the prod sometimes features are large you can't finish them in a day
有时部署生产环境中的功能很大，你无法在一天内完成它们

sometimes it literally takes weeks to finish the future just to do to how
有时，仅仅完成未来工作就需要数周时间，这取决于一个开发人员在这里工作八小时，并且他

complex it is if one Dev is over here working this eight hour day and he can
只能在功能中完成很多工作，这个过程是您必须获得该内容

only get so much done in the feature the process is you got to get that stuff
商户域，以便我们实际上可以集成在一起，但如果您这样做

Merchant domain so that we can actually integrate together but if you do that
这将部署产品，这意味着您的用户将获得未完成的功能，这

that deploys the prod which means that your users get unfinished features which

can be very off-putting and confusing the one approach you can take to kind of
可能会非常令人反感，并且混淆您能采取的一种方法

allow this process to work really well is doing something called feature flag
允许此流程真正有效的是执行一项称为功能标志的操作

so if I were to go ahead and add like a database what you can do is you can have
因此，如果我要继续添加一个数据库，你可以做的是你可以拥有

a feature flag I'll just say like feature flag database now this doesn't
一个功能标志，我现在只说功能标志数据库，这并不

have to live in a database this could live as environment variables on your
必须存在于数据库中，这可以作为你

deployed API this could live it's up to you right there's Services out there
部署的 API 上的环境变量，这可以存在，这取决于你，那里有服务

that you can actually integrate with I think like launch Darkly is one so like
你实际上可以与之集成，我认为像 launch Darkly 就是其中之一

there could be a you know a feature flag SAS product that you can use where
因此可能会有一个你知道的功能标志 SAS 产品，你可以使用它，其中

you're broad environment basically reads from
你广泛的环境基本上从

the SAS environment to figure out okay what needs to be turned on and off now I
SAS 环境中读取以弄清楚现在需要打开和关闭什么，我现在

do want to clarify there's two different types of flags there's deployment flags
想澄清一下，有两种不同类型的标志，有部署标志

and there's feature Flags I kind of just say feature flags for everything but if
并且有功能标志，我有点只是对所有事情都说是功能标志，但如果

you want to be like proper what we're talking about here is a deployment flag
你想成为适当的，我们在这里讨论的是一个部署标志

um a feature flag is more of like you need to actually just like test and
嗯，一个功能标志更像是你需要实际测试和

experiment different features for users you can do like a b testing with feature
为用户试验不同的功能，你可以使用功能进行类似 a b 的测试

Flags a deployment flag is basically you kick on a flag to true and then all your
标志部署标志基本上是你将标志踢为真，然后所有你的

users are able to see that uh that new feature I'll just go ahead and
用户能够看到那个呃那个新功能，我将继续

write both of them deployment Flags feature Flags the point is is that you
写下它们两个部署标志功能标志，重点是

have some type of Boolean that you can flick on and off so that when the
你有一些类型的布尔值，你可以打开和关闭，以便当

product owner or your team decides that hey this feature seems ready you can go
产品所有者或你的团队决定嘿，这个功能看起来准备好了，你可以继续

ahead and turn it on and then all your users will start seeing that I will say
打开它，然后所有你的用户将开始看到，我会说

that deployment flags and feature flags are usually easier said than done
部署标志和功能标志通常是说起来容易做起来难

because not every feature you add into your code base is just simple I added
因为并非你添加到代码库中的每个功能都简单，我添加了

like a new API or added a new page sometimes you're modifying a lot of
例如一个新的 API 或添加了一个新页面，有时你正在修改大量

existing functionality and you have to change a bunch of different places which
现有功能，并且你必须更改许多不同的地方，这

means you have feature flags and deployment Flags sprinkled all
意味着你在整个代码库中都散布着功能标志和部署标志，或者你有一个机制，比如从代码库中的集中位置读取

throughout your code base or you have a mechanism for like reading
它，并且它可能变得非常复杂，非常

it from a centralized place in your code base and it can get very complex very
快速，具体取决于你正在添加的功能类型，如果是这种情况，有时我会参考使用功能分支，如果它太复杂，并且你在到处散布标志，但我的意思是你的里程

fast depending on what type of feature that you're adding right and if that is
可能因功能而异，有时有些东西更多

the case sometimes I would refer to using like a feature Branch if it's just

too complicated and you're sprinkling Flags everywhere but I mean your mileage

may vary right depending on the feature It's just sometimes some stuff is more

complex than others so this works pretty good again this is another approach that
比其他方法复杂，所以这个方法再次很好用，这是另一种方法

a lot of teams probably do but some teams are more risk averse right if
很多团队可能都会做，但有些团队更厌恶风险，对吧

you're ever on a team or project where you deploy a bug and your client starts
如果你曾经在一个团队或项目中部署了一个 bug，你的客户开始

calling you and threatening you like hey you should not be breaking production
给你打电话并威胁你，比如嘿，你不应该破坏生产

like you keep breaking production because of this process of you guys
就像你因为这个过程不断破坏生产一样

shipping stuff too often sometimes that's when more processes are added in
太频繁地发布东西，有时会添加更多流程

and this is kind of a symptom of like maybe your test Suite is not robust
这有点像你的测试套件可能不够健壮的症状

enough maybe you're just not um you don't have enough automated tests to
也许你只是嗯，你没有足够的自动化测试来

really verify that the stuff that you're writing Works which I would probably go
真正验证你所写的东西是否有效，我可能会去

and spend more time writing more tests integration tests into in tests like
花更多时间编写更多测试，集成测试，如测试

that but if for whatever reason you're just making your client very unhappy or
但如果出于某种原因，你只是让你的客户非常不满意或

your your manager is unhappy that you just broke production for thousands of
你的经理不满意你刚刚为数千名用户破坏了生产环境

users and you've done it two days in a row that's when you start having
并且你连续两天都这样做了，这时你开始拥有

different environments kind of come into play
不同的环境开始发挥作用

so going back to like the tags the release tags if you do your deployment
所以回到标签，如果你进行部署，则释放标签

through these release tags so let's say you have a pipeline where you can just
通过这些发布标签，所以假设你有一个管道，你可以直接

go ahead and type in I want to deploy version 101 and that'll just go ahead
继续输入我想部署版本 101，然后它会继续

and grab a tag and just deploy it to prod for you okay the idea is that if
并获取一个标签，然后直接将其部署到你的产品中，好的，这个想法是，如果

your company or your team is a little bit more risk adverse or you're working
你的公司或你的团队有点厌恶风险，或者你在处理

on software that like you can't have mini production issues because you have
这样的软件，因为你不能出现小型的生产问题，因为你有

like thousands of users using this or hundreds of thousands whatever and a
数千个用户使用它，或者数十万个用户使用它，并且

single break in production means that you guys are going to be having like a
生产中的一个中断意味着你们将举行类似于

team meeting in like a a postmortem and all this other stuff and just more
事后分析的团队会议，以及所有其他内容，以及更多

processes to figure out why a single bug was added to your system I mean bugs
找出为什么向你的系统添加了一个错误，我的意思是错误

happen right I think that's also a training thing you have to realize that
发生，我认为这也是一个培训问题，你必须意识到

bugs are going to get in production but some teams are more risk adverse so you
缺陷会进入生产环境，但有些团队更厌恶风险，因此你

might have like a pre-prod environment or testing environment staging
可能有一个预生产环境或测试环境，你可以随意命名，每个团队都称之为

environment you can name this whatever you want every team calls this something
不同的东西，但基本上你可以说，好的，我想要

different but basically you could say Okay I want
部署一个新版本，我会说 1.0.2

to deploy a new version I'll say like 1.0.2
我将首先将其部署到预生产环境，以便我可以让利益相关者

I'm going to deploy this to pre-prod first so that I can have stakeholders
让我们继续并在此处进行用户操作，我可以说利益相关者，例如我说 QA

let's just go ahead and do user here I could say stakeholders like I say a QA
团队，我可以说产品负责人，基本上只是想勾选

team I could say product owner it's just basically people who want to check off
复选框上的内容并验证开发人员所做的工作

things on a check box and verify that the work being done by the developers is
在某人开始并启动此操作之前，实际上是好的

actually good before someone goes and kicks off this
实际上是好的

process um now I will say that if you have like
处理嗯，现在我要说，如果你有像

a designated QA team some
一个指定的质量保证团队，一些

agile fundamentalists will say you shouldn't have a QA team that just is a
敏捷基本主义者会说你不应该有一个质量保证团队，那只是

symptom of like you don't have proper testing I still think that no matter
症状，就像你没有进行适当的测试，我仍然认为无论

what project you're on it's good to have like someone who's able to really
你在哪个项目上，最好有像某人一样的人，他们能够真正

understand the feature being added and kind of Click through because there's
理解正在添加的功能并进行点击，因为有

actually professional QA testers who are really good at finding bugs like that's
实际上，专业的质量保证测试人员非常擅长发现此类错误，就像

their full-time job I just find bugs and they're really good at getting your
他们的全职工作，我只是发现错误，他们非常擅长让你

forms in a situation where bugs are going to happen but as you can tell this
处于错误将发生的情况中，但正如你所看到的，这

is like slowly adding more and more processes to what was working super well
就像慢慢地向原本运行良好的内容添加越来越多的流程

for your smaller scale project and team but then you know you started breaking
对于规模较小的项目和团队，但随后你知道你开始意外破坏

production on accident and now people are mad so now they're like you've got
生产，现在人们很生气，所以现在他们就像你必须

to find ways to like not break production and then you go and you add
找到方法来避免破坏生产，然后你继续，你添加

in this stuff and then hopefully it works you run into more issues you start
在这些东西中，然后希望它有效，你会遇到更多问题，你开始

changing your process more that's kind of how software development evolves and
更多地改变你的流程，这就是软件开发演变的方式，

how I've seen it um over the years of me working I will say again I want to
以及多年来我看到它如何演变，我再说一遍，我想

reiterate that your mileage will vary every team does stuff differently and
重申你的里程会有所不同，每个团队做事情的方式都不同，

that's fine dude the thing that works for your team and project like if
对于你的团队和项目来说，如果

developers are not happy with how this whole process works that's when your
开发人员对整个流程的工作方式不满意，那就是你的时候了

team has to realign and figure out how do we change the process and improve
团队必须重新调整并找出我们如何改变流程并改进

deployment speed reduce bugs like these are the kind of the goals that you're
部署速度降低错误，这些都是您要寻找的目标类型

looking for improve the developer happiness and I also say this train
提高开发人员的幸福感，我还要说培训人员，有些人有这样的心态，您永远无法将错误引入生产，但有些人有这样的心态

people right some people have this mindset that you can never get
嘿，我们有这样的管道，如果需要，我们可以在 10 分钟内部署代码修复，我很抱歉只是喋喋不休，就像我一样，它变得越来越复杂

bugs into production but some people have this mentality that
那里有一些被称为金丝雀发布的东西，所以让我们说您将您的东西部署到生产中，但您想确保没有问题，所以您所做的是您可以进行金丝雀发布，您有一个小部分用户，我们只说 5%，所有用户都使用这个新代码

hey we have this pipeline that we can deploy a code fix in 10 minutes if we
错误，这些都是您要寻找的目标类型

need to and I'm sorry for just rambling like I just it just gets more and more
提高开发人员的幸福感，我还要说培训人员，有些人有这样的心态，您永远无法将错误引入生产，但有些人有这样的心态

complex right there's there's something called like Canary releases so let's say
嘿，我们有这样的管道，如果需要，我们可以在 10 分钟内部署代码修复，我很抱歉只是喋喋不休，就像我一样，它变得越来越复杂

you deploy your stuff to production but you want to make sure that there are no
那里有一些被称为金丝雀发布的东西，所以让我们说您将您的东西部署到生产中，但您想确保没有问题，所以您所做的是您可以进行金丝雀发布，您有一个小部分用户，我们只说 5%，所有用户都使用这个新代码

issues right so what you do is you can do a canary release where you have a

small subset of users let's just say five percent all use this new code that

you guys just added so that'll be like a deployment flag or feature flag where
你们刚刚添加了，所以这将像一个部署标志或功能标志

basically you turn on and say I want new users or some subset of users sorry this
基本上，你打开并说我想要新用户或某些用户子集抱歉

might be a little small to use this new feature okay so then you might have like
可能有点小，无法使用此新功能，好吧，那么你可能需要

logging set up so I'll just go say logging which is kind of monitoring prod
设置日志记录，所以我只需说日志记录，这是一种监控产品

in checking to see if okay are any of those five percent of users are they
在检查以查看是否可以，那 5% 的用户是否

getting bugs right now are we getting a ton of like 500 errors that stuff just
现在遇到错误，我们是否收到大量类似 500 的错误，这些错误只是

keeps crashing for users if so and then you can set up an automated process to
持续为用户崩溃，如果是这样，那么你可以设置一个自动化流程

just turn off the feature flag so that everyone goes back to 100 and these
只需关闭功能标志，以便每个人都返回到 100，并且这些

people are basically like this feature is no longer on and then you can go back
人们基本上就像这个功能不再存在，然后你可以回去

to the drawing board try to fix a feature get it deployed out turn it on
到绘图板尝试修复一个功能，将其部署出去，打开它

again see if you get a bunch of errors and if you don't then you can slowly
再看看你是否会遇到一堆错误，如果没有，那么你可以慢慢地让人们越来越多地参与进来，直到你让每个人都了解这个新

start trickling people in more and more until you got everyone over to this new
功能，再次在纸上画出东西总是比

feature okay and again drawing the stuff out on paper is always much easier than
实现它容易得多，魔鬼就在细节中，就像这看起来很漂亮

implementing it the devil is in the details like this would seem pretty
简单，但对于从未实现过的人来说

simple but for someone who's never implemented before
呃，也许你正在使用 AWS 和所有其他东西，就像它可以变得非常

uh maybe you're using like AWS and all this other stuff like it can get pretty
复杂，无论如何，这是我在这段视频中要告诉你们的，希望你们喜欢，我希望你们至少从观看中学到了一件新东西

complex anyway that's all I got for you for this video hope you guys enjoy it I

hope you guys learned at least one new thing from watching this

um if you guys have ideas of something you want to see me kind of talk about I

really like just diagramming stuff and talking about it so leave a comment let
非常喜欢画图和讨论，所以请留言让我知道，也许我可以计划另一个视频，但是，像往常一样，我有一个 Discord

me know maybe I can plan another video but uh like always I have a Discord
频道，链接在下面的描述中，如果你想加入，请务必加入

channel the link is in the description below be sure to join if you want to
只是找一个与其他开发人员一起闲逛的地方，或者如果你遇到困难，只需提问

just find a place to hang out with other developers or just ask questions if
我正在努力建立一个友好的包容性社区，只是为了帮助人们

you're stuck I'm trying to build a nice inclusive community just to help people
除此之外，是的，祝你过得愉快，编码愉快

out other than that yeah have a good day happy coding


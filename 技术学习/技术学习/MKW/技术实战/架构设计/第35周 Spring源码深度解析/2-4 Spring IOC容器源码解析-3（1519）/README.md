---
title: 2-4 Spring IOC容器源码解析-3（1519）
---

# 2-4 Spring IOC容器源码解析-3（1519）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/5b187dcc-8599-42ff-9003-f027a8838047/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RECUFEHH%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232003Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDCywZxatsFVwgOGXeehB3RnW%2FNzFJ5LxOpo5h7OqugVQIgcyRuvPkPyyGck0WCzOUbnYmH%2Bm%2BjJaeQkfc7SwEETxMqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDByOJlYcGAzaj5GZ%2ByrcA%2BCDWjIyF9SZ5g8ZI0MH6gjaLE%2BerNY2XPy2fZ0WkcQRKUsa600H4bAih5%2BLxwn0XFFKhuJ6i6Zgijz%2FD%2B6udIM0pxNmB2v4UfsJ3cZ%2FCqiX8%2FoOrygng67uHEkkd7kmJx8lYY9aNU9bw3FwD5Nqs3vTI1SQ4rGhZDbry3DKOJ6DN4q6rj6hwJMcoPdA2gqRB9Bt96eEv4YozH9G1oJa%2BHoZd91PRvvw2vauoQ1E3DSx67oSipTCLioN5aTYZb1dqbdtf8KVhpe53kpYpB1mMlcHJUtPjJ4lQ4Sye9fymRJl9C028lsa8VQEKoLly%2FKrY881KLgq4c06jGq7rhZgOYE7irvLwuLCX%2BHuO3av1sxD2imTKyK5ViN7XIvBxTaPcmc2w9IS6he5RG23ClRsm2vI%2FZzuDj1CK5lj9jPr21b5ihaFf%2Bm8ZUIVLDHX%2FwY4H40tAx%2FzvZUgG4TTmuzjTMSHvlx%2BFUlOCy3OuOfEFpCiFU8r%2FYxYJvT%2FX0TJ%2F2s8STDU8%2FkoYj696IowXDfd4ie2gWjW1FS0kHR2zWtCAxmzeAIZ4GDOGxM8n2e0vgiX7%2B1Dvyug9XfqHuGL4HNHr7CsFB%2F%2BHrXggbl73QivMQ2kgtC50%2BhKgMZhjtaoMIi6%2F9IGOqUBII45lglTtQ1IBim98iPrBWKaBF7DX4uPXdOp1m3JoXlDG%2BjwtcSIw7LhsLrk0V%2ByiB2yPK1qYJZbURWNSmgKNWzpwdtuB1YQtJxYkJ6syipUZm61nPvEfyM%2Fd0uQnSoWH2eKkRIwWemiu3oPWV21jFQIvedPfDhM%2FsqQyqw0KpKdXWYS7RH9%2FcRcqDMjjzzRGTuIAKhPNoHaK8NQ6C2DEYlhWt2i&X-Amz-Signature=cbc0df8a135ea4c3a185004d8da12b7a30faf292d53fbb128aa65aa4151c4b70&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

好，那么我们现在去 debug get being 的方法，在这里面我们跟进去 get being 的方法。好，首先对于这些操作我们都可以去快速的跳过，我们直接跟进去讲 do get b，我们接下来去看里面的一些操作，这里面我们获取一下真正的 b name，这些其实对我们整个过程是没有太多的影响的，这里面是我们要 get sync tone 去获取我们的单例的操作，那么我们现在可以去进行去操作一下。跟进去。


好，在 debug 跟进去，那么在这里面首先它会去通过 single object 里面的这个 case 里面去获取，如果说获取不到的话再去创建，因为我们第一次获取它肯定是没有的，我们可以看到这里面获取的对象是一个null，通过 null 它就会去再去判断 is syncon current increasing。它的意思就是说我在获取的时候，我去判断一下我当前这个对象是否正在创建中。


我们当前是它 signal badcase，此前是now，它肯定也没有在创建的过程中，因为我们第一次进来它是一个空白的，那么接下来我们去向右看，它就会跳过这里面会直接得到一个 now 的对象，那么既然他获取他人 now 的话，那么我们就开始执行一个创建的操作了。


好，我们在这里面去看他一个执行创建的操作，这里面会有一个叫 STARTUP step，就是一个启动的过程，那么标记一下 be name，一个正在创建的过程，那么我们去对它进行一个打标，接下来我们要操作的是先获取一下我们的 being definition，获取到 being definition 去做一个 being definitely MOS。


这些常识我们可以忽略，这里面我们看它去，首先去看一下我当前这个 being definition，它有没有什么哪些依赖的对象，如果说要创建的过程中是应该去优先把它所依赖的 bin 去获取到进行创建的过程中进行装载。那么在这里面呢，我们再看待一下当前我们的是不是extend，也就是说它是不是单例的，当然我们这默认是单例的，这里面会执行我们 get sync ten 的一个操作，它最终会执行我们这里面的 get been， create been 的操作，我们可以在这里面去加入我们的断点，这里面我们看一下默认的操作。


我们这里面已经加入断点了，我们现在跳过直接到我们的断点过程，好在这里面是创建的过程，我们可以看一下这个创建的过程是在我们的 abstract out to where capable impact 里面去实现的，我们接下来继续。好在这里面去解析我们 resolve being class，也就是说通过 being definition 里面获取到我当前 being 的这个类是什么，获取到以后我们去做一个复制操作，好在这里面去解析一下我们是否需要做一些实例化之前的操作，我们可以根据你看一下，在这里面跟我们在这里面介绍的操作是执行到这一步，也就是在 create bin 里面的前一些操作，就是 resolve before instance，也就是执行我们实体化之前的操作。我们跟进去看一下。好在这里面我们看一下它的一些过程。


首先我们在这里面去找一下有没有对应的一些 being post process，我们在启动之前我们也注入了自己的 bin post process，所以说它可以自行进来，我们能看一下在这里面操作，这里面我们切记看一下，这里面是执行一个 being put the process before instance 的一个操作，那么它注的工作是什么呢？其实它就是在我们实例化之前，是不是要手工自己去注入我们实例化的操作，我们跟进去看一下，它会执行到我们自定义的方法里面。好，我们可以看到在这里面是我们 customer be impose process，在这里面会执行 before 磁力化，它在执行这个操作，这里面我们默认是 return null，我们并没有对它做什么实现。如果说我们需要对它做实现的话，我们去通过 being class 的类的名称，也就是我们的 hello bin，我们可以用我们的方式去把这个 bin 构建出来，返回过去，那么我们看一下这里面我们没有返回，那么就是它的默认行为。
那么返回过去以后，我们看一下它是一个闹，这里面我们并没有获取到结果，那么它是false，这样的话它就不会执行这个 apply being post process off 的installation，也就是说我们初始化完成的操作，那么因为我们没有实例化，所以说这一步它不会执行，那么我们接下来去继续好这个过程。它就是在我们实例化之前的一些操作，那么实例化之前并没有做任何事情，那么我们继续现在就开始真正的去执行我们 do create being 的一个操作，那么我们跟进去看一下，在这里面我们可以看到它会做一些前置的一些处理操作，这里面会执行我们的 create being intense 的一个操作，我们跟进去看一下，在这里面我们先解析出 bin 的 class 名称，我们继续。我们看一下，再找到对应的位置。


好，我们在这里面去执行我们的实例化，我们看这里面是它通过一个实例化策略的方式去实例化我们这个bin，我们可以看一下这个接口，它是有两个子类，一个是我们基于 city lab 生成一个子类作为它的代理去构建e，是个这样的实例化宾。另一种方式，一个比较简单的一 simple 这样的一种实例化策略。对于这种 simple 实例化策略，它是通过反式的方式去执行我们的构造方法来构建成我们的这个实例bin。好，我们现在回到我们的好，我们继续在这里面，我们这个 bin instance 的实例已经构建完成，构建完成以后，我们把它包装到一个 being wrapper 里面去供外部使用。


好，我们返回现在我们可以理解为我们整个这个实例化完成了，继续我们实例化完成以后，我们可以看一下这里面有需要 post across 的一些判断，在这里面是需要做一个合并的操作。我们继续，在这里面需要对我们的 bin 去做一些内容的填充，我们可以看一下这里面它做了一些哪些内容。我们断点跟进去看一下在 populate being 里面它是做了哪些。首先是看一下它有没有做一些类似于 aware 的一个 being post process 的操作，那么我们去跟进去看一下这里面我们是有相关的一些操作的，我们跟进去我们可以看到这个里面，这是我们 post part of 的instance，也就是说执行完我们的实例化操作，我们要执行的方法，那么这就到我们已有写的对应的 customer being postponed 方法里面，好，我们继续。


好指向，现在我们看一下它是不是有一些 aware 类的相关的一些 be imposed process，那么我们看一下这个也是有的，我们可以看到在这里面它会去做我们的一些 post process property，就是说做我们的属性相关的一些后处理，我们可以跟进去看一下，也到我们这应写的方法就是 post process，好，我们继续。


下面这些方法我们就不关心了，快速的跳出这个方法，现在我们看我们执行完 populate bin，那么接下来就需要对我们 bin 进行初始化，那么初始化操作也是我们的一大重点，那么我们可以跟进去仔细看一下，在这里面初始化的过程中我们去可以看到这里面有一个 inbook of where messed，它是做什么操作？就是我们可以跟进来去看一下这个方法。


在这里面我们首先看一下 BN 有没有去实现这个 aware 这个接口，如果有的话就去看一下它实现的是哪一个接口，因为我们这个 hello b n，它实现的是 b n aware 它会执行这个操作，那么我们可以把断点打到这里面，我们跟进来看一下。


好，那么断点到这里面我们去接下来看一下它是我们实现了我们的 b name where，不操作它就会执行我们的方法，在这里面可以看到执行我们的 aware 抄方法去执行 set b name 的操作。好，我们继续这样的话，就是把我们的 invoke where must 的方法做完，那么后面的是对我们 being 的去做一些操作，就是这里面是 a play being post process before in this lesson。


也就是说我们做完我们的一些属性注入，我们开始进行我们这些初始化之前的一些操作，我们跟进去看一下，在这里面我们会看到它执行的是 post process before installation 这样一个操作，我们并没有对它做什么自定义的操作，那么我们再看，接下来去执行我们的 invoke init messed，这就是执行我们一些初始化操作。


我们看一下这个初始化操作里面的内容，跟我们在这里面对应上，它执行我们insight，我们首先是执行 invoke aware master，在执行我们的初始化之前的操作。那么接下来执行我们 invoke init master，在 inmock init mess 的里面，我们跟进去看一下它出了哪些处理，在这里面我们看首先看一下这个 bin 是否实现了这个 ins lesson bin，如果实现的话，它会在这里面去执行我们的 of the property side 方法，如果说还有其他情况的话，它会执行我们的。我们可以看到这里面有一次我们自定义的，也就是说自定义的一些 init master 方法，也就是这里面是执行我们 invoke customer init messed。好，我们把代码让它执行起来。


好，这里面去执行我们的 after protosize 方法，我们可以根据你看一下这里面是执行我们的方法，好，那么行，我们接下来去看，下面就是判断一下是否要执行我们的 invoke custom init 方法，这样也是需要执行。


那么我们跟进来，因为这个方法它是使用反式的方式去执行的，找到对应反射方法执行的过程，这里面是 invoke 这个 invoke 方法会执行到我们的方法里面，执行到我们的 init mess 的方法，好跳出执行完成。那么整个这个过程我们这里面调研就是 invoke custom init mess 的方法执行完成，开始去处理我们的 post press of the inlisten，也就是说我们执行初始化的后处理，现在我们看这里面去执行我们初始化的后处理过来了，我们进行跟进，你看一下这是执行 up 的一个初始化后处理，我们执行完成这样的话整个这个创建的生命周期已就执行完成了。我们现在会通过执行完成得到我们的这个闭隐对象。好，我们快速返回执行完 do create bin，那么这样的话就把我们的 bin 呢返回出来。


OK，现在到最外层我们已经获取到我们这个闭隐对象，那么获取到我们闭隐对象以后，我们首先做了一个断言，判断一下它不会no，同时执行 say hello，这次我们的有方法，这个我们就不用再看了。紧接着执行完我们的业务方法，就需要把我们的病因容器去销毁操作，其实跟我们初始化操作对应的几件事情是需要执行完成的，我们看一下销毁操作，好，我们这里面跟进去这个销毁单例方法操作的方法，在这里面我们可以看一下，它会去做一些处理。这里面是对我们这些 disposable being name 进行一个循环处理，我们的操作就在这里面我们可以跟进去看一下，在这里面需要做的也是自行负例的方法，去，我们记得跟进去。


好，通过这里面也是执行我们 destroy b，在这里面我们应该看到它是我们需要关注的地方了，在这里面去移除对应的操作，这里面是有一个 being destroy，在这里面我们可以看到这个 being 对象，它是一个 disable post being Adapter，也就是说它是一个销毁前处理 bin 的一个适配器，那么这个适配器做了哪些事件？它就是做了我们真正的销毁操作，我们进去看一下，在这里面首先它会去执行一些销毁 aware being 的 post protect，也就是一些销毁之前的一些处理。首先我们会执行对应的操作，这里面会执行我们的执行 before 销毁 either being post process 销毁之前的一些操作。好，我们执行进去，这是跳过，那么下一步我们去看一下我们的操作是否需要去执行我们的 destroy 的方法，那么这里面我们是需要执行的，我们可以在这里面加个断点，我们看一下执行的过程，是在这里面继续执行，在执行的过程时我们跟进去。


这里面是执行 disposed being 的 destroy 方法，这是我们的执行插入。好，这是我们对应接口的方法，那么接下来去看一下我们当前是否需要进行我们的 invoke customer， destroy master 就是我们自定义的一些销毁方法，这里面我们也是因为有定义，所以说这里面去获取对应的操作，会去执行我们的操作。我们可以看到在这里面去通过反射的方式去执行我们对应的 destroy 的方法，那么我们跟进去看一下，就是到我们 destroy 的 mass 的这样一个方法。


好，这样呢整个我们销毁前的这些处理都处理完成了，那么就开始去真正的去执行我们的销毁，这是我们整个下午语的过程，那么我们可以去把我们断点的快速执行完成，我们去，执行跳出，好，现在已经回到我们的单元测试方法里面。整个过程执行完成。好，那么回到我们的PPT，我们再去看一下整个这个过程，这个我们里面也涉及到了整个病执行的这些生命周期的一个过程。我们先构建一些基础的信息，那么在这里面去装载我们的鼻音信息，装载到我们的鼻音容器里面，这里面是鼻音ignition，通过我们再去第一次去 get 鼻音的时候，去创建我们的鼻音信息，整个创建的过程中它可以去区分出我们的实例化，之前我们的实例化完成以后去创建实例化，并且去做我们的一些属性的一些预填也预处理。接下来去初始化我们的这些信息，整个初始化里面的流程，接下来去执行我们的业务类和我们的销毁方法。那么跟我们在上一节去讲到的这个整个我们的生命周期的过程其实是一样的，只是我们通过不同的角度来表现这个过程。好，整个我们对于这个 bin factory 它执行的过程跟大家先介绍到这里。


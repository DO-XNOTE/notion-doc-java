---
title: 2-3 线程池ScheduledThreadPoolExecutor详解
---

# 2-3 线程池ScheduledThreadPoolExecutor详解

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/a10bd89c-d50f-438c-8743-f889c648329c/SCR-20240728-bpif.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHPO6ADP%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230114Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCGD%2BYoL3KUmElXaIJr3i%2BrO5g7iaDG8A8EA2rBBKgTxgIhAJ6RNt%2FHi7Z8zbI3er7XJbkFEEEntnNiF%2FJd5IceMHweKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyfmoiTzyNojM%2FdOdYq3ANV9tbePI0prcOjyi314OHBrzfAinRF0nfWzPrBxxI9YDUhNZ88kCFoTu0nY7GwVk6UNJRmROdLzLeZjr7JA3DEXHpdcDpg1c%2BAKFu25stnKWr1zi4zZJfYaPafBfedE0RrRxPTzXKeradnLZVcLOKi%2F21X94gWw4r%2Bf3ICcAFcKSo9%2FanpoNN7m6Eq5%2B536VBkD0wFVGhUn7w37LK6aNBEZehCUyrg%2BACigLBsdwrly0mmPs66G0Uoj9dtAgl%2FlZvoOXaBErDqaNEwg8FELa1BldtgBj%2FbmMiXBwS5JctDMfHSUO3MEthd0s5dgCZv9d5swnzJnz%2FfmSGFFW8F3O6QcqtuWyqgmInVdxobryRkkaNhrN%2B1y9imOqlEri%2F9P6t%2F%2FyQD86tsWJ%2FsLbvFQdiB%2BWnnqbb1eemja%2BYrU3rz%2Fdf7Sa%2Fm4SdJA5LAzMr70C7fxCkmd0jRtIEK3%2B6BaT7x%2FPNYm3iGuHIFcK%2BpRUFi76e1ckYlpWn%2BtW7bBGy4pckAZRwuZ%2BaxvlkL9cK%2BZBO8YrmWeMMPXhzIAM3qMkGeRTyIJP6v9khVrtAFQfqsBPGR2wwHccS4F2Ona9v2xGIIVxz1GR%2BqNtxFyZIfGXurpIs4hIJHCq%2FM9EH8aDCQu%2F%2FSBjqkAcy7qe3C43pR30rcp2lv7YZ5vjL7HegFF42%2FL7pcSY32rFrMkiX6MfEOqP%2FAf0t%2BsVXoGyu21AbDv15k%2FgfWAh%2FFqWTCeut%2Bw%2BJscGdgP7nKkAfNm1bWpRtrJns3SCYFlZgjdO06kBaBoPcEKTjR%2F603pQ4kc1kImF%2FstGNh2%2FWEkp0rF9ZMEhDWoZ%2FNa1bcxXTk8uo58YsjhsfJOkCYgqVMy42W&X-Amz-Signature=ab8822b9503f0f9752c987a7248bcfe2b0035c562898bfcce386cc5b9fa68ab7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/adc95a1a-cade-4c8d-a742-1acac8044af5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHPO6ADP%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230114Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCGD%2BYoL3KUmElXaIJr3i%2BrO5g7iaDG8A8EA2rBBKgTxgIhAJ6RNt%2FHi7Z8zbI3er7XJbkFEEEntnNiF%2FJd5IceMHweKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyfmoiTzyNojM%2FdOdYq3ANV9tbePI0prcOjyi314OHBrzfAinRF0nfWzPrBxxI9YDUhNZ88kCFoTu0nY7GwVk6UNJRmROdLzLeZjr7JA3DEXHpdcDpg1c%2BAKFu25stnKWr1zi4zZJfYaPafBfedE0RrRxPTzXKeradnLZVcLOKi%2F21X94gWw4r%2Bf3ICcAFcKSo9%2FanpoNN7m6Eq5%2B536VBkD0wFVGhUn7w37LK6aNBEZehCUyrg%2BACigLBsdwrly0mmPs66G0Uoj9dtAgl%2FlZvoOXaBErDqaNEwg8FELa1BldtgBj%2FbmMiXBwS5JctDMfHSUO3MEthd0s5dgCZv9d5swnzJnz%2FfmSGFFW8F3O6QcqtuWyqgmInVdxobryRkkaNhrN%2B1y9imOqlEri%2F9P6t%2F%2FyQD86tsWJ%2FsLbvFQdiB%2BWnnqbb1eemja%2BYrU3rz%2Fdf7Sa%2Fm4SdJA5LAzMr70C7fxCkmd0jRtIEK3%2B6BaT7x%2FPNYm3iGuHIFcK%2BpRUFi76e1ckYlpWn%2BtW7bBGy4pckAZRwuZ%2BaxvlkL9cK%2BZBO8YrmWeMMPXhzIAM3qMkGeRTyIJP6v9khVrtAFQfqsBPGR2wwHccS4F2Ona9v2xGIIVxz1GR%2BqNtxFyZIfGXurpIs4hIJHCq%2FM9EH8aDCQu%2F%2FSBjqkAcy7qe3C43pR30rcp2lv7YZ5vjL7HegFF42%2FL7pcSY32rFrMkiX6MfEOqP%2FAf0t%2BsVXoGyu21AbDv15k%2FgfWAh%2FFqWTCeut%2Bw%2BJscGdgP7nKkAfNm1bWpRtrJns3SCYFlZgjdO06kBaBoPcEKTjR%2F603pQ4kc1kImF%2FstGNh2%2FWEkp0rF9ZMEhDWoZ%2FNa1bcxXTk8uo58YsjhsfJOkCYgqVMy42W&X-Amz-Signature=7e4468a26afbd4afdce608700fda6970dcf032b14d4e58666d727a199a864b7b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/29f85475-c7c0-4d0c-afb7-711752c7bdfa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHPO6ADP%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230114Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCGD%2BYoL3KUmElXaIJr3i%2BrO5g7iaDG8A8EA2rBBKgTxgIhAJ6RNt%2FHi7Z8zbI3er7XJbkFEEEntnNiF%2FJd5IceMHweKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyfmoiTzyNojM%2FdOdYq3ANV9tbePI0prcOjyi314OHBrzfAinRF0nfWzPrBxxI9YDUhNZ88kCFoTu0nY7GwVk6UNJRmROdLzLeZjr7JA3DEXHpdcDpg1c%2BAKFu25stnKWr1zi4zZJfYaPafBfedE0RrRxPTzXKeradnLZVcLOKi%2F21X94gWw4r%2Bf3ICcAFcKSo9%2FanpoNN7m6Eq5%2B536VBkD0wFVGhUn7w37LK6aNBEZehCUyrg%2BACigLBsdwrly0mmPs66G0Uoj9dtAgl%2FlZvoOXaBErDqaNEwg8FELa1BldtgBj%2FbmMiXBwS5JctDMfHSUO3MEthd0s5dgCZv9d5swnzJnz%2FfmSGFFW8F3O6QcqtuWyqgmInVdxobryRkkaNhrN%2B1y9imOqlEri%2F9P6t%2F%2FyQD86tsWJ%2FsLbvFQdiB%2BWnnqbb1eemja%2BYrU3rz%2Fdf7Sa%2Fm4SdJA5LAzMr70C7fxCkmd0jRtIEK3%2B6BaT7x%2FPNYm3iGuHIFcK%2BpRUFi76e1ckYlpWn%2BtW7bBGy4pckAZRwuZ%2BaxvlkL9cK%2BZBO8YrmWeMMPXhzIAM3qMkGeRTyIJP6v9khVrtAFQfqsBPGR2wwHccS4F2Ona9v2xGIIVxz1GR%2BqNtxFyZIfGXurpIs4hIJHCq%2FM9EH8aDCQu%2F%2FSBjqkAcy7qe3C43pR30rcp2lv7YZ5vjL7HegFF42%2FL7pcSY32rFrMkiX6MfEOqP%2FAf0t%2BsVXoGyu21AbDv15k%2FgfWAh%2FFqWTCeut%2Bw%2BJscGdgP7nKkAfNm1bWpRtrJns3SCYFlZgjdO06kBaBoPcEKTjR%2F603pQ4kc1kImF%2FstGNh2%2FWEkp0rF9ZMEhDWoZ%2FNa1bcxXTk8uo58YsjhsfJOkCYgqVMy42W&X-Amz-Signature=ffc068c53efc0cde2037dc1b4553068d3c46495850f30b889bbf33fd7db42382&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

大家好，我是大木。前面我们都是用 thread pull executor 创建线程池的。这一节我们来探讨 schedule 的 thread pull executor。 

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/0309caa9-8f5b-4df0-b47e-baf0cc54ec35/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHPO6ADP%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230114Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCGD%2BYoL3KUmElXaIJr3i%2BrO5g7iaDG8A8EA2rBBKgTxgIhAJ6RNt%2FHi7Z8zbI3er7XJbkFEEEntnNiF%2FJd5IceMHweKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyfmoiTzyNojM%2FdOdYq3ANV9tbePI0prcOjyi314OHBrzfAinRF0nfWzPrBxxI9YDUhNZ88kCFoTu0nY7GwVk6UNJRmROdLzLeZjr7JA3DEXHpdcDpg1c%2BAKFu25stnKWr1zi4zZJfYaPafBfedE0RrRxPTzXKeradnLZVcLOKi%2F21X94gWw4r%2Bf3ICcAFcKSo9%2FanpoNN7m6Eq5%2B536VBkD0wFVGhUn7w37LK6aNBEZehCUyrg%2BACigLBsdwrly0mmPs66G0Uoj9dtAgl%2FlZvoOXaBErDqaNEwg8FELa1BldtgBj%2FbmMiXBwS5JctDMfHSUO3MEthd0s5dgCZv9d5swnzJnz%2FfmSGFFW8F3O6QcqtuWyqgmInVdxobryRkkaNhrN%2B1y9imOqlEri%2F9P6t%2F%2FyQD86tsWJ%2FsLbvFQdiB%2BWnnqbb1eemja%2BYrU3rz%2Fdf7Sa%2Fm4SdJA5LAzMr70C7fxCkmd0jRtIEK3%2B6BaT7x%2FPNYm3iGuHIFcK%2BpRUFi76e1ckYlpWn%2BtW7bBGy4pckAZRwuZ%2BaxvlkL9cK%2BZBO8YrmWeMMPXhzIAM3qMkGeRTyIJP6v9khVrtAFQfqsBPGR2wwHccS4F2Ona9v2xGIIVxz1GR%2BqNtxFyZIfGXurpIs4hIJHCq%2FM9EH8aDCQu%2F%2FSBjqkAcy7qe3C43pR30rcp2lv7YZ5vjL7HegFF42%2FL7pcSY32rFrMkiX6MfEOqP%2FAf0t%2BsVXoGyu21AbDv15k%2FgfWAh%2FFqWTCeut%2Bw%2BJscGdgP7nKkAfNm1bWpRtrJns3SCYFlZgjdO06kBaBoPcEKTjR%2F603pQ4kc1kImF%2FstGNh2%2FWEkp0rF9ZMEhDWoZ%2FNa1bcxXTk8uo58YsjhsfJOkCYgqVMy42W&X-Amz-Signature=abc63ed439ac953d4cf0009b105a39b1dd076e10c69038f517ebe08dc2598be4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

scheduled thread pull executor 是 Threadpool executor 的子类，它扩展了 Threadpool executor，在原有功能的基础上，额外支持了延时执行任务以及周期性执行任务。好，来写代码，创建一个类叫 schedule 的。 threader full executor。Test， p s v m 创建边方法 new schedule 的 thread pull executor。打包。 scheduled thread pull executor 也有多个构造方法，最多可以传入 3 个参数。我们跟踪进源码看一下。第一个参数 core process 核心线程数，第二个是线程工厂，第三个是拒绝策略。在里面它是 super 调用了 thread pull executor 的构造方法。


好，我们写一下核心线程 10 县城工厂， executors default threat factory 拒绝策略。我们用默认的 about policy，宪政治就创建好了。
scheduled thread pull executed。


核心方法都以 schedule 开头，有 4 个。当然了，由于 schedule 的 Threadpool executor 继承自 threadpool executor，所以前面我们讲解的 Threadpool executor 的核心 API 都可以继续使用。


好，我们来用schedule。第一个是传入一个 run able delay time unit try again ramabo，在里面打印一下，叫AA。第二个参数叫delay，比如三。第三个是 time unit。这样表达的意思是，延时 3 秒之后再去执行 runable 任务。好，我们启动一下看看。协调好了，等待等了 3 秒左右，答应了。
schedule 也可以传入 call able， new cayable，string， return 一个b。第二个参数也是delay，比如4。第三个参数也是他们unit，他表达的意思。延时 3 秒之后执行任务 call able，它可以拿到执行的结果，对吧？所以这个方法它有返回。返回了 scheduled future，你可以用 future 点get。拿到这里的b， b b，异常，抛出去打印一下s，执行看看。


可以看到过了 4 秒之后，打印了 b b b。我们把注释完善一下，可以返回执行结果。
第三个方法， schedule at fix rate，可以插入一个runable。我们还是打印一个CCC，这个参数就比较多了。我们写一下。
第二个参数叫 initial delay，它表示第一次执行任务时延时多久。这里这个方法一旦执行第一次，不会做任何延迟，直接执行这个任务。 3 表示每隔多久直行任务。也就是这样写，每隔 3 秒就会执行一次任务。好，我们把前面的代码都注释掉。启动。


可以看到，一开始没有做任何延迟，就打印了 c c c 之后每隔 3 秒左右会再次执行任务。第四个方法，叫 schedule with fixed delay，它的参数和 schedule at fixed rate 一模一样。我们 copy 过来。这个方法表达的是什么意思？ initial delay 指的也是第一次执行任务的时候延时多久。但是这里的 delay 表达的意思不一样，他表示每次，执行完任务之后，延迟多久再次执行任务。


为了更好的说明这两个方法之间的区别，所以我们这里可以加一个 thread 点儿sleep， 1 秒，打印的时候做一点处理，叫 schedule at fixed rate，加上，系统的当前时间，汤里， cover 一下，把这里改掉。好，长期。


停掉。我们来分析这个结果。可以看到 schedule at fixed rate，是每隔 3 秒打印一次的， our schedule with fixed delay 它是每隔 4 秒打印的。这是为什么？我们来分析一下。大家想第一次执行没有延迟，立马执行了，先打印，然后睡了 1 秒。执行完了之后，它延迟了 3 秒，再次执行 3 + 1 = 4。总结一下， schedule 的 thread pool executor 有 4 个核心API。 schedule 传入 runable 表示延迟多久之行。传入 call able 作用和传入 runable 是一样的，但是它可以拿到任务的返回结果。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/89f74b7a-819e-4ea6-ba7e-d25bc5864f51/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SHPO6ADP%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230113Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCGD%2BYoL3KUmElXaIJr3i%2BrO5g7iaDG8A8EA2rBBKgTxgIhAJ6RNt%2FHi7Z8zbI3er7XJbkFEEEntnNiF%2FJd5IceMHweKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyfmoiTzyNojM%2FdOdYq3ANV9tbePI0prcOjyi314OHBrzfAinRF0nfWzPrBxxI9YDUhNZ88kCFoTu0nY7GwVk6UNJRmROdLzLeZjr7JA3DEXHpdcDpg1c%2BAKFu25stnKWr1zi4zZJfYaPafBfedE0RrRxPTzXKeradnLZVcLOKi%2F21X94gWw4r%2Bf3ICcAFcKSo9%2FanpoNN7m6Eq5%2B536VBkD0wFVGhUn7w37LK6aNBEZehCUyrg%2BACigLBsdwrly0mmPs66G0Uoj9dtAgl%2FlZvoOXaBErDqaNEwg8FELa1BldtgBj%2FbmMiXBwS5JctDMfHSUO3MEthd0s5dgCZv9d5swnzJnz%2FfmSGFFW8F3O6QcqtuWyqgmInVdxobryRkkaNhrN%2B1y9imOqlEri%2F9P6t%2F%2FyQD86tsWJ%2FsLbvFQdiB%2BWnnqbb1eemja%2BYrU3rz%2Fdf7Sa%2Fm4SdJA5LAzMr70C7fxCkmd0jRtIEK3%2B6BaT7x%2FPNYm3iGuHIFcK%2BpRUFi76e1ckYlpWn%2BtW7bBGy4pckAZRwuZ%2BaxvlkL9cK%2BZBO8YrmWeMMPXhzIAM3qMkGeRTyIJP6v9khVrtAFQfqsBPGR2wwHccS4F2Ona9v2xGIIVxz1GR%2BqNtxFyZIfGXurpIs4hIJHCq%2FM9EH8aDCQu%2F%2FSBjqkAcy7qe3C43pR30rcp2lv7YZ5vjL7HegFF42%2FL7pcSY32rFrMkiX6MfEOqP%2FAf0t%2BsVXoGyu21AbDv15k%2FgfWAh%2FFqWTCeut%2Bw%2BJscGdgP7nKkAfNm1bWpRtrJns3SCYFlZgjdO06kBaBoPcEKTjR%2F603pQ4kc1kImF%2FstGNh2%2FWEkp0rF9ZMEhDWoZ%2FNa1bcxXTk8uo58YsjhsfJOkCYgqVMy42W&X-Amz-Signature=bf26a1a199175f5c64c9625d0172f46c356cdba96f01ad3b50eb5eb4a15e9708&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

schedule at a fixed rate 表示每隔多久执行一次。 schedule with fixed delay 表示每次任务执行之后延迟多久再次执行。此期项目中，我们经常会使用后面这两个方法，特别是 schedule at a fixed rate 方法，经常用来实现定时任务。


说到定时任务，同学们很可能会想到timer。那么 scheduled thread pull executor 和 timer 之间有什么区别？这篇文章详细对比了 scheduled thread pool executor 和timer，写得非常的棒，值得一看。我直接说一下对比的结果是单线程的，用法大致上是这样子的，如果一个任务阻塞的时间比较久，可能会影响到下一个任务的执行。


第二是使用 timer 的时候，如果你的任务抛异常，会导致尚未执行的其他任务不能执行下去。所以一般来说，实际项目中应该尽可能的使用 schedule 的 thread poor executor，慎用timer。好，这节课就到这里，谢谢大家。







---
title: 2-5 Kafka海量日志收集实战_filebeat日志收集实战-2
---

# 2-5 Kafka海量日志收集实战_filebeat日志收集实战-2

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/49fcb50b-d811-4c04-8eb7-7895bcbd6ee1/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666JIO52YX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225327Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAR5phXQ7c0wCtyv07NWRLxBTfTVx44HtRV8PhZR7wqVAiBlskCxv1qNS2IHTvg8b4ahHaLpqO6fZfnbCx8sTBJITSqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMghl7ybVBOmqf90g4KtwD7bfAwIGUFAmy8CmpRrXkbNedpq%2FjF1Dt451o5borwRbu6dGW7XyyI6QuyLAwY4K3crkFr2ZvbOAfv9SfRbs5LXDRPSUSDl7YsZQCKZvv8ethnaCkI0OdW1xUxNe9MT%2BpD%2FGW5HrPcBocgW9oJBUSym%2BdeZ%2BxpkgylyhbglfClZKCYwWmMCZIxAE5hJhGJmLIGnvyEGwBvAVMbumZjauzTTbmFOec5vPDl4pPNUORUIDkSub1NeBfFwMf7bWs79NMAxN%2B%2B7XpOo%2FWuylQSXWrt6puCTuHazZKrmTGj2mFNDZ2yY2ob9ytscUcWfYeqh9Azl4jMN6%2B4GSc5VqSxKLmzoUjCQSAGCdslRuVwCfBiLMAx5M%2BuKzWi%2FfOHF7Ru6A0M8KnADpFNto2WGHetD2dXjtrBqL%2FcZBiNpNtiI%2BQDXezM0MJXdhQ1Zw2VdcXbDX1KAUm%2BaXOG1DBacJQ2iyPDMyNcGP6gtK0BpFD9vc1ow2HpLeHLeEsdm1ERQ5jtZKcZ8nff38hLI9w60bwGyHVlsgh2bKsT7P26hBOEE9jzb5cNnElxro7kyoDwqYmXTRnK5MT4dyFphwxK%2FXGWK9ZRxRusbs7gI63U0tdfdrKw7UghkEkhCVYL34fz4Qw17r%2F0gY6pgFSZB62dJm6R3RlsI9%2FWWB3IsGEm%2BQ%2FyKX4L63hs3MINOJiV1Ne2KvsQI%2BVctSUQmy2pq6izbaeEYwIrbksUktetNRXyyTkHE4t0taKlFMZyYhhCEtr4az2qZRVqkfAbF9o97xkaSH0HVFCF3lcUahL6jCYJYgn%2FpL87VdHfABS5qVHpDBmgKWYMFv6r7ZTBNI9KjsF4R8O130idNxejttB1yod7IiW&X-Amz-Signature=8a150708cccaa1ca94228d0400e8c3740ce99f1e56a1d836b3056ce039af6d71&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/476dbc3e-cf04-4280-9921-6364245e6a34/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666JIO52YX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225327Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAR5phXQ7c0wCtyv07NWRLxBTfTVx44HtRV8PhZR7wqVAiBlskCxv1qNS2IHTvg8b4ahHaLpqO6fZfnbCx8sTBJITSqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMghl7ybVBOmqf90g4KtwD7bfAwIGUFAmy8CmpRrXkbNedpq%2FjF1Dt451o5borwRbu6dGW7XyyI6QuyLAwY4K3crkFr2ZvbOAfv9SfRbs5LXDRPSUSDl7YsZQCKZvv8ethnaCkI0OdW1xUxNe9MT%2BpD%2FGW5HrPcBocgW9oJBUSym%2BdeZ%2BxpkgylyhbglfClZKCYwWmMCZIxAE5hJhGJmLIGnvyEGwBvAVMbumZjauzTTbmFOec5vPDl4pPNUORUIDkSub1NeBfFwMf7bWs79NMAxN%2B%2B7XpOo%2FWuylQSXWrt6puCTuHazZKrmTGj2mFNDZ2yY2ob9ytscUcWfYeqh9Azl4jMN6%2B4GSc5VqSxKLmzoUjCQSAGCdslRuVwCfBiLMAx5M%2BuKzWi%2FfOHF7Ru6A0M8KnADpFNto2WGHetD2dXjtrBqL%2FcZBiNpNtiI%2BQDXezM0MJXdhQ1Zw2VdcXbDX1KAUm%2BaXOG1DBacJQ2iyPDMyNcGP6gtK0BpFD9vc1ow2HpLeHLeEsdm1ERQ5jtZKcZ8nff38hLI9w60bwGyHVlsgh2bKsT7P26hBOEE9jzb5cNnElxro7kyoDwqYmXTRnK5MT4dyFphwxK%2FXGWK9ZRxRusbs7gI63U0tdfdrKw7UghkEkhCVYL34fz4Qw17r%2F0gY6pgFSZB62dJm6R3RlsI9%2FWWB3IsGEm%2BQ%2FyKX4L63hs3MINOJiV1Ne2KvsQI%2BVctSUQmy2pq6izbaeEYwIrbksUktetNRXyyTkHE4t0taKlFMZyYhhCEtr4az2qZRVqkfAbF9o97xkaSH0HVFCF3lcUahL6jCYJYgn%2FpL87VdHfABS5qVHpDBmgKWYMFv6r7ZTBNI9KjsF4R8O130idNxejttB1yod7IiW&X-Amz-Signature=4ed0bba84528bc4849821d9d37afccc2e659bf19ef789e063a711c005b346d2f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

OK 那现在已经打包好了，那我们现在把这个 connector 对应的这个文件去上传到我们的这个服务器上。好，那我们直接拖过来传上来之后，接下来我们要做的事情就是我们 Java 杠 jar 我们去启动这个凯莱克的运营服务。暗的雨后缀表示我们去后台进行去启动。启动了之后，然后我们来观察一下它的这个日志，看看它的日志是否都有来耐心等待一下。 OK 他现在这个 spring boot 工程已经启动起来了，然后已经用了 7 秒多钟对吧。已经 start application 然后端口是多少呢？我们找一下门口是 8001 对吧没问题。


好，接下来其实我们就可以去来看一看它有没有生成这个 logs 文件夹。大家可以看到这个 logs 文件夹已经有了，对不对？我们 CD 到这个 logs 下面，你看它里面有两个文件，一个是 App 杠 collector.log 还有一个是 error 杠 collector.log 两个文件都有了之后，其实我们可以 cat 其中一个 App 它应该是有内容的对不对？好，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/de870d6f-01d0-4e27-94ac-10ec22b217b3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666JIO52YX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225327Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAR5phXQ7c0wCtyv07NWRLxBTfTVx44HtRV8PhZR7wqVAiBlskCxv1qNS2IHTvg8b4ahHaLpqO6fZfnbCx8sTBJITSqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMghl7ybVBOmqf90g4KtwD7bfAwIGUFAmy8CmpRrXkbNedpq%2FjF1Dt451o5borwRbu6dGW7XyyI6QuyLAwY4K3crkFr2ZvbOAfv9SfRbs5LXDRPSUSDl7YsZQCKZvv8ethnaCkI0OdW1xUxNe9MT%2BpD%2FGW5HrPcBocgW9oJBUSym%2BdeZ%2BxpkgylyhbglfClZKCYwWmMCZIxAE5hJhGJmLIGnvyEGwBvAVMbumZjauzTTbmFOec5vPDl4pPNUORUIDkSub1NeBfFwMf7bWs79NMAxN%2B%2B7XpOo%2FWuylQSXWrt6puCTuHazZKrmTGj2mFNDZ2yY2ob9ytscUcWfYeqh9Azl4jMN6%2B4GSc5VqSxKLmzoUjCQSAGCdslRuVwCfBiLMAx5M%2BuKzWi%2FfOHF7Ru6A0M8KnADpFNto2WGHetD2dXjtrBqL%2FcZBiNpNtiI%2BQDXezM0MJXdhQ1Zw2VdcXbDX1KAUm%2BaXOG1DBacJQ2iyPDMyNcGP6gtK0BpFD9vc1ow2HpLeHLeEsdm1ERQ5jtZKcZ8nff38hLI9w60bwGyHVlsgh2bKsT7P26hBOEE9jzb5cNnElxro7kyoDwqYmXTRnK5MT4dyFphwxK%2FXGWK9ZRxRusbs7gI63U0tdfdrKw7UghkEkhCVYL34fz4Qw17r%2F0gY6pgFSZB62dJm6R3RlsI9%2FWWB3IsGEm%2BQ%2FyKX4L63hs3MINOJiV1Ne2KvsQI%2BVctSUQmy2pq6izbaeEYwIrbksUktetNRXyyTkHE4t0taKlFMZyYhhCEtr4az2qZRVqkfAbF9o97xkaSH0HVFCF3lcUahL6jCYJYgn%2FpL87VdHfABS5qVHpDBmgKWYMFv6r7ZTBNI9KjsF4R8O130idNxejttB1yod7IiW&X-Amz-Signature=5fd60a41d1227a8c779a17c7edde5cef7e8fcf49fd0a3cd00b6fd0c5482b9e0a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那我们再 cat 我们的这个 error 没有内容对吧？好了，现在对应着我们的应用服务已经起来了，那接下来要做什么事情呢？我们想一想，应用服务起来了，接下来我们马上要启动我们的 file beat 去来监控这两个文件，它如果有内容变更，那我们其实就可以把它扔到我们的 kafka 上。


那对应着我们的卡夫卡，我们来看看卡夫卡 GPS 一下卡夫卡的应用程序已经启动了对吧，那接下来我们要做什么呢？首先我们不要着急，我们来往下走，来看一下我们的这个文档 Docs 这个 file beat 文档。好，那对应的这个文档说我们可以启动 file beat 对吧，我们肯定是要启动 file beat 的。当然在启动这个 file beat 之前，我们要做的事情是什么呢？我们要先启动卡夫卡。


我们现在卡夫卡已经起来了，然后这个列表我们刚才已经查看了，接下来我们要创建两个 topic 为什么要创建 topic 呢？一个是 App 杠 log 杠 connector 还有一个是 error 杠 log 杠 collector 为什么要创建这两个 topic 因为我们在真正的去做实际的处理的时候，我们的 fail beat 是要把消息放到我们的卡夫卡上的对吧，要把消息扔到卡夫卡上，那你对应着往哪个 topic 去扔，所以说你先应该把这个 topic 放进去。好在这里头我们直接回车，我们先创建一个这个已经 OK 了。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/a6bd5e5a-d60c-465e-a0b2-bbf20cec8c42/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666JIO52YX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225327Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAR5phXQ7c0wCtyv07NWRLxBTfTVx44HtRV8PhZR7wqVAiBlskCxv1qNS2IHTvg8b4ahHaLpqO6fZfnbCx8sTBJITSqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMghl7ybVBOmqf90g4KtwD7bfAwIGUFAmy8CmpRrXkbNedpq%2FjF1Dt451o5borwRbu6dGW7XyyI6QuyLAwY4K3crkFr2ZvbOAfv9SfRbs5LXDRPSUSDl7YsZQCKZvv8ethnaCkI0OdW1xUxNe9MT%2BpD%2FGW5HrPcBocgW9oJBUSym%2BdeZ%2BxpkgylyhbglfClZKCYwWmMCZIxAE5hJhGJmLIGnvyEGwBvAVMbumZjauzTTbmFOec5vPDl4pPNUORUIDkSub1NeBfFwMf7bWs79NMAxN%2B%2B7XpOo%2FWuylQSXWrt6puCTuHazZKrmTGj2mFNDZ2yY2ob9ytscUcWfYeqh9Azl4jMN6%2B4GSc5VqSxKLmzoUjCQSAGCdslRuVwCfBiLMAx5M%2BuKzWi%2FfOHF7Ru6A0M8KnADpFNto2WGHetD2dXjtrBqL%2FcZBiNpNtiI%2BQDXezM0MJXdhQ1Zw2VdcXbDX1KAUm%2BaXOG1DBacJQ2iyPDMyNcGP6gtK0BpFD9vc1ow2HpLeHLeEsdm1ERQ5jtZKcZ8nff38hLI9w60bwGyHVlsgh2bKsT7P26hBOEE9jzb5cNnElxro7kyoDwqYmXTRnK5MT4dyFphwxK%2FXGWK9ZRxRusbs7gI63U0tdfdrKw7UghkEkhCVYL34fz4Qw17r%2F0gY6pgFSZB62dJm6R3RlsI9%2FWWB3IsGEm%2BQ%2FyKX4L63hs3MINOJiV1Ne2KvsQI%2BVctSUQmy2pq6izbaeEYwIrbksUktetNRXyyTkHE4t0taKlFMZyYhhCEtr4az2qZRVqkfAbF9o97xkaSH0HVFCF3lcUahL6jCYJYgn%2FpL87VdHfABS5qVHpDBmgKWYMFv6r7ZTBNI9KjsF4R8O130idNxejttB1yod7IiW&X-Amz-Signature=c9ab603e43471b73f40ceb0752139bd5d50a926d6ad23ffad99c9a2f74e8b224&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


然后我们再创建另外一个就是下面 L 这然后我们来再说好，两个 topic 都创建成功了以后，我们接下来来看一下 list 列表有没有这两个 topic 对不对？同学们请看有一个 error 杠 lock 杠 collector 还有一个 App 杠 log 杠前来。这那就是说我们现在需要用到这两个 topic 对吧。我们的 file beat 启动了之后，是往这两个 topic 里边去对应的去做消费。 OK 那接下来同学们想一想，接下来的事情就很简单了，我们只需要做一件事情，做哪件事情呢？只需要做我们往这个 topic 里边去扔消息是什么？我们启动 fail beat 即可对吧。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/f14603f6-410e-457a-959e-571edfcccb5f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666JIO52YX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225327Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAR5phXQ7c0wCtyv07NWRLxBTfTVx44HtRV8PhZR7wqVAiBlskCxv1qNS2IHTvg8b4ahHaLpqO6fZfnbCx8sTBJITSqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMghl7ybVBOmqf90g4KtwD7bfAwIGUFAmy8CmpRrXkbNedpq%2FjF1Dt451o5borwRbu6dGW7XyyI6QuyLAwY4K3crkFr2ZvbOAfv9SfRbs5LXDRPSUSDl7YsZQCKZvv8ethnaCkI0OdW1xUxNe9MT%2BpD%2FGW5HrPcBocgW9oJBUSym%2BdeZ%2BxpkgylyhbglfClZKCYwWmMCZIxAE5hJhGJmLIGnvyEGwBvAVMbumZjauzTTbmFOec5vPDl4pPNUORUIDkSub1NeBfFwMf7bWs79NMAxN%2B%2B7XpOo%2FWuylQSXWrt6puCTuHazZKrmTGj2mFNDZ2yY2ob9ytscUcWfYeqh9Azl4jMN6%2B4GSc5VqSxKLmzoUjCQSAGCdslRuVwCfBiLMAx5M%2BuKzWi%2FfOHF7Ru6A0M8KnADpFNto2WGHetD2dXjtrBqL%2FcZBiNpNtiI%2BQDXezM0MJXdhQ1Zw2VdcXbDX1KAUm%2BaXOG1DBacJQ2iyPDMyNcGP6gtK0BpFD9vc1ow2HpLeHLeEsdm1ERQ5jtZKcZ8nff38hLI9w60bwGyHVlsgh2bKsT7P26hBOEE9jzb5cNnElxro7kyoDwqYmXTRnK5MT4dyFphwxK%2FXGWK9ZRxRusbs7gI63U0tdfdrKw7UghkEkhCVYL34fz4Qw17r%2F0gY6pgFSZB62dJm6R3RlsI9%2FWWB3IsGEm%2BQ%2FyKX4L63hs3MINOJiV1Ne2KvsQI%2BVctSUQmy2pq6izbaeEYwIrbksUktetNRXyyTkHE4t0taKlFMZyYhhCEtr4az2qZRVqkfAbF9o97xkaSH0HVFCF3lcUahL6jCYJYgn%2FpL87VdHfABS5qVHpDBmgKWYMFv6r7ZTBNI9KjsF4R8O130idNxejttB1yod7IiW&X-Amz-Signature=3d815e7fa98b06ee70a5b2e39a1dd66ed5739d8732e4b11d16b40fdddd5da068&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


好，那接下来我们把我们的这个 fail beat 启动起来就好了。我们现在看我们这个命令 fail beat 启动其实很简单，就是 USR local 然后这个 fail beat 就可以了。然后 PS 杠 EF 还到 great fail beat 来看看它有没有就行了。那目前我们这个应用程序 GPS 杠 L 我们去看到了有这个 connector 的 Java 已经起来了。我们来起一下 fail beat 这个我们应该到对应的目录下面去。我现在这个目录是 logs 我们 CD 到这个 fail beat 下面，然后去敲这个命令，他会说什么呢？他会说没有那个文件。我们现在是 fail beat 杠6.0，我们前面再加一个斜杠。好这回我们的 fail beat 已经起来了，我们 PS 杠 EF right 我们的 fail beat OK 你会看到如果有进场，就证明这个 failbeat 已经起来了。 

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/154ee2ff-86a1-4eb3-8dcc-931333605c43/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666JIO52YX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225327Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAR5phXQ7c0wCtyv07NWRLxBTfTVx44HtRV8PhZR7wqVAiBlskCxv1qNS2IHTvg8b4ahHaLpqO6fZfnbCx8sTBJITSqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMghl7ybVBOmqf90g4KtwD7bfAwIGUFAmy8CmpRrXkbNedpq%2FjF1Dt451o5borwRbu6dGW7XyyI6QuyLAwY4K3crkFr2ZvbOAfv9SfRbs5LXDRPSUSDl7YsZQCKZvv8ethnaCkI0OdW1xUxNe9MT%2BpD%2FGW5HrPcBocgW9oJBUSym%2BdeZ%2BxpkgylyhbglfClZKCYwWmMCZIxAE5hJhGJmLIGnvyEGwBvAVMbumZjauzTTbmFOec5vPDl4pPNUORUIDkSub1NeBfFwMf7bWs79NMAxN%2B%2B7XpOo%2FWuylQSXWrt6puCTuHazZKrmTGj2mFNDZ2yY2ob9ytscUcWfYeqh9Azl4jMN6%2B4GSc5VqSxKLmzoUjCQSAGCdslRuVwCfBiLMAx5M%2BuKzWi%2FfOHF7Ru6A0M8KnADpFNto2WGHetD2dXjtrBqL%2FcZBiNpNtiI%2BQDXezM0MJXdhQ1Zw2VdcXbDX1KAUm%2BaXOG1DBacJQ2iyPDMyNcGP6gtK0BpFD9vc1ow2HpLeHLeEsdm1ERQ5jtZKcZ8nff38hLI9w60bwGyHVlsgh2bKsT7P26hBOEE9jzb5cNnElxro7kyoDwqYmXTRnK5MT4dyFphwxK%2FXGWK9ZRxRusbs7gI63U0tdfdrKw7UghkEkhCVYL34fz4Qw17r%2F0gY6pgFSZB62dJm6R3RlsI9%2FWWB3IsGEm%2BQ%2FyKX4L63hs3MINOJiV1Ne2KvsQI%2BVctSUQmy2pq6izbaeEYwIrbksUktetNRXyyTkHE4t0taKlFMZyYhhCEtr4az2qZRVqkfAbF9o97xkaSH0HVFCF3lcUahL6jCYJYgn%2FpL87VdHfABS5qVHpDBmgKWYMFv6r7ZTBNI9KjsF4R8O130idNxejttB1yod7IiW&X-Amz-Signature=c2cf71464121d044a2d7317f41343368b9edc21dc41473092f375d75114460c2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

blb 的起来之后它其实现在就已经在抓我们数据。并且我们通过这个 top 命令其实大家可以看到对应的，我们其实这个 file beat 它运行起来，其实它是非常的不吃我们的这个 CPU 跟内存的，这也是 fail beat 它得以广泛的去应用在我们的这个 erk 场景中。


作为一个数据收集的组件的核心的原因就是 fail beat 它其实性能特别高，特别好，而且还不吃内存，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/de64a9ff-9e59-44ab-808f-f1a4d8cf4754/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666JIO52YX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225327Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAR5phXQ7c0wCtyv07NWRLxBTfTVx44HtRV8PhZR7wqVAiBlskCxv1qNS2IHTvg8b4ahHaLpqO6fZfnbCx8sTBJITSqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMghl7ybVBOmqf90g4KtwD7bfAwIGUFAmy8CmpRrXkbNedpq%2FjF1Dt451o5borwRbu6dGW7XyyI6QuyLAwY4K3crkFr2ZvbOAfv9SfRbs5LXDRPSUSDl7YsZQCKZvv8ethnaCkI0OdW1xUxNe9MT%2BpD%2FGW5HrPcBocgW9oJBUSym%2BdeZ%2BxpkgylyhbglfClZKCYwWmMCZIxAE5hJhGJmLIGnvyEGwBvAVMbumZjauzTTbmFOec5vPDl4pPNUORUIDkSub1NeBfFwMf7bWs79NMAxN%2B%2B7XpOo%2FWuylQSXWrt6puCTuHazZKrmTGj2mFNDZ2yY2ob9ytscUcWfYeqh9Azl4jMN6%2B4GSc5VqSxKLmzoUjCQSAGCdslRuVwCfBiLMAx5M%2BuKzWi%2FfOHF7Ru6A0M8KnADpFNto2WGHetD2dXjtrBqL%2FcZBiNpNtiI%2BQDXezM0MJXdhQ1Zw2VdcXbDX1KAUm%2BaXOG1DBacJQ2iyPDMyNcGP6gtK0BpFD9vc1ow2HpLeHLeEsdm1ERQ5jtZKcZ8nff38hLI9w60bwGyHVlsgh2bKsT7P26hBOEE9jzb5cNnElxro7kyoDwqYmXTRnK5MT4dyFphwxK%2FXGWK9ZRxRusbs7gI63U0tdfdrKw7UghkEkhCVYL34fz4Qw17r%2F0gY6pgFSZB62dJm6R3RlsI9%2FWWB3IsGEm%2BQ%2FyKX4L63hs3MINOJiV1Ne2KvsQI%2BVctSUQmy2pq6izbaeEYwIrbksUktetNRXyyTkHE4t0taKlFMZyYhhCEtr4az2qZRVqkfAbF9o97xkaSH0HVFCF3lcUahL6jCYJYgn%2FpL87VdHfABS5qVHpDBmgKWYMFv6r7ZTBNI9KjsF4R8O130idNxejttB1yod7IiW&X-Amz-Signature=167e562a2a46f74290c97bc37c4aecb2c988a9227f7dc53d8e4097e2fa0fb42e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

不占用 CPU 就是一般来讲我们会把我们的应用程序跟 filebeat 部署到一个节点上。那现在我就是这样的，我们自己的这个应用程序和 filebeat 他们是在一台服务器上的对吧，然后对应着它的 logs 就是应用程序的 logs 收集日志，打日志，然后 file B 的进行收集到我们的这个卡夫卡上。


那其实接下来我们可以，做一些访问。现在我们就打开我们自己的浏览器，然后去访问一下。在这里我们来看一看。之前我们是 local host 对吧，现在我们应该换地址了幺九二点幺六八点幺幺点三幺是吧，然后冒号我们对应的 800 幺，然后我们去访问 index 回车 index 已经访问了，然后我们再访问一下 error 就是 err 回车好，都是能访问通的。


接下来我们来观察一下，你看在控制台已经输出对应的这个日志以及异常了，那这就是证明没问题。接下来我们私立到 logs 下，我们去 cat 一下我们的 App log 同学们请看 App log 里边有全量的数据对吧，然后我们再去 cut 我们的 arrow log arrow log 里边它有什么呢？有 warning 级别以上的是不是一个 warning 一个 error 这是之前我们打的 error 日志，还有刚才我们访问 error 那个算数异常，OK这些都没问题。日志现在已经帮我们收集到了。


日志收集到了之后，接下来的事情就是来看一看我们对应的卡夫卡里边到底有没有数据。那这个怎么看呢？其实我们现在就是你现在没有消费者，只有生产者对吧？那其实你可以通过这个命令，但是这个命令你看不到对应的这个到底有没有数据情况，只有我们一会儿把消费者搞定了之后，你才能看到它的消费进度。


现在这个卡罗卡杠 [topic.sh](http://topic.sh/) 它的这个 topic App 杠 log 杠 collector collector 然后回车。好同学们一起看。刚才其实我创建了这个 connector 就是 App 杠 log 杠 collector 这个里边其实我们看到 partition 就一个，然后 leader 一个 replicate 是没有的，因为我们就一台服务器，所以没有副本对吧。 OK 那其实我们再可以看一个 topic 就是我们的 error 杠 log error 在这里边你只能看到它的分区情况，还有它的 leader 以及副本，包括它的这个 sr 情况。那其他的你看不到。那怎么办？就是你只有有消费者的这个 group 然后你用 subscript 的那个命令，你才能去看到它的消费进度。


那怎么办呢？其实很简单，大家都知道卡夫卡里边有对应的，他肯定是把数据落地存储了，对不对？那存储到哪了呢？他一般会把 topic 都存到卡卡到 log 下面。所以说我们只要观察卡夫卡杠 logs 下面的内容就好了。同学们请看卡夫卡杠 logs 下面里面基本上就是针对于每一个 topic 我应该这么说，每一个 topic 下的每一个 partition 它会建一个目录，然后去真正的去存储数据，这是它这个数据存储的这么一个结构。那其实我们看到这个 App 杠 log 杠 collector 0 以及 error 杠 log 杠 collector 0 对吧，看见了，这两个就是它具体的 partition 那其实我们 CD 到其中一个，我们去看它下面的结构，你会看到它里边有 index log 还有这个 time index 文件。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/6ce58aa7-7431-4995-b2dd-a44448d802e0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666JIO52YX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225327Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAR5phXQ7c0wCtyv07NWRLxBTfTVx44HtRV8PhZR7wqVAiBlskCxv1qNS2IHTvg8b4ahHaLpqO6fZfnbCx8sTBJITSqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMghl7ybVBOmqf90g4KtwD7bfAwIGUFAmy8CmpRrXkbNedpq%2FjF1Dt451o5borwRbu6dGW7XyyI6QuyLAwY4K3crkFr2ZvbOAfv9SfRbs5LXDRPSUSDl7YsZQCKZvv8ethnaCkI0OdW1xUxNe9MT%2BpD%2FGW5HrPcBocgW9oJBUSym%2BdeZ%2BxpkgylyhbglfClZKCYwWmMCZIxAE5hJhGJmLIGnvyEGwBvAVMbumZjauzTTbmFOec5vPDl4pPNUORUIDkSub1NeBfFwMf7bWs79NMAxN%2B%2B7XpOo%2FWuylQSXWrt6puCTuHazZKrmTGj2mFNDZ2yY2ob9ytscUcWfYeqh9Azl4jMN6%2B4GSc5VqSxKLmzoUjCQSAGCdslRuVwCfBiLMAx5M%2BuKzWi%2FfOHF7Ru6A0M8KnADpFNto2WGHetD2dXjtrBqL%2FcZBiNpNtiI%2BQDXezM0MJXdhQ1Zw2VdcXbDX1KAUm%2BaXOG1DBacJQ2iyPDMyNcGP6gtK0BpFD9vc1ow2HpLeHLeEsdm1ERQ5jtZKcZ8nff38hLI9w60bwGyHVlsgh2bKsT7P26hBOEE9jzb5cNnElxro7kyoDwqYmXTRnK5MT4dyFphwxK%2FXGWK9ZRxRusbs7gI63U0tdfdrKw7UghkEkhCVYL34fz4Qw17r%2F0gY6pgFSZB62dJm6R3RlsI9%2FWWB3IsGEm%2BQ%2FyKX4L63hs3MINOJiV1Ne2KvsQI%2BVctSUQmy2pq6izbaeEYwIrbksUktetNRXyyTkHE4t0taKlFMZyYhhCEtr4az2qZRVqkfAbF9o97xkaSH0HVFCF3lcUahL6jCYJYgn%2FpL87VdHfABS5qVHpDBmgKWYMFv6r7ZTBNI9KjsF4R8O130idNxejttB1yod7IiW&X-Amz-Signature=200bae283418127e380ca012641b467aa6f5db71bb37f3c8b1a43c2fe9cca2a7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

其实这个 log 就是真正的数据文件，它的数据文件是从 0 开始的，这个数据文件它是定长的，你会看到它里边是 20 个长度，它是定长的。然后它为什么是定长？其实有同学想问老师说老师这个卡不卡，是不是跟 rocky MQ 的数据存储的结构差不多？其实我告诉他们两个数据存储 90% 都是一模一样的，他们都是存定长的这个 commit log 文件来存储实际的数据的。为什么是定长呢？其实是方便他去做 MM map 就是内存映射，这个后面再去说。有机会的话，然后我们去看到它里面实际是有 size 的，就是5512，它实际有数据的，那大家就放心了，它里边真正有数据就 OK 了对吧。


好了，那其实我们现在的这个环节就已经搞定了，现在我们起码能知道通过 fail beat 我们能把数据收集到我们的卡夫卡上。那么整个对于这个 file beat 这一块，小伙伴们你可能现在还看不到结果。但是没关系，下节课我们要讲这个 log stash 然后小伙伴们就能看到对应的结果了。 OK 那么这节课我们就先讲到这，感谢小伙伴们收看。

```java
========================最新版本的 8.7 的 filebeat================配置和之前的不一样了


## filebeat配置文件 
###################### Filebeat Configuration Example #########################
filebeat.inputs:

  - type: filestream
    id: app-collector.log # Unique ID among all inputs, an ID is required.
    enabled: true  # Change to true to enable this input configuration.
    paths:
      ## app-服务名称.log, 为什么写死，防止发生轮转抓取历史数据
      - /usr/local/logs/app-collector.log
        # 定义写入 ES 时的 _type 值
    #document_type: "app-log"
    multiline:
      type: pattern  # pattern: '^\s*(\d{4}|\d{2})\-(\d{2}|[a-zA-Z]{3})\-(\d{2}|\d{4})'   # 指定匹配的表达式（匹配以 2017-11-15 08:04:23:889 时间格式开头的字符串）
      pattern: '^\['                              # 指定匹配的表达式（匹配以 "{ 开头的字符串）
      negate: true                                # 是否匹配到
      match: after                                # 合并到上一行的末尾
      max_lines: 2000                             # 最大的行数
      timeout: 2s                                 # 如果在规定时间没有新的日志事件就不等待后面的日志
    fields:
      logbiz: collector
      logtopic: app-log-collector1   #  按服务划分用作kafka topic
      evn: dev

  - type: filestream
    id: app-collector.log # Unique ID among all inputs, an ID is required.
    enabled: true  # Change to true to enable this input configuration.
    paths:
      - /usr/local/logs/error-collector.log
    #document_type: "error-log"
    multiline:
      type: pattern   # pattern: '^\s*(\d{4}|\d{2})\-(\d{2}|[a-zA-Z]{3})\-(\d{2}|\d{4})'   # 指定匹配的表达式（匹配以 2017-11-15 08:04:23:889 时间格式开头的字符串）
      pattern: '^\['                              # 指定匹配的表达式（匹配以 "{ 开头的字符串）
      negate: true                                # 是否匹配到
      match: after                                # 合并到上一行的末尾
      max_lines: 2000                             # 最大的行数
      timeout: 2s                                 # 如果在规定时间没有新的日志事件就不等待后面的日志
    fields:
      logbiz: collector
      logtopic: error-log-collector1   # 按服务划分用作kafka topic
      evn: dev

output.kafka:
  hosts: ["192.168.13.210:9092", "192.168.13.211:9092", "192.168.13.212:9092"]
  topic: '%{[fields.log_topic]}'
  partition.round_robin:
    reachable_only: true
  required_acks: 1
  compression: gzip
  max_message_bytes: 1000000
logging.to_files: true
```




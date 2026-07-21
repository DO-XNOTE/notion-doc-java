---
title: 2-14 MyCat的HA-原理
---

# 2-14 MyCat的HA-原理

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e1de9b8f-f176-4c02-956f-a3f2b5d0acbe/SCR-20240807-rgws.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WZW6JWSB%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225412Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCRN2UPuIxeGlioV6txrVOdoAyJ5RsR1V6DDgjzo62YwQIhAI3qy96vtQNLGN9B9rLRzgYP7n%2BUxTuDQgp7FNksXyUoKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzh%2BUd2JwB4cqbQ%2Fk8q3ANXPnu9dfz2urTecqQmdk9%2FVXba3w07dCrJRI1zFaaj9XRa7J8HAj6ZNR6zSQng%2BQ5CaN%2FuuK6H0W2DrvFrFFhU%2BsiSIpNaOc4xP6GhycRDQ1VYrRVNBeWS3PzwjkVrpJvKAPmNmbpQAk3ciVTfmk3eYbNQ5EUTzot6qp1PgTjyF5cl2%2Ftx%2F5ACHylHWw0zzkQeOD2vru7BYn0A%2FJLIR0%2FV7LAe5T0fb6gB%2FkGbll8EeHEwUxh67MhSeEXhfro6ZxaXOi%2BHvkgqvRNZn%2FOkT9GgBN6fWOi3A6rHVIXNMwhsiBw%2F1Pv4zppvVke4kmaAZo0UN%2FLVP7%2BTfThXwTyPbuqzm6XUVm50GiPWsU69ZSkZj0NEUR%2BICvPX%2B2KM9pCFNc8%2BqMXxHRK90Ji7Ga%2BBIIT1znJ%2Fo1PRANbyaPuURhBTe2tb0mpY7IusufHSVo7Hlfv%2F6YWtyk7ycXUyVaKbvCjQf2nMxEt%2FPr2dmiXww84yVkL%2BHxnRMI1RPduhAbBRpUnACt9kMKo%2B%2F3Yza6oy5GsR5H%2BkfDEoPADDGHk6uTFEhudFsK3cluydppHvrYdKj0g7NE2RbWZSov2qIwsJ57wYw8U1%2Fkxbe%2BMf39OPF40VAjPn5H2Yb0meYi9ZvTCWt%2F%2FSBjqkAahUcwKYVMdsKV2amroMqU16UQC5HReztesxJNgRxLaFWV7uPhas7SS9sSh56P2cvcVhQcM1mVAJB33bZQuFjAfM19EldBKdjdDcBgtDRmD06%2FsSdKg4IEcPho2WCOEH6IkrBmib1JycO9ULCvooqGANIvoTeHXoLlZMRk6miDxKytJ4ly9LOOoN4tsFYBMgPvW%2BWeJneX1JnPY3gAmTgj%2FQ0W4u&X-Amz-Signature=7d63dcb2c00625cbad7bd2e089e1861861c83eacde82a807a1dffc2db45c3488&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/9c672cc0-97ca-407a-8e1f-1bf3d9fff2f5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WZW6JWSB%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225412Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCRN2UPuIxeGlioV6txrVOdoAyJ5RsR1V6DDgjzo62YwQIhAI3qy96vtQNLGN9B9rLRzgYP7n%2BUxTuDQgp7FNksXyUoKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzh%2BUd2JwB4cqbQ%2Fk8q3ANXPnu9dfz2urTecqQmdk9%2FVXba3w07dCrJRI1zFaaj9XRa7J8HAj6ZNR6zSQng%2BQ5CaN%2FuuK6H0W2DrvFrFFhU%2BsiSIpNaOc4xP6GhycRDQ1VYrRVNBeWS3PzwjkVrpJvKAPmNmbpQAk3ciVTfmk3eYbNQ5EUTzot6qp1PgTjyF5cl2%2Ftx%2F5ACHylHWw0zzkQeOD2vru7BYn0A%2FJLIR0%2FV7LAe5T0fb6gB%2FkGbll8EeHEwUxh67MhSeEXhfro6ZxaXOi%2BHvkgqvRNZn%2FOkT9GgBN6fWOi3A6rHVIXNMwhsiBw%2F1Pv4zppvVke4kmaAZo0UN%2FLVP7%2BTfThXwTyPbuqzm6XUVm50GiPWsU69ZSkZj0NEUR%2BICvPX%2B2KM9pCFNc8%2BqMXxHRK90Ji7Ga%2BBIIT1znJ%2Fo1PRANbyaPuURhBTe2tb0mpY7IusufHSVo7Hlfv%2F6YWtyk7ycXUyVaKbvCjQf2nMxEt%2FPr2dmiXww84yVkL%2BHxnRMI1RPduhAbBRpUnACt9kMKo%2B%2F3Yza6oy5GsR5H%2BkfDEoPADDGHk6uTFEhudFsK3cluydppHvrYdKj0g7NE2RbWZSov2qIwsJ57wYw8U1%2Fkxbe%2BMf39OPF40VAjPn5H2Yb0meYi9ZvTCWt%2F%2FSBjqkAahUcwKYVMdsKV2amroMqU16UQC5HReztesxJNgRxLaFWV7uPhas7SS9sSh56P2cvcVhQcM1mVAJB33bZQuFjAfM19EldBKdjdDcBgtDRmD06%2FsSdKg4IEcPho2WCOEH6IkrBmib1JycO9ULCvooqGANIvoTeHXoLlZMRk6miDxKytJ4ly9LOOoN4tsFYBMgPvW%2BWeJneX1JnPY3gAmTgj%2FQ0W4u&X-Amz-Signature=adf1c8f013a0249d75e0bae2f384926d19f73474fc5885a318bf6bab6ed42ee6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/7666e8f3-b8d5-4ea5-a88b-5da14e8d183a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WZW6JWSB%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225412Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCRN2UPuIxeGlioV6txrVOdoAyJ5RsR1V6DDgjzo62YwQIhAI3qy96vtQNLGN9B9rLRzgYP7n%2BUxTuDQgp7FNksXyUoKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzh%2BUd2JwB4cqbQ%2Fk8q3ANXPnu9dfz2urTecqQmdk9%2FVXba3w07dCrJRI1zFaaj9XRa7J8HAj6ZNR6zSQng%2BQ5CaN%2FuuK6H0W2DrvFrFFhU%2BsiSIpNaOc4xP6GhycRDQ1VYrRVNBeWS3PzwjkVrpJvKAPmNmbpQAk3ciVTfmk3eYbNQ5EUTzot6qp1PgTjyF5cl2%2Ftx%2F5ACHylHWw0zzkQeOD2vru7BYn0A%2FJLIR0%2FV7LAe5T0fb6gB%2FkGbll8EeHEwUxh67MhSeEXhfro6ZxaXOi%2BHvkgqvRNZn%2FOkT9GgBN6fWOi3A6rHVIXNMwhsiBw%2F1Pv4zppvVke4kmaAZo0UN%2FLVP7%2BTfThXwTyPbuqzm6XUVm50GiPWsU69ZSkZj0NEUR%2BICvPX%2B2KM9pCFNc8%2BqMXxHRK90Ji7Ga%2BBIIT1znJ%2Fo1PRANbyaPuURhBTe2tb0mpY7IusufHSVo7Hlfv%2F6YWtyk7ycXUyVaKbvCjQf2nMxEt%2FPr2dmiXww84yVkL%2BHxnRMI1RPduhAbBRpUnACt9kMKo%2B%2F3Yza6oy5GsR5H%2BkfDEoPADDGHk6uTFEhudFsK3cluydppHvrYdKj0g7NE2RbWZSov2qIwsJ57wYw8U1%2Fkxbe%2BMf39OPF40VAjPn5H2Yb0meYi9ZvTCWt%2F%2FSBjqkAahUcwKYVMdsKV2amroMqU16UQC5HReztesxJNgRxLaFWV7uPhas7SS9sSh56P2cvcVhQcM1mVAJB33bZQuFjAfM19EldBKdjdDcBgtDRmD06%2FsSdKg4IEcPho2WCOEH6IkrBmib1JycO9ULCvooqGANIvoTeHXoLlZMRk6miDxKytJ4ly9LOOoN4tsFYBMgPvW%2BWeJneX1JnPY3gAmTgj%2FQ0W4u&X-Amz-Signature=e421e05f423e3c962ca1a777cfaa62abc2fe4ddcbcad4497bfe7e82c90e7d206&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/47eee13f-6598-4d44-8f20-31b7c18f2ee8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WZW6JWSB%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225412Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCRN2UPuIxeGlioV6txrVOdoAyJ5RsR1V6DDgjzo62YwQIhAI3qy96vtQNLGN9B9rLRzgYP7n%2BUxTuDQgp7FNksXyUoKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzh%2BUd2JwB4cqbQ%2Fk8q3ANXPnu9dfz2urTecqQmdk9%2FVXba3w07dCrJRI1zFaaj9XRa7J8HAj6ZNR6zSQng%2BQ5CaN%2FuuK6H0W2DrvFrFFhU%2BsiSIpNaOc4xP6GhycRDQ1VYrRVNBeWS3PzwjkVrpJvKAPmNmbpQAk3ciVTfmk3eYbNQ5EUTzot6qp1PgTjyF5cl2%2Ftx%2F5ACHylHWw0zzkQeOD2vru7BYn0A%2FJLIR0%2FV7LAe5T0fb6gB%2FkGbll8EeHEwUxh67MhSeEXhfro6ZxaXOi%2BHvkgqvRNZn%2FOkT9GgBN6fWOi3A6rHVIXNMwhsiBw%2F1Pv4zppvVke4kmaAZo0UN%2FLVP7%2BTfThXwTyPbuqzm6XUVm50GiPWsU69ZSkZj0NEUR%2BICvPX%2B2KM9pCFNc8%2BqMXxHRK90Ji7Ga%2BBIIT1znJ%2Fo1PRANbyaPuURhBTe2tb0mpY7IusufHSVo7Hlfv%2F6YWtyk7ycXUyVaKbvCjQf2nMxEt%2FPr2dmiXww84yVkL%2BHxnRMI1RPduhAbBRpUnACt9kMKo%2B%2F3Yza6oy5GsR5H%2BkfDEoPADDGHk6uTFEhudFsK3cluydppHvrYdKj0g7NE2RbWZSov2qIwsJ57wYw8U1%2Fkxbe%2BMf39OPF40VAjPn5H2Yb0meYi9ZvTCWt%2F%2FSBjqkAahUcwKYVMdsKV2amroMqU16UQC5HReztesxJNgRxLaFWV7uPhas7SS9sSh56P2cvcVhQcM1mVAJB33bZQuFjAfM19EldBKdjdDcBgtDRmD06%2FsSdKg4IEcPho2WCOEH6IkrBmib1JycO9ULCvooqGANIvoTeHXoLlZMRk6miDxKytJ4ly9LOOoN4tsFYBMgPvW%2BWeJneX1JnPY3gAmTgj%2FQ0W4u&X-Amz-Signature=44a26e4979dfe7441ff38487d69f2eeb6a15b9bdef106e52ce239e1c353a9326&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

文章当中咱们给大家介绍了 my cat 也体验到了 my cat 非常强大的这个分库分表的功能，它不仅可以分库分表，还可以做读写分离。咱们再快速的回忆一下， my cat 在做读写分离的时候有一个非常关键的字段，就是这个 balancebalance 是控制什么的balance ，它是控制你 select 查询的，控制你 select 查询到底是落在读库上还是落在写库上，还是说读库写库平均分配这个是 balance 这个字段。然后还有一个是 right typeright type 是干什么用的呢？当你配置了多个写库你有多个写库，那你写的时候是怎么写？这个是由 red type 去控制的，它默认是写到第一个写库当中。如果你第一个写库挂了，那么这个时候他才会写到后面的写库当中。这一块就是他读写分离的配置。然后就是这他的分片表我们要指定你的这个表它的分片的字段，然后指定它的分片规则。而且还可以指定你的表是否是全局表。如果你的表是一些字典表的话，我们可以配置它为全局表，然后还可以再设置它的子表。
这一系列都是咱们在项目当中经常遇到的这种情况，买 cat 它是都给大家完全的支持了。那么这一小节咱们就要给大家介绍一下了，你在项目当中可以通过买 cat 把你的数据库做成读写分离，这样你的数据库也避免了单点故障。那么我们如何避免买 Kite 成为系统当中的单点呢？咱们看一下目前的架构图。这个架构图是咱们做示例，给大家做成了这么一个样子。首先是这个一个 my cat 他是做代理用的，然后有两个分片库。其中第一个分片库咱们做了读写分离，这个分片库一写库是131，这台机器读库是130。然后第二个分迁库是 132 是这么一个结构。当然了咱们在应用到项目当中的时候，其实这个分片库 2 也要做一个读写分离，保证它每一个数据库都有两台，这样避免了单点的故障，即使我的一个数据库挂了，那么也不影响我整个系统的使用。这个就是一个数据库这方面的一个架构。
咱们再想想在现在互联网时代对吧，对系统要求都比较高，都要避免单点故障。咱们的数据库已经做高可用了，然后缓存 Redis 咱们也可以做，咱们通常都是搭一个 Redis 的集群，比如说搜索引擎，咱们也是做一个高可用，也避免了单点故障。前面的系统应用就不用说了，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/d3c3cd1d-42a6-4a3e-ba61-74f2e91d306b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WZW6JWSB%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225412Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCRN2UPuIxeGlioV6txrVOdoAyJ5RsR1V6DDgjzo62YwQIhAI3qy96vtQNLGN9B9rLRzgYP7n%2BUxTuDQgp7FNksXyUoKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzh%2BUd2JwB4cqbQ%2Fk8q3ANXPnu9dfz2urTecqQmdk9%2FVXba3w07dCrJRI1zFaaj9XRa7J8HAj6ZNR6zSQng%2BQ5CaN%2FuuK6H0W2DrvFrFFhU%2BsiSIpNaOc4xP6GhycRDQ1VYrRVNBeWS3PzwjkVrpJvKAPmNmbpQAk3ciVTfmk3eYbNQ5EUTzot6qp1PgTjyF5cl2%2Ftx%2F5ACHylHWw0zzkQeOD2vru7BYn0A%2FJLIR0%2FV7LAe5T0fb6gB%2FkGbll8EeHEwUxh67MhSeEXhfro6ZxaXOi%2BHvkgqvRNZn%2FOkT9GgBN6fWOi3A6rHVIXNMwhsiBw%2F1Pv4zppvVke4kmaAZo0UN%2FLVP7%2BTfThXwTyPbuqzm6XUVm50GiPWsU69ZSkZj0NEUR%2BICvPX%2B2KM9pCFNc8%2BqMXxHRK90Ji7Ga%2BBIIT1znJ%2Fo1PRANbyaPuURhBTe2tb0mpY7IusufHSVo7Hlfv%2F6YWtyk7ycXUyVaKbvCjQf2nMxEt%2FPr2dmiXww84yVkL%2BHxnRMI1RPduhAbBRpUnACt9kMKo%2B%2F3Yza6oy5GsR5H%2BkfDEoPADDGHk6uTFEhudFsK3cluydppHvrYdKj0g7NE2RbWZSov2qIwsJ57wYw8U1%2Fkxbe%2BMf39OPF40VAjPn5H2Yb0meYi9ZvTCWt%2F%2FSBjqkAahUcwKYVMdsKV2amroMqU16UQC5HReztesxJNgRxLaFWV7uPhas7SS9sSh56P2cvcVhQcM1mVAJB33bZQuFjAfM19EldBKdjdDcBgtDRmD06%2FsSdKg4IEcPho2WCOEH6IkrBmib1JycO9ULCvooqGANIvoTeHXoLlZMRk6miDxKytJ4ly9LOOoN4tsFYBMgPvW%2BWeJneX1JnPY3gAmTgj%2FQ0W4u&X-Amz-Signature=37c6ac25dd2d55da5d6764b1037925febf50a68704a5f664ee2a0097aee320c7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

也是多台的机器。那么现在唯一的一个单点就是这个买 cat 了，你整个系统当中就是一个单点。如果你买 cat 挂了，那么你的数据层是不是就访问不了了，访问不到数据库了？那么我们如何避免买 cat 成为系统当中的这么一个单点的故障，这个咱们就要做一下买 cat 的高可用。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/edf0139c-229c-4cd2-a22c-df2deffc677e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WZW6JWSB%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225412Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCRN2UPuIxeGlioV6txrVOdoAyJ5RsR1V6DDgjzo62YwQIhAI3qy96vtQNLGN9B9rLRzgYP7n%2BUxTuDQgp7FNksXyUoKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzh%2BUd2JwB4cqbQ%2Fk8q3ANXPnu9dfz2urTecqQmdk9%2FVXba3w07dCrJRI1zFaaj9XRa7J8HAj6ZNR6zSQng%2BQ5CaN%2FuuK6H0W2DrvFrFFhU%2BsiSIpNaOc4xP6GhycRDQ1VYrRVNBeWS3PzwjkVrpJvKAPmNmbpQAk3ciVTfmk3eYbNQ5EUTzot6qp1PgTjyF5cl2%2Ftx%2F5ACHylHWw0zzkQeOD2vru7BYn0A%2FJLIR0%2FV7LAe5T0fb6gB%2FkGbll8EeHEwUxh67MhSeEXhfro6ZxaXOi%2BHvkgqvRNZn%2FOkT9GgBN6fWOi3A6rHVIXNMwhsiBw%2F1Pv4zppvVke4kmaAZo0UN%2FLVP7%2BTfThXwTyPbuqzm6XUVm50GiPWsU69ZSkZj0NEUR%2BICvPX%2B2KM9pCFNc8%2BqMXxHRK90Ji7Ga%2BBIIT1znJ%2Fo1PRANbyaPuURhBTe2tb0mpY7IusufHSVo7Hlfv%2F6YWtyk7ycXUyVaKbvCjQf2nMxEt%2FPr2dmiXww84yVkL%2BHxnRMI1RPduhAbBRpUnACt9kMKo%2B%2F3Yza6oy5GsR5H%2BkfDEoPADDGHk6uTFEhudFsK3cluydppHvrYdKj0g7NE2RbWZSov2qIwsJ57wYw8U1%2Fkxbe%2BMf39OPF40VAjPn5H2Yb0meYi9ZvTCWt%2F%2FSBjqkAahUcwKYVMdsKV2amroMqU16UQC5HReztesxJNgRxLaFWV7uPhas7SS9sSh56P2cvcVhQcM1mVAJB33bZQuFjAfM19EldBKdjdDcBgtDRmD06%2FsSdKg4IEcPho2WCOEH6IkrBmib1JycO9ULCvooqGANIvoTeHXoLlZMRk6miDxKytJ4ly9LOOoN4tsFYBMgPvW%2BWeJneX1JnPY3gAmTgj%2FQ0W4u&X-Amz-Signature=a6c8bf08baf03b0eae38c866c737a71fb0db29f8de6c47d27e8c8c20a132dcbe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

这个就是买菜的做高个胸的整体的一个架构图。咱们先从右侧开始看。右侧大家看到这块明显配置了两个买 K 的摆开的，后边连的肯定都是咱们的了，数据库的集群，这个没有什么可以说的。然后前面他首先是配置了一个 HA proxy 它是做负载均衡用的。咱们经常见到的还有一个做负载均衡用的是什么？就是 ngx 是吧。


那么这块我为什么不用 ngx 我要用 HA proxy 呢？这个主要先给大家说明一下，就是说 HA proxy 和 NGINX 它最大的不同点是什么地方？它最大的不同点就是 NGINX 是支持 HTTP 协议的，因为前面 NGINX 咱们比较熟悉用它是做什么用是做你前端应用的一个代理。


你的这个 Tom cat 部署了多台服务，我前面部署一个 NGINX 用它去做负载均衡，这个是没有问题的，因为它是 HTTP 请求。但是到了咱们买 cat 这一层， my cat 它不是 HTTP 协议这块，咱们所以是不可以使用 NGINX 的。咱们要用 HA proxyha proxy 它是支持 T CP 层的代理。咱们敲的这个命令比如说 MySQL 杠 U 杠 P 它都是通过 TCP 协议去传输的。所以这块咱们要搭一个 HA proxy 它做这个负载均衡，往两个买开的当中去分发请求。那么这样你买 cat 部署了多个，避免了单点的故障。
那么这个时候你的一个 HA proxy 是不是又成了单点了？那么这个时候怎么办？这个时候咱们又要用到 people live 的，people live 的是干什么用呢？它是可以提供双击热备，它是一个什么原理呢？这里边先给大家简单的介绍一下。


大家看到上面的这一组 people love 了加 HA proxy 在咱们那个土地当中，它是在 83 这台机器，然后下边 HA proxy 和 people live 它在 64 这台机器上，然后这两台机器通过 people live 的创建出来一个虚拟 IP 103。这个时候前面我们的应用程序，比如说我们的 Tom cat 里边有一个 gdbc 连接，它连接什么，它就连接这个虚拟的 IP 然后他会找到一个确定的一台机器。比如说他连接的是 64 以后所有的请求数据库的这个请求都会通过这个虚拟的 IP 然后分配到 64 这台机器上，然后再通过 HA proxy 再去做分发。


这个分发就看你的负载惊慌的策略了，不管是轮询也好，还是随机也好，还是什么最小连接柱也好，它都会分发到这两个 my cat 上，然后再通过 my cat 连接后端的数据库是吧，这块它只是连接一个确定的物理的这个机器物理的 IP 倘若你的下边这个 64 这台机器挂了，那么这个时候它会通过这个虚拟的 IP 去连接到上面的这个 83 这台机器。这个就是 keeper DEV 的这个双击热备的这么一个功能。其实你后边挂了是吧，它自动切换 IP 对咱们的系统都是没有影响的，因为咱们系统都是只连接到了这个虚拟 IP 上。至于它后边怎么做咱们是不关心的。
咱们下面要给大家搭建这么一套架构。首先咱们要搭建这个 HA proxy ，咱们先把后边的两个 my cat 给它配置好，然后再配置一个 HA proxy 咱们先测试一下通过 HA proxy 它能不能做负载均衡连接到两个 my cat 上，下面咱们就做这一步的操作。

[file](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/ab5b216f-c32e-4daf-9b38-2dbbaded05c0/198-haproxy.cfg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WZW6JWSB%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225412Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCRN2UPuIxeGlioV6txrVOdoAyJ5RsR1V6DDgjzo62YwQIhAI3qy96vtQNLGN9B9rLRzgYP7n%2BUxTuDQgp7FNksXyUoKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzh%2BUd2JwB4cqbQ%2Fk8q3ANXPnu9dfz2urTecqQmdk9%2FVXba3w07dCrJRI1zFaaj9XRa7J8HAj6ZNR6zSQng%2BQ5CaN%2FuuK6H0W2DrvFrFFhU%2BsiSIpNaOc4xP6GhycRDQ1VYrRVNBeWS3PzwjkVrpJvKAPmNmbpQAk3ciVTfmk3eYbNQ5EUTzot6qp1PgTjyF5cl2%2Ftx%2F5ACHylHWw0zzkQeOD2vru7BYn0A%2FJLIR0%2FV7LAe5T0fb6gB%2FkGbll8EeHEwUxh67MhSeEXhfro6ZxaXOi%2BHvkgqvRNZn%2FOkT9GgBN6fWOi3A6rHVIXNMwhsiBw%2F1Pv4zppvVke4kmaAZo0UN%2FLVP7%2BTfThXwTyPbuqzm6XUVm50GiPWsU69ZSkZj0NEUR%2BICvPX%2B2KM9pCFNc8%2BqMXxHRK90Ji7Ga%2BBIIT1znJ%2Fo1PRANbyaPuURhBTe2tb0mpY7IusufHSVo7Hlfv%2F6YWtyk7ycXUyVaKbvCjQf2nMxEt%2FPr2dmiXww84yVkL%2BHxnRMI1RPduhAbBRpUnACt9kMKo%2B%2F3Yza6oy5GsR5H%2BkfDEoPADDGHk6uTFEhudFsK3cluydppHvrYdKj0g7NE2RbWZSov2qIwsJ57wYw8U1%2Fkxbe%2BMf39OPF40VAjPn5H2Yb0meYi9ZvTCWt%2F%2FSBjqkAahUcwKYVMdsKV2amroMqU16UQC5HReztesxJNgRxLaFWV7uPhas7SS9sSh56P2cvcVhQcM1mVAJB33bZQuFjAfM19EldBKdjdDcBgtDRmD06%2FsSdKg4IEcPho2WCOEH6IkrBmib1JycO9ULCvooqGANIvoTeHXoLlZMRk6miDxKytJ4ly9LOOoN4tsFYBMgPvW%2BWeJneX1JnPY3gAmTgj%2FQ0W4u&X-Amz-Signature=003ad75edae808e56aeab0f4c808a396ee4e0c3229a58261626d57b17b934883&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```java
198-haproxy.cfg


#---------------------------------------------------------------------
# Example configuration for a possible web application.  See the
# full configuration options online.
#
#   http://haproxy.1wt.eu/download/1.4/doc/configuration.txt
#
#---------------------------------------------------------------------

#---------------------------------------------------------------------
# Global settings
#---------------------------------------------------------------------
global
    # to have these messages end up in /var/log/haproxy.log you will
    # need to:
    #
    # 1) configure syslog to accept network log events.  This is done
    #    by adding the '-r' option to the SYSLOGD_OPTIONS in
    #    /etc/sysconfig/syslog
    #
    # 2) configure local2 events to go to the /var/log/haproxy.log
    #   file. A line like the following can be added to
    #   /etc/sysconfig/syslog
    #
    #    local2.*                       /var/log/haproxy.log
    #
    log         127.0.0.1 local2

    chroot      /var/lib/haproxy
    pidfile     /var/run/haproxy.pid
    maxconn     4000
    user        haproxy
    group       haproxy
    daemon

    # turn on stats unix socket
    stats socket /var/lib/haproxy/stats

#---------------------------------------------------------------------
# common defaults that all the 'listen' and 'backend' sections will
# use if not designated in their block
#---------------------------------------------------------------------
defaults
    mode                    tcp
    log                     global
    option                  tcplog
    option                  dontlognull
    #option http-server-close
    #option forwardfor       except 127.0.0.0/8
    option                  redispatch
    retries                 3
    timeout http-request    10s
    timeout queue           1m
    timeout connect         10s
    timeout client          1m
    timeout server          1m
    timeout http-keep-alive 10s
    timeout check           10s
    maxconn                 3000

#---------------------------------------------------------------------
# main frontend which proxys to the backends
#---------------------------------------------------------------------
frontend  main *:5000
    #acl url_static       path_beg       -i /static /images /javascript /stylesheets
    #acl url_static       path_end       -i .jpg .gif .png .css .js

    #use_backend static          if url_static
    default_backend             app

#---------------------------------------------------------------------
# static backend for serving up images, stylesheets and such
#---------------------------------------------------------------------
backend static
    balance     roundrobin
    server      static 127.0.0.1:4331 check

#---------------------------------------------------------------------
# round robin balancing between the various backends
#---------------------------------------------------------------------
backend app
    balance     roundrobin
    server  app1 192.168.31.137:8066 check
   # server  app2 127.0.0.1:5002 check
   # server  app3 127.0.0.1:5003 check
   # server  app4 127.0.0.1:5004 check
```


[file](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/ca577a9b-7606-4b88-9447-2070fc192393/199-haproxy.cfg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WZW6JWSB%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225412Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCRN2UPuIxeGlioV6txrVOdoAyJ5RsR1V6DDgjzo62YwQIhAI3qy96vtQNLGN9B9rLRzgYP7n%2BUxTuDQgp7FNksXyUoKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igzh%2BUd2JwB4cqbQ%2Fk8q3ANXPnu9dfz2urTecqQmdk9%2FVXba3w07dCrJRI1zFaaj9XRa7J8HAj6ZNR6zSQng%2BQ5CaN%2FuuK6H0W2DrvFrFFhU%2BsiSIpNaOc4xP6GhycRDQ1VYrRVNBeWS3PzwjkVrpJvKAPmNmbpQAk3ciVTfmk3eYbNQ5EUTzot6qp1PgTjyF5cl2%2Ftx%2F5ACHylHWw0zzkQeOD2vru7BYn0A%2FJLIR0%2FV7LAe5T0fb6gB%2FkGbll8EeHEwUxh67MhSeEXhfro6ZxaXOi%2BHvkgqvRNZn%2FOkT9GgBN6fWOi3A6rHVIXNMwhsiBw%2F1Pv4zppvVke4kmaAZo0UN%2FLVP7%2BTfThXwTyPbuqzm6XUVm50GiPWsU69ZSkZj0NEUR%2BICvPX%2B2KM9pCFNc8%2BqMXxHRK90Ji7Ga%2BBIIT1znJ%2Fo1PRANbyaPuURhBTe2tb0mpY7IusufHSVo7Hlfv%2F6YWtyk7ycXUyVaKbvCjQf2nMxEt%2FPr2dmiXww84yVkL%2BHxnRMI1RPduhAbBRpUnACt9kMKo%2B%2F3Yza6oy5GsR5H%2BkfDEoPADDGHk6uTFEhudFsK3cluydppHvrYdKj0g7NE2RbWZSov2qIwsJ57wYw8U1%2Fkxbe%2BMf39OPF40VAjPn5H2Yb0meYi9ZvTCWt%2F%2FSBjqkAahUcwKYVMdsKV2amroMqU16UQC5HReztesxJNgRxLaFWV7uPhas7SS9sSh56P2cvcVhQcM1mVAJB33bZQuFjAfM19EldBKdjdDcBgtDRmD06%2FsSdKg4IEcPho2WCOEH6IkrBmib1JycO9ULCvooqGANIvoTeHXoLlZMRk6miDxKytJ4ly9LOOoN4tsFYBMgPvW%2BWeJneX1JnPY3gAmTgj%2FQ0W4u&X-Amz-Signature=fde54819b6833d79b1f8469923c71b9441cd461e1bd5ba63bef8520003b75f9c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```java
#---------------------------------------------------------------------
# Example configuration for a possible web application.  See the
# full configuration options online.
#
#   http://haproxy.1wt.eu/download/1.4/doc/configuration.txt
#
#---------------------------------------------------------------------

#---------------------------------------------------------------------
# Global settings
#---------------------------------------------------------------------
global
    # to have these messages end up in /var/log/haproxy.log you will
    # need to:
    #
    # 1) configure syslog to accept network log events.  This is done
    #    by adding the '-r' option to the SYSLOGD_OPTIONS in
    #    /etc/sysconfig/syslog
    #
    # 2) configure local2 events to go to the /var/log/haproxy.log
    #   file. A line like the following can be added to
    #   /etc/sysconfig/syslog
    #
    #    local2.*                       /var/log/haproxy.log
    #
    log         127.0.0.1 local2

    chroot      /var/lib/haproxy
    pidfile     /var/run/haproxy.pid
    maxconn     4000
    user        haproxy
    group       haproxy
    daemon

    # turn on stats unix socket
    stats socket /var/lib/haproxy/stats

#---------------------------------------------------------------------
# common defaults that all the 'listen' and 'backend' sections will
# use if not designated in their block
#---------------------------------------------------------------------
defaults
    mode                    tcp
    log                     global
    option                  tcplog
    option                  dontlognull
   # option http-server-close
   # option forwardfor       except 127.0.0.0/8
    option                  redispatch
    retries                 3
    timeout http-request    10s
    timeout queue           1m
    timeout connect         10s
    timeout client          1m
    timeout server          1m
    timeout http-keep-alive 10s
    timeout check           10s
    maxconn                 3000

#---------------------------------------------------------------------
# main frontend which proxys to the backends
#---------------------------------------------------------------------
frontend  main *:5000
   # acl url_static       path_beg       -i /static /images /javascript /stylesheets
   # acl url_static       path_end       -i .jpg .gif .png .css .js

   # use_backend static          if url_static
    default_backend             app

#---------------------------------------------------------------------
# static backend for serving up images, stylesheets and such
#---------------------------------------------------------------------
backend static
    balance     roundrobin
    server      static 127.0.0.1:4331 check

#---------------------------------------------------------------------
# round robin balancing between the various backends
#---------------------------------------------------------------------
backend app
    balance     roundrobin
    server  app1 192.168.31.137:8066 check
   # server  app2 127.0.0.1:5002 check
   # server  app3 127.0.0.1:5003 check
   # server  app4 127.0.0.1:5004 check
```





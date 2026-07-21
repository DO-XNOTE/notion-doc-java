---
title: 1-4 收货地址 - 修改收货地址
---

# 1-4 收货地址 - 修改收货地址

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/2c802922-54ed-4d0d-bee6-a3fef1eb7e72/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663UCREBGR%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCzMVK3zA9953t18sRqlJLfil%2FtjbzzwpG%2F1%2FF46ixjFwIgaUIS1l%2F5wz7JyAfnmlhX6iU9PsLlRp5IV7UbrKVBE50qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFhr2%2FhwaMyk6tJzECrcAzxiq4%2Bq3frTNVYQZb5Wp86HjFSgT5uukriKPTrovZzwWkLouDkR6RfrRhgcNfOYueYRdVZ9mBAr2ixZnJz2QqznZj1a4OcL9C28XxwpsUQGYeCykd%2BamoWgSGI%2BNeEEipp4slY9ddsyvz0gXYugvpPAfAfxsbA59SOT44dIoJxKfiJMeWb%2FVbYJFPBnG6nRp2vea%2FKxZxux4s4quIzHuyIdZIqk8DqBYOidaaYuGQ2Ucm79ARd7B913LMbBxR0HvKY6FJ1L%2BaOAqNhtThRyjXLvf3paVNOfDhCdONokMdtNSohsPV%2FEh%2B7oYp%2Fq%2BhLrfBQj%2Flbvez%2B714JFTpseLMVs5EZUQG%2BGYuZHnooGIwJ9niWMVYGGO6icLpZzvs7i6AH5RF9v%2BAEJtdlDPE3QWSbRR91M33IHCuVim8pX1PCOFy5%2BnKJKoC%2B%2BrCgipjP1ap69c6VqKImJwritRPd0L6Np1Cw44KrvP5Rbov%2ByN8F17r1MHXdxFrDXMCtA4GsiKKlmHHpgwNttWeXsKb%2BP%2Fb7mPOWYSVIvpofGgvvPPpnwssNpjbdiuRHDl8qnP2K%2BbWDNjicHjaPYL7juheagkS5BD9%2B0VvuOFuTM89U%2Bi0ZDtwlibl561qC8WskSMKG4%2F9IGOqUB9Ga5OFAQ2vF%2B5gtlZObZfj0FyAJP6D61lHh9K8sY1xbkdEMKC%2FF%2FtELTcW0HC1PsR3h0w%2BYQDqOs%2FWXVodoWpz9J7Eye320e3HRllytHImrFoJK3o7%2Ft5HROOv5O1yQsC6SOrYW0zNK9Sp6mHL8MLdSVBSqvzACM9ADAAQQ18%2BSmUtdHOEc810yquyjnftDCZ2Ih0PtpK8PBc2qRMzwvt%2FcjVTYu&X-Amz-Signature=14bfd55aab85e137f834952eb7963b712904162a3b841145fa2f8efefde1384a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

上一节我们是讲了新增一个地址，接下来我们讲一下修改。修改和新增其实本质上是差不多的，只不过是多了一个 address ID。我们在前端源码里面，在这里也已经是过了。好，我们就直接来写一下。咱们的后端先写service。先来写一个接口里面的方法。 public foid update user address 修改用户的地址，传入的参数和新增也是一样，都是一个Bo，只不过这里面是多了一个 address ID。把复制过来，这是用户修改地址。好回到我们的 service 实现这个方法来实现一下。涉及到修改，很显然数据库它的一个事物隔离也是使用的request。好在这里面我们可以来写一下。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/3aed737c-8193-43b5-b2a0-2a6cd32b0c08/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663UCREBGR%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224659Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCzMVK3zA9953t18sRqlJLfil%2FtjbzzwpG%2F1%2FF46ixjFwIgaUIS1l%2F5wz7JyAfnmlhX6iU9PsLlRp5IV7UbrKVBE50qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDFhr2%2FhwaMyk6tJzECrcAzxiq4%2Bq3frTNVYQZb5Wp86HjFSgT5uukriKPTrovZzwWkLouDkR6RfrRhgcNfOYueYRdVZ9mBAr2ixZnJz2QqznZj1a4OcL9C28XxwpsUQGYeCykd%2BamoWgSGI%2BNeEEipp4slY9ddsyvz0gXYugvpPAfAfxsbA59SOT44dIoJxKfiJMeWb%2FVbYJFPBnG6nRp2vea%2FKxZxux4s4quIzHuyIdZIqk8DqBYOidaaYuGQ2Ucm79ARd7B913LMbBxR0HvKY6FJ1L%2BaOAqNhtThRyjXLvf3paVNOfDhCdONokMdtNSohsPV%2FEh%2B7oYp%2Fq%2BhLrfBQj%2Flbvez%2B714JFTpseLMVs5EZUQG%2BGYuZHnooGIwJ9niWMVYGGO6icLpZzvs7i6AH5RF9v%2BAEJtdlDPE3QWSbRR91M33IHCuVim8pX1PCOFy5%2BnKJKoC%2B%2BrCgipjP1ap69c6VqKImJwritRPd0L6Np1Cw44KrvP5Rbov%2ByN8F17r1MHXdxFrDXMCtA4GsiKKlmHHpgwNttWeXsKb%2BP%2Fb7mPOWYSVIvpofGgvvPPpnwssNpjbdiuRHDl8qnP2K%2BbWDNjicHjaPYL7juheagkS5BD9%2B0VvuOFuTM89U%2Bi0ZDtwlibl561qC8WskSMKG4%2F9IGOqUB9Ga5OFAQ2vF%2B5gtlZObZfj0FyAJP6D61lHh9K8sY1xbkdEMKC%2FF%2FtELTcW0HC1PsR3h0w%2BYQDqOs%2FWXVodoWpz9J7Eye320e3HRllytHImrFoJK3o7%2Ft5HROOv5O1yQsC6SOrYW0zNK9Sp6mHL8MLdSVBSqvzACM9ADAAQQ18%2BSmUtdHOEc810yquyjnftDCZ2Ih0PtpK8PBc2qRMzwvt%2FcjVTYu&X-Amz-Signature=a746a581af4416f2ab038c6fe5ccb9e5d7b6fd7a25b9808e15e8ab69c4c885b8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

首先第一个我们要获得 address ID，这个 ID 其实就是从 Bo 里面给获得的，获得了以后相应的一个对象，我们要去进行一个组装。这个对象其实和我们之前在这里其实是一样，把这一段内容贴过来，目的也是为了要把 Bo 里面的信息给放到新的一个 address 里面。在这个 address 我们不再叫做 new 了，我们可以取一个名字叫做 penny address。当然你要改为 update address 也可以这样子去改。这里面的一个属性，也就是组件ID，主机 ID 和 Bo 里面的 address ID 是不一样的，所以它是拷贝不进去的。在这里面就需要额外的做一个 set 一个address， set 一个ID，把 address ID 给放进去。这样子你想要去更新的对象，里面所包含的一些内容就已经是有了，但是千万不要忘记，它还有一个 update set up date time，这个时间我们也要去覆盖一下。


好，这样子其实我们要去更新的对象，里面的内容就已经是有了。随后我们就可以通过 map 去做一个更新点，它有一个方法叫做up。在此，在这里面我们可以使用以对象的形式去做KC，也可以以一个 example 的形式去做更新，都是没有问题的，我们在使用。

Updates by primary key selective.


也就是根据主键去进行更新。 selective 这个东西加不加？我们之前提供了一份文档，在这里面也有是说明了如果你不使用，使用这个空的一些属性会覆盖数据库里面的内容的。所以我们往往通常会使用selective。再把 pending address 给传进来，他就可以去做一个更新的操作了。

好，随后我们再回到 Ctrl 了，在 Ctrl 里面去把相应的接口去完善一下。把新增的接口拷贝贴到这里。在改一下。这是用户修改地址。 mess 的，也是使用post。另外传入进来参数也叫做Bo。路由来看一下。前端我们定义为update，所以只要把写过来就行了。 check 肯定也是有必要，因为我们是做修改，所以地址信息也是要去做判断的，只不过在 Bo 里面，我们要额外的要去判断一下它的ID，也就是 address ID。 address ID 肯定不能为空，如果为空，那么地址就修改不了了。


StringUtils.isBlank(addressBo.getAddressID).

get address ID 判断是否为空？如果为空，直接 return m 可决胜results。点 error message 返回修改地址错误，写一下是 address ID 不能为空。这一段代码我们就直接可以写在这里就行了。下面一个应该是通过 service 进行一个update，把 address Bo 传入进去。


修改成功了以后，前端只要接受一个 OK 就行了。好，我们可以来做一个测试了。在这里我们漏掉了一个分号，分号这里加一下。好，先来install， install 成功以后再重启服务器。好，OK，重启服务器成功了，我们来回到前端刷新一下。刷新一下以后，我们可以先修改第一个地址，我们把它改为杰森手机号码，把后面的 4 个 0 改为 4 个1，所在地改为江苏南京白下去。详细地址来一个 update 地址，点击保存好。保存成功以后可以看到在我们这里面重新渲染以后，信息就修改了。再来修改下一个。这个是默认，刚刚修改的是默认地址，如果不是默认地址也可以去修改的。点击编辑把 Lucy 改掉，改为 lady 手机号码后四位改为四告所在地改成上海，上海随便挑一个。宝山区详细地址详细地址随便写，点击保存好。OK，现在可以看到这两个地址信息，我们都可以去进行一个相应的修改了。好，这节我们就把修改地址功能给写好了。


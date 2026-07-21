---
title: 2-4 搜索 - 编写商品相关查询service
---

# 2-4 搜索 - 编写商品相关查询service

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e714666f-9bd3-430e-a877-7513e01272e0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665E34QCZT%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T224642Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDWd7csksPaNliO4M4V4XV53u0wUY74L6U3FvTxafBf7AiEA20pV%2B2DWnG%2Faa8U5UqlaGTscpSSjRoUN%2BVpLRgXdo1MqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC6UzgLmlQiTt1baVircA%2FDNszuSpRQZHo%2BJm%2F4myFUv0GmARsnQD9TxaLuJZs8CJZ4z2kKI0SllPxRoBwiwr05jyDwpLisfna4gDgjfzKxL05Ucrog6%2BlPdFO6WtuPPI6Hei%2FWzIOWLcGixWU8IRNITdn7JZz5tzlfdzpjRlmhVJakS8S%2Bj5b%2BYGlts65%2FPR%2B5sbV%2F3lIE%2F4H9BOIh%2Fy8R5sqdJ5KNM262jql6xOYhCGSp8%2BTdxk2NREName2v7ykiTo1r34dn3vj43TrQAosE5IwlUBKuub5CJrKN8ge8c7QY8Tdh%2FSIsBYRTuIYCH%2Fe%2B6ajcEFT9eJ6cdwH%2FolqMQVX%2ByFjA8x8mCYDbsSa8GgVSt%2BeaszgTU2Lpa%2FkwtTvOoJRxNPFB6C3eBkYPfOtcrrAlGNFLH1n9XFvU%2B6xWN4uQ3Dblp59zhK%2BPK4JQ6sqBtKjhgn9iaaVxMhdnelJ5vUxWJng2GV%2F3%2FG8hNIFyytJ2hzupv28g5zHoSs4PYfsdhaQu0TcIElIzQWU5fZjz76OrCDJUeX5llaN4dr56fZGaeW8vcGfXL%2FSt3yjwE4v65%2FPimriNnZDmwznA2NW8j8lMt18jt3HNJq93dsrJnv4vBIaqKy5QlZrnpz%2FwR0HaJS8Dx1Sr8G%2FmNMNi6%2F9IGOqUBKYNufpCBJhxylpRfUkDt%2B7BIitAPdlkGX9y1HMXlawznf1trbYo8rpOsst0xzJTeOBQC0k%2F%2BACqJNVsw%2FH0ijpP%2FJcDCFnS7uBThar1tQXNILjyaXWwShV9sGpuuyzjxXG5dS1uvcKEZiS5cwp6ZxV07zIPAE9cRohME4PxU%2FU1x%2BCF61M40IQePrp7tZWtggZAumaf7R9xQR9EJ524uUrnB%2BGYe&X-Amz-Signature=193656525fbe54e416825727b50c3a6f461246221e81cb162e67d0b262ff1195&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

上一节咱们讲了商品详情页的一些基本功能，以后，这一节我们就可以着手来编写相应的代码。代码还是一样，我们会最先从 service 层开始编写。对于我们的查询来讲，其实我们所要去查询的相关表全部都是和商品相关的，并且其实都是单表查询。所以在我们这里所需要用到的，使用通用 map 就可以做到相应的一个查询工作了。好，我们可以来一起把相应的代码先可以去写一下。我们先找到 service 层，我们来看一下，目前我们还没有和商品相关的，我们可以先拷贝一个，取名 item service 也OK。好，下一个我们还是一样也拷贝一份。


好，OK。在这里面我们相应的代码我们都要去改一下，实现的是 item service，在这里面我们所需要去使用的就不要用了。在这里面我们先把它的 4 个 service 所要去请求的一个方法，我们先可以都在这里先写好，我们删掉重新写。首先第一个我们是要查询商品，所以我们会有一个items。

query item by ID。


这是根据商品的组件去查询的商品组件，它是一个 string 类型的ID。因为我们的商品可能会有很多，在后期肯定是会涉及到分库分表，所以你的 ID 要必须保证为全局唯一的，就需要使用到 string 类型。好，加一下注释，这是根据商品 ID 查询详情。下一个， public 我们要去查询 list 了，这个 list 我们所涉及到的应该是一个 items image，这是商品的图片信息，来一个 query item image。 list 参数也是一个商品ID。在这里我们写一个，写这个，写 item ID，这样子它可以更加的让我们知道它所表示的含义是什么。根据商品 ID 查询商品图片列表。好，再拷贝一份。现在我们要去查询商品的规格。 s p e c 规格列表参数保持不变，在这里需要改一下。好，OK，在这里。注释还是要加上，因为注释毕竟是给人看的，所以为了规范，注释是一定要加的。根据商品 ID 查询商品规格。好，这是最后一个查询，这是查询商品的参数。商品参数它只需要单条记录就可以了，也就是 item parameter，也就是。好。OK，在这里再加一个注释。根据商品 ID 查询商品参数，其实就是商品的属性。这些抽象的方法都已经是写好了，接下来我们就需要把相应的方法我们要进行一个实现。好，先把这些方法快速生成一下。我们可以看到其实会有很多的一些包，我们在类里面没有使用的，我们可以 Ctrl out 加一个o，可以把一些没有用到的包全部都踢掉。好，在这里我们就可以一个一个去进行实现了。


首先第一个我们要去查询商品，很显然我们要把商品相关的一些 map 我们都需要给导入进来。第一个我们所使用到的应该是 items map，写下 private items Mapper，好，住进来。OK。其实很简单，它只需要根据主键去查询就可以了。通过 itemsmapper 点有一个 select by primary key，这就是它的组件，好放进来。这样子通过一句话就可以把它的一个商品信息，商品的一些基本信息就可以查询出来了。好，下一个是商品图片，所以我们把都写一下。总共是有 4 项。这个是item， the mix lepper，好，住进来。再下一个是规格，再来一个是它的参数，参数是？好，OK。相应的 map 我们都注进来，我们就可以去实现它的代码。在这里我们要去查询。我们可以使用 example 来做 items image， EXP 等于把它给 mute 出来。在这里只需要把 items image 点 class 放进去就行了。通过这个东西，通过 example 点 create 它的一个条件，条件在这里我们是需要创建的，这是 t k 的 t k example。然后，条件在这里我们就来一个点 and equal to，我们只需要把它的外键放进去。外键其实就是 item ID，找一下和属性名称进行一一的对应就行了。这样子这就是我们的一个条件就可以构建好了。


随后通过 item image mapper 点 select by example，把 example 给丢进去，这样子我们就可以去把整个和商品相关的 list 这些图片都可以查询出来了。好，千万不要忘记这里我们的事务，也要去加一下。


事物的隔离级别，使用 support 就可以了。好，把拷贝一下以后，我们应该要提供给当前这个类，里面所有的查询方法都要来一份，对吧？好，下面我们就可以去查询商品的规格，规格其实它也是包含了相应的信息，它也是一个list。在这里其实我们可以把它代码直接拷贝一份，也可以把上面拷贝粉，这样子我们可以写得更加的快一些。


在这里我们可以把改成s、 p e、c，然后，快速的修改，这样子会更快。在它里面相应的属性也叫做 item ID，贴过来查询的时候，只要把 items SPC example 给丢过来，在这里改成 item s p e c map select by example。这样子就可以去做一个查询。好，做的比较快。下一个是查询他的商品参数，也是一样。把。我们直接可以拷贝一下，在这里改成 a pump， EXP 这些全部都修改。当然我们你们的 class 改成items， palm 这些我们都不需要去动它里面的外键，我们也进去看一下。外镜也是 item ID，需要去进行对应的。好，OK。随后我们可以通过 item palm， apple 点 select 去查询。现在我们可以直接通过 select one，也就是只查询一条记录就可以了。拿出来的一个对象，而不是一个list，把 example 丢进来。好，OK。现在我们这几个 service 方法就已经是全部都写好了。


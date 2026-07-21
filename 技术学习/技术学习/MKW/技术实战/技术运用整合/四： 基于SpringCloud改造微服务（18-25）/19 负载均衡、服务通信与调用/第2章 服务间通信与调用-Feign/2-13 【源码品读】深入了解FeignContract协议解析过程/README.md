---
title: 2-13 【源码品读】深入了解FeignContract协议解析过程
---

# 2-13 【源码品读】深入了解FeignContract协议解析过程

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/70ebde57-2808-44db-bc85-dacd5814a0ef/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665E34QCZT%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225627Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDWd7csksPaNliO4M4V4XV53u0wUY74L6U3FvTxafBf7AiEA20pV%2B2DWnG%2Faa8U5UqlaGTscpSSjRoUN%2BVpLRgXdo1MqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC6UzgLmlQiTt1baVircA%2FDNszuSpRQZHo%2BJm%2F4myFUv0GmARsnQD9TxaLuJZs8CJZ4z2kKI0SllPxRoBwiwr05jyDwpLisfna4gDgjfzKxL05Ucrog6%2BlPdFO6WtuPPI6Hei%2FWzIOWLcGixWU8IRNITdn7JZz5tzlfdzpjRlmhVJakS8S%2Bj5b%2BYGlts65%2FPR%2B5sbV%2F3lIE%2F4H9BOIh%2Fy8R5sqdJ5KNM262jql6xOYhCGSp8%2BTdxk2NREName2v7ykiTo1r34dn3vj43TrQAosE5IwlUBKuub5CJrKN8ge8c7QY8Tdh%2FSIsBYRTuIYCH%2Fe%2B6ajcEFT9eJ6cdwH%2FolqMQVX%2ByFjA8x8mCYDbsSa8GgVSt%2BeaszgTU2Lpa%2FkwtTvOoJRxNPFB6C3eBkYPfOtcrrAlGNFLH1n9XFvU%2B6xWN4uQ3Dblp59zhK%2BPK4JQ6sqBtKjhgn9iaaVxMhdnelJ5vUxWJng2GV%2F3%2FG8hNIFyytJ2hzupv28g5zHoSs4PYfsdhaQu0TcIElIzQWU5fZjz76OrCDJUeX5llaN4dr56fZGaeW8vcGfXL%2FSt3yjwE4v65%2FPimriNnZDmwznA2NW8j8lMt18jt3HNJq93dsrJnv4vBIaqKy5QlZrnpz%2FwR0HaJS8Dx1Sr8G%2FmNMNi6%2F9IGOqUBKYNufpCBJhxylpRfUkDt%2B7BIitAPdlkGX9y1HMXlawznf1trbYo8rpOsst0xzJTeOBQC0k%2F%2BACqJNVsw%2FH0ijpP%2FJcDCFnS7uBThar1tQXNILjyaXWwShV9sGpuuyzjxXG5dS1uvcKEZiS5cwp6ZxV07zIPAE9cRohME4PxU%2FU1x%2BCF61M40IQePrp7tZWtggZAumaf7R9xQR9EJ524uUrnB%2BGYe&X-Amz-Signature=23cd591dd9785541adf38f935dea950a84ff9ccebe98cbecace77875466ba234&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/3c26f290-6fd2-4ff8-88ca-f8c5f146301d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665E34QCZT%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225627Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDWd7csksPaNliO4M4V4XV53u0wUY74L6U3FvTxafBf7AiEA20pV%2B2DWnG%2Faa8U5UqlaGTscpSSjRoUN%2BVpLRgXdo1MqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC6UzgLmlQiTt1baVircA%2FDNszuSpRQZHo%2BJm%2F4myFUv0GmARsnQD9TxaLuJZs8CJZ4z2kKI0SllPxRoBwiwr05jyDwpLisfna4gDgjfzKxL05Ucrog6%2BlPdFO6WtuPPI6Hei%2FWzIOWLcGixWU8IRNITdn7JZz5tzlfdzpjRlmhVJakS8S%2Bj5b%2BYGlts65%2FPR%2B5sbV%2F3lIE%2F4H9BOIh%2Fy8R5sqdJ5KNM262jql6xOYhCGSp8%2BTdxk2NREName2v7ykiTo1r34dn3vj43TrQAosE5IwlUBKuub5CJrKN8ge8c7QY8Tdh%2FSIsBYRTuIYCH%2Fe%2B6ajcEFT9eJ6cdwH%2FolqMQVX%2ByFjA8x8mCYDbsSa8GgVSt%2BeaszgTU2Lpa%2FkwtTvOoJRxNPFB6C3eBkYPfOtcrrAlGNFLH1n9XFvU%2B6xWN4uQ3Dblp59zhK%2BPK4JQ6sqBtKjhgn9iaaVxMhdnelJ5vUxWJng2GV%2F3%2FG8hNIFyytJ2hzupv28g5zHoSs4PYfsdhaQu0TcIElIzQWU5fZjz76OrCDJUeX5llaN4dr56fZGaeW8vcGfXL%2FSt3yjwE4v65%2FPimriNnZDmwznA2NW8j8lMt18jt3HNJq93dsrJnv4vBIaqKy5QlZrnpz%2FwR0HaJS8Dx1Sr8G%2FmNMNi6%2F9IGOqUBKYNufpCBJhxylpRfUkDt%2B7BIitAPdlkGX9y1HMXlawznf1trbYo8rpOsst0xzJTeOBQC0k%2F%2BACqJNVsw%2FH0ijpP%2FJcDCFnS7uBThar1tQXNILjyaXWwShV9sGpuuyzjxXG5dS1uvcKEZiS5cwp6ZxV07zIPAE9cRohME4PxU%2FU1x%2BCF61M40IQePrp7tZWtggZAumaf7R9xQR9EJ524uUrnB%2BGYe&X-Amz-Signature=f97cb8f25d89d5ad8bae93e5374e70c1f2692cb0983922dbaba80877e554087b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e7bc5279-5ae3-4e6b-8fe2-13ef59a0100e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665E34QCZT%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225627Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDWd7csksPaNliO4M4V4XV53u0wUY74L6U3FvTxafBf7AiEA20pV%2B2DWnG%2Faa8U5UqlaGTscpSSjRoUN%2BVpLRgXdo1MqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC6UzgLmlQiTt1baVircA%2FDNszuSpRQZHo%2BJm%2F4myFUv0GmARsnQD9TxaLuJZs8CJZ4z2kKI0SllPxRoBwiwr05jyDwpLisfna4gDgjfzKxL05Ucrog6%2BlPdFO6WtuPPI6Hei%2FWzIOWLcGixWU8IRNITdn7JZz5tzlfdzpjRlmhVJakS8S%2Bj5b%2BYGlts65%2FPR%2B5sbV%2F3lIE%2F4H9BOIh%2Fy8R5sqdJ5KNM262jql6xOYhCGSp8%2BTdxk2NREName2v7ykiTo1r34dn3vj43TrQAosE5IwlUBKuub5CJrKN8ge8c7QY8Tdh%2FSIsBYRTuIYCH%2Fe%2B6ajcEFT9eJ6cdwH%2FolqMQVX%2ByFjA8x8mCYDbsSa8GgVSt%2BeaszgTU2Lpa%2FkwtTvOoJRxNPFB6C3eBkYPfOtcrrAlGNFLH1n9XFvU%2B6xWN4uQ3Dblp59zhK%2BPK4JQ6sqBtKjhgn9iaaVxMhdnelJ5vUxWJng2GV%2F3%2FG8hNIFyytJ2hzupv28g5zHoSs4PYfsdhaQu0TcIElIzQWU5fZjz76OrCDJUeX5llaN4dr56fZGaeW8vcGfXL%2FSt3yjwE4v65%2FPimriNnZDmwznA2NW8j8lMt18jt3HNJq93dsrJnv4vBIaqKy5QlZrnpz%2FwR0HaJS8Dx1Sr8G%2FmNMNi6%2F9IGOqUBKYNufpCBJhxylpRfUkDt%2B7BIitAPdlkGX9y1HMXlawznf1trbYo8rpOsst0xzJTeOBQC0k%2F%2BACqJNVsw%2FH0ijpP%2FJcDCFnS7uBThar1tQXNILjyaXWwShV9sGpuuyzjxXG5dS1uvcKEZiS5cwp6ZxV07zIPAE9cRohME4PxU%2FU1x%2BCF61M40IQePrp7tZWtggZAumaf7R9xQR9EJ524uUrnB%2BGYe&X-Amz-Signature=05890b092dc4a363658d292735c257dcc243fee1e48b7df337789d5f9adf4d88&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e62189ed-1b96-4108-8003-0f5ceb43cf38/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665E34QCZT%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225627Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDWd7csksPaNliO4M4V4XV53u0wUY74L6U3FvTxafBf7AiEA20pV%2B2DWnG%2Faa8U5UqlaGTscpSSjRoUN%2BVpLRgXdo1MqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC6UzgLmlQiTt1baVircA%2FDNszuSpRQZHo%2BJm%2F4myFUv0GmARsnQD9TxaLuJZs8CJZ4z2kKI0SllPxRoBwiwr05jyDwpLisfna4gDgjfzKxL05Ucrog6%2BlPdFO6WtuPPI6Hei%2FWzIOWLcGixWU8IRNITdn7JZz5tzlfdzpjRlmhVJakS8S%2Bj5b%2BYGlts65%2FPR%2B5sbV%2F3lIE%2F4H9BOIh%2Fy8R5sqdJ5KNM262jql6xOYhCGSp8%2BTdxk2NREName2v7ykiTo1r34dn3vj43TrQAosE5IwlUBKuub5CJrKN8ge8c7QY8Tdh%2FSIsBYRTuIYCH%2Fe%2B6ajcEFT9eJ6cdwH%2FolqMQVX%2ByFjA8x8mCYDbsSa8GgVSt%2BeaszgTU2Lpa%2FkwtTvOoJRxNPFB6C3eBkYPfOtcrrAlGNFLH1n9XFvU%2B6xWN4uQ3Dblp59zhK%2BPK4JQ6sqBtKjhgn9iaaVxMhdnelJ5vUxWJng2GV%2F3%2FG8hNIFyytJ2hzupv28g5zHoSs4PYfsdhaQu0TcIElIzQWU5fZjz76OrCDJUeX5llaN4dr56fZGaeW8vcGfXL%2FSt3yjwE4v65%2FPimriNnZDmwznA2NW8j8lMt18jt3HNJq93dsrJnv4vBIaqKy5QlZrnpz%2FwR0HaJS8Dx1Sr8G%2FmNMNi6%2F9IGOqUBKYNufpCBJhxylpRfUkDt%2B7BIitAPdlkGX9y1HMXlawznf1trbYo8rpOsst0xzJTeOBQC0k%2F%2BACqJNVsw%2FH0ijpP%2FJcDCFnS7uBThar1tQXNILjyaXWwShV9sGpuuyzjxXG5dS1uvcKEZiS5cwp6ZxV07zIPAE9cRohME4PxU%2FU1x%2BCF61M40IQePrp7tZWtggZAumaf7R9xQR9EJ524uUrnB%2BGYe&X-Amz-Signature=1fd74a04007a748eb65ffa82c248303da21a243ee0af362c36a0c28e4fa37013&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/17ef348c-7b7a-46e9-840c-b2160c2f8189/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665E34QCZT%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225627Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDWd7csksPaNliO4M4V4XV53u0wUY74L6U3FvTxafBf7AiEA20pV%2B2DWnG%2Faa8U5UqlaGTscpSSjRoUN%2BVpLRgXdo1MqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC6UzgLmlQiTt1baVircA%2FDNszuSpRQZHo%2BJm%2F4myFUv0GmARsnQD9TxaLuJZs8CJZ4z2kKI0SllPxRoBwiwr05jyDwpLisfna4gDgjfzKxL05Ucrog6%2BlPdFO6WtuPPI6Hei%2FWzIOWLcGixWU8IRNITdn7JZz5tzlfdzpjRlmhVJakS8S%2Bj5b%2BYGlts65%2FPR%2B5sbV%2F3lIE%2F4H9BOIh%2Fy8R5sqdJ5KNM262jql6xOYhCGSp8%2BTdxk2NREName2v7ykiTo1r34dn3vj43TrQAosE5IwlUBKuub5CJrKN8ge8c7QY8Tdh%2FSIsBYRTuIYCH%2Fe%2B6ajcEFT9eJ6cdwH%2FolqMQVX%2ByFjA8x8mCYDbsSa8GgVSt%2BeaszgTU2Lpa%2FkwtTvOoJRxNPFB6C3eBkYPfOtcrrAlGNFLH1n9XFvU%2B6xWN4uQ3Dblp59zhK%2BPK4JQ6sqBtKjhgn9iaaVxMhdnelJ5vUxWJng2GV%2F3%2FG8hNIFyytJ2hzupv28g5zHoSs4PYfsdhaQu0TcIElIzQWU5fZjz76OrCDJUeX5llaN4dr56fZGaeW8vcGfXL%2FSt3yjwE4v65%2FPimriNnZDmwznA2NW8j8lMt18jt3HNJq93dsrJnv4vBIaqKy5QlZrnpz%2FwR0HaJS8Dx1Sr8G%2FmNMNi6%2F9IGOqUBKYNufpCBJhxylpRfUkDt%2B7BIitAPdlkGX9y1HMXlawznf1trbYo8rpOsst0xzJTeOBQC0k%2F%2BACqJNVsw%2FH0ijpP%2FJcDCFnS7uBThar1tQXNILjyaXWwShV9sGpuuyzjxXG5dS1uvcKEZiS5cwp6ZxV07zIPAE9cRohME4PxU%2FU1x%2BCF61M40IQePrp7tZWtggZAumaf7R9xQR9EJ524uUrnB%2BGYe&X-Amz-Signature=71af785739d517c490be5579545a0c19005b6ca9a8572169a8be084da18289fc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

hello 慕课网的各位同学们，大家好，这一节我们学习整个份章节当中理论性最强、最绕人最复杂的源码部分，那就是分 contract 协议的解析过程。它在什么时候解析呢？整个项目加载的时候，我们来看一下本章的三个内容。第一个是我们先来认识一下这一家三口 

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/c319eef1-c528-4b14-98ab-54ca6b53a728/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665E34QCZT%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225627Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDWd7csksPaNliO4M4V4XV53u0wUY74L6U3FvTxafBf7AiEA20pV%2B2DWnG%2Faa8U5UqlaGTscpSSjRoUN%2BVpLRgXdo1MqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC6UzgLmlQiTt1baVircA%2FDNszuSpRQZHo%2BJm%2F4myFUv0GmARsnQD9TxaLuJZs8CJZ4z2kKI0SllPxRoBwiwr05jyDwpLisfna4gDgjfzKxL05Ucrog6%2BlPdFO6WtuPPI6Hei%2FWzIOWLcGixWU8IRNITdn7JZz5tzlfdzpjRlmhVJakS8S%2Bj5b%2BYGlts65%2FPR%2B5sbV%2F3lIE%2F4H9BOIh%2Fy8R5sqdJ5KNM262jql6xOYhCGSp8%2BTdxk2NREName2v7ykiTo1r34dn3vj43TrQAosE5IwlUBKuub5CJrKN8ge8c7QY8Tdh%2FSIsBYRTuIYCH%2Fe%2B6ajcEFT9eJ6cdwH%2FolqMQVX%2ByFjA8x8mCYDbsSa8GgVSt%2BeaszgTU2Lpa%2FkwtTvOoJRxNPFB6C3eBkYPfOtcrrAlGNFLH1n9XFvU%2B6xWN4uQ3Dblp59zhK%2BPK4JQ6sqBtKjhgn9iaaVxMhdnelJ5vUxWJng2GV%2F3%2FG8hNIFyytJ2hzupv28g5zHoSs4PYfsdhaQu0TcIElIzQWU5fZjz76OrCDJUeX5llaN4dr56fZGaeW8vcGfXL%2FSt3yjwE4v65%2FPimriNnZDmwznA2NW8j8lMt18jt3HNJq93dsrJnv4vBIaqKy5QlZrnpz%2FwR0HaJS8Dx1Sr8G%2FmNMNi6%2F9IGOqUBKYNufpCBJhxylpRfUkDt%2B7BIitAPdlkGX9y1HMXlawznf1trbYo8rpOsst0xzJTeOBQC0k%2F%2BACqJNVsw%2FH0ijpP%2FJcDCFnS7uBThar1tQXNILjyaXWwShV9sGpuuyzjxXG5dS1uvcKEZiS5cwp6ZxV07zIPAE9cRohME4PxU%2FU1x%2BCF61M40IQePrp7tZWtggZAumaf7R9xQR9EJ524uUrnB%2BGYe&X-Amz-Signature=72ea831f40f87ab0c61ef5350d833d9451d6c669b9cb73a9480e1fb49f199858&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

contract 老祖宗 base contract 儿子以及孙子类 spring MVC contract 它也是 open fan 这一个 dependency 下的内容。好。第二部分我们看一下子类 base contract 它里面都有哪些校验规则。最后一个看看这个孙子 spring MVC contract 它是如何来抽取 metadata 也就是元数据的？好，大家不用抄家伙，轻装上阵，源码品读走起，每天 coding 1 小时，健康工作 50 年。



那说到 contract 大家应该脑子中一下就能反应过来，我们需要先看哪个类，它的名字就叫 contract 好它是 open fin 包下的一个内容。大家看这里有很多很多 contract 不要找错地方，要找这个 open fin 下面的 contractok 进来看。这里面我们刚才说有什么子类孙类，那这个老祖宗 contract 什么都没有，光杆司令这个 base contract 定义了蛮多的逻辑，那主要的数据验证逻辑全在这里面。那接下来看谁继承这个 base contact 有两个家伙继承了它，一个叫 default 那它是 open phone 的 contract 我们项目中用的是谁是这个叫 spring MVC contract 的东西。它这里面包含的主要都是数据抽取的一部分逻辑。我们就由从上到下的顺序先来从最外层打一个断点，走进来看一看好了在哪个方法里打断点你看茫茫多的方法。


大家看这个光杆司令 contract 它有一个方法叫什么叫 purse and validate metadata 是一个数据验证的方法，对不对？那想必所有方法的入口必然就是它了。那好办，我们只要到这个 base contract 中，在相应的方法上面打上一个断点，用 debug 模式把它启动起来，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/a3a2a7bf-aca6-4663-89c9-890daf3aaa07/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665E34QCZT%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225627Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDWd7csksPaNliO4M4V4XV53u0wUY74L6U3FvTxafBf7AiEA20pV%2B2DWnG%2Faa8U5UqlaGTscpSSjRoUN%2BVpLRgXdo1MqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDC6UzgLmlQiTt1baVircA%2FDNszuSpRQZHo%2BJm%2F4myFUv0GmARsnQD9TxaLuJZs8CJZ4z2kKI0SllPxRoBwiwr05jyDwpLisfna4gDgjfzKxL05Ucrog6%2BlPdFO6WtuPPI6Hei%2FWzIOWLcGixWU8IRNITdn7JZz5tzlfdzpjRlmhVJakS8S%2Bj5b%2BYGlts65%2FPR%2B5sbV%2F3lIE%2F4H9BOIh%2Fy8R5sqdJ5KNM262jql6xOYhCGSp8%2BTdxk2NREName2v7ykiTo1r34dn3vj43TrQAosE5IwlUBKuub5CJrKN8ge8c7QY8Tdh%2FSIsBYRTuIYCH%2Fe%2B6ajcEFT9eJ6cdwH%2FolqMQVX%2ByFjA8x8mCYDbsSa8GgVSt%2BeaszgTU2Lpa%2FkwtTvOoJRxNPFB6C3eBkYPfOtcrrAlGNFLH1n9XFvU%2B6xWN4uQ3Dblp59zhK%2BPK4JQ6sqBtKjhgn9iaaVxMhdnelJ5vUxWJng2GV%2F3%2FG8hNIFyytJ2hzupv28g5zHoSs4PYfsdhaQu0TcIElIzQWU5fZjz76OrCDJUeX5llaN4dr56fZGaeW8vcGfXL%2FSt3yjwE4v65%2FPimriNnZDmwznA2NW8j8lMt18jt3HNJq93dsrJnv4vBIaqKy5QlZrnpz%2FwR0HaJS8Dx1Sr8G%2FmNMNi6%2F9IGOqUBKYNufpCBJhxylpRfUkDt%2B7BIitAPdlkGX9y1HMXlawznf1trbYo8rpOsst0xzJTeOBQC0k%2F%2BACqJNVsw%2FH0ijpP%2FJcDCFnS7uBThar1tQXNILjyaXWwShV9sGpuuyzjxXG5dS1uvcKEZiS5cwp6ZxV07zIPAE9cRohME4PxU%2FU1x%2BCF61M40IQePrp7tZWtggZAumaf7R9xQR9EJ524uUrnB%2BGYe&X-Amz-Signature=3756fa1b98a1080d1421810fcafb97a274b93d198c41fa28dc7b35d6a7e9b8f8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那自然就知道谁先进来了。二话不说，走起。好，这里第一个断点走到了哪里 base contract 里面拿到一个方法，谁先看入参 target type 这个 target type 是谁谁这么讨厌大清早敲门谁 I service 它不是 controller 而是我们定义的分 client 的 I service 好，接下来拿到 I service 应该干什么呢？当然是做数据验证了。


我们前面提到 base contract 主要的功能就是数据验证，它这里写了很多 check state 方法，check什么 state check 它前面的这个断言，也就是这个 expression 它是不是正确。如果它返回的是 true 相安无事，尽管放马过去。那如果它返回了 false 那不好意思，我要给你抛出一个异常。


OK 那看第一个验证的是什么？ target type.get type parameters 它的长度应该等于零。大家知道这个 get type parameters 是做什么用处的吗？这个是泛型，大家有没有用过泛型，应该会在很多类上看到泛型的存在。那这里先要判断你的 class 上面有没有声明泛型。如果你声明了泛型 oh IM so sorry yeah 它这里会抛出一个异常 paramised the types unsupported 也就是不支持大家。记得不要在自己累上声明泛型。我这里给大家看一个更直观的例子，比方说 list 这个类，大家没有不认识的，看这是什么一个大 E 对不对？那这个就是它的泛型。你如果对这个 list 尝试调用它的 get type parameters 方法，那它会返回一个大 E 那我们这个 I service 上面有没有，没有任何泛型，所以相安无事，顺利过关。


那第二关它看什么？它看你的 get interfaces 它的长度是不是小于等于1。如果你大于 1 代表什么？代表你不只继承了一个接口，所以它后面的这个错误提示是什么？
Only single inheritance supported.


也就是说你只能做一个单继承。同学们，那大家如果使用愤的时候，一定要注意这些点，在你声明接口的时候，如果没有遵守，那你是启动不起来的。 OK 接下来如果你的 interface 长度等于1，那它会做一个额外验证，做什么呢？它拿出你当前继承的那个 interface 然后再看这个 interface 上面是不是还有 interface 那如果还有 interface 怎么样？不允许它只能允许 single level 也就是单层次的继承。那结合前面三个验证，给大家总结一下，分别是验证什么呢？ 1 不能存在泛型。


2 只能继承一个接口。 3 你所继承的这个接口，它上面不能再继承其他接口。三板斧很严格。同学们。 OK 因为我们这个 I service 有没有继承接口？没有一个接口，所以光明正大，安全通过往下走。那这个方法就要对每一个 method 进行灵魂拷问了。怎么个拷问法？首先你这个 method 的 declaring class 如果是一个 object 类型，no这是不允许的。也不能是一个 static 方法，并且它这边有一个 [util.is](http://util.is/) default 也不能是 default 否则的话那直接 continue 有请下一位。那这个 is default 它 default 什么内容呢？我们点进去看一眼。


好了，你看它这边是很多货运算符，可能现在很多年轻人并不会这样用了，像我们那个年代学上来的，经常会使用未运算符，按未操作来做判断。你点进去看它实际上是什么？ ox 是什么位数，大家知道吗？如果不知道要恶补基础知识了，我这里不给大家做科普了，回头大家可以去先温习一下如何做安慰运算，因为这是一个比较实用的小技巧，我们写代码的时候也经常会使用 MV 计算，如果你不知道的话，那有可能一下不清楚这是做什么的。


OK 这里有给大家的小课后作业，就是复习一下这个或的数字运算。好，我们返回那看这个当前的方法是谁我们现在当前在做灵魂拷问的是 say hi 这个方法。 OK 那我们继续走到这里，我要怎么样？我要抽取它的 method metadata 也就是这个方法级别的元数据。那怎么来抽取呢？很简单，把这个反射的方法扔进去，把这个 target type 也就是 iservice 这个类也给扔进去，扔到哪个方法里呢？ parse and validate metadata 这个方法里还是继续做数据验证，加上数据抽取，我们点进去走。


这里来到柳暗花明又一村啦，一个新的类叫什么 spring MVC contract 他终于来到自己的孙子辈这里了。好，我们看看这孙子他干什么事儿。首先第一步，把当前正在验证的这个方法加入到一个 processed methods 里面，也就是说这个 method 已经被处理过了，那它加到这个 method 里面是用的 key 这个 key 是一个方法签名，我们后面也会教大家如何使用 fin.config key 来生成一个方法签名。这个方法签名在某些配置文件中是很有用的。我们在后面的 high streaks 章节中将要针对每一个不同的方法，即便配置熔断策略的时候就会用到了。


第二步，你看他调用了 super 也就是他爸爸的 pass and validate meta date 的方法。那走我们看看他老父亲。这里又回到了他老父亲。老父亲是谁？ base contractor 对不对？这里看他做什么事儿。第一步，声明了一个 method metadata 变量，这个是 Java 里面的反射类吗？不是，他是 fen 自己的 meta data 咱 Java 里面可没有这号人物，老师行走江湖十几年都没见过的。第二步，怎么样呢？把这个 data 里面 return type 给拿到，return type 很容易，你通过反射力 get a generic return type 这里就能找到你方法的返回值是什么？咱的 say hi 是返回值是什么？是 string 对不对？非常轻巧。 OK 拿到的返回值。


接下来，我要把这个 data 里面塞入一个 config key 这个 config key 是他的身份标识，什么身份表示 thin config key 生成的一串针对这个方法的签名，我们来用 expression 先读为快看一下这个方法签名是什么。字有点小，跟大家念一下它的方法签名是接口的名称 I service 一个井号，后面跟方法名 say hi 再加一个括号，因为我们的 say hi 方法没有入参，也就是没有接收方法的参数，所以这个括号里面没有内容。


假如你接受了一个 int 接受了一些复杂类型，那么这个方法签名会有所不同的。所以咱说它是一个方法，唯一的身份标识。紧接着往后如果你的 target type 它有上游的 interface 怎么办？它叫 process annotation on class 那要把你这个 interface 也给审查一遍，因为我们只允许单继承对不对？你不能声明多个 interface 所以他这里很自信，直接拿到当前的第一个。这里我们就不深入进去看了。


我们走到下一步，审查完方法要审查自己了，你看这个一步步审查，这个比正审还严格，我们点进去看看好了，就当陪太子读书走，大家看到吗？我们叫这种方法叫什么？ If if if. 那就像周杰伦那首歌里唱的什么一蜗牛，我要一步一步往上爬，就像个楼梯一样，一步这个在咱正常写代码里面，尽量避免这种方式一个是丑。另外一个导致你这个代码的逻辑分支很长，有的时候公司要求比较严格，会上一些 sonarow sona check 你可能过不了。他是开源项目，他说了算，咱就跟着他走。首先看他的 class 的 get interface 是不是等于0，那咱当然是等于 0 了。等于 0 以后你看他这里拿到了一个 request mapping 那咱有没有配置？ request mapping 没有配置，所以不随他。愿咱这个 if 进不去。


如果你在上面配置了 request mapping 那它下面将会检查什么呢？它会对你这个声明的 path 也就是你 request mapping 中后面声明的一段访问路径进行检查。好，我们这里先溜过去，不管它了顺利通关，为什么咱顺利通关同学们咱没有用 request mapping A 咱用的是谁？ get mapping 感觉像从后门逃走的样子。Ok.再接下来，你看他这里还不放过，咱过五关斩六将不够。走到这里还要对你的 annotation 再做一个验证。哇好烦好烦。当前咱的方法有哪些？ annotation get mapping 看到吗？前面说我们从后门溜走了，这又不被逮到了是不是？好吧，那我们再进去陪他玩一番走。第一个方法进不去，我们没有 request mapping 又逃掉了。


接下来第二个方法他还不放过，还是执着的要拿 request mapping 同学们学的能拿到吗？非常不幸，告诉大家真的被拿到了，为什么我们明明没有配置 request VIP 还能被拿到？这里我带同学们看一下，你在 controller 里面我们配置的这个 service 上面点进去，这里有个 post mappingget mapping 对不对？你看它这上面写的是谁，你点到这个 get mapping 上面看这是谁 request mapping 注解就写在这里了。对不对？所以说它前面你用 request mapping 逃掉了方法的验证，但是他现在验证的是你的annotation ，这一步你又栽到他手里了，往下走。好了，你拿到了 request mapping 以后，这一步他要知道你是 HTTP method 是谁？那咱这里面不用看，拿到了一定是 get 如果你这个 master 没配，它默认给你放一个 get 这里也就是一个默认请求，你不配get ，我们所有请求在框架层面都是把你当成 get 的。接下往后走。这个方法名字他霸气了。


Check one. check 什么one ？点进去看看，原来他是 check 你当前这个 annotation 也就是 request mapping 中的 H tdp method 是不是只有一个？那你不能声明又是 post 又是 get 对不对？所以它这里只是做这样一个简单的 check 名字起的倒是挺霸气的。


做完检查以后，把你的当前的 method 的类型放到 metadata 里面，我们离元数据组件又前进了一步。接下来 check 完 HDD B method 我们要再来检查这个 path 这个 path 就是路径，它的名字起得更霸气了。 check at most one ，我们点进去看一下。从这个方法顾名思义实际上也是 check 你的方法的路径最多只能有一个，如果你包含多个怎么办，那它这里就会报错了。好，我们返回名字起的唬人东西简单。


下面一个if ，当你指定了路径的时候，它会进去。如果你的路径没指定，就是一个空默认，那它这里不会进去的。首先拿到你的 pass value 我们这里配的路径就是斜杠 say hi 如果你的 pass value 有值的话，它这边一个 resolve 方法，实际上你看 fin 这个方法起名虽然简洁，但是并不是那么直观。你比如 resolve 你可能还要点进去看一下，我们给方法起名的时候，尽量比这个再稍微具象那么一点最好了。 OK 那这个 resolve 实际上是看你的 value 有没有一些 placeholder 你如果有一些占位符，那它会这里给你做一下处理。好这里返回以后，我们看经过处理的 pass value 还是 say hi 我们没有任何占位符的。那接下来这一步会对你的路径做一些规范。比如说在前面给你加入一个斜杠，规范完了以后，那就把你加入到 metadata 里边，我们的组件过程即将进入尾声了。


下一步是解析 producesproduces 是什么东西，点进去看看就知道了。好，我们这里从这个 annotation 上面获得了 server produces 我们这个什么都没有配置，它这里是拿不到的，往下走直接返回，很顺利的通关。
produce 完了再解析 consumes 点进去。 consumes 有没有依然是空的。我们用的极简配置就是想要它快速通关。那大家知道这个 purse produce 和 purse consumer 它意义是在哪吗？它意义是构造你的 header 大家心里有个数就可以。比方说 pass produce 里面它构造的是 accept 如果你 client accepts 不为空，它会把你配置的 client accepts 指定到 header 里面，那这个 header 也是 metadata 的一部分。同样的你的 past consumer 也是指定了 header 但是它并不是 accept 的，而是 content 点进去看 content type 所以这两个参数都是和 header 有关的。那么接下来这一步我们就要正儿八经的开始处理 header 了，怎么处理？点进去。


如果你的 annotation 上面设置了 header 大家注意你要设置了 header 它这里才会进去的。我们没有设置，所以直接跑到底了。那我们不妨回头看一下。如果你设置了 header 它怎么办？你的 header 中如果有一个等号，并且它不包含这个不等号的话，那它将要对你的占位符进行处理，将处理后的结果同样的加入到元数据。所以你看整个代码流程对源数据的解析相当细致，什么细枝末节它通通都不放过的。


好，最后一个处理完它就大结局了吗？好像还没有。那他这里只是处理完了一个 annotation 假设你这边还有其他 annotation 这个日子简直没完没了了，过不下去，再往后走一个 check state 这个 check state 它检查你的 metadata 里面是不是有方法信息了。如果你前面既没有加这些 get mappings 也没有加 request mappings 之类 annotation 那到这一步你就可以拜拜了一张飞机票。


走人好，再往下走，他开始对你的方法的参数类型开始做检查了，拿到你的 parameter types 我们有没有我们这里是空，因为方法里面没有接受任何的参数。再往下走这个事精又来找事了，他检查了你方法上的 annotation 还不够，你的参数上的 annotation 他也要再检查一遍，真的是事无巨细。
好，我们的方法上面有 annotation 吗？很高兴的告诉大家，大家节省了至少 10 分钟，我们方法上什么都没有，所以直接跳到了下一步。但是不妨切上去看一看。假设你有 annotation 那它这里会使用一个新的方法叫 process annotation on parameter 使用这个方法来验证你的 annotation 大家还记得我们其中有一些 pose 的方法，在它的入参上面也是有 annotation 的。所以有兴趣的同学可以在这边打一个断点，然后 debug 一下后续的方法，它怎么处理这部分流程，我们时间关系就不带大家看这里的步骤了。


接下来往后看我们的 header map index 是空的，所以这里跳过这一步是验证 query map index 的，同样我们也是空的。好，这里 return data 返回到上一层，那这就完事了吗？没有，同学们再往下走一步，这个 target type 又回到了 I service 这个类，他再次尝试找 request mapping 当然找不到了。那如果不幸被他找到了怎么办呢？那他是从 request mapping 中再会去拿 H ttb header 中的内容。我们这里因为没有设置 request mapping 所以这一步骤就跳过了。同学们可以这样尝试着在你的代码中某些方法上使用 get mappings 或者 post mapping 在其他方法尝试使用 request mapping 用不同的注解来看一看它这之间的解析都有什么不同。


我这里 meta data 终于构造完成了，返回到上一层，大家刚才深入敌后太久了，可能都忘了这一层是干什么的了，这一层就是我们入口的类，我们几乎就快要抵达终点了。坚持住好，把一个 method 也就是方法的元数据抽取出来以后，他这边要做一个什么检查呢？他要看你这个 result 里面是不是曾经处理过这个方法了。如果你曾经没有处理过这个方法，也就是说你并没有重在这个方法。那 OK 你可以顺利越过检查。每一个方法只能被处理一次，同学们他不能被处理两次。我们这个方法处理完了以后，接下来他就要处理 iservice 的其他方法了。因为步骤都是大同小异，所以这里就不一步步跟进去了。那同学们这里要打一个断点，自己跟进去看一看。因为相对于瑞本和尤瑞卡份组件的代码难度稍微有那么一点点的提升，这也是个循序渐进的过程，给后面更难的 high streaks 做铺垫。我这里直接在返回的地方打上一个断点，跑到结尾


处，大结局好跳到这里来了。那整个流程就结束了。相比较其他组件，其实分的代码并不算难。如果大家在 debug 的过程中，觉得看起来有那么点吃力，说明要好好的修炼这个阅读圆满的内功了。


我们说武林高手有一种什么境界啊？手中无剑，心中有剑对不对？草木树叶皆可伤人。那我们架构师的境界应该是什么呢？应该是眼中有马，心中午马。所以老师现在看所有东西都是午马的。现在倡导一个什么理念呢？就是说你即便成为架构师你也不能脱离一线，并不说你让你当一个 PB D 的架构师，让你只会写那种很 high level 很顶层的设计没有用的，除非你是整个集团的架构师。


Ok.那作为一个项目的架构师，你一定要深入自己的代码去研究。你不光要结合业务，你也不能脱离实际的代码，你把这个丢了。那作为一线的架构师其实是根本不合格的。我个人是很鄙视那些根本不写代码并且还在一线做架构师的人。这类人真的有很多，你即便像阿里这种水货也是比比皆是鱼龙混杂之地，我们不要当这种人，一定要亲身的去关注你的代码，这样你的架构才叫有源之水。你不能成为一个无源之水。但是如果你只是关注自己的一亩三分地，哼哧像老黄牛一样写代码，这叫闭门造车。那怎么样才能引来活水呢？看开源软件的项目。作为开源软件的开发者，如果你代码写得不好，要被全世界的人喷，所以他们的心理压力有多大呢？肯定写的都是相当工整的。所以我们多从开源项目的代码中汲取营养，这就叫开卷有益啦。同学们，那希望大家以后也能做到眼中有码，心中午马的境界。


OK 那这一节的内容就到此为止了。接下来一节我要带大家一起去做电商项目的改造了。学了这么多，终于有用武之地了，同学们站起来活动准备下一节开工吧。 See you later.





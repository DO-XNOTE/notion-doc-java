---
title: 4-11 批量操作 bulk 增删改查
---

# 4-11 批量操作 bulk 增删改查

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/c56ea0d1-051e-49a3-b074-9b824e852e6c/SCR-20240818-ojfq.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XH6YMKYT%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCb1o7%2BAVDff1p6yx%2BuQOmaiAID6JIyRxVx%2F2fJKcl%2BbgIgCMyn0WUBIW3NAfxwt86RC7Mwz90ZKHsIFoU52GDZdkwqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJlnHz0WrgGMKFrxNSrcAzT%2BzYLedwY57zliXoIa%2FRjkWfn8s3ka%2F6l9rFDVAY9qClPAMUhMzi1FYbMMDrZvsgL%2FgBusI%2F%2FPiTkMiAO%2BG1xwYmMbW92FQgojpcBbfCh1OVwWUNP0mBLcoS6%2FNXtZ%2FbrB%2F8R75JWajgeppcEzCFv4aB8gATbTAJfFba4skrHOaRZKkV7%2FAJo4t2sLmC%2F2DTbpN%2Be7aNJJ6iXOog%2FseC4rThTKmEykPjhj5rTz3fZrCpn4sqxiO2embUFXH9egNHlE5IXeK%2BimzbeSOrwls4T4efixi2JMinezfdCy6q7R1FysFrPHn1eXzYXM5zSloBPXxwu8i7utHAUmLtaEhB8c8MPhFFnY%2BJKJv2e%2FZNDfnxxJNXSHhhI3xZSScvTr0O3XToMRenFnsEoB1rBg4tcpMEs1O3ZQ8EuU%2FKywwJlrcp%2FCpXJLEtMAFZkwW2HRV%2FiNbqRM2YIFX3O5X6YGnSTXd9qAguoydVQfLqmrefpQxSL5soodjcnRssxa9qCa%2F5pvrSDUjQ%2FtlaNNj8Kq%2F1kKtb5g5l0Yv6lSuI1rZdQNOoy4GApai0AfbWlQlraI%2F19LbHHsXNQyQJAZ3uG8IcGaP9YfONYVhZXB6WiW2FAW3ANOVbEDnTuAN97oMMK6%2F9IGOqUBLCDjKDPfKFMYd3rCjHyYmcPAhAI41dCor4cgIO5puWxS1tohxX9tHUjYsulCjSkpmVFnYEhyl2T9IHusoQs1MlGJakfEdseDt95EVgvZcB%2BsstExYLlYK6Pjl9Ju8dKz5If7aEHUdhKrttt5sf8SelDw3kKK4vllojbfoV5WpYKaTWakPvalfqYgrELU46sO5rFCt7dkRt0KJ75gy7%2F3pBAigy%2Fp&X-Amz-Signature=fc53b351f819abdbdab9fc326bb0e1f220e226ff615932fa19fd3e19492efaf2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/d2731a61-ede1-4822-be0d-5ea47a557b7a/SCR-20240806-fjrz.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XH6YMKYT%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCb1o7%2BAVDff1p6yx%2BuQOmaiAID6JIyRxVx%2F2fJKcl%2BbgIgCMyn0WUBIW3NAfxwt86RC7Mwz90ZKHsIFoU52GDZdkwqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJlnHz0WrgGMKFrxNSrcAzT%2BzYLedwY57zliXoIa%2FRjkWfn8s3ka%2F6l9rFDVAY9qClPAMUhMzi1FYbMMDrZvsgL%2FgBusI%2F%2FPiTkMiAO%2BG1xwYmMbW92FQgojpcBbfCh1OVwWUNP0mBLcoS6%2FNXtZ%2FbrB%2F8R75JWajgeppcEzCFv4aB8gATbTAJfFba4skrHOaRZKkV7%2FAJo4t2sLmC%2F2DTbpN%2Be7aNJJ6iXOog%2FseC4rThTKmEykPjhj5rTz3fZrCpn4sqxiO2embUFXH9egNHlE5IXeK%2BimzbeSOrwls4T4efixi2JMinezfdCy6q7R1FysFrPHn1eXzYXM5zSloBPXxwu8i7utHAUmLtaEhB8c8MPhFFnY%2BJKJv2e%2FZNDfnxxJNXSHhhI3xZSScvTr0O3XToMRenFnsEoB1rBg4tcpMEs1O3ZQ8EuU%2FKywwJlrcp%2FCpXJLEtMAFZkwW2HRV%2FiNbqRM2YIFX3O5X6YGnSTXd9qAguoydVQfLqmrefpQxSL5soodjcnRssxa9qCa%2F5pvrSDUjQ%2FtlaNNj8Kq%2F1kKtb5g5l0Yv6lSuI1rZdQNOoy4GApai0AfbWlQlraI%2F19LbHHsXNQyQJAZ3uG8IcGaP9YfONYVhZXB6WiW2FAW3ANOVbEDnTuAN97oMMK6%2F9IGOqUBLCDjKDPfKFMYd3rCjHyYmcPAhAI41dCor4cgIO5puWxS1tohxX9tHUjYsulCjSkpmVFnYEhyl2T9IHusoQs1MlGJakfEdseDt95EVgvZcB%2BsstExYLlYK6Pjl9Ju8dKz5If7aEHUdhKrttt5sf8SelDw3kKK4vllojbfoV5WpYKaTWakPvalfqYgrELU46sO5rFCt7dkRt0KJ75gy7%2F3pBAigy%2Fp&X-Amz-Signature=c6a53782f57d8e1dc60afd63bd10e3a19ea5b8d216e472eb750f9fee4fa49cc8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

4—11附：批量操作bulk
基本语法
bulk操作和以往的普通请求格式有区别。不要格式化json，不然就不在同一行了，这个需要注意。
action: metadata }}\n request body
}\n action: metadata }}\n request body
}in
·{action:{metadata }}代表批量操作的类型，可以是 新增、删除或修改
·\n是每行结尾必须填写的一个规范，每一行包括最后一行
都要写，用于es的解析
·{ request body }是请求body,增加和修改操作需要，删 除操作则不需要
批量操作的类型
action必须是以下选项之一：
·create：如果文档不存在，那么就创建它。存在会报错。发
生异常报错不会影响其他操作。
·index：创建一个新文档或者替换一个现有的文档。
·update：部分更新一个文档。
·delete：删除一个文档。
metadata 中需要指定要操作的文档的_index、_type 和_id, _index 、_type 也可以在url中指定
实操
·create新增文档数据，在metadata中指定index以及type POST /_bulk
{"create": {"_index": "shop2", "_type": "_doc", id": "2001"1
{"id": "2001"，"nickname": "name2001"}
{"create": {"_index": "shop2", "_type": "_doc", id": "2002"11
{"nickname":"name2002","id":"2002"}
{"create": {"_index": "shop2", "_type": "_doc", id": "2003"1
{"id": "2003"， "nickname": "name2003"}
·create创建已有id文档，在url中指定index和type POST /shop/_doc/_bulk
{" create":{" id": "2003"])
{"id": "2003"，"nickname":"name2003"} {"create":{"_id":"2004"}}
("id" : "2004", "nickname" : "name2004") {" create":{"_id":"2005"}
{"id": "2005"，"nickname": "name2005"}
·index创建，已有文档id会被覆盖，不存在的id则新增POST /shop/_doc/_bulk
{" index":{"_id":"2004"}}
{"nickname":"index2004","id":"2004"} {"index":{"_id":"2007"}}
{"id": "2007"，"nickname":"name2007"} {"index":{"_id":"2008"}}
｛"id":"208"," nickname":"name2008"
·update跟新部分文档数据
POST /shop/ doc/ bulk {"update":{"_id":"2004"}} {"doc":{"id":"3004"}} {" update":{"_id":"2007"}}
("doc": "nickname": "nameupdate"}}
·delete批量删除
POST
/shop/doc/bulk {" delete": {" id": "2004"}] {"delete":{"_id":"2007"}} 综合批量各种操作
POST
/shop/_doc/_bulk {" create":{"_id":"8001"}}
("id": "8001", " nickname": "name8001"] {" update":{"_id":"2001"}}
{"doc":{"id":"20010"}} {" delete'": {" id": "2003"}] (" delete'": [" id": "2005"}}
·官文：https:/www.elastic.co/guide/cn/elasticsearch/guide/curre nt/bulk.html


[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/be10ab42-0f66-4b8d-854c-5a83c04fcccb/2020-09-17_175624.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XH6YMKYT%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225151Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCb1o7%2BAVDff1p6yx%2BuQOmaiAID6JIyRxVx%2F2fJKcl%2BbgIgCMyn0WUBIW3NAfxwt86RC7Mwz90ZKHsIFoU52GDZdkwqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJlnHz0WrgGMKFrxNSrcAzT%2BzYLedwY57zliXoIa%2FRjkWfn8s3ka%2F6l9rFDVAY9qClPAMUhMzi1FYbMMDrZvsgL%2FgBusI%2F%2FPiTkMiAO%2BG1xwYmMbW92FQgojpcBbfCh1OVwWUNP0mBLcoS6%2FNXtZ%2FbrB%2F8R75JWajgeppcEzCFv4aB8gATbTAJfFba4skrHOaRZKkV7%2FAJo4t2sLmC%2F2DTbpN%2Be7aNJJ6iXOog%2FseC4rThTKmEykPjhj5rTz3fZrCpn4sqxiO2embUFXH9egNHlE5IXeK%2BimzbeSOrwls4T4efixi2JMinezfdCy6q7R1FysFrPHn1eXzYXM5zSloBPXxwu8i7utHAUmLtaEhB8c8MPhFFnY%2BJKJv2e%2FZNDfnxxJNXSHhhI3xZSScvTr0O3XToMRenFnsEoB1rBg4tcpMEs1O3ZQ8EuU%2FKywwJlrcp%2FCpXJLEtMAFZkwW2HRV%2FiNbqRM2YIFX3O5X6YGnSTXd9qAguoydVQfLqmrefpQxSL5soodjcnRssxa9qCa%2F5pvrSDUjQ%2FtlaNNj8Kq%2F1kKtb5g5l0Yv6lSuI1rZdQNOoy4GApai0AfbWlQlraI%2F19LbHHsXNQyQJAZ3uG8IcGaP9YfONYVhZXB6WiW2FAW3ANOVbEDnTuAN97oMMK6%2F9IGOqUBLCDjKDPfKFMYd3rCjHyYmcPAhAI41dCor4cgIO5puWxS1tohxX9tHUjYsulCjSkpmVFnYEhyl2T9IHusoQs1MlGJakfEdseDt95EVgvZcB%2BsstExYLlYK6Pjl9Ju8dKz5If7aEHUdhKrttt5sf8SelDw3kKK4vllojbfoV5WpYKaTWakPvalfqYgrELU46sO5rFCt7dkRt0KJ75gy7%2F3pBAigy%2Fp&X-Amz-Signature=816b25f671ccad2c7e8be4fa4cac2e3239ad46aca5486bc6f446d8dcbb127e5f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


---
title: 2-12 本地消息表（订单操作接口）
---

# 2-12 本地消息表（订单操作接口）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/aab81de7-66f4-4cb4-b323-c0c89a6ad00c/SCR-20240808-evsa.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665WFMA2BL%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225436Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDRC8uH2ykVIlTZPgpneQx59KolwzvBUbxE3n9QeUev3QIgIaDPZe40FC5r1a%2FAKsfKwFOzkar1QYeFIPosCj1KFXUqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPEv89WXzxVXUwa6FircAxEVbo4SgSmHaTiBh28sb2tvZOt0xe5ng74JQhBUGbM1AARZ%2F%2B4oGCpe9MVf%2Bw9B43GsoeNhlBPaOQIM0%2BvG7roq%2Bp5PTZ9hl6tewmHI53RbW%2BKROQNQk6RURmBsXVSkDeU%2FMrPKG5KFQNq0ZUGcSdup%2FoUnX%2By5XHQ%2FUUtI8E%2B99Jk9gugJW2EapO%2BdzZBsMj5U%2BeR9xVH75WYZGbw%2FgV5O%2BXjKVjGk0GKihlEOpTHwogaFNqHa4fX16EDHT9%2FbWTB92Z0SHT23WAK3yXUzQ3PMRI7Jh0%2FpvkJYQXu7zHy%2Bwt2Bvw5R4vuhyy%2BWMOwNXeipo0k0mKQXTHZwUpGHOCq5GvoV3Rtc6YPPZPN5zshE%2BA8B6NFJDNg5WLJ2dV22gy7%2BgwxUYWcosMGSEpb1iU3clsG7pEAzzaobwZzILNSSj2vsWXlTSOg4wdAJcbHHs9JowXSzLxLVFX6%2BURc9pL%2BFaNNTJi5%2B7XYIO9cCqVL9PIKCf0xiMhTe00Uw7P6AJpAlVA900EUzb5YXkSimuGKviX5PjUviSvVtle1CgYRiCrAWWtLAteClWO8RXwxFukjQJQKi7O%2BdM%2B9LYbexJN%2BJtF45s6Sx1FcglANrbJT2BlO7p4t6upxDqeaCMIW4%2F9IGOqUBlJJebW1ogMLd%2F2onifZLJDAaTvUY0FzlMkHuzSDLBiDVOzb2eVgV2nTu1JgAgrlPOCEFuPAlh%2BowLvTmPbR3Tz6Sm4jKIOf%2FU0XdqGXk9ShfDqpdMYl9elRIMlHc2EkrpYJjEx1DY331BsqXkzKsWn5CnfHrzF5uRAv0OnTDV6nnzTA56e8rkU2J86lXCFfqWQm3guebxb3MfclmmsqhzsRlVt17&X-Amz-Signature=d147db7c26819a77309df9e908a1f12c50174d1fdb356da73d49950e30a5e650&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/2343d54c-3779-48cc-ba64-1281f26c2bf4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665WFMA2BL%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225436Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDRC8uH2ykVIlTZPgpneQx59KolwzvBUbxE3n9QeUev3QIgIaDPZe40FC5r1a%2FAKsfKwFOzkar1QYeFIPosCj1KFXUqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPEv89WXzxVXUwa6FircAxEVbo4SgSmHaTiBh28sb2tvZOt0xe5ng74JQhBUGbM1AARZ%2F%2B4oGCpe9MVf%2Bw9B43GsoeNhlBPaOQIM0%2BvG7roq%2Bp5PTZ9hl6tewmHI53RbW%2BKROQNQk6RURmBsXVSkDeU%2FMrPKG5KFQNq0ZUGcSdup%2FoUnX%2By5XHQ%2FUUtI8E%2B99Jk9gugJW2EapO%2BdzZBsMj5U%2BeR9xVH75WYZGbw%2FgV5O%2BXjKVjGk0GKihlEOpTHwogaFNqHa4fX16EDHT9%2FbWTB92Z0SHT23WAK3yXUzQ3PMRI7Jh0%2FpvkJYQXu7zHy%2Bwt2Bvw5R4vuhyy%2BWMOwNXeipo0k0mKQXTHZwUpGHOCq5GvoV3Rtc6YPPZPN5zshE%2BA8B6NFJDNg5WLJ2dV22gy7%2BgwxUYWcosMGSEpb1iU3clsG7pEAzzaobwZzILNSSj2vsWXlTSOg4wdAJcbHHs9JowXSzLxLVFX6%2BURc9pL%2BFaNNTJi5%2B7XYIO9cCqVL9PIKCf0xiMhTe00Uw7P6AJpAlVA900EUzb5YXkSimuGKviX5PjUviSvVtle1CgYRiCrAWWtLAteClWO8RXwxFukjQJQKi7O%2BdM%2B9LYbexJN%2BJtF45s6Sx1FcglANrbJT2BlO7p4t6upxDqeaCMIW4%2F9IGOqUBlJJebW1ogMLd%2F2onifZLJDAaTvUY0FzlMkHuzSDLBiDVOzb2eVgV2nTu1JgAgrlPOCEFuPAlh%2BowLvTmPbR3Tz6Sm4jKIOf%2FU0XdqGXk9ShfDqpdMYl9elRIMlHc2EkrpYJjEx1DY331BsqXkzKsWn5CnfHrzF5uRAv0OnTDV6nnzTA56e8rkU2J86lXCFfqWQm3guebxb3MfclmmsqhzsRlVt17&X-Amz-Signature=fb8ae6fae8cb9ca59dc77e356180ffa8d0d197a0aa25ed0d354009276e953a5c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

咱们再写这个操作接口，这个操作接口主要是更改这个订单的状态是吧。这块咱们同样创建一个 order service order service 打上注解。然后里边咱们要引入 order map 是吧，因为咱们要操作这个订单，order mapper resource 是吧。这个咱们也是写一个方法返回一个结果，结果的类型是 int 类型，方法的名字咱们叫做 handle order 好吧，里边的参数咱们其实只需要一个订单 ID 是不是就可以了？咱们查找到这个订单给他，把支付状态改一下，就完成咱们的这一步操作。


这块咱们还是在这个方法上加上一个注释，这个叫做订单回调接口是吧。第一步咱们要查询出这个订单 select by primary key 是吧。 Order id. 如果这个订单不存在的话，咱们直接返回一个错误。如果订单等于空，咱们直接返回一个一这块备注一下，1订单不存在。然后咱们把这个订单给他支付状态改一下 order status 设置成为一已支付。最后要设置它的 update 是吧？
Update time new date.


把这个类给它引入一下最后一个字段，更新人是吧。 update user 咱们就设置成为0。 0 是系统更新，最后 order mapper update primary key 是吧。 order 最后 return 一个0。 0 代表的是成功，那时候就可以了。同样咱们也写一个 controller 写一个 order controller 打上一个 rest controller 里边，把这个 order service 给它注入进来。 order size 咱们拼写错了是吧，改一下。


好了是吧，引入一下，然后 order service 上面加个 auto where 同样写一个方法，咱们也叫handle 。 handle order 传入一个订单的 ID 然后调用 order service 的 end order 前面有一个处理的结果，订单处理完成以后，咱们要给调用方返回一个成功或者失败的标识是吧。这那咱们判断，如果这个结果等于0，咱们就返回一个 success 好吧，一会咱们这个定时任务就去判断，如果接口返回此个SaaS ，咱们把这个消息的状态给它改成已发送，那么其他的情况咱们就返回一个费用。好吧，最后这一块咱们还要用开始给他包一下是吧。


catch 如果有这个 exception 咱们也给它返回 fail 这样是不是就可以了？然后前面给他打一个 request mapping 的注解，注解的名字叫做 handle order 那是不是就写完了？咱们再测试一下这个接口，启动一下这个项目，进入到启动内启动一下。


然后打开浏览器，想问一下这个处理订单的接口，local house 8080 handle order 然后 order ID 等于上一节课咱们设置的这个 order id010 是吧，这条记录是不是在数据库还没有了？咱们在这个数据库里边新建一条订单的记录。进入到这个 132 的 order 表，创建一个订单的记录。订单 ID 就是 10010 是吧，auto status 0 未支付 amount 200 这个收货人咱们随便写一个，写成慕课。


手机号 1341234 个 14 个 2 好吧，模拟一下创建用户一个就是当前的时间更新人和他是一样的，然后保存一下，这个订单在这个表里边就已经有了是吧，咱们访问一下这个接口，返回 success 成功了是吧？刷新一下这个订单，这个订单的状态已经变成了一已支付是吧。那么咱们这个第二步就写好了，第二步是这个操作接口，它主要是处理订单的状态。那么接下来咱们就要编写这个定时任务，把这个第一步和第二步给它串起来，咱们下一节再给大家编写这个竞职任务。



## 


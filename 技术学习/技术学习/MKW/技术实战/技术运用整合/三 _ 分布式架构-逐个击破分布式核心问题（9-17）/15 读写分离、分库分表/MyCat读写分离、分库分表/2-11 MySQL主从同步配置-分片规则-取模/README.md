---
title: 2-11 MySQL主从同步配置-分片规则-取模
---

# 2-11 MySQL主从同步配置-分片规则-取模

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/ba7877f8-ce74-46fa-a12a-745b40ca8eb7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQ2H5XWG%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCx3UPx8ol6%2BSjnREH2mOLO95cnaRAK9wpRNGxK5CgvEQIhAKGnBGjSkpB7BL1ojKiw3NDoTCiweNgahqEjQd4OqOY6KogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx1IZJVZLrx%2F832ajkq3ANSqM6%2F%2BP1F4a0ZnSs39pjUeMXeCuyGj5k9oX9%2B92lfWMCa23FjOa49yQjld2Tft0OXFp5kyj8fhyJ0o8w%2FRrZnMhNRZ61Y0W2YncGj45gFXG%2F5s8uT5cvE5WPRtQ%2Fy9G%2BUAA%2BNjY8T3xnjqvvaQeHZ5IZppT4QcaR258BZcRN%2BPwoXyvvQeD%2BlfLpVeIK60pU3jk7fsP4G2Zbfk85%2BfEE9RuXwSS181zSCTIDWVtGGIe%2F3PNW1x9r6WQu964mSBBzqNuJop0XJY8jUV8ye%2ByCUw0bPBpHLNmQMxbKtwUzazqEjVb3ezm6lyxZ5Oj8e7i2I2VG76v9HtRg%2BD0FyueSYThEHry5YPiAaSdEAj2sF5I9NzLlDQz5oIvsW2ohi7GXEVFzZeE7idzT4ruvoifaGt6EQZxc5C723SihdyoqKo2w34Mo62qdJJXCYy8KthpQcAer%2Fu8lRXEhhkBuxvSJqoDT4Ni3fGz74%2FgVocw8O3JqQFXyjISPHKupTlDWErIuaJs%2FMdSiX62wKAjDZfxwNdjg%2FzMG9erTGG%2BvoL%2FQlHYqgedkQXpslI%2BJJT8l%2FnV5D5JGDXUCix8%2BBFRkrWDyKPt%2B9K6SYYHrW%2BO%2BJz8DHPoIljee2dB9TDLUCJzDXuf%2FSBjqkAeWAy1wadipBmBzpyJwMfGTVG4GOspQXzOQLEkMvwf%2F55NdxfbhfFrp2UeR5%2BNhgQ0kMiCNpTJ%2F8%2Bl1b3B6BnlIiB%2F%2FpjIpz%2BOHYaJMKH6YiG5TyywIor28qdsvGbn6Z4DiLJwdkCCM2343PgICY%2BcfPSPMDwmQwQrzIAxXCdr%2B53l6RSp4ASIW6LXb9rtUn6UZAj7AWzqb3fqswcWgfOqqM71Qn&X-Amz-Signature=f282bbe491224cee8d254e2446f6c2f2540beca1ff4ca48e97bc94a723b756da&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/11b8efa2-e3ad-4f73-8089-48c7d4ee68d7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQ2H5XWG%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCx3UPx8ol6%2BSjnREH2mOLO95cnaRAK9wpRNGxK5CgvEQIhAKGnBGjSkpB7BL1ojKiw3NDoTCiweNgahqEjQd4OqOY6KogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx1IZJVZLrx%2F832ajkq3ANSqM6%2F%2BP1F4a0ZnSs39pjUeMXeCuyGj5k9oX9%2B92lfWMCa23FjOa49yQjld2Tft0OXFp5kyj8fhyJ0o8w%2FRrZnMhNRZ61Y0W2YncGj45gFXG%2F5s8uT5cvE5WPRtQ%2Fy9G%2BUAA%2BNjY8T3xnjqvvaQeHZ5IZppT4QcaR258BZcRN%2BPwoXyvvQeD%2BlfLpVeIK60pU3jk7fsP4G2Zbfk85%2BfEE9RuXwSS181zSCTIDWVtGGIe%2F3PNW1x9r6WQu964mSBBzqNuJop0XJY8jUV8ye%2ByCUw0bPBpHLNmQMxbKtwUzazqEjVb3ezm6lyxZ5Oj8e7i2I2VG76v9HtRg%2BD0FyueSYThEHry5YPiAaSdEAj2sF5I9NzLlDQz5oIvsW2ohi7GXEVFzZeE7idzT4ruvoifaGt6EQZxc5C723SihdyoqKo2w34Mo62qdJJXCYy8KthpQcAer%2Fu8lRXEhhkBuxvSJqoDT4Ni3fGz74%2FgVocw8O3JqQFXyjISPHKupTlDWErIuaJs%2FMdSiX62wKAjDZfxwNdjg%2FzMG9erTGG%2BvoL%2FQlHYqgedkQXpslI%2BJJT8l%2FnV5D5JGDXUCix8%2BBFRkrWDyKPt%2B9K6SYYHrW%2BO%2BJz8DHPoIljee2dB9TDLUCJzDXuf%2FSBjqkAeWAy1wadipBmBzpyJwMfGTVG4GOspQXzOQLEkMvwf%2F55NdxfbhfFrp2UeR5%2BNhgQ0kMiCNpTJ%2F8%2Bl1b3B6BnlIiB%2F%2FpjIpz%2BOHYaJMKH6YiG5TyywIor28qdsvGbn6Z4DiLJwdkCCM2343PgICY%2BcfPSPMDwmQwQrzIAxXCdr%2B53l6RSp4ASIW6LXb9rtUn6UZAj7AWzqb3fqswcWgfOqqM71Qn&X-Amz-Signature=d9d4878d21a27e5a447f8f21bdc0875a99e45df3e84a4d2509574bf1737b49c9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

**2-11 附:MySQL主从同步配置**

```java
MySQL主从同步配置

1.编辑MySQL主上的/etc/my.cnf，

log-bin=imooc_mysql

server-id=1

log-bin ：MySQL的bin-log的名字

server-id : MySQL实例中全局唯一，并且大于0。

2.编辑MySQL从上的/etc/my.cnf，

server-id=2

server-id : MySQL实例中全局唯一，并且大于0。与主上的 server-id 区分开。

3.在MySQL主上创建用于备份账号

mysql> CREATE USER 'repl'@'%' IDENTIFIED BY 'password';

mysql> GRANT REPLICATION SLAVE ON *.* TO 'repl'@'%';

4.MySQL主上加锁，阻止所有的写入操作

mysql> FLUSH TABLES WITH READ LOCK;

5.MySQL主上，查看bin-log的文件名和位置

mysql > SHOW MASTER STATUS;

6.MySQL主上dump所有数据，

mysqldump --all-databases --master-data > dbdump.db -uroot -p

7.MySQL主进行解锁，解锁后，主上可以写入数据

mysql> UNLOCK TABLES;

8.MySQL从上导入之前dump的数据

mysql < aa.db -uroot -p

9.MySQL从上配置主从连接信息

mysql> CHANGE MASTER TO

-> MASTER_HOST='master_host_name',

-> MASTER_PORT=port_num

-> MASTER_USER='replication_user_name',

-> MASTER_PASSWORD='replication_password',

-> MASTER_LOG_FILE='recorded_log_file_name',

- > MASTER_LOG_POS=recorded_log_position;

master_host_name : MySQL主的地址

port_num : MySQL主的端口（数字型）

replication_user_name : 备份账户的用户名

replication_password : 备份账户的密码

recorded_log_file_name ：bin-log的文件名

recorded_log_position : bin-log的位置（数字型）

bin-log的文件名和位置 是 步骤5中的show master status 得到的。

10.MySQL从上开启同步

mysql> START SLAVE;

查看MySQL从的状态

show slave status;
```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/d6a5d8af-e06c-410c-b615-a8a32e39ec8a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQ2H5XWG%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCx3UPx8ol6%2BSjnREH2mOLO95cnaRAK9wpRNGxK5CgvEQIhAKGnBGjSkpB7BL1ojKiw3NDoTCiweNgahqEjQd4OqOY6KogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx1IZJVZLrx%2F832ajkq3ANSqM6%2F%2BP1F4a0ZnSs39pjUeMXeCuyGj5k9oX9%2B92lfWMCa23FjOa49yQjld2Tft0OXFp5kyj8fhyJ0o8w%2FRrZnMhNRZ61Y0W2YncGj45gFXG%2F5s8uT5cvE5WPRtQ%2Fy9G%2BUAA%2BNjY8T3xnjqvvaQeHZ5IZppT4QcaR258BZcRN%2BPwoXyvvQeD%2BlfLpVeIK60pU3jk7fsP4G2Zbfk85%2BfEE9RuXwSS181zSCTIDWVtGGIe%2F3PNW1x9r6WQu964mSBBzqNuJop0XJY8jUV8ye%2ByCUw0bPBpHLNmQMxbKtwUzazqEjVb3ezm6lyxZ5Oj8e7i2I2VG76v9HtRg%2BD0FyueSYThEHry5YPiAaSdEAj2sF5I9NzLlDQz5oIvsW2ohi7GXEVFzZeE7idzT4ruvoifaGt6EQZxc5C723SihdyoqKo2w34Mo62qdJJXCYy8KthpQcAer%2Fu8lRXEhhkBuxvSJqoDT4Ni3fGz74%2FgVocw8O3JqQFXyjISPHKupTlDWErIuaJs%2FMdSiX62wKAjDZfxwNdjg%2FzMG9erTGG%2BvoL%2FQlHYqgedkQXpslI%2BJJT8l%2FnV5D5JGDXUCix8%2BBFRkrWDyKPt%2B9K6SYYHrW%2BO%2BJz8DHPoIljee2dB9TDLUCJzDXuf%2FSBjqkAeWAy1wadipBmBzpyJwMfGTVG4GOspQXzOQLEkMvwf%2F55NdxfbhfFrp2UeR5%2BNhgQ0kMiCNpTJ%2F8%2Bl1b3B6BnlIiB%2F%2FpjIpz%2BOHYaJMKH6YiG5TyywIor28qdsvGbn6Z4DiLJwdkCCM2343PgICY%2BcfPSPMDwmQwQrzIAxXCdr%2B53l6RSp4ASIW6LXb9rtUn6UZAj7AWzqb3fqswcWgfOqqM71Qn&X-Amz-Signature=fa7df50a522a8b38bfbcda528fff72cc31d98684be200457daf4d0949ccd2be3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

介绍，另外一种非常常用的这个分片规则就是这个曲膜曲膜咱们大家看一下里边都配置哪些内容？首先也是配置你要分片的这个列是吧。 Column. 然后分片的逻辑就是 model law 它是曲模。来具体看一下后边的这个方特审。方特审里边只有一个配置，就是你 data note 的数量。它的这个例子当中 data note 是有三个，咱们来看看这个说明，此种配置非常明确，即根据 ID 进行时进制的取模运算。也就是说你有几个 data load 我就会用你的这个列的值，也就是说你的这个 user ID 对你的 count 去进行取模，取得这个模式集我就插入哪一个分片当中。咱们举个例子，比如说你的这个 ID 是15，然后 15 对 3 取模等于0。那么你的这条数据将会给它分到数据节点 1 当中。如果这个 user ID 比如说等于 88 对这个三个进行取模，得到的是2，咱们这条数据将会分配到数据节点 2 当中。


咱们现在就试一下，咱们还是打开 130 这台机器。首先要看一下 steamer 的叉 L 怎么，把这个弱给它改一下，给它改成摩的浪是吧，复制一下，给它粘贴过来，然后保存再。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/43693489-a58d-457a-bf39-248caa3ff6ff/2020-09-17_172713.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TQ2H5XWG%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCx3UPx8ol6%2BSjnREH2mOLO95cnaRAK9wpRNGxK5CgvEQIhAKGnBGjSkpB7BL1ojKiw3NDoTCiweNgahqEjQd4OqOY6KogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igx1IZJVZLrx%2F832ajkq3ANSqM6%2F%2BP1F4a0ZnSs39pjUeMXeCuyGj5k9oX9%2B92lfWMCa23FjOa49yQjld2Tft0OXFp5kyj8fhyJ0o8w%2FRrZnMhNRZ61Y0W2YncGj45gFXG%2F5s8uT5cvE5WPRtQ%2Fy9G%2BUAA%2BNjY8T3xnjqvvaQeHZ5IZppT4QcaR258BZcRN%2BPwoXyvvQeD%2BlfLpVeIK60pU3jk7fsP4G2Zbfk85%2BfEE9RuXwSS181zSCTIDWVtGGIe%2F3PNW1x9r6WQu964mSBBzqNuJop0XJY8jUV8ye%2ByCUw0bPBpHLNmQMxbKtwUzazqEjVb3ezm6lyxZ5Oj8e7i2I2VG76v9HtRg%2BD0FyueSYThEHry5YPiAaSdEAj2sF5I9NzLlDQz5oIvsW2ohi7GXEVFzZeE7idzT4ruvoifaGt6EQZxc5C723SihdyoqKo2w34Mo62qdJJXCYy8KthpQcAer%2Fu8lRXEhhkBuxvSJqoDT4Ni3fGz74%2FgVocw8O3JqQFXyjISPHKupTlDWErIuaJs%2FMdSiX62wKAjDZfxwNdjg%2FzMG9erTGG%2BvoL%2FQlHYqgedkQXpslI%2BJJT8l%2FnV5D5JGDXUCix8%2BBFRkrWDyKPt%2B9K6SYYHrW%2BO%2BJz8DHPoIljee2dB9TDLUCJzDXuf%2FSBjqkAeWAy1wadipBmBzpyJwMfGTVG4GOspQXzOQLEkMvwf%2F55NdxfbhfFrp2UeR5%2BNhgQ0kMiCNpTJ%2F8%2Bl1b3B6BnlIiB%2F%2FpjIpz%2BOHYaJMKH6YiG5TyywIor28qdsvGbn6Z4DiLJwdkCCM2343PgICY%2BcfPSPMDwmQwQrzIAxXCdr%2B53l6RSp4ASIW6LXb9rtUn6UZAj7AWzqb3fqswcWgfOqqM71Qn&X-Amz-Signature=5539115e1cb692f83cca5b2416618e8b2152164e78551a7fcdcced0fbba76411&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



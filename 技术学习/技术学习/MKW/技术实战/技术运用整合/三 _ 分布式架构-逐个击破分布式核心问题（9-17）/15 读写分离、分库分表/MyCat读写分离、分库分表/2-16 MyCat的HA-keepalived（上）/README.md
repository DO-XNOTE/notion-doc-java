---
title: 2-16 MyCat的HA-keepalived（上）
---

# 2-16 MyCat的HA-keepalived（上）

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/dc97335c-d163-48ae-9d93-9a0985c1aeb8/SCR-20240807-rovm.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663IQYQSBH%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225414Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDlj3gz0GiD3%2BcMsdMZ%2FqO3bUaAxGwt9TX6S6sa5CbHJgIgdvHI8Z%2F5ataIlgTxUCc6j%2FMTB4siu7qJzUAXdapkTY4qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNhetsPvCPLAGs0rbCrcAypWo2qGL%2FkILpoK6od14OQsWno6RvZJgWuOZxDOBY6ivnm8JjpHYfsw%2F03%2BISxHUvGU6mMjNAqILzpqCKaj27BqF6qqqcP0L9HoGp3epc2xBwaYo%2B9GFh1Iy%2BGQ28eSi5omHYpYXBCn8KfSoXma1ePgr6QGbJkgZu7AXv0LLWj7RAuDydzY%2B%2Bl%2Bo1BQpRj36BZ6qBg3sHp6kID9tLJyMhJB0Nc55P8cWUh1%2FpLxBdllVmIJIvPLUbakP0%2BOL2C0GsIwqTNUG%2Fsa1j3ldSw%2BxIGU7nMASx%2FIpCbtEQ6fzFHTEE4qi3A2ilgxLznA%2BFbaqMV0qu7dGgpUuE5ynEM1lXHprSkENwZC0Ol6wZPkWOt6D27X4Ul0bQb3v4FGgi73ksNA4FW2zeuV87fs%2BNi9TV7zOxPQZ%2BOSowJYaY0IiHY8TyF3Iq8DMnnpijr%2BDKwSyXMSxMYrECzDyuQYdcb3PIWml4eR4V%2BkWE%2BjucozsQGXod7UEDKAAztiAw28wX%2FaKPRgIFUib2Dpdlwx%2BhoRAGIxM7qV9YVFMIdygbC1HgEMSYybtKpKc0v%2BoHvZPT1Tn20DIETwhBiZrQL4HinrlXRjq9TpoQEWC%2Fx353KgJ6p2%2BaAWcZyVwxIRfxrsMI64%2F9IGOqUBatgQ%2FBKqTA%2B6QUz%2Bm9MJlGpY0HvUWcVVDqfN4XzX2dl65lfm%2FnJKRvnF7E%2BYmmURVPYgONyYw7a7PJ%2Bdo3Va4DrN%2FoB2%2FZbiU8zv7blWxW3jkfS7LvFaPbj%2BkqGl6LlaeqwZIw%2BKBm%2F9nVdWKkuxuYNLBVMkxHiLoz3XWyol8ejKmfetVnT%2FIkzV3twjWM0%2FEiPoYrwddNHnK4fqPwVmAfD41Myw&X-Amz-Signature=c44a6a2e99d0c0dbdd7069d5ba43c7874528e9b3ff7a98d65a126a249b10077b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/bad1580d-e69d-41b9-8a3f-1649e6491068/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663IQYQSBH%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225414Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDlj3gz0GiD3%2BcMsdMZ%2FqO3bUaAxGwt9TX6S6sa5CbHJgIgdvHI8Z%2F5ataIlgTxUCc6j%2FMTB4siu7qJzUAXdapkTY4qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNhetsPvCPLAGs0rbCrcAypWo2qGL%2FkILpoK6od14OQsWno6RvZJgWuOZxDOBY6ivnm8JjpHYfsw%2F03%2BISxHUvGU6mMjNAqILzpqCKaj27BqF6qqqcP0L9HoGp3epc2xBwaYo%2B9GFh1Iy%2BGQ28eSi5omHYpYXBCn8KfSoXma1ePgr6QGbJkgZu7AXv0LLWj7RAuDydzY%2B%2Bl%2Bo1BQpRj36BZ6qBg3sHp6kID9tLJyMhJB0Nc55P8cWUh1%2FpLxBdllVmIJIvPLUbakP0%2BOL2C0GsIwqTNUG%2Fsa1j3ldSw%2BxIGU7nMASx%2FIpCbtEQ6fzFHTEE4qi3A2ilgxLznA%2BFbaqMV0qu7dGgpUuE5ynEM1lXHprSkENwZC0Ol6wZPkWOt6D27X4Ul0bQb3v4FGgi73ksNA4FW2zeuV87fs%2BNi9TV7zOxPQZ%2BOSowJYaY0IiHY8TyF3Iq8DMnnpijr%2BDKwSyXMSxMYrECzDyuQYdcb3PIWml4eR4V%2BkWE%2BjucozsQGXod7UEDKAAztiAw28wX%2FaKPRgIFUib2Dpdlwx%2BhoRAGIxM7qV9YVFMIdygbC1HgEMSYybtKpKc0v%2BoHvZPT1Tn20DIETwhBiZrQL4HinrlXRjq9TpoQEWC%2Fx353KgJ6p2%2BaAWcZyVwxIRfxrsMI64%2F9IGOqUBatgQ%2FBKqTA%2B6QUz%2Bm9MJlGpY0HvUWcVVDqfN4XzX2dl65lfm%2FnJKRvnF7E%2BYmmURVPYgONyYw7a7PJ%2Bdo3Va4DrN%2FoB2%2FZbiU8zv7blWxW3jkfS7LvFaPbj%2BkqGl6LlaeqwZIw%2BKBm%2F9nVdWKkuxuYNLBVMkxHiLoz3XWyol8ejKmfetVnT%2FIkzV3twjWM0%2FEiPoYrwddNHnK4fqPwVmAfD41Myw&X-Amz-Signature=1b3ef6841397ea99adbb0b83a615c37ce48c41785e2d8ea3c754349f756ac152&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[file](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/8990fb68-0fb7-4e54-aceb-7bfe86c353fa/198-keepalived.conf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663IQYQSBH%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225414Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDlj3gz0GiD3%2BcMsdMZ%2FqO3bUaAxGwt9TX6S6sa5CbHJgIgdvHI8Z%2F5ataIlgTxUCc6j%2FMTB4siu7qJzUAXdapkTY4qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNhetsPvCPLAGs0rbCrcAypWo2qGL%2FkILpoK6od14OQsWno6RvZJgWuOZxDOBY6ivnm8JjpHYfsw%2F03%2BISxHUvGU6mMjNAqILzpqCKaj27BqF6qqqcP0L9HoGp3epc2xBwaYo%2B9GFh1Iy%2BGQ28eSi5omHYpYXBCn8KfSoXma1ePgr6QGbJkgZu7AXv0LLWj7RAuDydzY%2B%2Bl%2Bo1BQpRj36BZ6qBg3sHp6kID9tLJyMhJB0Nc55P8cWUh1%2FpLxBdllVmIJIvPLUbakP0%2BOL2C0GsIwqTNUG%2Fsa1j3ldSw%2BxIGU7nMASx%2FIpCbtEQ6fzFHTEE4qi3A2ilgxLznA%2BFbaqMV0qu7dGgpUuE5ynEM1lXHprSkENwZC0Ol6wZPkWOt6D27X4Ul0bQb3v4FGgi73ksNA4FW2zeuV87fs%2BNi9TV7zOxPQZ%2BOSowJYaY0IiHY8TyF3Iq8DMnnpijr%2BDKwSyXMSxMYrECzDyuQYdcb3PIWml4eR4V%2BkWE%2BjucozsQGXod7UEDKAAztiAw28wX%2FaKPRgIFUib2Dpdlwx%2BhoRAGIxM7qV9YVFMIdygbC1HgEMSYybtKpKc0v%2BoHvZPT1Tn20DIETwhBiZrQL4HinrlXRjq9TpoQEWC%2Fx353KgJ6p2%2BaAWcZyVwxIRfxrsMI64%2F9IGOqUBatgQ%2FBKqTA%2B6QUz%2Bm9MJlGpY0HvUWcVVDqfN4XzX2dl65lfm%2FnJKRvnF7E%2BYmmURVPYgONyYw7a7PJ%2Bdo3Va4DrN%2FoB2%2FZbiU8zv7blWxW3jkfS7LvFaPbj%2BkqGl6LlaeqwZIw%2BKBm%2F9nVdWKkuxuYNLBVMkxHiLoz3XWyol8ejKmfetVnT%2FIkzV3twjWM0%2FEiPoYrwddNHnK4fqPwVmAfD41Myw&X-Amz-Signature=2fbe0798f94c9631eb104bab8216c0b9fc4cda84544a8f869eb32f7e02b24f34&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```java
! Configuration File for keepalived

global_defs {
   notification_email {
     acassen@firewall.loc
     failover@firewall.loc
     sysadmin@firewall.loc
   }
   notification_email_from Alexandre.Cassen@firewall.loc
   smtp_server 192.168.200.1
   smtp_connect_timeout 30
   router_id LVS_DEVEL
   vrrp_skip_check_adv_addr
   #vrrp_strict
   vrrp_garp_interval 0
   vrrp_gna_interval 0
}
#  检测haproxy 是否挂掉，如果挂掉就会虚拟ip切换到其他机器上
vrrp_script chk_haproxy {
    script "killall -0 haproxy"
    interval 2 #两秒执行一次检查 haproxy 是否还在线
}

vrrp_instance VI_1 {
    state BACKUP # 虚拟 ip 分配的 master上(199)  除非挂掉 才会分配到 BACKUP(slave) 上
    interface ens160 # 分配到的网卡上， 如果是大型的机器有多个网卡， 也可在这设置
    virtual_router_id 51
    priority 100
    advert_int 1
    authentication {
        auth_type PASS
        auth_pass 1111
    }
    virtual_ipaddress {  #分配虚拟ip 到真实的机器上，分配到的199上
        172.16.136.100
    }
    track_script {  # 检测haproxy 是否挂掉，如果挂掉就会虚拟ip切换到其他机器上
        chk_haproxy    
    }
}

virtual_server 172.16.136.100 6000 {  # 监听的端口  443改成了 6000
    delay_loop 6
    lb_algo rr
    lb_kind NAT
    persistence_timeout 50
    protocol TCP

    real_server 172.16.136.198 5000 { # Haproxy 的端口 5000 监听Haproxy是不是活着的
        weight 1
    }
}
```

[file](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e4995d75-5f7f-46ee-af64-b60a57f6860b/199-keepalived.conf?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663IQYQSBH%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225414Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDlj3gz0GiD3%2BcMsdMZ%2FqO3bUaAxGwt9TX6S6sa5CbHJgIgdvHI8Z%2F5ataIlgTxUCc6j%2FMTB4siu7qJzUAXdapkTY4qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNhetsPvCPLAGs0rbCrcAypWo2qGL%2FkILpoK6od14OQsWno6RvZJgWuOZxDOBY6ivnm8JjpHYfsw%2F03%2BISxHUvGU6mMjNAqILzpqCKaj27BqF6qqqcP0L9HoGp3epc2xBwaYo%2B9GFh1Iy%2BGQ28eSi5omHYpYXBCn8KfSoXma1ePgr6QGbJkgZu7AXv0LLWj7RAuDydzY%2B%2Bl%2Bo1BQpRj36BZ6qBg3sHp6kID9tLJyMhJB0Nc55P8cWUh1%2FpLxBdllVmIJIvPLUbakP0%2BOL2C0GsIwqTNUG%2Fsa1j3ldSw%2BxIGU7nMASx%2FIpCbtEQ6fzFHTEE4qi3A2ilgxLznA%2BFbaqMV0qu7dGgpUuE5ynEM1lXHprSkENwZC0Ol6wZPkWOt6D27X4Ul0bQb3v4FGgi73ksNA4FW2zeuV87fs%2BNi9TV7zOxPQZ%2BOSowJYaY0IiHY8TyF3Iq8DMnnpijr%2BDKwSyXMSxMYrECzDyuQYdcb3PIWml4eR4V%2BkWE%2BjucozsQGXod7UEDKAAztiAw28wX%2FaKPRgIFUib2Dpdlwx%2BhoRAGIxM7qV9YVFMIdygbC1HgEMSYybtKpKc0v%2BoHvZPT1Tn20DIETwhBiZrQL4HinrlXRjq9TpoQEWC%2Fx353KgJ6p2%2BaAWcZyVwxIRfxrsMI64%2F9IGOqUBatgQ%2FBKqTA%2B6QUz%2Bm9MJlGpY0HvUWcVVDqfN4XzX2dl65lfm%2FnJKRvnF7E%2BYmmURVPYgONyYw7a7PJ%2Bdo3Va4DrN%2FoB2%2FZbiU8zv7blWxW3jkfS7LvFaPbj%2BkqGl6LlaeqwZIw%2BKBm%2F9nVdWKkuxuYNLBVMkxHiLoz3XWyol8ejKmfetVnT%2FIkzV3twjWM0%2FEiPoYrwddNHnK4fqPwVmAfD41Myw&X-Amz-Signature=df93323acada97a33da3325e74a9995cb711a660c4044e883fa5d2e1e1175b5b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```java
! Configuration File for keepalived

global_defs {
   notification_email {
     acassen@firewall.loc
     failover@firewall.loc
     sysadmin@firewall.loc
   }
   notification_email_from Alexandre.Cassen@firewall.loc
   smtp_server 192.168.200.1
   smtp_connect_timeout 30
   router_id LVS_DEVEL
   vrrp_skip_check_adv_addr
   # vrrp_strict 这个一定要注释点 不然会影响大使用虚拟IP
   vrrp_garp_interval 0
   vrrp_gna_interval 0
}
 # 检测haproxy 是否挂掉，如果挂掉就会虚拟ip切换到其他机器上
vrrp_script chk_haproxy {
    script "killall -0 haproxy"
    interval 2 # 两秒钟检测一次
}

vrrp_instance VI_1 {
    state MASTER  # 一定用配置多台 这台是master 会得到虚拟ip, 除非master挂掉， 虚拟ip才会分配到 BACKUP（199.198主从） 机器上
    interface ens160 # 网卡(当前机器 ip addr查看)===虚拟 ip会分配上到这上面， 一些大型机器上又多块网卡， 会分配到多个网卡上， 在这里设置
    virtual_router_id 51 # 虚拟的路由，多台机器的话要配置成一样的， 这里就两台，都是一样的
    priority 100
    advert_int 1
    authentication {
        auth_type PASS
        auth_pass 1111
    }
    virtual_ipaddress { # 虚拟的 ip 地址==== 虚拟的 ip 和当前的机器一定要在 同一个网段内
        172.16.136.100
        #192.168.200.17
        #192.168.200.18
    }
    track_script {
        chk_haproxy    # 检测haproxy 是否挂掉，如果挂掉就会虚拟ip切换到其他机器上
    }
}

# 后台ip对应的真实的虚拟机 virtual_server, 就是上面的 （172.16.136.100 设置成本机）virtual_ipaddress，  443改成6000吧 表示的监听端口
virtual_server 172.16.136.100 6000 {   
    delay_loop 6
    lb_algo rr
    lb_kind NAT
    persistence_timeout 50
    protocol TCP

    real_server 172.16.136.199 5000 {  # haproxy的端口5000 haproxy部署在一起 监听Haproy 是不是活着的
        weight 1
        # 这个检测 haproxy是否还活着不管用 所以使用  chk_haproxy
        #TCP_CHECK {  # 心跳 检测haproxy 是否是活着的
        #    connect_port 5000 
        #    connect_timeout 10000 # 10秒 
       # } 
    }
}
```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/ea6f1209-40e3-4f3c-a624-c05a046fd12d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4663IQYQSBH%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225414Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDlj3gz0GiD3%2BcMsdMZ%2FqO3bUaAxGwt9TX6S6sa5CbHJgIgdvHI8Z%2F5ataIlgTxUCc6j%2FMTB4siu7qJzUAXdapkTY4qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDNhetsPvCPLAGs0rbCrcAypWo2qGL%2FkILpoK6od14OQsWno6RvZJgWuOZxDOBY6ivnm8JjpHYfsw%2F03%2BISxHUvGU6mMjNAqILzpqCKaj27BqF6qqqcP0L9HoGp3epc2xBwaYo%2B9GFh1Iy%2BGQ28eSi5omHYpYXBCn8KfSoXma1ePgr6QGbJkgZu7AXv0LLWj7RAuDydzY%2B%2Bl%2Bo1BQpRj36BZ6qBg3sHp6kID9tLJyMhJB0Nc55P8cWUh1%2FpLxBdllVmIJIvPLUbakP0%2BOL2C0GsIwqTNUG%2Fsa1j3ldSw%2BxIGU7nMASx%2FIpCbtEQ6fzFHTEE4qi3A2ilgxLznA%2BFbaqMV0qu7dGgpUuE5ynEM1lXHprSkENwZC0Ol6wZPkWOt6D27X4Ul0bQb3v4FGgi73ksNA4FW2zeuV87fs%2BNi9TV7zOxPQZ%2BOSowJYaY0IiHY8TyF3Iq8DMnnpijr%2BDKwSyXMSxMYrECzDyuQYdcb3PIWml4eR4V%2BkWE%2BjucozsQGXod7UEDKAAztiAw28wX%2FaKPRgIFUib2Dpdlwx%2BhoRAGIxM7qV9YVFMIdygbC1HgEMSYybtKpKc0v%2BoHvZPT1Tn20DIETwhBiZrQL4HinrlXRjq9TpoQEWC%2Fx353KgJ6p2%2BaAWcZyVwxIRfxrsMI64%2F9IGOqUBatgQ%2FBKqTA%2B6QUz%2Bm9MJlGpY0HvUWcVVDqfN4XzX2dl65lfm%2FnJKRvnF7E%2BYmmURVPYgONyYw7a7PJ%2Bdo3Va4DrN%2FoB2%2FZbiU8zv7blWxW3jkfS7LvFaPbj%2BkqGl6LlaeqwZIw%2BKBm%2F9nVdWKkuxuYNLBVMkxHiLoz3XWyol8ejKmfetVnT%2FIkzV3twjWM0%2FEiPoYrwddNHnK4fqPwVmAfD41Myw&X-Amz-Signature=191eb1c6137d984a140e11a1e3ea5f314c05c7afc2913c8ce832f395df33d780&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

上一节当中，咱们已经搭建了一个 HA proxy 是吧，通过 HA proxy 进行负载均衡，负载到后边的两个 my cat 上。也就是说在这张图当中，咱们完成了这三个点，一个 HA proxy 和两个 my cat 完成了这三个点的这么一个搭建。


那么现在这三个点的这个结构，my cat 做了高可用对吧？做了 HA 但是 HA proxy 又成为了系统当中的单点，如果你的 HA proxy 挂了，那你的整个服务也是不可用的了。所以现在咱们就要搭这个整套图的这个结构。除了 HA proxy 咱们还要再安装 people live 的，通过这一组两个 HA broxy 和两个 people live 的创建出一个虚拟的 IP 然后前端的应用连接这个虚拟的 IP 保证一个 HA proxy 的这么一个高可用。


现在咱们还要再搭建一个 HA proxy 咱们之前已经搭建了一个节点的 HA proxy 现在咱们搭建另外一个就另外一个咱们安装在哪台机器上？咱们先看一下雷威cat ，咱们给它安装在 130 上，咱们进入到 130 这台机器，然后安装 HA proxy 先用压膜搜索一下 HA proxy 对吧？好找到了 HA proxy 是吧，咱们给它复制一下，再使用亚米 store 杠 Y 粘贴一下。现在开始安装是吧，安装的过程有点慢。


好，现在已经开始下载了是吧，下载完以后咱们要修改它的配置文件对吧，配置文件的位置在 etcha proxy 在这下面叫一个 HA proxy 点儿 config 这个咱们首先要改一下它的 mode 这支 TTP 要给它改成 TCP 之前咱们在启动 HA proxy 的时候打印出了一些警告是吧，咱们把这些警告尝试的改一下，因为咱们这个模式给它改成了 TCP 然后后边这些 option 咱们也同样要改一下，这个应该改成 TCP 烙，然后这个 option 把一支洗衣器 server close 这个咱们就给它注释掉。


还有一个这个 forward for 这个应该也是针对 HTTP 协议的给它注释掉。接着往下前面的这三行都是针对 HTTP 协议的，咱们也给它注掉。这个现在只有一个 default back 了是吧，前面这个星号是 IP 后边是端口5000，这个咱们也不用动连接过来，5000的端口它都走 App 这个back ，然后就是后边 App 这个 back 咱们要配置一下，后两行给它注释掉。然后 IP 19 二点幺六，8.7，三点幺三零，后边跟的是8066。然后第二个 my cat 幺九二点幺六八点七三点幺三幺也是 8 零六6。


好，这个 HA proxy 的这个配置配置完了，咱们给它保存一下，然后启动一下 HA proxy 杠 F 指定你的配置文件，然后回车可以看看。刚才咱们在 132 那台机器操作的时候，那些警告这里边已经没有了，然后咱们再查看一下进程。好吧，进程在是吧，看来 HA proxy 已经启动成功了。然后咱们再通过那位 cat 给他连接一下，咱们直接用这个 aj proxy 。复制一个连接名字改一下，看到是 130 这台机器的 IP 改成 130 端口 5000 用户名密码不用变，咱们测试一下没有问题对吧。双击一下，进入到这个 user 数据库，看一下 order 这个表的数据没有问题了是吧，数据都能够正常的查询出来。


好，现在咱们 HA proxy 也已经有了两台，然后咱们要通过 people live 的给 HA prophecy 做一个高可用。这个咱们再看一下这个图， keep alive 的和这个 HA proxy 要在同一台机器上，咱们先安装一下130。在这个 130 这台机器上先安装一个 keep alive 的，咱们还是进入到 130 这台机器，然后安装 people love 的 people 怎么安装？咱们还是通过 YAML 咱们搜索一下 keep alive 的。好搜索到了是吧，咱们搜索到了一个 keep alive 的，看一下它的后边的注释。
Load balancer and availability service.


一个负载均衡和高可用的这么一个服务。咱们也是给它安装一下压膜 install 杠 Y 然后把这个名称给它复制一下，粘贴回车。安装好已经开始下载安装了是吧。然后咱们要进入到 people love 的配置文件进行配置。那么 people love 的配置文件在什么位置？他也是在 etc 下边 etc people live 的。然后在 keep alive 大家 CONF 咱们查看一下，它有一个交换文件是吧，咱们直接给它删除掉看一下。这个就是 keep alive 的配置文件。同样它也有一个 global defense 一个全局的定义。


这里边主要是配置一下，大家看一个，通知的邮件，然后邮件的服务器还有后边 vrrpvrrp 就是它的这个虚拟 IP 这块咱们特殊的要注意一下，就是这个 strict 这一行咱们要给它注释掉这一行一定要给它注释掉，它会影响到咱们使用虚 IP 这个一定要先注释掉。后边就是它的一些配置了。可以看到后边有好几段配置是吧，这些配置其实咱们只留两段就可以了只留哪两段呢？一个是 vrrp 它是虚 IP 的配置，这个一会咱们再给大家讲解。然后后边对应的 V 车 server 它是你这个需 IP 对应的后台的真实的物理机是吧，这个就是 real server 然后后边这个微车 server 咱们就都不要咱们给它删一下。好到这里这一段咱们都删完了，下面给大家。


讲解一下这个 keep alive 的这两段它到底都是什么意思。前面的这一段是你要配置一个虚 IP 虚 IP 里边是什么 state 它的状态，这个虚 IP 一定要配置多台机器，还要大于等于两台。其中一台是 master 就是你启动以后，你的这个虚 IP 把所有的请求都会分配到 master 所在的这个机器上。然后另外一台这个 state 一定要配成 slave 它是不会得到你的需 IP 的。除非你的这个主 master 这台机器挂了，这个时候这个需 IP 才会分配到你的从上面，也就是这个 slave 这台机器上就是这个 state 这个状态的意思。


然后 interface 后边接的是什么？接的是网卡，也就是说你的这个需 IP 分配到你的这台机器上的哪一块网卡上。咱们普通的情况下，一台机器只有一块网卡，但是有的像一些大型的网络当中，它都是有多块网卡的。有多块网卡的情况下，你的这个需 IP 它分配到哪一块网卡上，这个就是在这个 interface 里边去进行配置。然后后边这个虚拟路由的 ID 两台机器要配置成一样的，这里面是51，咱们就不用改了，然后后边优先级 100 这些都不用动。


然后就看最后的这一个配置虚拟的 IP 地址是吧，咱们再看一下这个图，这个虚拟的 IP 地址咱们配成什么，它主要是配你的虚拟的 IP 小配这个需 IP 咱们再回到 130 擂台机器上，这个需 IP 一定要和当前那个机器处在同一个网段内。当前咱们这台机器幺九二点幺九八点七三点幺三零是吧，咱们一定要配置在这个网段内。所以这个需 IP 咱们给他写一下幺九二点幺九八点七三点写一个199。也就是说这台机器咱们要有一个虚拟的 IP 产生，就是七三点幺九九，然后就是后边的这个配置了虚拟的服务。虚拟的服务是谁？就是后边的这个七三点幺九九，咱们把这一段也给它改一下，后边跟的是监听的端口，这个端口咱们也随便写一个。之前 HA proxy 咱们写的是5000，对吧，这块咱们写个6000，先听 6000 这个端口，然后它对应的后台的真实的这个 IP 地址。这块咱们就要写本机了。因为什么？再看一下这个图，一个 keep alive 的，它只对应了一个 HA proxy 是通过这个虚 IP 过来的，请求只会分配到当前的这个 HA proxy 它并没有这条线，并没有斜着这条线。如果有这条线的话，那是不是你的这个 people love 的就将这个请求分配到两个 HA proxy 了。


但是这个图当中，只给它分配到本机的这个 HA proxy 这块，咱们再回来配置一下它的真实的服务器 IP 是幺九二点幺六八七三点幺三零，也就是本机是吧。然后后边端口 HA proxy 的端口是吧5000。咱们要记住。然后后边的这一段就是他的心跳的监测，他监测你的 HA PRO 和 Z 是否是活着的。


但是这个是 SSL 改的，但是咱们用的是 TCP 的请求， TCP 的请求咱们这块怎么去配置呢？这块咱们还是上 keep a live 的官网去查询一下。咱们打开浏览器。好，咱们进入到了 people live 的这个官方的文档，然后咱们找到 keep alive 的 configuration keep alive 的配置。然后这里边有非常详细的说明。


第一段是 global global 的这些定义，然后是微车 service 虚拟服务的这个定义，咱们刚才就是要找这一段的配置是吧。虚拟服务咱们配置了 IP 和端口，然后后边配置了真实的这个服务是吧，真实的这个主机的 IP 和端口，然后里边有一个检查是吧检查咱们刚才使用的是 SSL get 针对这个 HT PS 这个协议使用到这个检查。那么如果咱们使用的是 HA proxy 咱们要检查 HA proxy 是否正确，咱们要用 TCP check 也就是这一段。


这一段配置里边描述了它的连接的端口，还有超时的时间。咱们把这一段给它复制一下，然后粘贴到 real server 里边来。这一段咱们就都给它删掉，给它粘贴一下。 tcd check 是端口，检查哪个端口检查 5000 对吧，因为 HA proxy 的端口是5000，超时的时间咱们，设置成 10 秒。那么这一段配置就配置完了。


还有一个咱们要查看一下当前的网卡，它这个 interface 写的是 ETH 0，咱们这段配置先保存一下，看一下当前的这个网卡叫什么名字。咱们用 IP address 当前的网卡叫 ENS 33，这里边有一个七三点幺三零，所以这个 interface 咱们要改成这个名字，咱们复制一下。然后再看一下 people love 的，把这个 interface 给他改一下，叫做 ENS 33。好，这个配置就配置完了，咱们给它保存一下。 130 这台机器的 keep a live 的就已经安装好了，也已经配置完成了。然后咱们在这个 132 上面也要装一个 people live 的亚默 install 杠 Y people 和 love 的。好，非常快，已经安装完成了。然后咱们进入到 etc people live 的目录看看。这里边这两个配置文件，咱们先给它删除掉。然后 SCP 咱们直接把 130 这台机器的 people live 的这个配置文件给它复制过来。 SCP root 艾特幺九二点幺六八点七三点幺三零 etc 提破 live 的。然后 people love 的 config 是吧，给大家复制到当前的这个目录。 yes 输入 130 这台机器的密码。


好，已经复制过来了是吧，咱们来看一下没有问题是吧，咱们从头再改一遍。首先要改的就是这个 state state 这里边咱们要给它改成 slave 它是从然后后边的网卡包括它的路由的 ID 这些都不用动，虚拟 IP 也不用动。然后就是后边的这个真实的 server 这个咱们要给它改成 132 是吧，然后端口还是5000，后边也都不用动了，咱们给它保存一下。


下面咱们要启动这个 keep alive 的，咱们先启动 130 这台机器，先检查一下 people love 的是不是有这个进程，没有这个进程是吧。然后咱们直接启动这个服务， people love 的他也是杠 F etc people love 的，然后 people love 的点 com 再查看一下进程已经起来了是吧。然后咱们再启动132，这台机器也是 keep alive 的杠 FE TC keep alive 的 keep life.top 再查看一下他的进程，没有问题，都启动起来了是吧。然后咱们查看一下 130 这台机器的 IP IP 咱们清空一下。 IP dress 可以看到 ES 33 它现在有两个 IP 了，一个是七三点幺三零，一个是七三点幺九九。然后咱们再看132，看看 132 它有几个 IP IP address 这里边 ENS 33 是吧，它还是只有一个 IP 七三点幺三二。


好，这个 keep alive 咱们也已经配置完了。下面咱们进入到 navicate 连接一下，这个连接咱们就是连接到 199 这个 VIP 上了。幺九二点幺六八点七三点幺九九给他备注一下。这个是 keep alive 的 IP 也是 199 端口，咱们刚才配置的端口是 6000 是吧。然后用户名密码，这个咱们要写你的 my cat 的用户名密码 root 然后密码 123456 咱们连接测试一下没有问题是吧，确定。咱们再双击一下查看一下， O 的这个表数据也都已经查询出来了。


然后咱们现在模拟一下，如果咱们 130 这台机器目前是绑定了你的这个虚 IP 是吧。 1199 如果 130 这台机器的提破 live 的挂了会出现什么情况？咱们先查看一下媳妇 live 的进程，有这三个进程是吧，然后咱们把这三个进程给它杀掉。 Q 七九零五，七九零六还有一个 7907 是吧，飞车在长安继承没有了是吧。也就是说 130 这台机器的 keep live 的已经挂掉了，咱们现在再查看一下 IP address 可以看到这个 ENS 33 现在没有这个 1999 的 IP 了，现在咱们再查看一下 132 里边咱们再执行一下 IP address 可以看到 199 这个 IP 已经绑定到了 132 这台机器。然后咱们前面再去查询一下这两条数据，没有问题是吧。好现在咱们再把这个 130 的 keep alive 给它提起来，杠 F 和 etckeep alive 的启动起来以后，这个需 IP 看看它变不变还是没有变。现在就是一直固定到了这个 132 的这台机械。


那么现在咱们来看一下这个图提破 love 的有挂的情况，咱们也已经演示了是吧。现在咱们要演示如果说你的 HA proxy 挂了，它会不会自动的切换。目前现在 199 这个需 IP 绑定的是 132 这台机器。如果我把 132 这台机器的 h1 proxy 给它停掉，那么它的这个 VIP 会不会切换到 130 这台机器？咱们试一下还是进入到 132 这台机器。现在我把 HA proxy 给它关掉，先查看一下 HA proxy 的进程，然后给他杀掉 7446 是吧。好，这个进程没有了是吧，然后看一下 IP address 看来 HA proxy 如果挂掉的话，它的这个虚 IP 并没有切换，咱们的这个配置可能还是存在的一些问题，咱们在下一节课的内容当中，再把这个问题给大家解决掉。





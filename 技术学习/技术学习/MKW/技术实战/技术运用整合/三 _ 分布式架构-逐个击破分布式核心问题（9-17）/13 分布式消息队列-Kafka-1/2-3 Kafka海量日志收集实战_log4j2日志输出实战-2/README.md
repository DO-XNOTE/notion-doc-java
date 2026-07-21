---
title: 2-3 Kafka海量日志收集实战_log4j2日志输出实战-2
---

# 2-3 Kafka海量日志收集实战_log4j2日志输出实战-2

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/7f26c28c-b100-4601-a1d9-2753fcd7da43/SCR-20240807-gtjc.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RSOENA7V%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCHnc4euZQJi4o1J9sUN1rEcMUJ9OgZu15%2BCsTJptQ7ZQIhAKt7%2BQhhGoro30KSjtag%2Ft5TRcZxYz2iwd5m5uWUIpsqKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw9ohKW97ts5UeUhFwq3AMOUJM4gffgkxHuNLEOlsVuK4Y1KrpY2MlxfqFgVB5i9vzN9j6IfIUhgfyqAydYvZuQkXuSpOdEiw9XWXYRHe0W%2FUcycBPST8Dm7fMLEy09T5tiX%2FIY3Cw0tfbBfn6eoy2pPZ4jTOWOXg7FT4UOK3vK7Q75ue6E8aYcLiyTtk2ztqf5NWc75DEMh0r0aSXF%2FCKiRxZwrhCa%2Bp19tY8eXeo75wU2xuCjubz3XrecStXc6xs36KYEPmiScZVuYaJz8Y0jyPCvc1sg4yh0VaMvP1Heynx%2F2GuOmIutssgRFUuRWOL3dcYn456Rdosb6HjIzU1Ddl2tRLPBEJW1kwNLow216mTpt7Ry5wZnmINTCh7Ny6ThU%2FNb53wcu6t%2FczMRoBG8%2FverdTPMO5VXEEP47CvA57w915wl5%2BlOTBFuwoVxDmBrdqW2OoKR3qAoqJw4mB%2Bq477H0mwpCst%2BeNlwnl3AVlfqH5lGxkEawp7o%2Fi2Vh2kRevhILAupJLiudb3MtO3iKkMVLx29GOV6IP4MsQt5GUDZImsUlGroFWnUS7HjGRylsvNCGZBVRqJI7UoLRiORImzg%2FTp7Xs9OhBVG9ev0pBpxfd23WazKNyVCzo3JYmvq2wFXJf%2BZ%2FxXGjTCRuP%2FSBjqkAfeR%2FH0S%2BaKpBw24OTnGsI6RQf90KSnogwPaoGCjwQuhmjFGWSjQRF27rrFzKkOWoTrRID1sBJfNahAyLU1OUtjgWkexqnDlSTx03ZOO7GYywKYKJwpRja55RvO3Y0T%2FFMKmW%2BKCaFokNoEyjc023mcMrkcVXOc76Wktt5kE6ZS0ncbJQdf0VpM8Snt6pL5fdYBH7jbK3yF8BPSjvJUGly1l8CeJ&X-Amz-Signature=d76a0314eca28029c191760a88226bb7a6a5508642448db8ea3d3af8eadf9800&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/2d86933f-9c58-4f4c-82a5-786347bf64ea/SCR-20240807-grri.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RSOENA7V%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCHnc4euZQJi4o1J9sUN1rEcMUJ9OgZu15%2BCsTJptQ7ZQIhAKt7%2BQhhGoro30KSjtag%2Ft5TRcZxYz2iwd5m5uWUIpsqKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw9ohKW97ts5UeUhFwq3AMOUJM4gffgkxHuNLEOlsVuK4Y1KrpY2MlxfqFgVB5i9vzN9j6IfIUhgfyqAydYvZuQkXuSpOdEiw9XWXYRHe0W%2FUcycBPST8Dm7fMLEy09T5tiX%2FIY3Cw0tfbBfn6eoy2pPZ4jTOWOXg7FT4UOK3vK7Q75ue6E8aYcLiyTtk2ztqf5NWc75DEMh0r0aSXF%2FCKiRxZwrhCa%2Bp19tY8eXeo75wU2xuCjubz3XrecStXc6xs36KYEPmiScZVuYaJz8Y0jyPCvc1sg4yh0VaMvP1Heynx%2F2GuOmIutssgRFUuRWOL3dcYn456Rdosb6HjIzU1Ddl2tRLPBEJW1kwNLow216mTpt7Ry5wZnmINTCh7Ny6ThU%2FNb53wcu6t%2FczMRoBG8%2FverdTPMO5VXEEP47CvA57w915wl5%2BlOTBFuwoVxDmBrdqW2OoKR3qAoqJw4mB%2Bq477H0mwpCst%2BeNlwnl3AVlfqH5lGxkEawp7o%2Fi2Vh2kRevhILAupJLiudb3MtO3iKkMVLx29GOV6IP4MsQt5GUDZImsUlGroFWnUS7HjGRylsvNCGZBVRqJI7UoLRiORImzg%2FTp7Xs9OhBVG9ev0pBpxfd23WazKNyVCzo3JYmvq2wFXJf%2BZ%2FxXGjTCRuP%2FSBjqkAfeR%2FH0S%2BaKpBw24OTnGsI6RQf90KSnogwPaoGCjwQuhmjFGWSjQRF27rrFzKkOWoTrRID1sBJfNahAyLU1OUtjgWkexqnDlSTx03ZOO7GYywKYKJwpRja55RvO3Y0T%2FFMKmW%2BKCaFokNoEyjc023mcMrkcVXOc76Wktt5kE6ZS0ncbJQdf0VpM8Snt6pL5fdYBH7jbK3yF8BPSjvJUGly1l8CeJ&X-Amz-Signature=131dd5edf524a371fe9cd2af4ebee74a1aeaf84bf5df8dbb8d260e80b7000696&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/affd56e5-979b-4439-859e-c71c06532818/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RSOENA7V%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCHnc4euZQJi4o1J9sUN1rEcMUJ9OgZu15%2BCsTJptQ7ZQIhAKt7%2BQhhGoro30KSjtag%2Ft5TRcZxYz2iwd5m5uWUIpsqKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw9ohKW97ts5UeUhFwq3AMOUJM4gffgkxHuNLEOlsVuK4Y1KrpY2MlxfqFgVB5i9vzN9j6IfIUhgfyqAydYvZuQkXuSpOdEiw9XWXYRHe0W%2FUcycBPST8Dm7fMLEy09T5tiX%2FIY3Cw0tfbBfn6eoy2pPZ4jTOWOXg7FT4UOK3vK7Q75ue6E8aYcLiyTtk2ztqf5NWc75DEMh0r0aSXF%2FCKiRxZwrhCa%2Bp19tY8eXeo75wU2xuCjubz3XrecStXc6xs36KYEPmiScZVuYaJz8Y0jyPCvc1sg4yh0VaMvP1Heynx%2F2GuOmIutssgRFUuRWOL3dcYn456Rdosb6HjIzU1Ddl2tRLPBEJW1kwNLow216mTpt7Ry5wZnmINTCh7Ny6ThU%2FNb53wcu6t%2FczMRoBG8%2FverdTPMO5VXEEP47CvA57w915wl5%2BlOTBFuwoVxDmBrdqW2OoKR3qAoqJw4mB%2Bq477H0mwpCst%2BeNlwnl3AVlfqH5lGxkEawp7o%2Fi2Vh2kRevhILAupJLiudb3MtO3iKkMVLx29GOV6IP4MsQt5GUDZImsUlGroFWnUS7HjGRylsvNCGZBVRqJI7UoLRiORImzg%2FTp7Xs9OhBVG9ev0pBpxfd23WazKNyVCzo3JYmvq2wFXJf%2BZ%2FxXGjTCRuP%2FSBjqkAfeR%2FH0S%2BaKpBw24OTnGsI6RQf90KSnogwPaoGCjwQuhmjFGWSjQRF27rrFzKkOWoTrRID1sBJfNahAyLU1OUtjgWkexqnDlSTx03ZOO7GYywKYKJwpRja55RvO3Y0T%2FFMKmW%2BKCaFokNoEyjc023mcMrkcVXOc76Wktt5kE6ZS0ncbJQdf0VpM8Snt6pL5fdYBH7jbK3yF8BPSjvJUGly1l8CeJ&X-Amz-Signature=7217f16078425b61362de7247c419b4ea416dd87dda0123e17b1617bf7e809fa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

我们看一下同学们，请看这里边有好多你应该选哪个？ log for G two 就是二点 X 我们点进去，这是它底层的代码了，是不是因为它底层代码就是 a single loggera single logger 它底层是使用了 decision 做的，我说的就是这个就是 disruptor 叫做 a single logo disruptor 那它其实实际上就是对 disruptor 又做了一层封装。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/ff161bbe-78be-4394-bb17-f9a9ac0c0ee7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RSOENA7V%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCHnc4euZQJi4o1J9sUN1rEcMUJ9OgZu15%2BCsTJptQ7ZQIhAKt7%2BQhhGoro30KSjtag%2Ft5TRcZxYz2iwd5m5uWUIpsqKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw9ohKW97ts5UeUhFwq3AMOUJM4gffgkxHuNLEOlsVuK4Y1KrpY2MlxfqFgVB5i9vzN9j6IfIUhgfyqAydYvZuQkXuSpOdEiw9XWXYRHe0W%2FUcycBPST8Dm7fMLEy09T5tiX%2FIY3Cw0tfbBfn6eoy2pPZ4jTOWOXg7FT4UOK3vK7Q75ue6E8aYcLiyTtk2ztqf5NWc75DEMh0r0aSXF%2FCKiRxZwrhCa%2Bp19tY8eXeo75wU2xuCjubz3XrecStXc6xs36KYEPmiScZVuYaJz8Y0jyPCvc1sg4yh0VaMvP1Heynx%2F2GuOmIutssgRFUuRWOL3dcYn456Rdosb6HjIzU1Ddl2tRLPBEJW1kwNLow216mTpt7Ry5wZnmINTCh7Ny6ThU%2FNb53wcu6t%2FczMRoBG8%2FverdTPMO5VXEEP47CvA57w915wl5%2BlOTBFuwoVxDmBrdqW2OoKR3qAoqJw4mB%2Bq477H0mwpCst%2BeNlwnl3AVlfqH5lGxkEawp7o%2Fi2Vh2kRevhILAupJLiudb3MtO3iKkMVLx29GOV6IP4MsQt5GUDZImsUlGroFWnUS7HjGRylsvNCGZBVRqJI7UoLRiORImzg%2FTp7Xs9OhBVG9ev0pBpxfd23WazKNyVCzo3JYmvq2wFXJf%2BZ%2FxXGjTCRuP%2FSBjqkAfeR%2FH0S%2BaKpBw24OTnGsI6RQf90KSnogwPaoGCjwQuhmjFGWSjQRF27rrFzKkOWoTrRID1sBJfNahAyLU1OUtjgWkexqnDlSTx03ZOO7GYywKYKJwpRja55RvO3Y0T%2FFMKmW%2BKCaFokNoEyjc023mcMrkcVXOc76Wktt5kE6ZS0ncbJQdf0VpM8Snt6pL5fdYBH7jbK3yF8BPSjvJUGly1l8CeJ&X-Amz-Signature=d81de1eac6f5625ed645849860838d2e01c63ae88545f2d0ed518da763d11c1f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/26a342c5-a65c-4340-8383-de6fb83906b2/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RSOENA7V%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCHnc4euZQJi4o1J9sUN1rEcMUJ9OgZu15%2BCsTJptQ7ZQIhAKt7%2BQhhGoro30KSjtag%2Ft5TRcZxYz2iwd5m5uWUIpsqKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw9ohKW97ts5UeUhFwq3AMOUJM4gffgkxHuNLEOlsVuK4Y1KrpY2MlxfqFgVB5i9vzN9j6IfIUhgfyqAydYvZuQkXuSpOdEiw9XWXYRHe0W%2FUcycBPST8Dm7fMLEy09T5tiX%2FIY3Cw0tfbBfn6eoy2pPZ4jTOWOXg7FT4UOK3vK7Q75ue6E8aYcLiyTtk2ztqf5NWc75DEMh0r0aSXF%2FCKiRxZwrhCa%2Bp19tY8eXeo75wU2xuCjubz3XrecStXc6xs36KYEPmiScZVuYaJz8Y0jyPCvc1sg4yh0VaMvP1Heynx%2F2GuOmIutssgRFUuRWOL3dcYn456Rdosb6HjIzU1Ddl2tRLPBEJW1kwNLow216mTpt7Ry5wZnmINTCh7Ny6ThU%2FNb53wcu6t%2FczMRoBG8%2FverdTPMO5VXEEP47CvA57w915wl5%2BlOTBFuwoVxDmBrdqW2OoKR3qAoqJw4mB%2Bq477H0mwpCst%2BeNlwnl3AVlfqH5lGxkEawp7o%2Fi2Vh2kRevhILAupJLiudb3MtO3iKkMVLx29GOV6IP4MsQt5GUDZImsUlGroFWnUS7HjGRylsvNCGZBVRqJI7UoLRiORImzg%2FTp7Xs9OhBVG9ev0pBpxfd23WazKNyVCzo3JYmvq2wFXJf%2BZ%2FxXGjTCRuP%2FSBjqkAfeR%2FH0S%2BaKpBw24OTnGsI6RQf90KSnogwPaoGCjwQuhmjFGWSjQRF27rrFzKkOWoTrRID1sBJfNahAyLU1OUtjgWkexqnDlSTx03ZOO7GYywKYKJwpRja55RvO3Y0T%2FFMKmW%2BKCaFokNoEyjc023mcMrkcVXOc76Wktt5kE6ZS0ncbJQdf0VpM8Snt6pL5fdYBH7jbK3yF8BPSjvJUGly1l8CeJ&X-Amz-Signature=9509ac22d601a377daafe7c1c525b212f3e4964cbef76e301ddc8664bc8e3e1c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


然后我们看一下这个迪斯拉特。其实我们点进去，大家可以看一看这里边一些比较核心的代码有什么？就是这个迪斯拉看第三个是 L max 它是一个高性能非阻塞的这么一个组件。那有兴趣的同学可以还是在这里打多说一嘴。老师在这个慕课网上已经出了这个关于 disarps 的一个时代课程。好了，在这里我就不领着小伙伴们去看这个具体的代码了。也就是说大家知道，这个 log for G two 确实是依赖了 disruptor 的。Ok.然后我在这里怎么去配呢？就你只需要说把它进行包裹一层就好了。就是声明说这个下面的所有的文件都帮我去输出。然后他引用这个 append 相当于这个 append 不是直接输出，而是又包了一层 a single logger 之后再去输出。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/d28954e8-e9c3-42f4-b72e-e1eeaacd9ccd/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RSOENA7V%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCHnc4euZQJi4o1J9sUN1rEcMUJ9OgZu15%2BCsTJptQ7ZQIhAKt7%2BQhhGoro30KSjtag%2Ft5TRcZxYz2iwd5m5uWUIpsqKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw9ohKW97ts5UeUhFwq3AMOUJM4gffgkxHuNLEOlsVuK4Y1KrpY2MlxfqFgVB5i9vzN9j6IfIUhgfyqAydYvZuQkXuSpOdEiw9XWXYRHe0W%2FUcycBPST8Dm7fMLEy09T5tiX%2FIY3Cw0tfbBfn6eoy2pPZ4jTOWOXg7FT4UOK3vK7Q75ue6E8aYcLiyTtk2ztqf5NWc75DEMh0r0aSXF%2FCKiRxZwrhCa%2Bp19tY8eXeo75wU2xuCjubz3XrecStXc6xs36KYEPmiScZVuYaJz8Y0jyPCvc1sg4yh0VaMvP1Heynx%2F2GuOmIutssgRFUuRWOL3dcYn456Rdosb6HjIzU1Ddl2tRLPBEJW1kwNLow216mTpt7Ry5wZnmINTCh7Ny6ThU%2FNb53wcu6t%2FczMRoBG8%2FverdTPMO5VXEEP47CvA57w915wl5%2BlOTBFuwoVxDmBrdqW2OoKR3qAoqJw4mB%2Bq477H0mwpCst%2BeNlwnl3AVlfqH5lGxkEawp7o%2Fi2Vh2kRevhILAupJLiudb3MtO3iKkMVLx29GOV6IP4MsQt5GUDZImsUlGroFWnUS7HjGRylsvNCGZBVRqJI7UoLRiORImzg%2FTp7Xs9OhBVG9ev0pBpxfd23WazKNyVCzo3JYmvq2wFXJf%2BZ%2FxXGjTCRuP%2FSBjqkAfeR%2FH0S%2BaKpBw24OTnGsI6RQf90KSnogwPaoGCjwQuhmjFGWSjQRF27rrFzKkOWoTrRID1sBJfNahAyLU1OUtjgWkexqnDlSTx03ZOO7GYywKYKJwpRja55RvO3Y0T%2FFMKmW%2BKCaFokNoEyjc023mcMrkcVXOc76Wktt5kE6ZS0ncbJQdf0VpM8Snt6pL5fdYBH7jbK3yF8BPSjvJUGly1l8CeJ&X-Amz-Signature=b7ddfacb1639e120749865c993ff6681d39b38b157ecbe4f68ad0ed41819d284&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

然后最后你要记得在 root info 的时候把这两个盘点也要加进去才行，那这样的话你就完整的实现了这个日志的配置了。


然后接下来其实我们可以启动一下，在启动之前我们先把刚才老师说那个小问题先演示一下，我把这个

disruptor 依赖去掉，然后我再去启动就是 run spring boot application 它启动的时候会报错，同学们请看我把它最大化会报什么错呢？说说我们看最核心的就是 class not front error 就是我们的 Lmax 的 destructor 它的这个 factory event factory 就是我们的事件工厂就没有了，说白了就是少一个类。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/2e01c146-5f34-4426-bc65-fe5f67a065a9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RSOENA7V%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCHnc4euZQJi4o1J9sUN1rEcMUJ9OgZu15%2BCsTJptQ7ZQIhAKt7%2BQhhGoro30KSjtag%2Ft5TRcZxYz2iwd5m5uWUIpsqKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw9ohKW97ts5UeUhFwq3AMOUJM4gffgkxHuNLEOlsVuK4Y1KrpY2MlxfqFgVB5i9vzN9j6IfIUhgfyqAydYvZuQkXuSpOdEiw9XWXYRHe0W%2FUcycBPST8Dm7fMLEy09T5tiX%2FIY3Cw0tfbBfn6eoy2pPZ4jTOWOXg7FT4UOK3vK7Q75ue6E8aYcLiyTtk2ztqf5NWc75DEMh0r0aSXF%2FCKiRxZwrhCa%2Bp19tY8eXeo75wU2xuCjubz3XrecStXc6xs36KYEPmiScZVuYaJz8Y0jyPCvc1sg4yh0VaMvP1Heynx%2F2GuOmIutssgRFUuRWOL3dcYn456Rdosb6HjIzU1Ddl2tRLPBEJW1kwNLow216mTpt7Ry5wZnmINTCh7Ny6ThU%2FNb53wcu6t%2FczMRoBG8%2FverdTPMO5VXEEP47CvA57w915wl5%2BlOTBFuwoVxDmBrdqW2OoKR3qAoqJw4mB%2Bq477H0mwpCst%2BeNlwnl3AVlfqH5lGxkEawp7o%2Fi2Vh2kRevhILAupJLiudb3MtO3iKkMVLx29GOV6IP4MsQt5GUDZImsUlGroFWnUS7HjGRylsvNCGZBVRqJI7UoLRiORImzg%2FTp7Xs9OhBVG9ev0pBpxfd23WazKNyVCzo3JYmvq2wFXJf%2BZ%2FxXGjTCRuP%2FSBjqkAfeR%2FH0S%2BaKpBw24OTnGsI6RQf90KSnogwPaoGCjwQuhmjFGWSjQRF27rrFzKkOWoTrRID1sBJfNahAyLU1OUtjgWkexqnDlSTx03ZOO7GYywKYKJwpRja55RvO3Y0T%2FFMKmW%2BKCaFokNoEyjc023mcMrkcVXOc76Wktt5kE6ZS0ncbJQdf0VpM8Snt6pL5fdYBH7jbK3yF8BPSjvJUGly1l8CeJ&X-Amz-Signature=3c1944ac729c9886532b4c6a9ffdf0fa70b3a9e302f3658779269d2c03a3ec8c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

所以说你没有第三特你想去用 log 获利图你是用不了的。所以说你必须要做这个事情，就是把 disruptor 这个依赖包粘过来点进来才行。然后接下来我们再次去启动。


好，同学们请看这回我的日志已经有了，他已经能够正常的启动了，你会看到他 8001 端口，他们 cat 已经起来了，并且没有任何错误。您看到它没有任何错误，它都是一些 infer 级别的，并且没有抛异常。那现在证明我们的服务已经，服务起来了之后，然后我们刷新一下这个应用，你可以看到有一个 lox 这个文件夹，文件夹怎么过来的？就是我们在这里声明的这个logs 。然后下面应该有两个文件，一个是 App 杠应用名称 collector 还有一个是 error 杠 collector 这是不是正好符合我们自己后面的两个 append 对不对？然后还有一个 panda 是 cancel 的控制台对不对？我们的 cancel 是不是有日输出？看见了吧？有日输出。


好了，然后我们点进去，第一个看看有没有日志，同学请看这里面是有日志的对不对？然后下面这个 error connect ，这里边是没有日志的，没问题，因为我现在没有任何 error 的信息。好了，那接下来一步我们要观察的一点是什么呢？我们要通过这个日志来看一看它具体的内容都是什么，我们来看一看它的这个怎么说，就是我们的 patents 排成这样的，我们来一个一个看。通过这就可以看我把这个日志就是整体的这个信息我去 copy 一份，我就随便 copy 一个就好了，

```java
[2023-04-08T17:38:00.727+08:00] [INFO] [main-1] [com.bfxy.collector.CollectorApplication] [] [] [] [StartupInfoLogger.java,50,org.springframework.boot.StartupInfoLogger,logStarting] [Starting CollectorApplication on Mac-mini.local with PID 9471 (/Users/guojun/workspaces/workspace5/collector/target/classes started by guojun in /Users/guojun/workspaces/workspace5/collector)] ## ''
[2023-04-08T17:38:00.787+08:00] [INFO] [main-1] [com.bfxy.collector.CollectorApplication] [] [] [] [SpringApplication.java,675,org.springframework.boot.SpringApplication,logStartupProfileInfo] [No active profile set, falling back to default profiles: default] ## ''
[2023-04-08T17:38:01.162+08:00] [INFO] [main-1] [org.springframework.boot.web.embedded.tomcat.TomcatWebServer] [] [] [] [TomcatWebServer.java,90,org.springframework.boot.web.embedded.tomcat.TomcatWebServer,initialize] [Tomcat initialized with port(s): 8001 (http)] ## ''
[2023-04-08T17:38:01.171+08:00] [INFO] [main-1] [org.apache.coyote.http11.Http11NioProtocol] [] [] [] [DirectJDKLog.java,173,org.apache.juli.logging.DirectJDKLog,log] [Initializing ProtocolHandler ["http-nio-8001"]] ## ''
[2023-04-08T17:38:01.175+08:00] [INFO] [main-1] [org.apache.catalina.core.StandardService] [] [] [] [DirectJDKLog.java,173,org.apache.juli.logging.DirectJDKLog,log] [Starting service [Tomcat]] ## ''
[2023-04-08T17:38:01.175+08:00] [INFO] [main-1] [org.apache.catalina.core.StandardEngine] [] [] [] [DirectJDKLog.java,173,org.apache.juli.logging.DirectJDKLog,log] [Starting Servlet engine: [Apache Tomcat/9.0.19]] ## ''
[2023-04-08T17:38:01.215+08:00] [INFO] [main-1] [org.apache.catalina.core.ContainerBase.[Tomcat].[localhost].[/]] [] [] [] [DirectJDKLog.java,173,org.apache.juli.logging.DirectJDKLog,log] [Initializing Spring embedded WebApplicationContext] ## ''
[2023-04-08T17:38:01.216+08:00] [INFO] [main-1] [org.springframework.web.context.ContextLoader] [] [] [] [ServletWebServerApplicationContext.java,296,org.springframework.boot.web.servlet.context.ServletWebServerApplicationContext,prepareWebApplicationContext] [Root WebApplicationContext: initialization completed in 413 ms] ## ''
[2023-04-08T17:38:01.306+08:00] [INFO] [main-1] [org.springframework.scheduling.concurrent.ThreadPoolTaskExecutor] [] [] [] [ExecutorConfigurationSupport.java,171,org.springframework.scheduling.concurrent.ExecutorConfigurationSupport,initialize] [Initializing ExecutorService 'applicationTaskExecutor'] ## ''
[2023-04-08T17:38:01.364+08:00] [INFO] [main-1] [org.apache.coyote.http11.Http11NioProtocol] [] [] [] [DirectJDKLog.java,173,org.apache.juli.logging.DirectJDKLog,log] [Starting ProtocolHandler ["http-nio-8001"]] ## ''
[2023-04-08T17:38:01.375+08:00] [INFO] [main-1] [org.springframework.boot.web.embedded.tomcat.TomcatWebServer] [] [] [] [TomcatWebServer.java,204,org.springframework.boot.web.embedded.tomcat.TomcatWebServer,start] [Tomcat started on port(s): 8001 (http) with context path ''] ## ''
[2023-04-08T17:38:01.377+08:00] [INFO] [main-1] [com.bfxy.collector.CollectorApplication] [] [] [] [StartupInfoLogger.java,59,org.springframework.boot.StartupInfoLogger,logStarted] [Started CollectorApplication in 0.822 seconds (JVM running for 1.301)] ## ''
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
/**
     * [%d{yyyy-MM-dd'T'HH:mm:ss.SSSZZ}]
     * [%level{length=5}]
     * [%thread-%tid]
     * [%logger]
     * [%X{hostName}]
     * [%X{ip}]
     * [%X{applicationName}]
     * [%F,%L,%C,%M]
     * [%m]
     * ## '%ex'%n
     *
     * @return
     */
    @RequestMapping(value = "/index")
    public String index( ) {
        log.info("我是一条 info 日志");
        log.warn("我是一条 warn 日志");
        log.error("我是一条 error 日志");

        return "inx";
    }
```

然后 copy 一个之后我就把它停掉了，咱们对照着一起来看一看这些都代表什么含义，就是这一块的 pattern 来，这是我们实际的日志。


第一个同学们请看它是一个 udc 的时间对吧，就是我们的这个代替的就是我们的东八区。好了，然后 F 真是 level 是不是日志的级别？日志的级别是 level 然后 thread 就是我当前的线程是不是主线程，没什么可说的。那这三个已经对应上了，再往下我们来看一看，再往下是什么呢？还有一个是什么？还有一个是我们的 loggerlogger 是什么东西？大家可以看 logger 你可以理解为它就是具体的一个类了一个类的名称，它启动的是他们看看 web server 这么一个类。然后再往下看有三个空格，三个空的一个中括号。这三个中括号没有填充，大家能理解吧，因为这是我自定义的 host name IP 跟 application name 我都不知道，我还没填，所以说这是没有值的，这是没问题的。



再往下看叫做 flcm 那它中间有逗号，是不是看见了吧？那 F 代表什么？ F 就代表你的这个当前执行的类是什么，是哪个 file 文件？就是我们的 common cat map through.java 这个文件 L 就是 Lens 行号当前执行了有多少行？第 90 行 K 了。然后后面 C 你可以认为是 class 对不对？奥克点 spring [framework.boot.web](http://framework.boot.web/) 点这个很长，就是 Tom cat web server 对吧？好了，那 M 就是 master 方法看见了吧。我的方法叫做 init lazer 再往下回车搞定完这个之后，我的 message 是不是叫做 Tom cat init lazer with point 8001 HTTP 看见了。那这一句话说白了是什么呢？就是你日志的 info 信息。然后后面两个井号看两个井号原样原封不动的，我们没有抛异常，所以说你看不到任何东西，后面杠 N 表示换行。 OK 基本上我已经把整个的 pattern 跟大家讲了一下了，现在大家应该有所了解了。

```java
[2023-04-08T17:38:01.162+08:00] 
[INFO] 
[main-1] 
[org.springframework.boot.web.embedded.tomcat.TomcatWebServer] 
[] 
[] 
[] 
[TomcatWebServer.java,90,org.springframework.boot.web.embedded.tomcat.TomcatWebServer,initialize] 
[Tomcat initialized with port(s): 8001 (http)] ## ''




@Slf4j
@RestController
public class IndexController {

    /**
     * [%d{yyyy-MM-dd'T'HH:mm:ss.SSSZZ}]
     * [%level{length=5}]
     * [%thread-%tid]
     * [%logger]
     * [%X{hostName}]
     * [%X{ip}]
     * [%X{applicationName}]
     * [%F,%L,%C,%M]
     * [%m]
     * ## '%ex'%n
     *
     *-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                     [2023-04-08T17:38:01.162+08:00]
                     [INFO]
                     [main-1]
                     [org.springframework.boot.web.embedded.tomcat.TomcatWebServer]
                     []
                     []
                     []
                     [TomcatWebServer.java,90,org.springframework.boot.web.embedded.tomcat.TomcatWebServer,initialize]
                     [Tomcat initialized with port(s): 8001 (http)] ## ''`
     *
     */
    @RequestMapping(value = "/index")
    public String index( ) {

        //  MDC  

        log.info("我是一条 info 日志");
        log.warn("我是一条 warn 日志");
        log.error("我是一条 error 日志");

        return "inx";
    }
```


OK 现在我们接下来要做的事情是什么呢？我们接下来要做的事情就是对于关键的这三个取余符号 X 进行一个填充。那其实我们既然应用了 log 复制数或者是 sl 复制，那有一个非常核心的概念叫做 mdcmdc 这个 mdc 是一个什么东西呢？你可以认为它是一个当前线程所绑定的一个局部变量，你可以认为它底层实现就是一个 srilocal 里边加一个 map 就是这么简单，就是跟当前这个 log 相关的mdc 。 sorry 写错了 mdc 好了，这个 mdc 怎么去用呢？很简单，你直接就可以直接这样去写说，当前线程，我直接用 mdc.cot 我就可以了。



put 一个 P 叫做001，然后 put 一个 value 叫做1a1，这就可以了。那这样的话对应的这个 K 如果你有，它就会帮你打到 log 日志里，就是这么简单。那这个 mdc 到底是什么东西呢？你点进去看一下就好了，是不是它是一个 class 对不对？然后它里边它的 put 方法我们找到它的这个 put 你看它这里面有 get map 对了吗？ 

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/837fbbc8-574c-48fe-a196-86375b6ef4e4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RSOENA7V%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCHnc4euZQJi4o1J9sUN1rEcMUJ9OgZu15%2BCsTJptQ7ZQIhAKt7%2BQhhGoro30KSjtag%2Ft5TRcZxYz2iwd5m5uWUIpsqKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw9ohKW97ts5UeUhFwq3AMOUJM4gffgkxHuNLEOlsVuK4Y1KrpY2MlxfqFgVB5i9vzN9j6IfIUhgfyqAydYvZuQkXuSpOdEiw9XWXYRHe0W%2FUcycBPST8Dm7fMLEy09T5tiX%2FIY3Cw0tfbBfn6eoy2pPZ4jTOWOXg7FT4UOK3vK7Q75ue6E8aYcLiyTtk2ztqf5NWc75DEMh0r0aSXF%2FCKiRxZwrhCa%2Bp19tY8eXeo75wU2xuCjubz3XrecStXc6xs36KYEPmiScZVuYaJz8Y0jyPCvc1sg4yh0VaMvP1Heynx%2F2GuOmIutssgRFUuRWOL3dcYn456Rdosb6HjIzU1Ddl2tRLPBEJW1kwNLow216mTpt7Ry5wZnmINTCh7Ny6ThU%2FNb53wcu6t%2FczMRoBG8%2FverdTPMO5VXEEP47CvA57w915wl5%2BlOTBFuwoVxDmBrdqW2OoKR3qAoqJw4mB%2Bq477H0mwpCst%2BeNlwnl3AVlfqH5lGxkEawp7o%2Fi2Vh2kRevhILAupJLiudb3MtO3iKkMVLx29GOV6IP4MsQt5GUDZImsUlGroFWnUS7HjGRylsvNCGZBVRqJI7UoLRiORImzg%2FTp7Xs9OhBVG9ev0pBpxfd23WazKNyVCzo3JYmvq2wFXJf%2BZ%2FxXGjTCRuP%2FSBjqkAfeR%2FH0S%2BaKpBw24OTnGsI6RQf90KSnogwPaoGCjwQuhmjFGWSjQRF27rrFzKkOWoTrRID1sBJfNahAyLU1OUtjgWkexqnDlSTx03ZOO7GYywKYKJwpRja55RvO3Y0T%2FFMKmW%2BKCaFokNoEyjc023mcMrkcVXOc76Wktt5kE6ZS0ncbJQdf0VpM8Snt6pL5fdYBH7jbK3yF8BPSjvJUGly1l8CeJ&X-Amz-Signature=0567dab11889d745922d9a5bb90ff3e612a3224a8c6bd5be60ee806b5f597ad1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

get mdc map 那证明它肯定是一个 map 好了，然后这里面没有，肯定在我们找到空调。这个 put 看见了吧。 Put. 然后你可以在 put mdc 点进去。当然具体下面的实现你自己可以去找，你看它有不同的实现，比如说 G boss logger manager provider 还有什么 log for G two 是不是 logger provider 还有 log for G logger provider 以及 sl for G log provider 就是它只是一个接口，它下面有不同的实现。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/2d1e43b3-1535-4571-a8e4-b26a6caac377/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RSOENA7V%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225324Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCHnc4euZQJi4o1J9sUN1rEcMUJ9OgZu15%2BCsTJptQ7ZQIhAKt7%2BQhhGoro30KSjtag%2Ft5TRcZxYz2iwd5m5uWUIpsqKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw9ohKW97ts5UeUhFwq3AMOUJM4gffgkxHuNLEOlsVuK4Y1KrpY2MlxfqFgVB5i9vzN9j6IfIUhgfyqAydYvZuQkXuSpOdEiw9XWXYRHe0W%2FUcycBPST8Dm7fMLEy09T5tiX%2FIY3Cw0tfbBfn6eoy2pPZ4jTOWOXg7FT4UOK3vK7Q75ue6E8aYcLiyTtk2ztqf5NWc75DEMh0r0aSXF%2FCKiRxZwrhCa%2Bp19tY8eXeo75wU2xuCjubz3XrecStXc6xs36KYEPmiScZVuYaJz8Y0jyPCvc1sg4yh0VaMvP1Heynx%2F2GuOmIutssgRFUuRWOL3dcYn456Rdosb6HjIzU1Ddl2tRLPBEJW1kwNLow216mTpt7Ry5wZnmINTCh7Ny6ThU%2FNb53wcu6t%2FczMRoBG8%2FverdTPMO5VXEEP47CvA57w915wl5%2BlOTBFuwoVxDmBrdqW2OoKR3qAoqJw4mB%2Bq477H0mwpCst%2BeNlwnl3AVlfqH5lGxkEawp7o%2Fi2Vh2kRevhILAupJLiudb3MtO3iKkMVLx29GOV6IP4MsQt5GUDZImsUlGroFWnUS7HjGRylsvNCGZBVRqJI7UoLRiORImzg%2FTp7Xs9OhBVG9ev0pBpxfd23WazKNyVCzo3JYmvq2wFXJf%2BZ%2FxXGjTCRuP%2FSBjqkAfeR%2FH0S%2BaKpBw24OTnGsI6RQf90KSnogwPaoGCjwQuhmjFGWSjQRF27rrFzKkOWoTrRID1sBJfNahAyLU1OUtjgWkexqnDlSTx03ZOO7GYywKYKJwpRja55RvO3Y0T%2FFMKmW%2BKCaFokNoEyjc023mcMrkcVXOc76Wktt5kE6ZS0ncbJQdf0VpM8Snt6pL5fdYBH7jbK3yF8BPSjvJUGly1l8CeJ&X-Amz-Signature=135359c198cc8958ab2c5f9e048e98580e5e9a290bdfe5fc40962a34536990ed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


那我们现在肯定是用的什么 sl for G two 对不对？那你看到这个 thread context 看到 thread context 就意味着这东西好像是什么，跟什么比较像对不对？就跟此外 local 比较像，就是一个现成的一个 contact 上下文对吧？然后这里边只不过是扔了一个 map 而已你可以这么去理解，你可以点进去看一下，再往后点一点，你可以去关注一下它里边到底是怎么做。就 thread context 就这 thread contact stack 等等。具体的我就不领着小伙伴们去看了。


其实你最终点的话，你再往后点，你看这个 thread context map 其实就是这个东西。很关键的就是我们刚才所看到的那个里边的一个脉。然后它其实什么呢？它其实是你可以理解为就是一个此外的 logo 


好了，那我们暂时就先看了解到这吗。关于 mdc 那接下来我们现在要做什么事情呢？我们先把这个都关掉。我们现在写一个简单的类，就是说我要用到 mdc 比如说有一些关键的参数，我想再请求每一次 request 我过来的时候帮我去 put 到 mdc 里。比如说我们刚才所想要的 host name IP 以及 observation name 对吧？那我们怎么去做呢？我们先写一个比如说在工具类里边，我们写一个卡拉斯，咱们叫做 inputmdc 。


简单写边 put mdc 音部的 mdc 怎么去做呢？首先前两个参数都比较好，过去比如说 host name 跟 IP 在我们的这个 net YouTube 里都有，但是 obligation name 这个东西是没有的，那它是在配置文件里配置好的，我们可以通过什么呢？我们可以通过一些什么 environment 环境变量是可以获取到的。比如说在这里老师 implements 很简单， environment environment where 这个接口。然后去重写一下，把这个东西当成一个成员变量。比如说我们来一个 static 这个东西。然后我们去对它进行赋个值是可以的，因为静态的，所以说什么时候赋值我没有加final ，所以说是无所谓的。

```java
package com.bfxy.collector.util;

import org.jboss.logging.MDC;
import org.springframework.context.EnvironmentAware;
import org.springframework.core.env.Environment;
import org.springframework.stereotype.Component;

@Component
public class InputMDC implements EnvironmentAware {

	private static Environment environment;
	
	@Override
	public void setEnvironment(Environment environment) {
		InputMDC.environment = environment;
	}
	
	public static void putMDC() {
		MDC.put("hostName", NetUtil.getLocalHostName());
		MDC.put("ip", NetUtil.getLocalIp());
		MDC.put("applicationName", environment.getProperty("spring.application.name"));
	}

}
```


好了，搞定这个事情之后，然后我们再来一个方法叫做 public static 然后咱们叫做 put 就叫做 put 就好了。然后它是什么呢？ Y 或者是 put MD C 写好看一点。我们要 put 什么内容？ MDC.put 这里边我们都被写死了，叫做 host name 是不是和 name 怎么来呢？我们通过 net util.get host name 就可以取到。


然后还有很多比如说我们的 IP 是什么？是不是？那我直接可以写 get IP ？是不是 local IP 然后还有一个叫做 application name 这个 application name 怎么去取呢？我们有 environment 环境了，是不是我可以点 get practice 是不是 get practice 这个 get property 这个 property 是什么呢？你在这里边 application practice 配置的它最终都会加载到那个环境变量里，所以说你直接取这个就好了，很简单就直接放到这里。这就取到了是不是？然后把对应内容都铺到 mdc 里了是吧。好，那我们比如说在这之前执行这个 index 方法之前，我先调用一下，我先 input 什么 input MD C 点好，然后再执行这三个方法，来大家一起来观察结果，看一看会有什么结果。


之前我们这三个空都是什么呢？都是空的，听见都是什么也没有的。所以我现在把两个 logs 文件给它干掉，干掉以后，然后接下来我重新再 run S spring boot application 一下。启动好了以后我们做一件事情，比如说我们现在就可以去访问了。启动好了之后，我们把这个浏览器拿过来，这里边对应着那个方法什么呢？看一下，因为是 index 是吧，index就好说了，我们把 index 拿过来。 index 启动的是 8001 回车。这有问题，local host 8001 index 他这里边给我报了一个错来，大家看 low point 是不是控制得异常，那这说明什么问题呢？这说明我们代码已经进来了，但是抛控制人长了是不是？ OK 那其实我们来看一看这里边抛控人异常是说明十九行这块有问题对吧？没关系，我们再往下找同学们请看其实最关键的是什么呢？最关键的就是这。


一个单引号上面看见了吗？这是什么？这是堆栈信息错误异常的对战机再看这又是一个单引号是不是？两个井号后面跟着单引号，两个单引号引起来的部分就是我们的堆栈信息，这个堆栈信息代表什么？这里边有换行对不对？我们以后再去做 group 就是在用我们的 loss 赛事去解析这一行日志的时候，你有换行，这是很难解析的。所以说老师在这里想了一个非常巧妙的方式，就是用单引号把所有的错误引起来。然后让他帮我去做一个单引号的这么一个级别的解析就好了。好了，那既然有错误，我们在这里来观察一下。既然有错误，说明一个什么问题说明我们的劳格日志，看这是我们的 App 日志，看这个错误是不是那个空指针异常，我们往后拖看。


no point exception 对吧？这个 App 日志里边有全量的错误。那我们 error 同学们请看 error 日志里边就一个 error 看见了，就一个 error 它没有任何其他的音符级别的日志。当然 warning 它也会有对不对？所以说在这里同学们你会发现一个问题是不是我们自己的什么呢？我们自己的对应的这个 log for G two 里边的第二一个 append 已经生效了，就是它只帮我去过滤 warning 级别以上的日志才收集，并且帮我去收集到 error 杠 cell name 就是我们的英文名称 collector 然后它这个日志是怎么去打的？是这样去打的对不对？ OK 好，你看到了，就是我们现在整体所有的都已经符合我们之前所定义的一些，就跟我们的设想是完全一致的了。然后我们再回过头来，把这个小问题解决，把它关掉，先整体的 close 掉，我的应用服务停掉之后，然后我把这两个文件先删掉就好了，这很简单了。


然后我们看一看刚才那个 no point 那个 seven 是由于什么原因导致的。首先第一点你会看到这个代码很简单，是不是就把它奥特维尔进来，但是它是空的。为什么呢？因为他没有去给他去扔，因为这个东西需要依赖我们的 pre 容器的，所以说你加一个 component 注解或者一个 service 就好了，这样的话他就不会抛弃控制人异常了。
OK 那接下来我们再次重新去启动一下我们自己的这个 spring boot 应用程序。现在 logo 是空的，没有任何内容。好同学们请看我刷新一下 logo 这里边 

```java
package com.bfxy.collector.util;

import org.jboss.logging.MDC;
import org.springframework.context.EnvironmentAware;
import org.springframework.core.env.Environment;
import org.springframework.stereotype.Component;

@Component
public class InputMDC implements EnvironmentAware {

	private static Environment environment;
	
	@Override
	public void setEnvironment(Environment environment) {
		InputMDC.environment = environment;
	}
	
	public static void putMDC() {
		MDC.put("hostName", NetUtil.getLocalHostName());
		MDC.put("ip", NetUtil.getLocalIp());
		MDC.put("applicationName", environment.getProperty("spring.application.name"));
	}

}
```

application.connector 里边它是有对应的日志输出的。然后我们的 arrow 里边是啥都没有的，对不对？然后接下来我们还是那句话，我们，访问一下 index 好同学们请看这个 index 已经有了这个访问的结果了，就是它有 response 响应了。也就是说刚才这个 controller 它已经返回了这个 index 并且他已经输出了这三行日志了。

```java
[2023-04-08T19:57:55.741+08:00] [INFO] [http-nio-8001-exec-1-27] [com.bfxy.collector.web.IndexController] [Mac-mini.local] [192.168.13.1] [collector] [IndexController.java,46,com.bfxy.collector.web.IndexController,index] [我是一条 info 日志] ## ''
[2023-04-08T19:57:55.741+08:00] [WARN] [http-nio-8001-exec-1-27] [com.bfxy.collector.web.IndexController] [Mac-mini.local] [192.168.13.1] [collector] [IndexController.java,47,com.bfxy.collector.web.IndexController,index] [我是一条 warn 日志] ## ''
[2023-04-08T19:57:55.741+08:00] [ERROR] [http-nio-8001-exec-1-27] [com.bfxy.collector.web.IndexController] [Mac-mini.local] [192.168.13.1] [collector] [IndexController.java,48,com.bfxy.collector.web.IndexController,index] [我是一条 error 日志] ## ''
```


第一个是 info warning 还有 L 控制台，我们能看到全量的 info warning 跟 error 这是没问题的。对不对？然后我们会看到我是一条音符日志，我是一条 warning 日志，我是一条 error 日志。注意，同学们请看我们后面那三个空已经有了。这个是我们自己的 host name 这是我自己的机器，然后是我们的 IP 地址 11 点三五。然后是我的应用名称，就是看 lecture 看见了。好了，完全没有问题。对不对？这就证明我们通过 mdc 已经把我们想要的一些特殊的 key put 到了这个我们的日志输出里边了。那这个就是所谓的mdc ，它能帮我们去做这种变量的这种替换输出。



然后除了这个以外，我们看一看 App log ，它里边应该也会有全量的日志对吧，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/58b2a2e9-71ac-40c7-b345-e3594e32e7b8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RSOENA7V%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCHnc4euZQJi4o1J9sUN1rEcMUJ9OgZu15%2BCsTJptQ7ZQIhAKt7%2BQhhGoro30KSjtag%2Ft5TRcZxYz2iwd5m5uWUIpsqKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw9ohKW97ts5UeUhFwq3AMOUJM4gffgkxHuNLEOlsVuK4Y1KrpY2MlxfqFgVB5i9vzN9j6IfIUhgfyqAydYvZuQkXuSpOdEiw9XWXYRHe0W%2FUcycBPST8Dm7fMLEy09T5tiX%2FIY3Cw0tfbBfn6eoy2pPZ4jTOWOXg7FT4UOK3vK7Q75ue6E8aYcLiyTtk2ztqf5NWc75DEMh0r0aSXF%2FCKiRxZwrhCa%2Bp19tY8eXeo75wU2xuCjubz3XrecStXc6xs36KYEPmiScZVuYaJz8Y0jyPCvc1sg4yh0VaMvP1Heynx%2F2GuOmIutssgRFUuRWOL3dcYn456Rdosb6HjIzU1Ddl2tRLPBEJW1kwNLow216mTpt7Ry5wZnmINTCh7Ny6ThU%2FNb53wcu6t%2FczMRoBG8%2FverdTPMO5VXEEP47CvA57w915wl5%2BlOTBFuwoVxDmBrdqW2OoKR3qAoqJw4mB%2Bq477H0mwpCst%2BeNlwnl3AVlfqH5lGxkEawp7o%2Fi2Vh2kRevhILAupJLiudb3MtO3iKkMVLx29GOV6IP4MsQt5GUDZImsUlGroFWnUS7HjGRylsvNCGZBVRqJI7UoLRiORImzg%2FTp7Xs9OhBVG9ev0pBpxfd23WazKNyVCzo3JYmvq2wFXJf%2BZ%2FxXGjTCRuP%2FSBjqkAfeR%2FH0S%2BaKpBw24OTnGsI6RQf90KSnogwPaoGCjwQuhmjFGWSjQRF27rrFzKkOWoTrRID1sBJfNahAyLU1OUtjgWkexqnDlSTx03ZOO7GYywKYKJwpRja55RvO3Y0T%2FFMKmW%2BKCaFokNoEyjc023mcMrkcVXOc76Wktt5kE6ZS0ncbJQdf0VpM8Snt6pL5fdYBH7jbK3yF8BPSjvJUGly1l8CeJ&X-Amz-Signature=f2282595d914f0103924bb46222de512ad6cad98da858277f1744c3471f0dbbb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

我们看到 info warning 以及 error 都是有的对吧？那同学们想一想，那对应着我们的 error.connector 它里面有什么呢？它里边只有 warning 级别以上的日志，只有两个就对了，warning跟 error 看见了吧。就是有了 warning 跟 errorok 没问题。
接下来我们再做最后一个小实验。刚才其实出现了一个小异常，所以说我们提前看到那个结果。现在我们再次来写个代码，比如说现在我们就手工的去造一个异常，我们写 request mapping request to mike 我们给它起一个名字，叫做杠 lerr poverty ER 好，我们就自己造一个小的异常。这个很简单，比如说我们造一个什么异常呢？我们造一个算术异常可以吗？可以是吧，我们就 try catch 然后我们自己就是 int A 等于 1 除0。对不对？就是 arise magic exception 然后 by zero 就算出异常了。

```java
@RequestMapping(value = "/err")
    public String err() {
        InputMDC.putMDC();
        try {
            int a = 1/0;
        } catch (Exception e) {
            log.error("算数异常", e);
        }
        return "err";
    }
}
```


好，算数异常的时候，不管怎么样，我们在这里记录一下我的 input 信息，就是把一些内容放到我们的 mdc 里的打一下。然后在这里边比如说我们就记录一下我们的这个 log 点，这就应该是 L 是不是 love.l 就说算数异常，然后逗号把这个 E 打进去对吧，可不可以没问题的。然后这里面有个返回值，我们就返回一个字符串就好了。 err 没错。好，接下来我把它停掉，然后我还是把这两个日先删掉，让咱们同学看到，就是正常你想要看到的结果才行。我再次去启动一下这个小的应用服务器来启动了以后，我们再次去通过浏览器去访问。首先访问一下 index 对不对？然后我们看我再访问一下 err 回车。好，我们来看一看日志结果。

```java
[2023-04-08T20:07:22.097+08:00] [ERROR] [http-nio-8001-exec-2-28] [com.bfxy.collector.web.IndexController] [Mac-mini.local] [192.168.13.1] [collector] [IndexController.java,48,com.bfxy.collector.web.IndexController,index] [我是一条 error 日志] ## ''
[2023-04-08T20:07:31.476+08:00] [ERROR] [http-nio-8001-exec-3-29] [com.bfxy.collector.web.IndexController] [Mac-mini.local] [192.168.13.1] [collector] [IndexController.java,60,com.bfxy.collector.web.IndexController,err] [算数异常] ## ' java.lang.ArithmeticException: / by zero
	at com.bfxy.collector.web.IndexController.err(IndexController.java:58)
	at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
	at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
	at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.lang.reflect.Method.invoke(Method.java:498)
	at org.springframework.web.method.support.InvocableHandlerMethod.doInvoke(InvocableHandlerMethod.java:190)
	at org.springframework.web.method.support.InvocableHandlerMethod.invokeForRequest(InvocableHandlerMethod.java:138)
	at org.springframework.web.servlet.mvc.method.annotation.ServletInvocableHandlerMethod.invokeAndHandle(ServletInvocableHandlerMethod.java:104)
	at org.springframework.web.servlet.mvc.method.annotation.RequestMappingHandlerAdapter.invokeHandlerMethod(RequestMappingHandlerAdapter.java:892)
	at org.springframework.web.servlet.mvc.method.annotation.RequestMappingHandlerAdapter.handleInternal(RequestMappingHandlerAdapter.java:797)
	at org.springframework.web.servlet.mvc.method.AbstractHandlerMethodAdapter.handle(AbstractHandlerMethodAdapter.java:87)
	at org.springframework.web.servlet.DispatcherServlet.doDispatch(DispatcherServlet.java:1039)
	at org.springframework.web.servlet.DispatcherServlet.doService(DispatcherServlet.java:942)
	at org.springframework.web.servlet.FrameworkServlet.processRequest(FrameworkServlet.java:1005)
	at org.springframework.web.servlet.FrameworkServlet.doGet(FrameworkServlet.java:897)
	at javax.servlet.http.HttpServlet.service(HttpServlet.java:634)
	at org.springframework.web.servlet.FrameworkServlet.service(FrameworkServlet.java:882)
```


首先我们看到了对应着个人产已经打印出来了，阿瑞斯 metric exception 算出一场 by zero 对不对？Ok.然后接下来我们其实你首先看一下全量日志是不是都有。然后再看一下这个错误的那个文件是不是都有就好。好，这是没问题的。对不对？这个全量里边肯定是有错误的。对不对？阿瑞斯 metric 在线打印了，然后我们关掉再看一下 error 日志里边。有一个 warning 有一个 error 这是我们之前 index 访问的两条日志。还有一个就是刚才我们算数异常，算术异常，艾瑞斯 let it exception 这里边已经有了，看见了，已经有了对应的输出，而且它通过单引号的方式帮我去把所有的堆栈信息通过单引号去引起来了。这样的话后面我们再去做 group 就是再去做这个 lox 战士去解析的时候才非常非常方便。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/15b5ea04-b059-4340-b479-9589bc4c939d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RSOENA7V%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCHnc4euZQJi4o1J9sUN1rEcMUJ9OgZu15%2BCsTJptQ7ZQIhAKt7%2BQhhGoro30KSjtag%2Ft5TRcZxYz2iwd5m5uWUIpsqKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw9ohKW97ts5UeUhFwq3AMOUJM4gffgkxHuNLEOlsVuK4Y1KrpY2MlxfqFgVB5i9vzN9j6IfIUhgfyqAydYvZuQkXuSpOdEiw9XWXYRHe0W%2FUcycBPST8Dm7fMLEy09T5tiX%2FIY3Cw0tfbBfn6eoy2pPZ4jTOWOXg7FT4UOK3vK7Q75ue6E8aYcLiyTtk2ztqf5NWc75DEMh0r0aSXF%2FCKiRxZwrhCa%2Bp19tY8eXeo75wU2xuCjubz3XrecStXc6xs36KYEPmiScZVuYaJz8Y0jyPCvc1sg4yh0VaMvP1Heynx%2F2GuOmIutssgRFUuRWOL3dcYn456Rdosb6HjIzU1Ddl2tRLPBEJW1kwNLow216mTpt7Ry5wZnmINTCh7Ny6ThU%2FNb53wcu6t%2FczMRoBG8%2FverdTPMO5VXEEP47CvA57w915wl5%2BlOTBFuwoVxDmBrdqW2OoKR3qAoqJw4mB%2Bq477H0mwpCst%2BeNlwnl3AVlfqH5lGxkEawp7o%2Fi2Vh2kRevhILAupJLiudb3MtO3iKkMVLx29GOV6IP4MsQt5GUDZImsUlGroFWnUS7HjGRylsvNCGZBVRqJI7UoLRiORImzg%2FTp7Xs9OhBVG9ev0pBpxfd23WazKNyVCzo3JYmvq2wFXJf%2BZ%2FxXGjTCRuP%2FSBjqkAfeR%2FH0S%2BaKpBw24OTnGsI6RQf90KSnogwPaoGCjwQuhmjFGWSjQRF27rrFzKkOWoTrRID1sBJfNahAyLU1OUtjgWkexqnDlSTx03ZOO7GYywKYKJwpRja55RvO3Y0T%2FFMKmW%2BKCaFokNoEyjc023mcMrkcVXOc76Wktt5kE6ZS0ncbJQdf0VpM8Snt6pL5fdYBH7jbK3yF8BPSjvJUGly1l8CeJ&X-Amz-Signature=8df9ec4ccbff59ea1449efc3605261f871f8021652dece59f44b005517a53c04&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/8b56d181-1e59-4c51-9a70-c53c0b025527/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RSOENA7V%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225325Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQCHnc4euZQJi4o1J9sUN1rEcMUJ9OgZu15%2BCsTJptQ7ZQIhAKt7%2BQhhGoro30KSjtag%2Ft5TRcZxYz2iwd5m5uWUIpsqKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1Igw9ohKW97ts5UeUhFwq3AMOUJM4gffgkxHuNLEOlsVuK4Y1KrpY2MlxfqFgVB5i9vzN9j6IfIUhgfyqAydYvZuQkXuSpOdEiw9XWXYRHe0W%2FUcycBPST8Dm7fMLEy09T5tiX%2FIY3Cw0tfbBfn6eoy2pPZ4jTOWOXg7FT4UOK3vK7Q75ue6E8aYcLiyTtk2ztqf5NWc75DEMh0r0aSXF%2FCKiRxZwrhCa%2Bp19tY8eXeo75wU2xuCjubz3XrecStXc6xs36KYEPmiScZVuYaJz8Y0jyPCvc1sg4yh0VaMvP1Heynx%2F2GuOmIutssgRFUuRWOL3dcYn456Rdosb6HjIzU1Ddl2tRLPBEJW1kwNLow216mTpt7Ry5wZnmINTCh7Ny6ThU%2FNb53wcu6t%2FczMRoBG8%2FverdTPMO5VXEEP47CvA57w915wl5%2BlOTBFuwoVxDmBrdqW2OoKR3qAoqJw4mB%2Bq477H0mwpCst%2BeNlwnl3AVlfqH5lGxkEawp7o%2Fi2Vh2kRevhILAupJLiudb3MtO3iKkMVLx29GOV6IP4MsQt5GUDZImsUlGroFWnUS7HjGRylsvNCGZBVRqJI7UoLRiORImzg%2FTp7Xs9OhBVG9ev0pBpxfd23WazKNyVCzo3JYmvq2wFXJf%2BZ%2FxXGjTCRuP%2FSBjqkAfeR%2FH0S%2BaKpBw24OTnGsI6RQf90KSnogwPaoGCjwQuhmjFGWSjQRF27rrFzKkOWoTrRID1sBJfNahAyLU1OUtjgWkexqnDlSTx03ZOO7GYywKYKJwpRja55RvO3Y0T%2FFMKmW%2BKCaFokNoEyjc023mcMrkcVXOc76Wktt5kE6ZS0ncbJQdf0VpM8Snt6pL5fdYBH7jbK3yF8BPSjvJUGly1l8CeJ&X-Amz-Signature=962706575cb85f68fb83e4a292e3eaf08348a99c2f72b1918840eef5d2fcead1&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


如果你没有这个，那你比如说你换行认为是一条日志吗？这不太合适，因为我们有很深的对战信息吧？然后你用什么特殊的字符呢？比如说你用中国号吗也不太合适，因为这个中国号可能是认为对于一条日志的这么一个截取方式，所以说你用什么样的手段截取都不太合适。那你就用一个固定的分隔符，比如说像老师这样用单引号，两个井号是表示两个井号后面所有的单引号都是一个错误日志，这是一个特殊的占位，你其实你不用它也可以，但是我习惯了好了，我把它停掉，现在我们已经没有任何问题了，也就是说对于日志的输出我们已经首先这节课做了日志的分级，还学了学习了这个 MD C 以及我们 L 日志的一个。这个输出全量日志在 App collector 里边，错误日志就是 warning 级别以上的日志在 error collector 里边。最后我们也接触了 mdc 可以去放一些动态的值。好了，那么这节课我们就讲到这，感谢小伙伴们收看。





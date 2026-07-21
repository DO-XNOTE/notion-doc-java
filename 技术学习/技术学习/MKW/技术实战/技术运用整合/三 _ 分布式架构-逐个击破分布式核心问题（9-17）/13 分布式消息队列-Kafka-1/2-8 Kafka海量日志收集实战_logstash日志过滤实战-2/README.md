---
title: 2-8 Kafka海量日志收集实战_logstash日志过滤实战-2
---

# 2-8 Kafka海量日志收集实战_logstash日志过滤实战-2

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e20eebc6-6213-4d6d-acf9-1f9f54896a19/SCR-20240807-hhfw.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJONFXAK%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCUU%2FsmgSmmA79vKAq2uPaSoZBvEhmupX7AzsFFbINgsgIgeOYT2%2FUl7GodgHiusoKPqEmLV6ajwH5Bz4LPAquoHCIqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDELdNWKmQzZP%2BflUQyrcAy9ethytFRz5ttEL4bTztKXb7s%2FzKryFYnwIN%2Bb0pU3Bhkk4ykC%2FLkqmh5uM7c7q1YFTnumR5JUwojDrjVXv%2BjuRNVfJiWv4kFDt7i0zF7Zhj0tdh1SaLHBd4hjjHSV8tfyULUlsID6Fp8Jh9hKVC5E6Tof6px8t9aRpEoUWx5nI1NSlCvIDom%2BSR842Nuo2v542wROpH12x7qRebmsG5Y%2FuM91o02ERP%2BF1Ho9QRkRwqs%2BPZq%2BXC2qTNyer3kjV9L5zjsr%2BFCVz20nJONUM%2BE9ycCMB6HXPN0ckr5nJ2GMyA0vE0dINqiBmjUno6ems6Tz5TFtWtwYGmHgMq8wCio7vYtR38caYSWy7WKTm%2BMcnmFfntZumGUY30xwqIC%2BNwwHTnR9mUClhvDOneYkHJ0Ye54WqJHnaVbB0wzPw%2Fqr2%2BI84Vac7vG4xWjcbv8n7b%2Bg8eJZn65xeAK1DTatatXlhynhnr39%2BLlF%2FJYEXOGRpj5exvWXo2KhhcbR6InwqTCZccErp6nE8uRdKDDT%2FYsj5gXZ3lFHoWd9vLT6BmWfp3GHHRjw2WT3oqgCDqsY8B5CTHl0J4uTLhbB5c1L0O%2F6pyp3xqbGdc8JnhG3ll%2BpzTTq5zi9KsDrmMYJTMJS3%2F9IGOqUB0vr1qeSs24enRiUO%2BP742m2MV26C2CVC7xWq6lXl3LgBHZ4yBN4nXFzoyC0vB935MlgrORIvlbE84WWWofmyT7s6W3gCrLS6j3rpxHwA8LzkE1AOWPGW1HUlApkcrSoEJrZvLVaWYGSF%2ByYVMYSQHLu%2BIwzFM3I91cppk%2FbfLVhl6U6guNdNuErwItY5PsvCbMdATria3zOMz2zD%2FRkryNxPwITf&X-Amz-Signature=822b4423a240978d69a43a846ef13886ca35981bcb4526d383e8571603e4ebcb&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e943d4ec-3998-492e-bedc-6d73e20ad71d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJONFXAK%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCUU%2FsmgSmmA79vKAq2uPaSoZBvEhmupX7AzsFFbINgsgIgeOYT2%2FUl7GodgHiusoKPqEmLV6ajwH5Bz4LPAquoHCIqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDELdNWKmQzZP%2BflUQyrcAy9ethytFRz5ttEL4bTztKXb7s%2FzKryFYnwIN%2Bb0pU3Bhkk4ykC%2FLkqmh5uM7c7q1YFTnumR5JUwojDrjVXv%2BjuRNVfJiWv4kFDt7i0zF7Zhj0tdh1SaLHBd4hjjHSV8tfyULUlsID6Fp8Jh9hKVC5E6Tof6px8t9aRpEoUWx5nI1NSlCvIDom%2BSR842Nuo2v542wROpH12x7qRebmsG5Y%2FuM91o02ERP%2BF1Ho9QRkRwqs%2BPZq%2BXC2qTNyer3kjV9L5zjsr%2BFCVz20nJONUM%2BE9ycCMB6HXPN0ckr5nJ2GMyA0vE0dINqiBmjUno6ems6Tz5TFtWtwYGmHgMq8wCio7vYtR38caYSWy7WKTm%2BMcnmFfntZumGUY30xwqIC%2BNwwHTnR9mUClhvDOneYkHJ0Ye54WqJHnaVbB0wzPw%2Fqr2%2BI84Vac7vG4xWjcbv8n7b%2Bg8eJZn65xeAK1DTatatXlhynhnr39%2BLlF%2FJYEXOGRpj5exvWXo2KhhcbR6InwqTCZccErp6nE8uRdKDDT%2FYsj5gXZ3lFHoWd9vLT6BmWfp3GHHRjw2WT3oqgCDqsY8B5CTHl0J4uTLhbB5c1L0O%2F6pyp3xqbGdc8JnhG3ll%2BpzTTq5zi9KsDrmMYJTMJS3%2F9IGOqUB0vr1qeSs24enRiUO%2BP742m2MV26C2CVC7xWq6lXl3LgBHZ4yBN4nXFzoyC0vB935MlgrORIvlbE84WWWofmyT7s6W3gCrLS6j3rpxHwA8LzkE1AOWPGW1HUlApkcrSoEJrZvLVaWYGSF%2ByYVMYSQHLu%2BIwzFM3I91cppk%2FbfLVhl6U6guNdNuErwItY5PsvCbMdATria3zOMz2zD%2FRkryNxPwITf&X-Amz-Signature=679b4339ebd5d0f8c1072f0b1272fbd798ae21fdf026f8f86b758818db7047d8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b9e6457e-217e-45d0-9c89-ade0029e44ab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJONFXAK%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCUU%2FsmgSmmA79vKAq2uPaSoZBvEhmupX7AzsFFbINgsgIgeOYT2%2FUl7GodgHiusoKPqEmLV6ajwH5Bz4LPAquoHCIqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDELdNWKmQzZP%2BflUQyrcAy9ethytFRz5ttEL4bTztKXb7s%2FzKryFYnwIN%2Bb0pU3Bhkk4ykC%2FLkqmh5uM7c7q1YFTnumR5JUwojDrjVXv%2BjuRNVfJiWv4kFDt7i0zF7Zhj0tdh1SaLHBd4hjjHSV8tfyULUlsID6Fp8Jh9hKVC5E6Tof6px8t9aRpEoUWx5nI1NSlCvIDom%2BSR842Nuo2v542wROpH12x7qRebmsG5Y%2FuM91o02ERP%2BF1Ho9QRkRwqs%2BPZq%2BXC2qTNyer3kjV9L5zjsr%2BFCVz20nJONUM%2BE9ycCMB6HXPN0ckr5nJ2GMyA0vE0dINqiBmjUno6ems6Tz5TFtWtwYGmHgMq8wCio7vYtR38caYSWy7WKTm%2BMcnmFfntZumGUY30xwqIC%2BNwwHTnR9mUClhvDOneYkHJ0Ye54WqJHnaVbB0wzPw%2Fqr2%2BI84Vac7vG4xWjcbv8n7b%2Bg8eJZn65xeAK1DTatatXlhynhnr39%2BLlF%2FJYEXOGRpj5exvWXo2KhhcbR6InwqTCZccErp6nE8uRdKDDT%2FYsj5gXZ3lFHoWd9vLT6BmWfp3GHHRjw2WT3oqgCDqsY8B5CTHl0J4uTLhbB5c1L0O%2F6pyp3xqbGdc8JnhG3ll%2BpzTTq5zi9KsDrmMYJTMJS3%2F9IGOqUB0vr1qeSs24enRiUO%2BP742m2MV26C2CVC7xWq6lXl3LgBHZ4yBN4nXFzoyC0vB935MlgrORIvlbE84WWWofmyT7s6W3gCrLS6j3rpxHwA8LzkE1AOWPGW1HUlApkcrSoEJrZvLVaWYGSF%2ByYVMYSQHLu%2BIwzFM3I91cppk%2FbfLVhl6U6guNdNuErwItY5PsvCbMdATria3zOMz2zD%2FRkryNxPwITf&X-Amz-Signature=4bf1f89a4ed473d224ebf12e4b0d3a19ccf61c51c66e234b67ef848a3c9c6673&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

然后 application 这是我们自己定义的三个数据，是不是分别是 hostname 主机名称跟 application name 然后这里面 date 表示数据了，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/60b0abde-1e70-49e7-b217-fcdac49f1ddb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJONFXAK%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCUU%2FsmgSmmA79vKAq2uPaSoZBvEhmupX7AzsFFbINgsgIgeOYT2%2FUl7GodgHiusoKPqEmLV6ajwH5Bz4LPAquoHCIqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDELdNWKmQzZP%2BflUQyrcAy9ethytFRz5ttEL4bTztKXb7s%2FzKryFYnwIN%2Bb0pU3Bhkk4ykC%2FLkqmh5uM7c7q1YFTnumR5JUwojDrjVXv%2BjuRNVfJiWv4kFDt7i0zF7Zhj0tdh1SaLHBd4hjjHSV8tfyULUlsID6Fp8Jh9hKVC5E6Tof6px8t9aRpEoUWx5nI1NSlCvIDom%2BSR842Nuo2v542wROpH12x7qRebmsG5Y%2FuM91o02ERP%2BF1Ho9QRkRwqs%2BPZq%2BXC2qTNyer3kjV9L5zjsr%2BFCVz20nJONUM%2BE9ycCMB6HXPN0ckr5nJ2GMyA0vE0dINqiBmjUno6ems6Tz5TFtWtwYGmHgMq8wCio7vYtR38caYSWy7WKTm%2BMcnmFfntZumGUY30xwqIC%2BNwwHTnR9mUClhvDOneYkHJ0Ye54WqJHnaVbB0wzPw%2Fqr2%2BI84Vac7vG4xWjcbv8n7b%2Bg8eJZn65xeAK1DTatatXlhynhnr39%2BLlF%2FJYEXOGRpj5exvWXo2KhhcbR6InwqTCZccErp6nE8uRdKDDT%2FYsj5gXZ3lFHoWd9vLT6BmWfp3GHHRjw2WT3oqgCDqsY8B5CTHl0J4uTLhbB5c1L0O%2F6pyp3xqbGdc8JnhG3ll%2BpzTTq5zi9KsDrmMYJTMJS3%2F9IGOqUB0vr1qeSs24enRiUO%2BP742m2MV26C2CVC7xWq6lXl3LgBHZ4yBN4nXFzoyC0vB935MlgrORIvlbE84WWWofmyT7s6W3gCrLS6j3rpxHwA8LzkE1AOWPGW1HUlApkcrSoEJrZvLVaWYGSF%2ByYVMYSQHLu%2BIwzFM3I91cppk%2FbfLVhl6U6guNdNuErwItY5PsvCbMdATria3zOMz2zD%2FRkryNxPwITf&X-Amz-Signature=eb0272a45412d1c447c4a625cae2545fa22742d8e0e1575b082a2844918c7d65&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

是不是只要数据就行，就只哪怕你里边传的是 none 是空，那我都认这个 nospace 就是说里边不能为空，我就这个表达式就不起的作用过滤不了，然后再往下看还是 date 就是 location 然后再往下看就是 message infomessage info 就是实际的数据，对不对？实际的就是这一块。比如说我们对应的就是这个杠 M 叫做 message info, location 是什么呢？ 

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/44537c8a-b54b-4308-9bf7-fcf7cf140ca3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJONFXAK%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCUU%2FsmgSmmA79vKAq2uPaSoZBvEhmupX7AzsFFbINgsgIgeOYT2%2FUl7GodgHiusoKPqEmLV6ajwH5Bz4LPAquoHCIqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDELdNWKmQzZP%2BflUQyrcAy9ethytFRz5ttEL4bTztKXb7s%2FzKryFYnwIN%2Bb0pU3Bhkk4ykC%2FLkqmh5uM7c7q1YFTnumR5JUwojDrjVXv%2BjuRNVfJiWv4kFDt7i0zF7Zhj0tdh1SaLHBd4hjjHSV8tfyULUlsID6Fp8Jh9hKVC5E6Tof6px8t9aRpEoUWx5nI1NSlCvIDom%2BSR842Nuo2v542wROpH12x7qRebmsG5Y%2FuM91o02ERP%2BF1Ho9QRkRwqs%2BPZq%2BXC2qTNyer3kjV9L5zjsr%2BFCVz20nJONUM%2BE9ycCMB6HXPN0ckr5nJ2GMyA0vE0dINqiBmjUno6ems6Tz5TFtWtwYGmHgMq8wCio7vYtR38caYSWy7WKTm%2BMcnmFfntZumGUY30xwqIC%2BNwwHTnR9mUClhvDOneYkHJ0Ye54WqJHnaVbB0wzPw%2Fqr2%2BI84Vac7vG4xWjcbv8n7b%2Bg8eJZn65xeAK1DTatatXlhynhnr39%2BLlF%2FJYEXOGRpj5exvWXo2KhhcbR6InwqTCZccErp6nE8uRdKDDT%2FYsj5gXZ3lFHoWd9vLT6BmWfp3GHHRjw2WT3oqgCDqsY8B5CTHl0J4uTLhbB5c1L0O%2F6pyp3xqbGdc8JnhG3ll%2BpzTTq5zi9KsDrmMYJTMJS3%2F9IGOqUB0vr1qeSs24enRiUO%2BP742m2MV26C2CVC7xWq6lXl3LgBHZ4yBN4nXFzoyC0vB935MlgrORIvlbE84WWWofmyT7s6W3gCrLS6j3rpxHwA8LzkE1AOWPGW1HUlApkcrSoEJrZvLVaWYGSF%2ByYVMYSQHLu%2BIwzFM3I91cppk%2FbfLVhl6U6guNdNuErwItY5PsvCbMdATria3zOMz2zD%2FRkryNxPwITf&X-Amz-Signature=4966ac48603b002b7c24b716867c609e7ae71bb1ca48b982135e4e5bf7e915fc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

location 就表示的这个 flcm 就这块东西再往下看看见了吗？两个井号，两个井号跟谁对应上了，是不是跟他对应上了？空格。然后这个是转译是不是转译是两个单引号，然后叫做这个 current string 然后 throwable 竖线就是你可以是空的两个字符串，两个单引号字符串，或者空的，你不是空的。里边可能就是一个凯瑞特 string 就是一个异常信息了，我用这种方式就可以去把换行统一的去抓取不到，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/67d1242d-9a1d-4f7a-a4d6-da76a955a102/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJONFXAK%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCUU%2FsmgSmmA79vKAq2uPaSoZBvEhmupX7AzsFFbINgsgIgeOYT2%2FUl7GodgHiusoKPqEmLV6ajwH5Bz4LPAquoHCIqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDELdNWKmQzZP%2BflUQyrcAy9ethytFRz5ttEL4bTztKXb7s%2FzKryFYnwIN%2Bb0pU3Bhkk4ykC%2FLkqmh5uM7c7q1YFTnumR5JUwojDrjVXv%2BjuRNVfJiWv4kFDt7i0zF7Zhj0tdh1SaLHBd4hjjHSV8tfyULUlsID6Fp8Jh9hKVC5E6Tof6px8t9aRpEoUWx5nI1NSlCvIDom%2BSR842Nuo2v542wROpH12x7qRebmsG5Y%2FuM91o02ERP%2BF1Ho9QRkRwqs%2BPZq%2BXC2qTNyer3kjV9L5zjsr%2BFCVz20nJONUM%2BE9ycCMB6HXPN0ckr5nJ2GMyA0vE0dINqiBmjUno6ems6Tz5TFtWtwYGmHgMq8wCio7vYtR38caYSWy7WKTm%2BMcnmFfntZumGUY30xwqIC%2BNwwHTnR9mUClhvDOneYkHJ0Ye54WqJHnaVbB0wzPw%2Fqr2%2BI84Vac7vG4xWjcbv8n7b%2Bg8eJZn65xeAK1DTatatXlhynhnr39%2BLlF%2FJYEXOGRpj5exvWXo2KhhcbR6InwqTCZccErp6nE8uRdKDDT%2FYsj5gXZ3lFHoWd9vLT6BmWfp3GHHRjw2WT3oqgCDqsY8B5CTHl0J4uTLhbB5c1L0O%2F6pyp3xqbGdc8JnhG3ll%2BpzTTq5zi9KsDrmMYJTMJS3%2F9IGOqUB0vr1qeSs24enRiUO%2BP742m2MV26C2CVC7xWq6lXl3LgBHZ4yBN4nXFzoyC0vB935MlgrORIvlbE84WWWofmyT7s6W3gCrLS6j3rpxHwA8LzkE1AOWPGW1HUlApkcrSoEJrZvLVaWYGSF%2ByYVMYSQHLu%2BIwzFM3I91cppk%2FbfLVhl6U6guNdNuErwItY5PsvCbMdATria3zOMz2zD%2FRkryNxPwITf&X-Amz-Signature=989c2866a078cb40f5b2817761723524e93dcd842885dcc04b7c9d02a63d5368&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

这个就是一个正则的匹配。 OK 那其实现在我们已经把我们的这个对应的我们的日志格式跟我们的 logo stands 过滤的这个表达式已经写好，写好了之后，那么你就可以去对它进行一个过滤了，去做一个升级收集了。那 group 里边内容就是说把所有 App 杠 log 里边收集过来的数据，只要匹配我这个表达式的，那我就可以去收集上来。就是这个意思。同理 arrow log 也是一样的，它的格式一样，看见了吗也收集上来。

```java
## multiline 插件也可以用于其他类似的堆栈式信息，比如 linux 的内核日志。
input {
  kafka {
    ## app-log-服务名称
    topics_pattern => "app-log-.*"
    bootstrap_servers => "192.168.11.51:9092"
	codec => json
	consumer_threads => 1	## 增加consumer的并行消费线程数
	decorate_events => true
    #auto_offset_rest => "latest"
	group_id => "app-log-group"
   }
   
   kafka {
    ## error-log-服务名称
    topics_pattern => "error-log-.*"
    bootstrap_servers => "192.168.11.51:9092"
	codec => json
	consumer_threads => 1
	decorate_events => true
    #auto_offset_rest => "latest"
	group_id => "error-log-group"
   }
   
}

filter {
  
  ## 时区转换
  ruby {
	code => "event.set('index_time',event.timestamp.time.localtime.strftime('%Y.%m.%d'))"
  }

  if "app-log" in [fields][logtopic]{
    grok {
        ## 表达式
        match => ["message", "\[%{NOTSPACE:currentDateTime}\] \[%{NOTSPACE:level}\] \[%{NOTSPACE:thread-id}\] \[%{NOTSPACE:class}\] \[%{DATA:hostName}\] \[%{DATA:ip}\] \[%{DATA:applicationName}\] \[%{DATA:location}\] \[%{DATA:messageInfo}\] ## (\'\'|%{QUOTEDSTRING:throwable})"]
    }
  }

  if "error-log" in [fields][logtopic]{
    grok {
        ## 表达式
        match => ["message", "\[%{NOTSPACE:currentDateTime}\] \[%{NOTSPACE:level}\] \[%{NOTSPACE:thread-id}\] \[%{NOTSPACE:class}\] \[%{DATA:hostName}\] \[%{DATA:ip}\] \[%{DATA:applicationName}\] \[%{DATA:location}\] \[%{DATA:messageInfo}\] ## (\'\'|%{QUOTEDSTRING:throwable})"]
    }
  }
  
}

## 测试输出到控制台：
output {
  stdout { codec => rubydebug }
}


## elasticsearch：
output {

  if "app-log" in [fields][logtopic]{
	## es插件
	elasticsearch {
  	    # es服务地址
        hosts => ["192.168.11.35:9200"]
        # 用户名密码      
        user => "elastic"
        password => "123456"
        ## 索引名，+ 号开头的，就会自动认为后面是时间格式：
        ## javalog-app-service-2019.01.23 
        index => "app-log-%{[fields][logbiz]}-%{index_time}"
        # 是否嗅探集群ip：一般设置true；http://192.168.11.35:9200/_nodes/http?pretty
        # 通过嗅探机制进行es集群负载均衡发日志消息
        sniffing => true
        # logstash默认自带一个mapping模板，进行模板覆盖
        template_overwrite => true
    } 
  }
  
  if "error-log" in [fields][logtopic]{
	elasticsearch {
        hosts => ["192.168.11.35:9200"]    
        user => "elastic"
        password => "123456"
        index => "error-log-%{[fields][logbiz]}-%{index_time}"
        sniffing => true
        template_overwrite => true
    } 
  }
}
```

然后最后老师这里边，其实我把它 output 到 elasticsearch 上，就是我们 think 的数据源，但是我们现在可以不着急，因为 elastic search 我们现在还没有起，那我们现在可以暂时的是干什么呢？去把它输出到控制台，让大家看一下效果。 output 标准输出是不是 stand out 那就是 codeC 我们用 rubydebug 的方式去把它打到控制台就可以了。好了，那这样的话我们现在就可以来起一下我们的 love 赛事了。起之前注意，因为我们现在还没有对应的什么，对应的我们的这个 elastic search 所以说在这里我们要把后面的内容暂时先注释掉，这里边我就用最笨的方法去注释了。其实这些东西都是很固定的。就是说 E LK 其实并不难很简单，但是其实对应着你要多学一些什么呢？多学一些你自己可能之前没玩过的一些语法格式。那其实这个就跟你学完了 Java 之后学其他语言一样，就是它都是大同小异，都是相通的。所以说小伙伴们也不要有什么心理的压力，很简单。 OK 那现在我已经把它注释掉了，现在我们只保留一个 output 看见了。 output 那也就是说所有数据只要过滤出来的，那我会把它输出到我们的控制台上标准输出，然后我们去 X 去把它保存一下。


那接下来的事情无非就是启动我们的 log 赛事，那启动命令很简单，老师在这里已经给出来了，在我们的 logstash 里边，我们把这个 copy 一下就可以了。 nohope 就是后台启动是不是？然后对应的你的 USR 杠 local 然后 log 三十六点六点零杠 bin 然后到下面这是 log 30 启动的脚本，

 F 指定他要按照什么方式去对应的启动。就是按照我们刚才给大家讲的那个配置文件，是不是这个配置文件就是 script 然后后面的 log stash 杠 script.config 好，我们去启动它。那注意启动它的时候会很慢，基本上起来可能需要花两分钟左右。


为什么起来要花这么长时间呢？无非是因为它是怎么说，它有一些初始化的工作。那这个工作其实我不想把它这个暂停，我们一起来耐心的去等一下这个 loss 赛事启动的过程。它里边如果说抛一些错或者是出现一些提示，我们能及时的感知到这个其实是很重要的。有的时候我们的 loss 再是起不来，你可能要排查问题的时候，你只能通过它的启动日志或者它的这个 L 日志来看，它这个会比较耗时。当然它启动起来之后，因为我们卡夫卡利已经有数据了，所以说它启动起来之后直接就会把数据消费到就会打印到控制台，它打印到控制台的颜色是黄色的，其实大家可以耐心去等一等。在这里我们就稍微休息一下会儿来耐心的去等一下它的启动。当然也是可能跟我的这个服务器性能有关。 frame 我看一下。 GPS 它已经停掉了，它已经这个刚才我们看到它已经退出了。那其实我们可以看看它为什么退出了，我们直接去看一看它里面有个 no hop 文件，我们去看一下这个 no hook 这里边说最终有一个什么 successful 但是他还服务还是停掉了。


好，它里边说 no config fails found in pass 这个下面他没有去找到这个配置文件吗，就是 log stash 杠点 config 是不是在 script 下，我是不是没有写错了？ script 写错了，看见了吧。我见的这个东西写错了，这个你看很致命，看见了吧这个也很关键，你必须要看到它的启动日志，你必须要看它的这个报错日志才行，要不然你真的是找半天。


script 我写的是 script way 这字没法拼了是吧。好，我们去 MV script 然后把它改成 script 好搞定。像这些就即使是出错，大家也是有迹可循，看他的这个 no hop 他的那个日志就好。好，我们再来重新洗一下，耐心等待一下它启动的热起来的时候是比较慢的。其实你也可以去看一看它的内存的使用情况。你看我现在是两个 G 它现在已经 use 了对不对？已经 use 了，基本上 feel 很少了，是不是所以说它是比较吃内存的你看一会儿，我的 swipe 区如果有那什么了，如果 use 的，这个系统就是卡了，就不能再卡了你看慢慢的就吃很多很多的这个资源。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/c8c82732-f214-417c-93b9-67954046981c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJONFXAK%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCUU%2FsmgSmmA79vKAq2uPaSoZBvEhmupX7AzsFFbINgsgIgeOYT2%2FUl7GodgHiusoKPqEmLV6ajwH5Bz4LPAquoHCIqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDELdNWKmQzZP%2BflUQyrcAy9ethytFRz5ttEL4bTztKXb7s%2FzKryFYnwIN%2Bb0pU3Bhkk4ykC%2FLkqmh5uM7c7q1YFTnumR5JUwojDrjVXv%2BjuRNVfJiWv4kFDt7i0zF7Zhj0tdh1SaLHBd4hjjHSV8tfyULUlsID6Fp8Jh9hKVC5E6Tof6px8t9aRpEoUWx5nI1NSlCvIDom%2BSR842Nuo2v542wROpH12x7qRebmsG5Y%2FuM91o02ERP%2BF1Ho9QRkRwqs%2BPZq%2BXC2qTNyer3kjV9L5zjsr%2BFCVz20nJONUM%2BE9ycCMB6HXPN0ckr5nJ2GMyA0vE0dINqiBmjUno6ems6Tz5TFtWtwYGmHgMq8wCio7vYtR38caYSWy7WKTm%2BMcnmFfntZumGUY30xwqIC%2BNwwHTnR9mUClhvDOneYkHJ0Ye54WqJHnaVbB0wzPw%2Fqr2%2BI84Vac7vG4xWjcbv8n7b%2Bg8eJZn65xeAK1DTatatXlhynhnr39%2BLlF%2FJYEXOGRpj5exvWXo2KhhcbR6InwqTCZccErp6nE8uRdKDDT%2FYsj5gXZ3lFHoWd9vLT6BmWfp3GHHRjw2WT3oqgCDqsY8B5CTHl0J4uTLhbB5c1L0O%2F6pyp3xqbGdc8JnhG3ll%2BpzTTq5zi9KsDrmMYJTMJS3%2F9IGOqUB0vr1qeSs24enRiUO%2BP742m2MV26C2CVC7xWq6lXl3LgBHZ4yBN4nXFzoyC0vB935MlgrORIvlbE84WWWofmyT7s6W3gCrLS6j3rpxHwA8LzkE1AOWPGW1HUlApkcrSoEJrZvLVaWYGSF%2ByYVMYSQHLu%2BIwzFM3I91cppk%2FbfLVhl6U6guNdNuErwItY5PsvCbMdATria3zOMz2zD%2FRkryNxPwITf&X-Amz-Signature=9532697a44bdfd70bd1f533cc26d2824f9eb8519c2134f6ac48393929fad5f2e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

所以说你想用 logstash 你一定要对应的你的资源要足够。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/c740daf2-3086-4bf1-b421-041c86b7d059/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJONFXAK%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCUU%2FsmgSmmA79vKAq2uPaSoZBvEhmupX7AzsFFbINgsgIgeOYT2%2FUl7GodgHiusoKPqEmLV6ajwH5Bz4LPAquoHCIqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDELdNWKmQzZP%2BflUQyrcAy9ethytFRz5ttEL4bTztKXb7s%2FzKryFYnwIN%2Bb0pU3Bhkk4ykC%2FLkqmh5uM7c7q1YFTnumR5JUwojDrjVXv%2BjuRNVfJiWv4kFDt7i0zF7Zhj0tdh1SaLHBd4hjjHSV8tfyULUlsID6Fp8Jh9hKVC5E6Tof6px8t9aRpEoUWx5nI1NSlCvIDom%2BSR842Nuo2v542wROpH12x7qRebmsG5Y%2FuM91o02ERP%2BF1Ho9QRkRwqs%2BPZq%2BXC2qTNyer3kjV9L5zjsr%2BFCVz20nJONUM%2BE9ycCMB6HXPN0ckr5nJ2GMyA0vE0dINqiBmjUno6ems6Tz5TFtWtwYGmHgMq8wCio7vYtR38caYSWy7WKTm%2BMcnmFfntZumGUY30xwqIC%2BNwwHTnR9mUClhvDOneYkHJ0Ye54WqJHnaVbB0wzPw%2Fqr2%2BI84Vac7vG4xWjcbv8n7b%2Bg8eJZn65xeAK1DTatatXlhynhnr39%2BLlF%2FJYEXOGRpj5exvWXo2KhhcbR6InwqTCZccErp6nE8uRdKDDT%2FYsj5gXZ3lFHoWd9vLT6BmWfp3GHHRjw2WT3oqgCDqsY8B5CTHl0J4uTLhbB5c1L0O%2F6pyp3xqbGdc8JnhG3ll%2BpzTTq5zi9KsDrmMYJTMJS3%2F9IGOqUB0vr1qeSs24enRiUO%2BP742m2MV26C2CVC7xWq6lXl3LgBHZ4yBN4nXFzoyC0vB935MlgrORIvlbE84WWWofmyT7s6W3gCrLS6j3rpxHwA8LzkE1AOWPGW1HUlApkcrSoEJrZvLVaWYGSF%2ByYVMYSQHLu%2BIwzFM3I91cppk%2FbfLVhl6U6guNdNuErwItY5PsvCbMdATria3zOMz2zD%2FRkryNxPwITf&X-Amz-Signature=28c590677b9d8626e8a8bab4a4ad433597f908e66d313094ac49380a1264a144&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


我现在做测试，两个 G 的服务器它基本上都撑不起来，就是它启动的会很慢。你看现在我的 feel 就是 99 很少了，98它如果说没有太往下降，就证明他正在起着，基本上稳定了。稳定了之后就说明他一会儿马上就起来了。还往下降，那还再往回升了，这个我把它退出，要等他真的是稍等很久。


GPS 一下，看你的进程，你看我的 loss 赛事进程还在，就证明他还在起着，所以这个过程是一个比较漫长的。 OK 我可能已经把这个 love 赛事启动起来了，我先把它 cue 掉。这个过程 49 我先把它 cue 掉。好 Q 掉了之后我们再重启一下。因为我刚才好像忘了一个事情来看一下。 nohope 我们就不要 no hope 就是后台启动的话你看不到前台输出的日志，就我已经习惯了去打这个事情。好，然后我们就正常的去启动，就是直接执行它的这个脚本，然后杠 F 指定配置文件，这样去起，你会看到他的那个日志输出的过程。好，同学们请看他现在已经起来了，你看他现在已经就有个 warning 其实无所谓，就是 pipeline 4 点 yml 没有去做 because module command 然后这没关系，然后 starting log says 6.0，它慢慢的去启动。然后同学们请看他这里边有一些异常，可能是老师之前做这个实验的时候有一些 topic 他没有找到这个不用去关心。你看他首先去连谁连我们的卡夫卡，因为他现在是作为一个卡夫卡的，什么呢？一个 consumer 消费者。然然后我们再往下看，他现在已经起来了，他现在已经起来了，已经起来了。


同学们，那现在我们为什么没有收到数据呢？这个原因很简单，因为刚才我们其实把它作为一个后台启动了，对不对？所以说我们看不到那个数据，现在怎么办呢？那我们这个数据到底消没消费，我能不能感知到，很简单，还记得吗？你就看卡夫卡它对应订阅的那个 topic 主题就可以了。


老师之前给大家，我之前给大家肯定是讲了对应的那个卡夫卡的这个 topic 应该怎么去看对吧？我们 CD 点点，然后 CD 到 bin 目录下对不对？然后我们去 history 去找，我们随便找一个主题去订阅一下，在这里是不是在这里就是我们订阅的那个组了。我们订阅那个我们的组叫什么名字？古鲁婆，我们来看一看我们的 group 叫什么？我们的 group 一个叫做 App log group 还有一个叫做 error 杠 log 杠 group 是不是？这两个组我们随便来看一个组来这粘过来。你说它的这个消费进度你看见了吗？他的 offset 是有的看见了吗？他 219 条，219条是不是？然后这个是 19 条，因为我之前做测试，就是这个组可能也订阅了其他的 topic 那我们只关注我们自己的这个叫做 App 杠 log 杠 collector 它的 partition 就一个它 offset 是19。对不对？那这个是老师历史的一些东西，我们一会可以把它干掉。那我们就看这个 19 条，它的 last offset 已经发生改变了，是不是它没有延迟，就证明之前肯定消费过。那其实我们再可以看再换一个换一个什么呢？换一个 lerror log 杠不如。所以说来看一下这个组。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/51fdf96b-39db-4c66-9099-36738af0f768/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJONFXAK%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCUU%2FsmgSmmA79vKAq2uPaSoZBvEhmupX7AzsFFbINgsgIgeOYT2%2FUl7GodgHiusoKPqEmLV6ajwH5Bz4LPAquoHCIqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDELdNWKmQzZP%2BflUQyrcAy9ethytFRz5ttEL4bTztKXb7s%2FzKryFYnwIN%2Bb0pU3Bhkk4ykC%2FLkqmh5uM7c7q1YFTnumR5JUwojDrjVXv%2BjuRNVfJiWv4kFDt7i0zF7Zhj0tdh1SaLHBd4hjjHSV8tfyULUlsID6Fp8Jh9hKVC5E6Tof6px8t9aRpEoUWx5nI1NSlCvIDom%2BSR842Nuo2v542wROpH12x7qRebmsG5Y%2FuM91o02ERP%2BF1Ho9QRkRwqs%2BPZq%2BXC2qTNyer3kjV9L5zjsr%2BFCVz20nJONUM%2BE9ycCMB6HXPN0ckr5nJ2GMyA0vE0dINqiBmjUno6ems6Tz5TFtWtwYGmHgMq8wCio7vYtR38caYSWy7WKTm%2BMcnmFfntZumGUY30xwqIC%2BNwwHTnR9mUClhvDOneYkHJ0Ye54WqJHnaVbB0wzPw%2Fqr2%2BI84Vac7vG4xWjcbv8n7b%2Bg8eJZn65xeAK1DTatatXlhynhnr39%2BLlF%2FJYEXOGRpj5exvWXo2KhhcbR6InwqTCZccErp6nE8uRdKDDT%2FYsj5gXZ3lFHoWd9vLT6BmWfp3GHHRjw2WT3oqgCDqsY8B5CTHl0J4uTLhbB5c1L0O%2F6pyp3xqbGdc8JnhG3ll%2BpzTTq5zi9KsDrmMYJTMJS3%2F9IGOqUB0vr1qeSs24enRiUO%2BP742m2MV26C2CVC7xWq6lXl3LgBHZ4yBN4nXFzoyC0vB935MlgrORIvlbE84WWWofmyT7s6W3gCrLS6j3rpxHwA8LzkE1AOWPGW1HUlApkcrSoEJrZvLVaWYGSF%2ByYVMYSQHLu%2BIwzFM3I91cppk%2FbfLVhl6U6guNdNuErwItY5PsvCbMdATria3zOMz2zD%2FRkryNxPwITf&X-Amz-Signature=c6caaa44f770b601a5bd7fcc6bf32692eedea7cbece17a4cd16bdd65800ba0e2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


这个组里边也有 collector 是不是它有三条消息，是不是三条消息？无非就是一个 warning 的，还有一个 L 的，然后还有一个是算数异常的 L 的我猜想是这样的，并且都消费了。看见了吧。 OK 那我们推测是没问题的。那接下来我们就来再次验证一下怎么验证？很简单，我们直接通过控制台来 index 回车敲一下看见了吗？同学们，我们的 lock 赛事已经有数据了，看见了。已经有数据了，那对应着这里面打了三条日志，那我们这里边到底有什么样的数据呢？我们来看一下。
首先一个大括号，这里边的内容有哪些？我们来看一看。那这是我的服务器名称，当前的这台服务器。然后我是从 31 过来的数据，是不是？所以说它的这个服务器的地址都是从 31 过来的 name 以及 host name 我的 class 是不是是 com.bfx y.controller.web.index controller 没问题，我的 location 是不是？然后还有这些 offset 你不用看，这是卡夫卡的，我审也不用看，然后 IP 是不是 IP 是 31 吧，我们刚才通过 31 打的日志对吧，继续往下看。


message info 我是一条 warning 日志，它这个先后顺序这个你没法保障，因为我们这里边输了三条日志，一个是 info 还有一个是 warning 还有一个是 L 对吧。 OK 我们看到第一条是 warning 没问题。然后这里边 message 就是全量的日志信息，看见了吧。


我是一条 warning 日志，然后它的 level 级别是 warning 然后它的 topic 在哪儿？叫做 App 杠 log 杠 connector 然后它的环境是 DEV 环境，它的 big 就是 log big 是 connect 这个服务，然后它的 file 是不是从哪来的？从这个文件里来的，它的 current 当前时间是不是当前时间？ timestep 它是东巴区会帮你做一个转换。后面我们去从 k8 上看就非常方便了。


应用服务的名称 application name 就是 connector 对吧？这个是我们放到有一些数据是我们放到 mdc 里的，比如说 host nameip 比如说 application name 这些是我们扔到 mdc 里的对吧。然后我们再往下去看 warning 看完了之后，我们看这又一个括号是不是这是什么？我是一条 L 日志看见了吗？对应着 L 日志也有信息，然后再往下看。


第三个括号，这可能有一些之前的日志我们没有那什么，

他可能有一些之前的日志我们没有收集到。再回来的时候，我们看这里边有一个我是一条 info 日志。好OK ，你看这还有好多数据，这可能是之前的数据，它肯定不会说重复。有一些之前的数据打过来了没关系。 OK 那我们打几个空格，是不是我们再次的去做一件事情？再次去访问浏览器，访问 lerr 回车 err 打完了之后我们耐心等已经有了，是不是？我们看这里输出了 L 的一条日志没问题。然后我们回过头来边看这里边是吧来看这么多的东西都是啥？是不是都是异常信息看见了吧，这个空格之后是我们输出的内容。这个就是抛了一个异常，这个 throba 是不是它是 arithmetic exception 算术异常？这是我们之前看到的是不是？往后这好长是不是？然后 message Infra 就是你的算术异常。


你的描述这个还记得吗？小伙伴们，这个就是我们之前这个 controller 里边打了这个描述，就是他然后再往下看是不是？ OK 那这里边还有一条记录，还有一条记录， arithmetic exception 算数异常。那有同学说问了老师，那现在我这怎么能收到两条呢？是不是收到两条，我们现在先不用关注这个事情，我们现在只需要知道我们的 log stash 已经能够上报数据，对不对？已经能够收到 Kafka 的数据了，就证明我们的消费者没问题。至于说为什么反映出来是两条问题呢？那这个可能是由于我们自己的配置什么的相关等等造成一些问题。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/919f5e75-938e-410e-b262-37b1e30f898c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QJONFXAK%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225329Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCUU%2FsmgSmmA79vKAq2uPaSoZBvEhmupX7AzsFFbINgsgIgeOYT2%2FUl7GodgHiusoKPqEmLV6ajwH5Bz4LPAquoHCIqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDELdNWKmQzZP%2BflUQyrcAy9ethytFRz5ttEL4bTztKXb7s%2FzKryFYnwIN%2Bb0pU3Bhkk4ykC%2FLkqmh5uM7c7q1YFTnumR5JUwojDrjVXv%2BjuRNVfJiWv4kFDt7i0zF7Zhj0tdh1SaLHBd4hjjHSV8tfyULUlsID6Fp8Jh9hKVC5E6Tof6px8t9aRpEoUWx5nI1NSlCvIDom%2BSR842Nuo2v542wROpH12x7qRebmsG5Y%2FuM91o02ERP%2BF1Ho9QRkRwqs%2BPZq%2BXC2qTNyer3kjV9L5zjsr%2BFCVz20nJONUM%2BE9ycCMB6HXPN0ckr5nJ2GMyA0vE0dINqiBmjUno6ems6Tz5TFtWtwYGmHgMq8wCio7vYtR38caYSWy7WKTm%2BMcnmFfntZumGUY30xwqIC%2BNwwHTnR9mUClhvDOneYkHJ0Ye54WqJHnaVbB0wzPw%2Fqr2%2BI84Vac7vG4xWjcbv8n7b%2Bg8eJZn65xeAK1DTatatXlhynhnr39%2BLlF%2FJYEXOGRpj5exvWXo2KhhcbR6InwqTCZccErp6nE8uRdKDDT%2FYsj5gXZ3lFHoWd9vLT6BmWfp3GHHRjw2WT3oqgCDqsY8B5CTHl0J4uTLhbB5c1L0O%2F6pyp3xqbGdc8JnhG3ll%2BpzTTq5zi9KsDrmMYJTMJS3%2F9IGOqUB0vr1qeSs24enRiUO%2BP742m2MV26C2CVC7xWq6lXl3LgBHZ4yBN4nXFzoyC0vB935MlgrORIvlbE84WWWofmyT7s6W3gCrLS6j3rpxHwA8LzkE1AOWPGW1HUlApkcrSoEJrZvLVaWYGSF%2ByYVMYSQHLu%2BIwzFM3I91cppk%2FbfLVhl6U6guNdNuErwItY5PsvCbMdATria3zOMz2zD%2FRkryNxPwITf&X-Amz-Signature=472c7638b19ee0f7f2f65ec9324f486124ce0508fa792375c426413ffd34612b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

后面我们来排查一下，我们来排查一下。然后我们把它接到我们的 elastic search 上。那这个时候你通过 elastic search 你就知道它到底是一条还是两条了。 OK 接下来我现在可以把它停掉了。我摁 ctrl C 我摁 ctrl C 的话，因为我的程序是前台启动的，所以说我摁 ctrl C 我对应的 GPS 你看我的 logstash 服务就已经停掉了，然后我们 CD 到 script 下，然后我们去 vam 我们的 lost config 我们来看一看。


为什么会出现这种情况？我们现在一个拦截的是 App 杠 log 杠星，这是没问题的。还有一个是拦截的，就是订阅的是 L 刚 log 到 C 对吧，然后一个是 L 刚 log group 还有一个是 App 纲 log group 然后我们的 group 表达式也写的没问题。接下来我们的 output 也没问题，就是我要把它输出，我把它输出到控台。那有两条的原因是什么呢？这里边你要排查问题就很简单了，你确定我们不是 34 这台服务器上配错了，那就是31。我们来看一看31。 31 这台服务器它的日志只记录了一次，这是没问题的。


所以说为什么是两条？在这里我留一个小悬念，我们下节课去配合 elastic search 跟大家把这个事情来看一看到底是不是两条，还是说我们套件出现一些小的问题。 OK 这节课主要让大家看到了这个 logstash 他们这对于日志的这么一个输出，我们是把它输出到控台上的。感谢小。



---
title: 3-4 从架构角度分析负载均衡策略的适用场景
---

# 3-4 从架构角度分析负载均衡策略的适用场景

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/c11e110a-064b-44d3-9641-34550df05942/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5PUEFTI%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFKIpHrKu8nmcJl7g2nGwWLiyrO1gGLwRMpE5kZX%2F27UAiEAspq%2FbTTUdt%2FMlrZSaKtqrpVgiR4iboKNaxtKIL%2BYRcMqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDML0eEa2%2BYShwqq0JSrcA%2BqyHrvUiZCZluGFdMCt14pNdSdb8v3eXokCdnOioMQhsIDgzkm312x14Gz3KIrwuW0mWTh281xPOWOHfpdiFxKUEU%2B%2F19K0SQn4tko%2FNQ2nMuC9UG%2FQf%2BV%2BIPmEADnBkifD5sk8E5j4%2FRPpyxQ5WIXfOEgNIKtLYUET1dZS6dW4tuMmjSCj98KkwcMnopuPqca1tFs%2FxKLRizJpMEE0c2pe3kOy0ZCQSQHHXsj549wCs3JlN20mdSEN0AkM1vqZjxYDXD%2BngeW0RqIx0K7vU5MGyZ72y2oU8WAAkPuhwN2xW03478gcmeLYJHi8ef%2B4mvTqZXhQQi%2F8oE6nE4JDEc9P3NEJ8sRxWoINOrL7IwF3S3KpaRFM3uSpmYYHtm4hWLaGpWlzABLVSs6iLjuZzbQQ3zvziNuyebbbWEs2warOG5fkRMZryMSaA3EBsnv60%2FvslCHO7lelsS69losR2jHm4s4pqtGQNmTtOL01p9THtCByR7JDoIHdENA79KWlYZ4DT41Ml6h%2Fj1SFuNSviYZbVlNGWFpqTYtoF2CDVhUMxL1EH5vUYCMPoeT8HL687U%2B3pDkkpwn3WXsQhQKd2PRQ76RlX5eiySZUL2Yne2Hz1BUcnZugOPLVKTM4MMS6%2F9IGOqUBCCfMK1Sca4bV1TX2hNYrEbfWVU%2BRWHOGZnvtcL7Hh08%2Fox8uggr7YVoGMhpuPxfPWkEbf0%2B921MTkEGtYh6Q519j%2BChbW4nZ9I07AIL2a9pQwPJ1xSQGeE3RMfMRXNd3N7OXY274YJ62o1Lou1QqE5wHE6rsmjMKJitUkC%2F42bqrt1dF2x8eZEfkCC48tAfIeJWNTNgulaQwkzvZznKYwTW%2FFozG&X-Amz-Signature=a10736f935f9842490b14bbd942d9ede2b0075e85449feb2ba49e076907c3ed4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/dafcce89-0b3d-49fd-93e3-8576528a7067/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5PUEFTI%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFKIpHrKu8nmcJl7g2nGwWLiyrO1gGLwRMpE5kZX%2F27UAiEAspq%2FbTTUdt%2FMlrZSaKtqrpVgiR4iboKNaxtKIL%2BYRcMqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDML0eEa2%2BYShwqq0JSrcA%2BqyHrvUiZCZluGFdMCt14pNdSdb8v3eXokCdnOioMQhsIDgzkm312x14Gz3KIrwuW0mWTh281xPOWOHfpdiFxKUEU%2B%2F19K0SQn4tko%2FNQ2nMuC9UG%2FQf%2BV%2BIPmEADnBkifD5sk8E5j4%2FRPpyxQ5WIXfOEgNIKtLYUET1dZS6dW4tuMmjSCj98KkwcMnopuPqca1tFs%2FxKLRizJpMEE0c2pe3kOy0ZCQSQHHXsj549wCs3JlN20mdSEN0AkM1vqZjxYDXD%2BngeW0RqIx0K7vU5MGyZ72y2oU8WAAkPuhwN2xW03478gcmeLYJHi8ef%2B4mvTqZXhQQi%2F8oE6nE4JDEc9P3NEJ8sRxWoINOrL7IwF3S3KpaRFM3uSpmYYHtm4hWLaGpWlzABLVSs6iLjuZzbQQ3zvziNuyebbbWEs2warOG5fkRMZryMSaA3EBsnv60%2FvslCHO7lelsS69losR2jHm4s4pqtGQNmTtOL01p9THtCByR7JDoIHdENA79KWlYZ4DT41Ml6h%2Fj1SFuNSviYZbVlNGWFpqTYtoF2CDVhUMxL1EH5vUYCMPoeT8HL687U%2B3pDkkpwn3WXsQhQKd2PRQ76RlX5eiySZUL2Yne2Hz1BUcnZugOPLVKTM4MMS6%2F9IGOqUBCCfMK1Sca4bV1TX2hNYrEbfWVU%2BRWHOGZnvtcL7Hh08%2Fox8uggr7YVoGMhpuPxfPWkEbf0%2B921MTkEGtYh6Q519j%2BChbW4nZ9I07AIL2a9pQwPJ1xSQGeE3RMfMRXNd3N7OXY274YJ62o1Lou1QqE5wHE6rsmjMKJitUkC%2F42bqrt1dF2x8eZEfkCC48tAfIeJWNTNgulaQwkzvZznKYwTW%2FFozG&X-Amz-Signature=118a77af434ac9295e10e8ed3dcad65fdab9cd4bf2f1b0ed184d16ee4557ea76&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

hello，幕后各位同学们大家好，我是杨半仙，在这一节里咱就从架构的角度来跟同学们去分析一下我们的负载均衡策略的使用的场景。那在这个**过程当中我还会告诉同学们一个事儿，就是说不要相信这些策略，**

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/53afd76c-d975-4683-8d45-be0662222e14/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5PUEFTI%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFKIpHrKu8nmcJl7g2nGwWLiyrO1gGLwRMpE5kZX%2F27UAiEAspq%2FbTTUdt%2FMlrZSaKtqrpVgiR4iboKNaxtKIL%2BYRcMqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDML0eEa2%2BYShwqq0JSrcA%2BqyHrvUiZCZluGFdMCt14pNdSdb8v3eXokCdnOioMQhsIDgzkm312x14Gz3KIrwuW0mWTh281xPOWOHfpdiFxKUEU%2B%2F19K0SQn4tko%2FNQ2nMuC9UG%2FQf%2BV%2BIPmEADnBkifD5sk8E5j4%2FRPpyxQ5WIXfOEgNIKtLYUET1dZS6dW4tuMmjSCj98KkwcMnopuPqca1tFs%2FxKLRizJpMEE0c2pe3kOy0ZCQSQHHXsj549wCs3JlN20mdSEN0AkM1vqZjxYDXD%2BngeW0RqIx0K7vU5MGyZ72y2oU8WAAkPuhwN2xW03478gcmeLYJHi8ef%2B4mvTqZXhQQi%2F8oE6nE4JDEc9P3NEJ8sRxWoINOrL7IwF3S3KpaRFM3uSpmYYHtm4hWLaGpWlzABLVSs6iLjuZzbQQ3zvziNuyebbbWEs2warOG5fkRMZryMSaA3EBsnv60%2FvslCHO7lelsS69losR2jHm4s4pqtGQNmTtOL01p9THtCByR7JDoIHdENA79KWlYZ4DT41Ml6h%2Fj1SFuNSviYZbVlNGWFpqTYtoF2CDVhUMxL1EH5vUYCMPoeT8HL687U%2B3pDkkpwn3WXsQhQKd2PRQ76RlX5eiySZUL2Yne2Hz1BUcnZugOPLVKTM4MMS6%2F9IGOqUBCCfMK1Sca4bV1TX2hNYrEbfWVU%2BRWHOGZnvtcL7Hh08%2Fox8uggr7YVoGMhpuPxfPWkEbf0%2B921MTkEGtYh6Q519j%2BChbW4nZ9I07AIL2a9pQwPJ1xSQGeE3RMfMRXNd3N7OXY274YJ62o1Lou1QqE5wHE6rsmjMKJitUkC%2F42bqrt1dF2x8eZEfkCC48tAfIeJWNTNgulaQwkzvZznKYwTW%2FFozG&X-Amz-Signature=e997d67842b5f295c887a3c613e7cf51f427e2680297c38141074f691772b1f0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

**他们自己鼓吹的侧重的优点，那在真实的超高并发项目当中，这里面可能还有坑需要同学们填。所以作为一个架构师，如果选择技术，我们是靠百度搜索引擎来告诉你答案，它有什么优点，有什么缺点，那等到了线上你这个业务肯定得拉稀**，不信的话我们就从几个点跟同学们来印证一下。那在开始之前我**先跟同学们纠正一个认知上的误区，那就是说负载均衡组件它的定位是什么？很多同学都认为我作为一个负载均衡组件，**

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/66564e33-4461-4488-9c0d-214f13721d3f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5PUEFTI%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFKIpHrKu8nmcJl7g2nGwWLiyrO1gGLwRMpE5kZX%2F27UAiEAspq%2FbTTUdt%2FMlrZSaKtqrpVgiR4iboKNaxtKIL%2BYRcMqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDML0eEa2%2BYShwqq0JSrcA%2BqyHrvUiZCZluGFdMCt14pNdSdb8v3eXokCdnOioMQhsIDgzkm312x14Gz3KIrwuW0mWTh281xPOWOHfpdiFxKUEU%2B%2F19K0SQn4tko%2FNQ2nMuC9UG%2FQf%2BV%2BIPmEADnBkifD5sk8E5j4%2FRPpyxQ5WIXfOEgNIKtLYUET1dZS6dW4tuMmjSCj98KkwcMnopuPqca1tFs%2FxKLRizJpMEE0c2pe3kOy0ZCQSQHHXsj549wCs3JlN20mdSEN0AkM1vqZjxYDXD%2BngeW0RqIx0K7vU5MGyZ72y2oU8WAAkPuhwN2xW03478gcmeLYJHi8ef%2B4mvTqZXhQQi%2F8oE6nE4JDEc9P3NEJ8sRxWoINOrL7IwF3S3KpaRFM3uSpmYYHtm4hWLaGpWlzABLVSs6iLjuZzbQQ3zvziNuyebbbWEs2warOG5fkRMZryMSaA3EBsnv60%2FvslCHO7lelsS69losR2jHm4s4pqtGQNmTtOL01p9THtCByR7JDoIHdENA79KWlYZ4DT41Ml6h%2Fj1SFuNSviYZbVlNGWFpqTYtoF2CDVhUMxL1EH5vUYCMPoeT8HL687U%2B3pDkkpwn3WXsQhQKd2PRQ76RlX5eiySZUL2Yne2Hz1BUcnZugOPLVKTM4MMS6%2F9IGOqUBCCfMK1Sca4bV1TX2hNYrEbfWVU%2BRWHOGZnvtcL7Hh08%2Fox8uggr7YVoGMhpuPxfPWkEbf0%2B921MTkEGtYh6Q519j%2BChbW4nZ9I07AIL2a9pQwPJ1xSQGeE3RMfMRXNd3N7OXY274YJ62o1Lou1QqE5wHE6rsmjMKJitUkC%2F42bqrt1dF2x8eZEfkCC48tAfIeJWNTNgulaQwkzvZznKYwTW%2FFozG&X-Amz-Signature=e09fdb6bc3029e71577060558585e3deb402c5f2daff3c2a1c7e58d670f6b619&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

**我应该既包了负载均衡功能，也要负责异常容错这个功能。因为请求是你发起的，你负责转发的，那么异常容错从你这边做全局的统一处理是最合适不过的。**

**
其实这个认知是不正确的，正所谓术也有专攻，我们做架构设计的时候也是一个样子，作为一个客户端的负载均衡组件，那我们尽量就专注你自己的主营业务好了，我们不要做这种跨界异常容错，**咱交给更适合他的其他组件来做。那我们作为负载均衡组件，就要牢记初心，不忘使命，管好自己的事儿就可以了。


那接下来我们开始对咱的负载均衡策略做一个适用性的讲解，在这之前我们先要跟同学们一起来聊一下，咱的远程访问的这些接口都有哪些类型。那老师这里把所有的接口我大致分为三个类型，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/0730ab8d-a513-450c-b938-ffe6fff4fb9f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5PUEFTI%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFKIpHrKu8nmcJl7g2nGwWLiyrO1gGLwRMpE5kZX%2F27UAiEAspq%2FbTTUdt%2FMlrZSaKtqrpVgiR4iboKNaxtKIL%2BYRcMqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDML0eEa2%2BYShwqq0JSrcA%2BqyHrvUiZCZluGFdMCt14pNdSdb8v3eXokCdnOioMQhsIDgzkm312x14Gz3KIrwuW0mWTh281xPOWOHfpdiFxKUEU%2B%2F19K0SQn4tko%2FNQ2nMuC9UG%2FQf%2BV%2BIPmEADnBkifD5sk8E5j4%2FRPpyxQ5WIXfOEgNIKtLYUET1dZS6dW4tuMmjSCj98KkwcMnopuPqca1tFs%2FxKLRizJpMEE0c2pe3kOy0ZCQSQHHXsj549wCs3JlN20mdSEN0AkM1vqZjxYDXD%2BngeW0RqIx0K7vU5MGyZ72y2oU8WAAkPuhwN2xW03478gcmeLYJHi8ef%2B4mvTqZXhQQi%2F8oE6nE4JDEc9P3NEJ8sRxWoINOrL7IwF3S3KpaRFM3uSpmYYHtm4hWLaGpWlzABLVSs6iLjuZzbQQ3zvziNuyebbbWEs2warOG5fkRMZryMSaA3EBsnv60%2FvslCHO7lelsS69losR2jHm4s4pqtGQNmTtOL01p9THtCByR7JDoIHdENA79KWlYZ4DT41Ml6h%2Fj1SFuNSviYZbVlNGWFpqTYtoF2CDVhUMxL1EH5vUYCMPoeT8HL687U%2B3pDkkpwn3WXsQhQKd2PRQ76RlX5eiySZUL2Yne2Hz1BUcnZugOPLVKTM4MMS6%2F9IGOqUBCCfMK1Sca4bV1TX2hNYrEbfWVU%2BRWHOGZnvtcL7Hh08%2Fox8uggr7YVoGMhpuPxfPWkEbf0%2B921MTkEGtYh6Q519j%2BChbW4nZ9I07AIL2a9pQwPJ1xSQGeE3RMfMRXNd3N7OXY274YJ62o1Lou1QqE5wHE6rsmjMKJitUkC%2F42bqrt1dF2x8eZEfkCC48tAfIeJWNTNgulaQwkzvZznKYwTW%2FFozG&X-Amz-Signature=30194beca88076410c65ec5eb94c213aa10fac2a866a6124e39f36c63965b97c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

第一个连接数敏感性，第二个响应时间敏感型，以及最后一个神经并行。这三个里面我们要重点关注的是哪一个？前两个都好办，我们有套路，能完美解决掉，那依法神经这里就不好使了，前面的招数都不好用了。所以我们在发神经之前，先来看一下怎么解决上面所说的这两个场景。


那这第一个场景就是连接数敏感性，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/d0a4ce26-1ab7-452e-beba-d165722c580b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5PUEFTI%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFKIpHrKu8nmcJl7g2nGwWLiyrO1gGLwRMpE5kZX%2F27UAiEAspq%2FbTTUdt%2FMlrZSaKtqrpVgiR4iboKNaxtKIL%2BYRcMqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDML0eEa2%2BYShwqq0JSrcA%2BqyHrvUiZCZluGFdMCt14pNdSdb8v3eXokCdnOioMQhsIDgzkm312x14Gz3KIrwuW0mWTh281xPOWOHfpdiFxKUEU%2B%2F19K0SQn4tko%2FNQ2nMuC9UG%2FQf%2BV%2BIPmEADnBkifD5sk8E5j4%2FRPpyxQ5WIXfOEgNIKtLYUET1dZS6dW4tuMmjSCj98KkwcMnopuPqca1tFs%2FxKLRizJpMEE0c2pe3kOy0ZCQSQHHXsj549wCs3JlN20mdSEN0AkM1vqZjxYDXD%2BngeW0RqIx0K7vU5MGyZ72y2oU8WAAkPuhwN2xW03478gcmeLYJHi8ef%2B4mvTqZXhQQi%2F8oE6nE4JDEc9P3NEJ8sRxWoINOrL7IwF3S3KpaRFM3uSpmYYHtm4hWLaGpWlzABLVSs6iLjuZzbQQ3zvziNuyebbbWEs2warOG5fkRMZryMSaA3EBsnv60%2FvslCHO7lelsS69losR2jHm4s4pqtGQNmTtOL01p9THtCByR7JDoIHdENA79KWlYZ4DT41Ml6h%2Fj1SFuNSviYZbVlNGWFpqTYtoF2CDVhUMxL1EH5vUYCMPoeT8HL687U%2B3pDkkpwn3WXsQhQKd2PRQ76RlX5eiySZUL2Yne2Hz1BUcnZugOPLVKTM4MMS6%2F9IGOqUBCCfMK1Sca4bV1TX2hNYrEbfWVU%2BRWHOGZnvtcL7Hh08%2Fox8uggr7YVoGMhpuPxfPWkEbf0%2B921MTkEGtYh6Q519j%2BChbW4nZ9I07AIL2a9pQwPJ1xSQGeE3RMfMRXNd3N7OXY274YJ62o1Lou1QqE5wHE6rsmjMKJitUkC%2F42bqrt1dF2x8eZEfkCC48tAfIeJWNTNgulaQwkzvZznKYwTW%2FFozG&X-Amz-Signature=b5e8fd98072c25b15cb732e3d3135a610149dc261b89c8d05c189d64f01ad83e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

我们都知道的一个服务，它的响应时间是一个非常重要的性能指标，那响应时间它这里还会受非常多的因素的制约，你比如说你服务自己的处理时间，还有说你网络开销，网络连接所花费的时间，甚至说你的 GVM 它会发生一个 for GC，那你 GC 过程当中我们有个时间停顿叫做 stop the world，停止时间转动，这都会影响到我最终接口的响应时间。


RT，OK，那咱现在来去思考一个场景，现在咱有一个非常非常轻量级的一个微服务，是一个短平快的接口，它的响应时间非常的快，比如说它的核心业务流程，它的核心组代码只用 5 毫秒以内就可以获取到响应。那么剩下的时间我可能要花费二 20 毫秒来花费在哪？花费在网络连接上的开销里，那么同学们来算一下你接口的业务逻辑实际上只占你整个接口响应时间的大概20%，对吧？只占一个很小的比例。


那前面咱说的响应实践， RT 是个非常重要的性能数字，但是在我们这个场景下，如果我以 RT 作为指标，其实并不能非常客观的知道你当前服务节点的性能数据。为什么呀？因为表达你这个服务器忙闲资源利用率的这个业务逻辑实际上是花费在这里。但是这一块儿同学们看，它其实只占你整时间当中的非常小的比重，也就是说你的 RT 当中只有一小部分才能反映出服务器它真实的性能数据。那对于这个例子来说，甚至你网络层稍微发生那么一些抖动，都可能去大幅影响你的性能预测的准确率。


所以在我们真实的线上的业务当中，对于这种响应时间非常短的接口，其实我们更偏向于使用什么呀？使用另一个维度来衡量它的机器盲线程度，那就是连接数，也就是当前 active 的线程数。因为你接口的响应时间比较短，你处理业务所花费的时间比例又很少，因此这个 RT 并不是一个非常敏感的数字，那它具有更加灵敏的指示作用。因为对于这类结构来说，如果你等到它的 RT 显著增加的时候，那这时候可能线生池早已经被吃爆了。所以对这类问题，我们的实践经验是尽可能的使用连接数敏感型的负载均衡策略。OK，那这是其中一个场景。


第二个场景，业务复杂度和 RT 非线性相关的场景，那我们也同样的去建议使用连接数敏感型的模型。那什么叫业务复杂度和 RT 非线性相关？举一个简单的例子，你查询请求当中肯定有很多的参数，对吧？那不管你用什么业务场景下的查询参数去调用接口，那它的 RT 响应时间基本上是一个这样的平衡的曲线，它不会随着你的业务场景不同来达到一个波动，那么这种情况下你的 RT 波动是非常平滑的。对于这类业务，实践经验也是说，它更有可能是一个连接数资源占用型的这种业务。所以对于这两类业务，我们通常更加倾向于让同学们使用哪种类型的负载均衡策略？ best available role，那咱前面已经学到过它是什么呀？它是获取到你当前连接数最少的一台服务器，也就是说你当前谁最闲我就挑谁。那这是这个场景，我们接下来再来看响应时间。


敏感型的，前面咱说 RT 非敏感，这里就到了 RT 敏感型的了。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/70b8aab7-0ac3-478c-8bd3-6599fa70c2fc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5PUEFTI%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFKIpHrKu8nmcJl7g2nGwWLiyrO1gGLwRMpE5kZX%2F27UAiEAspq%2FbTTUdt%2FMlrZSaKtqrpVgiR4iboKNaxtKIL%2BYRcMqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDML0eEa2%2BYShwqq0JSrcA%2BqyHrvUiZCZluGFdMCt14pNdSdb8v3eXokCdnOioMQhsIDgzkm312x14Gz3KIrwuW0mWTh281xPOWOHfpdiFxKUEU%2B%2F19K0SQn4tko%2FNQ2nMuC9UG%2FQf%2BV%2BIPmEADnBkifD5sk8E5j4%2FRPpyxQ5WIXfOEgNIKtLYUET1dZS6dW4tuMmjSCj98KkwcMnopuPqca1tFs%2FxKLRizJpMEE0c2pe3kOy0ZCQSQHHXsj549wCs3JlN20mdSEN0AkM1vqZjxYDXD%2BngeW0RqIx0K7vU5MGyZ72y2oU8WAAkPuhwN2xW03478gcmeLYJHi8ef%2B4mvTqZXhQQi%2F8oE6nE4JDEc9P3NEJ8sRxWoINOrL7IwF3S3KpaRFM3uSpmYYHtm4hWLaGpWlzABLVSs6iLjuZzbQQ3zvziNuyebbbWEs2warOG5fkRMZryMSaA3EBsnv60%2FvslCHO7lelsS69losR2jHm4s4pqtGQNmTtOL01p9THtCByR7JDoIHdENA79KWlYZ4DT41Ml6h%2Fj1SFuNSviYZbVlNGWFpqTYtoF2CDVhUMxL1EH5vUYCMPoeT8HL687U%2B3pDkkpwn3WXsQhQKd2PRQ76RlX5eiySZUL2Yne2Hz1BUcnZugOPLVKTM4MMS6%2F9IGOqUBCCfMK1Sca4bV1TX2hNYrEbfWVU%2BRWHOGZnvtcL7Hh08%2Fox8uggr7YVoGMhpuPxfPWkEbf0%2B921MTkEGtYh6Q519j%2BChbW4nZ9I07AIL2a9pQwPJ1xSQGeE3RMfMRXNd3N7OXY274YJ62o1Lou1QqE5wHE6rsmjMKJitUkC%2F42bqrt1dF2x8eZEfkCC48tAfIeJWNTNgulaQwkzvZznKYwTW%2FFozG&X-Amz-Signature=ea2d1c31ab225b87cf6cdb102d1460d8307f600dec8177af2d968e12628213f7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那什么样的服务是 RT 敏感型的呢？打一个比方，咱现在开发了一个大胖子，接口非常非常的重，它的响应时间非常的长，而且它这里有一个显著的跟前面不同的一点是， RT 波动大，就像你那个炒股的 k 线图一样，波动很大。


那什么能影响到 RT 波动？那就是你具体的业务，我打一个比方，订单导出业务，同学们平时做网购肯定也去使用过这类业务，那它们有什么特点？比如说我这个业务发起了一个请求，那这个请求我想导出一个报表，导出你当前全年度的报表，那这个请求一定会耗费非常多的系统资源，为什么呀？因为你选择的时间范围同学们非常的宽，也有一整年的范围，那么你会消耗大量的计算资源， CPU 还有你的内存来去参与这个导出业务。同时你的 RT 响应时间也是处于一个比较高的位置。


OK，那如果我们换一个角度来做导出，我只导出你当月的报表，这样一来你的数据量就会比全年度的数据量减少非常多，那么这种情况下，你导出的报表所占用的时间一定会比前一次要少那么一些，这就是说根据你的业务维度的不同，那么你的响应时间其实会呈现一个类似线性增加的这样的一个趋势。越复杂的业务，那么你的响应时间就越长，越简单的业务就越少。


那么对于咱这里举的这个例子来说，如果同样是一次导出，那你当前机器你可用的线程连接数，当前连接数都是一，对吧？当月是一，全年度是一，但是你在系统层面的资源占用率却是大不相同的。那么在这种场景下，如果我们以照连接数来去衡量系统的盲纤程度，那可能就会怎么样失真，那你无法很准确地衡量你当前机器的 CPU 还有内存，它究竟是忙还是闲。


所以在这种类似的场景下，我们更加偏向于让同学们去使用基于 RT 的指标，那它会具有更高的敏感性。那基于 RT 的指标大家都学过，是前面的一个叫 waited response time rule，这个负载均衡策略会根据你的响应时间做一个分权权重，那你响应时间越短的服务，那么对应的你的权重就越高，就越有可能被选上。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/ba79384e-ac67-4b0e-8640-b4176ff9decc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5PUEFTI%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFKIpHrKu8nmcJl7g2nGwWLiyrO1gGLwRMpE5kZX%2F27UAiEAspq%2FbTTUdt%2FMlrZSaKtqrpVgiR4iboKNaxtKIL%2BYRcMqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDML0eEa2%2BYShwqq0JSrcA%2BqyHrvUiZCZluGFdMCt14pNdSdb8v3eXokCdnOioMQhsIDgzkm312x14Gz3KIrwuW0mWTh281xPOWOHfpdiFxKUEU%2B%2F19K0SQn4tko%2FNQ2nMuC9UG%2FQf%2BV%2BIPmEADnBkifD5sk8E5j4%2FRPpyxQ5WIXfOEgNIKtLYUET1dZS6dW4tuMmjSCj98KkwcMnopuPqca1tFs%2FxKLRizJpMEE0c2pe3kOy0ZCQSQHHXsj549wCs3JlN20mdSEN0AkM1vqZjxYDXD%2BngeW0RqIx0K7vU5MGyZ72y2oU8WAAkPuhwN2xW03478gcmeLYJHi8ef%2B4mvTqZXhQQi%2F8oE6nE4JDEc9P3NEJ8sRxWoINOrL7IwF3S3KpaRFM3uSpmYYHtm4hWLaGpWlzABLVSs6iLjuZzbQQ3zvziNuyebbbWEs2warOG5fkRMZryMSaA3EBsnv60%2FvslCHO7lelsS69losR2jHm4s4pqtGQNmTtOL01p9THtCByR7JDoIHdENA79KWlYZ4DT41Ml6h%2Fj1SFuNSviYZbVlNGWFpqTYtoF2CDVhUMxL1EH5vUYCMPoeT8HL687U%2B3pDkkpwn3WXsQhQKd2PRQ76RlX5eiySZUL2Yne2Hz1BUcnZugOPLVKTM4MMS6%2F9IGOqUBCCfMK1Sca4bV1TX2hNYrEbfWVU%2BRWHOGZnvtcL7Hh08%2Fox8uggr7YVoGMhpuPxfPWkEbf0%2B921MTkEGtYh6Q519j%2BChbW4nZ9I07AIL2a9pQwPJ1xSQGeE3RMfMRXNd3N7OXY274YJ62o1Lou1QqE5wHE6rsmjMKJitUkC%2F42bqrt1dF2x8eZEfkCC48tAfIeJWNTNgulaQwkzvZznKYwTW%2FFozG&X-Amz-Signature=6524d73b942fe8ab37823814e7b78a0f1ef91bd27be5907475fd6a81aebf269a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

什么意思？神经命形式，这是什么形啊？其实这就是一个量变引起质变之后的一个表现。那为什么同样的功能，同学们想一想，在大厂里面和小厂里面，你实现方式是完全不同的，那一个下单接口，你在淘宝里边和在一个 18 线小应用当中，


它的实现模式一定是大不相同，原因就在这里，那就是流量QPS。任何的接口，你只要流量 QPS 打高，那你必须要去换一种实现方式来去写这个接口的逻辑。比如说一个最典型的场景秒杀场景，或者说流量脉冲的场景。那流量脉冲啥意思？


前面咱是不是还提到过一个连接数敏感模型，看起来非常好用，我们用的是 best available rule，对吧？那 Ripen 的这个负载均衡策略，同学们，你在当前的这个神经运行上面，你就完全玩不转，即使你这个接口它自己就是一个连接数敏感型的接口，它满足 best available rule 的使用场景，但是一旦它成为一个这种流量脉冲或者是秒杀类型的这种高 QPS 的接口，那你就不能用这个负载均衡策略。


为什么呀？就像前面一节当中，我们在课程里跟大家介绍的，你的高并发流量，它在抵达你服务器的瞬间，它可能会一台把你的机器全部给打崩，因为流量在瞬时抵达之后，如果它的这个抵达时间是相对密集一致的，那么这时候我四面八方的调用方我都会同时判定其中的一台机器它是连接数最少的，然后你全部流量就打到了这台当前最闲的机器上面。百万雄狮过大江，直接瞬间把你这台机器秒杀掉，然后再怎么呀，一个一个点杀你机群当中的其他机器。所以说这种负载均衡策略对于高并发的应用其实并不适用。所以这也告诉我们，尽信书不如无数。那如果你去相信这个负载均衡策略的字面意思，你把它用到了不适用的场景下，那一定会在生产环境上面栽一个大跟头。那怎么来避免这种情况呢？多测试上生产环境之前做充分的压测。


第二个，我们阅读它的源码里是最明白的业务逻辑，一看源码便知道这个负载均衡策略它的缺陷是什么。OK，这里其他的负载均衡策略可否用在当前的这种超高并发的场景下，其实并不是非常适用。为什么呀？这里有一个很重要的原因，就是说咱在真实环境当中，往往我会把不同的接口都部署到相同的一个应用当中，那时间敏感性、连接数敏感性这两种类型很有可能会同处一室，那你就很难去界定对一种服务应该去使用具体的哪一个负载均衡策略，那这是一个方面。


另一方面我们对于一些大厂的这种大规模的应用集群来说，你一个核心的服务主链路上的核心服务，你动辄大几千甚至上万台服务器，那如果我们采用前面的几种负载均衡手段的话，其实这里面很多策略它都要做这样一个操作，那就是循环查找。那这几种负载均衡策略，那这里面都有它循环的部分，那大家在学算法的时候都知道我们这种类似循环查找的方式，它就是一种 o n 的算法复杂度，那这种效率对于一个几十台的服务器集群来说，可能还不会产生什么大的性能问题，但是如果我们把这个集群数量扩增到几千台、上万台，那你这种循环查找其实也是一个不小的资源开销，一个消耗。


那这时候怎么办？同学们，这时候我们有一个万金油的方案，这里就体现出了一个道理，简单高效就是王道。那经典，为什么是经典？它原因就在这儿有一个类似 OE 的算法，那就是 round Robin row 是一个轮询负载均衡的这个策略，它的效率非常高，类似于 o one，在这个策略里面虽然我们也有循环，但是它其实只是 CAS 加自全来去锁定机器的下标，而不是像前面几种负载均衡策略使用 o n 这种算法来去查找机器。那这里边的逻辑我们在其中一节当中带同学们去看一下源码，立马就知道了。
OK，所以在很多的大厂里面核心应用，它的核心主链路微服务应用其实也是选用这个 round Robin room 作为负载均衡策略的，简单、高效、稳定其实就是它自己的一个优点。OK，那这一节的负载均衡策略适用场景的分享就跟同学们讲到这里了，所以从**前面几个例子当中，同学们应该可以悟出这么一点道理，对于我们做大型业务，尤其是高并发业务这种场景下，我们这里一定要记住流量，那流量可能会做出量变引起质变的事情，它可能把你原先的一些架构上面的假设给它打破。**

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/361b16b8-204c-4812-ac78-37c6cef1f02a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q5PUEFTI%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231319Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIFKIpHrKu8nmcJl7g2nGwWLiyrO1gGLwRMpE5kZX%2F27UAiEAspq%2FbTTUdt%2FMlrZSaKtqrpVgiR4iboKNaxtKIL%2BYRcMqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDML0eEa2%2BYShwqq0JSrcA%2BqyHrvUiZCZluGFdMCt14pNdSdb8v3eXokCdnOioMQhsIDgzkm312x14Gz3KIrwuW0mWTh281xPOWOHfpdiFxKUEU%2B%2F19K0SQn4tko%2FNQ2nMuC9UG%2FQf%2BV%2BIPmEADnBkifD5sk8E5j4%2FRPpyxQ5WIXfOEgNIKtLYUET1dZS6dW4tuMmjSCj98KkwcMnopuPqca1tFs%2FxKLRizJpMEE0c2pe3kOy0ZCQSQHHXsj549wCs3JlN20mdSEN0AkM1vqZjxYDXD%2BngeW0RqIx0K7vU5MGyZ72y2oU8WAAkPuhwN2xW03478gcmeLYJHi8ef%2B4mvTqZXhQQi%2F8oE6nE4JDEc9P3NEJ8sRxWoINOrL7IwF3S3KpaRFM3uSpmYYHtm4hWLaGpWlzABLVSs6iLjuZzbQQ3zvziNuyebbbWEs2warOG5fkRMZryMSaA3EBsnv60%2FvslCHO7lelsS69losR2jHm4s4pqtGQNmTtOL01p9THtCByR7JDoIHdENA79KWlYZ4DT41Ml6h%2Fj1SFuNSviYZbVlNGWFpqTYtoF2CDVhUMxL1EH5vUYCMPoeT8HL687U%2B3pDkkpwn3WXsQhQKd2PRQ76RlX5eiySZUL2Yne2Hz1BUcnZugOPLVKTM4MMS6%2F9IGOqUBCCfMK1Sca4bV1TX2hNYrEbfWVU%2BRWHOGZnvtcL7Hh08%2Fox8uggr7YVoGMhpuPxfPWkEbf0%2B921MTkEGtYh6Q519j%2BChbW4nZ9I07AIL2a9pQwPJ1xSQGeE3RMfMRXNd3N7OXY274YJ62o1Lou1QqE5wHE6rsmjMKJitUkC%2F42bqrt1dF2x8eZEfkCC48tAfIeJWNTNgulaQwkzvZznKYwTW%2FFozG&X-Amz-Signature=722a27f44c5a2b898954ef6a3124ce2b4b355203586af134c53d9cc793124bec&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

所以这就是我们说的为什么 10 万量级 QPS 的应用和1万量级的 QPS 应用，它这两者之间的架构可谓是大不相同，即使他们实现同样的业务逻辑，看上去也近乎是两个不同的业务系统。那当你的流量达到像淘系这么恐怖的，比如从 10 万一下上升到 50 万的时候，那就是另外一番天地了。所以说 QPS 其实也是技术人员的一个珠穆朗玛峰，那我们在自己学习工作过程当中，也一直要去挑战自己的极限，向着更高勇敢迈进。OK，同学们，这一节的内容就跟大家讲到这里，那在接下来小节里，我再带同学们一起做一个 ribbon 的简单落地，看一下他在项目当中应该如何来去做配置。好，同学们，我们下一小节再见。

```java
# 3-4 从架构角度分析负载均衡策略的适用场景

## 1. 负载均衡策略的定位与功能
   ### 1.1 定位:
     - 专注于负载均衡功能
     - 不应包含异常容错
   ### 1.2 功能:
     - 管理请求分发
     - 不负责跨界异常处理
   ### 1.3 原则:
     - 术业有专攻
     - 专注主营业务
     - 牢记初心，不忘使命

## 2. 远程接口类型
   ### 2.1 连接数敏感型
   ### 2.2 响应时间敏感型  
   ### 2.3 神经并行型(高并发场景)
   ### 2.4 重点关注:神经并行型，因为前两种有套路可解决

## 3. 连接数敏感型场景
   ### 3.1 特点:
     - 轻量级微服务
     - 响应时间短(如5ms内)
     - 网络连接开销占比大(如20ms)
     - 业务逻辑处理时间占比小(如20%)
   ### 3.2 问题:
     - RT不能准确反映服务器性能
     - 网络抖动可能影响性能预测准确率
   ### 3.3 解决方案:
     - 使用连接数(active线程数)衡量机器忙闲程度
     - 连接数比RT更敏感，可及时反映服务器状态
   ### 3.4 推荐策略:Best Available Rule
     - 选择当前连接数最少的服务器
   ### 3.5 适用情况:
     - 响应时间非常短的接口
     - 业务复杂度和RT非线性相关的场景

## 4. 响应时间敏感型场景  
   ### 4.1 特点:
     - 接口响应时间长
     - RT波动大
     - 业务复杂度与RT呈线性相关
   ### 4.2 举例:订单导出业务  
     - 全年度报表导出：耗时长，资源消耗大
     - 当月报表导出：耗时短，资源消耗小
   ### 4.3 问题:
     - 连接数相同，但系统资源占用差异大
     - 连接数无法准确反映系统忙闲程度
   ### 4.4 推荐策略:Weighted Response Time Rule
     - 根据响应时间分配权重
     - 响应时间越短，权重越高，被选中概率越大

## 5. 高并发(神经并行)场景
   ### 5.1 特点:
     - 流量QPS极高，需改变实现方式
     - 量变引起质变
   ### 5.2 不适用连接数敏感型策略的原因:
     - 瞬时高并发可能导致单机崩溃
     - 难以为混合部署的不同类型接口选择策略
     - 大规模集群下循环查找效率低
   ### 5.3 推荐策略:Round Robin Rule
     - 简单高效，算法复杂度O(1)
     - 适用于大规模集群
     - 使用CAS加自旋锁定机器下标，非O(n)查找
   ### 5.4 大厂核心应用选择原因:
     - 简单
     - 高效
     - 稳定

## 6. 负载均衡策略选择建议
   ### 6.1 不要盲信策略自称的优点
   ### 6.2 在生产环境前进行充分压测
   ### 6.3 阅读源码了解策略缺陷
   ### 6.4 考虑流量对架构的影响
   ### 6.5 根据实际QPS规模选择合适的架构和策略

## 7. QPS对系统架构的影响
   ### 7.1 不同QPS量级的系统架构差异巨大
     - 10万级QPS vs 1万级QPS：架构大不相同
     - 10万到50万QPS：又是另一番天地
   ### 7.2 QPS增长可能导致架构重构
   ### 7.3 QPS被视为技术人员的珠穆朗玛峰

## 8. 学习建议
   ### 8.1 不要相信负载均衡策略自己宣传的优点
   ### 8.2 在真实超高并发项目中可能存在坑
   ### 8.3 架构师选择技术不能只依赖搜索引擎
   ### 8.4 通过实践经验验证理论
   ### 8.5 持续挑战自己的极限，向更高目标迈进

## 9. 生产环境相关建议
   ### 9.1 上线前进行充分压测
   ### 9.2 阅读源码了解策略缺陷
   ### 9.3 考虑流量对架构的影响
   ### 9.4 根据实际QPS规模选择合适的架构和策略
   ### 9.5 注意高并发场景下负载均衡策略的适用性

## 10. 总结
    10.1 负载均衡策略选择需考虑多方面因素
    10.2 不同场景下适用不同的负载均衡策略
    10.3 高并发环境下需特别注意策略选择
    10.4 实践、测试和源码阅读是选择正确策略的关键
    10.5 随着QPS增长，可能需要调整系统架构
```


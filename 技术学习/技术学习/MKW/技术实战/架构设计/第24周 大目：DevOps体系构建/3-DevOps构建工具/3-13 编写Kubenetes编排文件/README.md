---
title: 3-13 编写Kubenetes编排文件
---

# 3-13 编写Kubenetes编排文件

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/5953b989-adcb-4fcb-9a0e-bd58ee3c7741/SCR-20240802-pihn.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXK5HXBX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFgIEw%2BQb9S3SbbJ8eTp%2FY6C2NiCo%2FMhJkF0jFf%2FZ7njAiBd4rdkQnkcmJ3L5PEpNjlVGvY3Byw%2BWj01pvKvr5e0aiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMi%2FGmeJpgLdKqMB29KtwDUJwV%2BKkuD61aDWlVj58uBqM8XIPKSyosnwXDgqdYVgIwdokwI51SmbHGuro%2BX3lc%2FPfC%2F5dolo4VARVmgHYJauqjILdtG0aheUaNayXbVYUpQPiaDTq3JRtYjc31o0lowbk6CfsNGgtUOjVKI2aH5tpjELBizB3dafhnPMsNdUPJyyczVO6DgB4QWa2upx1Q3hzT00EiHGF2kk354WFDGhpg1jexh5mDnME%2B8RTM8rYD4MAWjYX87VGiTP9WbvtnFgkFz31gFjpr3y697vBBXLrFQyUxHQvHr389MTDTtR%2BPhrmyP3VsJOWsIxEkFZZ9c3Fzfg29i4ZTnM7e8BF7DLOINRlZh09ZasZO6ePp0%2BPG2QakvON%2BCF9ct%2BrCXYzO1974tK9lSM7nWrfWR1CrvKIvAr2Acc2EcvIQTQyn77ZJ45MQox%2Bf2jRelolfct0sx9538qGP6afp9pG1SqBkBvy46u5zSjIADAUnjqVHr8M2hDyF5bMJNtfDcKDUfMe807bxgkum6jSGf8oF4%2F9DkP1YRtI8RN3bM%2FF1UrgoFH4t6nncE5pfg00gmTt1iEnNab60%2BtAsm4Ab1JzCXoAunk0IOgQUFPPfbm1sRdM9pNfEIyGFo4oNYr9Wc88whLn%2F0gY6pgHVJNv%2FpQbVCF1xNOdB1N9pktYdN6xROaCRF%2BcuqSjQFMKzv1RpMtlFslTroNch7ty9YxoPVAWl2SscwHu8hHHooUKkX147W9JwG13HfKSvwZhWV3JSlEMOLZo01FsxAKaJor6FJmo%2BlCmLJfPXqjHBoz5OSzgiP%2BNDQDGQgo08fnqLvV4vzHs%2Bd7OZwKTidvZbJwBf7mOnINZLW06EgBoqb%2B8vDDpm&X-Amz-Signature=f3d4cc91f79e2edbee75c2d2466516fd6a83ff2940514ed77e46dec902164591&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/471b617f-6ccd-4d40-9358-7a8825bb4c1e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXK5HXBX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFgIEw%2BQb9S3SbbJ8eTp%2FY6C2NiCo%2FMhJkF0jFf%2FZ7njAiBd4rdkQnkcmJ3L5PEpNjlVGvY3Byw%2BWj01pvKvr5e0aiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMi%2FGmeJpgLdKqMB29KtwDUJwV%2BKkuD61aDWlVj58uBqM8XIPKSyosnwXDgqdYVgIwdokwI51SmbHGuro%2BX3lc%2FPfC%2F5dolo4VARVmgHYJauqjILdtG0aheUaNayXbVYUpQPiaDTq3JRtYjc31o0lowbk6CfsNGgtUOjVKI2aH5tpjELBizB3dafhnPMsNdUPJyyczVO6DgB4QWa2upx1Q3hzT00EiHGF2kk354WFDGhpg1jexh5mDnME%2B8RTM8rYD4MAWjYX87VGiTP9WbvtnFgkFz31gFjpr3y697vBBXLrFQyUxHQvHr389MTDTtR%2BPhrmyP3VsJOWsIxEkFZZ9c3Fzfg29i4ZTnM7e8BF7DLOINRlZh09ZasZO6ePp0%2BPG2QakvON%2BCF9ct%2BrCXYzO1974tK9lSM7nWrfWR1CrvKIvAr2Acc2EcvIQTQyn77ZJ45MQox%2Bf2jRelolfct0sx9538qGP6afp9pG1SqBkBvy46u5zSjIADAUnjqVHr8M2hDyF5bMJNtfDcKDUfMe807bxgkum6jSGf8oF4%2F9DkP1YRtI8RN3bM%2FF1UrgoFH4t6nncE5pfg00gmTt1iEnNab60%2BtAsm4Ab1JzCXoAunk0IOgQUFPPfbm1sRdM9pNfEIyGFo4oNYr9Wc88whLn%2F0gY6pgHVJNv%2FpQbVCF1xNOdB1N9pktYdN6xROaCRF%2BcuqSjQFMKzv1RpMtlFslTroNch7ty9YxoPVAWl2SscwHu8hHHooUKkX147W9JwG13HfKSvwZhWV3JSlEMOLZo01FsxAKaJor6FJmo%2BlCmLJfPXqjHBoz5OSzgiP%2BNDQDGQgo08fnqLvV4vzHs%2Bd7OZwKTidvZbJwBf7mOnINZLW06EgBoqb%2B8vDDpm&X-Amz-Signature=b86f101f653457d23645a464dfa303c9196489163d025200bdc8d24b85fed5cf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/aabef747-197e-4b1b-b5b6-5db58d622170/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXK5HXBX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFgIEw%2BQb9S3SbbJ8eTp%2FY6C2NiCo%2FMhJkF0jFf%2FZ7njAiBd4rdkQnkcmJ3L5PEpNjlVGvY3Byw%2BWj01pvKvr5e0aiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMi%2FGmeJpgLdKqMB29KtwDUJwV%2BKkuD61aDWlVj58uBqM8XIPKSyosnwXDgqdYVgIwdokwI51SmbHGuro%2BX3lc%2FPfC%2F5dolo4VARVmgHYJauqjILdtG0aheUaNayXbVYUpQPiaDTq3JRtYjc31o0lowbk6CfsNGgtUOjVKI2aH5tpjELBizB3dafhnPMsNdUPJyyczVO6DgB4QWa2upx1Q3hzT00EiHGF2kk354WFDGhpg1jexh5mDnME%2B8RTM8rYD4MAWjYX87VGiTP9WbvtnFgkFz31gFjpr3y697vBBXLrFQyUxHQvHr389MTDTtR%2BPhrmyP3VsJOWsIxEkFZZ9c3Fzfg29i4ZTnM7e8BF7DLOINRlZh09ZasZO6ePp0%2BPG2QakvON%2BCF9ct%2BrCXYzO1974tK9lSM7nWrfWR1CrvKIvAr2Acc2EcvIQTQyn77ZJ45MQox%2Bf2jRelolfct0sx9538qGP6afp9pG1SqBkBvy46u5zSjIADAUnjqVHr8M2hDyF5bMJNtfDcKDUfMe807bxgkum6jSGf8oF4%2F9DkP1YRtI8RN3bM%2FF1UrgoFH4t6nncE5pfg00gmTt1iEnNab60%2BtAsm4Ab1JzCXoAunk0IOgQUFPPfbm1sRdM9pNfEIyGFo4oNYr9Wc88whLn%2F0gY6pgHVJNv%2FpQbVCF1xNOdB1N9pktYdN6xROaCRF%2BcuqSjQFMKzv1RpMtlFslTroNch7ty9YxoPVAWl2SscwHu8hHHooUKkX147W9JwG13HfKSvwZhWV3JSlEMOLZo01FsxAKaJor6FJmo%2BlCmLJfPXqjHBoz5OSzgiP%2BNDQDGQgo08fnqLvV4vzHs%2Bd7OZwKTidvZbJwBf7mOnINZLW06EgBoqb%2B8vDDpm&X-Amz-Signature=4b313b55677e104f0fe5ae3f3373d7e0dc02b3f934cfc7a923205c3fcd497c73&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/7af274d3-bfbd-4c14-8d44-f24313aaf1c4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXK5HXBX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFgIEw%2BQb9S3SbbJ8eTp%2FY6C2NiCo%2FMhJkF0jFf%2FZ7njAiBd4rdkQnkcmJ3L5PEpNjlVGvY3Byw%2BWj01pvKvr5e0aiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMi%2FGmeJpgLdKqMB29KtwDUJwV%2BKkuD61aDWlVj58uBqM8XIPKSyosnwXDgqdYVgIwdokwI51SmbHGuro%2BX3lc%2FPfC%2F5dolo4VARVmgHYJauqjILdtG0aheUaNayXbVYUpQPiaDTq3JRtYjc31o0lowbk6CfsNGgtUOjVKI2aH5tpjELBizB3dafhnPMsNdUPJyyczVO6DgB4QWa2upx1Q3hzT00EiHGF2kk354WFDGhpg1jexh5mDnME%2B8RTM8rYD4MAWjYX87VGiTP9WbvtnFgkFz31gFjpr3y697vBBXLrFQyUxHQvHr389MTDTtR%2BPhrmyP3VsJOWsIxEkFZZ9c3Fzfg29i4ZTnM7e8BF7DLOINRlZh09ZasZO6ePp0%2BPG2QakvON%2BCF9ct%2BrCXYzO1974tK9lSM7nWrfWR1CrvKIvAr2Acc2EcvIQTQyn77ZJ45MQox%2Bf2jRelolfct0sx9538qGP6afp9pG1SqBkBvy46u5zSjIADAUnjqVHr8M2hDyF5bMJNtfDcKDUfMe807bxgkum6jSGf8oF4%2F9DkP1YRtI8RN3bM%2FF1UrgoFH4t6nncE5pfg00gmTt1iEnNab60%2BtAsm4Ab1JzCXoAunk0IOgQUFPPfbm1sRdM9pNfEIyGFo4oNYr9Wc88whLn%2F0gY6pgHVJNv%2FpQbVCF1xNOdB1N9pktYdN6xROaCRF%2BcuqSjQFMKzv1RpMtlFslTroNch7ty9YxoPVAWl2SscwHu8hHHooUKkX147W9JwG13HfKSvwZhWV3JSlEMOLZo01FsxAKaJor6FJmo%2BlCmLJfPXqjHBoz5OSzgiP%2BNDQDGQgo08fnqLvV4vzHs%2Bd7OZwKTidvZbJwBf7mOnINZLW06EgBoqb%2B8vDDpm&X-Amz-Signature=d6f707839be49f13cc5ba35107247d37515f11045bcf3a413676a526e26d4921&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

家好，我是大木。前面已经为 Euroka server 构建了 Docker 镜像。这节课我们来为 Eurika server 编写 Kubernetes 编排文件，并把 Eurika server 运行到 Kubernetes 里面。下来为单机版 Uruca server 编写 K8S 编排文件。创建一个目录叫K8S，创建个文件叫 Eureka 杠single，点八秒，写上注释。单机版 Eureka server，开始编写 , **IDEA 它对 K8S 有比较良好的支持**。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/fd535876-19c8-4a76-b3b0-1ef606256070/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXK5HXBX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFgIEw%2BQb9S3SbbJ8eTp%2FY6C2NiCo%2FMhJkF0jFf%2FZ7njAiBd4rdkQnkcmJ3L5PEpNjlVGvY3Byw%2BWj01pvKvr5e0aiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMi%2FGmeJpgLdKqMB29KtwDUJwV%2BKkuD61aDWlVj58uBqM8XIPKSyosnwXDgqdYVgIwdokwI51SmbHGuro%2BX3lc%2FPfC%2F5dolo4VARVmgHYJauqjILdtG0aheUaNayXbVYUpQPiaDTq3JRtYjc31o0lowbk6CfsNGgtUOjVKI2aH5tpjELBizB3dafhnPMsNdUPJyyczVO6DgB4QWa2upx1Q3hzT00EiHGF2kk354WFDGhpg1jexh5mDnME%2B8RTM8rYD4MAWjYX87VGiTP9WbvtnFgkFz31gFjpr3y697vBBXLrFQyUxHQvHr389MTDTtR%2BPhrmyP3VsJOWsIxEkFZZ9c3Fzfg29i4ZTnM7e8BF7DLOINRlZh09ZasZO6ePp0%2BPG2QakvON%2BCF9ct%2BrCXYzO1974tK9lSM7nWrfWR1CrvKIvAr2Acc2EcvIQTQyn77ZJ45MQox%2Bf2jRelolfct0sx9538qGP6afp9pG1SqBkBvy46u5zSjIADAUnjqVHr8M2hDyF5bMJNtfDcKDUfMe807bxgkum6jSGf8oF4%2F9DkP1YRtI8RN3bM%2FF1UrgoFH4t6nncE5pfg00gmTt1iEnNab60%2BtAsm4Ab1JzCXoAunk0IOgQUFPPfbm1sRdM9pNfEIyGFo4oNYr9Wc88whLn%2F0gY6pgHVJNv%2FpQbVCF1xNOdB1N9pktYdN6xROaCRF%2BcuqSjQFMKzv1RpMtlFslTroNch7ty9YxoPVAWl2SscwHu8hHHooUKkX147W9JwG13HfKSvwZhWV3JSlEMOLZo01FsxAKaJor6FJmo%2BlCmLJfPXqjHBoz5OSzgiP%2BNDQDGQgo08fnqLvV4vzHs%2Bd7OZwKTidvZbJwBf7mOnINZLW06EgBoqb%2B8vDDpm&X-Amz-Signature=ec9936a3fe74bcbf27046fefb62d7c075debea5c243105423295fa1f6ad4d0ef&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[https://www.jianshu.com/p/669fc6ed78c9](https://www.jianshu.com/p/669fc6ed78c9)

只要用 **kdep** 就可以快速创建一个 deployment 了。

name eureka-server1 ,  image my-eureka。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/c842cf6c-e01a-49d8-a7cc-8757a31d8a4b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXK5HXBX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFgIEw%2BQb9S3SbbJ8eTp%2FY6C2NiCo%2FMhJkF0jFf%2FZ7njAiBd4rdkQnkcmJ3L5PEpNjlVGvY3Byw%2BWj01pvKvr5e0aiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMi%2FGmeJpgLdKqMB29KtwDUJwV%2BKkuD61aDWlVj58uBqM8XIPKSyosnwXDgqdYVgIwdokwI51SmbHGuro%2BX3lc%2FPfC%2F5dolo4VARVmgHYJauqjILdtG0aheUaNayXbVYUpQPiaDTq3JRtYjc31o0lowbk6CfsNGgtUOjVKI2aH5tpjELBizB3dafhnPMsNdUPJyyczVO6DgB4QWa2upx1Q3hzT00EiHGF2kk354WFDGhpg1jexh5mDnME%2B8RTM8rYD4MAWjYX87VGiTP9WbvtnFgkFz31gFjpr3y697vBBXLrFQyUxHQvHr389MTDTtR%2BPhrmyP3VsJOWsIxEkFZZ9c3Fzfg29i4ZTnM7e8BF7DLOINRlZh09ZasZO6ePp0%2BPG2QakvON%2BCF9ct%2BrCXYzO1974tK9lSM7nWrfWR1CrvKIvAr2Acc2EcvIQTQyn77ZJ45MQox%2Bf2jRelolfct0sx9538qGP6afp9pG1SqBkBvy46u5zSjIADAUnjqVHr8M2hDyF5bMJNtfDcKDUfMe807bxgkum6jSGf8oF4%2F9DkP1YRtI8RN3bM%2FF1UrgoFH4t6nncE5pfg00gmTt1iEnNab60%2BtAsm4Ab1JzCXoAunk0IOgQUFPPfbm1sRdM9pNfEIyGFo4oNYr9Wc88whLn%2F0gY6pgHVJNv%2FpQbVCF1xNOdB1N9pktYdN6xROaCRF%2BcuqSjQFMKzv1RpMtlFslTroNch7ty9YxoPVAWl2SscwHu8hHHooUKkX147W9JwG13HfKSvwZhWV3JSlEMOLZo01FsxAKaJor6FJmo%2BlCmLJfPXqjHBoz5OSzgiP%2BNDQDGQgo08fnqLvV4vzHs%2Bd7OZwKTidvZbJwBf7mOnINZLW06EgBoqb%2B8vDDpm&X-Amz-Signature=e034d5dea26474b688f1f0cf786775edac9704bcfd49fcf28b29bcf9cede9fd0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

deployment 的编写完成，由于我们需要在本机也就是 K8S 集群以外访问到 eureka server，

所以我们还需要编写一个service。用---连字符把 yaml 分割成多个部分，再用 kser 快速创建一个service。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/83a804c1-d807-42f4-9f55-ef2d41a6d8ce/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXK5HXBX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFgIEw%2BQb9S3SbbJ8eTp%2FY6C2NiCo%2FMhJkF0jFf%2FZ7njAiBd4rdkQnkcmJ3L5PEpNjlVGvY3Byw%2BWj01pvKvr5e0aiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMi%2FGmeJpgLdKqMB29KtwDUJwV%2BKkuD61aDWlVj58uBqM8XIPKSyosnwXDgqdYVgIwdokwI51SmbHGuro%2BX3lc%2FPfC%2F5dolo4VARVmgHYJauqjILdtG0aheUaNayXbVYUpQPiaDTq3JRtYjc31o0lowbk6CfsNGgtUOjVKI2aH5tpjELBizB3dafhnPMsNdUPJyyczVO6DgB4QWa2upx1Q3hzT00EiHGF2kk354WFDGhpg1jexh5mDnME%2B8RTM8rYD4MAWjYX87VGiTP9WbvtnFgkFz31gFjpr3y697vBBXLrFQyUxHQvHr389MTDTtR%2BPhrmyP3VsJOWsIxEkFZZ9c3Fzfg29i4ZTnM7e8BF7DLOINRlZh09ZasZO6ePp0%2BPG2QakvON%2BCF9ct%2BrCXYzO1974tK9lSM7nWrfWR1CrvKIvAr2Acc2EcvIQTQyn77ZJ45MQox%2Bf2jRelolfct0sx9538qGP6afp9pG1SqBkBvy46u5zSjIADAUnjqVHr8M2hDyF5bMJNtfDcKDUfMe807bxgkum6jSGf8oF4%2F9DkP1YRtI8RN3bM%2FF1UrgoFH4t6nncE5pfg00gmTt1iEnNab60%2BtAsm4Ab1JzCXoAunk0IOgQUFPPfbm1sRdM9pNfEIyGFo4oNYr9Wc88whLn%2F0gY6pgHVJNv%2FpQbVCF1xNOdB1N9pktYdN6xROaCRF%2BcuqSjQFMKzv1RpMtlFslTroNch7ty9YxoPVAWl2SscwHu8hHHooUKkX147W9JwG13HfKSvwZhWV3JSlEMOLZo01FsxAKaJor6FJmo%2BlCmLJfPXqjHBoz5OSzgiP%2BNDQDGQgo08fnqLvV4vzHs%2Bd7OZwKTidvZbJwBf7mOnINZLW06EgBoqb%2B8vDDpm&X-Amz-Signature=9f2288ae77b94018bf319503a8ad6f2ed991b40f6533d80e04991f4e8a358ff9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/d1a5eccb-f456-46fb-9445-44cee2173bab/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXK5HXBX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFgIEw%2BQb9S3SbbJ8eTp%2FY6C2NiCo%2FMhJkF0jFf%2FZ7njAiBd4rdkQnkcmJ3L5PEpNjlVGvY3Byw%2BWj01pvKvr5e0aiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMi%2FGmeJpgLdKqMB29KtwDUJwV%2BKkuD61aDWlVj58uBqM8XIPKSyosnwXDgqdYVgIwdokwI51SmbHGuro%2BX3lc%2FPfC%2F5dolo4VARVmgHYJauqjILdtG0aheUaNayXbVYUpQPiaDTq3JRtYjc31o0lowbk6CfsNGgtUOjVKI2aH5tpjELBizB3dafhnPMsNdUPJyyczVO6DgB4QWa2upx1Q3hzT00EiHGF2kk354WFDGhpg1jexh5mDnME%2B8RTM8rYD4MAWjYX87VGiTP9WbvtnFgkFz31gFjpr3y697vBBXLrFQyUxHQvHr389MTDTtR%2BPhrmyP3VsJOWsIxEkFZZ9c3Fzfg29i4ZTnM7e8BF7DLOINRlZh09ZasZO6ePp0%2BPG2QakvON%2BCF9ct%2BrCXYzO1974tK9lSM7nWrfWR1CrvKIvAr2Acc2EcvIQTQyn77ZJ45MQox%2Bf2jRelolfct0sx9538qGP6afp9pG1SqBkBvy46u5zSjIADAUnjqVHr8M2hDyF5bMJNtfDcKDUfMe807bxgkum6jSGf8oF4%2F9DkP1YRtI8RN3bM%2FF1UrgoFH4t6nncE5pfg00gmTt1iEnNab60%2BtAsm4Ab1JzCXoAunk0IOgQUFPPfbm1sRdM9pNfEIyGFo4oNYr9Wc88whLn%2F0gY6pgHVJNv%2FpQbVCF1xNOdB1N9pktYdN6xROaCRF%2BcuqSjQFMKzv1RpMtlFslTroNch7ty9YxoPVAWl2SscwHu8hHHooUKkX147W9JwG13HfKSvwZhWV3JSlEMOLZo01FsxAKaJor6FJmo%2BlCmLJfPXqjHBoz5OSzgiP%2BNDQDGQgo08fnqLvV4vzHs%2Bd7OZwKTidvZbJwBf7mOnINZLW06EgBoqb%2B8vDDpm&X-Amz-Signature=54455b8021a565b206cfc2b3e51a167d54ad3d61c6dd42fb5e6b120784170020&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

service 的名称也叫 eureka-server1。 这个 service 会选中带有 app 等于 eureka-server1 的pod，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/9aed0c3a-021e-465d-818e-ebbe61678733/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXK5HXBX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFgIEw%2BQb9S3SbbJ8eTp%2FY6C2NiCo%2FMhJkF0jFf%2FZ7njAiBd4rdkQnkcmJ3L5PEpNjlVGvY3Byw%2BWj01pvKvr5e0aiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMi%2FGmeJpgLdKqMB29KtwDUJwV%2BKkuD61aDWlVj58uBqM8XIPKSyosnwXDgqdYVgIwdokwI51SmbHGuro%2BX3lc%2FPfC%2F5dolo4VARVmgHYJauqjILdtG0aheUaNayXbVYUpQPiaDTq3JRtYjc31o0lowbk6CfsNGgtUOjVKI2aH5tpjELBizB3dafhnPMsNdUPJyyczVO6DgB4QWa2upx1Q3hzT00EiHGF2kk354WFDGhpg1jexh5mDnME%2B8RTM8rYD4MAWjYX87VGiTP9WbvtnFgkFz31gFjpr3y697vBBXLrFQyUxHQvHr389MTDTtR%2BPhrmyP3VsJOWsIxEkFZZ9c3Fzfg29i4ZTnM7e8BF7DLOINRlZh09ZasZO6ePp0%2BPG2QakvON%2BCF9ct%2BrCXYzO1974tK9lSM7nWrfWR1CrvKIvAr2Acc2EcvIQTQyn77ZJ45MQox%2Bf2jRelolfct0sx9538qGP6afp9pG1SqBkBvy46u5zSjIADAUnjqVHr8M2hDyF5bMJNtfDcKDUfMe807bxgkum6jSGf8oF4%2F9DkP1YRtI8RN3bM%2FF1UrgoFH4t6nncE5pfg00gmTt1iEnNab60%2BtAsm4Ab1JzCXoAunk0IOgQUFPPfbm1sRdM9pNfEIyGFo4oNYr9Wc88whLn%2F0gY6pgHVJNv%2FpQbVCF1xNOdB1N9pktYdN6xROaCRF%2BcuqSjQFMKzv1RpMtlFslTroNch7ty9YxoPVAWl2SscwHu8hHHooUKkX147W9JwG13HfKSvwZhWV3JSlEMOLZo01FsxAKaJor6FJmo%2BlCmLJfPXqjHBoz5OSzgiP%2BNDQDGQgo08fnqLvV4vzHs%2Bd7OZwKTidvZbJwBf7mOnINZLW06EgBoqb%2B8vDDpm&X-Amz-Signature=ec1f22303897c0fb34f8363f3608bf33641dbf2889f99fa756dfe3a11078d9d9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

也就是这些pod。OK。接着写 port 8761。这里的 port 指的是 service 的端口，此外还有 TargetPort 8761。 targetPort 指的是当访问 service 的端口，使转发到 pod 的哪个端口下。同学们还记得我们前面构建的 my-eureka 镜像里面使用的是 8762 端口对吧？ OK， type 是 service 的类型。

前面说过，由于我们需要在本机访问，所以要暴露到 K8S 外部。这里我们就用 nodeport 的方式去暴露到 K8S 外部。 NodePort 可以实现 K8S 集群任意 NodePort 端口访问到服务，  NodePort 可以自己指定，比方 3000 标也可以不指定。如果缺省会自动分配端口。


OK。这样当在宿主机访问 localhost 30001 的时候，就会请求到， eureka-server1 服务的 8761 端口， eureka-server1 的 8761 又会转发到对应 pod 的 8761，这样的

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/d121c91a-0ffa-49df-ad2b-aa770354c1dd/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXK5HXBX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231540Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFgIEw%2BQb9S3SbbJ8eTp%2FY6C2NiCo%2FMhJkF0jFf%2FZ7njAiBd4rdkQnkcmJ3L5PEpNjlVGvY3Byw%2BWj01pvKvr5e0aiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMi%2FGmeJpgLdKqMB29KtwDUJwV%2BKkuD61aDWlVj58uBqM8XIPKSyosnwXDgqdYVgIwdokwI51SmbHGuro%2BX3lc%2FPfC%2F5dolo4VARVmgHYJauqjILdtG0aheUaNayXbVYUpQPiaDTq3JRtYjc31o0lowbk6CfsNGgtUOjVKI2aH5tpjELBizB3dafhnPMsNdUPJyyczVO6DgB4QWa2upx1Q3hzT00EiHGF2kk354WFDGhpg1jexh5mDnME%2B8RTM8rYD4MAWjYX87VGiTP9WbvtnFgkFz31gFjpr3y697vBBXLrFQyUxHQvHr389MTDTtR%2BPhrmyP3VsJOWsIxEkFZZ9c3Fzfg29i4ZTnM7e8BF7DLOINRlZh09ZasZO6ePp0%2BPG2QakvON%2BCF9ct%2BrCXYzO1974tK9lSM7nWrfWR1CrvKIvAr2Acc2EcvIQTQyn77ZJ45MQox%2Bf2jRelolfct0sx9538qGP6afp9pG1SqBkBvy46u5zSjIADAUnjqVHr8M2hDyF5bMJNtfDcKDUfMe807bxgkum6jSGf8oF4%2F9DkP1YRtI8RN3bM%2FF1UrgoFH4t6nncE5pfg00gmTt1iEnNab60%2BtAsm4Ab1JzCXoAunk0IOgQUFPPfbm1sRdM9pNfEIyGFo4oNYr9Wc88whLn%2F0gY6pgHVJNv%2FpQbVCF1xNOdB1N9pktYdN6xROaCRF%2BcuqSjQFMKzv1RpMtlFslTroNch7ty9YxoPVAWl2SscwHu8hHHooUKkX147W9JwG13HfKSvwZhWV3JSlEMOLZo01FsxAKaJor6FJmo%2BlCmLJfPXqjHBoz5OSzgiP%2BNDQDGQgo08fnqLvV4vzHs%2Bd7OZwKTidvZbJwBf7mOnINZLW06EgBoqb%2B8vDDpm&X-Amz-Signature=92f7004cd8d2393670a74af3a29ee0a873ca93cd349f9f1cba2558c66386fc60&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

就可以访问到这个 pod 了。OK，顺便复习一下。

同学们还记得 **K8S 有几种方式可以暴露到 K8S 外部吗？写一下。主要有三种，分别是NodePort， LoadBalancer，以及 ingress**。如果同学们对于这部分内容感到陌生，可以复习一下。架构是一期 K8S 的相关章节，里面讲得非常的详细，**或者也可以看一下**[**这篇文章**](https://blog.csdn.net/weixin_44267608/article/details/102728050?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522167652738716800222856248%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fall.%2522%257D&request_id=167652738716800222856248&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~first_rank_ecpm_v1~rank_v31_ecpm-1-102728050-null-null.142%5Ev73%5Einsert_down2%2C201%5Ev4%5Eadd_ask%2C239%5Ev1%5Econtrol&utm_term=K8s%E4%B9%8B%20NodePport%20LoadBalancer%20%E5%92%8C%20ingress%20%E7%9A%84%E5%8C%BA%E5%88%AB&spm=1018.2226.3001.4187)**。**

[https://blog.csdn.net/weixin_44267608/article/details/102728050?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522167652738716800222856248%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fall.%2522%257D&request_id=167652738716800222856248&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~first_rank_ecpm_v1~rank_v31_ecpm-1-102728050-null-null.142^v73^insert_down2,201^v4^add_ask,239^v1^control&utm_term=K8s之 NodePport LoadBalancer 和 ingress 的区别&spm=1018.2226.3001.4187](https://blog.csdn.net/weixin_44267608/article/details/102728050?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522167652738716800222856248%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fall.%2522%257D&request_id=167652738716800222856248&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~first_rank_ecpm_v1~rank_v31_ecpm-1-102728050-null-null.142%5Ev73%5Einsert_down2%2C201%5Ev4%5Eadd_ask%2C239%5Ev1%5Econtrol&utm_term=K8s%E4%B9%8B%20NodePport%20LoadBalancer%20%E5%92%8C%20ingress%20%E7%9A%84%E5%8C%BA%E5%88%AB&spm=1018.2226.3001.4187)

首先是 classIp, classIp

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/4aa7d7c6-cd63-4875-98a1-2adf33217188/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXK5HXBX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFgIEw%2BQb9S3SbbJ8eTp%2FY6C2NiCo%2FMhJkF0jFf%2FZ7njAiBd4rdkQnkcmJ3L5PEpNjlVGvY3Byw%2BWj01pvKvr5e0aiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMi%2FGmeJpgLdKqMB29KtwDUJwV%2BKkuD61aDWlVj58uBqM8XIPKSyosnwXDgqdYVgIwdokwI51SmbHGuro%2BX3lc%2FPfC%2F5dolo4VARVmgHYJauqjILdtG0aheUaNayXbVYUpQPiaDTq3JRtYjc31o0lowbk6CfsNGgtUOjVKI2aH5tpjELBizB3dafhnPMsNdUPJyyczVO6DgB4QWa2upx1Q3hzT00EiHGF2kk354WFDGhpg1jexh5mDnME%2B8RTM8rYD4MAWjYX87VGiTP9WbvtnFgkFz31gFjpr3y697vBBXLrFQyUxHQvHr389MTDTtR%2BPhrmyP3VsJOWsIxEkFZZ9c3Fzfg29i4ZTnM7e8BF7DLOINRlZh09ZasZO6ePp0%2BPG2QakvON%2BCF9ct%2BrCXYzO1974tK9lSM7nWrfWR1CrvKIvAr2Acc2EcvIQTQyn77ZJ45MQox%2Bf2jRelolfct0sx9538qGP6afp9pG1SqBkBvy46u5zSjIADAUnjqVHr8M2hDyF5bMJNtfDcKDUfMe807bxgkum6jSGf8oF4%2F9DkP1YRtI8RN3bM%2FF1UrgoFH4t6nncE5pfg00gmTt1iEnNab60%2BtAsm4Ab1JzCXoAunk0IOgQUFPPfbm1sRdM9pNfEIyGFo4oNYr9Wc88whLn%2F0gY6pgHVJNv%2FpQbVCF1xNOdB1N9pktYdN6xROaCRF%2BcuqSjQFMKzv1RpMtlFslTroNch7ty9YxoPVAWl2SscwHu8hHHooUKkX147W9JwG13HfKSvwZhWV3JSlEMOLZo01FsxAKaJor6FJmo%2BlCmLJfPXqjHBoz5OSzgiP%2BNDQDGQgo08fnqLvV4vzHs%2Bd7OZwKTidvZbJwBf7mOnINZLW06EgBoqb%2B8vDDpm&X-Amz-Signature=012798e77b3818dd55573930e24d9c6966c168f2e321c780e97ef90f1c5fb410&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

 只是在 K8S 内部去访问其他的服务，通过 service 请求到 service 所选择的 pod Notepods。

我们课上所使用的，可以使用集群里面任意一个 node 的 nodePort 端口访问到对应的 service。 

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/253c8f31-21e9-44f6-aed8-94a31d9a3fd5/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXK5HXBX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFgIEw%2BQb9S3SbbJ8eTp%2FY6C2NiCo%2FMhJkF0jFf%2FZ7njAiBd4rdkQnkcmJ3L5PEpNjlVGvY3Byw%2BWj01pvKvr5e0aiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMi%2FGmeJpgLdKqMB29KtwDUJwV%2BKkuD61aDWlVj58uBqM8XIPKSyosnwXDgqdYVgIwdokwI51SmbHGuro%2BX3lc%2FPfC%2F5dolo4VARVmgHYJauqjILdtG0aheUaNayXbVYUpQPiaDTq3JRtYjc31o0lowbk6CfsNGgtUOjVKI2aH5tpjELBizB3dafhnPMsNdUPJyyczVO6DgB4QWa2upx1Q3hzT00EiHGF2kk354WFDGhpg1jexh5mDnME%2B8RTM8rYD4MAWjYX87VGiTP9WbvtnFgkFz31gFjpr3y697vBBXLrFQyUxHQvHr389MTDTtR%2BPhrmyP3VsJOWsIxEkFZZ9c3Fzfg29i4ZTnM7e8BF7DLOINRlZh09ZasZO6ePp0%2BPG2QakvON%2BCF9ct%2BrCXYzO1974tK9lSM7nWrfWR1CrvKIvAr2Acc2EcvIQTQyn77ZJ45MQox%2Bf2jRelolfct0sx9538qGP6afp9pG1SqBkBvy46u5zSjIADAUnjqVHr8M2hDyF5bMJNtfDcKDUfMe807bxgkum6jSGf8oF4%2F9DkP1YRtI8RN3bM%2FF1UrgoFH4t6nncE5pfg00gmTt1iEnNab60%2BtAsm4Ab1JzCXoAunk0IOgQUFPPfbm1sRdM9pNfEIyGFo4oNYr9Wc88whLn%2F0gY6pgHVJNv%2FpQbVCF1xNOdB1N9pktYdN6xROaCRF%2BcuqSjQFMKzv1RpMtlFslTroNch7ty9YxoPVAWl2SscwHu8hHHooUKkX147W9JwG13HfKSvwZhWV3JSlEMOLZo01FsxAKaJor6FJmo%2BlCmLJfPXqjHBoz5OSzgiP%2BNDQDGQgo08fnqLvV4vzHs%2Bd7OZwKTidvZbJwBf7mOnINZLW06EgBoqb%2B8vDDpm&X-Amz-Signature=900e75459e39677aad41d75d4ad5fd85b4d13a9c8b4fbde3957fdcd49eb1437d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

loadbalancer 可以使用云主机厂商提供的负载均衡器产品。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/ed9c7b89-3d1e-407f-bbac-cb706173f414/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXK5HXBX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFgIEw%2BQb9S3SbbJ8eTp%2FY6C2NiCo%2FMhJkF0jFf%2FZ7njAiBd4rdkQnkcmJ3L5PEpNjlVGvY3Byw%2BWj01pvKvr5e0aiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMi%2FGmeJpgLdKqMB29KtwDUJwV%2BKkuD61aDWlVj58uBqM8XIPKSyosnwXDgqdYVgIwdokwI51SmbHGuro%2BX3lc%2FPfC%2F5dolo4VARVmgHYJauqjILdtG0aheUaNayXbVYUpQPiaDTq3JRtYjc31o0lowbk6CfsNGgtUOjVKI2aH5tpjELBizB3dafhnPMsNdUPJyyczVO6DgB4QWa2upx1Q3hzT00EiHGF2kk354WFDGhpg1jexh5mDnME%2B8RTM8rYD4MAWjYX87VGiTP9WbvtnFgkFz31gFjpr3y697vBBXLrFQyUxHQvHr389MTDTtR%2BPhrmyP3VsJOWsIxEkFZZ9c3Fzfg29i4ZTnM7e8BF7DLOINRlZh09ZasZO6ePp0%2BPG2QakvON%2BCF9ct%2BrCXYzO1974tK9lSM7nWrfWR1CrvKIvAr2Acc2EcvIQTQyn77ZJ45MQox%2Bf2jRelolfct0sx9538qGP6afp9pG1SqBkBvy46u5zSjIADAUnjqVHr8M2hDyF5bMJNtfDcKDUfMe807bxgkum6jSGf8oF4%2F9DkP1YRtI8RN3bM%2FF1UrgoFH4t6nncE5pfg00gmTt1iEnNab60%2BtAsm4Ab1JzCXoAunk0IOgQUFPPfbm1sRdM9pNfEIyGFo4oNYr9Wc88whLn%2F0gY6pgHVJNv%2FpQbVCF1xNOdB1N9pktYdN6xROaCRF%2BcuqSjQFMKzv1RpMtlFslTroNch7ty9YxoPVAWl2SscwHu8hHHooUKkX147W9JwG13HfKSvwZhWV3JSlEMOLZo01FsxAKaJor6FJmo%2BlCmLJfPXqjHBoz5OSzgiP%2BNDQDGQgo08fnqLvV4vzHs%2Bd7OZwKTidvZbJwBf7mOnINZLW06EgBoqb%2B8vDDpm&X-Amz-Signature=2797ece6e444c0fbcc2b0a422fece4f4af729afb792aad7f148f0c6fd46b21f8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

最后 ingress 请求。经过 ingress 上配置路由规则，把请求打到不同的 service 上。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/86856973-4156-4034-969f-d0b7332bee2d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXK5HXBX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFgIEw%2BQb9S3SbbJ8eTp%2FY6C2NiCo%2FMhJkF0jFf%2FZ7njAiBd4rdkQnkcmJ3L5PEpNjlVGvY3Byw%2BWj01pvKvr5e0aiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMi%2FGmeJpgLdKqMB29KtwDUJwV%2BKkuD61aDWlVj58uBqM8XIPKSyosnwXDgqdYVgIwdokwI51SmbHGuro%2BX3lc%2FPfC%2F5dolo4VARVmgHYJauqjILdtG0aheUaNayXbVYUpQPiaDTq3JRtYjc31o0lowbk6CfsNGgtUOjVKI2aH5tpjELBizB3dafhnPMsNdUPJyyczVO6DgB4QWa2upx1Q3hzT00EiHGF2kk354WFDGhpg1jexh5mDnME%2B8RTM8rYD4MAWjYX87VGiTP9WbvtnFgkFz31gFjpr3y697vBBXLrFQyUxHQvHr389MTDTtR%2BPhrmyP3VsJOWsIxEkFZZ9c3Fzfg29i4ZTnM7e8BF7DLOINRlZh09ZasZO6ePp0%2BPG2QakvON%2BCF9ct%2BrCXYzO1974tK9lSM7nWrfWR1CrvKIvAr2Acc2EcvIQTQyn77ZJ45MQox%2Bf2jRelolfct0sx9538qGP6afp9pG1SqBkBvy46u5zSjIADAUnjqVHr8M2hDyF5bMJNtfDcKDUfMe807bxgkum6jSGf8oF4%2F9DkP1YRtI8RN3bM%2FF1UrgoFH4t6nncE5pfg00gmTt1iEnNab60%2BtAsm4Ab1JzCXoAunk0IOgQUFPPfbm1sRdM9pNfEIyGFo4oNYr9Wc88whLn%2F0gY6pgHVJNv%2FpQbVCF1xNOdB1N9pktYdN6xROaCRF%2BcuqSjQFMKzv1RpMtlFslTroNch7ty9YxoPVAWl2SscwHu8hHHooUKkX147W9JwG13HfKSvwZhWV3JSlEMOLZo01FsxAKaJor6FJmo%2BlCmLJfPXqjHBoz5OSzgiP%2BNDQDGQgo08fnqLvV4vzHs%2Bd7OZwKTidvZbJwBf7mOnINZLW06EgBoqb%2B8vDDpm&X-Amz-Signature=e20e2549b53c9d6c9a17dd98922b5c65de71546ce81764fdac86cdf9f7a5fcfd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

OK。回来，将目录切换到 k8s，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/8cb86466-ada1-4d4e-8010-430de4f3231c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXK5HXBX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFgIEw%2BQb9S3SbbJ8eTp%2FY6C2NiCo%2FMhJkF0jFf%2FZ7njAiBd4rdkQnkcmJ3L5PEpNjlVGvY3Byw%2BWj01pvKvr5e0aiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMi%2FGmeJpgLdKqMB29KtwDUJwV%2BKkuD61aDWlVj58uBqM8XIPKSyosnwXDgqdYVgIwdokwI51SmbHGuro%2BX3lc%2FPfC%2F5dolo4VARVmgHYJauqjILdtG0aheUaNayXbVYUpQPiaDTq3JRtYjc31o0lowbk6CfsNGgtUOjVKI2aH5tpjELBizB3dafhnPMsNdUPJyyczVO6DgB4QWa2upx1Q3hzT00EiHGF2kk354WFDGhpg1jexh5mDnME%2B8RTM8rYD4MAWjYX87VGiTP9WbvtnFgkFz31gFjpr3y697vBBXLrFQyUxHQvHr389MTDTtR%2BPhrmyP3VsJOWsIxEkFZZ9c3Fzfg29i4ZTnM7e8BF7DLOINRlZh09ZasZO6ePp0%2BPG2QakvON%2BCF9ct%2BrCXYzO1974tK9lSM7nWrfWR1CrvKIvAr2Acc2EcvIQTQyn77ZJ45MQox%2Bf2jRelolfct0sx9538qGP6afp9pG1SqBkBvy46u5zSjIADAUnjqVHr8M2hDyF5bMJNtfDcKDUfMe807bxgkum6jSGf8oF4%2F9DkP1YRtI8RN3bM%2FF1UrgoFH4t6nncE5pfg00gmTt1iEnNab60%2BtAsm4Ab1JzCXoAunk0IOgQUFPPfbm1sRdM9pNfEIyGFo4oNYr9Wc88whLn%2F0gY6pgHVJNv%2FpQbVCF1xNOdB1N9pktYdN6xROaCRF%2BcuqSjQFMKzv1RpMtlFslTroNch7ty9YxoPVAWl2SscwHu8hHHooUKkX147W9JwG13HfKSvwZhWV3JSlEMOLZo01FsxAKaJor6FJmo%2BlCmLJfPXqjHBoz5OSzgiP%2BNDQDGQgo08fnqLvV4vzHs%2Bd7OZwKTidvZbJwBf7mOnINZLW06EgBoqb%2B8vDDpm&X-Amz-Signature=5c45828eba303f429fe4b75c267e72fbb01d6e54cdda9108b1a0ad9649949a01&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

再用 kubectl apply -f 跟上 eureka single，点 yaml 去应用yaml 执行。创建完成,访问 localhost 30001 可以正常访问。到目前为止，我们已经搭建了一个单机版的 eureka server。在实际项目中，我们往往需要搭建高可用的 eureka server，这个时候该怎么玩？

先来复习一下 eureka server 的高可用原理。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/46512fd2-38a2-450a-a579-614dbc02f719/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXK5HXBX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFgIEw%2BQb9S3SbbJ8eTp%2FY6C2NiCo%2FMhJkF0jFf%2FZ7njAiBd4rdkQnkcmJ3L5PEpNjlVGvY3Byw%2BWj01pvKvr5e0aiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMi%2FGmeJpgLdKqMB29KtwDUJwV%2BKkuD61aDWlVj58uBqM8XIPKSyosnwXDgqdYVgIwdokwI51SmbHGuro%2BX3lc%2FPfC%2F5dolo4VARVmgHYJauqjILdtG0aheUaNayXbVYUpQPiaDTq3JRtYjc31o0lowbk6CfsNGgtUOjVKI2aH5tpjELBizB3dafhnPMsNdUPJyyczVO6DgB4QWa2upx1Q3hzT00EiHGF2kk354WFDGhpg1jexh5mDnME%2B8RTM8rYD4MAWjYX87VGiTP9WbvtnFgkFz31gFjpr3y697vBBXLrFQyUxHQvHr389MTDTtR%2BPhrmyP3VsJOWsIxEkFZZ9c3Fzfg29i4ZTnM7e8BF7DLOINRlZh09ZasZO6ePp0%2BPG2QakvON%2BCF9ct%2BrCXYzO1974tK9lSM7nWrfWR1CrvKIvAr2Acc2EcvIQTQyn77ZJ45MQox%2Bf2jRelolfct0sx9538qGP6afp9pG1SqBkBvy46u5zSjIADAUnjqVHr8M2hDyF5bMJNtfDcKDUfMe807bxgkum6jSGf8oF4%2F9DkP1YRtI8RN3bM%2FF1UrgoFH4t6nncE5pfg00gmTt1iEnNab60%2BtAsm4Ab1JzCXoAunk0IOgQUFPPfbm1sRdM9pNfEIyGFo4oNYr9Wc88whLn%2F0gY6pgHVJNv%2FpQbVCF1xNOdB1N9pktYdN6xROaCRF%2BcuqSjQFMKzv1RpMtlFslTroNch7ty9YxoPVAWl2SscwHu8hHHooUKkX147W9JwG13HfKSvwZhWV3JSlEMOLZo01FsxAKaJor6FJmo%2BlCmLJfPXqjHBoz5OSzgiP%2BNDQDGQgo08fnqLvV4vzHs%2Bd7OZwKTidvZbJwBf7mOnINZLW06EgBoqb%2B8vDDpm&X-Amz-Signature=1b112f4ec14575c312510a97032673908b39e020dd7ce7b63e7c91ce2a9b3f95&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

这张图大家一定非常熟悉了， eureka server 集群通过让 eureka server 实例之间彼此互相注册，并互相复制数据，从而构建集群。所以构建 eureka-server 集群的核心就是要让多个 eureka-server 实例能够互相连接。只要能够互相连接，数据就可以互相的复制。


要想实现这一点，有两种方式，一是利用  deployment  关闭创建一个新的文件。 eureka-ha1.yaml 写上注释，利用 deployment 实现高可用 eureka server kdep 先来编写一个 deployment ，叫做 eureka-server2 ,image my-eureka replicas 实力个数2 

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/0fee3bce-8c11-44ab-8449-1d988d1fff5d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXK5HXBX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFgIEw%2BQb9S3SbbJ8eTp%2FY6C2NiCo%2FMhJkF0jFf%2FZ7njAiBd4rdkQnkcmJ3L5PEpNjlVGvY3Byw%2BWj01pvKvr5e0aiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMi%2FGmeJpgLdKqMB29KtwDUJwV%2BKkuD61aDWlVj58uBqM8XIPKSyosnwXDgqdYVgIwdokwI51SmbHGuro%2BX3lc%2FPfC%2F5dolo4VARVmgHYJauqjILdtG0aheUaNayXbVYUpQPiaDTq3JRtYjc31o0lowbk6CfsNGgtUOjVKI2aH5tpjELBizB3dafhnPMsNdUPJyyczVO6DgB4QWa2upx1Q3hzT00EiHGF2kk354WFDGhpg1jexh5mDnME%2B8RTM8rYD4MAWjYX87VGiTP9WbvtnFgkFz31gFjpr3y697vBBXLrFQyUxHQvHr389MTDTtR%2BPhrmyP3VsJOWsIxEkFZZ9c3Fzfg29i4ZTnM7e8BF7DLOINRlZh09ZasZO6ePp0%2BPG2QakvON%2BCF9ct%2BrCXYzO1974tK9lSM7nWrfWR1CrvKIvAr2Acc2EcvIQTQyn77ZJ45MQox%2Bf2jRelolfct0sx9538qGP6afp9pG1SqBkBvy46u5zSjIADAUnjqVHr8M2hDyF5bMJNtfDcKDUfMe807bxgkum6jSGf8oF4%2F9DkP1YRtI8RN3bM%2FF1UrgoFH4t6nncE5pfg00gmTt1iEnNab60%2BtAsm4Ab1JzCXoAunk0IOgQUFPPfbm1sRdM9pNfEIyGFo4oNYr9Wc88whLn%2F0gY6pgHVJNv%2FpQbVCF1xNOdB1N9pktYdN6xROaCRF%2BcuqSjQFMKzv1RpMtlFslTroNch7ty9YxoPVAWl2SscwHu8hHHooUKkX147W9JwG13HfKSvwZhWV3JSlEMOLZo01FsxAKaJor6FJmo%2BlCmLJfPXqjHBoz5OSzgiP%2BNDQDGQgo08fnqLvV4vzHs%2Bd7OZwKTidvZbJwBf7mOnINZLW06EgBoqb%2B8vDDpm&X-Amz-Signature=776d61b54d4c889a435ccf28efa3384e2e78c6013796823ddade8ed5fc641a3f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

我们创建一个 2个实例的 eureka-server 集群。


按照道理来说，对于高可用的 eureka-server，我们需要去修改 application.yaml 。但是修改了 yaml 之后，我们又需要重新构建镜像，这样有点麻烦。为了不重新构建镜像，我们这里直接用环境变量的方式去覆盖 application.yaml 的配置。 env name引号--跟上 application 里面的配置key。比方我们想要覆盖 eureka client register with eureka，就可以这样写。

eureka client register with eureka value.


two 这样在启动的时候就会以这里的环境变量为准，环境变量的优先级高于这里的配置。port 我们还需要把 fetch registry 设成 true name 蛋糕 eureka clients 点 fetch registry value shoe。

```javascript
#  利用 deployment 实现高可用的 eureka-server
apiVersion: apps/v1
kind: Deployment
metadata:
  name: my-eureka2
  labels:
    app: my-eureka2
spec:
  replicas: 2
  template:
    metadata:
      name: my-eureka2
      labels:
        app: my-eureka2
    spec:
      containers:
        - name: my-eureka2
          image: my-eureka
          imagePullPolicy: IfNotPresent
          env:
            - name: "--eureka.client.register-with-eureka"
              value: "true"
            - name:  "--eureka-client.fetch-registry"
              value: "true"
            - name: "--eureka.client.service-url.defaultZone"
              value: "http://eureka-server2:8761/eureka"
      restartPolicy: Always
  selector:
    matchLabels:
      app: my-eureka2
```

此外要覆盖 service URL default zone eureka clients 第二value。关键是这里的 value 怎么写。大家想要让两个 eureka server 实例互相连接，我们该怎么办？其实只要创建一个 service 就 OK 了。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/dbf848b6-877b-4ea1-b0d5-1b2a0b44123e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXK5HXBX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFgIEw%2BQb9S3SbbJ8eTp%2FY6C2NiCo%2FMhJkF0jFf%2FZ7njAiBd4rdkQnkcmJ3L5PEpNjlVGvY3Byw%2BWj01pvKvr5e0aiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMi%2FGmeJpgLdKqMB29KtwDUJwV%2BKkuD61aDWlVj58uBqM8XIPKSyosnwXDgqdYVgIwdokwI51SmbHGuro%2BX3lc%2FPfC%2F5dolo4VARVmgHYJauqjILdtG0aheUaNayXbVYUpQPiaDTq3JRtYjc31o0lowbk6CfsNGgtUOjVKI2aH5tpjELBizB3dafhnPMsNdUPJyyczVO6DgB4QWa2upx1Q3hzT00EiHGF2kk354WFDGhpg1jexh5mDnME%2B8RTM8rYD4MAWjYX87VGiTP9WbvtnFgkFz31gFjpr3y697vBBXLrFQyUxHQvHr389MTDTtR%2BPhrmyP3VsJOWsIxEkFZZ9c3Fzfg29i4ZTnM7e8BF7DLOINRlZh09ZasZO6ePp0%2BPG2QakvON%2BCF9ct%2BrCXYzO1974tK9lSM7nWrfWR1CrvKIvAr2Acc2EcvIQTQyn77ZJ45MQox%2Bf2jRelolfct0sx9538qGP6afp9pG1SqBkBvy46u5zSjIADAUnjqVHr8M2hDyF5bMJNtfDcKDUfMe807bxgkum6jSGf8oF4%2F9DkP1YRtI8RN3bM%2FF1UrgoFH4t6nncE5pfg00gmTt1iEnNab60%2BtAsm4Ab1JzCXoAunk0IOgQUFPPfbm1sRdM9pNfEIyGFo4oNYr9Wc88whLn%2F0gY6pgHVJNv%2FpQbVCF1xNOdB1N9pktYdN6xROaCRF%2BcuqSjQFMKzv1RpMtlFslTroNch7ty9YxoPVAWl2SscwHu8hHHooUKkX147W9JwG13HfKSvwZhWV3JSlEMOLZo01FsxAKaJor6FJmo%2BlCmLJfPXqjHBoz5OSzgiP%2BNDQDGQgo08fnqLvV4vzHs%2Bd7OZwKTidvZbJwBf7mOnINZLW06EgBoqb%2B8vDDpm&X-Amz-Signature=948b1ad7f5a30cf36cf8c9374e9566150dc185d8f4260a12d40977bbbfa26cea&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

在 k8s 里面，比方微服 x 的某一个pod，想要调用 service y 的某一个pod，只要构造 service y 的服务名称冒号 service 的端口跟这叉叉叉，就可以请求到 Pod1 或者 Pod2 的叉叉叉了。并且 service 会自带负载均衡对吧？而现在我们想要实现两个 eureka server 实例之间的互联，该怎么办？我们可以把实例1 想象成是这里的 pod1，实例2 想象成这里的 pod2。


问题就变成了 pod1 和 pod2 该怎么样通信？对于同一个 service 里面的不同pod，想要通信也可以使用 http 服务名称端口的方式进行请求。只不过当访问地址的时候，请求可能会打到自己上面去。比方 pod1 通过这个地址去请求，可能会打到自己上面去，也可能打到 pod2 上面去。


对于 eureka server 来说，就变成了比如卡server。实例1 想要往实例2 上面同步数据，结果同步的时候，可能有的时候还是请求到了自己身上去了，不过没有关系，由于 service 有负载中型的机制，它总会有请求打到 pod2 上面去的。这样一来，最终两个实例的数据还还是会打到一致。


OK，了解这一点之后，我们来编写这里的 value http eureka server2 冒号八七 6 幺- eureka--这里的 eureka server2 是一个 service 名称，于是接下来我们就需要编写一个名为 eureka server2 的 service, kscr ,

```javascript
#  利用 deployment 实现高可用的 eureka-server
apiVersion: v1
kind: Service
metadata:
  name: eureka-server2
spec:
  selector:
    app: eureka-server2
  ports:
    - port: 8761
      targetPort: 8761
      nodePort: 30002
  type: NodePort
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: eureka-server2
  labels:
    app: eureka-server2
spec:
  replicas: 2
  template:
    metadata:
      name: eureka-server2
      labels:
        app: eureka-server2
    spec:
      containers:
        - name: eureka-server2
          image: my-eureka
          imagePullPolicy: IfNotPresent
          env:
            - name: "--eureka.client.register-with-eureka"
              value: "true"
            - name:  "--eureka-client.fetch-registry"
              value: "true"
            - name: "--eureka.client.service-url.defaultZone"
              value: "http://eureka-server2:8761/eureka"
      restartPolicy: Always
  selector:
    matchLabels:
      app: eureka-server2
```

名称 比如 eureka-server2 ， 这个 service 选中带有 app 等于 eureka-serve2 的那些 pod，也就是这些

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/d010b462-0149-41df-8614-880c8ce8870e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXK5HXBX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFgIEw%2BQb9S3SbbJ8eTp%2FY6C2NiCo%2FMhJkF0jFf%2FZ7njAiBd4rdkQnkcmJ3L5PEpNjlVGvY3Byw%2BWj01pvKvr5e0aiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMi%2FGmeJpgLdKqMB29KtwDUJwV%2BKkuD61aDWlVj58uBqM8XIPKSyosnwXDgqdYVgIwdokwI51SmbHGuro%2BX3lc%2FPfC%2F5dolo4VARVmgHYJauqjILdtG0aheUaNayXbVYUpQPiaDTq3JRtYjc31o0lowbk6CfsNGgtUOjVKI2aH5tpjELBizB3dafhnPMsNdUPJyyczVO6DgB4QWa2upx1Q3hzT00EiHGF2kk354WFDGhpg1jexh5mDnME%2B8RTM8rYD4MAWjYX87VGiTP9WbvtnFgkFz31gFjpr3y697vBBXLrFQyUxHQvHr389MTDTtR%2BPhrmyP3VsJOWsIxEkFZZ9c3Fzfg29i4ZTnM7e8BF7DLOINRlZh09ZasZO6ePp0%2BPG2QakvON%2BCF9ct%2BrCXYzO1974tK9lSM7nWrfWR1CrvKIvAr2Acc2EcvIQTQyn77ZJ45MQox%2Bf2jRelolfct0sx9538qGP6afp9pG1SqBkBvy46u5zSjIADAUnjqVHr8M2hDyF5bMJNtfDcKDUfMe807bxgkum6jSGf8oF4%2F9DkP1YRtI8RN3bM%2FF1UrgoFH4t6nncE5pfg00gmTt1iEnNab60%2BtAsm4Ab1JzCXoAunk0IOgQUFPPfbm1sRdM9pNfEIyGFo4oNYr9Wc88whLn%2F0gY6pgHVJNv%2FpQbVCF1xNOdB1N9pktYdN6xROaCRF%2BcuqSjQFMKzv1RpMtlFslTroNch7ty9YxoPVAWl2SscwHu8hHHooUKkX147W9JwG13HfKSvwZhWV3JSlEMOLZo01FsxAKaJor6FJmo%2BlCmLJfPXqjHBoz5OSzgiP%2BNDQDGQgo08fnqLvV4vzHs%2Bd7OZwKTidvZbJwBf7mOnINZLW06EgBoqb%2B8vDDpm&X-Amz-Signature=d56b332b40208039fff2737ed0f22758161a8df10ca0b648ed82eb71701b618c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

pod 对吧？没问题。端口 8761 这里的端口

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b6a6f0e4-39fb-4c55-9f86-0fd3c699fc8d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXK5HXBX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFgIEw%2BQb9S3SbbJ8eTp%2FY6C2NiCo%2FMhJkF0jFf%2FZ7njAiBd4rdkQnkcmJ3L5PEpNjlVGvY3Byw%2BWj01pvKvr5e0aiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMi%2FGmeJpgLdKqMB29KtwDUJwV%2BKkuD61aDWlVj58uBqM8XIPKSyosnwXDgqdYVgIwdokwI51SmbHGuro%2BX3lc%2FPfC%2F5dolo4VARVmgHYJauqjILdtG0aheUaNayXbVYUpQPiaDTq3JRtYjc31o0lowbk6CfsNGgtUOjVKI2aH5tpjELBizB3dafhnPMsNdUPJyyczVO6DgB4QWa2upx1Q3hzT00EiHGF2kk354WFDGhpg1jexh5mDnME%2B8RTM8rYD4MAWjYX87VGiTP9WbvtnFgkFz31gFjpr3y697vBBXLrFQyUxHQvHr389MTDTtR%2BPhrmyP3VsJOWsIxEkFZZ9c3Fzfg29i4ZTnM7e8BF7DLOINRlZh09ZasZO6ePp0%2BPG2QakvON%2BCF9ct%2BrCXYzO1974tK9lSM7nWrfWR1CrvKIvAr2Acc2EcvIQTQyn77ZJ45MQox%2Bf2jRelolfct0sx9538qGP6afp9pG1SqBkBvy46u5zSjIADAUnjqVHr8M2hDyF5bMJNtfDcKDUfMe807bxgkum6jSGf8oF4%2F9DkP1YRtI8RN3bM%2FF1UrgoFH4t6nncE5pfg00gmTt1iEnNab60%2BtAsm4Ab1JzCXoAunk0IOgQUFPPfbm1sRdM9pNfEIyGFo4oNYr9Wc88whLn%2F0gY6pgHVJNv%2FpQbVCF1xNOdB1N9pktYdN6xROaCRF%2BcuqSjQFMKzv1RpMtlFslTroNch7ty9YxoPVAWl2SscwHu8hHHooUKkX147W9JwG13HfKSvwZhWV3JSlEMOLZo01FsxAKaJor6FJmo%2BlCmLJfPXqjHBoz5OSzgiP%2BNDQDGQgo08fnqLvV4vzHs%2Bd7OZwKTidvZbJwBf7mOnINZLW06EgBoqb%2B8vDDpm&X-Amz-Signature=5bf69dd10852e79a2f5ab61462f6de6a2776ed375ff2d897f73c03f197384b4a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

要和这里的

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/3eaa73bc-bc4a-4edc-9f48-3e2896132437/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXK5HXBX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFgIEw%2BQb9S3SbbJ8eTp%2FY6C2NiCo%2FMhJkF0jFf%2FZ7njAiBd4rdkQnkcmJ3L5PEpNjlVGvY3Byw%2BWj01pvKvr5e0aiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMi%2FGmeJpgLdKqMB29KtwDUJwV%2BKkuD61aDWlVj58uBqM8XIPKSyosnwXDgqdYVgIwdokwI51SmbHGuro%2BX3lc%2FPfC%2F5dolo4VARVmgHYJauqjILdtG0aheUaNayXbVYUpQPiaDTq3JRtYjc31o0lowbk6CfsNGgtUOjVKI2aH5tpjELBizB3dafhnPMsNdUPJyyczVO6DgB4QWa2upx1Q3hzT00EiHGF2kk354WFDGhpg1jexh5mDnME%2B8RTM8rYD4MAWjYX87VGiTP9WbvtnFgkFz31gFjpr3y697vBBXLrFQyUxHQvHr389MTDTtR%2BPhrmyP3VsJOWsIxEkFZZ9c3Fzfg29i4ZTnM7e8BF7DLOINRlZh09ZasZO6ePp0%2BPG2QakvON%2BCF9ct%2BrCXYzO1974tK9lSM7nWrfWR1CrvKIvAr2Acc2EcvIQTQyn77ZJ45MQox%2Bf2jRelolfct0sx9538qGP6afp9pG1SqBkBvy46u5zSjIADAUnjqVHr8M2hDyF5bMJNtfDcKDUfMe807bxgkum6jSGf8oF4%2F9DkP1YRtI8RN3bM%2FF1UrgoFH4t6nncE5pfg00gmTt1iEnNab60%2BtAsm4Ab1JzCXoAunk0IOgQUFPPfbm1sRdM9pNfEIyGFo4oNYr9Wc88whLn%2F0gY6pgHVJNv%2FpQbVCF1xNOdB1N9pktYdN6xROaCRF%2BcuqSjQFMKzv1RpMtlFslTroNch7ty9YxoPVAWl2SscwHu8hHHooUKkX147W9JwG13HfKSvwZhWV3JSlEMOLZo01FsxAKaJor6FJmo%2BlCmLJfPXqjHBoz5OSzgiP%2BNDQDGQgo08fnqLvV4vzHs%2Bd7OZwKTidvZbJwBf7mOnINZLW06EgBoqb%2B8vDDpm&X-Amz-Signature=fef1a7d1557afc1783768cacf2d278dc4951f610a262a52b85290e62f0ca6639&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

端口保持一致。 TargetPort:8761 , TargetPort 要和我们 application.yaml 的这里的端口保持一致，同学们不要搞混。

NodePort:30002，编写完成，一起看看。因为我的机器内存有限了，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/d5b3abe0-987e-4cd8-b6b8-021ed1daf17c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXK5HXBX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFgIEw%2BQb9S3SbbJ8eTp%2FY6C2NiCo%2FMhJkF0jFf%2FZ7njAiBd4rdkQnkcmJ3L5PEpNjlVGvY3Byw%2BWj01pvKvr5e0aiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMi%2FGmeJpgLdKqMB29KtwDUJwV%2BKkuD61aDWlVj58uBqM8XIPKSyosnwXDgqdYVgIwdokwI51SmbHGuro%2BX3lc%2FPfC%2F5dolo4VARVmgHYJauqjILdtG0aheUaNayXbVYUpQPiaDTq3JRtYjc31o0lowbk6CfsNGgtUOjVKI2aH5tpjELBizB3dafhnPMsNdUPJyyczVO6DgB4QWa2upx1Q3hzT00EiHGF2kk354WFDGhpg1jexh5mDnME%2B8RTM8rYD4MAWjYX87VGiTP9WbvtnFgkFz31gFjpr3y697vBBXLrFQyUxHQvHr389MTDTtR%2BPhrmyP3VsJOWsIxEkFZZ9c3Fzfg29i4ZTnM7e8BF7DLOINRlZh09ZasZO6ePp0%2BPG2QakvON%2BCF9ct%2BrCXYzO1974tK9lSM7nWrfWR1CrvKIvAr2Acc2EcvIQTQyn77ZJ45MQox%2Bf2jRelolfct0sx9538qGP6afp9pG1SqBkBvy46u5zSjIADAUnjqVHr8M2hDyF5bMJNtfDcKDUfMe807bxgkum6jSGf8oF4%2F9DkP1YRtI8RN3bM%2FF1UrgoFH4t6nncE5pfg00gmTt1iEnNab60%2BtAsm4Ab1JzCXoAunk0IOgQUFPPfbm1sRdM9pNfEIyGFo4oNYr9Wc88whLn%2F0gY6pgHVJNv%2FpQbVCF1xNOdB1N9pktYdN6xROaCRF%2BcuqSjQFMKzv1RpMtlFslTroNch7ty9YxoPVAWl2SscwHu8hHHooUKkX147W9JwG13HfKSvwZhWV3JSlEMOLZo01FsxAKaJor6FJmo%2BlCmLJfPXqjHBoz5OSzgiP%2BNDQDGQgo08fnqLvV4vzHs%2Bd7OZwKTidvZbJwBf7mOnINZLW06EgBoqb%2B8vDDpm&X-Amz-Signature=36bd92d3ab2f9f5cb9fd6fb16b2c53cf05db8dd08dfe99fe2bc0d61ba2088bbe&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

所以我们可以先用 kubectl delete -f eureka-single.yaml，把之前的单机版eureka先销毁掉。然后再用 kubectl apply -f eureka-ha1.yaml 去启动。


说找不到文件，这里的名字写错了。 shift F6 重命名 eureka reflector OK 再次执行 kubectl apply，创建完成。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/9fab8374-2d51-4c0e-bef6-a156e2c496eb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXK5HXBX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFgIEw%2BQb9S3SbbJ8eTp%2FY6C2NiCo%2FMhJkF0jFf%2FZ7njAiBd4rdkQnkcmJ3L5PEpNjlVGvY3Byw%2BWj01pvKvr5e0aiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMi%2FGmeJpgLdKqMB29KtwDUJwV%2BKkuD61aDWlVj58uBqM8XIPKSyosnwXDgqdYVgIwdokwI51SmbHGuro%2BX3lc%2FPfC%2F5dolo4VARVmgHYJauqjILdtG0aheUaNayXbVYUpQPiaDTq3JRtYjc31o0lowbk6CfsNGgtUOjVKI2aH5tpjELBizB3dafhnPMsNdUPJyyczVO6DgB4QWa2upx1Q3hzT00EiHGF2kk354WFDGhpg1jexh5mDnME%2B8RTM8rYD4MAWjYX87VGiTP9WbvtnFgkFz31gFjpr3y697vBBXLrFQyUxHQvHr389MTDTtR%2BPhrmyP3VsJOWsIxEkFZZ9c3Fzfg29i4ZTnM7e8BF7DLOINRlZh09ZasZO6ePp0%2BPG2QakvON%2BCF9ct%2BrCXYzO1974tK9lSM7nWrfWR1CrvKIvAr2Acc2EcvIQTQyn77ZJ45MQox%2Bf2jRelolfct0sx9538qGP6afp9pG1SqBkBvy46u5zSjIADAUnjqVHr8M2hDyF5bMJNtfDcKDUfMe807bxgkum6jSGf8oF4%2F9DkP1YRtI8RN3bM%2FF1UrgoFH4t6nncE5pfg00gmTt1iEnNab60%2BtAsm4Ab1JzCXoAunk0IOgQUFPPfbm1sRdM9pNfEIyGFo4oNYr9Wc88whLn%2F0gY6pgHVJNv%2FpQbVCF1xNOdB1N9pktYdN6xROaCRF%2BcuqSjQFMKzv1RpMtlFslTroNch7ty9YxoPVAWl2SscwHu8hHHooUKkX147W9JwG13HfKSvwZhWV3JSlEMOLZo01FsxAKaJor6FJmo%2BlCmLJfPXqjHBoz5OSzgiP%2BNDQDGQgo08fnqLvV4vzHs%2Bd7OZwKTidvZbJwBf7mOnINZLW06EgBoqb%2B8vDDpm&X-Amz-Signature=cd6a99f18156a2476012eaba1d6a98e8e2770d19f6a356bc8211839412589725&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

修改端口 30002 可以看到。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/70e1afad-190d-4bba-b1f4-f64c0c09c55b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXK5HXBX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFgIEw%2BQb9S3SbbJ8eTp%2FY6C2NiCo%2FMhJkF0jFf%2FZ7njAiBd4rdkQnkcmJ3L5PEpNjlVGvY3Byw%2BWj01pvKvr5e0aiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMi%2FGmeJpgLdKqMB29KtwDUJwV%2BKkuD61aDWlVj58uBqM8XIPKSyosnwXDgqdYVgIwdokwI51SmbHGuro%2BX3lc%2FPfC%2F5dolo4VARVmgHYJauqjILdtG0aheUaNayXbVYUpQPiaDTq3JRtYjc31o0lowbk6CfsNGgtUOjVKI2aH5tpjELBizB3dafhnPMsNdUPJyyczVO6DgB4QWa2upx1Q3hzT00EiHGF2kk354WFDGhpg1jexh5mDnME%2B8RTM8rYD4MAWjYX87VGiTP9WbvtnFgkFz31gFjpr3y697vBBXLrFQyUxHQvHr389MTDTtR%2BPhrmyP3VsJOWsIxEkFZZ9c3Fzfg29i4ZTnM7e8BF7DLOINRlZh09ZasZO6ePp0%2BPG2QakvON%2BCF9ct%2BrCXYzO1974tK9lSM7nWrfWR1CrvKIvAr2Acc2EcvIQTQyn77ZJ45MQox%2Bf2jRelolfct0sx9538qGP6afp9pG1SqBkBvy46u5zSjIADAUnjqVHr8M2hDyF5bMJNtfDcKDUfMe807bxgkum6jSGf8oF4%2F9DkP1YRtI8RN3bM%2FF1UrgoFH4t6nncE5pfg00gmTt1iEnNab60%2BtAsm4Ab1JzCXoAunk0IOgQUFPPfbm1sRdM9pNfEIyGFo4oNYr9Wc88whLn%2F0gY6pgHVJNv%2FpQbVCF1xNOdB1N9pktYdN6xROaCRF%2BcuqSjQFMKzv1RpMtlFslTroNch7ty9YxoPVAWl2SscwHu8hHHooUKkX147W9JwG13HfKSvwZhWV3JSlEMOLZo01FsxAKaJor6FJmo%2BlCmLJfPXqjHBoz5OSzgiP%2BNDQDGQgo08fnqLvV4vzHs%2Bd7OZwKTidvZbJwBf7mOnINZLW06EgBoqb%2B8vDDpm&X-Amz-Signature=09e2ca48224ec3f5e51d4fbb64cce11d6d88d0b3d49b7fae2c6c69c8f7e95e34&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

server 集群搭建 OK 集群有两个实例。好，这是第一种方式。



第二种方式利用 StatefulSet 换的一个新的文件。 eureka-ha2.yaml，显然注释利用 StatefulSet 实现 eureka server 集群。回顾一下 StatefulSet 叫有状态集对吧？一起来复习一下。


StatefulSet 的特性

```javascript
# 利用 StatefulSet 实现 Eureka Server 集群
#1：pod 名称固定，会用 pod name-{index} index从，指的是这里的 name， 下标从 0 开始。OK，这是第一个特性。
#2：启动有顺序，会依次启动，下边为零0 , 1, 2..
#3： 停止有顺序，会依次停止，-n, - n-1 …，也会先停下边大的，再停下边小的。
#4： 有固定的网络标识，每个 pod 会存在一条 DNS 记录，DNS 记录是 pod-name{index}.service名称
```

一是 pod 名称固定，会用 part name，指的是这里的name。一个下标从 0 开始。OK，这是第一个特性。

第二 个特性，启动有顺序，会依次启动，下边为零0 , 1, 2 点点点。也就是先启动 pod name -0， 0 启动完了再启动 pod name -1，依此类推。

三是 停止有顺序，会依次停止，-n, -n-1 …，也会先停下边大的，再停下边小的。

四是 有固定的网络标识，每个 pod 会存在一条 DNS 记录，DNS 记录是 pod name - index 点， service 名称 OK。


回顾完 StatefulSet 的特性之后，我们来编写一个 StatefulSet。由于 idea 的快捷键，它不支持直接编写 StatefulSet，所以我们可以先创建一个 deployment，再用 deployment 去进行修改。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/a8b01f53-9eed-49e2-ac4b-db75bcad4837/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXK5HXBX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFgIEw%2BQb9S3SbbJ8eTp%2FY6C2NiCo%2FMhJkF0jFf%2FZ7njAiBd4rdkQnkcmJ3L5PEpNjlVGvY3Byw%2BWj01pvKvr5e0aiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMi%2FGmeJpgLdKqMB29KtwDUJwV%2BKkuD61aDWlVj58uBqM8XIPKSyosnwXDgqdYVgIwdokwI51SmbHGuro%2BX3lc%2FPfC%2F5dolo4VARVmgHYJauqjILdtG0aheUaNayXbVYUpQPiaDTq3JRtYjc31o0lowbk6CfsNGgtUOjVKI2aH5tpjELBizB3dafhnPMsNdUPJyyczVO6DgB4QWa2upx1Q3hzT00EiHGF2kk354WFDGhpg1jexh5mDnME%2B8RTM8rYD4MAWjYX87VGiTP9WbvtnFgkFz31gFjpr3y697vBBXLrFQyUxHQvHr389MTDTtR%2BPhrmyP3VsJOWsIxEkFZZ9c3Fzfg29i4ZTnM7e8BF7DLOINRlZh09ZasZO6ePp0%2BPG2QakvON%2BCF9ct%2BrCXYzO1974tK9lSM7nWrfWR1CrvKIvAr2Acc2EcvIQTQyn77ZJ45MQox%2Bf2jRelolfct0sx9538qGP6afp9pG1SqBkBvy46u5zSjIADAUnjqVHr8M2hDyF5bMJNtfDcKDUfMe807bxgkum6jSGf8oF4%2F9DkP1YRtI8RN3bM%2FF1UrgoFH4t6nncE5pfg00gmTt1iEnNab60%2BtAsm4Ab1JzCXoAunk0IOgQUFPPfbm1sRdM9pNfEIyGFo4oNYr9Wc88whLn%2F0gY6pgHVJNv%2FpQbVCF1xNOdB1N9pktYdN6xROaCRF%2BcuqSjQFMKzv1RpMtlFslTroNch7ty9YxoPVAWl2SscwHu8hHHooUKkX147W9JwG13HfKSvwZhWV3JSlEMOLZo01FsxAKaJor6FJmo%2BlCmLJfPXqjHBoz5OSzgiP%2BNDQDGQgo08fnqLvV4vzHs%2Bd7OZwKTidvZbJwBf7mOnINZLW06EgBoqb%2B8vDDpm&X-Amz-Signature=38c449ca1c01d3c6ea9c479c376755289872b28455b3653fd0756ff9a53b1b96&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

**kdep** 类目比如 eureka-erver3, image my-eureka，然后 deployment 改成 `StatefulSet`， replicas 改成2。两个实例, StatefulSet 需要引用一个service，所以这里写上 serviceName。 service 的名称也叫 eureka-server3。于是我们需要编写一个名为 `eureka-server3`， service 会命中 app 等于 eureka-server3 pod 的。也就是这些 pod，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/3ae297a2-5ced-4dd5-a23f-80721f997bd9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXK5HXBX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFgIEw%2BQb9S3SbbJ8eTp%2FY6C2NiCo%2FMhJkF0jFf%2FZ7njAiBd4rdkQnkcmJ3L5PEpNjlVGvY3Byw%2BWj01pvKvr5e0aiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMi%2FGmeJpgLdKqMB29KtwDUJwV%2BKkuD61aDWlVj58uBqM8XIPKSyosnwXDgqdYVgIwdokwI51SmbHGuro%2BX3lc%2FPfC%2F5dolo4VARVmgHYJauqjILdtG0aheUaNayXbVYUpQPiaDTq3JRtYjc31o0lowbk6CfsNGgtUOjVKI2aH5tpjELBizB3dafhnPMsNdUPJyyczVO6DgB4QWa2upx1Q3hzT00EiHGF2kk354WFDGhpg1jexh5mDnME%2B8RTM8rYD4MAWjYX87VGiTP9WbvtnFgkFz31gFjpr3y697vBBXLrFQyUxHQvHr389MTDTtR%2BPhrmyP3VsJOWsIxEkFZZ9c3Fzfg29i4ZTnM7e8BF7DLOINRlZh09ZasZO6ePp0%2BPG2QakvON%2BCF9ct%2BrCXYzO1974tK9lSM7nWrfWR1CrvKIvAr2Acc2EcvIQTQyn77ZJ45MQox%2Bf2jRelolfct0sx9538qGP6afp9pG1SqBkBvy46u5zSjIADAUnjqVHr8M2hDyF5bMJNtfDcKDUfMe807bxgkum6jSGf8oF4%2F9DkP1YRtI8RN3bM%2FF1UrgoFH4t6nncE5pfg00gmTt1iEnNab60%2BtAsm4Ab1JzCXoAunk0IOgQUFPPfbm1sRdM9pNfEIyGFo4oNYr9Wc88whLn%2F0gY6pgHVJNv%2FpQbVCF1xNOdB1N9pktYdN6xROaCRF%2BcuqSjQFMKzv1RpMtlFslTroNch7ty9YxoPVAWl2SscwHu8hHHooUKkX147W9JwG13HfKSvwZhWV3JSlEMOLZo01FsxAKaJor6FJmo%2BlCmLJfPXqjHBoz5OSzgiP%2BNDQDGQgo08fnqLvV4vzHs%2Bd7OZwKTidvZbJwBf7mOnINZLW06EgBoqb%2B8vDDpm&X-Amz-Signature=9e8efc2214ab81ab8f2600825258e51fba844c52769c1874ab8678cd576f48e9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

 OK 端口 8761， TargetPort 8761。而 StatefulSet 所引用的 service 要是一个 headless service，所以我们需要指定 `clusterIP` 等于 NodePort，也不能写。写上 注释 clusterIP:none  表示这是一个 Headless service。

```javascript
# 利用 StatefulSet 实现 Eureka Server 集群
#1：pod 名称固定，会用 pod name-{index} index从，指的是这里的 name， 下标从 0 开始。OK，这是第一个特性。
#2：启动有顺序，会依次启动，下边为零0 , 1, 2../
#3： 停止有顺序，会依次停止，-n, - n-1 …，也会先停下边大的，再停下边小的。
#4： 有固定的网络标识，每个 pod 会存在一条 DNS 记录，DNS 记录是 pod-name{index}.service名称
apiVersion: v1
kind: Service
metadata:
  name: eureka-server3
spec:
  selector:
    app: eureka-server3
  ports:
    - port: 8761
      targetPort: 8761
   #  clusterIP 等于 none 表示是一个 Headless service
  clusterIP: none
---
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: eureka-server3
  labels:
    app: eureka-server3
spec:
  replicas: 2
  serviceName: eureka-server3
  template:
    metadata:
      name: eureka-server3
      labels:
        app: eureka-server3
    spec:
      containers:
        - name: eureka-server3
          image: my-eureka
          imagePullPolicy: IfNotPresent
      restartPolicy: Always
  selector:
    matchLabels:
      app: eureka-server3
```

到现在为止，我们的 StatefulSet 就已经编写完成了。

只要 kube apply 跟上这个文件，

就可以去启动有一个 server 集群了。但是我们也需要在本机验证 eureka server 集群搭建的有没有问题。所以该怎么办？

很简单，只要额外创建一个service，

```javascript
apiVersion: v1
kind: Service
metadata:
  name: eureka-server3
spec:
  selector:
    app: eureka-server3
  ports:
    - port: 8761
      targetPort: 8761
      nodePort: 30003
  type: NodePort
```

比方说 name 是 eureka server3-out 表示对外暴露。端口抄一下 type 我们选 NodePort， nodePord 是 30003 ,selector 我们改成比如改 server3，这样 service 会选中这些pod，也就是 StatefulSet 所关联的那些pod。说白了，我们创建了两个service，一个 service 用来去创建 StatefulSets，另外一个 service 用来对外暴露。

OK。最后，我们还需要编写环境变量，到 ha1 文件里面抄一下。copy 粘贴，这里的 value 我们需要修改一下，把它改成 pod 的名称是 eureka。 server3跟上**下标 0 点 再跟上 service 的名称**， service 的名称是他3 。第二个示例粘贴，把下标改成 1，这样一个两个实例的高可用 eureka server 就编写好了。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/6e77e54e-bc6a-45de-b08a-5c3e9394a706/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WXK5HXBX%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFgIEw%2BQb9S3SbbJ8eTp%2FY6C2NiCo%2FMhJkF0jFf%2FZ7njAiBd4rdkQnkcmJ3L5PEpNjlVGvY3Byw%2BWj01pvKvr5e0aiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMi%2FGmeJpgLdKqMB29KtwDUJwV%2BKkuD61aDWlVj58uBqM8XIPKSyosnwXDgqdYVgIwdokwI51SmbHGuro%2BX3lc%2FPfC%2F5dolo4VARVmgHYJauqjILdtG0aheUaNayXbVYUpQPiaDTq3JRtYjc31o0lowbk6CfsNGgtUOjVKI2aH5tpjELBizB3dafhnPMsNdUPJyyczVO6DgB4QWa2upx1Q3hzT00EiHGF2kk354WFDGhpg1jexh5mDnME%2B8RTM8rYD4MAWjYX87VGiTP9WbvtnFgkFz31gFjpr3y697vBBXLrFQyUxHQvHr389MTDTtR%2BPhrmyP3VsJOWsIxEkFZZ9c3Fzfg29i4ZTnM7e8BF7DLOINRlZh09ZasZO6ePp0%2BPG2QakvON%2BCF9ct%2BrCXYzO1974tK9lSM7nWrfWR1CrvKIvAr2Acc2EcvIQTQyn77ZJ45MQox%2Bf2jRelolfct0sx9538qGP6afp9pG1SqBkBvy46u5zSjIADAUnjqVHr8M2hDyF5bMJNtfDcKDUfMe807bxgkum6jSGf8oF4%2F9DkP1YRtI8RN3bM%2FF1UrgoFH4t6nncE5pfg00gmTt1iEnNab60%2BtAsm4Ab1JzCXoAunk0IOgQUFPPfbm1sRdM9pNfEIyGFo4oNYr9Wc88whLn%2F0gY6pgHVJNv%2FpQbVCF1xNOdB1N9pktYdN6xROaCRF%2BcuqSjQFMKzv1RpMtlFslTroNch7ty9YxoPVAWl2SscwHu8hHHooUKkX147W9JwG13HfKSvwZhWV3JSlEMOLZo01FsxAKaJor6FJmo%2BlCmLJfPXqjHBoz5OSzgiP%2BNDQDGQgo08fnqLvV4vzHs%2Bd7OZwKTidvZbJwBf7mOnINZLW06EgBoqb%2B8vDDpm&X-Amz-Signature=e7cd6809ba8b2065846bc47263418f60a3389184aaf2d85a2312d44a175d6ac5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```javascript
---
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: eureka-server3
  labels:
    app: eureka-server3
spec:
  replicas: 2
  serviceName: eureka-server3
  template:
    metadata:
      name: eureka-server3
      labels:
        app: eureka-server3
    spec:
      containers:
        - name: eureka-server3
          image: my-eureka
          imagePullPolicy: IfNotPresent
          env:
            - name: "--eureka.client.register-with-eureka"
              value: "true"
            - name: "--eureka-client.fetch-registry"
              value: "true"
            - name: "--eureka.client.service-url.defaultZone"
              value: "http://eureka-server3-0.eureka-server3:8761/eureka, http://eureka-server3-1.eureka-server3:8761/eureka"
      restartPolicy: Always
  selector:
    matchLabels:
      app: eureka-server3
```


OK。由于机器的内存比较有限，我们把 ha1 先删掉，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/bf6fc664-3954-42b8-bd12-516b6a3e8386/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BWHEADZ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBDZOSmL2hwlKO9QQ4bVZW4jnj2Gzd%2BXa00tGyS3OJqyAiBT8LbH%2Bpy04Ql3YUpANzB93VdTPa3fae6%2FwQaDD8kKyCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM6W9MC3hLvesPxdKuKtwDxgpMnIWyB173Box5yGSkErwACDmlFjAtYlxels1EoIbsxFqRt8rvDdFQHzT%2FkZeXScid45D%2B0%2FMAbFQiiMs98%2FSDmKS%2F8IMCJV4FLCQIiGr24jWfpQgD6kA4e2Vi9Y7wShv29yA7q1vRRi8rg2CftUokVD4yhaZRXvggfczn7NlCDJnLKeFPf6URlF1Z7ds7Wvt%2BAu5M%2FJxjH0ALAUeM78olOyYaf5qQy%2Fn%2FDgeoi55l4edEDXcGZKqsYHhoObPgQ4GgM0nYEkrh%2FvfONU2qiEUPe2BZ3CurBs3TBnDw69YSwCMUqV5tumaFdTeO2E1SMPMT4ACm3szvucx9qgjQN50MW0lu%2BrkmOjqssW7hZnpM8Ulymf36nR705BkL0WthXnXy%2Fl7dlyYlTcOlgX5bqvuzcYgVlGdGTn5kvIF%2Bxd%2Bp6hqWD6xHFyUHyBZTP%2Ft%2FcfdaMy18icmTzigFEsBXOJdNuC7Lph2r%2F0log1AItN9G0rAvI41QQfkSVul0eKfjt4umDd03CNHcFLWnwok29ApgwI0iyHWXz4Lsd1ddt036DniEd6lAm3CF3thd%2BxI%2FOP9shgOHY7RxtduJ6rmD1pNV016F2s88e8USeLKoZA0GO2vw%2Fyz4J7UHgSgw3bf%2F0gY6pgGlWfPZ%2BeEzSzA96mhV5QcJzvWuQ5raQRwaOT0cZ9dvYwADVU2Vs4DS%2Fkc%2B78lU0lpPpJH7xXEo27kCpat46pvGMhK97PivG4EhdbWrE51QhQZBCnl1Xjtq0R%2B%2FysyfFYaEzFkuS%2F6DtLUYJoRHpLAeHRMEbW2YFu1V9VMpbwLCnLXlEt4ewh4N31%2FyYTdkqaZ%2FWTOSxDrHJO4LICbWy%2BuaYVeXVwaL&X-Amz-Signature=b4cab259a4a2470b567955b4ba52ba5d4e21a2f2307365a97eba582a4878b5fa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

再来创建 ha2，创建完成，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/390c6cab-744f-4e75-b62a-63731a777080/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BWHEADZ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBDZOSmL2hwlKO9QQ4bVZW4jnj2Gzd%2BXa00tGyS3OJqyAiBT8LbH%2Bpy04Ql3YUpANzB93VdTPa3fae6%2FwQaDD8kKyCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM6W9MC3hLvesPxdKuKtwDxgpMnIWyB173Box5yGSkErwACDmlFjAtYlxels1EoIbsxFqRt8rvDdFQHzT%2FkZeXScid45D%2B0%2FMAbFQiiMs98%2FSDmKS%2F8IMCJV4FLCQIiGr24jWfpQgD6kA4e2Vi9Y7wShv29yA7q1vRRi8rg2CftUokVD4yhaZRXvggfczn7NlCDJnLKeFPf6URlF1Z7ds7Wvt%2BAu5M%2FJxjH0ALAUeM78olOyYaf5qQy%2Fn%2FDgeoi55l4edEDXcGZKqsYHhoObPgQ4GgM0nYEkrh%2FvfONU2qiEUPe2BZ3CurBs3TBnDw69YSwCMUqV5tumaFdTeO2E1SMPMT4ACm3szvucx9qgjQN50MW0lu%2BrkmOjqssW7hZnpM8Ulymf36nR705BkL0WthXnXy%2Fl7dlyYlTcOlgX5bqvuzcYgVlGdGTn5kvIF%2Bxd%2Bp6hqWD6xHFyUHyBZTP%2Ft%2FcfdaMy18icmTzigFEsBXOJdNuC7Lph2r%2F0log1AItN9G0rAvI41QQfkSVul0eKfjt4umDd03CNHcFLWnwok29ApgwI0iyHWXz4Lsd1ddt036DniEd6lAm3CF3thd%2BxI%2FOP9shgOHY7RxtduJ6rmD1pNV016F2s88e8USeLKoZA0GO2vw%2Fyz4J7UHgSgw3bf%2F0gY6pgGlWfPZ%2BeEzSzA96mhV5QcJzvWuQ5raQRwaOT0cZ9dvYwADVU2Vs4DS%2Fkc%2B78lU0lpPpJH7xXEo27kCpat46pvGMhK97PivG4EhdbWrE51QhQZBCnl1Xjtq0R%2B%2FysyfFYaEzFkuS%2F6DtLUYJoRHpLAeHRMEbW2YFu1V9VMpbwLCnLXlEt4ewh4N31%2FyYTdkqaZ%2FWTOSxDrHJO4LICbWy%2BuaYVeXVwaL&X-Amz-Signature=99ddfec3a69afa9c2debe0d0d9acb287db7bf9bfd27899145ba440441cf1d342&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

访问 localhost 30003。可以看到现在已经有一个实例。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/8fb979f0-43a7-4547-9439-762cd22a3c20/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BWHEADZ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBDZOSmL2hwlKO9QQ4bVZW4jnj2Gzd%2BXa00tGyS3OJqyAiBT8LbH%2Bpy04Ql3YUpANzB93VdTPa3fae6%2FwQaDD8kKyCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM6W9MC3hLvesPxdKuKtwDxgpMnIWyB173Box5yGSkErwACDmlFjAtYlxels1EoIbsxFqRt8rvDdFQHzT%2FkZeXScid45D%2B0%2FMAbFQiiMs98%2FSDmKS%2F8IMCJV4FLCQIiGr24jWfpQgD6kA4e2Vi9Y7wShv29yA7q1vRRi8rg2CftUokVD4yhaZRXvggfczn7NlCDJnLKeFPf6URlF1Z7ds7Wvt%2BAu5M%2FJxjH0ALAUeM78olOyYaf5qQy%2Fn%2FDgeoi55l4edEDXcGZKqsYHhoObPgQ4GgM0nYEkrh%2FvfONU2qiEUPe2BZ3CurBs3TBnDw69YSwCMUqV5tumaFdTeO2E1SMPMT4ACm3szvucx9qgjQN50MW0lu%2BrkmOjqssW7hZnpM8Ulymf36nR705BkL0WthXnXy%2Fl7dlyYlTcOlgX5bqvuzcYgVlGdGTn5kvIF%2Bxd%2Bp6hqWD6xHFyUHyBZTP%2Ft%2FcfdaMy18icmTzigFEsBXOJdNuC7Lph2r%2F0log1AItN9G0rAvI41QQfkSVul0eKfjt4umDd03CNHcFLWnwok29ApgwI0iyHWXz4Lsd1ddt036DniEd6lAm3CF3thd%2BxI%2FOP9shgOHY7RxtduJ6rmD1pNV016F2s88e8USeLKoZA0GO2vw%2Fyz4J7UHgSgw3bf%2F0gY6pgGlWfPZ%2BeEzSzA96mhV5QcJzvWuQ5raQRwaOT0cZ9dvYwADVU2Vs4DS%2Fkc%2B78lU0lpPpJH7xXEo27kCpat46pvGMhK97PivG4EhdbWrE51QhQZBCnl1Xjtq0R%2B%2FysyfFYaEzFkuS%2F6DtLUYJoRHpLAeHRMEbW2YFu1V9VMpbwLCnLXlEt4ewh4N31%2FyYTdkqaZ%2FWTOSxDrHJO4LICbWy%2BuaYVeXVwaL&X-Amz-Signature=c2b599bb176c2a7f679b5fbd079987aab552c3d3d03ac99d6d3ef70f9e0f2357&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

稍等一下。两个实例，比如卡 server 集群搭建完成。OK，最后我们来对比一下两种集群的搭建方式。


先来分析

第一种方式，这种方式的优点是伸缩比较方便，不管你是想搭建2 个实例还是 5 个实例，都不需要修改这里的配置。

第二种方式，如果原先是2 个实例，现在想要扩容到 3 个实例，就得修改这里的地址列表了。而缺点是性能不是最优，因为 eureka server 实例之间在同步的时候，每次请求都要经过 service 转移, 另外，在同步数据的时候，有一部分请求其实是无用功，因为请求打到自己身上去了对吧？OK，我们把它剪切贴到最上面来。


再来分析第二种方式。**这种方式的优点是性能比较好，而缺点是伸缩的时候需要修改配置。不过在实际项目中，对于 eureka server 来说并不会频繁伸缩。早上2 个实例，中午 5 个实例，晚上 3 个实例这样。eureka server 实例的个数，一般是相对固定的，我们做个标记，实际项目中并不会频繁进行伸缩，所以该缺点能够容忍。于是更多企业采用这套方案。**


OK，最后简单总结一下这节课

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b374b96b-40bc-4d65-864a-c95f8383489d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BWHEADZ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBDZOSmL2hwlKO9QQ4bVZW4jnj2Gzd%2BXa00tGyS3OJqyAiBT8LbH%2Bpy04Ql3YUpANzB93VdTPa3fae6%2FwQaDD8kKyCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM6W9MC3hLvesPxdKuKtwDxgpMnIWyB173Box5yGSkErwACDmlFjAtYlxels1EoIbsxFqRt8rvDdFQHzT%2FkZeXScid45D%2B0%2FMAbFQiiMs98%2FSDmKS%2F8IMCJV4FLCQIiGr24jWfpQgD6kA4e2Vi9Y7wShv29yA7q1vRRi8rg2CftUokVD4yhaZRXvggfczn7NlCDJnLKeFPf6URlF1Z7ds7Wvt%2BAu5M%2FJxjH0ALAUeM78olOyYaf5qQy%2Fn%2FDgeoi55l4edEDXcGZKqsYHhoObPgQ4GgM0nYEkrh%2FvfONU2qiEUPe2BZ3CurBs3TBnDw69YSwCMUqV5tumaFdTeO2E1SMPMT4ACm3szvucx9qgjQN50MW0lu%2BrkmOjqssW7hZnpM8Ulymf36nR705BkL0WthXnXy%2Fl7dlyYlTcOlgX5bqvuzcYgVlGdGTn5kvIF%2Bxd%2Bp6hqWD6xHFyUHyBZTP%2Ft%2FcfdaMy18icmTzigFEsBXOJdNuC7Lph2r%2F0log1AItN9G0rAvI41QQfkSVul0eKfjt4umDd03CNHcFLWnwok29ApgwI0iyHWXz4Lsd1ddt036DniEd6lAm3CF3thd%2BxI%2FOP9shgOHY7RxtduJ6rmD1pNV016F2s88e8USeLKoZA0GO2vw%2Fyz4J7UHgSgw3bf%2F0gY6pgGlWfPZ%2BeEzSzA96mhV5QcJzvWuQ5raQRwaOT0cZ9dvYwADVU2Vs4DS%2Fkc%2B78lU0lpPpJH7xXEo27kCpat46pvGMhK97PivG4EhdbWrE51QhQZBCnl1Xjtq0R%2B%2FysyfFYaEzFkuS%2F6DtLUYJoRHpLAeHRMEbW2YFu1V9VMpbwLCnLXlEt4ewh4N31%2FyYTdkqaZ%2FWTOSxDrHJO4LICbWy%2BuaYVeXVwaL&X-Amz-Signature=a20b3d341d22ac3e1f4bbfbffeb0ef2ddf62e33d774430666e7f31da761076a7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

。我们围绕 eureka server 的搭建，探讨了如何编写 K8S 的编排文件，并在实战的过程中复习了 eureka server 的高可用 K8S 的 deployment service 以及 StatefulSets，并提供了两种在 K8S 里面搭建高可用 eureka server 的方案。


如果同学们对这节课的内容感到陌生的话，请务必复习一下架构师第一阶段 K8S 的相关章节。因为随着云原生的不断普及，越来越多的节用 K8S 交付应用，可以说 K8S 已经成为了一个必备技能。同时，经过这一节的学习之后，同学们应该能够理解在本章最初为什么要拿 eureka server 这样的一个简单的 spring cloud 应用去做演示了，因为它可以用到 K8S 里面很多的知识，并且我们还可以活学活用。顺便还可以做一点扩展。


基于 deployment 是把两个 eureka server 实例

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/f4654493-598b-41b8-b256-43a5c997cbdb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BWHEADZ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBDZOSmL2hwlKO9QQ4bVZW4jnj2Gzd%2BXa00tGyS3OJqyAiBT8LbH%2Bpy04Ql3YUpANzB93VdTPa3fae6%2FwQaDD8kKyCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM6W9MC3hLvesPxdKuKtwDxgpMnIWyB173Box5yGSkErwACDmlFjAtYlxels1EoIbsxFqRt8rvDdFQHzT%2FkZeXScid45D%2B0%2FMAbFQiiMs98%2FSDmKS%2F8IMCJV4FLCQIiGr24jWfpQgD6kA4e2Vi9Y7wShv29yA7q1vRRi8rg2CftUokVD4yhaZRXvggfczn7NlCDJnLKeFPf6URlF1Z7ds7Wvt%2BAu5M%2FJxjH0ALAUeM78olOyYaf5qQy%2Fn%2FDgeoi55l4edEDXcGZKqsYHhoObPgQ4GgM0nYEkrh%2FvfONU2qiEUPe2BZ3CurBs3TBnDw69YSwCMUqV5tumaFdTeO2E1SMPMT4ACm3szvucx9qgjQN50MW0lu%2BrkmOjqssW7hZnpM8Ulymf36nR705BkL0WthXnXy%2Fl7dlyYlTcOlgX5bqvuzcYgVlGdGTn5kvIF%2Bxd%2Bp6hqWD6xHFyUHyBZTP%2Ft%2FcfdaMy18icmTzigFEsBXOJdNuC7Lph2r%2F0log1AItN9G0rAvI41QQfkSVul0eKfjt4umDd03CNHcFLWnwok29ApgwI0iyHWXz4Lsd1ddt036DniEd6lAm3CF3thd%2BxI%2FOP9shgOHY7RxtduJ6rmD1pNV016F2s88e8USeLKoZA0GO2vw%2Fyz4J7UHgSgw3bf%2F0gY6pgGlWfPZ%2BeEzSzA96mhV5QcJzvWuQ5raQRwaOT0cZ9dvYwADVU2Vs4DS%2Fkc%2B78lU0lpPpJH7xXEo27kCpat46pvGMhK97PivG4EhdbWrE51QhQZBCnl1Xjtq0R%2B%2FysyfFYaEzFkuS%2F6DtLUYJoRHpLAeHRMEbW2YFu1V9VMpbwLCnLXlEt4ewh4N31%2FyYTdkqaZ%2FWTOSxDrHJO4LICbWy%2BuaYVeXVwaL&X-Amz-Signature=9c1ea604feb21bb531eca2247ff7d3eeddc2604b90336fbf9df93cbe8988f12a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

当做 pod1 以及 pod2 的，其实你也可以把两个 eureka-service 里想象成是这里的微服 x 和这里的微服y。你可以这样玩为 eureka server 实例 1 创建一个 deployment ，加一个 service , eureka server 实例2 也创建一个deployment，加一个service。这样实例 1 想要连接实例 2 的时候，用实例2 的 service 名称, 实例2 想要连接实例 1 的时候，就用实例 1 的 service 名称。这样也可以实现 eureka-server 的高可用。同学们在实际项目里面还是要能够灵活的使用 K8S 的各种特性去交付你的应用。这节课就到这里，谢谢大家。


















[file](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/71341815-1639-4cba-b0c1-5c7c3598de25/eureka-ha1.yaml?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BWHEADZ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBDZOSmL2hwlKO9QQ4bVZW4jnj2Gzd%2BXa00tGyS3OJqyAiBT8LbH%2Bpy04Ql3YUpANzB93VdTPa3fae6%2FwQaDD8kKyCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM6W9MC3hLvesPxdKuKtwDxgpMnIWyB173Box5yGSkErwACDmlFjAtYlxels1EoIbsxFqRt8rvDdFQHzT%2FkZeXScid45D%2B0%2FMAbFQiiMs98%2FSDmKS%2F8IMCJV4FLCQIiGr24jWfpQgD6kA4e2Vi9Y7wShv29yA7q1vRRi8rg2CftUokVD4yhaZRXvggfczn7NlCDJnLKeFPf6URlF1Z7ds7Wvt%2BAu5M%2FJxjH0ALAUeM78olOyYaf5qQy%2Fn%2FDgeoi55l4edEDXcGZKqsYHhoObPgQ4GgM0nYEkrh%2FvfONU2qiEUPe2BZ3CurBs3TBnDw69YSwCMUqV5tumaFdTeO2E1SMPMT4ACm3szvucx9qgjQN50MW0lu%2BrkmOjqssW7hZnpM8Ulymf36nR705BkL0WthXnXy%2Fl7dlyYlTcOlgX5bqvuzcYgVlGdGTn5kvIF%2Bxd%2Bp6hqWD6xHFyUHyBZTP%2Ft%2FcfdaMy18icmTzigFEsBXOJdNuC7Lph2r%2F0log1AItN9G0rAvI41QQfkSVul0eKfjt4umDd03CNHcFLWnwok29ApgwI0iyHWXz4Lsd1ddt036DniEd6lAm3CF3thd%2BxI%2FOP9shgOHY7RxtduJ6rmD1pNV016F2s88e8USeLKoZA0GO2vw%2Fyz4J7UHgSgw3bf%2F0gY6pgGlWfPZ%2BeEzSzA96mhV5QcJzvWuQ5raQRwaOT0cZ9dvYwADVU2Vs4DS%2Fkc%2B78lU0lpPpJH7xXEo27kCpat46pvGMhK97PivG4EhdbWrE51QhQZBCnl1Xjtq0R%2B%2FysyfFYaEzFkuS%2F6DtLUYJoRHpLAeHRMEbW2YFu1V9VMpbwLCnLXlEt4ewh4N31%2FyYTdkqaZ%2FWTOSxDrHJO4LICbWy%2BuaYVeXVwaL&X-Amz-Signature=05d8ba816620a2f1e7a18acf5444d159206658887c0162230dd96e6badb27913&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[file](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/cdbc4bf4-b7ef-4d1a-aa48-bb01a5f003e7/eureka-ha2.yaml?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BWHEADZ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBDZOSmL2hwlKO9QQ4bVZW4jnj2Gzd%2BXa00tGyS3OJqyAiBT8LbH%2Bpy04Ql3YUpANzB93VdTPa3fae6%2FwQaDD8kKyCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM6W9MC3hLvesPxdKuKtwDxgpMnIWyB173Box5yGSkErwACDmlFjAtYlxels1EoIbsxFqRt8rvDdFQHzT%2FkZeXScid45D%2B0%2FMAbFQiiMs98%2FSDmKS%2F8IMCJV4FLCQIiGr24jWfpQgD6kA4e2Vi9Y7wShv29yA7q1vRRi8rg2CftUokVD4yhaZRXvggfczn7NlCDJnLKeFPf6URlF1Z7ds7Wvt%2BAu5M%2FJxjH0ALAUeM78olOyYaf5qQy%2Fn%2FDgeoi55l4edEDXcGZKqsYHhoObPgQ4GgM0nYEkrh%2FvfONU2qiEUPe2BZ3CurBs3TBnDw69YSwCMUqV5tumaFdTeO2E1SMPMT4ACm3szvucx9qgjQN50MW0lu%2BrkmOjqssW7hZnpM8Ulymf36nR705BkL0WthXnXy%2Fl7dlyYlTcOlgX5bqvuzcYgVlGdGTn5kvIF%2Bxd%2Bp6hqWD6xHFyUHyBZTP%2Ft%2FcfdaMy18icmTzigFEsBXOJdNuC7Lph2r%2F0log1AItN9G0rAvI41QQfkSVul0eKfjt4umDd03CNHcFLWnwok29ApgwI0iyHWXz4Lsd1ddt036DniEd6lAm3CF3thd%2BxI%2FOP9shgOHY7RxtduJ6rmD1pNV016F2s88e8USeLKoZA0GO2vw%2Fyz4J7UHgSgw3bf%2F0gY6pgGlWfPZ%2BeEzSzA96mhV5QcJzvWuQ5raQRwaOT0cZ9dvYwADVU2Vs4DS%2Fkc%2B78lU0lpPpJH7xXEo27kCpat46pvGMhK97PivG4EhdbWrE51QhQZBCnl1Xjtq0R%2B%2FysyfFYaEzFkuS%2F6DtLUYJoRHpLAeHRMEbW2YFu1V9VMpbwLCnLXlEt4ewh4N31%2FyYTdkqaZ%2FWTOSxDrHJO4LICbWy%2BuaYVeXVwaL&X-Amz-Signature=f0b57f03591a4d287b9b2b651cf07f939affa2713fffd125c617b3b57acfb9e5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[file](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/ecaacb86-2a6d-4587-9372-f7e368a4a427/eureka-single.yaml?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BWHEADZ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBDZOSmL2hwlKO9QQ4bVZW4jnj2Gzd%2BXa00tGyS3OJqyAiBT8LbH%2Bpy04Ql3YUpANzB93VdTPa3fae6%2FwQaDD8kKyCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM6W9MC3hLvesPxdKuKtwDxgpMnIWyB173Box5yGSkErwACDmlFjAtYlxels1EoIbsxFqRt8rvDdFQHzT%2FkZeXScid45D%2B0%2FMAbFQiiMs98%2FSDmKS%2F8IMCJV4FLCQIiGr24jWfpQgD6kA4e2Vi9Y7wShv29yA7q1vRRi8rg2CftUokVD4yhaZRXvggfczn7NlCDJnLKeFPf6URlF1Z7ds7Wvt%2BAu5M%2FJxjH0ALAUeM78olOyYaf5qQy%2Fn%2FDgeoi55l4edEDXcGZKqsYHhoObPgQ4GgM0nYEkrh%2FvfONU2qiEUPe2BZ3CurBs3TBnDw69YSwCMUqV5tumaFdTeO2E1SMPMT4ACm3szvucx9qgjQN50MW0lu%2BrkmOjqssW7hZnpM8Ulymf36nR705BkL0WthXnXy%2Fl7dlyYlTcOlgX5bqvuzcYgVlGdGTn5kvIF%2Bxd%2Bp6hqWD6xHFyUHyBZTP%2Ft%2FcfdaMy18icmTzigFEsBXOJdNuC7Lph2r%2F0log1AItN9G0rAvI41QQfkSVul0eKfjt4umDd03CNHcFLWnwok29ApgwI0iyHWXz4Lsd1ddt036DniEd6lAm3CF3thd%2BxI%2FOP9shgOHY7RxtduJ6rmD1pNV016F2s88e8USeLKoZA0GO2vw%2Fyz4J7UHgSgw3bf%2F0gY6pgGlWfPZ%2BeEzSzA96mhV5QcJzvWuQ5raQRwaOT0cZ9dvYwADVU2Vs4DS%2Fkc%2B78lU0lpPpJH7xXEo27kCpat46pvGMhK97PivG4EhdbWrE51QhQZBCnl1Xjtq0R%2B%2FysyfFYaEzFkuS%2F6DtLUYJoRHpLAeHRMEbW2YFu1V9VMpbwLCnLXlEt4ewh4N31%2FyYTdkqaZ%2FWTOSxDrHJO4LICbWy%2BuaYVeXVwaL&X-Amz-Signature=a8bd94a2f8f22b238d1d49ba1a98adf48587578cf1ff250556c9882f3d113c00&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[file](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b4ed40f4-dd43-4396-8293-61f0915469a3/application.yaml?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665BWHEADZ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231541Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBDZOSmL2hwlKO9QQ4bVZW4jnj2Gzd%2BXa00tGyS3OJqyAiBT8LbH%2Bpy04Ql3YUpANzB93VdTPa3fae6%2FwQaDD8kKyCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM6W9MC3hLvesPxdKuKtwDxgpMnIWyB173Box5yGSkErwACDmlFjAtYlxels1EoIbsxFqRt8rvDdFQHzT%2FkZeXScid45D%2B0%2FMAbFQiiMs98%2FSDmKS%2F8IMCJV4FLCQIiGr24jWfpQgD6kA4e2Vi9Y7wShv29yA7q1vRRi8rg2CftUokVD4yhaZRXvggfczn7NlCDJnLKeFPf6URlF1Z7ds7Wvt%2BAu5M%2FJxjH0ALAUeM78olOyYaf5qQy%2Fn%2FDgeoi55l4edEDXcGZKqsYHhoObPgQ4GgM0nYEkrh%2FvfONU2qiEUPe2BZ3CurBs3TBnDw69YSwCMUqV5tumaFdTeO2E1SMPMT4ACm3szvucx9qgjQN50MW0lu%2BrkmOjqssW7hZnpM8Ulymf36nR705BkL0WthXnXy%2Fl7dlyYlTcOlgX5bqvuzcYgVlGdGTn5kvIF%2Bxd%2Bp6hqWD6xHFyUHyBZTP%2Ft%2FcfdaMy18icmTzigFEsBXOJdNuC7Lph2r%2F0log1AItN9G0rAvI41QQfkSVul0eKfjt4umDd03CNHcFLWnwok29ApgwI0iyHWXz4Lsd1ddt036DniEd6lAm3CF3thd%2BxI%2FOP9shgOHY7RxtduJ6rmD1pNV016F2s88e8USeLKoZA0GO2vw%2Fyz4J7UHgSgw3bf%2F0gY6pgGlWfPZ%2BeEzSzA96mhV5QcJzvWuQ5raQRwaOT0cZ9dvYwADVU2Vs4DS%2Fkc%2B78lU0lpPpJH7xXEo27kCpat46pvGMhK97PivG4EhdbWrE51QhQZBCnl1Xjtq0R%2B%2FysyfFYaEzFkuS%2F6DtLUYJoRHpLAeHRMEbW2YFu1V9VMpbwLCnLXlEt4ewh4N31%2FyYTdkqaZ%2FWTOSxDrHJO4LICbWy%2BuaYVeXVwaL&X-Amz-Signature=4fb739a115bb705ae2b4efd9abedd8e100cb09d04542492c946a7cf2fe6bda74&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)




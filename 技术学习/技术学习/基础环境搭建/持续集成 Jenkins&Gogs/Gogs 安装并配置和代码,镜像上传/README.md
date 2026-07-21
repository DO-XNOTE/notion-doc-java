---
title: Gogs 安装并配置和代码,镜像上传
---

# Gogs 安装并配置和代码,镜像上传

# 代码传到服务器上-依然使用 docker 安装 Gogs

使用二进制安装 gogs 

[https://gogs.io/docs/installation/install_from_binary.html](https://gogs.io/docs/installation/install_from_binary.html)

```markdown
## docker run -d  --restart=always -p 10022:22 -p 3000:3000 --name=gogs -v /usr/local/cicd/gogs/:/data gogs/gogs
```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/447cbbf7-5db7-4647-902e-51936f8432d3/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663RNBET7%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDovQj1U%2B6PQory5XTRakzc%2FcPZm0dOv9A%2BTkQmQ2RbhwIhAJNIChh4K3tWOxq2cpgJSVtWXRDKnZmnK0UYhwYZWv0uKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxGqi0RXExglpQp5r8q3ANCui422ifppptlK%2Fe0%2BxWzE6ef7esjKMqk9VrwVJ%2BrDo0vXGcRX8Kf9qIi%2F7tIEnLbMM3vhzLMumExbg%2BT%2FruxUk5MpBemTSkTx5RtPA0ZvPQFmGkmktPtR4r6%2FJc5LviU57l3ZhV3mo7aLh9R2nzJOBSp0KsmkUNI0CCfXeNI5ayP%2BUHWclUo37FIU33FvfGqStY6lRMn75j3FlJlsZoSdeI4DP6sb9WRkbjdQQz1NjrblzaqEZqxYUG3bKM3A0bo63GOpXIgkCSimoAbX58cmqjRi%2FOt%2FWky7hos9zCwk%2BCr7%2Bn3iTsocdSb%2BH0gUJ0u3zqbJImFoT4ex8Ox2XI%2FLwf7aWSm%2BhgUcH69bMa1creml6%2BaKenfFvnZuuBXkduLoC%2FULML1%2F0%2FPkzHGjpaMKHXnMdlYj0SNtzKKta4kUpkC8kU%2BNq52dn%2Fucv%2FsDBESwaQ%2FnmOMi0uGJX18tmVrElB%2BnVWNIBtmY0Cut%2BvPjvajo8NykhLyxke7TrfmTRkEAcV82g8dco74hWl3pLwPS5mse74Mr%2BN1xgDcnpj0JaY5FnBnxp%2FTo4%2B8bdWyle85GDeeCa4%2BLiXRMCUOr3TtmFlf7QhrK0nxboiZKc4oknbwd9UGdslGocgtrjDXuv%2FSBjqkAVTyM%2BaCT0JksVzLtJHtslApq27oylCCQtl3SaueKldMj7aH4lr1PL8vj4WquSdkL9AwY9KaNweqhlR5ldpg5IAWk%2BETKwtErNeZl7KZ3iBgTp59mEw7KkWqlKuEGLvjT1QWhBBQbnFrGZHyma5G%2BoThdam7D9WqXytAh375bprRmGPE028MZso8G5WkMo7Np5dV6JZa%2BJrXPZau%2FhazhK0ZBFGx&X-Amz-Signature=daa8f4dac5961155d2486e2bcec9d923129298a4e3ff1e8fbd47d14e904f3787&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/1fa7fdee-ee25-4d7f-993e-01c93c5d8583/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663RNBET7%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDovQj1U%2B6PQory5XTRakzc%2FcPZm0dOv9A%2BTkQmQ2RbhwIhAJNIChh4K3tWOxq2cpgJSVtWXRDKnZmnK0UYhwYZWv0uKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxGqi0RXExglpQp5r8q3ANCui422ifppptlK%2Fe0%2BxWzE6ef7esjKMqk9VrwVJ%2BrDo0vXGcRX8Kf9qIi%2F7tIEnLbMM3vhzLMumExbg%2BT%2FruxUk5MpBemTSkTx5RtPA0ZvPQFmGkmktPtR4r6%2FJc5LviU57l3ZhV3mo7aLh9R2nzJOBSp0KsmkUNI0CCfXeNI5ayP%2BUHWclUo37FIU33FvfGqStY6lRMn75j3FlJlsZoSdeI4DP6sb9WRkbjdQQz1NjrblzaqEZqxYUG3bKM3A0bo63GOpXIgkCSimoAbX58cmqjRi%2FOt%2FWky7hos9zCwk%2BCr7%2Bn3iTsocdSb%2BH0gUJ0u3zqbJImFoT4ex8Ox2XI%2FLwf7aWSm%2BhgUcH69bMa1creml6%2BaKenfFvnZuuBXkduLoC%2FULML1%2F0%2FPkzHGjpaMKHXnMdlYj0SNtzKKta4kUpkC8kU%2BNq52dn%2Fucv%2FsDBESwaQ%2FnmOMi0uGJX18tmVrElB%2BnVWNIBtmY0Cut%2BvPjvajo8NykhLyxke7TrfmTRkEAcV82g8dco74hWl3pLwPS5mse74Mr%2BN1xgDcnpj0JaY5FnBnxp%2FTo4%2B8bdWyle85GDeeCa4%2BLiXRMCUOr3TtmFlf7QhrK0nxboiZKc4oknbwd9UGdslGocgtrjDXuv%2FSBjqkAVTyM%2BaCT0JksVzLtJHtslApq27oylCCQtl3SaueKldMj7aH4lr1PL8vj4WquSdkL9AwY9KaNweqhlR5ldpg5IAWk%2BETKwtErNeZl7KZ3iBgTp59mEw7KkWqlKuEGLvjT1QWhBBQbnFrGZHyma5G%2BoThdam7D9WqXytAh375bprRmGPE028MZso8G5WkMo7Np5dV6JZa%2BJrXPZau%2FhazhK0ZBFGx&X-Amz-Signature=4f206fd4db48c44fbc28957528cf8f31a4da69ec0ecc15b4823dd50df9252c23&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```markdown
##用户名：guojun
##密码：guojun12
```

```javascript
这个需要设置成这个才可以安装（默认的）， 然后安装完成
```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/0e0cb045-59fc-4da4-a38b-4534230c4dd4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663RNBET7%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDovQj1U%2B6PQory5XTRakzc%2FcPZm0dOv9A%2BTkQmQ2RbhwIhAJNIChh4K3tWOxq2cpgJSVtWXRDKnZmnK0UYhwYZWv0uKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxGqi0RXExglpQp5r8q3ANCui422ifppptlK%2Fe0%2BxWzE6ef7esjKMqk9VrwVJ%2BrDo0vXGcRX8Kf9qIi%2F7tIEnLbMM3vhzLMumExbg%2BT%2FruxUk5MpBemTSkTx5RtPA0ZvPQFmGkmktPtR4r6%2FJc5LviU57l3ZhV3mo7aLh9R2nzJOBSp0KsmkUNI0CCfXeNI5ayP%2BUHWclUo37FIU33FvfGqStY6lRMn75j3FlJlsZoSdeI4DP6sb9WRkbjdQQz1NjrblzaqEZqxYUG3bKM3A0bo63GOpXIgkCSimoAbX58cmqjRi%2FOt%2FWky7hos9zCwk%2BCr7%2Bn3iTsocdSb%2BH0gUJ0u3zqbJImFoT4ex8Ox2XI%2FLwf7aWSm%2BhgUcH69bMa1creml6%2BaKenfFvnZuuBXkduLoC%2FULML1%2F0%2FPkzHGjpaMKHXnMdlYj0SNtzKKta4kUpkC8kU%2BNq52dn%2Fucv%2FsDBESwaQ%2FnmOMi0uGJX18tmVrElB%2BnVWNIBtmY0Cut%2BvPjvajo8NykhLyxke7TrfmTRkEAcV82g8dco74hWl3pLwPS5mse74Mr%2BN1xgDcnpj0JaY5FnBnxp%2FTo4%2B8bdWyle85GDeeCa4%2BLiXRMCUOr3TtmFlf7QhrK0nxboiZKc4oknbwd9UGdslGocgtrjDXuv%2FSBjqkAVTyM%2BaCT0JksVzLtJHtslApq27oylCCQtl3SaueKldMj7aH4lr1PL8vj4WquSdkL9AwY9KaNweqhlR5ldpg5IAWk%2BETKwtErNeZl7KZ3iBgTp59mEw7KkWqlKuEGLvjT1QWhBBQbnFrGZHyma5G%2BoThdam7D9WqXytAh375bprRmGPE028MZso8G5WkMo7Np5dV6JZa%2BJrXPZau%2FhazhK0ZBFGx&X-Amz-Signature=758e91c61bdc9c0dc734c175b86b5a5bb77654f190dba3c74f333584225ba544&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/9deb7629-ec8a-4be4-8d08-9866e4512e3c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663RNBET7%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDovQj1U%2B6PQory5XTRakzc%2FcPZm0dOv9A%2BTkQmQ2RbhwIhAJNIChh4K3tWOxq2cpgJSVtWXRDKnZmnK0UYhwYZWv0uKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxGqi0RXExglpQp5r8q3ANCui422ifppptlK%2Fe0%2BxWzE6ef7esjKMqk9VrwVJ%2BrDo0vXGcRX8Kf9qIi%2F7tIEnLbMM3vhzLMumExbg%2BT%2FruxUk5MpBemTSkTx5RtPA0ZvPQFmGkmktPtR4r6%2FJc5LviU57l3ZhV3mo7aLh9R2nzJOBSp0KsmkUNI0CCfXeNI5ayP%2BUHWclUo37FIU33FvfGqStY6lRMn75j3FlJlsZoSdeI4DP6sb9WRkbjdQQz1NjrblzaqEZqxYUG3bKM3A0bo63GOpXIgkCSimoAbX58cmqjRi%2FOt%2FWky7hos9zCwk%2BCr7%2Bn3iTsocdSb%2BH0gUJ0u3zqbJImFoT4ex8Ox2XI%2FLwf7aWSm%2BhgUcH69bMa1creml6%2BaKenfFvnZuuBXkduLoC%2FULML1%2F0%2FPkzHGjpaMKHXnMdlYj0SNtzKKta4kUpkC8kU%2BNq52dn%2Fucv%2FsDBESwaQ%2FnmOMi0uGJX18tmVrElB%2BnVWNIBtmY0Cut%2BvPjvajo8NykhLyxke7TrfmTRkEAcV82g8dco74hWl3pLwPS5mse74Mr%2BN1xgDcnpj0JaY5FnBnxp%2FTo4%2B8bdWyle85GDeeCa4%2BLiXRMCUOr3TtmFlf7QhrK0nxboiZKc4oknbwd9UGdslGocgtrjDXuv%2FSBjqkAVTyM%2BaCT0JksVzLtJHtslApq27oylCCQtl3SaueKldMj7aH4lr1PL8vj4WquSdkL9AwY9KaNweqhlR5ldpg5IAWk%2BETKwtErNeZl7KZ3iBgTp59mEw7KkWqlKuEGLvjT1QWhBBQbnFrGZHyma5G%2BoThdam7D9WqXytAh375bprRmGPE028MZso8G5WkMo7Np5dV6JZa%2BJrXPZau%2FhazhK0ZBFGx&X-Amz-Signature=2e11d36fb5d6d2ae801b3cadc499230e0e0b92718061c83241d3055e26b95652&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

# 创建仓库

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/a4e46035-ee04-48dc-be41-6bcb280e6d70/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663RNBET7%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDovQj1U%2B6PQory5XTRakzc%2FcPZm0dOv9A%2BTkQmQ2RbhwIhAJNIChh4K3tWOxq2cpgJSVtWXRDKnZmnK0UYhwYZWv0uKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxGqi0RXExglpQp5r8q3ANCui422ifppptlK%2Fe0%2BxWzE6ef7esjKMqk9VrwVJ%2BrDo0vXGcRX8Kf9qIi%2F7tIEnLbMM3vhzLMumExbg%2BT%2FruxUk5MpBemTSkTx5RtPA0ZvPQFmGkmktPtR4r6%2FJc5LviU57l3ZhV3mo7aLh9R2nzJOBSp0KsmkUNI0CCfXeNI5ayP%2BUHWclUo37FIU33FvfGqStY6lRMn75j3FlJlsZoSdeI4DP6sb9WRkbjdQQz1NjrblzaqEZqxYUG3bKM3A0bo63GOpXIgkCSimoAbX58cmqjRi%2FOt%2FWky7hos9zCwk%2BCr7%2Bn3iTsocdSb%2BH0gUJ0u3zqbJImFoT4ex8Ox2XI%2FLwf7aWSm%2BhgUcH69bMa1creml6%2BaKenfFvnZuuBXkduLoC%2FULML1%2F0%2FPkzHGjpaMKHXnMdlYj0SNtzKKta4kUpkC8kU%2BNq52dn%2Fucv%2FsDBESwaQ%2FnmOMi0uGJX18tmVrElB%2BnVWNIBtmY0Cut%2BvPjvajo8NykhLyxke7TrfmTRkEAcV82g8dco74hWl3pLwPS5mse74Mr%2BN1xgDcnpj0JaY5FnBnxp%2FTo4%2B8bdWyle85GDeeCa4%2BLiXRMCUOr3TtmFlf7QhrK0nxboiZKc4oknbwd9UGdslGocgtrjDXuv%2FSBjqkAVTyM%2BaCT0JksVzLtJHtslApq27oylCCQtl3SaueKldMj7aH4lr1PL8vj4WquSdkL9AwY9KaNweqhlR5ldpg5IAWk%2BETKwtErNeZl7KZ3iBgTp59mEw7KkWqlKuEGLvjT1QWhBBQbnFrGZHyma5G%2BoThdam7D9WqXytAh375bprRmGPE028MZso8G5WkMo7Np5dV6JZa%2BJrXPZau%2FhazhK0ZBFGx&X-Amz-Signature=8f55648054b015753cf81cbfa54a25b4ef76e909253f5bf0b6fc7bbaeffa68b3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/cd1755e1-1c34-4088-b4af-db2ce3c98b7d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663RNBET7%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDovQj1U%2B6PQory5XTRakzc%2FcPZm0dOv9A%2BTkQmQ2RbhwIhAJNIChh4K3tWOxq2cpgJSVtWXRDKnZmnK0UYhwYZWv0uKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxGqi0RXExglpQp5r8q3ANCui422ifppptlK%2Fe0%2BxWzE6ef7esjKMqk9VrwVJ%2BrDo0vXGcRX8Kf9qIi%2F7tIEnLbMM3vhzLMumExbg%2BT%2FruxUk5MpBemTSkTx5RtPA0ZvPQFmGkmktPtR4r6%2FJc5LviU57l3ZhV3mo7aLh9R2nzJOBSp0KsmkUNI0CCfXeNI5ayP%2BUHWclUo37FIU33FvfGqStY6lRMn75j3FlJlsZoSdeI4DP6sb9WRkbjdQQz1NjrblzaqEZqxYUG3bKM3A0bo63GOpXIgkCSimoAbX58cmqjRi%2FOt%2FWky7hos9zCwk%2BCr7%2Bn3iTsocdSb%2BH0gUJ0u3zqbJImFoT4ex8Ox2XI%2FLwf7aWSm%2BhgUcH69bMa1creml6%2BaKenfFvnZuuBXkduLoC%2FULML1%2F0%2FPkzHGjpaMKHXnMdlYj0SNtzKKta4kUpkC8kU%2BNq52dn%2Fucv%2FsDBESwaQ%2FnmOMi0uGJX18tmVrElB%2BnVWNIBtmY0Cut%2BvPjvajo8NykhLyxke7TrfmTRkEAcV82g8dco74hWl3pLwPS5mse74Mr%2BN1xgDcnpj0JaY5FnBnxp%2FTo4%2B8bdWyle85GDeeCa4%2BLiXRMCUOr3TtmFlf7QhrK0nxboiZKc4oknbwd9UGdslGocgtrjDXuv%2FSBjqkAVTyM%2BaCT0JksVzLtJHtslApq27oylCCQtl3SaueKldMj7aH4lr1PL8vj4WquSdkL9AwY9KaNweqhlR5ldpg5IAWk%2BETKwtErNeZl7KZ3iBgTp59mEw7KkWqlKuEGLvjT1QWhBBQbnFrGZHyma5G%2BoThdam7D9WqXytAh375bprRmGPE028MZso8G5WkMo7Np5dV6JZa%2BJrXPZau%2FhazhK0ZBFGx&X-Amz-Signature=97e97a7ae539e23c6617074be898360a50493bed87bc5b7759605ba6672ce939&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

# 代码上传仓库

打开IDEA

```markdown
#commit Direact 提交 文件件
#然后commit and push 
#输入用户名和密码  guojun / guojun12

## git： http://172.16.136.100:3000/guojun/mkw_hema.git 地址



## 使用代码提交
##从命令行创建一个新的仓库
touch README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin http://192.168.13.206:3000/guojun/myproject_cloud.git
git push -u origin master
## 从命令行推送已经创建的仓库
git remote add origin http://192.168.13.206:3000/guojun/myproject_cloud.git
git push -u origin master
```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/ee8b2291-20fa-49ad-8e00-40497789ccfc/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663RNBET7%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDovQj1U%2B6PQory5XTRakzc%2FcPZm0dOv9A%2BTkQmQ2RbhwIhAJNIChh4K3tWOxq2cpgJSVtWXRDKnZmnK0UYhwYZWv0uKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxGqi0RXExglpQp5r8q3ANCui422ifppptlK%2Fe0%2BxWzE6ef7esjKMqk9VrwVJ%2BrDo0vXGcRX8Kf9qIi%2F7tIEnLbMM3vhzLMumExbg%2BT%2FruxUk5MpBemTSkTx5RtPA0ZvPQFmGkmktPtR4r6%2FJc5LviU57l3ZhV3mo7aLh9R2nzJOBSp0KsmkUNI0CCfXeNI5ayP%2BUHWclUo37FIU33FvfGqStY6lRMn75j3FlJlsZoSdeI4DP6sb9WRkbjdQQz1NjrblzaqEZqxYUG3bKM3A0bo63GOpXIgkCSimoAbX58cmqjRi%2FOt%2FWky7hos9zCwk%2BCr7%2Bn3iTsocdSb%2BH0gUJ0u3zqbJImFoT4ex8Ox2XI%2FLwf7aWSm%2BhgUcH69bMa1creml6%2BaKenfFvnZuuBXkduLoC%2FULML1%2F0%2FPkzHGjpaMKHXnMdlYj0SNtzKKta4kUpkC8kU%2BNq52dn%2Fucv%2FsDBESwaQ%2FnmOMi0uGJX18tmVrElB%2BnVWNIBtmY0Cut%2BvPjvajo8NykhLyxke7TrfmTRkEAcV82g8dco74hWl3pLwPS5mse74Mr%2BN1xgDcnpj0JaY5FnBnxp%2FTo4%2B8bdWyle85GDeeCa4%2BLiXRMCUOr3TtmFlf7QhrK0nxboiZKc4oknbwd9UGdslGocgtrjDXuv%2FSBjqkAVTyM%2BaCT0JksVzLtJHtslApq27oylCCQtl3SaueKldMj7aH4lr1PL8vj4WquSdkL9AwY9KaNweqhlR5ldpg5IAWk%2BETKwtErNeZl7KZ3iBgTp59mEw7KkWqlKuEGLvjT1QWhBBQbnFrGZHyma5G%2BoThdam7D9WqXytAh375bprRmGPE028MZso8G5WkMo7Np5dV6JZa%2BJrXPZau%2FhazhK0ZBFGx&X-Amz-Signature=7fa231a6c9b44de97fb5d770b65b924e6522050502122205cc3a7d9efb8f5e96&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b1d64910-6a85-49d6-837d-679b94979028/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663RNBET7%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDovQj1U%2B6PQory5XTRakzc%2FcPZm0dOv9A%2BTkQmQ2RbhwIhAJNIChh4K3tWOxq2cpgJSVtWXRDKnZmnK0UYhwYZWv0uKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxGqi0RXExglpQp5r8q3ANCui422ifppptlK%2Fe0%2BxWzE6ef7esjKMqk9VrwVJ%2BrDo0vXGcRX8Kf9qIi%2F7tIEnLbMM3vhzLMumExbg%2BT%2FruxUk5MpBemTSkTx5RtPA0ZvPQFmGkmktPtR4r6%2FJc5LviU57l3ZhV3mo7aLh9R2nzJOBSp0KsmkUNI0CCfXeNI5ayP%2BUHWclUo37FIU33FvfGqStY6lRMn75j3FlJlsZoSdeI4DP6sb9WRkbjdQQz1NjrblzaqEZqxYUG3bKM3A0bo63GOpXIgkCSimoAbX58cmqjRi%2FOt%2FWky7hos9zCwk%2BCr7%2Bn3iTsocdSb%2BH0gUJ0u3zqbJImFoT4ex8Ox2XI%2FLwf7aWSm%2BhgUcH69bMa1creml6%2BaKenfFvnZuuBXkduLoC%2FULML1%2F0%2FPkzHGjpaMKHXnMdlYj0SNtzKKta4kUpkC8kU%2BNq52dn%2Fucv%2FsDBESwaQ%2FnmOMi0uGJX18tmVrElB%2BnVWNIBtmY0Cut%2BvPjvajo8NykhLyxke7TrfmTRkEAcV82g8dco74hWl3pLwPS5mse74Mr%2BN1xgDcnpj0JaY5FnBnxp%2FTo4%2B8bdWyle85GDeeCa4%2BLiXRMCUOr3TtmFlf7QhrK0nxboiZKc4oknbwd9UGdslGocgtrjDXuv%2FSBjqkAVTyM%2BaCT0JksVzLtJHtslApq27oylCCQtl3SaueKldMj7aH4lr1PL8vj4WquSdkL9AwY9KaNweqhlR5ldpg5IAWk%2BETKwtErNeZl7KZ3iBgTp59mEw7KkWqlKuEGLvjT1QWhBBQbnFrGZHyma5G%2BoThdam7D9WqXytAh375bprRmGPE028MZso8G5WkMo7Np5dV6JZa%2BJrXPZau%2FhazhK0ZBFGx&X-Amz-Signature=3b12bc92fece09fe0007765f473e9ef35efbbe2557cf44205185f462bfe9047c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/c64c8f5d-dc53-4b16-af63-49771ff18bf9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663RNBET7%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDovQj1U%2B6PQory5XTRakzc%2FcPZm0dOv9A%2BTkQmQ2RbhwIhAJNIChh4K3tWOxq2cpgJSVtWXRDKnZmnK0UYhwYZWv0uKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxGqi0RXExglpQp5r8q3ANCui422ifppptlK%2Fe0%2BxWzE6ef7esjKMqk9VrwVJ%2BrDo0vXGcRX8Kf9qIi%2F7tIEnLbMM3vhzLMumExbg%2BT%2FruxUk5MpBemTSkTx5RtPA0ZvPQFmGkmktPtR4r6%2FJc5LviU57l3ZhV3mo7aLh9R2nzJOBSp0KsmkUNI0CCfXeNI5ayP%2BUHWclUo37FIU33FvfGqStY6lRMn75j3FlJlsZoSdeI4DP6sb9WRkbjdQQz1NjrblzaqEZqxYUG3bKM3A0bo63GOpXIgkCSimoAbX58cmqjRi%2FOt%2FWky7hos9zCwk%2BCr7%2Bn3iTsocdSb%2BH0gUJ0u3zqbJImFoT4ex8Ox2XI%2FLwf7aWSm%2BhgUcH69bMa1creml6%2BaKenfFvnZuuBXkduLoC%2FULML1%2F0%2FPkzHGjpaMKHXnMdlYj0SNtzKKta4kUpkC8kU%2BNq52dn%2Fucv%2FsDBESwaQ%2FnmOMi0uGJX18tmVrElB%2BnVWNIBtmY0Cut%2BvPjvajo8NykhLyxke7TrfmTRkEAcV82g8dco74hWl3pLwPS5mse74Mr%2BN1xgDcnpj0JaY5FnBnxp%2FTo4%2B8bdWyle85GDeeCa4%2BLiXRMCUOr3TtmFlf7QhrK0nxboiZKc4oknbwd9UGdslGocgtrjDXuv%2FSBjqkAVTyM%2BaCT0JksVzLtJHtslApq27oylCCQtl3SaueKldMj7aH4lr1PL8vj4WquSdkL9AwY9KaNweqhlR5ldpg5IAWk%2BETKwtErNeZl7KZ3iBgTp59mEw7KkWqlKuEGLvjT1QWhBBQbnFrGZHyma5G%2BoThdam7D9WqXytAh375bprRmGPE028MZso8G5WkMo7Np5dV6JZa%2BJrXPZau%2FhazhK0ZBFGx&X-Amz-Signature=65d2ab0561fbbb97a5e39fda55d7814c7825100c2a1102bb51694370f03899fc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

# Jenkins任务的创建和执行

```markdown
# 新建任务->任务名称 ->构建一个maven项目 -> git -> build - 项目下的pom（不是默认的pom啊注意！！！）

#review-base-java/mac-foodie/foodie-dev/pom.xml

#build中的命令
#clean package docker.build -DpushImage

```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/78de241d-73fc-4744-a406-6f945001bbf6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663RNBET7%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDovQj1U%2B6PQory5XTRakzc%2FcPZm0dOv9A%2BTkQmQ2RbhwIhAJNIChh4K3tWOxq2cpgJSVtWXRDKnZmnK0UYhwYZWv0uKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxGqi0RXExglpQp5r8q3ANCui422ifppptlK%2Fe0%2BxWzE6ef7esjKMqk9VrwVJ%2BrDo0vXGcRX8Kf9qIi%2F7tIEnLbMM3vhzLMumExbg%2BT%2FruxUk5MpBemTSkTx5RtPA0ZvPQFmGkmktPtR4r6%2FJc5LviU57l3ZhV3mo7aLh9R2nzJOBSp0KsmkUNI0CCfXeNI5ayP%2BUHWclUo37FIU33FvfGqStY6lRMn75j3FlJlsZoSdeI4DP6sb9WRkbjdQQz1NjrblzaqEZqxYUG3bKM3A0bo63GOpXIgkCSimoAbX58cmqjRi%2FOt%2FWky7hos9zCwk%2BCr7%2Bn3iTsocdSb%2BH0gUJ0u3zqbJImFoT4ex8Ox2XI%2FLwf7aWSm%2BhgUcH69bMa1creml6%2BaKenfFvnZuuBXkduLoC%2FULML1%2F0%2FPkzHGjpaMKHXnMdlYj0SNtzKKta4kUpkC8kU%2BNq52dn%2Fucv%2FsDBESwaQ%2FnmOMi0uGJX18tmVrElB%2BnVWNIBtmY0Cut%2BvPjvajo8NykhLyxke7TrfmTRkEAcV82g8dco74hWl3pLwPS5mse74Mr%2BN1xgDcnpj0JaY5FnBnxp%2FTo4%2B8bdWyle85GDeeCa4%2BLiXRMCUOr3TtmFlf7QhrK0nxboiZKc4oknbwd9UGdslGocgtrjDXuv%2FSBjqkAVTyM%2BaCT0JksVzLtJHtslApq27oylCCQtl3SaueKldMj7aH4lr1PL8vj4WquSdkL9AwY9KaNweqhlR5ldpg5IAWk%2BETKwtErNeZl7KZ3iBgTp59mEw7KkWqlKuEGLvjT1QWhBBQbnFrGZHyma5G%2BoThdam7D9WqXytAh375bprRmGPE028MZso8G5WkMo7Np5dV6JZa%2BJrXPZau%2FhazhK0ZBFGx&X-Amz-Signature=a30e21f5ba0dd948e868063359e06423eb5bda23de79bedb9a205694ec232cd3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/8727c28a-701d-4db0-b11a-52bbe065ca7f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663RNBET7%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDovQj1U%2B6PQory5XTRakzc%2FcPZm0dOv9A%2BTkQmQ2RbhwIhAJNIChh4K3tWOxq2cpgJSVtWXRDKnZmnK0UYhwYZWv0uKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxGqi0RXExglpQp5r8q3ANCui422ifppptlK%2Fe0%2BxWzE6ef7esjKMqk9VrwVJ%2BrDo0vXGcRX8Kf9qIi%2F7tIEnLbMM3vhzLMumExbg%2BT%2FruxUk5MpBemTSkTx5RtPA0ZvPQFmGkmktPtR4r6%2FJc5LviU57l3ZhV3mo7aLh9R2nzJOBSp0KsmkUNI0CCfXeNI5ayP%2BUHWclUo37FIU33FvfGqStY6lRMn75j3FlJlsZoSdeI4DP6sb9WRkbjdQQz1NjrblzaqEZqxYUG3bKM3A0bo63GOpXIgkCSimoAbX58cmqjRi%2FOt%2FWky7hos9zCwk%2BCr7%2Bn3iTsocdSb%2BH0gUJ0u3zqbJImFoT4ex8Ox2XI%2FLwf7aWSm%2BhgUcH69bMa1creml6%2BaKenfFvnZuuBXkduLoC%2FULML1%2F0%2FPkzHGjpaMKHXnMdlYj0SNtzKKta4kUpkC8kU%2BNq52dn%2Fucv%2FsDBESwaQ%2FnmOMi0uGJX18tmVrElB%2BnVWNIBtmY0Cut%2BvPjvajo8NykhLyxke7TrfmTRkEAcV82g8dco74hWl3pLwPS5mse74Mr%2BN1xgDcnpj0JaY5FnBnxp%2FTo4%2B8bdWyle85GDeeCa4%2BLiXRMCUOr3TtmFlf7QhrK0nxboiZKc4oknbwd9UGdslGocgtrjDXuv%2FSBjqkAVTyM%2BaCT0JksVzLtJHtslApq27oylCCQtl3SaueKldMj7aH4lr1PL8vj4WquSdkL9AwY9KaNweqhlR5ldpg5IAWk%2BETKwtErNeZl7KZ3iBgTp59mEw7KkWqlKuEGLvjT1QWhBBQbnFrGZHyma5G%2BoThdam7D9WqXytAh375bprRmGPE028MZso8G5WkMo7Np5dV6JZa%2BJrXPZau%2FhazhK0ZBFGx&X-Amz-Signature=d1dcdbca9e6c17defd22b07b65d248093265000629d07dd4db65b5d581a659ac&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/f0d81828-3c34-481b-86ae-f55b97bf59ff/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663RNBET7%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDovQj1U%2B6PQory5XTRakzc%2FcPZm0dOv9A%2BTkQmQ2RbhwIhAJNIChh4K3tWOxq2cpgJSVtWXRDKnZmnK0UYhwYZWv0uKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxGqi0RXExglpQp5r8q3ANCui422ifppptlK%2Fe0%2BxWzE6ef7esjKMqk9VrwVJ%2BrDo0vXGcRX8Kf9qIi%2F7tIEnLbMM3vhzLMumExbg%2BT%2FruxUk5MpBemTSkTx5RtPA0ZvPQFmGkmktPtR4r6%2FJc5LviU57l3ZhV3mo7aLh9R2nzJOBSp0KsmkUNI0CCfXeNI5ayP%2BUHWclUo37FIU33FvfGqStY6lRMn75j3FlJlsZoSdeI4DP6sb9WRkbjdQQz1NjrblzaqEZqxYUG3bKM3A0bo63GOpXIgkCSimoAbX58cmqjRi%2FOt%2FWky7hos9zCwk%2BCr7%2Bn3iTsocdSb%2BH0gUJ0u3zqbJImFoT4ex8Ox2XI%2FLwf7aWSm%2BhgUcH69bMa1creml6%2BaKenfFvnZuuBXkduLoC%2FULML1%2F0%2FPkzHGjpaMKHXnMdlYj0SNtzKKta4kUpkC8kU%2BNq52dn%2Fucv%2FsDBESwaQ%2FnmOMi0uGJX18tmVrElB%2BnVWNIBtmY0Cut%2BvPjvajo8NykhLyxke7TrfmTRkEAcV82g8dco74hWl3pLwPS5mse74Mr%2BN1xgDcnpj0JaY5FnBnxp%2FTo4%2B8bdWyle85GDeeCa4%2BLiXRMCUOr3TtmFlf7QhrK0nxboiZKc4oknbwd9UGdslGocgtrjDXuv%2FSBjqkAVTyM%2BaCT0JksVzLtJHtslApq27oylCCQtl3SaueKldMj7aH4lr1PL8vj4WquSdkL9AwY9KaNweqhlR5ldpg5IAWk%2BETKwtErNeZl7KZ3iBgTp59mEw7KkWqlKuEGLvjT1QWhBBQbnFrGZHyma5G%2BoThdam7D9WqXytAh375bprRmGPE028MZso8G5WkMo7Np5dV6JZa%2BJrXPZau%2FhazhK0ZBFGx&X-Amz-Signature=a8e4b59d4cbe1ac0389db87edb4d900416809268d574a62c6a0061b84abe4856&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/aee87363-261a-4346-a4c4-c3fa7b940bfb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663RNBET7%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDovQj1U%2B6PQory5XTRakzc%2FcPZm0dOv9A%2BTkQmQ2RbhwIhAJNIChh4K3tWOxq2cpgJSVtWXRDKnZmnK0UYhwYZWv0uKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxGqi0RXExglpQp5r8q3ANCui422ifppptlK%2Fe0%2BxWzE6ef7esjKMqk9VrwVJ%2BrDo0vXGcRX8Kf9qIi%2F7tIEnLbMM3vhzLMumExbg%2BT%2FruxUk5MpBemTSkTx5RtPA0ZvPQFmGkmktPtR4r6%2FJc5LviU57l3ZhV3mo7aLh9R2nzJOBSp0KsmkUNI0CCfXeNI5ayP%2BUHWclUo37FIU33FvfGqStY6lRMn75j3FlJlsZoSdeI4DP6sb9WRkbjdQQz1NjrblzaqEZqxYUG3bKM3A0bo63GOpXIgkCSimoAbX58cmqjRi%2FOt%2FWky7hos9zCwk%2BCr7%2Bn3iTsocdSb%2BH0gUJ0u3zqbJImFoT4ex8Ox2XI%2FLwf7aWSm%2BhgUcH69bMa1creml6%2BaKenfFvnZuuBXkduLoC%2FULML1%2F0%2FPkzHGjpaMKHXnMdlYj0SNtzKKta4kUpkC8kU%2BNq52dn%2Fucv%2FsDBESwaQ%2FnmOMi0uGJX18tmVrElB%2BnVWNIBtmY0Cut%2BvPjvajo8NykhLyxke7TrfmTRkEAcV82g8dco74hWl3pLwPS5mse74Mr%2BN1xgDcnpj0JaY5FnBnxp%2FTo4%2B8bdWyle85GDeeCa4%2BLiXRMCUOr3TtmFlf7QhrK0nxboiZKc4oknbwd9UGdslGocgtrjDXuv%2FSBjqkAVTyM%2BaCT0JksVzLtJHtslApq27oylCCQtl3SaueKldMj7aH4lr1PL8vj4WquSdkL9AwY9KaNweqhlR5ldpg5IAWk%2BETKwtErNeZl7KZ3iBgTp59mEw7KkWqlKuEGLvjT1QWhBBQbnFrGZHyma5G%2BoThdam7D9WqXytAh375bprRmGPE028MZso8G5WkMo7Np5dV6JZa%2BJrXPZau%2FhazhK0ZBFGx&X-Amz-Signature=38d7310dc463269102d1723fc5df07688dd73cc78c4bb5cfc220f238dd52ebe2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/57c6c46b-2670-4ff4-9220-cf2b282f7b95/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663RNBET7%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDovQj1U%2B6PQory5XTRakzc%2FcPZm0dOv9A%2BTkQmQ2RbhwIhAJNIChh4K3tWOxq2cpgJSVtWXRDKnZmnK0UYhwYZWv0uKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxGqi0RXExglpQp5r8q3ANCui422ifppptlK%2Fe0%2BxWzE6ef7esjKMqk9VrwVJ%2BrDo0vXGcRX8Kf9qIi%2F7tIEnLbMM3vhzLMumExbg%2BT%2FruxUk5MpBemTSkTx5RtPA0ZvPQFmGkmktPtR4r6%2FJc5LviU57l3ZhV3mo7aLh9R2nzJOBSp0KsmkUNI0CCfXeNI5ayP%2BUHWclUo37FIU33FvfGqStY6lRMn75j3FlJlsZoSdeI4DP6sb9WRkbjdQQz1NjrblzaqEZqxYUG3bKM3A0bo63GOpXIgkCSimoAbX58cmqjRi%2FOt%2FWky7hos9zCwk%2BCr7%2Bn3iTsocdSb%2BH0gUJ0u3zqbJImFoT4ex8Ox2XI%2FLwf7aWSm%2BhgUcH69bMa1creml6%2BaKenfFvnZuuBXkduLoC%2FULML1%2F0%2FPkzHGjpaMKHXnMdlYj0SNtzKKta4kUpkC8kU%2BNq52dn%2Fucv%2FsDBESwaQ%2FnmOMi0uGJX18tmVrElB%2BnVWNIBtmY0Cut%2BvPjvajo8NykhLyxke7TrfmTRkEAcV82g8dco74hWl3pLwPS5mse74Mr%2BN1xgDcnpj0JaY5FnBnxp%2FTo4%2B8bdWyle85GDeeCa4%2BLiXRMCUOr3TtmFlf7QhrK0nxboiZKc4oknbwd9UGdslGocgtrjDXuv%2FSBjqkAVTyM%2BaCT0JksVzLtJHtslApq27oylCCQtl3SaueKldMj7aH4lr1PL8vj4WquSdkL9AwY9KaNweqhlR5ldpg5IAWk%2BETKwtErNeZl7KZ3iBgTp59mEw7KkWqlKuEGLvjT1QWhBBQbnFrGZHyma5G%2BoThdam7D9WqXytAh375bprRmGPE028MZso8G5WkMo7Np5dV6JZa%2BJrXPZau%2FhazhK0ZBFGx&X-Amz-Signature=612e2092f7f647251208d8bd3a209ee9d0039fa7299ce95cabc588d94f22e1c7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/ad5a1d60-be8c-4a83-b9c6-1e28efad5efa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663RNBET7%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDovQj1U%2B6PQory5XTRakzc%2FcPZm0dOv9A%2BTkQmQ2RbhwIhAJNIChh4K3tWOxq2cpgJSVtWXRDKnZmnK0UYhwYZWv0uKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxGqi0RXExglpQp5r8q3ANCui422ifppptlK%2Fe0%2BxWzE6ef7esjKMqk9VrwVJ%2BrDo0vXGcRX8Kf9qIi%2F7tIEnLbMM3vhzLMumExbg%2BT%2FruxUk5MpBemTSkTx5RtPA0ZvPQFmGkmktPtR4r6%2FJc5LviU57l3ZhV3mo7aLh9R2nzJOBSp0KsmkUNI0CCfXeNI5ayP%2BUHWclUo37FIU33FvfGqStY6lRMn75j3FlJlsZoSdeI4DP6sb9WRkbjdQQz1NjrblzaqEZqxYUG3bKM3A0bo63GOpXIgkCSimoAbX58cmqjRi%2FOt%2FWky7hos9zCwk%2BCr7%2Bn3iTsocdSb%2BH0gUJ0u3zqbJImFoT4ex8Ox2XI%2FLwf7aWSm%2BhgUcH69bMa1creml6%2BaKenfFvnZuuBXkduLoC%2FULML1%2F0%2FPkzHGjpaMKHXnMdlYj0SNtzKKta4kUpkC8kU%2BNq52dn%2Fucv%2FsDBESwaQ%2FnmOMi0uGJX18tmVrElB%2BnVWNIBtmY0Cut%2BvPjvajo8NykhLyxke7TrfmTRkEAcV82g8dco74hWl3pLwPS5mse74Mr%2BN1xgDcnpj0JaY5FnBnxp%2FTo4%2B8bdWyle85GDeeCa4%2BLiXRMCUOr3TtmFlf7QhrK0nxboiZKc4oknbwd9UGdslGocgtrjDXuv%2FSBjqkAVTyM%2BaCT0JksVzLtJHtslApq27oylCCQtl3SaueKldMj7aH4lr1PL8vj4WquSdkL9AwY9KaNweqhlR5ldpg5IAWk%2BETKwtErNeZl7KZ3iBgTp59mEw7KkWqlKuEGLvjT1QWhBBQbnFrGZHyma5G%2BoThdam7D9WqXytAh375bprRmGPE028MZso8G5WkMo7Np5dV6JZa%2BJrXPZau%2FhazhK0ZBFGx&X-Amz-Signature=ad2c6c8dbc402702b06df5086bd932e43ecf5b03800bb4a940c0d0db4092e6c2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


```markdown
# jenkins 设置开机启动
## Centos 7 Linux创建Jenkins启动脚本以及开机启动服务

1.启动 jenkins 脚本
-------------------------------------------------------------
#!/bin/bash
#主要目的用于开机启动服务,不然 启动jenkins.war包没有java -jar的>权限
JAVA_HOME=/usr/local/cicd/jdk1.8.0_391/


pid=`ps -ef | grep jenkins.war | grep -v 'grep'| awk '{print $2}'| wc -l`
  if [ "$1" = "start" ];then
  if [ $pid -gt 0 ];then
  echo 'jenkins is running...'
else
  #java启动服务 配置java安装根路径,和启动war包存的根路径
  nohup $JAVA_HOME/bin/java -jar /usr/local/cicd/jenkins.war>jenkins.log --httpPort=8080  2>&1 &
  fi
  elif [ "$1" = "stop" ];then
  exec ps -ef | grep jenkins | grep -v grep | awk '{print $2}'| xargs kill -9
  echo 'jenkins is stop..'
else
  echo "Please input like this:"./jenkins.sh start" or "./jenkins stop""
  fi
-------------------------------------------------------------
注意：在写shell脚本时，开头一定要加上#!/bin/bash，否则执行该脚本会报错
根据自己的java安装目录，和jenkins.war包存放目录来修改脚本，我的脚本放在/usr/local/jenkins/目录下

2.让jenkins有可执行权限
登录后复制 
chmod +x /usr/local/cicd/jenkins.sh

补充：

启动jenkins
/usr/local/cicd/jenkins.sh start
1.
停止jenkins
/usr/local/cicd/jenkins.sh stop
3.配置开机启动服务
3.1 到 /lib/systemd/system 服务注册目录下创建 jenkins.service
--------------------------------------------------------------------
[Unit]
Description=Jenkins
After=network.target
 
[Service]
Type=forking
ExecStart=/usr/local/cicd//jenkins.sh start
ExecReload=
ExecStop=/usr/local/cicd/jenkins.sh stop
PrivateTmp=true
 
[Install]
WantedBy=multi-user.target
----------------------------------------------------------------
执行路径根据实际情况进行修改

3.2创建好服务后,执行一下命令刷新配置
systemctl daemon-reload

3.3启动脚本
systemctl start jenkins.service


3.4查看启动脚本状态是否启用成功(失败的话,看错误日志进行修改)
失败时，查看日志：journalctl -xe


systemctl status jenkins.service
```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/638425c2-dd78-4c7c-beb4-bfae125db33f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663RNBET7%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDovQj1U%2B6PQory5XTRakzc%2FcPZm0dOv9A%2BTkQmQ2RbhwIhAJNIChh4K3tWOxq2cpgJSVtWXRDKnZmnK0UYhwYZWv0uKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxGqi0RXExglpQp5r8q3ANCui422ifppptlK%2Fe0%2BxWzE6ef7esjKMqk9VrwVJ%2BrDo0vXGcRX8Kf9qIi%2F7tIEnLbMM3vhzLMumExbg%2BT%2FruxUk5MpBemTSkTx5RtPA0ZvPQFmGkmktPtR4r6%2FJc5LviU57l3ZhV3mo7aLh9R2nzJOBSp0KsmkUNI0CCfXeNI5ayP%2BUHWclUo37FIU33FvfGqStY6lRMn75j3FlJlsZoSdeI4DP6sb9WRkbjdQQz1NjrblzaqEZqxYUG3bKM3A0bo63GOpXIgkCSimoAbX58cmqjRi%2FOt%2FWky7hos9zCwk%2BCr7%2Bn3iTsocdSb%2BH0gUJ0u3zqbJImFoT4ex8Ox2XI%2FLwf7aWSm%2BhgUcH69bMa1creml6%2BaKenfFvnZuuBXkduLoC%2FULML1%2F0%2FPkzHGjpaMKHXnMdlYj0SNtzKKta4kUpkC8kU%2BNq52dn%2Fucv%2FsDBESwaQ%2FnmOMi0uGJX18tmVrElB%2BnVWNIBtmY0Cut%2BvPjvajo8NykhLyxke7TrfmTRkEAcV82g8dco74hWl3pLwPS5mse74Mr%2BN1xgDcnpj0JaY5FnBnxp%2FTo4%2B8bdWyle85GDeeCa4%2BLiXRMCUOr3TtmFlf7QhrK0nxboiZKc4oknbwd9UGdslGocgtrjDXuv%2FSBjqkAVTyM%2BaCT0JksVzLtJHtslApq27oylCCQtl3SaueKldMj7aH4lr1PL8vj4WquSdkL9AwY9KaNweqhlR5ldpg5IAWk%2BETKwtErNeZl7KZ3iBgTp59mEw7KkWqlKuEGLvjT1QWhBBQbnFrGZHyma5G%2BoThdam7D9WqXytAh375bprRmGPE028MZso8G5WkMo7Np5dV6JZa%2BJrXPZau%2FhazhK0ZBFGx&X-Amz-Signature=ca204bb74a4133b716ddf16811a19865a249d739c681578a0bc2a57564942a55&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```markdown
3.5设置开机启动
systemctl enable jenkins.service

3.6查看设置开机启动的服务列表
systemctl list-units --type=service
```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/af66ac91-4428-4c6c-9f31-df201b5de297/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663RNBET7%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDovQj1U%2B6PQory5XTRakzc%2FcPZm0dOv9A%2BTkQmQ2RbhwIhAJNIChh4K3tWOxq2cpgJSVtWXRDKnZmnK0UYhwYZWv0uKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxGqi0RXExglpQp5r8q3ANCui422ifppptlK%2Fe0%2BxWzE6ef7esjKMqk9VrwVJ%2BrDo0vXGcRX8Kf9qIi%2F7tIEnLbMM3vhzLMumExbg%2BT%2FruxUk5MpBemTSkTx5RtPA0ZvPQFmGkmktPtR4r6%2FJc5LviU57l3ZhV3mo7aLh9R2nzJOBSp0KsmkUNI0CCfXeNI5ayP%2BUHWclUo37FIU33FvfGqStY6lRMn75j3FlJlsZoSdeI4DP6sb9WRkbjdQQz1NjrblzaqEZqxYUG3bKM3A0bo63GOpXIgkCSimoAbX58cmqjRi%2FOt%2FWky7hos9zCwk%2BCr7%2Bn3iTsocdSb%2BH0gUJ0u3zqbJImFoT4ex8Ox2XI%2FLwf7aWSm%2BhgUcH69bMa1creml6%2BaKenfFvnZuuBXkduLoC%2FULML1%2F0%2FPkzHGjpaMKHXnMdlYj0SNtzKKta4kUpkC8kU%2BNq52dn%2Fucv%2FsDBESwaQ%2FnmOMi0uGJX18tmVrElB%2BnVWNIBtmY0Cut%2BvPjvajo8NykhLyxke7TrfmTRkEAcV82g8dco74hWl3pLwPS5mse74Mr%2BN1xgDcnpj0JaY5FnBnxp%2FTo4%2B8bdWyle85GDeeCa4%2BLiXRMCUOr3TtmFlf7QhrK0nxboiZKc4oknbwd9UGdslGocgtrjDXuv%2FSBjqkAVTyM%2BaCT0JksVzLtJHtslApq27oylCCQtl3SaueKldMj7aH4lr1PL8vj4WquSdkL9AwY9KaNweqhlR5ldpg5IAWk%2BETKwtErNeZl7KZ3iBgTp59mEw7KkWqlKuEGLvjT1QWhBBQbnFrGZHyma5G%2BoThdam7D9WqXytAh375bprRmGPE028MZso8G5WkMo7Np5dV6JZa%2BJrXPZau%2FhazhK0ZBFGx&X-Amz-Signature=ddffaf668bc401215f4c2085119dce9398975b7556b6e4537d98f67f9a29df9c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```markdown
3.7停止服务命令
systemctl stop jenkins.service
```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/0628a4bc-ae63-46bc-a41e-f2a1be0b30e7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46663RNBET7%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234345Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDovQj1U%2B6PQory5XTRakzc%2FcPZm0dOv9A%2BTkQmQ2RbhwIhAJNIChh4K3tWOxq2cpgJSVtWXRDKnZmnK0UYhwYZWv0uKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxGqi0RXExglpQp5r8q3ANCui422ifppptlK%2Fe0%2BxWzE6ef7esjKMqk9VrwVJ%2BrDo0vXGcRX8Kf9qIi%2F7tIEnLbMM3vhzLMumExbg%2BT%2FruxUk5MpBemTSkTx5RtPA0ZvPQFmGkmktPtR4r6%2FJc5LviU57l3ZhV3mo7aLh9R2nzJOBSp0KsmkUNI0CCfXeNI5ayP%2BUHWclUo37FIU33FvfGqStY6lRMn75j3FlJlsZoSdeI4DP6sb9WRkbjdQQz1NjrblzaqEZqxYUG3bKM3A0bo63GOpXIgkCSimoAbX58cmqjRi%2FOt%2FWky7hos9zCwk%2BCr7%2Bn3iTsocdSb%2BH0gUJ0u3zqbJImFoT4ex8Ox2XI%2FLwf7aWSm%2BhgUcH69bMa1creml6%2BaKenfFvnZuuBXkduLoC%2FULML1%2F0%2FPkzHGjpaMKHXnMdlYj0SNtzKKta4kUpkC8kU%2BNq52dn%2Fucv%2FsDBESwaQ%2FnmOMi0uGJX18tmVrElB%2BnVWNIBtmY0Cut%2BvPjvajo8NykhLyxke7TrfmTRkEAcV82g8dco74hWl3pLwPS5mse74Mr%2BN1xgDcnpj0JaY5FnBnxp%2FTo4%2B8bdWyle85GDeeCa4%2BLiXRMCUOr3TtmFlf7QhrK0nxboiZKc4oknbwd9UGdslGocgtrjDXuv%2FSBjqkAVTyM%2BaCT0JksVzLtJHtslApq27oylCCQtl3SaueKldMj7aH4lr1PL8vj4WquSdkL9AwY9KaNweqhlR5ldpg5IAWk%2BETKwtErNeZl7KZ3iBgTp59mEw7KkWqlKuEGLvjT1QWhBBQbnFrGZHyma5G%2BoThdam7D9WqXytAh375bprRmGPE028MZso8G5WkMo7Np5dV6JZa%2BJrXPZau%2FhazhK0ZBFGx&X-Amz-Signature=86b810db1115770fbd46f481d4dbc61e32045fc8857936b2656938d2a8e47e4b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)







---
title: 1-9 附黑白名单控制文档说明
---

# 1-9 附黑白名单控制文档说明

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/075630a9-40f1-4685-8abc-41624be3b0cb/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665DT3WM6C%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIELag3VL108PQpUAPnEa5py3ks%2BvRPCSGh1ZyBFO1I4EAiB%2BrflfmQfJdEmlvOa%2B2u5QjBZAgpmRVa26ho3f0WjnsiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM0uKgl5%2BIZZXDMDTWKtwD6FHy38AMwyOrbpu4BzDvpi4BMmpdCk6G40fPNWDaHz0eldTaJXBSfkN%2B8uRR7vTI8w%2B7Q0GE7mqEvRiBwKr%2BfUMSvp0zaaUVmFAPhpWzjjrB0zrwtu4GhWZMLe4yuat2C2lLq%2Fk4mehbrkQ7WDgPhVW85PwWGU5COJLCA5q4AwM9srDYNjIfhBl2jKXD82a1H%2Bl3hWnlL1fWDOjVaffYfi8cNYI9saio%2FKOFlRXe62Nm%2Fqb8YtmlsEuq1ZKhi2JoXs721m0MXHlq%2BlarNEvr%2F1nSzKtMqE9xPMKHksoePKHL%2BKYA11MvzLLFlr%2BFUccOwl7n%2BGjSecMr13NaUPfEF6uZWPuiryCeXh4346NjNgzAkNMWM80lzcCoB6q%2BV7Gy87ZNEh1rLjm%2Foni6yfSSEL6i3q3dcjOKsAjZHRs7DFgXnh8%2BYMlJ6gFDwFvLCVQECTtmAxyaeBtfQsdDAmG6b4x%2FY6jZlgl44JvlVrV3LFNkVP4HdD0V2d%2FzNr1QpJvuvx2I4ueM8kPEIgOWIs%2Bbt%2B560U%2Bvzxuc%2BOS71OK%2F6WDVY%2BIpyGxNHQHI7y%2BRGawseB7lV%2BPTs3ylJ735kakCoZ7rLWfA%2BhjaGlLy1gfztwYA2uzYNkDsqZY%2F26gwg7f%2F0gY6pgE42OJAJprlAtRVn4PSXVC0g74j%2BBcQRRyFppsZwwDQLxqFBeSd2qp8noTRpZX8RatQQXWcyxZv8Av8yFTa2lcIn4Mz9F3cJK93LaG5PtM%2FTvONIbmSZH2l3gwC5WrTPYtJN7DPjeix7VFWzyhCAY%2Bxs2srGNPSM%2BExFuftW7veNjixogh1SugjZXJh33sru3Htjiz8WsSJoP5qeoKSCm0pD5dj4pSz&X-Amz-Signature=10a8872282d6f669ebc31954843fde3866e6f7a90adb235414bfa8f42a851b46&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

**概述**

很多时候，我们需要根据调用方来限制资源是否通过，这时候可以使用 Sentinel 的黑白名单控制的功能。黑白名单根据资源的请求来源（origin）限制资源是否通过，若配置白名单则只有请求来源位于白名单内时才可通过；若配置黑名单则请求来源位于黑名单时不通过，其余的请求通过。

调用方信息通过 ContextUtil.enter(resourceName, origin) 方法中的 origin 参数传入。

**规则配置**

黑白名单规则（AuthorityRule）非常简单，主要有以下配置项：

```java
resource：资源名，即限流规则的作用对象

limitApp：对应的黑名单/白名单，不同 origin 用 , 分隔，如 appA,appB

strategy：限制模式，AUTHORITY_WHITE 为白名单模式，

AUTHORITY_BLACK 为黑名单模式，默认为白名单模式
```

**示例**

比如我们希望控制对资源 test 的访问设置白名单，只有来源为 appA 和 appB 的请求才可通过，则可以配置如下白名单规则：

```java
AuthorityRule rule = new AuthorityRule();

rule.setResource("test");

// 白名单规则

rule.setStrategy(RuleConstant.AUTHORITY_WHITE);

// 限制的app

rule.setLimitApp("appA,appB");

AuthorityRuleManager.loadRules(Collections.singletonList(rule));
```

详细示例请参考 [AuthorityDemo](https://github.com/alibaba/Sentinel/blob/master/sentinel-demo/sentinel-demo-basic/src/main/java/com/alibaba/csp/sentinel/demo/authority/AuthorityDemo.java).

输出结果：

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/9b966de3-6047-4db9-8cf2-b29095a1e94a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665DT3WM6C%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIELag3VL108PQpUAPnEa5py3ks%2BvRPCSGh1ZyBFO1I4EAiB%2BrflfmQfJdEmlvOa%2B2u5QjBZAgpmRVa26ho3f0WjnsiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM0uKgl5%2BIZZXDMDTWKtwD6FHy38AMwyOrbpu4BzDvpi4BMmpdCk6G40fPNWDaHz0eldTaJXBSfkN%2B8uRR7vTI8w%2B7Q0GE7mqEvRiBwKr%2BfUMSvp0zaaUVmFAPhpWzjjrB0zrwtu4GhWZMLe4yuat2C2lLq%2Fk4mehbrkQ7WDgPhVW85PwWGU5COJLCA5q4AwM9srDYNjIfhBl2jKXD82a1H%2Bl3hWnlL1fWDOjVaffYfi8cNYI9saio%2FKOFlRXe62Nm%2Fqb8YtmlsEuq1ZKhi2JoXs721m0MXHlq%2BlarNEvr%2F1nSzKtMqE9xPMKHksoePKHL%2BKYA11MvzLLFlr%2BFUccOwl7n%2BGjSecMr13NaUPfEF6uZWPuiryCeXh4346NjNgzAkNMWM80lzcCoB6q%2BV7Gy87ZNEh1rLjm%2Foni6yfSSEL6i3q3dcjOKsAjZHRs7DFgXnh8%2BYMlJ6gFDwFvLCVQECTtmAxyaeBtfQsdDAmG6b4x%2FY6jZlgl44JvlVrV3LFNkVP4HdD0V2d%2FzNr1QpJvuvx2I4ueM8kPEIgOWIs%2Bbt%2B560U%2Bvzxuc%2BOS71OK%2F6WDVY%2BIpyGxNHQHI7y%2BRGawseB7lV%2BPTs3ylJ735kakCoZ7rLWfA%2BhjaGlLy1gfztwYA2uzYNkDsqZY%2F26gwg7f%2F0gY6pgE42OJAJprlAtRVn4PSXVC0g74j%2BBcQRRyFppsZwwDQLxqFBeSd2qp8noTRpZX8RatQQXWcyxZv8Av8yFTa2lcIn4Mz9F3cJK93LaG5PtM%2FTvONIbmSZH2l3gwC5WrTPYtJN7DPjeix7VFWzyhCAY%2Bxs2srGNPSM%2BExFuftW7veNjixogh1SugjZXJh33sru3Htjiz8WsSJoP5qeoKSCm0pD5dj4pSz&X-Amz-Signature=05aad28113f0c5d6e6fb2fdac7e9e18a633161f99441487b30fc59e1d462e6e4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/8a58f1a7-6808-4895-b4f6-bf0413570378/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4665DT3WM6C%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225831Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIELag3VL108PQpUAPnEa5py3ks%2BvRPCSGh1ZyBFO1I4EAiB%2BrflfmQfJdEmlvOa%2B2u5QjBZAgpmRVa26ho3f0WjnsiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIM0uKgl5%2BIZZXDMDTWKtwD6FHy38AMwyOrbpu4BzDvpi4BMmpdCk6G40fPNWDaHz0eldTaJXBSfkN%2B8uRR7vTI8w%2B7Q0GE7mqEvRiBwKr%2BfUMSvp0zaaUVmFAPhpWzjjrB0zrwtu4GhWZMLe4yuat2C2lLq%2Fk4mehbrkQ7WDgPhVW85PwWGU5COJLCA5q4AwM9srDYNjIfhBl2jKXD82a1H%2Bl3hWnlL1fWDOjVaffYfi8cNYI9saio%2FKOFlRXe62Nm%2Fqb8YtmlsEuq1ZKhi2JoXs721m0MXHlq%2BlarNEvr%2F1nSzKtMqE9xPMKHksoePKHL%2BKYA11MvzLLFlr%2BFUccOwl7n%2BGjSecMr13NaUPfEF6uZWPuiryCeXh4346NjNgzAkNMWM80lzcCoB6q%2BV7Gy87ZNEh1rLjm%2Foni6yfSSEL6i3q3dcjOKsAjZHRs7DFgXnh8%2BYMlJ6gFDwFvLCVQECTtmAxyaeBtfQsdDAmG6b4x%2FY6jZlgl44JvlVrV3LFNkVP4HdD0V2d%2FzNr1QpJvuvx2I4ueM8kPEIgOWIs%2Bbt%2B560U%2Bvzxuc%2BOS71OK%2F6WDVY%2BIpyGxNHQHI7y%2BRGawseB7lV%2BPTs3ylJ735kakCoZ7rLWfA%2BhjaGlLy1gfztwYA2uzYNkDsqZY%2F26gwg7f%2F0gY6pgE42OJAJprlAtRVn4PSXVC0g74j%2BBcQRRyFppsZwwDQLxqFBeSd2qp8noTRpZX8RatQQXWcyxZv8Av8yFTa2lcIn4Mz9F3cJK93LaG5PtM%2FTvONIbmSZH2l3gwC5WrTPYtJN7DPjeix7VFWzyhCAY%2Bxs2srGNPSM%2BExFuftW7veNjixogh1SugjZXJh33sru3Htjiz8WsSJoP5qeoKSCm0pD5dj4pSz&X-Amz-Signature=504827f305dc2e4ceb542266f4c9bd0e8f5022a7668d3e1d7aa39961bd239a92&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


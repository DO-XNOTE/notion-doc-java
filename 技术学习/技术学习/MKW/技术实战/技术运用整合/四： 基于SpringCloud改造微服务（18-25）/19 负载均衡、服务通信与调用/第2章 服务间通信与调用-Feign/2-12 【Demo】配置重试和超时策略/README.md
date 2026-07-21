---
title: 2-12 【Demo】配置重试和超时策略
---

# 2-12 【Demo】配置重试和超时策略

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/8cf37f26-400a-4ca9-971c-5c7496f97b4f/SCR-20240820-qcyp.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SGL4J3B2%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225627Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCRv1zzQ5mzDEetXoLIg3%2Bthr02FfBrhj%2FbXQoEzkfVcAIgS2KzolitdsmB6e2Z2ADundnkAjiMg2%2B%2BSlWMWO1%2F804qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD0YdWMHzVMbqOU0OyrcA0Q2IO2%2BHKo5eaZ2Jr%2FJfJ5EyR%2F3Cs8DvCWk0CJF7bT61kuRuAkXNVFH1K1wcTkkJ%2BxhH6lZ4sbvPOsgOvG6Qs2BukTrbx%2FpZhWLBr5YGxTaQ4wgfdV72AMiBOkB17ONQrgOB4FdE6o%2FKDcoMzB1AeTtP5RR63NKqS394%2BSTiTlHMmP27YmWOUwRoVEi3GzWn%2BXO4M%2BAW2CMnubaILEKwL%2BqsbLGrVflwaJF93tDPxo%2Buwa5F8fE5U1xJ89YFuQPB3kfR9O5frtQ3xG%2FyUCzbZKqXp%2BMCYR%2FxJ1eiY0QsEtDuJuhKQnZ4lG2hgsMZPul6h0auiZ%2F1p1HPmVQdqsrgHqoT36ZpXSjbDmIGreWH67dWlY0%2Fr8RanrVQmFtX%2B9qTUTUFUaA362fWxcnrgie8vQPlT2bd9r65mSNdVvg4sCCft3jiCAYSP2ujppiYnnGZrzJzs7eAHzhxMnJg8GBzl64FTJ%2BvNwF0sMGoy7sfMzT6pP18oL3maEuUICo5skZtC%2BIe6sGSrY%2FKalL4v137US3Qo9s9vQLGjLPWAhuuGEehejzFydr9DMniT6MNr8z4LRrxLceB5bHj25lXUah7wVFbkF%2BIOInpbushbueIn2dhPgaBiWd%2FByAp%2FZXMNu3%2F9IGOqUB9yNH%2FmZSB0znQuKN4U%2FzjP9%2FRlZb4J3QIbCLLNt3deu%2FiYt5%2F5VHSA6ziE%2F1wvhMfAHrYeIn0A%2FrjZH8YkNAsEHHsr3mnLP7kwZZzYnUcnBzDbJQbP1545t7Cpvhb0QAgiOb2ukr34kAzc5lXWr4Qvn7ioup4Qpw9DGDsBImdtpauyEyvOhF0lXRHmJP27OJOkJlPDHeijdeKvD1ELs8Ga%2BveBiO&X-Amz-Signature=736d9227506f3580965f5ced34a8d1f994b7631a50959d0b6a796545e17a9142&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/76e58eee-eefd-4e6f-802d-daabff7f6f99/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SGL4J3B2%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225627Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCRv1zzQ5mzDEetXoLIg3%2Bthr02FfBrhj%2FbXQoEzkfVcAIgS2KzolitdsmB6e2Z2ADundnkAjiMg2%2B%2BSlWMWO1%2F804qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD0YdWMHzVMbqOU0OyrcA0Q2IO2%2BHKo5eaZ2Jr%2FJfJ5EyR%2F3Cs8DvCWk0CJF7bT61kuRuAkXNVFH1K1wcTkkJ%2BxhH6lZ4sbvPOsgOvG6Qs2BukTrbx%2FpZhWLBr5YGxTaQ4wgfdV72AMiBOkB17ONQrgOB4FdE6o%2FKDcoMzB1AeTtP5RR63NKqS394%2BSTiTlHMmP27YmWOUwRoVEi3GzWn%2BXO4M%2BAW2CMnubaILEKwL%2BqsbLGrVflwaJF93tDPxo%2Buwa5F8fE5U1xJ89YFuQPB3kfR9O5frtQ3xG%2FyUCzbZKqXp%2BMCYR%2FxJ1eiY0QsEtDuJuhKQnZ4lG2hgsMZPul6h0auiZ%2F1p1HPmVQdqsrgHqoT36ZpXSjbDmIGreWH67dWlY0%2Fr8RanrVQmFtX%2B9qTUTUFUaA362fWxcnrgie8vQPlT2bd9r65mSNdVvg4sCCft3jiCAYSP2ujppiYnnGZrzJzs7eAHzhxMnJg8GBzl64FTJ%2BvNwF0sMGoy7sfMzT6pP18oL3maEuUICo5skZtC%2BIe6sGSrY%2FKalL4v137US3Qo9s9vQLGjLPWAhuuGEehejzFydr9DMniT6MNr8z4LRrxLceB5bHj25lXUah7wVFbkF%2BIOInpbushbueIn2dhPgaBiWd%2FByAp%2FZXMNu3%2F9IGOqUB9yNH%2FmZSB0znQuKN4U%2FzjP9%2FRlZb4J3QIbCLLNt3deu%2FiYt5%2F5VHSA6ziE%2F1wvhMfAHrYeIn0A%2FrjZH8YkNAsEHHsr3mnLP7kwZZzYnUcnBzDbJQbP1545t7Cpvhb0QAgiOb2ukr34kAzc5lXWr4Qvn7ioup4Qpw9DGDsBImdtpauyEyvOhF0lXRHmJP27OJOkJlPDHeijdeKvD1ELs8Ga%2BveBiO&X-Amz-Signature=0def7c959a7e4c2df427ed198758a3b97d5fe87268c8d474d5c97418d927f560&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/f4525186-eec4-4715-a04b-8d6e50681db8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SGL4J3B2%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225627Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCRv1zzQ5mzDEetXoLIg3%2Bthr02FfBrhj%2FbXQoEzkfVcAIgS2KzolitdsmB6e2Z2ADundnkAjiMg2%2B%2BSlWMWO1%2F804qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD0YdWMHzVMbqOU0OyrcA0Q2IO2%2BHKo5eaZ2Jr%2FJfJ5EyR%2F3Cs8DvCWk0CJF7bT61kuRuAkXNVFH1K1wcTkkJ%2BxhH6lZ4sbvPOsgOvG6Qs2BukTrbx%2FpZhWLBr5YGxTaQ4wgfdV72AMiBOkB17ONQrgOB4FdE6o%2FKDcoMzB1AeTtP5RR63NKqS394%2BSTiTlHMmP27YmWOUwRoVEi3GzWn%2BXO4M%2BAW2CMnubaILEKwL%2BqsbLGrVflwaJF93tDPxo%2Buwa5F8fE5U1xJ89YFuQPB3kfR9O5frtQ3xG%2FyUCzbZKqXp%2BMCYR%2FxJ1eiY0QsEtDuJuhKQnZ4lG2hgsMZPul6h0auiZ%2F1p1HPmVQdqsrgHqoT36ZpXSjbDmIGreWH67dWlY0%2Fr8RanrVQmFtX%2B9qTUTUFUaA362fWxcnrgie8vQPlT2bd9r65mSNdVvg4sCCft3jiCAYSP2ujppiYnnGZrzJzs7eAHzhxMnJg8GBzl64FTJ%2BvNwF0sMGoy7sfMzT6pP18oL3maEuUICo5skZtC%2BIe6sGSrY%2FKalL4v137US3Qo9s9vQLGjLPWAhuuGEehejzFydr9DMniT6MNr8z4LRrxLceB5bHj25lXUah7wVFbkF%2BIOInpbushbueIn2dhPgaBiWd%2FByAp%2FZXMNu3%2F9IGOqUB9yNH%2FmZSB0znQuKN4U%2FzjP9%2FRlZb4J3QIbCLLNt3deu%2FiYt5%2F5VHSA6ziE%2F1wvhMfAHrYeIn0A%2FrjZH8YkNAsEHHsr3mnLP7kwZZzYnUcnBzDbJQbP1545t7Cpvhb0QAgiOb2ukr34kAzc5lXWr4Qvn7ioup4Qpw9DGDsBImdtpauyEyvOhF0lXRHmJP27OJOkJlPDHeijdeKvD1ELs8Ga%2BveBiO&X-Amz-Signature=d9e6dc88cd6fbab8d740fdab043d861f8ea16d6a314d503f0a854b09720c0c5f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/7742525f-0ab3-4a0c-9582-0f36cba2a86f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SGL4J3B2%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225627Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCRv1zzQ5mzDEetXoLIg3%2Bthr02FfBrhj%2FbXQoEzkfVcAIgS2KzolitdsmB6e2Z2ADundnkAjiMg2%2B%2BSlWMWO1%2F804qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD0YdWMHzVMbqOU0OyrcA0Q2IO2%2BHKo5eaZ2Jr%2FJfJ5EyR%2F3Cs8DvCWk0CJF7bT61kuRuAkXNVFH1K1wcTkkJ%2BxhH6lZ4sbvPOsgOvG6Qs2BukTrbx%2FpZhWLBr5YGxTaQ4wgfdV72AMiBOkB17ONQrgOB4FdE6o%2FKDcoMzB1AeTtP5RR63NKqS394%2BSTiTlHMmP27YmWOUwRoVEi3GzWn%2BXO4M%2BAW2CMnubaILEKwL%2BqsbLGrVflwaJF93tDPxo%2Buwa5F8fE5U1xJ89YFuQPB3kfR9O5frtQ3xG%2FyUCzbZKqXp%2BMCYR%2FxJ1eiY0QsEtDuJuhKQnZ4lG2hgsMZPul6h0auiZ%2F1p1HPmVQdqsrgHqoT36ZpXSjbDmIGreWH67dWlY0%2Fr8RanrVQmFtX%2B9qTUTUFUaA362fWxcnrgie8vQPlT2bd9r65mSNdVvg4sCCft3jiCAYSP2ujppiYnnGZrzJzs7eAHzhxMnJg8GBzl64FTJ%2BvNwF0sMGoy7sfMzT6pP18oL3maEuUICo5skZtC%2BIe6sGSrY%2FKalL4v137US3Qo9s9vQLGjLPWAhuuGEehejzFydr9DMniT6MNr8z4LRrxLceB5bHj25lXUah7wVFbkF%2BIOInpbushbueIn2dhPgaBiWd%2FByAp%2FZXMNu3%2F9IGOqUB9yNH%2FmZSB0znQuKN4U%2FzjP9%2FRlZb4J3QIbCLLNt3deu%2FiYt5%2F5VHSA6ziE%2F1wvhMfAHrYeIn0A%2FrjZH8YkNAsEHHsr3mnLP7kwZZzYnUcnBzDbJQbP1545t7Cpvhb0QAgiOb2ukr34kAzc5lXWr4Qvn7ioup4Qpw9DGDsBImdtpauyEyvOhF0lXRHmJP27OJOkJlPDHeijdeKvD1ELs8Ga%2BveBiO&X-Amz-Signature=a5b893d5f50a397ff94e98ec3254aa7142fc0474865f2f3b7615ce2252fe9e50&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

hello 慕课网的各位同学们，大家好，这一节老师来清旧账来了什么旧账。上一节当中瑞本遗留了两个知识点，分别是超时和重试。对不对？那既然瑞本已经集成到了 fin 里面，这一节我们就从 fin 的角度来看，如何借助瑞本实现超时判定还有重试。好，这一节主要分为三个部分。第一部分我既然要构造一个超时和重试场景，那么必定需要一个 100% 会超时的方法。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/99828322-e16f-42d1-a08b-db6f269f19ae/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SGL4J3B2%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225627Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCRv1zzQ5mzDEetXoLIg3%2Bthr02FfBrhj%2FbXQoEzkfVcAIgS2KzolitdsmB6e2Z2ADundnkAjiMg2%2B%2BSlWMWO1%2F804qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD0YdWMHzVMbqOU0OyrcA0Q2IO2%2BHKo5eaZ2Jr%2FJfJ5EyR%2F3Cs8DvCWk0CJF7bT61kuRuAkXNVFH1K1wcTkkJ%2BxhH6lZ4sbvPOsgOvG6Qs2BukTrbx%2FpZhWLBr5YGxTaQ4wgfdV72AMiBOkB17ONQrgOB4FdE6o%2FKDcoMzB1AeTtP5RR63NKqS394%2BSTiTlHMmP27YmWOUwRoVEi3GzWn%2BXO4M%2BAW2CMnubaILEKwL%2BqsbLGrVflwaJF93tDPxo%2Buwa5F8fE5U1xJ89YFuQPB3kfR9O5frtQ3xG%2FyUCzbZKqXp%2BMCYR%2FxJ1eiY0QsEtDuJuhKQnZ4lG2hgsMZPul6h0auiZ%2F1p1HPmVQdqsrgHqoT36ZpXSjbDmIGreWH67dWlY0%2Fr8RanrVQmFtX%2B9qTUTUFUaA362fWxcnrgie8vQPlT2bd9r65mSNdVvg4sCCft3jiCAYSP2ujppiYnnGZrzJzs7eAHzhxMnJg8GBzl64FTJ%2BvNwF0sMGoy7sfMzT6pP18oL3maEuUICo5skZtC%2BIe6sGSrY%2FKalL4v137US3Qo9s9vQLGjLPWAhuuGEehejzFydr9DMniT6MNr8z4LRrxLceB5bHj25lXUah7wVFbkF%2BIOInpbushbueIn2dhPgaBiWd%2FByAp%2FZXMNu3%2F9IGOqUB9yNH%2FmZSB0znQuKN4U%2FzjP9%2FRlZb4J3QIbCLLNt3deu%2FiYt5%2F5VHSA6ziE%2F1wvhMfAHrYeIn0A%2FrjZH8YkNAsEHHsr3mnLP7kwZZzYnUcnBzDbJQbP1545t7Cpvhb0QAgiOb2ukr34kAzc5lXWr4Qvn7ioup4Qpw9DGDsBImdtpauyEyvOhF0lXRHmJP27OJOkJlPDHeijdeKvD1ELs8Ga%2BveBiO&X-Amz-Signature=ff9c679b64d81def7882e0d9a3deeea69fd8c6166908d85518223797981adcb5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/c636ae82-aeb6-4d68-969b-b4f4bff71ff4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SGL4J3B2%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225627Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCRv1zzQ5mzDEetXoLIg3%2Bthr02FfBrhj%2FbXQoEzkfVcAIgS2KzolitdsmB6e2Z2ADundnkAjiMg2%2B%2BSlWMWO1%2F804qiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD0YdWMHzVMbqOU0OyrcA0Q2IO2%2BHKo5eaZ2Jr%2FJfJ5EyR%2F3Cs8DvCWk0CJF7bT61kuRuAkXNVFH1K1wcTkkJ%2BxhH6lZ4sbvPOsgOvG6Qs2BukTrbx%2FpZhWLBr5YGxTaQ4wgfdV72AMiBOkB17ONQrgOB4FdE6o%2FKDcoMzB1AeTtP5RR63NKqS394%2BSTiTlHMmP27YmWOUwRoVEi3GzWn%2BXO4M%2BAW2CMnubaILEKwL%2BqsbLGrVflwaJF93tDPxo%2Buwa5F8fE5U1xJ89YFuQPB3kfR9O5frtQ3xG%2FyUCzbZKqXp%2BMCYR%2FxJ1eiY0QsEtDuJuhKQnZ4lG2hgsMZPul6h0auiZ%2F1p1HPmVQdqsrgHqoT36ZpXSjbDmIGreWH67dWlY0%2Fr8RanrVQmFtX%2B9qTUTUFUaA362fWxcnrgie8vQPlT2bd9r65mSNdVvg4sCCft3jiCAYSP2ujppiYnnGZrzJzs7eAHzhxMnJg8GBzl64FTJ%2BvNwF0sMGoy7sfMzT6pP18oL3maEuUICo5skZtC%2BIe6sGSrY%2FKalL4v137US3Qo9s9vQLGjLPWAhuuGEehejzFydr9DMniT6MNr8z4LRrxLceB5bHj25lXUah7wVFbkF%2BIOInpbushbueIn2dhPgaBiWd%2FByAp%2FZXMNu3%2F9IGOqUB9yNH%2FmZSB0znQuKN4U%2FzjP9%2FRlZb4J3QIbCLLNt3deu%2FiYt5%2F5VHSA6ziE%2F1wvhMfAHrYeIn0A%2FrjZH8YkNAsEHHsr3mnLP7kwZZzYnUcnBzDbJQbP1545t7Cpvhb0QAgiOb2ukr34kAzc5lXWr4Qvn7ioup4Qpw9DGDsBImdtpauyEyvOhF0lXRHmJP27OJOkJlPDHeijdeKvD1ELs8Ga%2BveBiO&X-Amz-Signature=2c2624ad99cec923605a0ef1a07588d1b400ea7cf36c162264183096bb74be0b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

有了这个方法以后，我们再看如何借助 ribbon 来配置超时和重试的配置项。最后一点，我们知道 ribbon 不仅可以在当前节点重试，它也可以在其他节点重试。那么我们就开启多个服务提供者来看我们的服务调用者是如何在本节点重试失败之后，再选择其他节点来进行重试的。大家抄起家伙到主场开拔。又到了主场了，我们大声喊出自己的口号，没哪个同学喊没有蛀牙的，我们口号是每天扣丁 1 小时，健康工作 50 年。对不对？今天我们需要创建新的茅酒吗？不需要，我们一言不合，就是拿起就干，直接在 fin 的 consumer 里做一些配置改动就好了。所以这是个非常轻轻松松的一节的配置在哪里？ application.properties 对不对？今天要配置什么内容？大概 123455 个属性，我们先从第一个属性开始讲起。



第一个属性它的配置格式是什么呢？我们要先把服务名给打上去，服务名是谁调用方调用方就是分 client 接下来所有的属性后面都跟着 ribbon 大家看，把这一段先给复制下来，后面就要 copy 来用的。你看咱配置的是 ribbon 但是起作用的是在哪里在 fin 里面起作用的。所以 ribbon 就是 fin 的左膀右臂一元心腹。咱们从今往后都不会单独使用，ribbon都会搭配一些组件来使用。比方说这一张咱是 fen 接下来往后那就是其他组件了，比如说 gateway 等等。


接下来的名称是什么？ fen 的名称可没这么长。 max auto retries 大家记得这个 retry 有 S 不是 retry 你要是配 retry 它不起作用的，说明它这会多次 retry 对不对？后面跟次数。那它是什么业务含义呢？它的业务含义是指每台机器最大的重试次数。那什么是每台机器最大重试次数？这个看起来有点蒙圈我这样给大家打个比方，如果你调用了分 client 的服务，并且发生超时，那么在当前这台机器上发生超时的这台服务器上，它最多可以重试两次。如果它转移到其他的服务器上进行重试，那么它能重试几次依然是两次。这个就是限制了你最多可以在每立的机器上从事多少次。


好，那我们接下来配置第二个参数，它前面的开头和这个参数是一模一样的，所以我们把它直接 copy 下来。那后面跟什么呢？后面跟的东西不一样嘞？ next server 同学们这里应该可以看出什么椴倪了对不对？ next server 是指在下一个节点上进行重试，那它这个 2 是什么含义呢？是指下一个节点可以进行重试的次数吗？同学们看了图文教程那个复杂的方程式还有印象吗？这里告诉大家，它不是纸可以重试的次数，而是纸可以再重试几台机器。比方说你现在服务器集群中有 1000 台机器，那么他第一次调用超时了，重试两次依然超时。那接下来他需要换一台服务器进行重试啦。对不对，那他可以换几台？它总共可以换两台，也就是总共算上当前第一次访问的那台机器，它可以在三台机器上分别发生重试。而在每台机器上最大的重试次数是谁控制的第一个参数？ OK 大家听到这里有没有，蒙圈的同学赶紧回去看一下图文教程里面给出的方程式。


好，接下来我们要配置一些更简单易懂的属性了。上面两个属性设置了重试的行为，一台机器不行，我换个姿势再来一次，那光有行为还不够，我们还要约束时间对不对？好，后面的第三个属性它就跟时间有关系了，我们前面还是以分 client 瑞本开头，接下来它叫 connect time out 什么含义，这个从字面意思上也非常好理解，它是指连接超时。那通常我们一个 HDD P 访问请求，它的连接所花费的时间实际上是非常短的，真正花时间实际上是业务处理。而连接部分，我们可以把它的超时时间设置的短一些。在正常的生产环境中，大家设置成个 200 毫秒 300 毫秒其实就绰绰有余了。我这里 demo 把它设置成了 1000 毫秒。


Ok. 第四个属性依然和时间有关，它是以份克兰特瑞本开头，后面跟什么呢？ Read time out. 这个属性就是跟业务处理有点那么关系了，一个 htd P request 中大部分的时间都花费在业务处理上了，对不对？所以这个业务处理超时的时间，我们可以把它设置的稍微长那么一点，根据不同的服务类型设置不同的服务超时要求。我这里暂时把它设置成2000，单位是毫秒。


接下来就是最后一个属性了。它的名字大家看非常奇怪，开头还是这个开头，但是后面跟的名字叫 OK 这个 K 是小写，大家注意不是两个全大写。 Ok. to retry on all operations 什么含义？它是指你是否可以在所有的 HT DP method 上进行重试。言下之意，如果你没有把它开启，它的默认是 false 的，那么这种情况下它就不会在所有的 HTTP method 上进行重试。我们说的 HT T method 就是像 post getput delete options 这些方法默认情况下，它就在 get 之类不会改动数据的方法上进行重试。所以我也建议大家在正式的生产环境中谨慎地开启这个开关。因为某些 pose 的请求它涉及到对数据的改动对不对？在很多情况下，我们并不会对 pose 的方法做幂等性检查。那么在这种情况下，你对非幂等性的接口进行重试，那可能就会发生数据不一致的情况。所以谨记，如果对 post put delete 这类方法进行重试，一定要保证它后台的接口实现了严格的幂等性。


那我们所有的配置到这里就全部配置完了。接下来就要去 controller 里创建一个必定超时的接口来配合我们后面的测试。在开始创建 controller 方法之前，我们先把这些配置属性给它 copy 进来，复制到另外一个项目当中。


读越乐与重，乐熟乐无弱与重我们的分 consumer 享受了重试的策略，也要把这个优惠政策分享给另外一个分 consumer 也就是我们昨天创建的分 consumer advanced 对不对？好？创建完以后，我们开始放手更改超时接口了。这个超时接口先拿谁来动刀子呢？ think client interface 对不对？在这里添加一个空的实现。我们把 say hi copy 一下，但是可不能再叫 say hi 了，千万次你不停地问候。够了，把这个 say hi 改名叫 retryok 然后它的接收参数我们给它添加一个什么呢？叫 request 


parameter 这个代表什么意思呢？他是说我调用你的时候，我传给你一个超时的秒数，那你就按我这个秒数来执行方法，比方说我传给了你 1 那你这个方法就执行一秒传给你 2 那你就执行两秒，就是这么简单。好声明了方法以后转战到 think client 里面，把这个方法写出来实现方法，我们这里竟然要让它按照既定的秒数来执行。


那很简单。 sleep 对不对？非常简单，我就直接 time out 减减，如果它冒的尖尖大于等于0，那你给我睡一秒钟 thread.sleep 1000 毫秒。 Ok. 这里需要把它用 try catch 给引入进来。在最后结尾的地方，我这里要给他打一行 log [log.info](http://log.info/) 证明他已经处理完了，他叫 retry 然后再跟上他的端口 portok 最终 return 一个什么呢？ return 一个当前的服务器的端口。


好，那方法体就是这样实现了。我们这里不妨再给它的 request parameter 指定一个名称，就叫 name 等于 time out 其实如果不指定的话，有些情况下它会以你当前这个变量的名称来默认作为它的 field name 我们这里保持一致，保持编程规范，给他在 service 层里也把这个东西给加上去。


好，那我有了方法实现，接下来就要做方法调用了。 papa 调用在哪里啊？ fin consumer advanced 在 advanced controller 里，我们来一个 retry 的函数，同样也是 copy say hi 打上去以后我们调用谁？我们调用 service 的 retry 然后传入一个秒数，我这里这个秒数也想从外面传入。那怎么办？我给他这里声明一个 long 型的 time out 把它塞入进去。你还不领情吗？还不是 long 是个 int 型。
好吧，好吧，大人不计小人过给你传入一个 int 的 time out 然后把 mapping 改成 retry 改完以后是不是就可以启动项目了？我们都启动谁呢？这里可要启动的项目多一点了，先把尤瑞卡 server 给它启动起来。紧接着启动谁启动 think client 启动几个，当然是启动三个了，因为为什么我们要测试不同节点的重试对不对？所以它要启动多个节点，这样方便看到效果。启动完第一个，我们要把它的端口给它改一下，改成 40,003 再启动。第二个，启动完再把它的端口改一下，改成 40,004 再启动。


第三个，幸亏老师这个电脑性能好，当年是 17 年的顶配麦克。但是我如果想把整个微服务全套 20 多个包全跑起来，真的是非常非常的困难。所以同学们如果在本地跑不起所有的包，没关系的，大家分模块来跑，吃透一个模块和吃透整个项目。其实是一样的。很多同学本地用的可能是 8g 的电脑。如果是 Windows 的同学，我建议大家可以去尝试着加一些内存条，至少把它打到 16g 如果大家是买的游戏本，那就随意发挥，游戏本的性能都非常好。 OK 我还要启动最后一个项目是谁服务的调用者 fin consumer advanced 对不对？在启动它之前，我们先来回顾一下配置，这里配置了每台机器最大重试次数是2，再加上其中第一次是正常调用，那么他每台机器上会调用几次呢？三次对不对？当他在第一台机器上调用了三次依然超时，那么它可以换几台机器再重试呢？两台机器，也就是说它总共可以在三台机器上，每台机器上调用三次请求。 OK 那么我们现在就把它的闷方法给它启动起来。启动完成以后，到 postman 里进行一次调用，看一看它是否能在不同的节点上发起重试，好启动完成转战 postman 那我们这里调用 local host 。


40,001 的端口就是 fin consumer advanced 这个项目的端口，它是一个 get 方法，发送到 retry 这个 method 里，并且它的 time out 是几是零，我不想让它有任何延迟。那我们先调用一次。好，你看已经正常返回了40,004。


OK 我们接下来看一下 log 这台 40,004 的机器接收到了一个请求，它有没有重试呢？没有重试，剩下两台机器没有接到任何重试请求，说明我现在的这个 request 并没有触发它的超时判定对不对？好，我们把 log 清掉，再把时间改长一点。这不是零秒吗？我看你三秒还能不能坚持得住，三秒一定超时喽。


同学们点击发送，看后台是哪个。不幸的，服务器接收到了第一个请求，这台服务器40,003。又来了一次，超时了三次。那接下来应该到其他服务器了，我们看看接下来是40,004。12334。那剩下一个人就应该是 40,002 了。123。好嘞，那在超时的情况下，我们每台服务器都接收到了三次不同的请求实验结果与配置项完美重合，实验成功。


OK 同学们，那我们这一节的 demo 部分就到这里结束了。大家如果对这个超时计算的公式还把玩不清楚，觉得非常的困惑。那怎么办呢？打开图文教程，在里面有详细的方程式，教大家怎么来计算这个超时判定。 OK 同学们学了一个份的超时计算，可不要先沾沾自喜了，我们 spring cloud 组件库可不止一个 phone 可以控制超时。接下来的 high streaks 也有超时判定，并且它可能会跟你的 fin 超时判定有所冲突。在后面一个 high strikes 章节，我还会教大家如何调整配置，让 high streaks 的超时和 ribbon 的超时可以和谐共处。那么今天的课程就先讲到这里了，下一小节带大家品味一些不一样的歌调，看看 thin 的 contract 也就是协议层是如何来解析的。好同学们，我们下期再见。





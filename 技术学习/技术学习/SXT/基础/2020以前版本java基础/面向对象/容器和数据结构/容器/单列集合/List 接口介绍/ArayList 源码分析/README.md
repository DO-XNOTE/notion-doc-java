---
title: ArayList 源码分析
---

# ArayList 源码分析

```java
3.413 ArayList 源码分析
3.413.1 ArayList 底层存储方式
ArayList 底层是用数组实现的存储。 /**
*Default initial capacity. /+
private static final int DEFAULT CAPACITY = 10; /**
*The array buffer into which the elements of the ArrayList are stored. /**
*The array buffer into which the elements of the ArrayList are stored.
*The capacity of the ArrayList is the length of this array buffer. Any
* empty ArrayList with elementData =m DEFAULTCAPACITY_EMPTY_ELEMENTDATA
*will be expanded to DEFAULT_CAPACITY when the first element is added.
*/
transient Object[] elementData;// non-private to simplify nested class access
/**
* The size of the ArrayList (the number of elements it contains). -
* @serial */+
private int size; 3.413.2初始容量
*DefauIt initial capacity. /
private static final int DEFAULT_CAPACITY =10; 3.413．添加元素
*Appends the specified element to the end of this list.
* @param e element to be appended to this list.
* @return <tt>true</tt> (as specified by (@link Collection#add)) public boolean add(E e){
ensureCapacityInternal(size+1); // Increments modCount!! elementData[size++]=e;
return true; }
/**
*This helper method split out from add(E) to keep method
* bytecode size under 35 (the -XX:MaxInlineSize default value),
*which helps when add(E) is called in a C1-compiled loop.
*/
private void add(E e, Object[] elementData, int s) ( 
     if (s ==elementData.length)
               elementData =grow(); elementData[s]=e; size=s+1; 
   {
3.413.4数组扩容 
／／容量检查
private void ensureCapacityInternal(int minCapacity) { 
   ensureExplicitCapacity(calculateCapacity(elementData, minCapacity));
(
／／容量确认
private void ensureExplicitCapacity(int minCapacity)( modCount++;
// 判断是否需要扩容，数组中的元素个数—数组长度，如果大于。表明需要扩容 
if (minCapacity - elementData.length > 0) {
     grow (minCapacity); 
}
/**
* Increases the capacity to ensure that it can hold at least the
* number of elements specified by the minimum capacity argument.
*
* @param minCapacity the desired minimum capacity
*/
private void grow(int minCapacity) ( // overflow-conscious code
int o1dCapacity =elementData.length; ／／扩容1.5倍
int newCapacity = oldCapacity + (oldCapacity>> 1); if (newCapacity - minCapacity < 0)
newCapacity =minCapacity;
if (newCapacity - MAX ARRAY_SIZE > 0)
newCapacity = hugeCapacity(minCapacity);
//mincapacity is usually close to size, so this is a win: 
elementData = Arrays.copyOf(elementData, newCapacity);
```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/3d6b7fab-8830-4c78-80b8-3c3631af59b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466V4WCY7OK%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232708Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDD%2BjQMFVcjMJvoKVm8LOsziFhvM7FKdG6SL3furBLZTAIhAIAQkc9LJaasM1Bk8Is0QMIM58qkRo3ZT8sl6jii5znqKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxtWQ2MccpivuAJ484q3AMqIRU4B41gilDKJd6RkzQlhjgqnhD9Z1ufrA8OYdfM1w4X%2BfFfh5V%2FLR62hWwnwZa4oKAUw3MdZqIh%2F%2BprkErXCLQ2kbZReS%2FMoaYDaAvJZDNsy48r9oZGIjT6ja4kGtSD6boQaeDpi23HpB47NHada%2FLut%2BrVHODZIdzBh5ZNgP%2FXCDIV8qU0EkcXT2oU%2F%2FX25ZNtWINTPqxnJc4ObCGVJ0tC%2BJI1JMoozIGuZuUIrrRyh8MXPiVTsuvBHZNNy7Qx6BCKE%2FMlcj5f9xmX2mMWpCFiiyOXytg%2F1KR5pzsn56C4cmv4KHrJIp%2FWz%2BrQFNNwj6NYHB%2Brh0k5mnjUVvp2%2B5HTuQXKkC52xM2b%2B%2BSXNdo8tbd41fEYqq%2B2DVnzkXN6G2JOMUyEUsS9S3cUjYUnTCpLh5HjWZH4G4FzCeH5VMQP6crFzumBZrSuzbITMRyUStmXRj8MVrL21U1gOJjl3TTdSgtpOzVO8MPbfpkUB0GqKK5GTq4qV2gNVb4HOAS%2FQ8vbQMLLKEGBZsXn5BjjzP6cfJ4wPlaMzlST%2FW8D%2FpuE6zG%2FjhkWf9BxfNt8jNQ%2BOqG4OzK%2FJpWKXAVqkXKZzHr5jaSvVsZHBpfoXsHcqPx4%2BmMh%2BYuIq9zXmTCtuv%2FSBjqkAbIPa58D9UbGGYB1w1uluGa%2FbU%2BZKqkKCzhtwW35RZ4FF6ZfSmHdn%2Bv5NypRS8hdOKNguNi71lwwq5mcKcVwvP8SyvH5hWVRyTDsUL6cOfk6%2FrLdDoNAp5Ixx%2BfgyUSzcjRNCCd3vMXtL%2F%2F9il36RqEtlihhc5sBXsRgukk8e1lHcHRBtHyuKg%2FKJptTUenL%2FPnolapKnWhkiHUkQiQu9Dfj%2Fmsg&X-Amz-Signature=c0bf6179a34e272fb61122bc9715219be45d00908a528f4511faa1656babb96a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



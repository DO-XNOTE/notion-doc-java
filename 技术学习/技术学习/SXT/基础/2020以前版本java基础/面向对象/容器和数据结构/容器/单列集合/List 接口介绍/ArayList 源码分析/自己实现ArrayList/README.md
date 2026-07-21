---
title: 自己实现ArrayList
---

# 自己实现ArrayList

```java
package cn.bjsxt.colletion.arraylist; 
／**
  ＊＠描述：自己实现一个ArrayList，帮助更好的理解ArrayList类底 层实现
  */
public class SxtArrayList /*implements List*/ {
＊核心数是数组，仿造源码来写
*new ArrayList0
*/
private transient Object[ elementData; private int size;
／／初始化值容量传入的值的判断
public SxtArrayList(int initialCapacity){ if(initialCapacity<0){
}새
throw new lllegalArgumentException("Illegal Capacity:"+initialCapacity);
)catch (Exception e) { e.printStackTrace(): {
elementData = new Object[initialCapacity]: {
／／初始化容量
public SxtArrayList0{ this.size=10;
{
／／元素对象的个数 public int size({ return size; {
／／集合是否是空的
public boolean isEmpty 0{ if (elementData.length<=0){ return false;
{
return true; {
／／获取集合中的元素
public Object get(int index){ rangeChect(index);
/**if (index< 0 || index>=size){ try{
new Exception0: }catch(Exception e){ e.pr
.printStackTrace(: }
}*/
return elementData[index]; ／／删除指定位置的一个对象
public voi
id remove(int index){ rangeChect(index):
／／abcd位置，删除后，后面的元素位置都往前移动一个int numMoved = size - index - 1
if(numMoved>0){
System.arraycopy(elementData,index + 1, elementData, index,numMoved);
}
elementData[--size]= null;/** clear to let GC do its work 垃圾回收＊／
}
／＊＊重载删除方法，容器里面和这个相同的对象删除＊／public void remove(Object obj) {
for(int i=0;i<size;i++){
if（get（i）.equals（obj））｛／＊＊注意：底层调用的是equals方 法，而不是＝＝＊／
remove(i); }
} }
／＊＊set方法＊／
public Object set(int index,Object obj) {
／＊＊设置一个新得值，返回设置之前的那个老的值＊／／／索引判断
rangeChect(index): Object oldValue
ue=elementData[index]; elementData[index]= obj;
／／返回老的值 return oldValue; {
／＊＊集合中指定位置添加元素对象＊／
public void add (int index,Object obj) { rangeChect(index);
／＊＊数组扩容和数据拷贝＊／ensureCapacity0:
／／指定位置当前元素和后面的全部元素往后面移动System.arraycopy(element
index+1,size-index):
elementData[index] = obj; size++;
}
／＊＊向集合中中添加元素＊／public void add(Object obj) (
／＊＊数组扩容 和拷贝＊／
if(size ==elementData.length){
／＊＊扩容实际上就搞得大的框，才够装，两倍扩容＊／Object[]newArry=new Object[size*2+1]; ／＊＊拷贝＊／
System.arraycopy(elementData, 0, newArry,0, elementData.length):
／苏
／／循环的方式进行赋值也行
for (inti=0;i<=elementData.length;i++){ newArry[i]=elementData[i];}
*/
elementData=new/Arry: {
elementData[size++]=obj: //
size＋＋；都一样的}
／＊＊范围的检查＊／private
if(index <0||index>=size){ try{
throw new Exception0: }catch (Exception e) {
e.printStackTrace():
private void ensureCapacity0 {
／＊＊数组扩容和拷贝＊／
if(size ==elementData.length){
／＊＊扩容实际上就搞得大的框，才够装，两倍扩容＊／Object[] newArry=new Object[size*2+1]; ／＊＊ 拷贝＊／
System.arraycopy(elementData,0, newArry, 0, elementData.length);
/**
／／循环的方式进行赋值也行
for (int i =0;i<= elementData.length;i++){ newArry/[i]=elementData[i];}
*/
elementData=newArry;
public static void main(Stringl args){ SxtArrayList list =new SxtArrayList(3); list.add("333");
list.add("444"); list.add("555"); list.add("666"); list.add("777"); list.add("88");
System.out.println(list.size); System.out.println(list.isEmpty0); System.out.printin(list.get(5));
```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/a90a7268-ef79-478e-8d03-321b9c857698/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X3BN4432%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232708Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBIiC26C8OfkS8q1LVsv9Nlp5i7F9tyrgR7LP7Op9wcdAiByAQcQ4zrSqKvBTpEvHzVK33PoTsNB9FxRXerkXB4hSiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrvnbuo3eiH8eux2yKtwD2pUI%2FWTOGF0RVQqUlHl6rrezjb4uaFh1P%2FjtFmIgBf1jZtADIy96lQiY5lHR9eBXagRZZha0bwhZe9c3MOh2Z1%2BOz3wwiR3Cs%2BptUVcb0xlv6%2FoM5uxyCM2sPndudp3c3HuTsPh20puVSDnhQi%2Be2cjNLcP23xqPJL%2FplYmGWKj8P3TESRcthHYy1JpZbD2O6F5PU2kivqjGGlHXez9N2f7%2Bq52sggNoo24ivG0yZKz2Cbmd7phtCfdkr0U%2FMMTEORG5aHIJah%2FOcuPHdk8knFtTNvr2OTCQaX%2Fcs3fxgb0Dokoo6PAhwbNdr%2BkVHtWi5J2CMV3st3OXzKAKJRLyvTFjwRTmI%2FvkOa1sx%2FlXrqvg4KS5wygaYtEEskZvoJKP7AiZlDFY8Bn8gBTnDoMASSSTYDhGQEHQgefl4Od8VR1vHTRRftDr72hI3wo7gUbWlxo1y5yXJJVDXRYDjo%2BPjgebsIYV4JWTxmqdwDGlI0LZpjwoWHxbi%2FZZfx4UorJ%2Bk9qbDrkV4p1pL7HxAhf0EQUTphsZ6pRT9aQX0%2BikZ32e9TvjRmDLc%2FlssR7yXi6QSbsP8WE9OgkWvUB%2FyjzOJj8SLltkz%2Bhupal%2FFCwRXlUIKB5LbAht9ZIgNbow8rr%2F0gY6pgG1mqCsQGuyn%2Fi%2FgYFzIfjoGZTNyvbNgM%2F2M10GmR0ZdZMgMpBl1oZyGMw%2FKRu%2FBwvj4gLi80IAHeLtPP44t2BrLNdTeg55MLR6%2BQxFmJaE5RClDZ%2Bd3S9z6q%2BrTVdaLQA5lGjGIXgKlBx8SQkQGiY9JBIoQdjeqmRlOz3dbwHSC7hu%2BfWipWbSCIBluOM4ZbIgZEP9UKRqNacqjHFHMYpcYlVtpIdV&X-Amz-Signature=22a9473dac55f17fd517b21d040b3dd1cda691144605c62e0889d11761f3feb8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



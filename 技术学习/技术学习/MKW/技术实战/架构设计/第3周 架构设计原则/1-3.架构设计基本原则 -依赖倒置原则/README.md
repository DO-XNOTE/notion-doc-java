---
title: 1-3.架构设计基本原则 -依赖倒置原则
---

# 1-3.架构设计基本原则 -依赖倒置原则

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/2db4a15e-f99d-4427-bb1c-59d37bb14892/SCR-20240808-pbnz.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPX3YAKE%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230354Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDpcMvuwp49PhrVObgfuIrXIl2SpFtNGmCnabK45G792QIgS0SnY0zcxIsDfX9kDc%2FrJvop3l6493WzXej83A%2FtoIYqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPSJfqPuEqZxP%2B3MoyrcA70uBngSMYwh3U3fSQRkxlvXehxVF%2BCxr%2FTEfPM0FGX2QdnbCzKpzR7zA6tQW6zt6ppLXu%2B3hadH13FWHrqVjHe2BR4h%2FPlFdws0kQvURedvzsqUUbI0RyYDMJwlsEZIeBLIFetTN4cpkDuoqNbZzswlZ2nKkHMggOWxvZvpfNMlAay4Hogf9xzp4%2FlzCsCb6e7Fdyf4I8wcXsjp%2FLfyewRrQkSh0%2ByYucMghNrKAg2TVFKQnVj%2FvoL7mFUapZ7juIaWLQU0OsV48d7uSmxmSpKkRzsL1CO3WZ0tcJongmQNfu3c54W7fqzXJVjhsf%2FPFtCppFdqJpNblyL2b8r2F64Xmy%2Bz1SJWayKscgjXncMzskZB8x%2FnzphV3yQbg3xH7YDdCepXUL6Vf8SAOWx7VimyqJDNXNP2jhm4IljOW3VXPY0KeMJFARtZKg1zSDgqTkcqkDrjMGuFiSt5wO3ugAXnQa%2B%2F3CsawPbftErQIuXKs2cYiyk4Y0W9T19ltFTKpNSIzKkNgeLtpMcsvVFBzVAKUZG84Ew9GT8RuEAV8Lp42kS2HxX5IG5ysW4YsZ6s72yCO11K83Z3XfqYmZF99NodOJbYq0q9bEFW1RQSgJEEsubunsDZwWQO6ZYTMMW5%2F9IGOqUBpeq1gFKY3E9Q7mYhTOHLdhgX5h1fN5fJGP%2BVeUzJ4Wcuu9tl3l9VOyUv5ucAMyXbO2WNtRyhQlwNRupCE0%2B4EZhvxQbLzT6vb6kb3lSbEratkdGGT5BwHGjRetU5tqa0D10WwIA%2FRrjxM2p6LJOAl22RL4yPjHTM2Ovhu%2BB7ZAAZ69zGdwqZVB%2FXR6%2BIQ1CkGPITXhllnto6aMKqz%2FwV3r3C7O1b&X-Amz-Signature=6854dafcbe2a81b710f7529606f01677b5d8e16846ff567b153b50c686554e8e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

1-3架构设计基本原则-依赖倒置原则
这一节我们来重新认识一个老朋友，那就是依赖倒置原则，相信同学们对它熟悉得不能再熟悉了，从出道至今就被各路面试官问“讲一讲Spring的依赖倒置”，那同学们真的理解什么是依赖倒置吗？如何将依赖倒置的理念应用在微观代码架构层面呢？这一节我们就重新会一会这个老朋友。
**依赖倒置**
衣赖倒置原则有两个核心用锅思想

.上层模块不依赖底层模块的实现，而应该对底层模块做抽象

·抽象不应该依赖于底层细节，而细节应该依赖于抽象

咱就拿组装电脑的例子来说，如何应用上面这两条逻辑。我们把电脑屏幕作为最“上层的模块，在它之下有主板，主板再往下有CPU、显卡、内存条。那么按照我们的常识来说，处于上层的显示器需要依赖于下层模块主板吗？如果主板换了，难道显示器也要跟随着一并换掉吗？当然不需要咯。


同学们思考这样一个问题，应该怎么做才能让显示器、主板、显卡内存这一条上下游链路玩得转，使上层模块脱离底层模块的束缚？这便是第二个“抽象原则里讲到的方法，由上层模块定义抽象接口，下游模块依赖于这个抽象来做适配。比如这样，我的显示器定义了一套串行外设接口（抽象层），而主板（底层细节）依赖于这个抽象层来适配上层应用。这样即便更换了主板，我们也并不需要对显示器做任何变更


体现在我们的软件设计层面，上层模块通过定义抽象接口对底层组件的访问进行约定，底层组件依赖于抽象接口实现细节，这个设计理念在JDK和Spring里随处可见。鉴于IT行业找对象比较难，老师这里将依赖倒置原则应用在相亲的过程里跟同学们看一下，一个抢手的架构师该如何应对疯狂追求的女嘉宾

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e7383cf8-d6bd-4aff-b3f2-a7caedae2b8c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPX3YAKE%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230354Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDpcMvuwp49PhrVObgfuIrXIl2SpFtNGmCnabK45G792QIgS0SnY0zcxIsDfX9kDc%2FrJvop3l6493WzXej83A%2FtoIYqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPSJfqPuEqZxP%2B3MoyrcA70uBngSMYwh3U3fSQRkxlvXehxVF%2BCxr%2FTEfPM0FGX2QdnbCzKpzR7zA6tQW6zt6ppLXu%2B3hadH13FWHrqVjHe2BR4h%2FPlFdws0kQvURedvzsqUUbI0RyYDMJwlsEZIeBLIFetTN4cpkDuoqNbZzswlZ2nKkHMggOWxvZvpfNMlAay4Hogf9xzp4%2FlzCsCb6e7Fdyf4I8wcXsjp%2FLfyewRrQkSh0%2ByYucMghNrKAg2TVFKQnVj%2FvoL7mFUapZ7juIaWLQU0OsV48d7uSmxmSpKkRzsL1CO3WZ0tcJongmQNfu3c54W7fqzXJVjhsf%2FPFtCppFdqJpNblyL2b8r2F64Xmy%2Bz1SJWayKscgjXncMzskZB8x%2FnzphV3yQbg3xH7YDdCepXUL6Vf8SAOWx7VimyqJDNXNP2jhm4IljOW3VXPY0KeMJFARtZKg1zSDgqTkcqkDrjMGuFiSt5wO3ugAXnQa%2B%2F3CsawPbftErQIuXKs2cYiyk4Y0W9T19ltFTKpNSIzKkNgeLtpMcsvVFBzVAKUZG84Ew9GT8RuEAV8Lp42kS2HxX5IG5ysW4YsZ6s72yCO11K83Z3XfqYmZF99NodOJbYq0q9bEFW1RQSgJEEsubunsDZwWQO6ZYTMMW5%2F9IGOqUBpeq1gFKY3E9Q7mYhTOHLdhgX5h1fN5fJGP%2BVeUzJ4Wcuu9tl3l9VOyUv5ucAMyXbO2WNtRyhQlwNRupCE0%2B4EZhvxQbLzT6vb6kb3lSbEratkdGGT5BwHGjRetU5tqa0D10WwIA%2FRrjxM2p6LJOAl22RL4yPjHTM2Ovhu%2BB7ZAAZ69zGdwqZVB%2FXR6%2BIQ1CkGPITXhllnto6aMKqz%2FwV3r3C7O1b&X-Amz-Signature=6d825a644ac2a5bad08bf1e8b6a1f7ab801e5fd222b9ed9ebd3a6f7d298c9a35&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```java
public class Architect{

		IGir1 gir1:
		
		public void play(){ 
       gir1.talk(); 
    }

}

public interface IGir1{ 

    void talk(); 

 }
```


这里我定义了一个架构师类，作为上层模块，架构师要相亲，我们假设这是一个蚂蚁金服的架构师，借着蚂蚁上市身价已经达到了一个小目标，各种各样的女嘉宾都来求包养。但是架构师并不迁就底层对象，他定义了-个抽象层叫IGirl


```java
public class YuJie implements IGir1 { 
      
      public void talk(){
			System．out．print1n（“大王，鞭挞我吧！”）； 
			}
			
}

public class LuoLi implements IGir1 { 
      
      public void talk(){
			System．out．print1n（“小哥哥，打架吗？”）； 
			}

}
```


来了两位女嘉宾，分别是御姐和萝莉，她们都依赖于抽象接口实现各自特殊的对话，对于架构师来说并不需要关注底层的女嘉宾是什么来历，统统来者不拒全盘接收，底层的改变并不会影响到上层应用

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/00654eb2-0acd-42c0-96f4-8ae3c0003793/1-3.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RPX3YAKE%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230354Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQDpcMvuwp49PhrVObgfuIrXIl2SpFtNGmCnabK45G792QIgS0SnY0zcxIsDfX9kDc%2FrJvop3l6493WzXej83A%2FtoIYqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDPSJfqPuEqZxP%2B3MoyrcA70uBngSMYwh3U3fSQRkxlvXehxVF%2BCxr%2FTEfPM0FGX2QdnbCzKpzR7zA6tQW6zt6ppLXu%2B3hadH13FWHrqVjHe2BR4h%2FPlFdws0kQvURedvzsqUUbI0RyYDMJwlsEZIeBLIFetTN4cpkDuoqNbZzswlZ2nKkHMggOWxvZvpfNMlAay4Hogf9xzp4%2FlzCsCb6e7Fdyf4I8wcXsjp%2FLfyewRrQkSh0%2ByYucMghNrKAg2TVFKQnVj%2FvoL7mFUapZ7juIaWLQU0OsV48d7uSmxmSpKkRzsL1CO3WZ0tcJongmQNfu3c54W7fqzXJVjhsf%2FPFtCppFdqJpNblyL2b8r2F64Xmy%2Bz1SJWayKscgjXncMzskZB8x%2FnzphV3yQbg3xH7YDdCepXUL6Vf8SAOWx7VimyqJDNXNP2jhm4IljOW3VXPY0KeMJFARtZKg1zSDgqTkcqkDrjMGuFiSt5wO3ugAXnQa%2B%2F3CsawPbftErQIuXKs2cYiyk4Y0W9T19ltFTKpNSIzKkNgeLtpMcsvVFBzVAKUZG84Ew9GT8RuEAV8Lp42kS2HxX5IG5ysW4YsZ6s72yCO11K83Z3XfqYmZF99NodOJbYq0q9bEFW1RQSgJEEsubunsDZwWQO6ZYTMMW5%2F9IGOqUBpeq1gFKY3E9Q7mYhTOHLdhgX5h1fN5fJGP%2BVeUzJ4Wcuu9tl3l9VOyUv5ucAMyXbO2WNtRyhQlwNRupCE0%2B4EZhvxQbLzT6vb6kb3lSbEratkdGGT5BwHGjRetU5tqa0D10WwIA%2FRrjxM2p6LJOAl22RL4yPjHTM2Ovhu%2BB7ZAAZ69zGdwqZVB%2FXR6%2BIQ1CkGPITXhllnto6aMKqz%2FwV3r3C7O1b&X-Amz-Signature=b939a34b17bbd135b0df066f920c70f493e0736b55e9ea1262b14120f929470b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



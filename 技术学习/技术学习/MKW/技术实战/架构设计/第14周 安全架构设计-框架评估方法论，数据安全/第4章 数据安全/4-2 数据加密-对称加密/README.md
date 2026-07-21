---
title: 4-2 数据加密-对称加密
---

# 4-2 数据加密-对称加密

架起需求到落地的桥梁，构建 it 新蓝图。我是张飞扬，上一节我们聊了聊数据安全的总体概括、分层以及访问控制。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/91244893-fad0-403f-90af-07dcb01b2f49/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MUPL2LF%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231017Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDRsyhU%2Bd0l5QRVwW45cHI%2BsfX4U4aL646pqW8t0tKAGAIhAMmFJEancHyjQHtTJpmwTzHqr4XUVD%2F3OBa%2FlVcE5rZoKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyR31BooB%2FiyTAH7%2BQq3APRfV1jDRu4JVuuUwSsGRt9Yn3QIXdl2vXimj5hnwXGW%2Fu2bthJpIOV3H4oaXX71u%2FWvxOQk3hBH2EzD%2Fe2Zdhb17nNzMn70ox%2BI0ouP8Wqk3xhM0%2Fg%2Bs4z29%2B%2FwDbLx%2BJIuBnW5kNs6JvTPlcy5iB%2BZVpTyqizCRgEaJ4NH5yRK%2BLCJBcKsazZ7axrlgyzQFIEJ%2Buhv4amtYXN7VoCNJ1NxfO2XC5uYrlnU4ckcQ6dHFCfijrsjVjW8shqF2YE7IaRrL%2FPsT%2BrJbZoZ4B%2BCkpHOoNI09K3uU5459%2B6m5%2FVagm%2FY4hK%2B0poa1aBkozTXPwmMpH6NiYJhlXVAbphJrHqoGER%2Fhd7UNP3xP3vA3viq4YswO1eSXZ3YpBbxDwWrTiGtGFUYt1p7UK84G2syqUKDKYokgq1jAkiA%2Ft%2BGxX3ZpHcnBY1gOAexbIzg2LesnfoEej%2FtbhBozxxpS6X9pvtaG%2FJKdUpYAo9SZQGWwcpIz5rlceQ3yCVRMywbQ3Ph46XSOUhxdeNaNZ2KY7RBfAkqL2hlsrRsTa3PCqxQAX5mLVo28wGak6xnBVeRbyJKL4JWNC%2BvzhGwWIaByjBfITW0LJDiUqoI%2F%2BY%2F3GSq%2FG3VoH9OnrQIhzA4NpIuzD8t%2F%2FSBjqkASyijuPkhsplpo9NGRKWf25%2FrELaYwNNYepoFsxXnbEt%2FzYV6Vl57rLrKavD5m8x%2B%2FO9rD8MGpQAuJ%2FpELhxIpr%2F%2BiFbxk%2BR%2BPZ5a32KDbJ8mCCZP4om1DTlbRIRhemJ850OtS2cTsH4KBksjlRNui7Ti9V01CnjO8OOXxosWuJHbpe%2BnCOL6sNuApTXeftWlHW%2FgBWog1o7kBQ8OlwVo2aPW6HH&X-Amz-Signature=efca8a7df505c7343cad87de88a691c599b5189851cd45908f53c8dd855893d7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那这一节我们来看一看密码学的第一章，数据加密中的对称加密。好，其实密码学说复杂很复杂的，我们大学可能读过好几本密码学的书。那说简单也就那么点事儿。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/3530a3e2-b8f5-418d-b8e8-226389159347/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MUPL2LF%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231017Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDRsyhU%2Bd0l5QRVwW45cHI%2BsfX4U4aL646pqW8t0tKAGAIhAMmFJEancHyjQHtTJpmwTzHqr4XUVD%2F3OBa%2FlVcE5rZoKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyR31BooB%2FiyTAH7%2BQq3APRfV1jDRu4JVuuUwSsGRt9Yn3QIXdl2vXimj5hnwXGW%2Fu2bthJpIOV3H4oaXX71u%2FWvxOQk3hBH2EzD%2Fe2Zdhb17nNzMn70ox%2BI0ouP8Wqk3xhM0%2Fg%2Bs4z29%2B%2FwDbLx%2BJIuBnW5kNs6JvTPlcy5iB%2BZVpTyqizCRgEaJ4NH5yRK%2BLCJBcKsazZ7axrlgyzQFIEJ%2Buhv4amtYXN7VoCNJ1NxfO2XC5uYrlnU4ckcQ6dHFCfijrsjVjW8shqF2YE7IaRrL%2FPsT%2BrJbZoZ4B%2BCkpHOoNI09K3uU5459%2B6m5%2FVagm%2FY4hK%2B0poa1aBkozTXPwmMpH6NiYJhlXVAbphJrHqoGER%2Fhd7UNP3xP3vA3viq4YswO1eSXZ3YpBbxDwWrTiGtGFUYt1p7UK84G2syqUKDKYokgq1jAkiA%2Ft%2BGxX3ZpHcnBY1gOAexbIzg2LesnfoEej%2FtbhBozxxpS6X9pvtaG%2FJKdUpYAo9SZQGWwcpIz5rlceQ3yCVRMywbQ3Ph46XSOUhxdeNaNZ2KY7RBfAkqL2hlsrRsTa3PCqxQAX5mLVo28wGak6xnBVeRbyJKL4JWNC%2BvzhGwWIaByjBfITW0LJDiUqoI%2F%2BY%2F3GSq%2FG3VoH9OnrQIhzA4NpIuzD8t%2F%2FSBjqkASyijuPkhsplpo9NGRKWf25%2FrELaYwNNYepoFsxXnbEt%2FzYV6Vl57rLrKavD5m8x%2B%2FO9rD8MGpQAuJ%2FpELhxIpr%2F%2BiFbxk%2BR%2BPZ5a32KDbJ8mCCZP4om1DTlbRIRhemJ850OtS2cTsH4KBksjlRNui7Ti9V01CnjO8OOXxosWuJHbpe%2BnCOL6sNuApTXeftWlHW%2FgBWog1o7kBQ8OlwVo2aPW6HH&X-Amz-Signature=2ea08c94e7ecbc075f9192ef08a80bb6df97361cad0622e0642d874057350ed7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

密码学在飞扬老师的这个词典里，就相当于赌场学，你要学密码就要会玩赌术，密码学第一定律的脑乱心智，通过怎样的扰乱心智呢？当我拿到一张Q2、张 k 的时候，我想到的第一件是什么？我说打出去，然后是什么？出老千，把 q 变成k，这样，我三张k，不管是三张大牌还是什么，再加一对，变成什么俘虏，或者是再加一个k，再变成王炸都有可能了，所以扰乱的第一件事情就是换牌，是吧？那第二件是什么？密码学第二件大事就是扩散。当我碰到像是周润发以的赌神来进行赌的时候，我一个色子是没法什么让他听不出我的这个最后落地的这个上面的牌面怎么办呢？我弄 5 个色子，然后在里面转转，混乱，它让声音混乱起来，让他无法听出最后落地的时候什么，到底里面是什么样的点数朝上。


这就是扩散，让骰子和骰子之间碰撞、移动交换，还是什么增加复杂度？还有最后一个关键问题就是初始向量，所谓初始向量就是增加随机数，比如经典的就是什么掷色子，掷色子什么决定谁先开牌，是吧？掷色子决定什么谁先发牌，那这种掷色子其实也是增加了一些复杂度和混乱度，那这个色子可正可反对吧？可一可二，可三可四，这个初始向量随机指数完全什么硬随机，大家没法知道老天的眷顾，那这种就是密码学的三定律，混乱、扩散和初始化，通过这三种方法来完成不同的对称密钥、非对称密钥，各种各样的加密技术，我们来看一看在对称加密里面，传统的加密树是怎样通过这三个技术或者这三个思维来实现的，其中的第一个具体实现就是替换了，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/310fb23d-34e6-4a99-b159-9c8cac48fe3f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MUPL2LF%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231017Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDRsyhU%2Bd0l5QRVwW45cHI%2BsfX4U4aL646pqW8t0tKAGAIhAMmFJEancHyjQHtTJpmwTzHqr4XUVD%2F3OBa%2FlVcE5rZoKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyR31BooB%2FiyTAH7%2BQq3APRfV1jDRu4JVuuUwSsGRt9Yn3QIXdl2vXimj5hnwXGW%2Fu2bthJpIOV3H4oaXX71u%2FWvxOQk3hBH2EzD%2Fe2Zdhb17nNzMn70ox%2BI0ouP8Wqk3xhM0%2Fg%2Bs4z29%2B%2FwDbLx%2BJIuBnW5kNs6JvTPlcy5iB%2BZVpTyqizCRgEaJ4NH5yRK%2BLCJBcKsazZ7axrlgyzQFIEJ%2Buhv4amtYXN7VoCNJ1NxfO2XC5uYrlnU4ckcQ6dHFCfijrsjVjW8shqF2YE7IaRrL%2FPsT%2BrJbZoZ4B%2BCkpHOoNI09K3uU5459%2B6m5%2FVagm%2FY4hK%2B0poa1aBkozTXPwmMpH6NiYJhlXVAbphJrHqoGER%2Fhd7UNP3xP3vA3viq4YswO1eSXZ3YpBbxDwWrTiGtGFUYt1p7UK84G2syqUKDKYokgq1jAkiA%2Ft%2BGxX3ZpHcnBY1gOAexbIzg2LesnfoEej%2FtbhBozxxpS6X9pvtaG%2FJKdUpYAo9SZQGWwcpIz5rlceQ3yCVRMywbQ3Ph46XSOUhxdeNaNZ2KY7RBfAkqL2hlsrRsTa3PCqxQAX5mLVo28wGak6xnBVeRbyJKL4JWNC%2BvzhGwWIaByjBfITW0LJDiUqoI%2F%2BY%2F3GSq%2FG3VoH9OnrQIhzA4NpIuzD8t%2F%2FSBjqkASyijuPkhsplpo9NGRKWf25%2FrELaYwNNYepoFsxXnbEt%2FzYV6Vl57rLrKavD5m8x%2B%2FO9rD8MGpQAuJ%2FpELhxIpr%2F%2BiFbxk%2BR%2BPZ5a32KDbJ8mCCZP4om1DTlbRIRhemJ850OtS2cTsH4KBksjlRNui7Ti9V01CnjO8OOXxosWuJHbpe%2BnCOL6sNuApTXeftWlHW%2FgBWog1o7kBQ8OlwVo2aPW6HH&X-Amz-Signature=c33fde74d1738ccf05b28cbeb9275d06a02d3fdc3d3e1ec001e68f0746b74c20&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

那怎么替换呢？这里是达芬骑密码那本书里面说到的达芬骑密码桶，不管你是什么数字，我有一套标准规律，对吧？这个数字一旦什么在我的这个密码桶里设定好以后，我按照我标准规律，上转三圈、下转三圈，上三下三、上四下四、上五下五，这样就把 6 个什么圈都转完，转完以后最终出现的结果就是我们密码学的什么密文了？以前面输入的结果叫铭文，我最终出错的结果叫幂文，中间的转圈就是算法其实实现了什么是一个字符跟另外一个字符之间的替代，还有比较经典的就是我们中国的，对吧？我们的老祖先发明了什么四角字典法，一个字根据四角的特征变成四个阿拉伯数字，这是个数字就能唯一确定这个字，诶？这也是一种替代，那这个替代的密码的算法，有个算法本就是这个四角字典查字表，那除了这种老祖先发明的密码学以外，还有一位什么我们的女科学家，对吧？他发明了第一个什么打字机，但他发明的时候他把字的顺序全混乱了，这个思路也用在了密码学里，叫做换位思路。


假设我有一个篇文章，这个文章我拿到以后，我提取出前面的 26 个字符，然后依次在这个打字机上面贴上去。比如第一个字符贴在 q 上，第二个字符贴在 w 上，贴完以后，然后我密文怎么样？我密文是把 a 上面那个字符拿出来作为第一个字符， b 上那个字符拿出来作为第二个字符，通过这种方法就自动的，是吧？把我原来的 26 个字符进行排序，这个排序用一套密码学的标准套路排，排完以后出来的字符就非常混乱了，这也是一种加密手段，如果替代和换位都用在密码学里面了，其实会碰到一个难点。什么难点？左边的达芬奇密码桶只能适合 6 个字符的加密。


右边的这个打字机换位机只能是和 26 个字符的加密，但我一篇文章可能几k，对吧？一个文件可能几兆，一个视频可能几g，怎么样实现真正的加密呢？这就引入了第三个套路，分组，假设我是 128 分组，就是我不管你是 1G 还是一兆还是1K，我都以前 128 个字符进行一个密码学的处理。可能是替换，也可能是替代，也可能是换位，然后我再拿下一个 128 个字符进行替代换位，这样的多组处理完以后，最后合并成一篇完整的密文。


但到底怎么合并，到底怎么处理？谁来说了算？这个来说了算 DES 对称密钥的第一个算法 DES 里面有 5 种具体的分组和处理方法。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/d8cc8cc9-9132-4320-bb2f-248ca62628de/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MUPL2LF%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231017Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDRsyhU%2Bd0l5QRVwW45cHI%2BsfX4U4aL646pqW8t0tKAGAIhAMmFJEancHyjQHtTJpmwTzHqr4XUVD%2F3OBa%2FlVcE5rZoKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyR31BooB%2FiyTAH7%2BQq3APRfV1jDRu4JVuuUwSsGRt9Yn3QIXdl2vXimj5hnwXGW%2Fu2bthJpIOV3H4oaXX71u%2FWvxOQk3hBH2EzD%2Fe2Zdhb17nNzMn70ox%2BI0ouP8Wqk3xhM0%2Fg%2Bs4z29%2B%2FwDbLx%2BJIuBnW5kNs6JvTPlcy5iB%2BZVpTyqizCRgEaJ4NH5yRK%2BLCJBcKsazZ7axrlgyzQFIEJ%2Buhv4amtYXN7VoCNJ1NxfO2XC5uYrlnU4ckcQ6dHFCfijrsjVjW8shqF2YE7IaRrL%2FPsT%2BrJbZoZ4B%2BCkpHOoNI09K3uU5459%2B6m5%2FVagm%2FY4hK%2B0poa1aBkozTXPwmMpH6NiYJhlXVAbphJrHqoGER%2Fhd7UNP3xP3vA3viq4YswO1eSXZ3YpBbxDwWrTiGtGFUYt1p7UK84G2syqUKDKYokgq1jAkiA%2Ft%2BGxX3ZpHcnBY1gOAexbIzg2LesnfoEej%2FtbhBozxxpS6X9pvtaG%2FJKdUpYAo9SZQGWwcpIz5rlceQ3yCVRMywbQ3Ph46XSOUhxdeNaNZ2KY7RBfAkqL2hlsrRsTa3PCqxQAX5mLVo28wGak6xnBVeRbyJKL4JWNC%2BvzhGwWIaByjBfITW0LJDiUqoI%2F%2BY%2F3GSq%2FG3VoH9OnrQIhzA4NpIuzD8t%2F%2FSBjqkASyijuPkhsplpo9NGRKWf25%2FrELaYwNNYepoFsxXnbEt%2FzYV6Vl57rLrKavD5m8x%2B%2FO9rD8MGpQAuJ%2FpELhxIpr%2F%2BiFbxk%2BR%2BPZ5a32KDbJ8mCCZP4om1DTlbRIRhemJ850OtS2cTsH4KBksjlRNui7Ti9V01CnjO8OOXxosWuJHbpe%2BnCOL6sNuApTXeftWlHW%2FgBWog1o7kBQ8OlwVo2aPW6HH&X-Amz-Signature=5dbe52d8c70f8f7f47f038fb2a323bf322ceb7fe06f6e54e72eff310bb68aec5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

但每一组方法里面的本质都是刚刚说什么替代跟换位，我们来看一看，让老司机教大家怎么样开 DES 这把车，它的第一个思路就是什么呀？叫 ECB 电子密码本，这里就是展现了三根车道，对吧？那车是由上往下开，每辆车开的过程当中都是什么标准呢？比如 128 个字符进行一个车道挤进去，挤进去以后进行数据的替代换位，换位完了以后再替代，那替代换位，替代完了以后就把结果输出了，这就是什么分组，然后再替代换位的？标准的 DS 电子密码本 ECB 法。


好，这个方法漂是很漂亮，但是有个很不好的结果。什么不好的结果？黑客来尝试的时候，他只要每次输入同样的内容，你就输出结果总归是一样的，这个时候他可以通过大量的输入不停让你输入，比如说他输个12345，我再输个13546，然后你不停地输出，然后它根据你的输入输出对，来猜你的密码的算法，你的替代和你的换位该怎么样来实现？很容易猜出来，所以 DS 的 ECB 几乎没有真正的实战。


那真正实战最常见的五六年以前基本上都是这个算法， CBC 算法跟 ECB 一开始都一样，唯一区别是什么？是第一个车道的结果，要去抑或第二个车道的明文的输入，然后生成的密文再去什么，抑或第三根车道有什么样的好处呢？那我们来看一下假设输入的铭文是年轻人，那经过加密以后，我们假设变成了天天向上。


嗯，下次又有人输年轻人了，我们就会把年轻人跟替天香上先抑或一下，然后作为这个密码这个桶的输入，那这个桶里面实现什么？替代和换位输出？结果是不讲武德诶，是不是两次输入年轻人结果不一样了？好，我们把第三次输入年轻人，我们就会跟不讲武德，抑或然后重新进行什么替代和换位，最后结果是什么？大家猜出来没有？很经典的耗子尾之是不是诶？每次我们黑客输入的结果输出的密文却不一样，这很难猜了，是不是混乱度增加了？好，这是第二种非常常见的算法，那基于这个算法以上有好几种变种，我们来简单看一下一种变种叫什么？就 CFB 密文反馈，说白了就是因为桶是 128 的那个长度的，所以你每次必须 128 位输入，假设这次我输入了 16 位，怎么办？我要等后面的 100 多位到期才能输出吗？诶，也不是这样哦，我们可以在第一次车道的输出的密文上面进行一个什么，进行一个特殊的处理，这个处理可以把长度跟它的那个结果进行特殊的矫正。


矫正完了以后第二个车道也许可以 16 位进行开车，以 16 位数据，我可以给你个 16 位车道，然后可以跟第一次输出的密文的 16 位的收缩以后的那个内容进行，抑或然后再输出？这是一种变种， CFB 用的很少，所以大家可以忽略 OFB 也是一种变种，这种变种怎么样？你看到跟 CFB 相比只差了一点点，我们来个大家来找茬掺哪里啊？我不是从输出进行什么，进行第二这个车道的输入，而是从中间，是吧？这样有什么好处呢？因为黑客来尝试你的时候，它是可以不停地制造明文。所以它每个明文，它每个密文都有，它可以猜出来，也许你用的是 CFB 方法，那这个时候它就可以自动，它自己可以把上一次的输出的密文跟什么明文进行，抑或这样它就其实知道你每一个管道里面的输入和输出的结果。对了，所以这种情况下有个不好，就是它可以根据上次的密文来猜测我们下一次管道输入的内容。那通过 OFB 把什么把输出的中间内容进行了一个特殊处理以后跟密文进行了解耦，所以第一次输出的密文不会帮助黑客去判断第二次输出的铭文和铭文的处理方法，这也是一个 CBC 的变种，这两个变种用的比较少，所以大家听过且听过好。


第三种变种是用的非常多的，所以一定要这个详细听一听，这就是计数器。所谓计数器是什么呀？是这样的东西，还是三根车车道，三根车道上开的不是车了。是什么？是三只表。这个表是这样的，一开始我们假设这个表上的时间点是十点零五分。好，那这是一串数字，那这个数字通过我们的什么，我们的这个换位，我们的替代，那完成一次我们的密码学的处理，变成密文，然后我们第二个车道上就是什么十点零六分，第三个数字上面跑十点零七分，它那时间一直在往前滚，然后那个数值一直在累加，这个累加的值每次进行加密处理，大家说这不是我的加密的明文，你的，你是处理你的时间跟我明文有什么关系啊？冥婚是不是就那辆车，我们车横过来开计入器，跟前面所有的算法不同的地方，就是车是横开的，车就是什么？就是把它的内容进行跟我们的密文加密过程的数据进行一个，抑或在整个加密处理过程当中，车子负责异火车里面的内容从来没有加密过，加密的永远是计数器的那个时间值，通过这种奇奇特特的方式依然能保证密文没法能反推密文。


我给你一段密文，你是没法反推出我整个处理过程，因为整个处理过程有换位、有替代，还有抑或，而且抑或的内容却是明文。而同时什么每一次开同样的车，年轻人进来的时候结果也不一样，因为第一次年轻人进来的时候，他的抑或的内容是什么？是由 10.05 分的这个数据加密产生的结果，第二次抑或的是由十点零六分的数据加密产生的结果。所以三四年轻人进来还有可能是天天向上，不讲武德和耗资，伟之依然增加了我们什么反解密的难度。所以 CTR 计数器这里埋一个坑，后面马上就会说到是一个非常潮、非常不错的 DS 的加密算法。


好，聊完了， DES 5 大加密算法，大家回过去看，其实说白了就是对于前面的分组，最前面的换位，对于前面的替代的一种什么？一种综合，把三个拳头，把三个拳法合起来变成一套组合拳，那这套组合拳 DS 曾经在十年之前是最知名的我们对称加密的组合拳，但是时过境迁是吧？我们的什么前浪拍在沙滩上了，后浪 a s。出现了 a s。


三五年前最经典的就是 AS 128 CBC 128 大家应该很容易猜到了，就是分组的长度， CBC 就是我刚刚说的年轻人不讲武的，好自为之的这个算法。那 AES 呢？

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/545c399c-fe15-4396-9c69-de63874d72f6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666MUPL2LF%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T231017Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDRsyhU%2Bd0l5QRVwW45cHI%2BsfX4U4aL646pqW8t0tKAGAIhAMmFJEancHyjQHtTJpmwTzHqr4XUVD%2F3OBa%2FlVcE5rZoKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyR31BooB%2FiyTAH7%2BQq3APRfV1jDRu4JVuuUwSsGRt9Yn3QIXdl2vXimj5hnwXGW%2Fu2bthJpIOV3H4oaXX71u%2FWvxOQk3hBH2EzD%2Fe2Zdhb17nNzMn70ox%2BI0ouP8Wqk3xhM0%2Fg%2Bs4z29%2B%2FwDbLx%2BJIuBnW5kNs6JvTPlcy5iB%2BZVpTyqizCRgEaJ4NH5yRK%2BLCJBcKsazZ7axrlgyzQFIEJ%2Buhv4amtYXN7VoCNJ1NxfO2XC5uYrlnU4ckcQ6dHFCfijrsjVjW8shqF2YE7IaRrL%2FPsT%2BrJbZoZ4B%2BCkpHOoNI09K3uU5459%2B6m5%2FVagm%2FY4hK%2B0poa1aBkozTXPwmMpH6NiYJhlXVAbphJrHqoGER%2Fhd7UNP3xP3vA3viq4YswO1eSXZ3YpBbxDwWrTiGtGFUYt1p7UK84G2syqUKDKYokgq1jAkiA%2Ft%2BGxX3ZpHcnBY1gOAexbIzg2LesnfoEej%2FtbhBozxxpS6X9pvtaG%2FJKdUpYAo9SZQGWwcpIz5rlceQ3yCVRMywbQ3Ph46XSOUhxdeNaNZ2KY7RBfAkqL2hlsrRsTa3PCqxQAX5mLVo28wGak6xnBVeRbyJKL4JWNC%2BvzhGwWIaByjBfITW0LJDiUqoI%2F%2BY%2F3GSq%2FG3VoH9OnrQIhzA4NpIuzD8t%2F%2FSBjqkASyijuPkhsplpo9NGRKWf25%2FrELaYwNNYepoFsxXnbEt%2FzYV6Vl57rLrKavD5m8x%2B%2FO9rD8MGpQAuJ%2FpELhxIpr%2F%2BiFbxk%2BR%2BPZ5a32KDbJ8mCCZP4om1DTlbRIRhemJ850OtS2cTsH4KBksjlRNui7Ti9V01CnjO8OOXxosWuJHbpe%2BnCOL6sNuApTXeftWlHW%2FgBWog1o7kBQ8OlwVo2aPW6HH&X-Amz-Signature=f490bb9c4190855c4ef394809f33d50c544b66a3d629d04746d8e11ee34f5f21&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

有这样一个说法，就是相当于多花了 DES 计算能力的百分之几十，也就是稍微多花了点CPO，但是相当于是做了 3 次 DES 的安全的强度。可见什么非常有性价比的，你多花了 50% 的钱，你却收获了 300% 的什么加密的能力，对 a s 已经基本上完全替代了，是吧？浅浪 DES 成为了最经典的算法。


那 a s 上完全可以支持前面 5 种具体的加密的细节的处理方法，那当前比较流行的一种就是老的就是 a e s 128 c b c。还有一种是现在最火最新的，也是我们 2020 年隆重推出的 a s 256 GCM，当前很多的像是我们的网上的签证系统，很多的我们内部安全服务器已经宣称从 2020 年下半年开始不支持 128 CBC 的。所以如果你的客户端，你的这个 Java 的 library 里面选用的还是 128 CBC 的，可以考虑一下是不是替换成256GCM。你要问孙老师， GCM 好像刚刚没有聊到过，对不对？ 256 容易理解， 256 就是最强大的 AES 加密算法的 256 字节进行分组。


那 GCM 是什么呢？ GCM 我把它翻成中文g，对吧？很复杂的一个单词，当我们翻成中文，可以用高雅的来翻成 c 就是计数器，对吧？ counter m 就是 MODULE 模式，高雅的计数器模式其实就是前面第五种计数器模式的翻版，那计数器模式大家可以想一想这个计数值和提前的这个，我们的这个密码学的这个替换和代替这个算法是不是可以提前做？所以它更快？同时它因为有一个什么，有一个技术指一个随机值的累进，所以也是很难破解。


另外这个级其实真正的单词其实不是高雅，是蕴含着一个它便于什么通讯握手的这种能力。于是快握手、难破解，同时快速计算的一种模式基本上是什么？ c b seed 一个翻版和强化。那这样的这种计数器模式处理完以后是不是完全可以替换CBC？未必。原因是什么？原因是我们，可能，特别是已经用过数据加密技术的那些硬盘，或者说是我们的一些数据库，比如像Oracle、DB，two、MySQL，很多的这种数据系统都采用以前是用 a E S E R 8 CBC 加密的。你不可能把所有数据全部反解密，再用新的 AES 256 GCM 加密。因为他们是不兼容的，所以这种情况下导致我们很多系统被迫还要支持我们的什么。中朗的已经不是前朗，是中朗 a E S E R 8 和CBC。另外我们的很多的浏览器甚至于都不支持 AS 256 GCM，以及很多老旧的像 Java 的什么1.7、 1.8 版本的这个库里面可能都没有对它进行支持，所以也导致我们很多站点不能够全面升级到 256 GCM。那相信大家进入 2021 以后应该看到更多的是这种高雅计数器的 AS 256 分片二五六分组的强大的对称加密技术。


好，聊完了强大的对称加密，我们下一节会聊一聊更加复杂的非对称加密。希望老司机的这个车，希望我们的年轻人不讲武德，没有难倒大家，敬请期待下一节的非对称加密。


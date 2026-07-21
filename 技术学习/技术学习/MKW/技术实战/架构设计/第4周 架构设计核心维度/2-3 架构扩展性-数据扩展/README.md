---
title: 2-3 架构扩展性-数据扩展
---

# 2-3 架构扩展性-数据扩展

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/6e0d0e9f-0c1b-4b35-b8fa-d7a49553295b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SU54GG4R%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230421Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAZK10ni6pJlNGQy5V%2FsEISi%2Bur4tz4mCCeRUtYdKlmsAiBB9iaxtszFQICoq4lcfhVhjAjo3AfYEMHOkt%2FxhpMtHCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMaieZ%2FEXIwajEnExIKtwDP2eK8ax7kODgQLC2L1XxFg0Vd32MXDDDwzIeYfBnHyHwEG0%2FX9NesPZsZAmLu6HWf3vgAsyb9jb28HS24I5nB%2FXtpxqnbXXd%2B5HFTp1Ch%2B5l7YIJJLyLgYKrvbcsp0zN2i1CC1pPH6qBzumePFLJGkcQH5U7BXPVv%2BSJvC25IJUHTGW3ELIlHM3h3raLyxILfGjXFt0prN5CrZZk7n8M1jjTsA%2BBtpIjDOkhQ5KEh5cdjkBdtFiVDEoIGXnf3fgIjDxLW70%2BRd9UcFT5gjcJX5z%2F1U0O5EQwlHY3n8qUF0FbSwapxa%2BG0VTqnM3BHza5yKZ0AcAqeS1VRO0aGQ3%2F4DKiMVjj6ipaBgEaPQ186OH7nmYviyVogeTWb8acgrnlfORUeRBTLV6clBtyOZQMVqxWYyDl2lsyfrhjHZE3PQGApG2WUwt2AaR85z6JMnadoJXTAOtIjRId4OtYQ7q%2FRsHl8VZpa922mxYE5FdA1OVZAKzd3HOGHD6NxoIPFZhftmB3IQEd5%2FqbkNzGZ1psYreePrtd2pXOr5i%2Fj2qoET9suFs3y%2BEgqXgQv6mT3TGUr4He%2BFotk%2BV%2BLkonNap6XgyY9oUNuImw9qOcs20u4BY54Xo6sS7XO16llVgwgbf%2F0gY6pgFYatv3q%2FZgcZvBSlF7BMbX05sx5OgDkVbm5gK8ZCM%2FTSbJuS88OuoQ5joR%2Fw8STwQju5RrAdKNF6NOOnIHYWAXFPOzWJS2bNzDYGXHjmmWSArHLEuuInQFvcjeLavpVpiqmWa7%2FuHWtpBzFDNoBmzFQjie8P4AXZCwIlkXmqkc32gd3pgWhVcy4G6iUf6iBxyiuvnDe1LNiFKnmqhImf8dESR1yc3G&X-Amz-Signature=395828df80f08fefd5084dc2eb4a3789d0c3f0e03d854078550a770d9b5d3b3b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/13ced8ad-d5a7-445f-b9bd-4898eb536cbd/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SU54GG4R%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230421Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAZK10ni6pJlNGQy5V%2FsEISi%2Bur4tz4mCCeRUtYdKlmsAiBB9iaxtszFQICoq4lcfhVhjAjo3AfYEMHOkt%2FxhpMtHCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMaieZ%2FEXIwajEnExIKtwDP2eK8ax7kODgQLC2L1XxFg0Vd32MXDDDwzIeYfBnHyHwEG0%2FX9NesPZsZAmLu6HWf3vgAsyb9jb28HS24I5nB%2FXtpxqnbXXd%2B5HFTp1Ch%2B5l7YIJJLyLgYKrvbcsp0zN2i1CC1pPH6qBzumePFLJGkcQH5U7BXPVv%2BSJvC25IJUHTGW3ELIlHM3h3raLyxILfGjXFt0prN5CrZZk7n8M1jjTsA%2BBtpIjDOkhQ5KEh5cdjkBdtFiVDEoIGXnf3fgIjDxLW70%2BRd9UcFT5gjcJX5z%2F1U0O5EQwlHY3n8qUF0FbSwapxa%2BG0VTqnM3BHza5yKZ0AcAqeS1VRO0aGQ3%2F4DKiMVjj6ipaBgEaPQ186OH7nmYviyVogeTWb8acgrnlfORUeRBTLV6clBtyOZQMVqxWYyDl2lsyfrhjHZE3PQGApG2WUwt2AaR85z6JMnadoJXTAOtIjRId4OtYQ7q%2FRsHl8VZpa922mxYE5FdA1OVZAKzd3HOGHD6NxoIPFZhftmB3IQEd5%2FqbkNzGZ1psYreePrtd2pXOr5i%2Fj2qoET9suFs3y%2BEgqXgQv6mT3TGUr4He%2BFotk%2BV%2BLkonNap6XgyY9oUNuImw9qOcs20u4BY54Xo6sS7XO16llVgwgbf%2F0gY6pgFYatv3q%2FZgcZvBSlF7BMbX05sx5OgDkVbm5gK8ZCM%2FTSbJuS88OuoQ5joR%2Fw8STwQju5RrAdKNF6NOOnIHYWAXFPOzWJS2bNzDYGXHjmmWSArHLEuuInQFvcjeLavpVpiqmWa7%2FuHWtpBzFDNoBmzFQjie8P4AXZCwIlkXmqkc32gd3pgWhVcy4G6iUf6iBxyiuvnDe1LNiFKnmqhImf8dESR1yc3G&X-Amz-Signature=126134bef6137b5cd3bb980b2fa4b64bdd22c9bf3e9265353bb5f3ee299c796c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

架起需求到落地的桥梁，构建 it 新蓝图。我是张飞扬。上一节我们聊聊应用扩展，看了看什么应用扩展的套娃是长什么样子。那这一节我们来说一说数据是如何扩展的，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/da07f78f-a09d-419f-b40f-a9f8a568aa8f/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SU54GG4R%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230421Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAZK10ni6pJlNGQy5V%2FsEISi%2Bur4tz4mCCeRUtYdKlmsAiBB9iaxtszFQICoq4lcfhVhjAjo3AfYEMHOkt%2FxhpMtHCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMaieZ%2FEXIwajEnExIKtwDP2eK8ax7kODgQLC2L1XxFg0Vd32MXDDDwzIeYfBnHyHwEG0%2FX9NesPZsZAmLu6HWf3vgAsyb9jb28HS24I5nB%2FXtpxqnbXXd%2B5HFTp1Ch%2B5l7YIJJLyLgYKrvbcsp0zN2i1CC1pPH6qBzumePFLJGkcQH5U7BXPVv%2BSJvC25IJUHTGW3ELIlHM3h3raLyxILfGjXFt0prN5CrZZk7n8M1jjTsA%2BBtpIjDOkhQ5KEh5cdjkBdtFiVDEoIGXnf3fgIjDxLW70%2BRd9UcFT5gjcJX5z%2F1U0O5EQwlHY3n8qUF0FbSwapxa%2BG0VTqnM3BHza5yKZ0AcAqeS1VRO0aGQ3%2F4DKiMVjj6ipaBgEaPQ186OH7nmYviyVogeTWb8acgrnlfORUeRBTLV6clBtyOZQMVqxWYyDl2lsyfrhjHZE3PQGApG2WUwt2AaR85z6JMnadoJXTAOtIjRId4OtYQ7q%2FRsHl8VZpa922mxYE5FdA1OVZAKzd3HOGHD6NxoIPFZhftmB3IQEd5%2FqbkNzGZ1psYreePrtd2pXOr5i%2Fj2qoET9suFs3y%2BEgqXgQv6mT3TGUr4He%2BFotk%2BV%2BLkonNap6XgyY9oUNuImw9qOcs20u4BY54Xo6sS7XO16llVgwgbf%2F0gY6pgFYatv3q%2FZgcZvBSlF7BMbX05sx5OgDkVbm5gK8ZCM%2FTSbJuS88OuoQ5joR%2Fw8STwQju5RrAdKNF6NOOnIHYWAXFPOzWJS2bNzDYGXHjmmWSArHLEuuInQFvcjeLavpVpiqmWa7%2FuHWtpBzFDNoBmzFQjie8P4AXZCwIlkXmqkc32gd3pgWhVcy4G6iUf6iBxyiuvnDe1LNiFKnmqhImf8dESR1yc3G&X-Amz-Signature=6d2849ca4cee36d1464f8bed9b96eb781cd52f567c3788df17bac3754d7d72c9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

还是那熟悉的立方体。但这次 x 轴变成了水平复制，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/325a3093-d02e-4072-9682-0295e48a82e8/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SU54GG4R%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230421Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAZK10ni6pJlNGQy5V%2FsEISi%2Bur4tz4mCCeRUtYdKlmsAiBB9iaxtszFQICoq4lcfhVhjAjo3AfYEMHOkt%2FxhpMtHCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMaieZ%2FEXIwajEnExIKtwDP2eK8ax7kODgQLC2L1XxFg0Vd32MXDDDwzIeYfBnHyHwEG0%2FX9NesPZsZAmLu6HWf3vgAsyb9jb28HS24I5nB%2FXtpxqnbXXd%2B5HFTp1Ch%2B5l7YIJJLyLgYKrvbcsp0zN2i1CC1pPH6qBzumePFLJGkcQH5U7BXPVv%2BSJvC25IJUHTGW3ELIlHM3h3raLyxILfGjXFt0prN5CrZZk7n8M1jjTsA%2BBtpIjDOkhQ5KEh5cdjkBdtFiVDEoIGXnf3fgIjDxLW70%2BRd9UcFT5gjcJX5z%2F1U0O5EQwlHY3n8qUF0FbSwapxa%2BG0VTqnM3BHza5yKZ0AcAqeS1VRO0aGQ3%2F4DKiMVjj6ipaBgEaPQ186OH7nmYviyVogeTWb8acgrnlfORUeRBTLV6clBtyOZQMVqxWYyDl2lsyfrhjHZE3PQGApG2WUwt2AaR85z6JMnadoJXTAOtIjRId4OtYQ7q%2FRsHl8VZpa922mxYE5FdA1OVZAKzd3HOGHD6NxoIPFZhftmB3IQEd5%2FqbkNzGZ1psYreePrtd2pXOr5i%2Fj2qoET9suFs3y%2BEgqXgQv6mT3TGUr4He%2BFotk%2BV%2BLkonNap6XgyY9oUNuImw9qOcs20u4BY54Xo6sS7XO16llVgwgbf%2F0gY6pgFYatv3q%2FZgcZvBSlF7BMbX05sx5OgDkVbm5gK8ZCM%2FTSbJuS88OuoQ5joR%2Fw8STwQju5RrAdKNF6NOOnIHYWAXFPOzWJS2bNzDYGXHjmmWSArHLEuuInQFvcjeLavpVpiqmWa7%2FuHWtpBzFDNoBmzFQjie8P4AXZCwIlkXmqkc32gd3pgWhVcy4G6iUf6iBxyiuvnDe1LNiFKnmqhImf8dESR1yc3G&X-Amz-Signature=5062b08b9726544848e7feaa70a5e4e355e5785c55147bf4e07bad3bf9b80c21&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

强调复制二字。 y 轴是什么？是库表分割a，重点在于库表， z 轴是哈希驱魔，是不是很熟悉的单词？好，那让我们来看一看x、y、 z 具体是什么吧。


数据要水平复制，自然先要聊一聊我们传统的数据库SQL，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/b28c7385-9b46-4a12-8b56-e496c54b56e0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SU54GG4R%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230421Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAZK10ni6pJlNGQy5V%2FsEISi%2Bur4tz4mCCeRUtYdKlmsAiBB9iaxtszFQICoq4lcfhVhjAjo3AfYEMHOkt%2FxhpMtHCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMaieZ%2FEXIwajEnExIKtwDP2eK8ax7kODgQLC2L1XxFg0Vd32MXDDDwzIeYfBnHyHwEG0%2FX9NesPZsZAmLu6HWf3vgAsyb9jb28HS24I5nB%2FXtpxqnbXXd%2B5HFTp1Ch%2B5l7YIJJLyLgYKrvbcsp0zN2i1CC1pPH6qBzumePFLJGkcQH5U7BXPVv%2BSJvC25IJUHTGW3ELIlHM3h3raLyxILfGjXFt0prN5CrZZk7n8M1jjTsA%2BBtpIjDOkhQ5KEh5cdjkBdtFiVDEoIGXnf3fgIjDxLW70%2BRd9UcFT5gjcJX5z%2F1U0O5EQwlHY3n8qUF0FbSwapxa%2BG0VTqnM3BHza5yKZ0AcAqeS1VRO0aGQ3%2F4DKiMVjj6ipaBgEaPQ186OH7nmYviyVogeTWb8acgrnlfORUeRBTLV6clBtyOZQMVqxWYyDl2lsyfrhjHZE3PQGApG2WUwt2AaR85z6JMnadoJXTAOtIjRId4OtYQ7q%2FRsHl8VZpa922mxYE5FdA1OVZAKzd3HOGHD6NxoIPFZhftmB3IQEd5%2FqbkNzGZ1psYreePrtd2pXOr5i%2Fj2qoET9suFs3y%2BEgqXgQv6mT3TGUr4He%2BFotk%2BV%2BLkonNap6XgyY9oUNuImw9qOcs20u4BY54Xo6sS7XO16llVgwgbf%2F0gY6pgFYatv3q%2FZgcZvBSlF7BMbX05sx5OgDkVbm5gK8ZCM%2FTSbJuS88OuoQ5joR%2Fw8STwQju5RrAdKNF6NOOnIHYWAXFPOzWJS2bNzDYGXHjmmWSArHLEuuInQFvcjeLavpVpiqmWa7%2FuHWtpBzFDNoBmzFQjie8P4AXZCwIlkXmqkc32gd3pgWhVcy4G6iUf6iBxyiuvnDe1LNiFKnmqhImf8dESR1yc3G&X-Amz-Signature=22fcab0435e08cb4d05800c1d9ca731d42ef0fa91dcf69efe549f766583961ea&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

是不是像 Oracle 这样，起一个 rack 3- 5 个节点，然后数据强一执行。这可不是电商平台的推荐的思路，所有的强一致性必然遇到什么扩展的瓶颈？你扩展 3- 5 个节点可以，你给我扩展 30 个节点试试看有没有 30 个节点？ Oracle rock 这个非常难，甚至于都要产生崩溃的情况了。


那怎么样在多节点情况下很好的进行横向扩展呢？通常在电商平台，我们推荐什么读写分一写多读，这样比较容易扩展，因为写的数据库的话总归会有binlog，我们可以采用一些CDC，(Change Data Capture，变更数据捕获) 等技术，把它的数据的变化量发布到更多的读数据库。而我们平时大型互联网，有可能是什么读的压力是十倍甚至于百倍于写的压力。这种情况下，读写分离，一写多读很适合快速的横向了，大量的扩展，同时也能让我们的应用能够承载更大的数据吞吐量。


好聊完了传统CQ，我们 no CQ 像卡三周，像芒果利比亚，像海杜普，它天生就支持什么多副本，只要我设个参数， replica 等于5，是不是 5 副本轻松就搞定？还有什么是水平复制的好方法？缓存键值对，比如像Redis，比如像 coach base 既支持写到盘里面落盘，也支持什么更多个节点的非落盘缓存直接读取，那通过这种方法也能够实现横向的扩展。好看一看他打的是不是一手好牌。


首先它支持最终一致性，这个在什么？在飞扬老师的这个理论里面应该会给大家详细讲讲。 CIP 的，我这里就简单带过 CIP 就是什么，一旦你要体现强一致性，你就会牺牲掉高可用，甚至于牺牲掉什么多副本，而我们这里一致性没那么重要，对吧？大型电商平台通常是我们的可用性和我们的多副本性能扩展性很关键，所以牺牲少量一致性，通过最终一致性就能满足要求。


还有什么优点？下一个优点我们要重点聊一聊了，就是这个优点了。 CDC 便捷复制所谓 CDC 便捷复制，就是不管你是用CDC， CC 是 change data capture 这种就传统的数据复制方式，还是像 no C Q2 这种天生的多副本方式，整个复制过程其实只要配一两条命令或者配一两个参数就可以了，不需要你很复杂，像MySQL、 Oracle d b two 还有 SQL Server 天生都有。它自带的什么 CDC 的软件很方便实现一写多读，其他的 no CQ 基本上原生就是多瑞布利克的复制。除此以外，数据高可用也并不很难。一旦你实现了三个副本，你就自然而然实现了什么三份可用性。你原来的如果是说有 99 的高可用性，那你三个副本呢？你就是什么 0. 1 *0. 1 *0. 1 就是 0. 001 的出错概率，这个时候你就变成什么 99. 99 了。是不是稳定性上升很方便？高可用上升如此轻松？唉，就是这样，事实也就是如此。好，有什么弱点？弱点太明显了。


当我什么一写九毒的时候，是不是我浪费了 9 份数据空间？本来我存 1T 空间，我只要存 1T 就够了，现在我有 9 份毒，我要复制 9 份，所以我足足浪费了 9 倍的数据空间，但我一写 99 毒怎么办？那浪费的也太多了吧。所以 x 轴水平复制还是有上限的，不能够无限制的复制好。


我们看一看 y 轴， y 轴通常配合什么 y 轴的应用进行分割，前面也聊了，为了防止，是吧支付应用影响到登录应用，会把支付跟登录进行分割那一样道理。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/a709734d-c7a1-4cb1-bd39-c059c6bda3b9/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SU54GG4R%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230421Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAZK10ni6pJlNGQy5V%2FsEISi%2Bur4tz4mCCeRUtYdKlmsAiBB9iaxtszFQICoq4lcfhVhjAjo3AfYEMHOkt%2FxhpMtHCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMaieZ%2FEXIwajEnExIKtwDP2eK8ax7kODgQLC2L1XxFg0Vd32MXDDDwzIeYfBnHyHwEG0%2FX9NesPZsZAmLu6HWf3vgAsyb9jb28HS24I5nB%2FXtpxqnbXXd%2B5HFTp1Ch%2B5l7YIJJLyLgYKrvbcsp0zN2i1CC1pPH6qBzumePFLJGkcQH5U7BXPVv%2BSJvC25IJUHTGW3ELIlHM3h3raLyxILfGjXFt0prN5CrZZk7n8M1jjTsA%2BBtpIjDOkhQ5KEh5cdjkBdtFiVDEoIGXnf3fgIjDxLW70%2BRd9UcFT5gjcJX5z%2F1U0O5EQwlHY3n8qUF0FbSwapxa%2BG0VTqnM3BHza5yKZ0AcAqeS1VRO0aGQ3%2F4DKiMVjj6ipaBgEaPQ186OH7nmYviyVogeTWb8acgrnlfORUeRBTLV6clBtyOZQMVqxWYyDl2lsyfrhjHZE3PQGApG2WUwt2AaR85z6JMnadoJXTAOtIjRId4OtYQ7q%2FRsHl8VZpa922mxYE5FdA1OVZAKzd3HOGHD6NxoIPFZhftmB3IQEd5%2FqbkNzGZ1psYreePrtd2pXOr5i%2Fj2qoET9suFs3y%2BEgqXgQv6mT3TGUr4He%2BFotk%2BV%2BLkonNap6XgyY9oUNuImw9qOcs20u4BY54Xo6sS7XO16llVgwgbf%2F0gY6pgFYatv3q%2FZgcZvBSlF7BMbX05sx5OgDkVbm5gK8ZCM%2FTSbJuS88OuoQ5joR%2Fw8STwQju5RrAdKNF6NOOnIHYWAXFPOzWJS2bNzDYGXHjmmWSArHLEuuInQFvcjeLavpVpiqmWa7%2FuHWtpBzFDNoBmzFQjie8P4AXZCwIlkXmqkc32gd3pgWhVcy4G6iUf6iBxyiuvnDe1LNiFKnmqhImf8dESR1yc3G&X-Amz-Signature=33fccc133204f320d76f32cb9177037332751605ba35b0cd2372bff18b34c4e0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

数据库支付数据库可以登录数据库，用户登录数据库必须是两套独立的数据库，而这两套独立的表跟数据库要运行在不同的什么节点上，这很关键。我们扩展性不光是在讨论应用架构，也在讨论系统架构，一定要在系统上采用不同的节点，不同的 CPU 内存来承载它。好，那除此以外，什么我们的库表分割是不是跟微幅的气氛很相关？跟我们前面聊的模块的分割非常相似，另外它也符合康威定律，抗歪定律。说什么？说？一旦你的组织定好以后，你的组织就应该管理你整个的组织里运行的所有业务了，包含我们应用，包含我们的数据库。所以数据库不应该让什么多个数据库运行在同样的物理节点上，而应该把它切分开来。好有什么好处？首先就是什么数据故障隔离，就是我刚刚聊的，当你支付数据的什么崩溃了以后，你的 DDR 写错了，或者你的 DMR 出现了删表删库的操作，这个时候你支付不能支付了没有关系，但是数据一样保存在那里，什么数据用户登录？数据用户仍然可以什么正常的登录，对不对？同样道理，这也很适合资源迭代。


（

康威定律（Conway's Law）是由迈克尔·康威（Mike Conway）提出的一个观察，它指出组织的技术架构的设计和结构往往反映了组织的沟通结构。换句话说，如果一个组织的沟通结构是垂直的，那么其技术架构也会是垂直的；如果组织的沟通结构是水平的，那么其技术架构也会是水平的。

在IT架构设计中，康威定律的运用意味着架构师需要考虑组织的沟通结构，以确保技术架构能够支持组织的工作方式。例如，如果一个组织的团队是分散在不同地点的，那么架构师可能需要设计一个分布式的架构，以支持这种工作方式。

使用康威定律的好处主要有：

- **提高效率**：通过设计与组织沟通结构相匹配的架构，可以减少不必要的沟通和协调成本，提高工作效率。
- **增强协作**：对于分布式的组织结构，康威定律鼓励使用开放的、透明的沟通方式，这有助于增强团队之间的协作。
- **适应变化**：随着组织的变化，康威定律也可以指导架构师调整架构，以适应新的工作方式和需求。
在实际应用中，康威定律可以通过以下方式运用：

- **识别组织的沟通结构**：首先，架构师需要理解组织的沟通结构，包括团队的分布、协作方式等。
- **设计与沟通结构相匹配的架构**：基于组织的沟通结构，架构师设计出能够支持这种结构的技术架构。
- **适应变化**：当组织的沟通结构发生变化时，架构师需要及时调整架构，以保持与康威定律的一致性。
总的来说，康威定律是一个重要的原则，它强调了组织的沟通结构对技术架构的影响，并提供了一种方法来指导架构师设计出能够支持组织工作方式的架构。

）


所谓资源迭代，就是业务先要迭代什么业务？我新开发了一个购物车业务。好，那我的代码是不是也要开发一个购物车代码？开发的购物车代码，那我的数据库起一个新的数据库节点，跑一个新的购物车数据库，然后购物车表。好，这就是什么资源迭代分配。另外， Y9 是可以实现**强一致的，每一个不同的业务落在他自己的数据库，这个数据库是完完全全的强一致性。你甚至可以用前面说什么 Oracle rack 3 减 rack 来跑你的这个本业务的数据库，所以它是强一致的。缺点很明显，跟它的 y 轴业务分割一样，你要懂业务，你才能运行你的数据库。比如说我们说登录业务后台跑登录数据库，所以这个数据库的管理员其实要懂你的登录业务，这样也导致什么？因为你的微服务不可能割成千上万个微服务，所以你的数据库分表分库没法分割成千上万的，它的横向扩展还是受到了业务扩展性的限制。**

**
那什么才是无限**的？这就是 z 轴哈希取模。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/d6802e96-1f17-4cfb-a00b-8a2f7e812c9b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SU54GG4R%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230421Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAZK10ni6pJlNGQy5V%2FsEISi%2Bur4tz4mCCeRUtYdKlmsAiBB9iaxtszFQICoq4lcfhVhjAjo3AfYEMHOkt%2FxhpMtHCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMaieZ%2FEXIwajEnExIKtwDP2eK8ax7kODgQLC2L1XxFg0Vd32MXDDDwzIeYfBnHyHwEG0%2FX9NesPZsZAmLu6HWf3vgAsyb9jb28HS24I5nB%2FXtpxqnbXXd%2B5HFTp1Ch%2B5l7YIJJLyLgYKrvbcsp0zN2i1CC1pPH6qBzumePFLJGkcQH5U7BXPVv%2BSJvC25IJUHTGW3ELIlHM3h3raLyxILfGjXFt0prN5CrZZk7n8M1jjTsA%2BBtpIjDOkhQ5KEh5cdjkBdtFiVDEoIGXnf3fgIjDxLW70%2BRd9UcFT5gjcJX5z%2F1U0O5EQwlHY3n8qUF0FbSwapxa%2BG0VTqnM3BHza5yKZ0AcAqeS1VRO0aGQ3%2F4DKiMVjj6ipaBgEaPQ186OH7nmYviyVogeTWb8acgrnlfORUeRBTLV6clBtyOZQMVqxWYyDl2lsyfrhjHZE3PQGApG2WUwt2AaR85z6JMnadoJXTAOtIjRId4OtYQ7q%2FRsHl8VZpa922mxYE5FdA1OVZAKzd3HOGHD6NxoIPFZhftmB3IQEd5%2FqbkNzGZ1psYreePrtd2pXOr5i%2Fj2qoET9suFs3y%2BEgqXgQv6mT3TGUr4He%2BFotk%2BV%2BLkonNap6XgyY9oUNuImw9qOcs20u4BY54Xo6sS7XO16llVgwgbf%2F0gY6pgFYatv3q%2FZgcZvBSlF7BMbX05sx5OgDkVbm5gK8ZCM%2FTSbJuS88OuoQ5joR%2Fw8STwQju5RrAdKNF6NOOnIHYWAXFPOzWJS2bNzDYGXHjmmWSArHLEuuInQFvcjeLavpVpiqmWa7%2FuHWtpBzFDNoBmzFQjie8P4AXZCwIlkXmqkc32gd3pgWhVcy4G6iUf6iBxyiuvnDe1LNiFKnmqhImf8dESR1yc3G&X-Amz-Signature=1ec65488e2affdddcbdde3c4d90fb806491a457d279d3c8518cdb317a1d6ad0b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

哈希取模还是跟原来的应用 z 轴一样，它可以根据 user ID、 SPU ID、 SKU ID、产品的或者是库存单元的这个 ID 来进行，哈希先哈希再取膜，它同时还有什么？我们的传统数据库有很多的，这个叫做加强界，或者叫做什么强化功能，比如像什么阿里巴巴的 my cat，它可以支持像我们的 MySQL 或者 Postgrid SQL 上面盖一个帽子，这个帽子底下可以挂 5- 10 个， 50 个甚至 100 个左右的不同的MySQL。然后它通过前端是 key 的哈希取模，所有 user name 叫 a 的，我们分配到 a 库，我们 user name 以 b 开头的分配到 b 库，或者 user ID 以什么 c 开头的，我们分配到 c 库，等等。不管你是阿拉伯数字也好，英文字母也好，它都有一套规则分配到不同的库。那这是对传统 CQ 来说，要配合一个帽子来实现分库分别。


而对于 no CQ，几乎大部分Nosql，像Hadoop， MongoDB 前面聊的那些都是天生支持sharding， shard chunk，不管什么英文单词，中文单词就一个分片，它都能够分成很多很多的片。那这个 z 轴哈希曲目有什么好处？第一条就是加快了查询，因为只要你给我一个什么查询的键值，我很快能找到你对应的数据库，然后用这个数据库提供你快速的响应。那除此以外，它的扩展是无限，只要你能做一个什么散射，你散射成大概上万个单词，然后你这个单词就可以什么在和取模，你这个取模可以取成对时，取模就是可以发在 10 台服务器上。你如果对 100 驱模，就是发在 100 服务器上。如果你对1万驱模，你就可以分布在1万个服务器上，扩展是几乎无限的。


这就是 z 轴哈希取末的一个很大的亮点，除此以外，你不需要考虑业务是吧？你只需要对某一个 k 值进行分片就可以，你不需要去考虑跟什么业务有关。同时每一个分片都是强一致的，你这个分片的数据库实现了这个分片的所有的数据一致性的任务，它没有跟其他分片有关系，所以每片自身都非常的一致。


好，聊完了XYZ，又到了什么五套娃的时间了，我们看一看啊，**真正生产环境是怎么样用 XYZ 组合起来实现数据的扩展性的？**

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/519a79f3-4655-47ef-a9ed-5d40d88cb6d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SU54GG4R%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230421Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAZK10ni6pJlNGQy5V%2FsEISi%2Bur4tz4mCCeRUtYdKlmsAiBB9iaxtszFQICoq4lcfhVhjAjo3AfYEMHOkt%2FxhpMtHCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMaieZ%2FEXIwajEnExIKtwDP2eK8ax7kODgQLC2L1XxFg0Vd32MXDDDwzIeYfBnHyHwEG0%2FX9NesPZsZAmLu6HWf3vgAsyb9jb28HS24I5nB%2FXtpxqnbXXd%2B5HFTp1Ch%2B5l7YIJJLyLgYKrvbcsp0zN2i1CC1pPH6qBzumePFLJGkcQH5U7BXPVv%2BSJvC25IJUHTGW3ELIlHM3h3raLyxILfGjXFt0prN5CrZZk7n8M1jjTsA%2BBtpIjDOkhQ5KEh5cdjkBdtFiVDEoIGXnf3fgIjDxLW70%2BRd9UcFT5gjcJX5z%2F1U0O5EQwlHY3n8qUF0FbSwapxa%2BG0VTqnM3BHza5yKZ0AcAqeS1VRO0aGQ3%2F4DKiMVjj6ipaBgEaPQ186OH7nmYviyVogeTWb8acgrnlfORUeRBTLV6clBtyOZQMVqxWYyDl2lsyfrhjHZE3PQGApG2WUwt2AaR85z6JMnadoJXTAOtIjRId4OtYQ7q%2FRsHl8VZpa922mxYE5FdA1OVZAKzd3HOGHD6NxoIPFZhftmB3IQEd5%2FqbkNzGZ1psYreePrtd2pXOr5i%2Fj2qoET9suFs3y%2BEgqXgQv6mT3TGUr4He%2BFotk%2BV%2BLkonNap6XgyY9oUNuImw9qOcs20u4BY54Xo6sS7XO16llVgwgbf%2F0gY6pgFYatv3q%2FZgcZvBSlF7BMbX05sx5OgDkVbm5gK8ZCM%2FTSbJuS88OuoQ5joR%2Fw8STwQju5RrAdKNF6NOOnIHYWAXFPOzWJS2bNzDYGXHjmmWSArHLEuuInQFvcjeLavpVpiqmWa7%2FuHWtpBzFDNoBmzFQjie8P4AXZCwIlkXmqkc32gd3pgWhVcy4G6iUf6iBxyiuvnDe1LNiFKnmqhImf8dESR1yc3G&X-Amz-Signature=d56b758684e9860fa16c764915724c3118b0b462f72ebd1bcbb66b81cb6a2681&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

我们以搜索引擎 Elastic search 为例，那大家都知道 electric search 是什么？基于我们的卢森引擎，假设我们先起一个节点，在一个节点上我们可以跑一个我们的简单的数据，对吧？但是这个数据也许我们可以采用这样的方法，把 z 轴哈希曲模进行分片。假设，我们先对一个输入的key，假设是 user ID，我们对这个 key 取哈希哈希完了以后是一长串数字，然后我们要分成三片，怎么办？我们就对 3 取模，对它的结果不是 0 就是一就是2。所以这样我们就会把数据放在 P0 这个一片上，或者放在 P1 这一片上，或者放在 P2 这一片上，他们在一台服务器里面。现在我进一步扩展一下，我是不是能够放在两台服务器，然后采用 x 轴横向扩展，当然可以，我可以创建一个副本P0，我创建它的副本放在 NODE 2 节点 2 上，叫做什么 replicate 0 叫R0，那 P1 它的副本叫R1， P2 的它的副本就叫R2。然后我再增加一个节点，这时候我可以把什么？我可以把分片跟副本分散在不同的节点上，那同时确保什么我的 P0 分布在 3 节点上，那我它的 R0 保证肯定不在 3 上，不是一就是2，这里就是在 2 节点上。那一样道理， P1 的副本 R1 和 P2 的副本 R2 放在合理的节点上。


大家可以想象，如果我是 50 个节点， 500 个分片，是不是也能够很容易的进行扩展？这就是 Elastic search 天生具有的 XZ 轴横向数据扩展能力。好只有 XJ 够不够？当然不够， Z轴可能是最里面的套娃了，套娃的心， x 是中间那个套娃，还有一个什么最大的套娃，那是什么呢？那就是 y 轴。

```shell
Elasticsearch作为例子来说明XYZ模型在实际应用中是如何实现数据扩展的。以下是Elasticsearch中XYZ扩展模型的详细解释：

### Z轴 - 哈希分片 (Sharding)

1. **哈希分片**：Elasticsearch使用哈希函数对数据进行分片。这意味着，当数据被索引时，Elasticsearch会根据数据的某个键（如用户ID）进行哈希处理，然后根据哈希值对一个设定的数值（比如3）取模，以此来决定数据应该存储在哪个分片上。

2. **取模分配**：假设我们有三个分片（P0, P1, P2），数据的哈希值取模后的结果可能是0、1或2，这将决定数据存储在P0、P1或P2。

3. **分片分布**：在初始阶段，这些分片可能都位于同一个节点上。

### X轴 - 副本 (Replication)

1. **副本创建**：为了提高数据的可用性和读取性能，Elasticsearch允许为每个主分片（primary shard）创建副本分片（replica shard）。这些副本分片包含了主分片数据的精确副本。

2. **副本分配**：副本分片会被分配到不同的节点上。例如，如果P0的主分片在节点1上，其副本（R0）可以放在节点2上。

3. **横向扩展**：通过增加节点并将副本分布在这些节点上，Elasticsearch实现了X轴的扩展，提高了系统的读取吞吐量和可用性。

### Y轴 - 索引分离

1. **索引分配**：在Elasticsearch中，不同的业务或数据类型可以被分配到不同的索引（index）中。例如，用户数据、产品数据和库存数据可以分别存储在不同的索引中。

2. **集群分离**：更进一步，不同的索引可以分布在不同的Elasticsearch集群中，每个集群专注于处理特定类型的查询和数据管理任务。

3. **业务隔离**：通过Y轴的扩展，不仅实现了数据的物理分离，还实现了业务逻辑上的隔离，这有助于提高系统的稳定性和可维护性。

### 综合XYZ扩展

1. **节点扩展**：随着业务的增长，可以简单地增加更多的节点来扩展Elasticsearch集群。

2. **分片和副本调整**：可以根据需要调整分片的数量和副本的数量，以适应数据量和查询负载的变化。

3. **业务集群分配**：不同的业务或服务可以分配到不同的Elasticsearch集群中，实现业务之间的物理和逻辑隔离。

通过XYZ模型的扩展，Elasticsearch能够实现高效的数据存储、快速的查询响应，并且具有良好的可扩展性和高可用性。这种模型不仅适用于Elasticsearch，也适用于其他需要进行水平扩展的分布式系统设计。
```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/518ef19b-f52d-43d9-b111-ece1bd3b50cd/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SU54GG4R%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230421Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIAZK10ni6pJlNGQy5V%2FsEISi%2Bur4tz4mCCeRUtYdKlmsAiBB9iaxtszFQICoq4lcfhVhjAjo3AfYEMHOkt%2FxhpMtHCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMaieZ%2FEXIwajEnExIKtwDP2eK8ax7kODgQLC2L1XxFg0Vd32MXDDDwzIeYfBnHyHwEG0%2FX9NesPZsZAmLu6HWf3vgAsyb9jb28HS24I5nB%2FXtpxqnbXXd%2B5HFTp1Ch%2B5l7YIJJLyLgYKrvbcsp0zN2i1CC1pPH6qBzumePFLJGkcQH5U7BXPVv%2BSJvC25IJUHTGW3ELIlHM3h3raLyxILfGjXFt0prN5CrZZk7n8M1jjTsA%2BBtpIjDOkhQ5KEh5cdjkBdtFiVDEoIGXnf3fgIjDxLW70%2BRd9UcFT5gjcJX5z%2F1U0O5EQwlHY3n8qUF0FbSwapxa%2BG0VTqnM3BHza5yKZ0AcAqeS1VRO0aGQ3%2F4DKiMVjj6ipaBgEaPQ186OH7nmYviyVogeTWb8acgrnlfORUeRBTLV6clBtyOZQMVqxWYyDl2lsyfrhjHZE3PQGApG2WUwt2AaR85z6JMnadoJXTAOtIjRId4OtYQ7q%2FRsHl8VZpa922mxYE5FdA1OVZAKzd3HOGHD6NxoIPFZhftmB3IQEd5%2FqbkNzGZ1psYreePrtd2pXOr5i%2Fj2qoET9suFs3y%2BEgqXgQv6mT3TGUr4He%2BFotk%2BV%2BLkonNap6XgyY9oUNuImw9qOcs20u4BY54Xo6sS7XO16llVgwgbf%2F0gY6pgFYatv3q%2FZgcZvBSlF7BMbX05sx5OgDkVbm5gK8ZCM%2FTSbJuS88OuoQ5joR%2Fw8STwQju5RrAdKNF6NOOnIHYWAXFPOzWJS2bNzDYGXHjmmWSArHLEuuInQFvcjeLavpVpiqmWa7%2FuHWtpBzFDNoBmzFQjie8P4AXZCwIlkXmqkc32gd3pgWhVcy4G6iUf6iBxyiuvnDe1LNiFKnmqhImf8dESR1yc3G&X-Amz-Signature=96e34cbae369716523eac73dccfb25fe20cb4bbe1e651f6423aa2edd329f6ff6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

假设我们刚刚提的是search，这个集群是给用户端搜索服务的，那我们是不是能够再弄一个产品搜索的 it search，再弄一个库存搜索里的search，这样就实现了 y 轴的库表分离的扩展。那么在实际操作过程当中，也许用户产品跟库存是通过不同的indexing，通过不同的 collection 分布在同一个集群里面。但很多时候，特别是大型电商平台，确实是每个微服务有独立的我们的管理部门，那这个部门完全运行他自己的。这么一来，社群集群这个时候就真真正正是不同的集群的 y 轴组合了。


大家现在是不是对套娃理论很了解了？套娃里面不管是数据还是什么应用，都是先套x，外面再套个z，最后还是可以在最外层套一个y，这样就套出完整的一套什么扩展性应用、扩展性数据了。好，聊完了架构的扩展性，下节我们就来聊一聊作为架构师，你应该如何考虑组织的扩展性，大家敬请期待。





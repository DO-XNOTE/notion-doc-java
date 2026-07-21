---
title: 2-10 枚举分片
---

# 2-10 枚举分片

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/6edf9eef-d13f-4d00-921d-85f0ad42329f/SCR-20240807-qvmg.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667OU56QUW%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQClPAvi8f6ymRxwS4tpXsmmyr66MHVbsb%2B%2FF6yoYwDAggIgWG6ocYg5aYi0jresbzwUqSt7l%2F%2B8tUdyiHM4wsdxg6sqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLpjDSQ9AhqzQVSfzCrcA9FxMM34h1Q4Pe1BiTrYSJOnQ%2BpfCKdLu2YrkhsCS%2B0WsQkEKxPsoGOTIFkd%2BuTgE7adr%2BDBPcG5Kv4kAiX5CHfLwh45jXUF02KIWJ9piNBjEAgkvxuspfKCevHRrMNstK4izXPOB0oPReayTBSSFBb2sCFvSZp%2BqAsILI8Ogvoq3lBf4LycGS8f2jqGPXiuGS2we91KtePS0%2BDomoDE25jRS8TjYJthuoitmmB4en2VeuRZrBkj0qVWpGvZuzLdyaIPdUzzmWVY5i5RUsgYJOnzgGjr2ejfUWsmdHqvLq5yHBwxq7BIg9ZgbZsvYRHVuTIuvo%2F5eY%2Fi%2BSjh5TiEJ2c6K%2FIHowqNGvqvKlkwHxjNguFQfimQo6Abwk0OF4COCSk2BJku90B%2BkgRzvZCNDTRS19CqwjxvbRucA6nUSSfs7ecVndHYGXEKf%2B20%2B9N5NjMa5L1pi1ocnmcyQwYvYbEHbgmGjVy8q72sbbooOuTU9ohWpDGDmYKQSQ0a5uCm3NmylRO%2BA25ilYeDMMOiO%2BfZdSIsRxp%2FRR2jSN25Rm9bR%2By0ZF9BRj3QrK0G5YVfKqfIi0t5tky5j2O4opge%2BdMOfbj6ohwOm1zusYHzsOZTXPIoxM6%2B4tkIkLISMJS3%2F9IGOqUBrwDm%2B0%2FamKpQUsoNSi3rdm949p99UpMl5Pa9Kg4fwNWZ1rJwA96jcIPJq5d3MwIkkNhD9y7sIkYd1ZISYRgsjC2YnPcxO9TsVGqOShekwKarofY%2FsVka5EkSfdnOHHf2rS2K36Hj%2FSpIV5rmhwMYJ06KvqZmElmaOdywmUEpzpBJkIUh1BAzYukYOMhLU06ocMDFAkk118gNeD2RGCYtAONJoOOg&X-Amz-Signature=66779f916cb10239cc9bdf1ac7b13744d2d4e56131dd9b35dedd2b97ebba4ad5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/ff59c725-ee39-4968-be3f-96e79cd9c760/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667OU56QUW%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQClPAvi8f6ymRxwS4tpXsmmyr66MHVbsb%2B%2FF6yoYwDAggIgWG6ocYg5aYi0jresbzwUqSt7l%2F%2B8tUdyiHM4wsdxg6sqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLpjDSQ9AhqzQVSfzCrcA9FxMM34h1Q4Pe1BiTrYSJOnQ%2BpfCKdLu2YrkhsCS%2B0WsQkEKxPsoGOTIFkd%2BuTgE7adr%2BDBPcG5Kv4kAiX5CHfLwh45jXUF02KIWJ9piNBjEAgkvxuspfKCevHRrMNstK4izXPOB0oPReayTBSSFBb2sCFvSZp%2BqAsILI8Ogvoq3lBf4LycGS8f2jqGPXiuGS2we91KtePS0%2BDomoDE25jRS8TjYJthuoitmmB4en2VeuRZrBkj0qVWpGvZuzLdyaIPdUzzmWVY5i5RUsgYJOnzgGjr2ejfUWsmdHqvLq5yHBwxq7BIg9ZgbZsvYRHVuTIuvo%2F5eY%2Fi%2BSjh5TiEJ2c6K%2FIHowqNGvqvKlkwHxjNguFQfimQo6Abwk0OF4COCSk2BJku90B%2BkgRzvZCNDTRS19CqwjxvbRucA6nUSSfs7ecVndHYGXEKf%2B20%2B9N5NjMa5L1pi1ocnmcyQwYvYbEHbgmGjVy8q72sbbooOuTU9ohWpDGDmYKQSQ0a5uCm3NmylRO%2BA25ilYeDMMOiO%2BfZdSIsRxp%2FRR2jSN25Rm9bR%2By0ZF9BRj3QrK0G5YVfKqfIi0t5tky5j2O4opge%2BdMOfbj6ohwOm1zusYHzsOZTXPIoxM6%2B4tkIkLISMJS3%2F9IGOqUBrwDm%2B0%2FamKpQUsoNSi3rdm949p99UpMl5Pa9Kg4fwNWZ1rJwA96jcIPJq5d3MwIkkNhD9y7sIkYd1ZISYRgsjC2YnPcxO9TsVGqOShekwKarofY%2FsVka5EkSfdnOHHf2rS2K36Hj%2FSpIV5rmhwMYJ06KvqZmElmaOdywmUEpzpBJkIUh1BAzYukYOMhLU06ocMDFAkk118gNeD2RGCYtAONJoOOg&X-Amz-Signature=772bf775c74b07fb8481a0bb86e9852bbb33abe542421f817227f560fad7e5dd&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/9ea5f164-425d-408c-a130-0b09dc3f48a6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667OU56QUW%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQClPAvi8f6ymRxwS4tpXsmmyr66MHVbsb%2B%2FF6yoYwDAggIgWG6ocYg5aYi0jresbzwUqSt7l%2F%2B8tUdyiHM4wsdxg6sqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLpjDSQ9AhqzQVSfzCrcA9FxMM34h1Q4Pe1BiTrYSJOnQ%2BpfCKdLu2YrkhsCS%2B0WsQkEKxPsoGOTIFkd%2BuTgE7adr%2BDBPcG5Kv4kAiX5CHfLwh45jXUF02KIWJ9piNBjEAgkvxuspfKCevHRrMNstK4izXPOB0oPReayTBSSFBb2sCFvSZp%2BqAsILI8Ogvoq3lBf4LycGS8f2jqGPXiuGS2we91KtePS0%2BDomoDE25jRS8TjYJthuoitmmB4en2VeuRZrBkj0qVWpGvZuzLdyaIPdUzzmWVY5i5RUsgYJOnzgGjr2ejfUWsmdHqvLq5yHBwxq7BIg9ZgbZsvYRHVuTIuvo%2F5eY%2Fi%2BSjh5TiEJ2c6K%2FIHowqNGvqvKlkwHxjNguFQfimQo6Abwk0OF4COCSk2BJku90B%2BkgRzvZCNDTRS19CqwjxvbRucA6nUSSfs7ecVndHYGXEKf%2B20%2B9N5NjMa5L1pi1ocnmcyQwYvYbEHbgmGjVy8q72sbbooOuTU9ohWpDGDmYKQSQ0a5uCm3NmylRO%2BA25ilYeDMMOiO%2BfZdSIsRxp%2FRR2jSN25Rm9bR%2By0ZF9BRj3QrK0G5YVfKqfIi0t5tky5j2O4opge%2BdMOfbj6ohwOm1zusYHzsOZTXPIoxM6%2B4tkIkLISMJS3%2F9IGOqUBrwDm%2B0%2FamKpQUsoNSi3rdm949p99UpMl5Pa9Kg4fwNWZ1rJwA96jcIPJq5d3MwIkkNhD9y7sIkYd1ZISYRgsjC2YnPcxO9TsVGqOShekwKarofY%2FsVka5EkSfdnOHHf2rS2K36Hj%2FSpIV5rmhwMYJ06KvqZmElmaOdywmUEpzpBJkIUh1BAzYukYOMhLU06ocMDFAkk118gNeD2RGCYtAONJoOOg&X-Amz-Signature=bf0f8320f7d211d8ff896c4cc723a702f54a61fd23a9ac0e663aef5f3449cc03&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[file](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/9445fc1e-ea80-46d1-8e4c-791c63e4a0d3/rule.xml?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667OU56QUW%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225410Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQClPAvi8f6ymRxwS4tpXsmmyr66MHVbsb%2B%2FF6yoYwDAggIgWG6ocYg5aYi0jresbzwUqSt7l%2F%2B8tUdyiHM4wsdxg6sqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLpjDSQ9AhqzQVSfzCrcA9FxMM34h1Q4Pe1BiTrYSJOnQ%2BpfCKdLu2YrkhsCS%2B0WsQkEKxPsoGOTIFkd%2BuTgE7adr%2BDBPcG5Kv4kAiX5CHfLwh45jXUF02KIWJ9piNBjEAgkvxuspfKCevHRrMNstK4izXPOB0oPReayTBSSFBb2sCFvSZp%2BqAsILI8Ogvoq3lBf4LycGS8f2jqGPXiuGS2we91KtePS0%2BDomoDE25jRS8TjYJthuoitmmB4en2VeuRZrBkj0qVWpGvZuzLdyaIPdUzzmWVY5i5RUsgYJOnzgGjr2ejfUWsmdHqvLq5yHBwxq7BIg9ZgbZsvYRHVuTIuvo%2F5eY%2Fi%2BSjh5TiEJ2c6K%2FIHowqNGvqvKlkwHxjNguFQfimQo6Abwk0OF4COCSk2BJku90B%2BkgRzvZCNDTRS19CqwjxvbRucA6nUSSfs7ecVndHYGXEKf%2B20%2B9N5NjMa5L1pi1ocnmcyQwYvYbEHbgmGjVy8q72sbbooOuTU9ohWpDGDmYKQSQ0a5uCm3NmylRO%2BA25ilYeDMMOiO%2BfZdSIsRxp%2FRR2jSN25Rm9bR%2By0ZF9BRj3QrK0G5YVfKqfIi0t5tky5j2O4opge%2BdMOfbj6ohwOm1zusYHzsOZTXPIoxM6%2B4tkIkLISMJS3%2F9IGOqUBrwDm%2B0%2FamKpQUsoNSi3rdm949p99UpMl5Pa9Kg4fwNWZ1rJwA96jcIPJq5d3MwIkkNhD9y7sIkYd1ZISYRgsjC2YnPcxO9TsVGqOShekwKarofY%2FsVka5EkSfdnOHHf2rS2K36Hj%2FSpIV5rmhwMYJ06KvqZmElmaOdywmUEpzpBJkIUh1BAzYukYOMhLU06ocMDFAkk118gNeD2RGCYtAONJoOOg&X-Amz-Signature=e01dc0b7a57d7209226242254f3327b7290a292d2ffe7ab18993fa1e0fc9d1e9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

```javascript
<?xml version="1.0" encoding="UTF-8"?>
<!-- - - Licensed under the Apache License, Version 2.0 (the "License"); 
	- you may not use this file except in compliance with the License. - You 
	may obtain a copy of the License at - - http://www.apache.org/licenses/LICENSE-2.0 
	- - Unless required by applicable law or agreed to in writing, software - 
	distributed under the License is distributed on an "AS IS" BASIS, - WITHOUT 
	WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. - See the 
	License for the specific language governing permissions and - limitations 
	under the License. -->
<!DOCTYPE mycat:rule SYSTEM "rule.dtd">
<mycat:rule xmlns:mycat="http://io.mycat/">
	<tableRule name="rule1">
		<rule>
			<columns>id</columns>
			<algorithm>func1</algorithm>
		</rule>
	</tableRule>

	<tableRule name="sharding-by-date">
		<rule>
			<columns>createTime</columns>
			<algorithm>partbyday</algorithm>
		</rule>
	</tableRule>

	<tableRule name="rule2">
		<rule>
			<columns>user_id</columns>
			<algorithm>func1</algorithm>
		</rule>
	</tableRule>

	<tableRule name="sharding-by-intfile">
		<rule>
			<columns>sharding_id</columns>
			<algorithm>hash-int</algorithm>
		</rule>
	</tableRule>
	<tableRule name="auto-sharding-long">
		<rule>
			<columns>id</columns>
			<algorithm>rang-long</algorithm>
		</rule>
	</tableRule>
	<tableRule name="mod-long">
		<rule>
			<columns>id</columns>
			<algorithm>mod-long</algorithm>
		</rule>
	</tableRule>
	<tableRule name="sharding-by-murmur">
		<rule>
			<columns>id</columns>
			<algorithm>murmur</algorithm>
		</rule>
	</tableRule>
	<tableRule name="crc32slot">
		<rule>
			<columns>id</columns>
			<algorithm>crc32slot</algorithm>
		</rule>
	</tableRule>
	<tableRule name="sharding-by-month">
		<rule>
			<columns>create_time</columns>
			<algorithm>partbymonth</algorithm>
		</rule>
	</tableRule>
	<tableRule name="latest-month-calldate">
		<rule>
			<columns>calldate</columns>
			<algorithm>latestMonth</algorithm>
		</rule>
	</tableRule>

	<tableRule name="auto-sharding-rang-mod">
		<rule>
			<columns>id</columns>
			<algorithm>rang-mod</algorithm>
		</rule>
	</tableRule>

	<tableRule name="jch">
		<rule>
			<columns>id</columns>
			<algorithm>jump-consistent-hash</algorithm>
		</rule>
	</tableRule>

	<function name="murmur"
			  class="io.mycat.route.function.PartitionByMurmurHash">
		<property name="seed">0</property><!-- 默认是0 -->
		<property name="count">2</property><!-- 要分片的数据库节点数量，必须指定，否则没法分片 -->
		<property name="virtualBucketTimes">160</property><!-- 一个实际的数据库节点被映射为这么多虚拟节点，默认是160倍，也就是虚拟节点数是物理节点数的160倍 -->
		<!-- <property name="weightMapFile">weightMapFile</property> 节点的权重，没有指定权重的节点默认是1。以properties文件的格式填写，以从0开始到count-1的整数值也就是节点索引为key，以节点权重值为值。所有权重值必须是正整数，否则以1代替 -->
		<!-- <property name="bucketMapPath">/etc/mycat/bucketMapPath</property>
			用于测试时观察各物理节点与虚拟节点的分布情况，如果指定了这个属性，会把虚拟节点的murmur hash值与物理节点的映射按行输出到这个文件，没有默认值，如果不指定，就不会输出任何东西 -->
	</function>

	<function name="crc32slot"
			  class="io.mycat.route.function.PartitionByCRC32PreSlot">
		<property name="count">2</property><!-- 要分片的数据库节点数量，必须指定，否则没法分片 -->
	</function>
	<function name="hash-int"
			  class="io.mycat.route.function.PartitionByFileMap">
		<property name="mapFile">partition-hash-int.txt</property>
	</function>
	<function name="rang-long"
			  class="io.mycat.route.function.AutoPartitionByLong">
		<property name="mapFile">autopartition-long.txt</property>
	</function>
	<function name="mod-long" class="io.mycat.route.function.PartitionByMod">
		<!-- how many data nodes -->
		<property name="count">3</property>
	</function>

	<function name="func1" class="io.mycat.route.function.PartitionByLong">
		<property name="partitionCount">8</property>
		<property name="partitionLength">128</property>
	</function>
	<function name="latestMonth"
			  class="io.mycat.route.function.LatestMonthPartion">
		<property name="splitOneDay">24</property>
	</function>
	<function name="partbymonth"
			  class="io.mycat.route.function.PartitionByMonth">
		<property name="dateFormat">yyyy-MM-dd</property>
		<property name="sBeginDate">2015-01-01</property>
	</function>


	<function name="partbyday"
			  class="io.mycat.route.function.PartitionByDate">
		<property name="dateFormat">yyyy-MM-dd</property>
		<property name="sNaturalDay">0</property>
		<property name="sBeginDate">2014-01-01</property>
		<property name="sEndDate">2014-01-31</property>
		<property name="sPartionDay">10</property>
	</function>

	<function name="rang-mod" class="io.mycat.route.function.PartitionByRangeMod">
		<property name="mapFile">partition-range-mod.txt</property>
	</function>

	<function name="jump-consistent-hash" class="io.mycat.route.function.PartitionByJumpConsistentHash">
		<property name="totalBuckets">3</property>
	</function>
</mycat:rule>
```

大家好，咱们继续讲这个买 cat 配置文件里边的内容。这节课主要给大家介绍这个和分片表相关的一个非常重要的属性，就是这个弱属弱属性它定义了分片表的分片规则，这个分片规则必须与你的弱点叉 ML 里边的这个 table 弱标签要对应起来。这个咱们先看一下咱们还是回到 130 买 cat 这台服务器130。然后咱们进入到买 cat 的目录，买 cat 是吧，进入到抗伏目录，然后看一下 schema 的叉 ML 这里边咱们看一下 table 这个标签。 table 这个标签它标志着你的一张分片表咱们设置的是 user 然后它有两个分片节点，分别是 DN 131 和 DN 132。


接下来看一下的，它的规则凹凸沙丁浪这个规则去哪里找？咱们看一下，它是从这个弱点叉 L 里边弱点叉 ML 里边分为两段配置，第一段就是这个 table 弱，它可以看到都有一个内幕属性，咱们刚才那个弱就要和这个 table 弱对应起来，咱们刚才配置的是凹凸沙鲸浪这个 table 弱对吧。所以它的一些规则都要从这个凹凸沙鲸浪这个 table 弱里边去找。


大家接着往下看。这里边分别有两个标签，一个是 column 它标志着你的分片的列你按照哪一列去分片，咱们这里边标志的是 ID 咱们前面也给大家做了演示，如果你的 ID 小于 500 万的话，它会分配到第一个数据节点上。如果在 500 万到 1000 万之间要分配到第二个节点上。那有的同学可能会问了，如果你的这个 ID 大于 1000 万，那怎么办？由于它的这个配置文件里边没有标注大于 1000 万，要分配到哪个数据节点。所以如果大于 1000 万的话，系统会报错了。


这里边分片的列是 ID 分片的逻辑标签是这个润之乱，润之乱，咱们怎么去找？再往下看，前面的这一段都是 table rule 的标签，后面就会有它的翻看人标签。翻看人标签主要是对应它的分片逻辑。咱们找到刚才写的这个润植 run 就在这里边。润植 run 里边有一个属性 class 它标志了这个分片规则的实现类。如果大家看这个 my cat 的源码，可以找到这个凹凸 partition 摆浪这个类，它里边描述了如何去进行这个范围的分片。然后它里边还有一个属性叫做 map file 它的映射的文件就是这个 auto partition 了。


这个咱们再看一下，它的范围其实都在这个凹凸 party 山杠这个文件当中，大家可以看到前面的注释范围的开始和结束。然后后面是 data note 的这个 index 然后还标注了一下 K 是多少，然后 M 是多少。这块咱们配置的是 0 到 500 万，它在第一个这个数据节点，然后 500 万到 1000 万在这个第二个数据节点。所以它就是一个范围的这么一个分片的规则，咱们先退出来。它的这个分片规则有很多买 K 的为咱们提供的这个分片规则，咱们怎么去找？其实都在它的使用文档里边，有说明咱们来看一下。


打开这个买 cat 的使用文档到第 10 章 my cat 的分片规则。下面有一个 my cat 常用的分片规则对吧。 my cat 常用的分片规则里边咱们看看有多少种从分片枚举开始。然后你知道自然月分片有很多种都已经给咱们实现好了。其中第一个就是这个分片枚举通过在配置文件中配置可能的枚举 ID 自己配置分片。本规则适用于特殊的场景，比如说有些业务需要按照省市区来保存，而全国的这个省市区县是固定的。所以使用这种分片规则的配置如下是吧。那么看到它的这个 table rule 叫做沙丁 by in the file 也是配置了一个分片的列。然后分片的规则配置的是哈希 int 哈希 int 里边咱们看看有配置了什么东西。首先是一个 function 标签，然后是它的类实现，在里边标注了它对应的文件对应的这么一个 tst 文件，咱们一会着重来看一下这个 tst 文件。然后 type 类型是0， default node 是0，这两个什么意思？咱们继续往下看。


我们看到这段， type 的默认值是0，0表示 intake 是一个数字型的。如果非 0 表示 string 也就是说你的分片的列它是什么类型的，一般的情况下都是数字类型，所有的节点都从 0 开始，0代表着第一个节点，咱们来看看这个 default default node default node 是默认节点，小于 0 表示不设置默认节点，如果大于 0 就表示设置默认节点。


这回咱们来看那个 tst 文件大家可以看到配置了三段，第一段 1 万是在第零个节点，如果是10,010，它是在第一个节点，然后默认的节点是 1 咱们说一下这个用法，咱们从这名字就可以看出，你的这个分片的这些列是一些固定的值，你只有分片的这些列是一些固定的值，我才可以用分片枚举。


枚举什么意思啊？就是有一些固定的值对吧？分片的这些列在这些值当中，像这种他用了 user ID user ID 一般咱们会用自增的，如果要是自增的话，就不适合你用分片枚举了。比如说我有 1 万个用户，那我这个 ucid 肯定是 1 万个值对吧？那你 1 万个值我这个 tst 文件里边要配置成什么样？是不是要配置成 1 万个以后每增加一些用户，我是不是在这里边我都要配置？所以对一些自增的这些列是不适合用分片枚举的。就像他描述的这样，比如说按照省市区，省市区一般不会变化，就那么几个值，咱们都把这些省市区都给它配置到这个 tst 文件当中。如果你的这条记录是哪个省的，我会在这个 tic 文件当中找到你对应的分片，这样就可以了。


好，下面咱们给大家演示一下分片枚举，咱们还是进入到 130 这台机器进入到 schema schema 咱们先把之前的这一段给它处理掉，怎么把这个 m2 这个已经给它注释掉了，因为咱们现在 130 这台机器上也有一个 MySQL 并且和 1311 是一个主从的关系。


所以这块咱们改一下这个配置，把这个 read host 写进来，这个都是上节课的内容了，咱们也是快速的回顾一下，host等于S1， URL 等于一九二点一六八点七三点一三零，user等于慕课， passport 等于慕课艾特 123456 这样是不是就可以了？然后咱们再改一下上面的这个表。 user 这张表咱们只有两个字段是吧，一个是 ID 一个是 username 然后给它再加一列，咱们用这列作为这个分片枚举是吧。什么呢？这块这个弱要给它改一下变成什么，咱看一下这个文档，改成 shutting by in the file 好，这样就可以了。然后咱们保存一下，再看一下弱点叉 ML 弱点叉 ML 找到沙丁 by int file 这一段它的分片的列，咱们给它指定一下，给它改一下叫做什么呢？叫做 province 杠 ID province 杠 ID 然后他的逻辑哈希 int 往下找，找到 function function 里边哈希 int 它对应的文件 partition 哈希 int.tst 咱们给它保存一下。提神哈希这里边配了两个值，一个是10,010。对吧，这块咱们就不动了，一会咱们这个 province ID 就差这两个值。如果你差多了怎么办？咱们看一下这文档，写一个 default node 对吧，默认的这个节点 default node 等于咱们默认到第零个节点，保存一下。


好，所有的配置文件咱们都配置完了怎么了？买 cat 给它启动一下，用console ，咱们看到报错了是吧，看看报道什么错越界。然后他是在创建 DB host 的时候报错了是吧，咱们再看一下，看一下 schema.xml DB host 这块这块咱们忘了写端口号了，咱们给它补上 3306 对吧，保存一下，这回咱们再启动一下卖 Kite 康。 so 咱们来看看他还报不报错没有问题了是吧。启动成功了。然后咱们进入到 navicate 连接一下买开的这个服务。咱们要在这右侧表里边增加一个字段是吧。之前咱们都是在具体的这个数据库当中去增加的字段，创建表创建字段都是在 131 和 132 这个实体的数据库当中。现在咱们增加字段，咱们试一下，直接在这个 my cat 里边去增加字段，看看三个实体的数据库是不是也相应的增加字段了。咱们点设计表添加一列是吧。


这一列是 province ID 省的 ID 对吧，印咱们也给他来个 11 位加个注释，省 ID 保存一下，看看能不能保存没有问题是吧，咱们连接的是买 cat 通过买 cat 直接给这个右侧表增加个字段。然后咱们再分别看一下 131 和132，看看 131 刷新一下好，131这个数据库 promise ID 已经增加好了，咱们再看一下132，132也没有问题对吧，再看一下这个背库，131的这个从库 130 对吧，刷新一下也没有问题可以看到。如果大家创建表创建好以后，咱们可以通过 my cat 直接去修改这些表，你买开的修改了这些表了，它会同步到你所有的这个 data node 上，现在这个 province ID 咱们也已经创建好了，然后咱们插一条记录试试。这个 province ID 它插入的是一个枚举值，就是咱们之前在这里面配置的，咱们来复制一个。这个枚举值只能有两个，一个，一个是10,010。咱们来看一下。进入到买 cat 康复里边，看一下这个弱点叉 L 里边对应的塔踢山哈希 int 对吧。希山哈希 int 配置了两个，一个是 1 万，一个是10,010，咱们先插一个 1 万的数据进入到 130 对吧，咱们把这窗口先关一下，先听到 130 对吧。金色塔 intouser 第一个 ID 然后 username province ID 后边 values 现在它的分片和 ID 就没有关系了对吧，咱们 ID 可以随便的取值，随便写一个值。然后 u3 类目咱们叫做北京，然后这个值 province ID 咱们写一个 1 万插入一下。


好没有问题是吧，这边咱们再刷新一下数据，1万这条数据已经查询出来了。那么它在哪一个真实的数据库当中呢？咱们看一下，看看是在 131 还是在132。那么先看131，看到这块已经出来了，在 131 的这个数据库下面咱们再改一下，咱们再改一个上海，这个给他传一个10,010，再运行一下，也插入了一条数据对吧，这个总的买菜的，那么刷新一下没问题。这个咱们看看在 131 还是在132。先刷新一下 131 吧。 131 没有对吧，咱们再打开132，可以看到这条数据在 132 里，这个 province ID 是10,010。那么这个时候如果我们插入了一条数据，它的 ID 既也不是10,010，那么会怎么办呢？这么改一下，改成广州，差了一个 10,110 是吧，它不是一个咱们规定的枚举式。


那么按照咱们的配置文件，它默认会插在数据库 0 当中。这个数据库 0 也就是咱们的 DB 131 对吧，大家可以看到这块写了看到的 found user 然后 province ID 一百零一十，看来是插不进去的对吧。咱们虽然写了这个 default node 咱们来看一下这个配置文件，看看哪块没配置。对，这个 tse 文件咱们已经配置了 default note 等于 0 是吧，默认是在第一个数据节点上，怎么了再退出，再看一下弱点叉 ML 弱点叉 L 这里边只配置了一个 map file 对吧。其实按照这个文档当中，这个 function 里边咱们还要再配置两个属性，一个是 type 一个是 default node 这个 depot note 是什么意思啊？这个 depot note 是标志着你是否开启了默认的配置。
这个 depot note 小于 0 表示不设置默认节点对吧？大于等于 0 表示设置默认节点。但是咱们这里边并没有配置是吧，咱们给这个 default node 给它复制一下，然后粘贴到这里边来。只要配置它等于零，是不是也是表示设置了默认节点？这样如果你发现不在枚举值里边的这些结果，都会给它分配到默认节点。


默认节点咱们设置的是第一个节点对吧。好，修改完配置文件以后，咱们要刷新一下配置，进入到这个买 cat 的管理端口。管理端口咱们要打开命令行刷新配置了，这个命令大家一定要记住。 reload 对吧。 reload config oh 对吧，进行一下。 OK 刷新完成了。


下面咱们再插这么一条记录，这个是吧，插入了一个不在配置文件里边的这么一个枚举值，运行一下，这个也已经插入成功了是吧，咱们配置的是默认把它插到第一个数据节点也是131，咱们刷新一下 131 看到没有问题了对吧。好，这个枚举分片就先给大家介绍到这，然后咱们还会给大家介绍另外一个比较常用的这个分片规则，就是曲膜，这个咱们在下一节会给大家讲解。



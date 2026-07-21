---
title: 1-15 项目管理-项目成本管理-2（1749）
---

# 1-15 项目管理-项目成本管理-2（1749）

那我们看一个练习题，有一个开发项目计划用 10 天搞定，花1万块钱完成 20 个接口开发，当这个项目进行到第六天结束的时候，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/16e5e916-86fc-4f5f-bc8c-c97f6ae0cd91/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RF7MLU4N%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFY7urbhhuCspp3gGwcKTgbb9n%2FXyYzkojvQJcVwrCgDAiBHDlf9GaX%2FL04m0vP99P5yUEMfN3RCIGoluUgb874aVCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMKMaEEcmDRTC0bUo5KtwDyDsI0AFYlu1iirCyCjQTX8wJn1Y7BDhfpMMIAoQxBEQ8AcJoY%2Fm9W335iAM7zSpNlKgqkzOSvH25uhLH%2BLLJunnBH3gXF%2FKwLc7MuIQpgaAdvXGfVxxBvfWuJ7f6UoEeUMpkrH%2FzFhaPBQTe8GetYNB677Uj9YMbPOm9YDZ8q9OgsleuUovGnLRsN9qs6MbDQqKbND3ew9hzIuKK1ZfJjR3bpaVifQdAi%2FUsaaE%2B%2FjHBdRbLJm8EbtNYKdQya4wDoLfjlrx7MhdVPQsbXNYvWJeQBkJKqTeM%2B6Gbf%2B8QYNvK4lMYvl2iJ%2Bu3QZT1R1OZ7bdIWILE3Q4hNu5CpTshDt7OWJWhEyS2G4flUGRv2R%2FyJ6MuonQBlctASS6CwLzCbq0NYNerFE26uHjICilpDQ2ZJMlyMIZ0zBWdMZKBzE4kV5L2xASI%2F9%2BvrRYHh%2FO58fjWjES1v1TbfL7wqzxO0p0By4fdV8d%2B4Ox7F6KDhQ4Kql89gMxuyJXpanOE6EUMJr7XPFDFZaRGI7pZKSi25M8VNYklEjlARq%2F7F8VEAfrzbHlgcdv%2FHKSpI5NBjyZKBib58ZGTq9aNm2%2F9%2B3ul2WqEGetCXDVsEGLfem1X0rJGe2x8YvaRef8D6%2F0ws7r%2F0gY6pgGRDcKGx4ZJa%2BpRWvCZfBXx3neSstuC55ezr%2BngU61quD%2FC9AEZPc7jRfKFN94%2BBbtW%2FsPefpnPmaq4jQnBFXv0hu%2F2%2ByuNasIQ7uscm56eISTCnUp9IqzMkI7LkqUp5g6Ay4O0QmEwPyxurbyZA7dT0gaIBnhs3tmFLuF9l5hQsadHhXSkbgo8SBamPrNPFAytr7tehEQIdH4uclSu0E1Aq6Vm9i9v&X-Amz-Signature=26b7325e328e73b55087c1782514dba16dacb5d0fb7e893f1d191e2dfc457295&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

已经完成了 15 个接口，但是预算就只剩下 1000 块了。那我们当前这个开发项目这个绩效水平是什么样的？绩效水平我们就看两个，一个是成本，一个是进度。


那我们看一下那这个题要怎么算？这个不仅仅是一个计算题，这个在我们实际工作中也非常有用，我们可以去拿现实的一些项目去计算一下，大概对这个项目也就有所了解，整个的一个趋势和它的健康状态也会非常了解，而且这个非常好量化。首先完工预算b、 a C 就是指这个项目计划用 10 天花1万块，所以它就是1万，我要完成这个工作要花多少钱？那 EV 比较好理解，也就是说当前的一个正值。因为我们计划是用1万块开发 20 个接口，所以我们每个接口平均下来就是 500 块，用1万除以20，我们假设每个接口的工作量是一样的，成本也是一样的，所以这个项目的正值只和这个项目目前已经开发的接口数有关，和花费的时间、实际的花费都没有关系。所以正值也仅仅是和结果相关。


那我们这个项目里边就是说开发了这 15 个接口，所以 EV 就等于1万 /20，算出每个接口的一个值乘以15，这个就得到当前这个阶段开发完 15 个接口的一个正值是 7500 块。那然后说一下PV， PV 是计划价值，它只和时间有关，和我们现在项目的进度有关。那我们这个项目的开发计划是要用 10 天开发出 20 个接口，我们还是这 20 个接口工作量是一样的，可以均匀下来。所以如果按照这个逻辑， 10 天开发 20 个，每天要开发两个接口，第一天 PV 就等于两个接口的一个价值。进度是开发到第六天结束正好是 6 天，还有7890，还有 4 天，前边付出了 6 天，所以 PV 就等于6，除以 10 再乘以1万就等于6000，整体这个进度和开发已经完成了多少个接口是没有关系的。


那因为它是只和进度有关，所以到最后一天这个 PV 应该和b、 a C 相等，因为他不考虑具体开发了多少个接口，那我们再看一下这个项目实际花费的多少钱，因为只剩 1000 块了，所以他实际花了 9000 块钱，这个就是实际开销，和我们开发的接口数，还有这个项目经营的时间都没有关系。就是花了多少钱，指描述在第六天结束的时候，我剩 1000 块，所以我花了 9000 块。接下来就比较有趣了，可以算了。


我们再回顾一下b、 a C，也就是说完成这个项目要花的钱计划是1万块，所以它等于1万EV。这个正值在当前结束的时候，已经开发完成了 15 个接口，一共是 20 个，所以计划花费1万块，所以每个接口是1万除以20，但是完成了 15 个，所以乘以 15 等于 7500 EV，表示已经完成的 PV 只看进度。当前第六天一共花 10 天，所以 6 除以 10 再乘以1万块，等于 6000 AC，实际会花费计划花1万，现在剩1000，所以花9000。这些参数都拿到之后，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/ea50642c-7182-43e0-b140-52af19b7d158/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RF7MLU4N%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFY7urbhhuCspp3gGwcKTgbb9n%2FXyYzkojvQJcVwrCgDAiBHDlf9GaX%2FL04m0vP99P5yUEMfN3RCIGoluUgb874aVCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMKMaEEcmDRTC0bUo5KtwDyDsI0AFYlu1iirCyCjQTX8wJn1Y7BDhfpMMIAoQxBEQ8AcJoY%2Fm9W335iAM7zSpNlKgqkzOSvH25uhLH%2BLLJunnBH3gXF%2FKwLc7MuIQpgaAdvXGfVxxBvfWuJ7f6UoEeUMpkrH%2FzFhaPBQTe8GetYNB677Uj9YMbPOm9YDZ8q9OgsleuUovGnLRsN9qs6MbDQqKbND3ew9hzIuKK1ZfJjR3bpaVifQdAi%2FUsaaE%2B%2FjHBdRbLJm8EbtNYKdQya4wDoLfjlrx7MhdVPQsbXNYvWJeQBkJKqTeM%2B6Gbf%2B8QYNvK4lMYvl2iJ%2Bu3QZT1R1OZ7bdIWILE3Q4hNu5CpTshDt7OWJWhEyS2G4flUGRv2R%2FyJ6MuonQBlctASS6CwLzCbq0NYNerFE26uHjICilpDQ2ZJMlyMIZ0zBWdMZKBzE4kV5L2xASI%2F9%2BvrRYHh%2FO58fjWjES1v1TbfL7wqzxO0p0By4fdV8d%2B4Ox7F6KDhQ4Kql89gMxuyJXpanOE6EUMJr7XPFDFZaRGI7pZKSi25M8VNYklEjlARq%2F7F8VEAfrzbHlgcdv%2FHKSpI5NBjyZKBib58ZGTq9aNm2%2F9%2B3ul2WqEGetCXDVsEGLfem1X0rJGe2x8YvaRef8D6%2F0ws7r%2F0gY6pgGRDcKGx4ZJa%2BpRWvCZfBXx3neSstuC55ezr%2BngU61quD%2FC9AEZPc7jRfKFN94%2BBbtW%2FsPefpnPmaq4jQnBFXv0hu%2F2%2ByuNasIQ7uscm56eISTCnUp9IqzMkI7LkqUp5g6Ay4O0QmEwPyxurbyZA7dT0gaIBnhs3tmFLuF9l5hQsadHhXSkbgo8SBamPrNPFAytr7tehEQIdH4uclSu0E1Aq6Vm9i9v&X-Amz-Signature=769dd1af48a465cc2ec7fa5afbfb12a5a8576df02b155b2b551790ffd80c06f2&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

我们就可以计算了，比较有意思。


看一下 SV 进度偏差等于 EV 减PV，所以就等于7500，减去 6000 等于1500，它是大于 0 的。大于 0 代表什么呢？进度超前了。也就是说正常这个进度来讲，到第六天不需要完成 15 个接口，但是现在已经完成 15 个接口了，说明这个进度已经超前了，那它大于 0 代表进度超前，小于 0 代表进度延后。


再看一下 SPI 等于 EV 除以 PV 等于 7500 / 6000，大于1，这个也是代表进度超前，那 SPI 就是把这个减号变成一个除号， SV 是一个数值，是一个绝对值，看不出来这个趋势和比例。 SPI 就能看出来 SPI 算出来的值，例如说 7500 / 6000，这个值和一的差的绝对值就代表了这个偏差的一个程度，在这个案例里边就代表提前的一个程度。然后我们看一下成本， CV 等于EV，减 AC 就等于 7500 - 9000 等于负的1500，小于 0 意味就是实际在当前完成的一个工作， AC 实际花费这里边我们一共花了 9000 块， AC 实际只干了 7500 块的活，所以小于 0 代表这个成本已经超支了。


SPI 是一样的，用 EV 除以 AC 等于 0. 833，小于一，它也代表这个成本已经超支了。所以当前这个项目在第六天结束的时候，它我们可以给出结论，进度提前了，但是成本超支了。那希望小伙伴们通过这个正直管理实战，能从更宏观的项目管理角度来理解这个项目当前的成本绩效是什么情况，当前的进度绩效是什么情况？对于我们控制这个项目，可以辅助我们更好的完成项目目标。那么继续结论，刚才已经说了进度提前了，成本超支了。


那我们分析一下这个参数在实际项目的可能的一些情况。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/6c3b8d19-947d-4bc2-b366-feb93b53f28b/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RF7MLU4N%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFY7urbhhuCspp3gGwcKTgbb9n%2FXyYzkojvQJcVwrCgDAiBHDlf9GaX%2FL04m0vP99P5yUEMfN3RCIGoluUgb874aVCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMKMaEEcmDRTC0bUo5KtwDyDsI0AFYlu1iirCyCjQTX8wJn1Y7BDhfpMMIAoQxBEQ8AcJoY%2Fm9W335iAM7zSpNlKgqkzOSvH25uhLH%2BLLJunnBH3gXF%2FKwLc7MuIQpgaAdvXGfVxxBvfWuJ7f6UoEeUMpkrH%2FzFhaPBQTe8GetYNB677Uj9YMbPOm9YDZ8q9OgsleuUovGnLRsN9qs6MbDQqKbND3ew9hzIuKK1ZfJjR3bpaVifQdAi%2FUsaaE%2B%2FjHBdRbLJm8EbtNYKdQya4wDoLfjlrx7MhdVPQsbXNYvWJeQBkJKqTeM%2B6Gbf%2B8QYNvK4lMYvl2iJ%2Bu3QZT1R1OZ7bdIWILE3Q4hNu5CpTshDt7OWJWhEyS2G4flUGRv2R%2FyJ6MuonQBlctASS6CwLzCbq0NYNerFE26uHjICilpDQ2ZJMlyMIZ0zBWdMZKBzE4kV5L2xASI%2F9%2BvrRYHh%2FO58fjWjES1v1TbfL7wqzxO0p0By4fdV8d%2B4Ox7F6KDhQ4Kql89gMxuyJXpanOE6EUMJr7XPFDFZaRGI7pZKSi25M8VNYklEjlARq%2F7F8VEAfrzbHlgcdv%2FHKSpI5NBjyZKBib58ZGTq9aNm2%2F9%2B3ul2WqEGetCXDVsEGLfem1X0rJGe2x8YvaRef8D6%2F0ws7r%2F0gY6pgGRDcKGx4ZJa%2BpRWvCZfBXx3neSstuC55ezr%2BngU61quD%2FC9AEZPc7jRfKFN94%2BBbtW%2FsPefpnPmaq4jQnBFXv0hu%2F2%2ByuNasIQ7uscm56eISTCnUp9IqzMkI7LkqUp5g6Ay4O0QmEwPyxurbyZA7dT0gaIBnhs3tmFLuF9l5hQsadHhXSkbgo8SBamPrNPFAytr7tehEQIdH4uclSu0E1Aq6Vm9i9v&X-Amz-Signature=38bb18eb450f8b20b7310cc81d10c2904eab8e66bc7098aef2d942e9985e7158&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

首先看第一个 a C 大于 PV 大于EV，那利用公式就可以发现 SV 小于0， CV 小于0，那这种情况就是效率低，进度慢，投入超前了，因为这里边实际花费是最大的。那我们要采取哪些项目管理措施，很明显，这里边效率比较低，我们可以用工作效率高的人员来替换工作效率低的人员，来优化目前的这几个指标。


那第二种情况就是 PV 更大了， PV 大于 AC 大于EV，那同样的 SV 还是会小于 0 CV 也会小于0，它反映的是什么呢？效率较低，进度慢，投入延后了，因为 PV 大于AC，所以这个也会造成一定的差异。这个解决方案也是一样的，这里边不仅仅可能是开发，也可能是项目施工人员，也有可能是具体的提效的一些方案。


还有一种情况， EV 最大于 PV 大于AC， SV 会大于 0 CV 大于0，这个反映出来的就是进度比较快，投入延后了，效率比较高，目前看问题不大，进行持续的监控就可以了。还有一种情况， EV 大于 AC 大于PV， SV 大于 0 CV 大于0，反应出来的就是效率比较高，进度快，投入超前了。这个投入超前和延后，就看 PV 和 AC 的大小关系就可以。还有一种情况， AC 大于 EV 大于PV，算出来 SV 大于0， CV 小于0，它代表效率较低，进度比较快，投入超前。


第五个和第四个采取的方式可能都是说进度可以放缓一下，再考虑一下成本的一个问题。第六种可能就是 PV 大于 EV 大于AC， SV 小于0， CV 大于零，表现就是效率比较高，进度缓慢，投入延后。那这种情况我们可以增加人员的一个投入，这些投入都是成本成本投入，一个是成本投入超前了，一个是成本投入延后了。对于当前这个项目的一个现状，通过正值管理能计算出来目前的一个状态预测来讲，它也能起着至关重要的一个作用。


看一下预测技术里边主要是这几个参数，完工预算e、 a C。也就是说随着项目进展，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/8355d844-0900-4f23-9801-3fb57a75ca64/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RF7MLU4N%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232249Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFY7urbhhuCspp3gGwcKTgbb9n%2FXyYzkojvQJcVwrCgDAiBHDlf9GaX%2FL04m0vP99P5yUEMfN3RCIGoluUgb874aVCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMKMaEEcmDRTC0bUo5KtwDyDsI0AFYlu1iirCyCjQTX8wJn1Y7BDhfpMMIAoQxBEQ8AcJoY%2Fm9W335iAM7zSpNlKgqkzOSvH25uhLH%2BLLJunnBH3gXF%2FKwLc7MuIQpgaAdvXGfVxxBvfWuJ7f6UoEeUMpkrH%2FzFhaPBQTe8GetYNB677Uj9YMbPOm9YDZ8q9OgsleuUovGnLRsN9qs6MbDQqKbND3ew9hzIuKK1ZfJjR3bpaVifQdAi%2FUsaaE%2B%2FjHBdRbLJm8EbtNYKdQya4wDoLfjlrx7MhdVPQsbXNYvWJeQBkJKqTeM%2B6Gbf%2B8QYNvK4lMYvl2iJ%2Bu3QZT1R1OZ7bdIWILE3Q4hNu5CpTshDt7OWJWhEyS2G4flUGRv2R%2FyJ6MuonQBlctASS6CwLzCbq0NYNerFE26uHjICilpDQ2ZJMlyMIZ0zBWdMZKBzE4kV5L2xASI%2F9%2BvrRYHh%2FO58fjWjES1v1TbfL7wqzxO0p0By4fdV8d%2B4Ox7F6KDhQ4Kql89gMxuyJXpanOE6EUMJr7XPFDFZaRGI7pZKSi25M8VNYklEjlARq%2F7F8VEAfrzbHlgcdv%2FHKSpI5NBjyZKBib58ZGTq9aNm2%2F9%2B3ul2WqEGetCXDVsEGLfem1X0rJGe2x8YvaRef8D6%2F0ws7r%2F0gY6pgGRDcKGx4ZJa%2BpRWvCZfBXx3neSstuC55ezr%2BngU61quD%2FC9AEZPc7jRfKFN94%2BBbtW%2FsPefpnPmaq4jQnBFXv0hu%2F2%2ByuNasIQ7uscm56eISTCnUp9IqzMkI7LkqUp5g6Ay4O0QmEwPyxurbyZA7dT0gaIBnhs3tmFLuF9l5hQsadHhXSkbgo8SBamPrNPFAytr7tehEQIdH4uclSu0E1Aq6Vm9i9v&X-Amz-Signature=c5912f499c34040dfc14738d02ddb3fd7a7800ee6500130279febd3765a796ad&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

项目团队根据当前的项目进度和成本的情况，对完工估算进行预测，那预测的结果可能和前面我们说的b、 a C 存在一些差异，那如果b、 a C 已经明显的不再可行，例如说整体的预算，前面我们讲的这个题，开发 20 个接口要花1万，但是目前已经花了1万五了，这很明显的这个b、 a C 已经不准确了。那这个时候我们要计算一下e、 a C 大概是多少，也就是说预测一下我们要完成整个项目到底是花1万 8 还是花2万，因为之前做的计划是1万。在这种情况下预测ea、 c 就非常重要了，估算和预计项目未来的一个情况，甚至如果有必要的时候，我们要重新校对这个基准。


这个 e 都是estimate，都是评估的一个意思，通过这个字母就比较好理解。那完工上位估算就是etc，这不是走高速的，这个 etc 重点就是一个to，它是代表完工尚未估算，也就是说在项目执行的不同时间点，还有要重新估算完成剩余工作还需要多少成本，那完工偏差就是 v a C，它是指对预算目前是负的还是正的一种预测。它是完工预算和完工估算之差。完工尚需绩效指数。 TCPI 主要是指为了完成这个项目剩余的一些工作必须要达到的一个成本。绩效指标是多少。



那我们看一下具体的计算方法。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/f4e3ed28-e475-489e-96ae-9707f087ec59/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RF7MLU4N%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFY7urbhhuCspp3gGwcKTgbb9n%2FXyYzkojvQJcVwrCgDAiBHDlf9GaX%2FL04m0vP99P5yUEMfN3RCIGoluUgb874aVCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMKMaEEcmDRTC0bUo5KtwDyDsI0AFYlu1iirCyCjQTX8wJn1Y7BDhfpMMIAoQxBEQ8AcJoY%2Fm9W335iAM7zSpNlKgqkzOSvH25uhLH%2BLLJunnBH3gXF%2FKwLc7MuIQpgaAdvXGfVxxBvfWuJ7f6UoEeUMpkrH%2FzFhaPBQTe8GetYNB677Uj9YMbPOm9YDZ8q9OgsleuUovGnLRsN9qs6MbDQqKbND3ew9hzIuKK1ZfJjR3bpaVifQdAi%2FUsaaE%2B%2FjHBdRbLJm8EbtNYKdQya4wDoLfjlrx7MhdVPQsbXNYvWJeQBkJKqTeM%2B6Gbf%2B8QYNvK4lMYvl2iJ%2Bu3QZT1R1OZ7bdIWILE3Q4hNu5CpTshDt7OWJWhEyS2G4flUGRv2R%2FyJ6MuonQBlctASS6CwLzCbq0NYNerFE26uHjICilpDQ2ZJMlyMIZ0zBWdMZKBzE4kV5L2xASI%2F9%2BvrRYHh%2FO58fjWjES1v1TbfL7wqzxO0p0By4fdV8d%2B4Ox7F6KDhQ4Kql89gMxuyJXpanOE6EUMJr7XPFDFZaRGI7pZKSi25M8VNYklEjlARq%2F7F8VEAfrzbHlgcdv%2FHKSpI5NBjyZKBib58ZGTq9aNm2%2F9%2B3ul2WqEGetCXDVsEGLfem1X0rJGe2x8YvaRef8D6%2F0ws7r%2F0gY6pgGRDcKGx4ZJa%2BpRWvCZfBXx3neSstuC55ezr%2BngU61quD%2FC9AEZPc7jRfKFN94%2BBbtW%2FsPefpnPmaq4jQnBFXv0hu%2F2%2ByuNasIQ7uscm56eISTCnUp9IqzMkI7LkqUp5g6Ay4O0QmEwPyxurbyZA7dT0gaIBnhs3tmFLuF9l5hQsadHhXSkbgo8SBamPrNPFAytr7tehEQIdH4uclSu0E1Aq6Vm9i9v&X-Amz-Signature=c60ea281dd52f77179696627feef970759a80f71aa9edbd49b685fc8e0ea0536&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

首先 e a C，它有三种方式，第一种是 a C 加 ETC 又等于b， a C 减EV，所以 e a C 也可以等于 a C 加b， a C 减EV， e a C 也等于 b a C 除以CPI， e a C 等于 a C 加 e t c 这个和这是一样的，但是后边的方式不一样，还等于 b a C 减去 EV 就是括号再除以 CPI 乘以SPI。那这种方法主要是承认现在这个实际成本能表示累计的这个实际项目的一个成本绩效情况，不关心好坏，并且预测未来全部的一个工作。这个完工估算对于项目经理来说还是非常方便的，通过计算得出的 EAC 可以考虑到不同程度的一个风险。


那这种方式最主要的也就是说目前讲的这三种，一种这种方式，它是承认以实际成本表示的累积实际项目的一个成本绩效情况，不关心这个好坏，也就是说我不关心现在是超支了还是没超支，并且预测未来的全部的 etc 工作都按预算的一个单价完成，是这样的一个指标。
还有一种方式是以 CPI 来完成 etc 的一个工作，也就是说通过成本这个绩效指数来完成还没有估算的，并且要达到完工的目标的这部分的一个估算结果。如果采用这种方式，也就代表着未来还没有做的工作都将按同样的 CPI 来执行，同样的一个成本绩效来执行，这个是只受 CPI 影响。那如果是受进度指数和成本指数都影响的话，我们就可以采用这种公式， B a C 减1V，然后再除以 cpi 乘以spi，这样被这两个都影响到了，然后再加上AC。


那这里边也有个假设， etc 都都将采用目前估算出来的 CPI 和 SPI 同样的一个指数来完成未来的一个工作。如果这个项目进度对 etc 有比较大的影响，那这个 SPI 在这个公司里边发现只有 SPI 在这个公式里，所以它也代表着如果这个项目进度对未来影响比较大，我们就可以采用这种方式。


要把 SPI 作为因子算进来，具体这两个也可以改变，例如说给它们赋予不同的一个权重，比如说五五分成本和进度，认为五五分可以或者二八分都可以比例，项目团队经理或者项目团队成员可以共同来决定一下。那完工尚未估算也同样的有这三种方法，b， a c 减 1V 之后再除以一个CPI。 a C 减 1V 之后除以 CPI 乘以SPI，所以这个就看是否被 CPI 影响，是否被 CPI 和 SPI 同时影响。



那我们再看一下完工偏差，这比较简单，就是等于 b a C 减 e a C，也就是说 b a C 是1万的话， e a C 计算出来假设等于2万，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/28a48db9-2d05-4ba2-9893-e0d4b2f12990/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RF7MLU4N%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFY7urbhhuCspp3gGwcKTgbb9n%2FXyYzkojvQJcVwrCgDAiBHDlf9GaX%2FL04m0vP99P5yUEMfN3RCIGoluUgb874aVCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMKMaEEcmDRTC0bUo5KtwDyDsI0AFYlu1iirCyCjQTX8wJn1Y7BDhfpMMIAoQxBEQ8AcJoY%2Fm9W335iAM7zSpNlKgqkzOSvH25uhLH%2BLLJunnBH3gXF%2FKwLc7MuIQpgaAdvXGfVxxBvfWuJ7f6UoEeUMpkrH%2FzFhaPBQTe8GetYNB677Uj9YMbPOm9YDZ8q9OgsleuUovGnLRsN9qs6MbDQqKbND3ew9hzIuKK1ZfJjR3bpaVifQdAi%2FUsaaE%2B%2FjHBdRbLJm8EbtNYKdQya4wDoLfjlrx7MhdVPQsbXNYvWJeQBkJKqTeM%2B6Gbf%2B8QYNvK4lMYvl2iJ%2Bu3QZT1R1OZ7bdIWILE3Q4hNu5CpTshDt7OWJWhEyS2G4flUGRv2R%2FyJ6MuonQBlctASS6CwLzCbq0NYNerFE26uHjICilpDQ2ZJMlyMIZ0zBWdMZKBzE4kV5L2xASI%2F9%2BvrRYHh%2FO58fjWjES1v1TbfL7wqzxO0p0By4fdV8d%2B4Ox7F6KDhQ4Kql89gMxuyJXpanOE6EUMJr7XPFDFZaRGI7pZKSi25M8VNYklEjlARq%2F7F8VEAfrzbHlgcdv%2FHKSpI5NBjyZKBib58ZGTq9aNm2%2F9%2B3ul2WqEGetCXDVsEGLfem1X0rJGe2x8YvaRef8D6%2F0ws7r%2F0gY6pgGRDcKGx4ZJa%2BpRWvCZfBXx3neSstuC55ezr%2BngU61quD%2FC9AEZPc7jRfKFN94%2BBbtW%2FsPefpnPmaq4jQnBFXv0hu%2F2%2ByuNasIQ7uscm56eISTCnUp9IqzMkI7LkqUp5g6Ay4O0QmEwPyxurbyZA7dT0gaIBnhs3tmFLuF9l5hQsadHhXSkbgo8SBamPrNPFAytr7tehEQIdH4uclSu0E1Aq6Vm9i9v&X-Amz-Signature=84ee0d0e9fde2a98ae8772a6f5ccd3962dc9a26bd217e269a73c7b95c9d92b33&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

这个偏差就是 -1万，我还差1万块钱，那完工尚需绩效指数，它就等于 BAC 减1V，然后除以 BAC 减AC。这个用计划完工的一个钱减去实际花费，这个是用计划完工的钱减去目前阶段已经完成的一个价值，用它们做一个除法。


既然 VIC 是一种偏差，还有这个绩效指数就要和 0 和一做对比了，那那 VC 大于 0 的时候，那就代表着这个成本实际的成本是小于计划成本的，可以在项目计划内完成。如果等于0，就代表实际成本和计划成本持平，那如果小于0，就代表了已经超支了，这个实际成本已经超过了计划成本。


TCPI 也是一样的，如果 TCPI 大于一，则代表这个项目完成的难度比较大，如果它小于一，则代表比较容易完成，相等就是正常。



那我们看一下实战，还是之前这个项目，我们把之前的参数拿过来，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e238dcc5-9ea5-46d4-a9bc-3db647007e38/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RF7MLU4N%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFY7urbhhuCspp3gGwcKTgbb9n%2FXyYzkojvQJcVwrCgDAiBHDlf9GaX%2FL04m0vP99P5yUEMfN3RCIGoluUgb874aVCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMKMaEEcmDRTC0bUo5KtwDyDsI0AFYlu1iirCyCjQTX8wJn1Y7BDhfpMMIAoQxBEQ8AcJoY%2Fm9W335iAM7zSpNlKgqkzOSvH25uhLH%2BLLJunnBH3gXF%2FKwLc7MuIQpgaAdvXGfVxxBvfWuJ7f6UoEeUMpkrH%2FzFhaPBQTe8GetYNB677Uj9YMbPOm9YDZ8q9OgsleuUovGnLRsN9qs6MbDQqKbND3ew9hzIuKK1ZfJjR3bpaVifQdAi%2FUsaaE%2B%2FjHBdRbLJm8EbtNYKdQya4wDoLfjlrx7MhdVPQsbXNYvWJeQBkJKqTeM%2B6Gbf%2B8QYNvK4lMYvl2iJ%2Bu3QZT1R1OZ7bdIWILE3Q4hNu5CpTshDt7OWJWhEyS2G4flUGRv2R%2FyJ6MuonQBlctASS6CwLzCbq0NYNerFE26uHjICilpDQ2ZJMlyMIZ0zBWdMZKBzE4kV5L2xASI%2F9%2BvrRYHh%2FO58fjWjES1v1TbfL7wqzxO0p0By4fdV8d%2B4Ox7F6KDhQ4Kql89gMxuyJXpanOE6EUMJr7XPFDFZaRGI7pZKSi25M8VNYklEjlARq%2F7F8VEAfrzbHlgcdv%2FHKSpI5NBjyZKBib58ZGTq9aNm2%2F9%2B3ul2WqEGetCXDVsEGLfem1X0rJGe2x8YvaRef8D6%2F0ws7r%2F0gY6pgGRDcKGx4ZJa%2BpRWvCZfBXx3neSstuC55ezr%2BngU61quD%2FC9AEZPc7jRfKFN94%2BBbtW%2FsPefpnPmaq4jQnBFXv0hu%2F2%2ByuNasIQ7uscm56eISTCnUp9IqzMkI7LkqUp5g6Ay4O0QmEwPyxurbyZA7dT0gaIBnhs3tmFLuF9l5hQsadHhXSkbgo8SBamPrNPFAytr7tehEQIdH4uclSu0E1Aq6Vm9i9v&X-Amz-Signature=ddc587c8e48ce3d51b6d246c2e57deda6c3cdbf0cf5471de585d6f86f30d592e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

这个开发项目目前是进度超前的，但是成本超支了，预测一下它的未来，还是同样的参数预测这个开发项目的一个绩效水平。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e3d51993-b012-498a-90de-bd99fa145026/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RF7MLU4N%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFY7urbhhuCspp3gGwcKTgbb9n%2FXyYzkojvQJcVwrCgDAiBHDlf9GaX%2FL04m0vP99P5yUEMfN3RCIGoluUgb874aVCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMKMaEEcmDRTC0bUo5KtwDyDsI0AFYlu1iirCyCjQTX8wJn1Y7BDhfpMMIAoQxBEQ8AcJoY%2Fm9W335iAM7zSpNlKgqkzOSvH25uhLH%2BLLJunnBH3gXF%2FKwLc7MuIQpgaAdvXGfVxxBvfWuJ7f6UoEeUMpkrH%2FzFhaPBQTe8GetYNB677Uj9YMbPOm9YDZ8q9OgsleuUovGnLRsN9qs6MbDQqKbND3ew9hzIuKK1ZfJjR3bpaVifQdAi%2FUsaaE%2B%2FjHBdRbLJm8EbtNYKdQya4wDoLfjlrx7MhdVPQsbXNYvWJeQBkJKqTeM%2B6Gbf%2B8QYNvK4lMYvl2iJ%2Bu3QZT1R1OZ7bdIWILE3Q4hNu5CpTshDt7OWJWhEyS2G4flUGRv2R%2FyJ6MuonQBlctASS6CwLzCbq0NYNerFE26uHjICilpDQ2ZJMlyMIZ0zBWdMZKBzE4kV5L2xASI%2F9%2BvrRYHh%2FO58fjWjES1v1TbfL7wqzxO0p0By4fdV8d%2B4Ox7F6KDhQ4Kql89gMxuyJXpanOE6EUMJr7XPFDFZaRGI7pZKSi25M8VNYklEjlARq%2F7F8VEAfrzbHlgcdv%2FHKSpI5NBjyZKBib58ZGTq9aNm2%2F9%2B3ul2WqEGetCXDVsEGLfem1X0rJGe2x8YvaRef8D6%2F0ws7r%2F0gY6pgGRDcKGx4ZJa%2BpRWvCZfBXx3neSstuC55ezr%2BngU61quD%2FC9AEZPc7jRfKFN94%2BBbtW%2FsPefpnPmaq4jQnBFXv0hu%2F2%2ByuNasIQ7uscm56eISTCnUp9IqzMkI7LkqUp5g6Ay4O0QmEwPyxurbyZA7dT0gaIBnhs3tmFLuF9l5hQsadHhXSkbgo8SBamPrNPFAytr7tehEQIdH4uclSu0E1Aq6Vm9i9v&X-Amz-Signature=1d34b8bd3e16e5696dc9921395cddbfe09f03247976d874b557089c257e982a4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

首先我们要对这个项目成本进行预算，也就是说完工估算 a C，它就是等于 a C 已经实际花费的加上e、 t c，也就是说加上 b a C 减EV，所以它计算下来翻译过来就是已经花出去的钱，再加上完成剩余工作还要花的钱，一共需要11500，也就是说和计划已经超支了。


它代表什么意思？例如说我们现在这个题，它就代表着我们花了 9000 块，1万减1000，但是我们只创造了 7500 块的一个价值。这么算完之后就代表着如果要完成这个项目，我大概要花 11500 才能完成这个项目。那如果我们采用同样的成本绩效指数，那就是说用 b a C 除以 CPI 7 PI，前面我们算过 00. 83，它算下来就代表着12000，它就代表什么意思？就代表我要花 12000 块才能完成这个原计划花1万块钱的一个项目，同时保证 CPI 不变，这个是成本。那我们看一下 VAC 就等于 BAC 减， EAC 等于负的 1500 块，它就代表这个成本。如如果想要完成的话，成本会超之，大概超值 1500 块。如果用第二个 EA c 计算出来就是超值 2000 块，那第二个 EA c 是保持同样的CPI，目前看这个成本肯定是超了。如果想要完成的话，超有两种，一种是超1500，一种保持同样的一个指数是超 2000 块。


那我们再分析一下这个进度情况。例如当前我们用了 6 天开发了 15 个接口，这个代表着进度是超前的，可以计算出来每天的一个进度情况，然后剩余 5 个接口， 20 - 15 个，大概用几天？如果按计划情况，一天两个接口，如果按实际情况算下来， 15 / 6，一天大概 2. 5 个接口。所以按计划就是每天两个，我还剩 5 个5，除以2，大概剩 2. 5 天。那如果按实际剩余 5 个接口，我再除以 2. 5，就用两天，最多不会超过 2. 5 天。


看一下TCPI，哈纳等于 BAC 减EV，除以 BAC 减以c，所以就等于1万 -7500，再除以1万 - 9000 = 2. 5 是大于一的，那等于 2. 5 是什么意思？这个就比较有意思了，它就代表着我花一块钱，我必须和之前计划的两块 5 保持一致，也就是说我花一块钱，它的价值应该是两块 5 的价值，我才能完成这个项目。


那如果 TPI 是一个小于一的值，例如说等于 0. 5，它就代表着我接下来我每花两块钱，只要起到 1 块钱的效果，我就可以完工了。而现在是大于一的，我每花一块钱，要起到花两块 5 的一个效果才能完工。所以 TCPI 小于一，它是越小越好，它就代表着剩余的钱比较多，所以只有它是越小越好的。


那在政治管理计算里边还有很多其他的一些概念，那和我们实际工作用的相对较少，而这些我们在实际工作中用的非常多，所以这里边也重点做了一个议题的一个讲解，我们小伙伴们可以在实际开发过程中多观察，多记录，用实际的学习到的这些政治管理来计算一下我们项目的当前的一个绩效情况，并且对它进行一个预测，这个也非常能体现项目管理的一个水平。


那我们接着看一下项目成本的管理总结。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/a5332bc5-be55-4cbb-9138-c52821febbca/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RF7MLU4N%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T232250Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFY7urbhhuCspp3gGwcKTgbb9n%2FXyYzkojvQJcVwrCgDAiBHDlf9GaX%2FL04m0vP99P5yUEMfN3RCIGoluUgb874aVCqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMKMaEEcmDRTC0bUo5KtwDyDsI0AFYlu1iirCyCjQTX8wJn1Y7BDhfpMMIAoQxBEQ8AcJoY%2Fm9W335iAM7zSpNlKgqkzOSvH25uhLH%2BLLJunnBH3gXF%2FKwLc7MuIQpgaAdvXGfVxxBvfWuJ7f6UoEeUMpkrH%2FzFhaPBQTe8GetYNB677Uj9YMbPOm9YDZ8q9OgsleuUovGnLRsN9qs6MbDQqKbND3ew9hzIuKK1ZfJjR3bpaVifQdAi%2FUsaaE%2B%2FjHBdRbLJm8EbtNYKdQya4wDoLfjlrx7MhdVPQsbXNYvWJeQBkJKqTeM%2B6Gbf%2B8QYNvK4lMYvl2iJ%2Bu3QZT1R1OZ7bdIWILE3Q4hNu5CpTshDt7OWJWhEyS2G4flUGRv2R%2FyJ6MuonQBlctASS6CwLzCbq0NYNerFE26uHjICilpDQ2ZJMlyMIZ0zBWdMZKBzE4kV5L2xASI%2F9%2BvrRYHh%2FO58fjWjES1v1TbfL7wqzxO0p0By4fdV8d%2B4Ox7F6KDhQ4Kql89gMxuyJXpanOE6EUMJr7XPFDFZaRGI7pZKSi25M8VNYklEjlARq%2F7F8VEAfrzbHlgcdv%2FHKSpI5NBjyZKBib58ZGTq9aNm2%2F9%2B3ul2WqEGetCXDVsEGLfem1X0rJGe2x8YvaRef8D6%2F0ws7r%2F0gY6pgGRDcKGx4ZJa%2BpRWvCZfBXx3neSstuC55ezr%2BngU61quD%2FC9AEZPc7jRfKFN94%2BBbtW%2FsPefpnPmaq4jQnBFXv0hu%2F2%2ByuNasIQ7uscm56eISTCnUp9IqzMkI7LkqUp5g6Ay4O0QmEwPyxurbyZA7dT0gaIBnhs3tmFLuF9l5hQsadHhXSkbgo8SBamPrNPFAytr7tehEQIdH4uclSu0E1Aq6Vm9i9v&X-Amz-Signature=083e7b37fb3dc960cafed5bbccf8714df09f6d8d8eff9eefcbad4542e39431e4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

首先就是规划成本管理，这里边要做哪些工作，大家回想一下。还有估算成本，主要就是和估算进度采用的方式是一样的，也可以使用 a 的分布，也可以使用三角分布，都可以，参数估算，专家判断都可以。制定预算就是来制定我们这个项目大概要花多少钱，整个变更计划是什么样的。然后就是控制成本了，控制成本这里边最重要的，刚刚也讲了三大核心成本管理里边的政治管理非常重要，那政治管理里边我们讲了很多参数，比如说 PV EV、 PV 计划价值 EV 正值 AC 实际成本 BAC 完工预算。


当然还有一些计算出来的，例如说指标 CV 大于 0 等于 0 小于0，分别代表什么？成本绩效 CPI 进度偏差 SV 进度绩效SPI，还有预测技术，比如说etc，EAC， TCPI 还有VAC，根据不同的参数，它们大小关系和零的对比，我们就能分析出来这个效率是什么样的。进度是提前了还是延后了，成本投入是超前了还是延后了，把这些都能计算出来，这样对我们管控项目是非常有帮助的。然后就是成本概念，我们讲了间接直接成本，沉默成本等等这些成本概念，希望大家在生活中，工作中都有自己的体会。那么项目成本管理这一节就到这里结束，我是gitly，我们下节课再见。


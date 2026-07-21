---
title: 3-23 前缀-模糊-占位符搜索
---

# 3-23 前缀-模糊-占位符搜索

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/ce89ac70-069d-415c-8dfc-27e167d56df8/SCR-20240806-enom.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WPJURFFK%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225152Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD8x5jlV%2B%2BUJI12T1fkw9uAePX4PzpwSHzCEf5KihI6BgIhAI8NA3niNeggQoBUvUV8IPmSYvdp5%2BgJ9%2Fx7Avzi46oIKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyBtGP0ul5hlO5tnf4q3AOM22bjAmC05wYI6DuGMg6%2FSNEm%2B4j62Da2EreL6b1NzoFrXXHZAY9TQyYsEElO1XfS8a1Y34PzbKvwNtmBmgeWOJEPPcBVgkz1FiR5idMVtDzss3%2Fg82ZjGZ36UvJ1knNBdx1Ef2eV4bwo4hftP3qiowx5bGs0msqq1ojv4Ew9A0v%2Bim7Gyv4AOfvBoDR6VZ4lt1Ftkd60Xkox%2Fzedylt3gBgpgHWFgQ%2Bo%2FvnUzcK5zbp2Hpuam2Ln5WQAl%2FRTBOOFaFD4Dicfb7wxg8SY%2BttB%2BuV1lDrRNBOMu6ETJjyimo4yIPRwJJPwB2bR1Eghn%2FBZwh4Frf%2FP4z4aIIDtioiUBBBoO1led0BZn18cukctVU7WDnY%2BWqRzay1X6hr28p3sFZq6sF%2FesFiuZfgeyvJpUaFcTZu8i1BfK76zFfxwOqPHqiVzScFd%2BJpPSO%2BI30TNwxTJuyPrAE5xAZJoUNry9%2B9lGE7Dh7dd2hUmQCoqeYl0rHAZ6PL1UP0OHm2dZYIpf2Zj9A4nJ2910gGzPFYY1Us8UtqxLQeX8%2B43XdKjs6MknV0QV4O5MyLvSA5tMgC0Mg9tfau3Z6Xq3RcHNI%2FDxNfhIVLC2p0rcksmD5MPsL9VP6jw1wJNzgrsUTC6uf%2FSBjqkAfyK5%2Fy%2BOuFy%2Fb%2BOzPWpAkh9j%2FcH%2BHphPWrdIWbBZmVj0zbvvnQ%2BYvaApjY0bW6ebASBiHwYqyNcv6REWQ%2FIzGOBo8C%2FJX0u0ZWOg%2BDIamfZrP9bTaQ%2FgjfWVqZqzKrDitpLrhrDMnIgrjhg61oS2V8kMoPuVAANy2J693l3luQRR9aC%2F4EriVdafcjqn2hVr2cWgpfuQs1w7K84oyuM63hB4r1C&X-Amz-Signature=2804151ad224b537f452d511af25a5de08ad6cde259acedd01cf915864f61ab9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

3-23附：课外拓展-prefx-fuzzy-
wildcard prefix
根据前缀去查询 POST
/shop/_doc/_search "query":
"prefix":
"desc": "imo'
·head可视化
fuzzy
模糊搜索，并不是指的sql的模糊搜索，而是用户在进行搜索的时候的打字错误现象，搜索引擎会自动纠正，然后尝试匹配索引库中的数据。
POST
/shop/_doc/_search "query":{
"fuzzy":
"desc": "imoov. coom'" √
或多字段搜索 "query":{
"multi match":
"fields": "desc", "nickname"], "query": "imcoc supor"
"fuzziness": "AUTO" }
}
"query":{
"multi_match":{
"fields": "desc", "nickname"] "query":"演说"，
"fuzziness":"1"
·官文：https:/www.elastic.co/guide/cn/elasticsearch/guide/curre nt/fuzzy-match-query.html
wildcard 占位符查询。
·?:1个字符
○*：1个或多个字符POST
/shop/_doc/_search "query":
wildcard":{
"desc":"*00? 'query":
"wildcard":
"desc":"演*"
官文：https:/www.elastic.co/guide/en/elasticsearch/reference/c urrent/query-dsl-wildcard-query. html


[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/7406af0b-f232-4561-b5df-9f5dc75daae3/2020-09-17_175540.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WPJURFFK%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T225152Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD8x5jlV%2B%2BUJI12T1fkw9uAePX4PzpwSHzCEf5KihI6BgIhAI8NA3niNeggQoBUvUV8IPmSYvdp5%2BgJ9%2Fx7Avzi46oIKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyBtGP0ul5hlO5tnf4q3AOM22bjAmC05wYI6DuGMg6%2FSNEm%2B4j62Da2EreL6b1NzoFrXXHZAY9TQyYsEElO1XfS8a1Y34PzbKvwNtmBmgeWOJEPPcBVgkz1FiR5idMVtDzss3%2Fg82ZjGZ36UvJ1knNBdx1Ef2eV4bwo4hftP3qiowx5bGs0msqq1ojv4Ew9A0v%2Bim7Gyv4AOfvBoDR6VZ4lt1Ftkd60Xkox%2Fzedylt3gBgpgHWFgQ%2Bo%2FvnUzcK5zbp2Hpuam2Ln5WQAl%2FRTBOOFaFD4Dicfb7wxg8SY%2BttB%2BuV1lDrRNBOMu6ETJjyimo4yIPRwJJPwB2bR1Eghn%2FBZwh4Frf%2FP4z4aIIDtioiUBBBoO1led0BZn18cukctVU7WDnY%2BWqRzay1X6hr28p3sFZq6sF%2FesFiuZfgeyvJpUaFcTZu8i1BfK76zFfxwOqPHqiVzScFd%2BJpPSO%2BI30TNwxTJuyPrAE5xAZJoUNry9%2B9lGE7Dh7dd2hUmQCoqeYl0rHAZ6PL1UP0OHm2dZYIpf2Zj9A4nJ2910gGzPFYY1Us8UtqxLQeX8%2B43XdKjs6MknV0QV4O5MyLvSA5tMgC0Mg9tfau3Z6Xq3RcHNI%2FDxNfhIVLC2p0rcksmD5MPsL9VP6jw1wJNzgrsUTC6uf%2FSBjqkAfyK5%2Fy%2BOuFy%2Fb%2BOzPWpAkh9j%2FcH%2BHphPWrdIWbBZmVj0zbvvnQ%2BYvaApjY0bW6ebASBiHwYqyNcv6REWQ%2FIzGOBo8C%2FJX0u0ZWOg%2BDIamfZrP9bTaQ%2FgjfWVqZqzKrDitpLrhrDMnIgrjhg61oS2V8kMoPuVAANy2J693l3luQRR9aC%2F4EriVdafcjqn2hVr2cWgpfuQs1w7K84oyuM63hB4r1C&X-Amz-Signature=cd3440672c7a698ca8b51d88082f8b04d91ca4fc829ce4dc974cd992ad6c4bb3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


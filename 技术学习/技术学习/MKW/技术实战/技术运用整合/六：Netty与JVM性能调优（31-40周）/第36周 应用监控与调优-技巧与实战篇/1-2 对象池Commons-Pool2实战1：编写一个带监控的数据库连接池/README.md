---
title: 1-2 对象池Commons-Pool2实战1：编写一个带监控的数据库连接池
---

# 1-2 对象池Commons-Pool2实战1：编写一个带监控的数据库连接池

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/f2ebf8a5-e500-4460-8245-8bedb27dc0d0/SCR-20240727-uczb.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBG4YFWK%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230107Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFBCsjjKa28ItAe9AHbjwodarufFeFuoWbVmvsN3O5CWAiBSQcZ7%2BH9R%2Bn2UKIC4p43aURr6hw4D90w2otoyYhbYeyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrBvCYE7VgibCglS4KtwDH2GdFwmf2Mg06W4%2ByP8zJVCu1cGCZqI9c26bA4%2Bx9YjRm%2Bf%2BGP0scbtKhx%2B26L%2BLYX1mbKPu2%2B19qOlggupAybdCxnWHC99awMTw8TD3v4yBGcl1vjjQNtMBYgGMQsE7CJ2pZ3n1jvRE381cov0W8548WFrGNu7VxIbejogaXT7q4bRQ0geYwygOAEHvGNfaEFNaEs8oGpHu6FN4B%2B6%2FXKsdMINSbJXbJ9TnEP1qWIseaRH1qqwJG180MimNFbRPBPTvHjSJbr88Catrg35YqgWrGH5hgKaJL1EaZ7syrRkvzHZtJv6O8EJtOYU%2Ba3qmaZwOFIt1oSOcJbtJPDfvGQXd30KPeXBFVLzAzWPN875V0%2F8TNNyYGCJCMx7pxuJKZZavqwJP8H%2Bc5N5ZOYFe%2FlifX0cnVCZIVrLr5XLX1Mv8AL0GWq1Rz5FfEzSUvFNd4OT0aOeG9cqnl8RRubPC9EdygPNsYweU65cVmXtDaCpVAK%2B4X8NGrB4aWCQo15re93sUA1rnx%2FNTWF5owddnrHEOG9aUJ263svxEgjzSCEBxYyeSA6x%2BGbf1LOTriLm%2B0lP2zlv%2FINaAvJ6l3XZxM1cpG7fhqfbYyWrDZe%2BnR5W89qVdCa%2BPLNbw7Lww1bn%2F0gY6pgGNIITLRjAlDRxi5uVr8kdxYxEPWP9Re%2FumNKVUG7pxDGvmiXBY9Po4s6h9T1onrxSvxbPTC6VPlMUDA9%2BfJ0zOCnDNJ7zPSw7Ud6%2BLLfH04G%2FmD29Y8ae0DdPSiI5MWQQNyZMH6s2aRpZkW3nTbRQGQ3S4Q1dNsSJv0EirMrJ7qlGAn1HVoBi2Bqhc9j%2Fvas1PQHA8dja1pqWgMmfTcMp4fFPE3%2B40&X-Amz-Signature=a17452fe46f890ca13e2c42128a533c8bb53b976a8fc22595bb0c134e660056d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/6aa3f61a-b4b2-4b4a-9294-db36a06294d7/SCR-20240727-uigh.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBG4YFWK%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230107Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFBCsjjKa28ItAe9AHbjwodarufFeFuoWbVmvsN3O5CWAiBSQcZ7%2BH9R%2Bn2UKIC4p43aURr6hw4D90w2otoyYhbYeyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrBvCYE7VgibCglS4KtwDH2GdFwmf2Mg06W4%2ByP8zJVCu1cGCZqI9c26bA4%2Bx9YjRm%2Bf%2BGP0scbtKhx%2B26L%2BLYX1mbKPu2%2B19qOlggupAybdCxnWHC99awMTw8TD3v4yBGcl1vjjQNtMBYgGMQsE7CJ2pZ3n1jvRE381cov0W8548WFrGNu7VxIbejogaXT7q4bRQ0geYwygOAEHvGNfaEFNaEs8oGpHu6FN4B%2B6%2FXKsdMINSbJXbJ9TnEP1qWIseaRH1qqwJG180MimNFbRPBPTvHjSJbr88Catrg35YqgWrGH5hgKaJL1EaZ7syrRkvzHZtJv6O8EJtOYU%2Ba3qmaZwOFIt1oSOcJbtJPDfvGQXd30KPeXBFVLzAzWPN875V0%2F8TNNyYGCJCMx7pxuJKZZavqwJP8H%2Bc5N5ZOYFe%2FlifX0cnVCZIVrLr5XLX1Mv8AL0GWq1Rz5FfEzSUvFNd4OT0aOeG9cqnl8RRubPC9EdygPNsYweU65cVmXtDaCpVAK%2B4X8NGrB4aWCQo15re93sUA1rnx%2FNTWF5owddnrHEOG9aUJ263svxEgjzSCEBxYyeSA6x%2BGbf1LOTriLm%2B0lP2zlv%2FINaAvJ6l3XZxM1cpG7fhqfbYyWrDZe%2BnR5W89qVdCa%2BPLNbw7Lww1bn%2F0gY6pgGNIITLRjAlDRxi5uVr8kdxYxEPWP9Re%2FumNKVUG7pxDGvmiXBY9Po4s6h9T1onrxSvxbPTC6VPlMUDA9%2BfJ0zOCnDNJ7zPSw7Ud6%2BLLfH04G%2FmD29Y8ae0DdPSiI5MWQQNyZMH6s2aRpZkW3nTbRQGQ3S4Q1dNsSJv0EirMrJ7qlGAn1HVoBi2Bqhc9j%2Fvas1PQHA8dja1pqWgMmfTcMp4fFPE3%2B40&X-Amz-Signature=796e1513f8ff21dfe69b8393730ebd58102d5f6d321f0691c1e30ff59fe23a96&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/a7763339-d6d7-4a79-8ae0-b768a6a3c459/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBG4YFWK%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230107Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFBCsjjKa28ItAe9AHbjwodarufFeFuoWbVmvsN3O5CWAiBSQcZ7%2BH9R%2Bn2UKIC4p43aURr6hw4D90w2otoyYhbYeyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrBvCYE7VgibCglS4KtwDH2GdFwmf2Mg06W4%2ByP8zJVCu1cGCZqI9c26bA4%2Bx9YjRm%2Bf%2BGP0scbtKhx%2B26L%2BLYX1mbKPu2%2B19qOlggupAybdCxnWHC99awMTw8TD3v4yBGcl1vjjQNtMBYgGMQsE7CJ2pZ3n1jvRE381cov0W8548WFrGNu7VxIbejogaXT7q4bRQ0geYwygOAEHvGNfaEFNaEs8oGpHu6FN4B%2B6%2FXKsdMINSbJXbJ9TnEP1qWIseaRH1qqwJG180MimNFbRPBPTvHjSJbr88Catrg35YqgWrGH5hgKaJL1EaZ7syrRkvzHZtJv6O8EJtOYU%2Ba3qmaZwOFIt1oSOcJbtJPDfvGQXd30KPeXBFVLzAzWPN875V0%2F8TNNyYGCJCMx7pxuJKZZavqwJP8H%2Bc5N5ZOYFe%2FlifX0cnVCZIVrLr5XLX1Mv8AL0GWq1Rz5FfEzSUvFNd4OT0aOeG9cqnl8RRubPC9EdygPNsYweU65cVmXtDaCpVAK%2B4X8NGrB4aWCQo15re93sUA1rnx%2FNTWF5owddnrHEOG9aUJ263svxEgjzSCEBxYyeSA6x%2BGbf1LOTriLm%2B0lP2zlv%2FINaAvJ6l3XZxM1cpG7fhqfbYyWrDZe%2BnR5W89qVdCa%2BPLNbw7Lww1bn%2F0gY6pgGNIITLRjAlDRxi5uVr8kdxYxEPWP9Re%2FumNKVUG7pxDGvmiXBY9Po4s6h9T1onrxSvxbPTC6VPlMUDA9%2BfJ0zOCnDNJ7zPSw7Ud6%2BLLfH04G%2FmD29Y8ae0DdPSiI5MWQQNyZMH6s2aRpZkW3nTbRQGQ3S4Q1dNsSJv0EirMrJ7qlGAn1HVoBi2Bqhc9j%2Fvas1PQHA8dja1pqWgMmfTcMp4fFPE3%2B40&X-Amz-Signature=e582bfe53bca0e20a5f126227f7a9ce6793e1cfa1eeb6bd91fe622e44df6dbfa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/cd33a675-c522-46c3-865f-b30b1f74a756/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBG4YFWK%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230107Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFBCsjjKa28ItAe9AHbjwodarufFeFuoWbVmvsN3O5CWAiBSQcZ7%2BH9R%2Bn2UKIC4p43aURr6hw4D90w2otoyYhbYeyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrBvCYE7VgibCglS4KtwDH2GdFwmf2Mg06W4%2ByP8zJVCu1cGCZqI9c26bA4%2Bx9YjRm%2Bf%2BGP0scbtKhx%2B26L%2BLYX1mbKPu2%2B19qOlggupAybdCxnWHC99awMTw8TD3v4yBGcl1vjjQNtMBYgGMQsE7CJ2pZ3n1jvRE381cov0W8548WFrGNu7VxIbejogaXT7q4bRQ0geYwygOAEHvGNfaEFNaEs8oGpHu6FN4B%2B6%2FXKsdMINSbJXbJ9TnEP1qWIseaRH1qqwJG180MimNFbRPBPTvHjSJbr88Catrg35YqgWrGH5hgKaJL1EaZ7syrRkvzHZtJv6O8EJtOYU%2Ba3qmaZwOFIt1oSOcJbtJPDfvGQXd30KPeXBFVLzAzWPN875V0%2F8TNNyYGCJCMx7pxuJKZZavqwJP8H%2Bc5N5ZOYFe%2FlifX0cnVCZIVrLr5XLX1Mv8AL0GWq1Rz5FfEzSUvFNd4OT0aOeG9cqnl8RRubPC9EdygPNsYweU65cVmXtDaCpVAK%2B4X8NGrB4aWCQo15re93sUA1rnx%2FNTWF5owddnrHEOG9aUJ263svxEgjzSCEBxYyeSA6x%2BGbf1LOTriLm%2B0lP2zlv%2FINaAvJ6l3XZxM1cpG7fhqfbYyWrDZe%2BnR5W89qVdCa%2BPLNbw7Lww1bn%2F0gY6pgGNIITLRjAlDRxi5uVr8kdxYxEPWP9Re%2FumNKVUG7pxDGvmiXBY9Po4s6h9T1onrxSvxbPTC6VPlMUDA9%2BfJ0zOCnDNJ7zPSw7Ud6%2BLLfH04G%2FmD29Y8ae0DdPSiI5MWQQNyZMH6s2aRpZkW3nTbRQGQ3S4Q1dNsSJv0EirMrJ7qlGAn1HVoBi2Bqhc9j%2Fvas1PQHA8dja1pqWgMmfTcMp4fFPE3%2B40&X-Amz-Signature=3841e9075d78a4c2e971244ef5e5b795a2b0b6bd60d54b8528f5a666782423aa&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

大家好，我是大木。这几个一起来用 Com sport two 编写一个数据库连接池。我们要求这个数据库连接池能够替代其他的数据库连接池产品，比如 Hackery d、b、c、p、汤 k 的连接池，阿里巴巴德路语等等。第二，我们希望数据库连接池带有监控，也就是我们能够随时了解连接池的运行情况。这节课是有一定难度的，学习起来可能不是那么容易，建议同学们如果第一次观看掌握不了，可以多刷一两次。同时，为了防止大家不被我吓跑，这里特地列出来了学习本节课的收益。首先，学习本节可以巩固对象池的用法，这是最基本的。第二，你可以收获到若干个开发 springboot 的技巧。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/0b6c645e-d311-471c-8127-de3a25ba115e/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBG4YFWK%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230107Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFBCsjjKa28ItAe9AHbjwodarufFeFuoWbVmvsN3O5CWAiBSQcZ7%2BH9R%2Bn2UKIC4p43aURr6hw4D90w2otoyYhbYeyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrBvCYE7VgibCglS4KtwDH2GdFwmf2Mg06W4%2ByP8zJVCu1cGCZqI9c26bA4%2Bx9YjRm%2Bf%2BGP0scbtKhx%2B26L%2BLYX1mbKPu2%2B19qOlggupAybdCxnWHC99awMTw8TD3v4yBGcl1vjjQNtMBYgGMQsE7CJ2pZ3n1jvRE381cov0W8548WFrGNu7VxIbejogaXT7q4bRQ0geYwygOAEHvGNfaEFNaEs8oGpHu6FN4B%2B6%2FXKsdMINSbJXbJ9TnEP1qWIseaRH1qqwJG180MimNFbRPBPTvHjSJbr88Catrg35YqgWrGH5hgKaJL1EaZ7syrRkvzHZtJv6O8EJtOYU%2Ba3qmaZwOFIt1oSOcJbtJPDfvGQXd30KPeXBFVLzAzWPN875V0%2F8TNNyYGCJCMx7pxuJKZZavqwJP8H%2Bc5N5ZOYFe%2FlifX0cnVCZIVrLr5XLX1Mv8AL0GWq1Rz5FfEzSUvFNd4OT0aOeG9cqnl8RRubPC9EdygPNsYweU65cVmXtDaCpVAK%2B4X8NGrB4aWCQo15re93sUA1rnx%2FNTWF5owddnrHEOG9aUJ263svxEgjzSCEBxYyeSA6x%2BGbf1LOTriLm%2B0lP2zlv%2FINaAvJ6l3XZxM1cpG7fhqfbYyWrDZe%2BnR5W89qVdCa%2BPLNbw7Lww1bn%2F0gY6pgGNIITLRjAlDRxi5uVr8kdxYxEPWP9Re%2FumNKVUG7pxDGvmiXBY9Po4s6h9T1onrxSvxbPTC6VPlMUDA9%2BfJ0zOCnDNJ7zPSw7Ud6%2BLLfH04G%2FmD29Y8ae0DdPSiI5MWQQNyZMH6s2aRpZkW3nTbRQGQ3S4Q1dNsSJv0EirMrJ7qlGAn1HVoBi2Bqhc9j%2Fvas1PQHA8dja1pqWgMmfTcMp4fFPE3%2B40&X-Amz-Signature=324366ffdf43f616192352791e629c40365c13d3c5e3d3ba45cc780fccbf146c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

第三，你还可以学到怎么样扩展 spring boot actuator。话不多说，来写代码。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/ac12240e-4eb5-4a5e-902b-9a4f88cac3c7/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UBG4YFWK%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230107Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFBCsjjKa28ItAe9AHbjwodarufFeFuoWbVmvsN3O5CWAiBSQcZ7%2BH9R%2Bn2UKIC4p43aURr6hw4D90w2otoyYhbYeyqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMrBvCYE7VgibCglS4KtwDH2GdFwmf2Mg06W4%2ByP8zJVCu1cGCZqI9c26bA4%2Bx9YjRm%2Bf%2BGP0scbtKhx%2B26L%2BLYX1mbKPu2%2B19qOlggupAybdCxnWHC99awMTw8TD3v4yBGcl1vjjQNtMBYgGMQsE7CJ2pZ3n1jvRE381cov0W8548WFrGNu7VxIbejogaXT7q4bRQ0geYwygOAEHvGNfaEFNaEs8oGpHu6FN4B%2B6%2FXKsdMINSbJXbJ9TnEP1qWIseaRH1qqwJG180MimNFbRPBPTvHjSJbr88Catrg35YqgWrGH5hgKaJL1EaZ7syrRkvzHZtJv6O8EJtOYU%2Ba3qmaZwOFIt1oSOcJbtJPDfvGQXd30KPeXBFVLzAzWPN875V0%2F8TNNyYGCJCMx7pxuJKZZavqwJP8H%2Bc5N5ZOYFe%2FlifX0cnVCZIVrLr5XLX1Mv8AL0GWq1Rz5FfEzSUvFNd4OT0aOeG9cqnl8RRubPC9EdygPNsYweU65cVmXtDaCpVAK%2B4X8NGrB4aWCQo15re93sUA1rnx%2FNTWF5owddnrHEOG9aUJ263svxEgjzSCEBxYyeSA6x%2BGbf1LOTriLm%2B0lP2zlv%2FINaAvJ6l3XZxM1cpG7fhqfbYyWrDZe%2BnR5W89qVdCa%2BPLNbw7Lww1bn%2F0gY6pgGNIITLRjAlDRxi5uVr8kdxYxEPWP9Re%2FumNKVUG7pxDGvmiXBY9Po4s6h9T1onrxSvxbPTC6VPlMUDA9%2BfJ0zOCnDNJ7zPSw7Ud6%2BLLfH04G%2FmD29Y8ae0DdPSiI5MWQQNyZMH6s2aRpZkW3nTbRQGQ3S4Q1dNsSJv0EirMrJ7qlGAn1HVoBi2Bqhc9j%2Fvas1PQHA8dja1pqWgMmfTcMp4fFPE3%2B40&X-Amz-Signature=5bb5806df1a0009349ba48af7e5e2af57069573bcf0aead55a453c6834983645&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

为了照顾基础不好的同学，先来写一段 JDBC 操作数据库的代码，带大家复习一下。 JDBC 基础创建个包叫JDBC，创建个类叫 JDBC test， p s v m 创建面方法，大写的时候我们都学过。操作数据库之前，需要用 class 点 for name，通过反射传入数据库驱动的报名类名全路径，异常抛出去。用 driver manager 点 get connection，传入数据库的 URL 账号以及密码，依然抛出去。这样的就会获得操作数据库的连接。 URL 账号以及密码可以在 application DV 文件里面找到。 copy 粘贴账号 roots 密码都在123。拿到 connection 之后就可以操作数据库了。


可以用 connection 点 create statement 拿到 statement 的对象，也可以使用 connection 点 prepare statement 传入。想要直接的circle，可以返回 prepared statement。对象。还记得 statement 存在 SQL 注入的风险，所以实际项目中我们应该尽可能的使用 prepared statement，对吧？下掉circle，我们随便写一个，比如。


Select the same promo others down. Your unprepared statement excuse the query.
就可以执行 circle 了。返回的 result set 对象就是 SQL 的返回，配用 well without set next 去迭代返回的结果。我们可以打印一下，用 result set 点儿 get string，比如 i d， user ID。代码写好了，来测试一下。不让，可以正常返回，但是这个代码是有问题的。在操作完之后，我们应该把 result set close 掉， statement close 掉， connection closed out，否则会造成资源的极大浪费。如果我们还想继续操作数据库，可以在这里 connection close 之前 copy 一段粘贴，改成二二22，发送一条其他的 SQL 语句。这里我们可以使用 get string 的第二种写法。


一、表达的意思是获取返回的第一个字段以及第二个字段，再次让下，可以正常返回，对吧？如果 connection close 掉之后再去用 connection prepare statement 就会报错了，对吧？报的异常。他说不允许在连接关闭之后做任何操作。好。


从这个代码可以看出， statement 以及 result set 是 SQL 语句级别的，而一个 connection 可以被多个 statement 以及多个 result set 共享。按照上一节的描述，连接池它是复用连接的对吧？所以我们会很容易想到这样去定义连接池。创建一个包叫 data source。创建个类叫做connection， poor 的 object factory，让它实现 pull 的 object factory 接口。泛型的写connection。实现一下方法。这里的 make object 的方法可以连接数据库，我们可以把这一段拷贝过来。
拿到连接之后，我们用 default fold object 包装一下。这里的 destroy object。我们很容易想到应该把 connection 关闭掉对吧？用 p 点 get object 点close， validate object 我们可以这样写。 p 点 get object。拿到连接，用 connection 点 prepare statement 传入 select 1。


大家看到 select 1 会不会比较熟悉？我们是不是配置数据源的时候都会有一个东西叫 validation query，这里与 select e 对吧？这里我们可以模拟一下。我们 try catch 一下，用 statement their execute query 得到结果。用 without set 点 get Int 然后一，如果 i 等于1，说明数据库是正常的，如果不等于 1 或者抛异常了，说明数据库不正常。


摆个force，这样就可以校验 connection 是不是正常了。这里的激活 object 我们可以留空，因为这里的 connection 我们已经可以使用了，对吧？高级一些的连接池可以把对 connection 额外的配置放到这里。可以把 connection 额外的配置放到这里，这样可以定制 connection 对不对。这里的 passive object 我们也可以留空。


好，工厂已经写完了，我们怎么样去满足 PPT 里面的第一点诉求，能够替代其他的数据库连接池产品？还记得我们在初始化各种数据库连接池的时候，都会去 new 一个某 data source 的对象。这里我们可以又一个，大幕， data sauce，这个类可以实现一下 data source 接口，这也是j，d、b、 c 规范里面定义的一个接口。实现一下方法最核心的方法。从这里可以看出来是 get connection 以及 get a connection。讲到这里，同学们应该可以猜到这个代码怎么写了。我们可以创建一个构造方法，在这里初始化一个generic。 object pull 泛型写connection，传入我们的 connection pull 的 object factory。


破，把它放到外面去。private， this 点在这里就可以用 this 点儿 pool 点儿borrow。 object 可能会发生异常，所以我们可以去 catch 一下。如果截获到异常，我们就可以抛出去 throw 一个 circle exception，获取连接失败。


同理第二个 get connection，我们可以用 this 点儿 get a connection。其他的方法我们都可以不实现，直接 throw new on support operation exception。不支持的操作。


好， data source 也写好了，下面我们就为初始化 data source 了。到启动类里面， your add beam， public 大木 data source， return new 一个弹幕 data sauce 就可以了，可以加上 primary 注解。这样的 my baddies 注入的数据源就是这里的大幕 data source，而不是默认的 hickory data source 了。启动项目，运行看看，可以正常返回。okay。下面我们来为数据源实现。


第二点诉求监控。创建一个新的类，叫 data source， any points，在类上添加endpoint，注解 ID 等于 data source。这是一个 spring boot activator 的注解，它表达的意思是可以用， Actuator dead source 访问到这个端点。在里面创建一个方法，比如 map string object for。


打包。在方法上面加上 read operation，表示用 get 方法访问端点的时候，就会调用到这个方法。这里我们可以使用 private 弹幕，带着 source get a sauce。用 data source 点， get 一下这里的pull，我们想要监控的数据都在 pull 里面对吧。生成一下 get set 方法到这里。 get full。打到破之后， maps 你有一个Hashmap，放几个监控指标进去。 map 点 put number active， full 点儿 number active，还记得 number active 以及 number Idol 都是 pool 的核心 API 对吧？再扑克一下 number Idol，获取空闲的对象个数。


再来获得一下 four 点 get a created account 对象值创建的对象总数 pretty 的count。最后 return 一下 map 就可以了。 endpoint 也写好了。初始化一下 at bin public get us at any point。打包又一个 get a sauce and point。我们需要注入 data sauce，所以这里可以创建一个构造方法，用 this 点儿 data sauce， return 就可以了。重启项目，可以发现项目启动失败了。


在这一行画出了一场。他说大木 data source 和 proxy lay 无法兼容。为什么会报这样的异常？这种异常一般都是由于动态代理造成的对吧？这是因为 Java melody，它能够监控数据源对不对。它的做法是把 spring 容器里面的 data source 类用反向代理，甚至一个代理类，从而时间监控。我经过源码分析之后发现， Java melody 是在 j d b c wrapper 这个类里面的， create a data source proxy 这个方法里面去实现反向代理的。并且它经过反向代理之后返回的是一个 data source。所以至少我们应该把这里的大木 data source 改成 data source。这个时候，我们可以强转一下，把它改成 dum data source。空气。你会发现，依然会报错，不过到这里还没有报错，可以看到它确实是一个 proxy 类，里面包裹了一个 data source，这一行代码就会报错了，对吧？试问一个 proxy 类怎么可以转换成大幕？ data source 报错了？解决方案有两种，一种是把这里的 data source 用反射拿到一个我们原先的大木 data source，再传入到 data source endpoint 里面去。


第二种方式是在 application where 妙里面添加一个配置。还记得前面讲过， Java melody 有一个 excluded 的 data sources，把不想监控的 data source 给它排除掉。配置这里的方法名就可以了，也就是 spring 容器里面的 b 名称双击项目，这样 data source 就不会被加个 melody 封装。可以看到已经不是 proxy 了，项目就不会报错了。同学们也可以用反向代理的方式拿到原先的 data source 注入到这里，顺便复习一下反向代理对不对？课上我就不带大家演示了，没有什么注意点，就是用反向代理去解包对不对？OK，项目启动好之后，我们来访问 Lockhoster 8088 actuator data source，可以看到都是0，我们来调用API，在哪可以正常返回。


多算了几次刷新可以发现创建了 5 个对象，活跃了 5 个对象，有 0 个是空闲的，再调用一次，依然是 0 个空闲的。案例来讲，大部分对象应该都是空闲的，因为调用完了连接就会释放。而现在 active 是6，说明 connection 没有被回收，每调用一次就会创建一个新的connection，所以目前的代码有很大的问题。


怎么样才能回收connection？准确的说，应该是回收 connection 里面的result， the set 以及statement。要想实现这一点，我们需要创建一个新的类，叫 my connection。通过这个类实现什么？一回收 statement 2 回收result， the sets。 3 复用CONNECTION。怎么玩儿？可以这样弄 implements 一下connection，实现一下方法。要实现 n 多的方法，我们把注释放到最上面。





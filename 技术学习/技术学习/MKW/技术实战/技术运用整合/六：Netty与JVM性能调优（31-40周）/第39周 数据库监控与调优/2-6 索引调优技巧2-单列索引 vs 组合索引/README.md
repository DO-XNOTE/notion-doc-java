---
title: 2-6 索引调优技巧2-单列索引 vs 组合索引
---

# 2-6 索引调优技巧2-单列索引 vs 组合索引

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/ca489b23-1ee3-4806-bb51-d504c6e52a1d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VIE4LO4U%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230215Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDWdwKCk2VGpXkyF7%2F5m0XH%2BnbFRBzpXrzMiU9c%2BjDk3gIhAJyyDgdq7NR2B9nqGcgBN57jviIXITfc8wofH3%2FeoPHHKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyRuOvFuMf23iQLyzgq3AM2OhhQqKaxCBu4gMUmeoAh7kkq2JRHGvWD0rWuUE1U9HPdWjAxYOKNrPS7NlMXyvMG4Qwi%2Bbq%2F97gpAQXqOm1OV7bji9YlK4Jiwn5wdMFjw5gqY1Z1kfCgqMDF06llmhf0R7%2F4uurS1eJbo7xTkp6utgov3kbycMAfJ3vj%2BR28%2By9QyYfJyI%2F6nOmGNBuYTki%2BoLMXibagoELZEX955BWzDcPyq%2FZ94k929MTqZfWVK1spKp13qS8MuXFK5jUDgmxd2WXtkfyTgMJapyLF5jp6cilqm2M0vrFgr4RdCznRCeu36Spy09AueVcLEOHKnL%2BfiYIiEAA9y7jo4GPktK3pFSaYeO5urvKXlzKVsJf2CJWmCdSAqJaAYlC4u6%2FMlmuDtmKL1Q0TavpapX2bvzMDcUL81jiq3iAaNh5gxPooCBVbGGURnljb%2BGvMsgr8UhxCLWR4wqDeqiCSXK3vfXQcx8XumcGzChlpanKm%2FemHcdWByizSHToIEo26t%2FLjvFPEbSyDCSrzdO7YTQbN92IC4zWPYSAGW6hRAKEAMplJNFi7Vbf1YVmLUUgA4r8YmA%2Fg8l8684myO0yiwYH3i1ZzNut%2F4yojlGz7EopRTEz0EVbx7uO3yy%2B6hERGLTDLuP%2FSBjqkASPYhFjy%2BIVz1BaJvOsKRlc1THs53PxHiPsPgm1%2BbgYCp7A6oYCyvKjfGqPUpR6aAohpLlvRuHg4LmCBM%2FuUCE9dIRt2uEgW1ysSXSiN3u7OkixXt8og5Wnt%2F07IDhz2GlyLNUwdur6zZrVrwAIBnxAI9vZjLgCsozdijJIBy1QyWT3qLFdgvLWP4Iw0tKTm29hVtSfaNYhKarPdf8GEJpBXyMYF&X-Amz-Signature=4ebebab2c9a597d24f49024a080cf9e15bc674e96376e91db7d9bfd4e6566aa9&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/ca37133f-6117-4709-9fcd-19714885d4d0/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VIE4LO4U%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230215Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDWdwKCk2VGpXkyF7%2F5m0XH%2BnbFRBzpXrzMiU9c%2BjDk3gIhAJyyDgdq7NR2B9nqGcgBN57jviIXITfc8wofH3%2FeoPHHKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyRuOvFuMf23iQLyzgq3AM2OhhQqKaxCBu4gMUmeoAh7kkq2JRHGvWD0rWuUE1U9HPdWjAxYOKNrPS7NlMXyvMG4Qwi%2Bbq%2F97gpAQXqOm1OV7bji9YlK4Jiwn5wdMFjw5gqY1Z1kfCgqMDF06llmhf0R7%2F4uurS1eJbo7xTkp6utgov3kbycMAfJ3vj%2BR28%2By9QyYfJyI%2F6nOmGNBuYTki%2BoLMXibagoELZEX955BWzDcPyq%2FZ94k929MTqZfWVK1spKp13qS8MuXFK5jUDgmxd2WXtkfyTgMJapyLF5jp6cilqm2M0vrFgr4RdCznRCeu36Spy09AueVcLEOHKnL%2BfiYIiEAA9y7jo4GPktK3pFSaYeO5urvKXlzKVsJf2CJWmCdSAqJaAYlC4u6%2FMlmuDtmKL1Q0TavpapX2bvzMDcUL81jiq3iAaNh5gxPooCBVbGGURnljb%2BGvMsgr8UhxCLWR4wqDeqiCSXK3vfXQcx8XumcGzChlpanKm%2FemHcdWByizSHToIEo26t%2FLjvFPEbSyDCSrzdO7YTQbN92IC4zWPYSAGW6hRAKEAMplJNFi7Vbf1YVmLUUgA4r8YmA%2Fg8l8684myO0yiwYH3i1ZzNut%2F4yojlGz7EopRTEz0EVbx7uO3yy%2B6hERGLTDLuP%2FSBjqkASPYhFjy%2BIVz1BaJvOsKRlc1THs53PxHiPsPgm1%2BbgYCp7A6oYCyvKjfGqPUpR6aAohpLlvRuHg4LmCBM%2FuUCE9dIRt2uEgW1ysSXSiN3u7OkixXt8og5Wnt%2F07IDhz2GlyLNUwdur6zZrVrwAIBnxAI9vZjLgCsozdijJIBy1QyWT3qLFdgvLWP4Iw0tKTm29hVtSfaNYhKarPdf8GEJpBXyMYF&X-Amz-Signature=7b9783cc58e27bbe52fd534fa058e4f6e68f1b3c88360d0da707b0561b641083&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/54953bd6-dd18-4f8c-92c4-7f0f85b6f3bf/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VIE4LO4U%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230215Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDWdwKCk2VGpXkyF7%2F5m0XH%2BnbFRBzpXrzMiU9c%2BjDk3gIhAJyyDgdq7NR2B9nqGcgBN57jviIXITfc8wofH3%2FeoPHHKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyRuOvFuMf23iQLyzgq3AM2OhhQqKaxCBu4gMUmeoAh7kkq2JRHGvWD0rWuUE1U9HPdWjAxYOKNrPS7NlMXyvMG4Qwi%2Bbq%2F97gpAQXqOm1OV7bji9YlK4Jiwn5wdMFjw5gqY1Z1kfCgqMDF06llmhf0R7%2F4uurS1eJbo7xTkp6utgov3kbycMAfJ3vj%2BR28%2By9QyYfJyI%2F6nOmGNBuYTki%2BoLMXibagoELZEX955BWzDcPyq%2FZ94k929MTqZfWVK1spKp13qS8MuXFK5jUDgmxd2WXtkfyTgMJapyLF5jp6cilqm2M0vrFgr4RdCznRCeu36Spy09AueVcLEOHKnL%2BfiYIiEAA9y7jo4GPktK3pFSaYeO5urvKXlzKVsJf2CJWmCdSAqJaAYlC4u6%2FMlmuDtmKL1Q0TavpapX2bvzMDcUL81jiq3iAaNh5gxPooCBVbGGURnljb%2BGvMsgr8UhxCLWR4wqDeqiCSXK3vfXQcx8XumcGzChlpanKm%2FemHcdWByizSHToIEo26t%2FLjvFPEbSyDCSrzdO7YTQbN92IC4zWPYSAGW6hRAKEAMplJNFi7Vbf1YVmLUUgA4r8YmA%2Fg8l8684myO0yiwYH3i1ZzNut%2F4yojlGz7EopRTEz0EVbx7uO3yy%2B6hERGLTDLuP%2FSBjqkASPYhFjy%2BIVz1BaJvOsKRlc1THs53PxHiPsPgm1%2BbgYCp7A6oYCyvKjfGqPUpR6aAohpLlvRuHg4LmCBM%2FuUCE9dIRt2uEgW1ysSXSiN3u7OkixXt8og5Wnt%2F07IDhz2GlyLNUwdur6zZrVrwAIBnxAI9vZjLgCsozdijJIBy1QyWT3qLFdgvLWP4Iw0tKTm29hVtSfaNYhKarPdf8GEJpBXyMYF&X-Amz-Signature=dfc404268b3fdaf8f311585e2e9bd0766074dff600480570be387016608cb303&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

大家好，我是大木。这节课来探讨单列索引和组合索引对于查询的执行差异。现在比方我们有这样的一条SQL语句。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/3f380137-c018-4c35-821f-02158b5bbe76/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VIE4LO4U%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230215Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDWdwKCk2VGpXkyF7%2F5m0XH%2BnbFRBzpXrzMiU9c%2BjDk3gIhAJyyDgdq7NR2B9nqGcgBN57jviIXITfc8wofH3%2FeoPHHKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyRuOvFuMf23iQLyzgq3AM2OhhQqKaxCBu4gMUmeoAh7kkq2JRHGvWD0rWuUE1U9HPdWjAxYOKNrPS7NlMXyvMG4Qwi%2Bbq%2F97gpAQXqOm1OV7bji9YlK4Jiwn5wdMFjw5gqY1Z1kfCgqMDF06llmhf0R7%2F4uurS1eJbo7xTkp6utgov3kbycMAfJ3vj%2BR28%2By9QyYfJyI%2F6nOmGNBuYTki%2BoLMXibagoELZEX955BWzDcPyq%2FZ94k929MTqZfWVK1spKp13qS8MuXFK5jUDgmxd2WXtkfyTgMJapyLF5jp6cilqm2M0vrFgr4RdCznRCeu36Spy09AueVcLEOHKnL%2BfiYIiEAA9y7jo4GPktK3pFSaYeO5urvKXlzKVsJf2CJWmCdSAqJaAYlC4u6%2FMlmuDtmKL1Q0TavpapX2bvzMDcUL81jiq3iAaNh5gxPooCBVbGGURnljb%2BGvMsgr8UhxCLWR4wqDeqiCSXK3vfXQcx8XumcGzChlpanKm%2FemHcdWByizSHToIEo26t%2FLjvFPEbSyDCSrzdO7YTQbN92IC4zWPYSAGW6hRAKEAMplJNFi7Vbf1YVmLUUgA4r8YmA%2Fg8l8684myO0yiwYH3i1ZzNut%2F4yojlGz7EopRTEz0EVbx7uO3yy%2B6hERGLTDLuP%2FSBjqkASPYhFjy%2BIVz1BaJvOsKRlc1THs53PxHiPsPgm1%2BbgYCp7A6oYCyvKjfGqPUpR6aAohpLlvRuHg4LmCBM%2FuUCE9dIRt2uEgW1ysSXSiN3u7OkixXt8og5Wnt%2F07IDhz2GlyLNUwdur6zZrVrwAIBnxAI9vZjLgCsozdijJIBy1QyWT3qLFdgvLWP4Iw0tKTm29hVtSfaNYhKarPdf8GEJpBXyMYF&X-Amz-Signature=690c636f7569cbbc57b9b23a95043cc165867c5ac3dcf70750b5eaea1054526e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

目前在 salary 表上并没有创建任何的索引，所以当我们 explain 的时候，它会展示 type all 也就是全表扫描。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/ae85433b-c15f-41ef-a7af-bd8a93e94dee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VIE4LO4U%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230215Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDWdwKCk2VGpXkyF7%2F5m0XH%2BnbFRBzpXrzMiU9c%2BjDk3gIhAJyyDgdq7NR2B9nqGcgBN57jviIXITfc8wofH3%2FeoPHHKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyRuOvFuMf23iQLyzgq3AM2OhhQqKaxCBu4gMUmeoAh7kkq2JRHGvWD0rWuUE1U9HPdWjAxYOKNrPS7NlMXyvMG4Qwi%2Bbq%2F97gpAQXqOm1OV7bji9YlK4Jiwn5wdMFjw5gqY1Z1kfCgqMDF06llmhf0R7%2F4uurS1eJbo7xTkp6utgov3kbycMAfJ3vj%2BR28%2By9QyYfJyI%2F6nOmGNBuYTki%2BoLMXibagoELZEX955BWzDcPyq%2FZ94k929MTqZfWVK1spKp13qS8MuXFK5jUDgmxd2WXtkfyTgMJapyLF5jp6cilqm2M0vrFgr4RdCznRCeu36Spy09AueVcLEOHKnL%2BfiYIiEAA9y7jo4GPktK3pFSaYeO5urvKXlzKVsJf2CJWmCdSAqJaAYlC4u6%2FMlmuDtmKL1Q0TavpapX2bvzMDcUL81jiq3iAaNh5gxPooCBVbGGURnljb%2BGvMsgr8UhxCLWR4wqDeqiCSXK3vfXQcx8XumcGzChlpanKm%2FemHcdWByizSHToIEo26t%2FLjvFPEbSyDCSrzdO7YTQbN92IC4zWPYSAGW6hRAKEAMplJNFi7Vbf1YVmLUUgA4r8YmA%2Fg8l8684myO0yiwYH3i1ZzNut%2F4yojlGz7EopRTEz0EVbx7uO3yy%2B6hERGLTDLuP%2FSBjqkASPYhFjy%2BIVz1BaJvOsKRlc1THs53PxHiPsPgm1%2BbgYCp7A6oYCyvKjfGqPUpR6aAohpLlvRuHg4LmCBM%2FuUCE9dIRt2uEgW1ysSXSiN3u7OkixXt8og5Wnt%2F07IDhz2GlyLNUwdur6zZrVrwAIBnxAI9vZjLgCsozdijJIBy1QyWT3qLFdgvLWP4Iw0tKTm29hVtSfaNYhKarPdf8GEJpBXyMYF&X-Amz-Signature=9f03cbc08d59e9796d3d9e172ab5054a6b8dede50a196bda748d6188633195be&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

下面我们来创建两个单列索引。 modify table indices 创建第一个索引，作用在 from date 上。再创建第二个索引，作用在 to date 上。 execute 点大索引创建完成，他就好了。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/24dbf034-1871-4a04-bf35-33ef806589d6/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VIE4LO4U%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230215Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDWdwKCk2VGpXkyF7%2F5m0XH%2BnbFRBzpXrzMiU9c%2BjDk3gIhAJyyDgdq7NR2B9nqGcgBN57jviIXITfc8wofH3%2FeoPHHKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyRuOvFuMf23iQLyzgq3AM2OhhQqKaxCBu4gMUmeoAh7kkq2JRHGvWD0rWuUE1U9HPdWjAxYOKNrPS7NlMXyvMG4Qwi%2Bbq%2F97gpAQXqOm1OV7bji9YlK4Jiwn5wdMFjw5gqY1Z1kfCgqMDF06llmhf0R7%2F4uurS1eJbo7xTkp6utgov3kbycMAfJ3vj%2BR28%2By9QyYfJyI%2F6nOmGNBuYTki%2BoLMXibagoELZEX955BWzDcPyq%2FZ94k929MTqZfWVK1spKp13qS8MuXFK5jUDgmxd2WXtkfyTgMJapyLF5jp6cilqm2M0vrFgr4RdCznRCeu36Spy09AueVcLEOHKnL%2BfiYIiEAA9y7jo4GPktK3pFSaYeO5urvKXlzKVsJf2CJWmCdSAqJaAYlC4u6%2FMlmuDtmKL1Q0TavpapX2bvzMDcUL81jiq3iAaNh5gxPooCBVbGGURnljb%2BGvMsgr8UhxCLWR4wqDeqiCSXK3vfXQcx8XumcGzChlpanKm%2FemHcdWByizSHToIEo26t%2FLjvFPEbSyDCSrzdO7YTQbN92IC4zWPYSAGW6hRAKEAMplJNFi7Vbf1YVmLUUgA4r8YmA%2Fg8l8684myO0yiwYH3i1ZzNut%2F4yojlGz7EopRTEz0EVbx7uO3yy%2B6hERGLTDLuP%2FSBjqkASPYhFjy%2BIVz1BaJvOsKRlc1THs53PxHiPsPgm1%2BbgYCp7A6oYCyvKjfGqPUpR6aAohpLlvRuHg4LmCBM%2FuUCE9dIRt2uEgW1ysSXSiN3u7OkixXt8og5Wnt%2F07IDhz2GlyLNUwdur6zZrVrwAIBnxAI9vZjLgCsozdijJIBy1QyWT3qLFdgvLWP4Iw0tKTm29hVtSfaNYhKarPdf8GEJpBXyMYF&X-Amz-Signature=e2b84c4600951b894bfe88e81b7a723b71e7b6aa03b7af5c71dd7e440e2807a3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

执行一下这条 select 语句。执行点击 output 可以发现了这条SQL，需要花费 68 毫秒。我们记录一下。创建单列索引，花费 68 毫秒。再来执行explain，可以发现 tab 是 index merge，也就是发生了索引合并。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/97edabe5-8fd6-4e07-b81a-f8463798b6c4/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VIE4LO4U%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230215Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDWdwKCk2VGpXkyF7%2F5m0XH%2BnbFRBzpXrzMiU9c%2BjDk3gIhAJyyDgdq7NR2B9nqGcgBN57jviIXITfc8wofH3%2FeoPHHKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyRuOvFuMf23iQLyzgq3AM2OhhQqKaxCBu4gMUmeoAh7kkq2JRHGvWD0rWuUE1U9HPdWjAxYOKNrPS7NlMXyvMG4Qwi%2Bbq%2F97gpAQXqOm1OV7bji9YlK4Jiwn5wdMFjw5gqY1Z1kfCgqMDF06llmhf0R7%2F4uurS1eJbo7xTkp6utgov3kbycMAfJ3vj%2BR28%2By9QyYfJyI%2F6nOmGNBuYTki%2BoLMXibagoELZEX955BWzDcPyq%2FZ94k929MTqZfWVK1spKp13qS8MuXFK5jUDgmxd2WXtkfyTgMJapyLF5jp6cilqm2M0vrFgr4RdCznRCeu36Spy09AueVcLEOHKnL%2BfiYIiEAA9y7jo4GPktK3pFSaYeO5urvKXlzKVsJf2CJWmCdSAqJaAYlC4u6%2FMlmuDtmKL1Q0TavpapX2bvzMDcUL81jiq3iAaNh5gxPooCBVbGGURnljb%2BGvMsgr8UhxCLWR4wqDeqiCSXK3vfXQcx8XumcGzChlpanKm%2FemHcdWByizSHToIEo26t%2FLjvFPEbSyDCSrzdO7YTQbN92IC4zWPYSAGW6hRAKEAMplJNFi7Vbf1YVmLUUgA4r8YmA%2Fg8l8684myO0yiwYH3i1ZzNut%2F4yojlGz7EopRTEz0EVbx7uO3yy%2B6hERGLTDLuP%2FSBjqkASPYhFjy%2BIVz1BaJvOsKRlc1THs53PxHiPsPgm1%2BbgYCp7A6oYCyvKjfGqPUpR6aAohpLlvRuHg4LmCBM%2FuUCE9dIRt2uEgW1ysSXSiN3u7OkixXt8og5Wnt%2F07IDhz2GlyLNUwdur6zZrVrwAIBnxAI9vZjLgCsozdijJIBy1QyWT3qLFdgvLWP4Iw0tKTm29hVtSfaNYhKarPdf8GEJpBXyMYF&X-Amz-Signature=c37812d3554b9ac218c010e37260d2fd735988ac3189e0333b398769e640b895&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

使用带的索引是我们刚刚创建的 2 个单列索引，而 extra 里面有一个 using intersect， 

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/4b73a17b-c3b2-4668-981d-88ab7b8d0a53/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VIE4LO4U%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230215Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDWdwKCk2VGpXkyF7%2F5m0XH%2BnbFRBzpXrzMiU9c%2BjDk3gIhAJyyDgdq7NR2B9nqGcgBN57jviIXITfc8wofH3%2FeoPHHKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyRuOvFuMf23iQLyzgq3AM2OhhQqKaxCBu4gMUmeoAh7kkq2JRHGvWD0rWuUE1U9HPdWjAxYOKNrPS7NlMXyvMG4Qwi%2Bbq%2F97gpAQXqOm1OV7bji9YlK4Jiwn5wdMFjw5gqY1Z1kfCgqMDF06llmhf0R7%2F4uurS1eJbo7xTkp6utgov3kbycMAfJ3vj%2BR28%2By9QyYfJyI%2F6nOmGNBuYTki%2BoLMXibagoELZEX955BWzDcPyq%2FZ94k929MTqZfWVK1spKp13qS8MuXFK5jUDgmxd2WXtkfyTgMJapyLF5jp6cilqm2M0vrFgr4RdCznRCeu36Spy09AueVcLEOHKnL%2BfiYIiEAA9y7jo4GPktK3pFSaYeO5urvKXlzKVsJf2CJWmCdSAqJaAYlC4u6%2FMlmuDtmKL1Q0TavpapX2bvzMDcUL81jiq3iAaNh5gxPooCBVbGGURnljb%2BGvMsgr8UhxCLWR4wqDeqiCSXK3vfXQcx8XumcGzChlpanKm%2FemHcdWByizSHToIEo26t%2FLjvFPEbSyDCSrzdO7YTQbN92IC4zWPYSAGW6hRAKEAMplJNFi7Vbf1YVmLUUgA4r8YmA%2Fg8l8684myO0yiwYH3i1ZzNut%2F4yojlGz7EopRTEz0EVbx7uO3yy%2B6hERGLTDLuP%2FSBjqkASPYhFjy%2BIVz1BaJvOsKRlc1THs53PxHiPsPgm1%2BbgYCp7A6oYCyvKjfGqPUpR6aAohpLlvRuHg4LmCBM%2FuUCE9dIRt2uEgW1ysSXSiN3u7OkixXt8og5Wnt%2F07IDhz2GlyLNUwdur6zZrVrwAIBnxAI9vZjLgCsozdijJIBy1QyWT3qLFdgvLWP4Iw0tKTm29hVtSfaNYhKarPdf8GEJpBXyMYF&X-Amz-Signature=b55c58adb3119b7eebfa78726c9acc3d8286bf20580fcbd1a765063c71bcaa4c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

**intersect 的意思是交集的意思**。括号里面写上了我们的两个索引，表示使用这两个索引做了一个求交集的操作。


我们可以使用 optimizer trace 来看一下这条 sql。更加详细的执行过程。首先开启 optimizer trace，执行一下我们的 SQL 运行。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/cb2388f2-70b0-48cf-8417-e80d8a51ed2c/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VIE4LO4U%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230215Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDWdwKCk2VGpXkyF7%2F5m0XH%2BnbFRBzpXrzMiU9c%2BjDk3gIhAJyyDgdq7NR2B9nqGcgBN57jviIXITfc8wofH3%2FeoPHHKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyRuOvFuMf23iQLyzgq3AM2OhhQqKaxCBu4gMUmeoAh7kkq2JRHGvWD0rWuUE1U9HPdWjAxYOKNrPS7NlMXyvMG4Qwi%2Bbq%2F97gpAQXqOm1OV7bji9YlK4Jiwn5wdMFjw5gqY1Z1kfCgqMDF06llmhf0R7%2F4uurS1eJbo7xTkp6utgov3kbycMAfJ3vj%2BR28%2By9QyYfJyI%2F6nOmGNBuYTki%2BoLMXibagoELZEX955BWzDcPyq%2FZ94k929MTqZfWVK1spKp13qS8MuXFK5jUDgmxd2WXtkfyTgMJapyLF5jp6cilqm2M0vrFgr4RdCznRCeu36Spy09AueVcLEOHKnL%2BfiYIiEAA9y7jo4GPktK3pFSaYeO5urvKXlzKVsJf2CJWmCdSAqJaAYlC4u6%2FMlmuDtmKL1Q0TavpapX2bvzMDcUL81jiq3iAaNh5gxPooCBVbGGURnljb%2BGvMsgr8UhxCLWR4wqDeqiCSXK3vfXQcx8XumcGzChlpanKm%2FemHcdWByizSHToIEo26t%2FLjvFPEbSyDCSrzdO7YTQbN92IC4zWPYSAGW6hRAKEAMplJNFi7Vbf1YVmLUUgA4r8YmA%2Fg8l8684myO0yiwYH3i1ZzNut%2F4yojlGz7EopRTEz0EVbx7uO3yy%2B6hERGLTDLuP%2FSBjqkASPYhFjy%2BIVz1BaJvOsKRlc1THs53PxHiPsPgm1%2BbgYCp7A6oYCyvKjfGqPUpR6aAohpLlvRuHg4LmCBM%2FuUCE9dIRt2uEgW1ysSXSiN3u7OkixXt8og5Wnt%2F07IDhz2GlyLNUwdur6zZrVrwAIBnxAI9vZjLgCsozdijJIBy1QyWT3qLFdgvLWP4Iw0tKTm29hVtSfaNYhKarPdf8GEJpBXyMYF&X-Amz-Signature=ccd7a6569209c019c1788046800b4f1a7bbae2a71ec67f5043cd432d10ea1d01&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

接着 show select sing from。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/372430ec-16ac-4137-8bd1-dcefe6048926/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VIE4LO4U%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230215Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDWdwKCk2VGpXkyF7%2F5m0XH%2BnbFRBzpXrzMiU9c%2BjDk3gIhAJyyDgdq7NR2B9nqGcgBN57jviIXITfc8wofH3%2FeoPHHKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyRuOvFuMf23iQLyzgq3AM2OhhQqKaxCBu4gMUmeoAh7kkq2JRHGvWD0rWuUE1U9HPdWjAxYOKNrPS7NlMXyvMG4Qwi%2Bbq%2F97gpAQXqOm1OV7bji9YlK4Jiwn5wdMFjw5gqY1Z1kfCgqMDF06llmhf0R7%2F4uurS1eJbo7xTkp6utgov3kbycMAfJ3vj%2BR28%2By9QyYfJyI%2F6nOmGNBuYTki%2BoLMXibagoELZEX955BWzDcPyq%2FZ94k929MTqZfWVK1spKp13qS8MuXFK5jUDgmxd2WXtkfyTgMJapyLF5jp6cilqm2M0vrFgr4RdCznRCeu36Spy09AueVcLEOHKnL%2BfiYIiEAA9y7jo4GPktK3pFSaYeO5urvKXlzKVsJf2CJWmCdSAqJaAYlC4u6%2FMlmuDtmKL1Q0TavpapX2bvzMDcUL81jiq3iAaNh5gxPooCBVbGGURnljb%2BGvMsgr8UhxCLWR4wqDeqiCSXK3vfXQcx8XumcGzChlpanKm%2FemHcdWByizSHToIEo26t%2FLjvFPEbSyDCSrzdO7YTQbN92IC4zWPYSAGW6hRAKEAMplJNFi7Vbf1YVmLUUgA4r8YmA%2Fg8l8684myO0yiwYH3i1ZzNut%2F4yojlGz7EopRTEz0EVbx7uO3yy%2B6hERGLTDLuP%2FSBjqkASPYhFjy%2BIVz1BaJvOsKRlc1THs53PxHiPsPgm1%2BbgYCp7A6oYCyvKjfGqPUpR6aAohpLlvRuHg4LmCBM%2FuUCE9dIRt2uEgW1ysSXSiN3u7OkixXt8og5Wnt%2F07IDhz2GlyLNUwdur6zZrVrwAIBnxAI9vZjLgCsozdijJIBy1QyWT3qLFdgvLWP4Iw0tKTm29hVtSfaNYhKarPdf8GEJpBXyMYF&X-Amz-Signature=23d0f041610cfc299c47d898452f2eff3b4899dc8928daaaa1cc27515fab293a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

More information schema they are optimize the trees where Perry.
three like 比方Salaries limit 30 ，执行全选 trace 的结果，贴到结算文件里面来。

```json
{
  "steps": [
    {
      "join_preparation": {
        "select#": 1,
        "steps": [
          {
            "expanded_query": "/* select#1 */ select `salaries`.`emp_no` AS `emp_no`,`salaries`.`salary` AS `salary`,`salaries`.`from_date` AS `from_date`,`salaries`.`to_date` AS `to_date` from `salaries` where ((`salaries`.`from_date` = '1986-06-26') and (`salaries`.`to_date` = '1987-06-26'))"
          }
        ] /* steps */
      } /* join_preparation */
    },
    {
      "join_optimization": {
        "select#": 1,
        "steps": [
          {
            "condition_processing": {
              "condition": "WHERE",
              "original_condition": "((`salaries`.`from_date` = '1986-06-26') and (`salaries`.`to_date` = '1987-06-26'))",
              "steps": [
                {
                  "transformation": "equality_propagation",
                  "resulting_condition": "(multiple equal('1986-06-26', `salaries`.`from_date`) and multiple equal('1987-06-26', `salaries`.`to_date`))"
                },
                {
                  "transformation": "constant_propagation",
                  "resulting_condition": "(multiple equal('1986-06-26', `salaries`.`from_date`) and multiple equal('1987-06-26', `salaries`.`to_date`))"
                },
                {
                  "transformation": "trivial_condition_removal",
                  "resulting_condition": "(multiple equal(DATE'1986-06-26', `salaries`.`from_date`) and multiple equal(DATE'1987-06-26', `salaries`.`to_date`))"
                }
              ] /* steps */
            } /* condition_processing */
          },
          {
            "substitute_generated_columns": {
            } /* substitute_generated_columns */
          },
          {
            "table_dependencies": [
              {
                "table": "`salaries`",
                "row_may_be_null": false,
                "map_bit": 0,
                "depends_on_map_bits": [
                ] /* depends_on_map_bits */
              }
            ] /* table_dependencies */
          },
          {
            "ref_optimizer_key_uses": [
              {
                "table": "`salaries`",
                "field": "from_date",
                "equals": "DATE'1986-06-26'",
                "null_rejecting": true
              },
              {
                "table": "`salaries`",
                "field": "to_date",
                "equals": "DATE'1987-06-26'",
                "null_rejecting": true
              }
            ] /* ref_optimizer_key_uses */
          },
          {
            "rows_estimation": [
              {
                "table": "`salaries`",
                "range_analysis": {
                  "table_scan": {
                    "rows": 2838426,
                    "cost": 2.29708e+06
                  } /* table_scan */,
                  "potential_range_indexes": [    // 这张表中所有的索引
                    {
                      "index": "PRIMARY",
                      "usable": false,  // 主键是不可用的
                      "cause": "not_applicable"
                    },
                    {
                      "index": "salaries_from_date_index",
                      "usable": true,  // 作用在 from_date 的索引是可用的
                      "key_parts": [
                        "from_date",
                        "emp_no"
                      ] /* key_parts */
                    },
                    {
                      "index": "salaries_to_date_index",
                      "usable": true,   // 作用在 to_date 的索引是可用的
                      "key_parts": [
                        "to_date",
                        "emp_no",
                        "from_date"
                      ] /* key_parts */
                    }
                  ] /* potential_range_indexes */,
                  "setup_range_conditions": [
                  ] /* setup_range_conditions */,
                  "group_index_range": {
                    "chosen": false,
                    "cause": "not_group_by_or_distinct"
                  } /* group_index_range */,
                  "skip_scan_range": {  // 分析是否可以执行跳跃扫描 mysq8.0引入的新特性，mysql 内部
                    "potential_skip_scan_indexes": [
                      {
                        "index": "salaries_from_date_index",
                        "usable": false, //  不可用
                        "cause": "query_references_nonkey_column"
                      },
                      {
                        "index": "salaries_to_date_index",
                        "usable": false,
                        "cause": "query_references_nonkey_column"
                      }
                    ] /* potential_skip_scan_indexes */
                  } /* skip_scan_range */,
                  "analyzing_range_alternatives": {
                    "range_scan_alternatives": [
                      {
                        "index": "salaries_from_date_index",
                        "ranges": [
                          "from_date = '1986-06-26'"
                        ] /* ranges */,
                        "index_dives_for_eq_ranges": true,
                        "rowid_ordered": true,
                        "using_mrr": false,
                        "index_only": false,
                        "in_memory": 0,
                        "rows": 88,
                        "cost": 71.9359,
                        "chosen": true
                      },
                      {
                        "index": "salaries_to_date_index",
                        "ranges": [
                          "to_date = '1987-06-26'"
                        ] /* ranges */,
                        "index_dives_for_eq_ranges": true,
                        "rowid_ordered": true,
                        "using_mrr": false,
                        "index_only": false,
                        "in_memory": 0,
                        "rows": 86,
                        "cost": 70.3173,
                        "chosen": true
                      }
                    ] /* range_scan_alternatives */,
                    "analyzing_roworder_intersect": {
                      "intersecting_indexes": [
                        {
                          "index": "salaries_to_date_index",
                          "index_scan_cost": 1.10366,
                          "cumulated_index_scan_cost": 1.10366,
                          "disk_sweep_cost": 60.8922,
                          "cumulated_total_cost": 61.9959,
                          "usable": true,
                          "matching_rows_now": 86,
                          "isect_covering_with_this_index": false,
                          "chosen": true
                        },
                        {
                          "index": "salaries_from_date_index",
                          "index_scan_cost": 1.14846,
                          "cumulated_index_scan_cost": 2.25212,
                          "disk_sweep_cost": 0,
                          "cumulated_total_cost": 2.25212,
                          "usable": true,
                          "matching_rows_now": 0.00266627,
                          "isect_covering_with_this_index": false,
                          "chosen": true
                        }
                      ] /* intersecting_indexes */,
                      "clustered_pk": {
                        "clustered_pk_added_to_intersect": false,
                        "cause": "no_clustered_pk_index"
                      } /* clustered_pk */,
                      "rows": 1,
                      "cost": 2.25212,
                      "covering": false,
                      "chosen": true
                    } /* analyzing_roworder_intersect */
                  } /* analyzing_range_alternatives */,
                  "chosen_range_access_summary": {
                    "range_access_plan": {
                      "type": "index_roworder_intersect",
                      "rows": 1,
                      "cost": 2.25212,
                      "covering": false,
                      "clustered_pk_scan": false,
                      "intersect_of": [
                        {
                          "type": "range_scan",
                          "index": "salaries_to_date_index",
                          "rows": 86,
                          "ranges": [
                            "to_date = '1987-06-26'"
                          ] /* ranges */
                        },
                        {
                          "type": "range_scan",
                          "index": "salaries_from_date_index",
                          "rows": 88,
                          "ranges": [
                            "from_date = '1986-06-26'"
                          ] /* ranges */
                        }
                      ] /* intersect_of */
                    } /* range_access_plan */,
                    "rows_for_plan": 1,
                    "cost_for_plan": 2.25212,
                    "chosen": true
                  } /* chosen_range_access_summary */
                } /* range_analysis */
              }
            ] /* rows_estimation */
          },
          {
            "considered_execution_plans": [
              {
                "plan_prefix": [
                ] /* plan_prefix */,
                "table": "`salaries`",
                "best_access_path": {
                  "considered_access_paths": [
                    {
                      "access_type": "ref",
                      "index": "salaries_from_date_index",
                      "rows": 88,
                      "cost": 71.2166,
                      "chosen": true
                    },
                    {
                      "access_type": "ref",
                      "index": "salaries_to_date_index",
                      "rows": 86,
                      "cost": 69.598,
                      "chosen": true
                    },
                    {
                      "rows_to_scan": 1,
                      "access_type": "range",
                      "range_details": {
                        "used_index": "intersect(salaries_to_date_index,salaries_from_date_index)"
                      } /* range_details */,
                      "resulting_rows": 1,
                      "cost": 2.35212,
                      "chosen": true
                    }
                  ] /* considered_access_paths */
                } /* best_access_path */,
                "condition_filtering_pct": 100,
                "rows_for_plan": 1,
                "cost_for_plan": 2.35212,
                "chosen": true
              }
            ] /* considered_execution_plans */
          },
          {
            "attaching_conditions_to_tables": {
              "original_condition": "((`salaries`.`to_date` = DATE'1987-06-26') and (`salaries`.`from_date` = DATE'1986-06-26'))",
              "attached_conditions_computation": [
              ] /* attached_conditions_computation */,
              "attached_conditions_summary": [
                {
                  "table": "`salaries`",
                  "attached": "((`salaries`.`to_date` = DATE'1987-06-26') and (`salaries`.`from_date` = DATE'1986-06-26'))"
                }
              ] /* attached_conditions_summary */
            } /* attaching_conditions_to_tables */
          },
          {
            "finalizing_table_conditions": [
              {
                "table": "`salaries`",
                "original_table_condition": "((`salaries`.`to_date` = DATE'1987-06-26') and (`salaries`.`from_date` = DATE'1986-06-26'))",
                "final_table_condition   ": "((`salaries`.`to_date` = DATE'1987-06-26') and (`salaries`.`from_date` = DATE'1986-06-26'))"
              }
            ] /* finalizing_table_conditions */
          },
          {
            "refine_plan": [
              {
                "table": "`salaries`"
              }
            ] /* refine_plan */
          }
        ] /* steps */
      } /* join_optimization */
    },
    {
      "join_execution": {
        "select#": 1,
        "steps": [
        ] /* steps */
      } /* join_execution */
    }
  ] /* steps */
}
```

前面说过 optimizer trace 对于单表查询，最重要的是肉丝estimation，对吧？我们来分析一下。首先 tablescan 他说如果做全表扫描，需要扫描这么多行开销是这样子的。


potential range indexes 它列出了这张表里面的所有索引，并分析是不是可用。主键是不可用的，作用在 from date 上面的索引是可用的，重在 to date 上面的索引也是可用的。 set up a range condition 词没有内容，不理它。 group next range 因为我们没有 group 操作，所以 chosen 是false，不用理它。 skip scan range 去分析是否能够执行跳跃扫描。 


skip scan range 是 MySQL 8. 0 引入的一个新特性，它可以在 MySQL 内部优化特定的查询，同学们感兴趣可以百度一下。当然不了解也没有太大关系。 usable 都是false，不能skip。最重要的部分 analyzing range alternatives 分析各个索引的使用成本。他说作用在 from data 上面的索引，预估会扫描 88 行，开销是 72. 541。记录下copy，粘贴 from data index。而作用在 to day 的上面的索引，预估会扫描 86 行，开销是 70. 909。


two eight index 开箱是这样子的，并且这两个索引的 choosen 都是true，说明这两个索引都使用了。接着， analyzing reward in effect 用来做索引合并。 in affecting indexes 表示做交集操作的索引有哪些？目前来说有两个 choosing true。求交集的开销是这么大，记录一下求交集。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e9431727-8eb1-4b4e-8d36-5a6b6e8c1e91/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VIE4LO4U%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDWdwKCk2VGpXkyF7%2F5m0XH%2BnbFRBzpXrzMiU9c%2BjDk3gIhAJyyDgdq7NR2B9nqGcgBN57jviIXITfc8wofH3%2FeoPHHKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyRuOvFuMf23iQLyzgq3AM2OhhQqKaxCBu4gMUmeoAh7kkq2JRHGvWD0rWuUE1U9HPdWjAxYOKNrPS7NlMXyvMG4Qwi%2Bbq%2F97gpAQXqOm1OV7bji9YlK4Jiwn5wdMFjw5gqY1Z1kfCgqMDF06llmhf0R7%2F4uurS1eJbo7xTkp6utgov3kbycMAfJ3vj%2BR28%2By9QyYfJyI%2F6nOmGNBuYTki%2BoLMXibagoELZEX955BWzDcPyq%2FZ94k929MTqZfWVK1spKp13qS8MuXFK5jUDgmxd2WXtkfyTgMJapyLF5jp6cilqm2M0vrFgr4RdCznRCeu36Spy09AueVcLEOHKnL%2BfiYIiEAA9y7jo4GPktK3pFSaYeO5urvKXlzKVsJf2CJWmCdSAqJaAYlC4u6%2FMlmuDtmKL1Q0TavpapX2bvzMDcUL81jiq3iAaNh5gxPooCBVbGGURnljb%2BGvMsgr8UhxCLWR4wqDeqiCSXK3vfXQcx8XumcGzChlpanKm%2FemHcdWByizSHToIEo26t%2FLjvFPEbSyDCSrzdO7YTQbN92IC4zWPYSAGW6hRAKEAMplJNFi7Vbf1YVmLUUgA4r8YmA%2Fg8l8684myO0yiwYH3i1ZzNut%2F4yojlGz7EopRTEz0EVbx7uO3yy%2B6hERGLTDLuP%2FSBjqkASPYhFjy%2BIVz1BaJvOsKRlc1THs53PxHiPsPgm1%2BbgYCp7A6oYCyvKjfGqPUpR6aAohpLlvRuHg4LmCBM%2FuUCE9dIRt2uEgW1ysSXSiN3u7OkixXt8og5Wnt%2F07IDhz2GlyLNUwdur6zZrVrwAIBnxAI9vZjLgCsozdijJIBy1QyWT3qLFdgvLWP4Iw0tKTm29hVtSfaNYhKarPdf8GEJpBXyMYF&X-Amz-Signature=f70358285d9653208052c2101b85ec63e7681d35906b91460a66cb54e3fc47e4&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

OK，下面我们再来做一个实验。我们把 salaries 表上面刚刚创建的两个单列索引给去掉，然后重新创建一个组合索引，装在 from data 字段以及 to data 字段下面。Execute。


再次执行 explain 这条语句。可以发现这一次 type 变成了ref。前面讲解 explain 的时候有说过， type 的性能从好到坏排序如下

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/662fef6e-bdf3-4907-b49c-32ac46e7e810/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VIE4LO4U%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDWdwKCk2VGpXkyF7%2F5m0XH%2BnbFRBzpXrzMiU9c%2BjDk3gIhAJyyDgdq7NR2B9nqGcgBN57jviIXITfc8wofH3%2FeoPHHKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyRuOvFuMf23iQLyzgq3AM2OhhQqKaxCBu4gMUmeoAh7kkq2JRHGvWD0rWuUE1U9HPdWjAxYOKNrPS7NlMXyvMG4Qwi%2Bbq%2F97gpAQXqOm1OV7bji9YlK4Jiwn5wdMFjw5gqY1Z1kfCgqMDF06llmhf0R7%2F4uurS1eJbo7xTkp6utgov3kbycMAfJ3vj%2BR28%2By9QyYfJyI%2F6nOmGNBuYTki%2BoLMXibagoELZEX955BWzDcPyq%2FZ94k929MTqZfWVK1spKp13qS8MuXFK5jUDgmxd2WXtkfyTgMJapyLF5jp6cilqm2M0vrFgr4RdCznRCeu36Spy09AueVcLEOHKnL%2BfiYIiEAA9y7jo4GPktK3pFSaYeO5urvKXlzKVsJf2CJWmCdSAqJaAYlC4u6%2FMlmuDtmKL1Q0TavpapX2bvzMDcUL81jiq3iAaNh5gxPooCBVbGGURnljb%2BGvMsgr8UhxCLWR4wqDeqiCSXK3vfXQcx8XumcGzChlpanKm%2FemHcdWByizSHToIEo26t%2FLjvFPEbSyDCSrzdO7YTQbN92IC4zWPYSAGW6hRAKEAMplJNFi7Vbf1YVmLUUgA4r8YmA%2Fg8l8684myO0yiwYH3i1ZzNut%2F4yojlGz7EopRTEz0EVbx7uO3yy%2B6hERGLTDLuP%2FSBjqkASPYhFjy%2BIVz1BaJvOsKRlc1THs53PxHiPsPgm1%2BbgYCp7A6oYCyvKjfGqPUpR6aAohpLlvRuHg4LmCBM%2FuUCE9dIRt2uEgW1ysSXSiN3u7OkixXt8og5Wnt%2F07IDhz2GlyLNUwdur6zZrVrwAIBnxAI9vZjLgCsozdijJIBy1QyWT3qLFdgvLWP4Iw0tKTm29hVtSfaNYhKarPdf8GEJpBXyMYF&X-Amz-Signature=253489cd5cc199615a0d2cffdfe148c9f75cda32d4f77f3f9efd91072c813ec5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

 ref 是排在第四的，而 index merge 还在了后面。也就是我们使用组合索引性能比刚刚的两个单列索引应该要好一些。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/abb58e05-dab1-4679-9990-a67e4456056a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VIE4LO4U%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDWdwKCk2VGpXkyF7%2F5m0XH%2BnbFRBzpXrzMiU9c%2BjDk3gIhAJyyDgdq7NR2B9nqGcgBN57jviIXITfc8wofH3%2FeoPHHKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyRuOvFuMf23iQLyzgq3AM2OhhQqKaxCBu4gMUmeoAh7kkq2JRHGvWD0rWuUE1U9HPdWjAxYOKNrPS7NlMXyvMG4Qwi%2Bbq%2F97gpAQXqOm1OV7bji9YlK4Jiwn5wdMFjw5gqY1Z1kfCgqMDF06llmhf0R7%2F4uurS1eJbo7xTkp6utgov3kbycMAfJ3vj%2BR28%2By9QyYfJyI%2F6nOmGNBuYTki%2BoLMXibagoELZEX955BWzDcPyq%2FZ94k929MTqZfWVK1spKp13qS8MuXFK5jUDgmxd2WXtkfyTgMJapyLF5jp6cilqm2M0vrFgr4RdCznRCeu36Spy09AueVcLEOHKnL%2BfiYIiEAA9y7jo4GPktK3pFSaYeO5urvKXlzKVsJf2CJWmCdSAqJaAYlC4u6%2FMlmuDtmKL1Q0TavpapX2bvzMDcUL81jiq3iAaNh5gxPooCBVbGGURnljb%2BGvMsgr8UhxCLWR4wqDeqiCSXK3vfXQcx8XumcGzChlpanKm%2FemHcdWByizSHToIEo26t%2FLjvFPEbSyDCSrzdO7YTQbN92IC4zWPYSAGW6hRAKEAMplJNFi7Vbf1YVmLUUgA4r8YmA%2Fg8l8684myO0yiwYH3i1ZzNut%2F4yojlGz7EopRTEz0EVbx7uO3yy%2B6hERGLTDLuP%2FSBjqkASPYhFjy%2BIVz1BaJvOsKRlc1THs53PxHiPsPgm1%2BbgYCp7A6oYCyvKjfGqPUpR6aAohpLlvRuHg4LmCBM%2FuUCE9dIRt2uEgW1ysSXSiN3u7OkixXt8og5Wnt%2F07IDhz2GlyLNUwdur6zZrVrwAIBnxAI9vZjLgCsozdijJIBy1QyWT3qLFdgvLWP4Iw0tKTm29hVtSfaNYhKarPdf8GEJpBXyMYF&X-Amz-Signature=dfcc280ffaaab25e94cb9bff8d80f6158aa65ac7c84a97fb4d1ddb3cb695ac99&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

key 我们发现使用到了我们刚刚的组合索引。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/4a97c1cf-3eba-4d80-9067-ab0f98a4fa4a/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VIE4LO4U%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDWdwKCk2VGpXkyF7%2F5m0XH%2BnbFRBzpXrzMiU9c%2BjDk3gIhAJyyDgdq7NR2B9nqGcgBN57jviIXITfc8wofH3%2FeoPHHKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyRuOvFuMf23iQLyzgq3AM2OhhQqKaxCBu4gMUmeoAh7kkq2JRHGvWD0rWuUE1U9HPdWjAxYOKNrPS7NlMXyvMG4Qwi%2Bbq%2F97gpAQXqOm1OV7bji9YlK4Jiwn5wdMFjw5gqY1Z1kfCgqMDF06llmhf0R7%2F4uurS1eJbo7xTkp6utgov3kbycMAfJ3vj%2BR28%2By9QyYfJyI%2F6nOmGNBuYTki%2BoLMXibagoELZEX955BWzDcPyq%2FZ94k929MTqZfWVK1spKp13qS8MuXFK5jUDgmxd2WXtkfyTgMJapyLF5jp6cilqm2M0vrFgr4RdCznRCeu36Spy09AueVcLEOHKnL%2BfiYIiEAA9y7jo4GPktK3pFSaYeO5urvKXlzKVsJf2CJWmCdSAqJaAYlC4u6%2FMlmuDtmKL1Q0TavpapX2bvzMDcUL81jiq3iAaNh5gxPooCBVbGGURnljb%2BGvMsgr8UhxCLWR4wqDeqiCSXK3vfXQcx8XumcGzChlpanKm%2FemHcdWByizSHToIEo26t%2FLjvFPEbSyDCSrzdO7YTQbN92IC4zWPYSAGW6hRAKEAMplJNFi7Vbf1YVmLUUgA4r8YmA%2Fg8l8684myO0yiwYH3i1ZzNut%2F4yojlGz7EopRTEz0EVbx7uO3yy%2B6hERGLTDLuP%2FSBjqkASPYhFjy%2BIVz1BaJvOsKRlc1THs53PxHiPsPgm1%2BbgYCp7A6oYCyvKjfGqPUpR6aAohpLlvRuHg4LmCBM%2FuUCE9dIRt2uEgW1ysSXSiN3u7OkixXt8og5Wnt%2F07IDhz2GlyLNUwdur6zZrVrwAIBnxAI9vZjLgCsozdijJIBy1QyWT3qLFdgvLWP4Iw0tKTm29hVtSfaNYhKarPdf8GEJpBXyMYF&X-Amz-Signature=449dde93d79f7b2e6d19c0f7b9439c38088f5e4bbdc454e1aac157aa185c1860&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

extra 里面是空，

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/f74b930a-a051-44e7-9ea5-bce35e40b11d/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VIE4LO4U%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDWdwKCk2VGpXkyF7%2F5m0XH%2BnbFRBzpXrzMiU9c%2BjDk3gIhAJyyDgdq7NR2B9nqGcgBN57jviIXITfc8wofH3%2FeoPHHKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyRuOvFuMf23iQLyzgq3AM2OhhQqKaxCBu4gMUmeoAh7kkq2JRHGvWD0rWuUE1U9HPdWjAxYOKNrPS7NlMXyvMG4Qwi%2Bbq%2F97gpAQXqOm1OV7bji9YlK4Jiwn5wdMFjw5gqY1Z1kfCgqMDF06llmhf0R7%2F4uurS1eJbo7xTkp6utgov3kbycMAfJ3vj%2BR28%2By9QyYfJyI%2F6nOmGNBuYTki%2BoLMXibagoELZEX955BWzDcPyq%2FZ94k929MTqZfWVK1spKp13qS8MuXFK5jUDgmxd2WXtkfyTgMJapyLF5jp6cilqm2M0vrFgr4RdCznRCeu36Spy09AueVcLEOHKnL%2BfiYIiEAA9y7jo4GPktK3pFSaYeO5urvKXlzKVsJf2CJWmCdSAqJaAYlC4u6%2FMlmuDtmKL1Q0TavpapX2bvzMDcUL81jiq3iAaNh5gxPooCBVbGGURnljb%2BGvMsgr8UhxCLWR4wqDeqiCSXK3vfXQcx8XumcGzChlpanKm%2FemHcdWByizSHToIEo26t%2FLjvFPEbSyDCSrzdO7YTQbN92IC4zWPYSAGW6hRAKEAMplJNFi7Vbf1YVmLUUgA4r8YmA%2Fg8l8684myO0yiwYH3i1ZzNut%2F4yojlGz7EopRTEz0EVbx7uO3yy%2B6hERGLTDLuP%2FSBjqkASPYhFjy%2BIVz1BaJvOsKRlc1THs53PxHiPsPgm1%2BbgYCp7A6oYCyvKjfGqPUpR6aAohpLlvRuHg4LmCBM%2FuUCE9dIRt2uEgW1ysSXSiN3u7OkixXt8og5Wnt%2F07IDhz2GlyLNUwdur6zZrVrwAIBnxAI9vZjLgCsozdijJIBy1QyWT3qLFdgvLWP4Iw0tKTm29hVtSfaNYhKarPdf8GEJpBXyMYF&X-Amz-Signature=3b4a15162d059d4b40694f8794f984605beb4a2161c0f46d9950e0ee14e4e91d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

同学们也可以使用 optimizer 看一下现在的结果是怎样的，比方使用索引的开销等等。我们这一次再次执行一下这条 SQL 语句，看一下需要花费多久。执行 output 可以发现需要 62 毫秒。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/073fd774-0567-49e5-97b9-acd38eb52c25/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VIE4LO4U%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDWdwKCk2VGpXkyF7%2F5m0XH%2BnbFRBzpXrzMiU9c%2BjDk3gIhAJyyDgdq7NR2B9nqGcgBN57jviIXITfc8wofH3%2FeoPHHKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyRuOvFuMf23iQLyzgq3AM2OhhQqKaxCBu4gMUmeoAh7kkq2JRHGvWD0rWuUE1U9HPdWjAxYOKNrPS7NlMXyvMG4Qwi%2Bbq%2F97gpAQXqOm1OV7bji9YlK4Jiwn5wdMFjw5gqY1Z1kfCgqMDF06llmhf0R7%2F4uurS1eJbo7xTkp6utgov3kbycMAfJ3vj%2BR28%2By9QyYfJyI%2F6nOmGNBuYTki%2BoLMXibagoELZEX955BWzDcPyq%2FZ94k929MTqZfWVK1spKp13qS8MuXFK5jUDgmxd2WXtkfyTgMJapyLF5jp6cilqm2M0vrFgr4RdCznRCeu36Spy09AueVcLEOHKnL%2BfiYIiEAA9y7jo4GPktK3pFSaYeO5urvKXlzKVsJf2CJWmCdSAqJaAYlC4u6%2FMlmuDtmKL1Q0TavpapX2bvzMDcUL81jiq3iAaNh5gxPooCBVbGGURnljb%2BGvMsgr8UhxCLWR4wqDeqiCSXK3vfXQcx8XumcGzChlpanKm%2FemHcdWByizSHToIEo26t%2FLjvFPEbSyDCSrzdO7YTQbN92IC4zWPYSAGW6hRAKEAMplJNFi7Vbf1YVmLUUgA4r8YmA%2Fg8l8684myO0yiwYH3i1ZzNut%2F4yojlGz7EopRTEz0EVbx7uO3yy%2B6hERGLTDLuP%2FSBjqkASPYhFjy%2BIVz1BaJvOsKRlc1THs53PxHiPsPgm1%2BbgYCp7A6oYCyvKjfGqPUpR6aAohpLlvRuHg4LmCBM%2FuUCE9dIRt2uEgW1ysSXSiN3u7OkixXt8og5Wnt%2F07IDhz2GlyLNUwdur6zZrVrwAIBnxAI9vZjLgCsozdijJIBy1QyWT3qLFdgvLWP4Iw0tKTm29hVtSfaNYhKarPdf8GEJpBXyMYF&X-Amz-Signature=97289ea5937ca0a4ef375426cf19193c8262281c606fece32976e33c9d8d6a52&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

记录一下copy，创建组合索引粘贴，和刚刚的 68 毫秒差异并不大。按理来讲，组合索引的性能应该是要比多个单列索引去做索引合并的性能要好的。但是为什么两次耗时没有太大变化？


这是因为在我们的例子里面，除交集的开销并不大，也就是 88 行数据和 86 行数据除了一个交集而已。但是一旦求交集的行数多，求交集的开销也会比较的大。这个时候组合作用的优势就体现出来了。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/994f8cab-9e8b-4d27-b7b3-b03e2dc10b04/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VIE4LO4U%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDWdwKCk2VGpXkyF7%2F5m0XH%2BnbFRBzpXrzMiU9c%2BjDk3gIhAJyyDgdq7NR2B9nqGcgBN57jviIXITfc8wofH3%2FeoPHHKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyRuOvFuMf23iQLyzgq3AM2OhhQqKaxCBu4gMUmeoAh7kkq2JRHGvWD0rWuUE1U9HPdWjAxYOKNrPS7NlMXyvMG4Qwi%2Bbq%2F97gpAQXqOm1OV7bji9YlK4Jiwn5wdMFjw5gqY1Z1kfCgqMDF06llmhf0R7%2F4uurS1eJbo7xTkp6utgov3kbycMAfJ3vj%2BR28%2By9QyYfJyI%2F6nOmGNBuYTki%2BoLMXibagoELZEX955BWzDcPyq%2FZ94k929MTqZfWVK1spKp13qS8MuXFK5jUDgmxd2WXtkfyTgMJapyLF5jp6cilqm2M0vrFgr4RdCznRCeu36Spy09AueVcLEOHKnL%2BfiYIiEAA9y7jo4GPktK3pFSaYeO5urvKXlzKVsJf2CJWmCdSAqJaAYlC4u6%2FMlmuDtmKL1Q0TavpapX2bvzMDcUL81jiq3iAaNh5gxPooCBVbGGURnljb%2BGvMsgr8UhxCLWR4wqDeqiCSXK3vfXQcx8XumcGzChlpanKm%2FemHcdWByizSHToIEo26t%2FLjvFPEbSyDCSrzdO7YTQbN92IC4zWPYSAGW6hRAKEAMplJNFi7Vbf1YVmLUUgA4r8YmA%2Fg8l8684myO0yiwYH3i1ZzNut%2F4yojlGz7EopRTEz0EVbx7uO3yy%2B6hERGLTDLuP%2FSBjqkASPYhFjy%2BIVz1BaJvOsKRlc1THs53PxHiPsPgm1%2BbgYCp7A6oYCyvKjfGqPUpR6aAohpLlvRuHg4LmCBM%2FuUCE9dIRt2uEgW1ysSXSiN3u7OkixXt8og5Wnt%2F07IDhz2GlyLNUwdur6zZrVrwAIBnxAI9vZjLgCsozdijJIBy1QyWT3qLFdgvLWP4Iw0tKTm29hVtSfaNYhKarPdf8GEJpBXyMYF&X-Amz-Signature=7371cc9b54a1775704a2edf8b4d0193d231f1b1ed9fbd186801b29eb27e03539&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

好回答 PPT 简单总结一下这节课的内容。


这节课我们对比了单列索引和组合索引之间执行的差异。从中可以知道，


首先 当搜索在多个条件的时候， MySQL 会使用索引合并，扫描多个索引并去求交集。


第二，有一个索引调优的经验，那就是实际项目中如果出现索引合并，往往说明你创建的索引不够合理，建议使用组合索引去优化。

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/820aa29c-8378-424b-b934-3236fe223010/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VIE4LO4U%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T230216Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDWdwKCk2VGpXkyF7%2F5m0XH%2BnbFRBzpXrzMiU9c%2BjDk3gIhAJyyDgdq7NR2B9nqGcgBN57jviIXITfc8wofH3%2FeoPHHKogECMb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyRuOvFuMf23iQLyzgq3AM2OhhQqKaxCBu4gMUmeoAh7kkq2JRHGvWD0rWuUE1U9HPdWjAxYOKNrPS7NlMXyvMG4Qwi%2Bbq%2F97gpAQXqOm1OV7bji9YlK4Jiwn5wdMFjw5gqY1Z1kfCgqMDF06llmhf0R7%2F4uurS1eJbo7xTkp6utgov3kbycMAfJ3vj%2BR28%2By9QyYfJyI%2F6nOmGNBuYTki%2BoLMXibagoELZEX955BWzDcPyq%2FZ94k929MTqZfWVK1spKp13qS8MuXFK5jUDgmxd2WXtkfyTgMJapyLF5jp6cilqm2M0vrFgr4RdCznRCeu36Spy09AueVcLEOHKnL%2BfiYIiEAA9y7jo4GPktK3pFSaYeO5urvKXlzKVsJf2CJWmCdSAqJaAYlC4u6%2FMlmuDtmKL1Q0TavpapX2bvzMDcUL81jiq3iAaNh5gxPooCBVbGGURnljb%2BGvMsgr8UhxCLWR4wqDeqiCSXK3vfXQcx8XumcGzChlpanKm%2FemHcdWByizSHToIEo26t%2FLjvFPEbSyDCSrzdO7YTQbN92IC4zWPYSAGW6hRAKEAMplJNFi7Vbf1YVmLUUgA4r8YmA%2Fg8l8684myO0yiwYH3i1ZzNut%2F4yojlGz7EopRTEz0EVbx7uO3yy%2B6hERGLTDLuP%2FSBjqkASPYhFjy%2BIVz1BaJvOsKRlc1THs53PxHiPsPgm1%2BbgYCp7A6oYCyvKjfGqPUpR6aAohpLlvRuHg4LmCBM%2FuUCE9dIRt2uEgW1ysSXSiN3u7OkixXt8og5Wnt%2F07IDhz2GlyLNUwdur6zZrVrwAIBnxAI9vZjLgCsozdijJIBy1QyWT3qLFdgvLWP4Iw0tKTm29hVtSfaNYhKarPdf8GEJpBXyMYF&X-Amz-Signature=c38fcbe15c6674a7afe2209b82089ea795206a7d272f31c1a32ab91d36238217&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

**但是同学们也不要被我这句话给误导了。如果你的 SQL 目前没有性能问题，建议暂时不要去折腾。**

**调优的目的一般都是为了解决问题，如果目前没有性能问题，我们就没有必要去投入时间。**

**又比如咱们这节课的例子，**


**使用单列索引和组合索引的性能差异并不大，如果你的项目最初创建的是 2 个单列索引，而6， 68 毫秒这个时间能够满足你的需求，你依然可以继续使用，不做任何的优化。**

**
如果有一天你发现 SQL 的执行效率达不到你的要求，并且发现在 explain 里面出现了索引合并的话，这个时候再去考虑使用组合索引去调优。**


总之，同学们还是应该具体问题具体分析，这只是一个参考原则和经验之谈。


另外还要再次强调一下，**当使用组合索引的时候，一定要注意索引里面字段的顺序，一定要符合最左前缀原则，否则的话**，组合索引是用不上的。关于最左前缀原则，课上已经强调过多次了对吧？那么同学们一定要记得这节课就到这里，谢谢大家。



---
title: M1芯片的Mac安装Fooocus图片生成和换脸工具安装
---

# M1芯片的Mac安装Fooocus图片生成和换脸工具安装

```shell
Apple Mac 芯片（M1 或 M2）上安装 Fooocus。 
Fooocus 通过 PyTorch MPS（Mac 上的加速 PyTorch 训练） 设备加速在 Apple 硅计算机上运行。 
Mac Silicon 计算机不配备专用显卡，因此与配备专用显卡的计算机相比，图像处理时间显着延长


1：安装python之后自带pip包管理工具
2：安装pytorch ：pip3 install --pre torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/nightly/cpu
3：验证是否成功安装，使用简单的 Python 脚本验证 mps 支持
----------------------------------------------------------
import torch
if torch.backends.mps.is_available():
			mps_device = torch.device("mps")
			x = torch.ones(1, device=mps_device)
			print (x)
else:
     print ("MPS device not found.")
----------------------------------------------------------
3.1：终端打开（或者iterm2）
python3 pytoch.py
输出 tensor([1.], device='mps:0')说明成功了

4： git clone https://github.com/lllyasviel/Fooocus.git 下载项目。进入项目
5： 创建一个虚拟环境
使用conda也行，这里我使用 python3 -m venv venv
激活虚拟环境  source venv/bin/activate
6:  pip安装需要的依赖 pip install -r requirements_versions.txt
7:  运行 python entry_with_update.py 启动 Fooocus。 （某些 Mac M2 用户可能需要 python entry_with_update.py --disable-offload-from-vram 来加速模型加载/卸载。）第一次运行 Fooocus 时，它将自动下载 Stable Diffusion SDXL 模型，并且会花费大量时间，具体取决于您的互联网连接
7.1 （如果出现urllib错误，请关闭科学上网工具再次运行，如果还是出现此错误，请登录huggingface
命令  huggingface-cli --token xxxxxxxxxxxxx   (xx表示huggingface的token--没有去注册然后setting中生成获取)
）  如果重新运行需要再次登录 huggingface    


8：运行和创建公共链接

在本地 URL 上运行：http://127.0.0.1:7865
要创建公共链接，请在 `launch()` 中设置 `share=True`。



参考链接
https://github.com/lllyasviel/Fooocus?tab=readme-ov-file
https://developer.apple.com/metal/pytorch/
https://developer.aliyun.com/article/1212430（MPS）




要生生成的目标-正向提示词
a girl,blue hair,green eyes,beautiful, hight quality,ultra detail,masterpiece,8k


生成怎人的反向提示词：
nsfw, paintings, cartoon, anime, sketches, worst quality, low quality, normal quality,
lowres, watermark, monochrome, grayscale, ugly, blurry, Tan skin, dark skin, black skin,
skin spots, skin blemishes, age spot, glans, disabled, distorted, bad anatomy, morbid,
malformation, amputation, bad proportions, twins
missing body, fused body, extra head, poorly drawn face, bad eyes, deformed eye,
unclear eyes, cross-eyed, long neck, malformed limbs, extra limbs, extra arms,
missing arms, bad tongue, strange fingers, mutated hands, missing hands,
poorly drawn hands, extra hands, fused hands, connected hand, bad hands,
wrong fingers, missing fingers, extra fingers, 4 fingers, 3 fingers,
deformed hands, extra legs, bad legs, many legs,
more than two legs, bad feet, wrong feet, extra feets


```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/5383921c-c5c9-4861-b9b1-b5016544d5ee/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VFYJYHOD%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIER%2F48ZbBkVm1FgGEUcqCF7jThxIMThTEBjyUvYATmyVAiEA6jdFISQNerJo%2BL0Vk4SOE29i1WqC87b%2Bz0ieXpv5WJcqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEDmGtVtG62QIQVXNCrcAy4YcZeD8GkdoXZJWjm0LC%2Bu9fLqAEyg60ec%2FmDCyKBOJQOaQW8e5byR2vI9m%2BaAzqHiACUd1DBvinLb9RxEeV%2BOXhbg3EyhM%2BxKm3o4qw7EgAtVZlJBSZjTkKpgW9zqHc4BrfUSoQ2AxjXPywj%2FjwLBIPFw11TUFLEQ%2FQkO0MhHICCj5EmGpRT1m9eQPXtduVsM4DoBhbAi42xpNbjCarx4ompAun%2FVqihmhhBJ2McHDYj3kzkRCaoH7pk7VX0cWNmfj%2FQ0mNA6yTPkp0tClPhjtBjlcto0iLl4W%2F2TDfzTzWmq9w2HKW5l%2B5XX2L6xUJxRGb167e%2BTYDYwSZwzz1KATXU3eRRKa9WrjG%2BpbfVZHtyGgH4M5wDrdKUlM7dLgePpe3z8QLDIopkOma3s3PtrA%2B6zrUmCmogrBRbQDLY3S5jEe7fYzZzCGk8Y2VlgSSjlDOB8otWU%2BidaQwahfrr4KW0WNLaE%2FzibvmpXD1qfOBPx%2F2CMrKVIOxgDKP4t7GoT8LwS5mj7er4Huwb%2BQVm5yarNL4bybBxY86%2FtM45KApoPjBMRsTDIO8BKf1HPkGX0BmAU1uD1Fe1qXyw6H78kGZomcmL7xV7ZoUMec%2FkibEnu9QOckZ05FhjxMIu6%2F9IGOqUBjcYwJNCoDJ%2Bd1d%2FHBWmcm5E8xtmgfr%2Bjmb%2B%2BZR7KmZkDKzFKHPuRyQ1OWbLFZj6WbjXsY3tbzz8cIxm2I6hz9Zu6%2BcjwUGpjd0eolhbsSmUdbFiL1wA%2FDwZ9SSvDvBOHzMukMMGA5oc07oWg6UY4maK7fpc%2FZsneAiSsuD%2B21IPjc8rHrzKoIL1F%2FpzSmTl1DCsT7Kx%2FMYC6y28Ebg%2BT71Md%2BG2L&X-Amz-Signature=7e476f111a78e2391b6047826c885c5785fa394134019ae2f08da616ced60a58&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/635faa91-7c08-4afc-b202-68e596dbd2aa/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VFYJYHOD%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIER%2F48ZbBkVm1FgGEUcqCF7jThxIMThTEBjyUvYATmyVAiEA6jdFISQNerJo%2BL0Vk4SOE29i1WqC87b%2Bz0ieXpv5WJcqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEDmGtVtG62QIQVXNCrcAy4YcZeD8GkdoXZJWjm0LC%2Bu9fLqAEyg60ec%2FmDCyKBOJQOaQW8e5byR2vI9m%2BaAzqHiACUd1DBvinLb9RxEeV%2BOXhbg3EyhM%2BxKm3o4qw7EgAtVZlJBSZjTkKpgW9zqHc4BrfUSoQ2AxjXPywj%2FjwLBIPFw11TUFLEQ%2FQkO0MhHICCj5EmGpRT1m9eQPXtduVsM4DoBhbAi42xpNbjCarx4ompAun%2FVqihmhhBJ2McHDYj3kzkRCaoH7pk7VX0cWNmfj%2FQ0mNA6yTPkp0tClPhjtBjlcto0iLl4W%2F2TDfzTzWmq9w2HKW5l%2B5XX2L6xUJxRGb167e%2BTYDYwSZwzz1KATXU3eRRKa9WrjG%2BpbfVZHtyGgH4M5wDrdKUlM7dLgePpe3z8QLDIopkOma3s3PtrA%2B6zrUmCmogrBRbQDLY3S5jEe7fYzZzCGk8Y2VlgSSjlDOB8otWU%2BidaQwahfrr4KW0WNLaE%2FzibvmpXD1qfOBPx%2F2CMrKVIOxgDKP4t7GoT8LwS5mj7er4Huwb%2BQVm5yarNL4bybBxY86%2FtM45KApoPjBMRsTDIO8BKf1HPkGX0BmAU1uD1Fe1qXyw6H78kGZomcmL7xV7ZoUMec%2FkibEnu9QOckZ05FhjxMIu6%2F9IGOqUBjcYwJNCoDJ%2Bd1d%2FHBWmcm5E8xtmgfr%2Bjmb%2B%2BZR7KmZkDKzFKHPuRyQ1OWbLFZj6WbjXsY3tbzz8cIxm2I6hz9Zu6%2BcjwUGpjd0eolhbsSmUdbFiL1wA%2FDwZ9SSvDvBOHzMukMMGA5oc07oWg6UY4maK7fpc%2FZsneAiSsuD%2B21IPjc8rHrzKoIL1F%2FpzSmTl1DCsT7Kx%2FMYC6y28Ebg%2BT71Md%2BG2L&X-Amz-Signature=455b4abf24c03a72521e4cbc13db72f0ac54e4d59a919e079ef988d76470b607&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/e96b9888-92d2-45cd-9f8c-57972128f633/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VFYJYHOD%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIER%2F48ZbBkVm1FgGEUcqCF7jThxIMThTEBjyUvYATmyVAiEA6jdFISQNerJo%2BL0Vk4SOE29i1WqC87b%2Bz0ieXpv5WJcqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEDmGtVtG62QIQVXNCrcAy4YcZeD8GkdoXZJWjm0LC%2Bu9fLqAEyg60ec%2FmDCyKBOJQOaQW8e5byR2vI9m%2BaAzqHiACUd1DBvinLb9RxEeV%2BOXhbg3EyhM%2BxKm3o4qw7EgAtVZlJBSZjTkKpgW9zqHc4BrfUSoQ2AxjXPywj%2FjwLBIPFw11TUFLEQ%2FQkO0MhHICCj5EmGpRT1m9eQPXtduVsM4DoBhbAi42xpNbjCarx4ompAun%2FVqihmhhBJ2McHDYj3kzkRCaoH7pk7VX0cWNmfj%2FQ0mNA6yTPkp0tClPhjtBjlcto0iLl4W%2F2TDfzTzWmq9w2HKW5l%2B5XX2L6xUJxRGb167e%2BTYDYwSZwzz1KATXU3eRRKa9WrjG%2BpbfVZHtyGgH4M5wDrdKUlM7dLgePpe3z8QLDIopkOma3s3PtrA%2B6zrUmCmogrBRbQDLY3S5jEe7fYzZzCGk8Y2VlgSSjlDOB8otWU%2BidaQwahfrr4KW0WNLaE%2FzibvmpXD1qfOBPx%2F2CMrKVIOxgDKP4t7GoT8LwS5mj7er4Huwb%2BQVm5yarNL4bybBxY86%2FtM45KApoPjBMRsTDIO8BKf1HPkGX0BmAU1uD1Fe1qXyw6H78kGZomcmL7xV7ZoUMec%2FkibEnu9QOckZ05FhjxMIu6%2F9IGOqUBjcYwJNCoDJ%2Bd1d%2FHBWmcm5E8xtmgfr%2Bjmb%2B%2BZR7KmZkDKzFKHPuRyQ1OWbLFZj6WbjXsY3tbzz8cIxm2I6hz9Zu6%2BcjwUGpjd0eolhbsSmUdbFiL1wA%2FDwZ9SSvDvBOHzMukMMGA5oc07oWg6UY4maK7fpc%2FZsneAiSsuD%2B21IPjc8rHrzKoIL1F%2FpzSmTl1DCsT7Kx%2FMYC6y28Ebg%2BT71Md%2BG2L&X-Amz-Signature=86d49347dde210de5b185564f51a28547b6ab7800bea423913bcd54ffc9efe78&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/f7573ba2-f510-4095-8c06-a47f4ec65665/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466VFYJYHOD%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234341Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIER%2F48ZbBkVm1FgGEUcqCF7jThxIMThTEBjyUvYATmyVAiEA6jdFISQNerJo%2BL0Vk4SOE29i1WqC87b%2Bz0ieXpv5WJcqiAQIxv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDEDmGtVtG62QIQVXNCrcAy4YcZeD8GkdoXZJWjm0LC%2Bu9fLqAEyg60ec%2FmDCyKBOJQOaQW8e5byR2vI9m%2BaAzqHiACUd1DBvinLb9RxEeV%2BOXhbg3EyhM%2BxKm3o4qw7EgAtVZlJBSZjTkKpgW9zqHc4BrfUSoQ2AxjXPywj%2FjwLBIPFw11TUFLEQ%2FQkO0MhHICCj5EmGpRT1m9eQPXtduVsM4DoBhbAi42xpNbjCarx4ompAun%2FVqihmhhBJ2McHDYj3kzkRCaoH7pk7VX0cWNmfj%2FQ0mNA6yTPkp0tClPhjtBjlcto0iLl4W%2F2TDfzTzWmq9w2HKW5l%2B5XX2L6xUJxRGb167e%2BTYDYwSZwzz1KATXU3eRRKa9WrjG%2BpbfVZHtyGgH4M5wDrdKUlM7dLgePpe3z8QLDIopkOma3s3PtrA%2B6zrUmCmogrBRbQDLY3S5jEe7fYzZzCGk8Y2VlgSSjlDOB8otWU%2BidaQwahfrr4KW0WNLaE%2FzibvmpXD1qfOBPx%2F2CMrKVIOxgDKP4t7GoT8LwS5mj7er4Huwb%2BQVm5yarNL4bybBxY86%2FtM45KApoPjBMRsTDIO8BKf1HPkGX0BmAU1uD1Fe1qXyw6H78kGZomcmL7xV7ZoUMec%2FkibEnu9QOckZ05FhjxMIu6%2F9IGOqUBjcYwJNCoDJ%2Bd1d%2FHBWmcm5E8xtmgfr%2Bjmb%2B%2BZR7KmZkDKzFKHPuRyQ1OWbLFZj6WbjXsY3tbzz8cIxm2I6hz9Zu6%2BcjwUGpjd0eolhbsSmUdbFiL1wA%2FDwZ9SSvDvBOHzMukMMGA5oc07oWg6UY4maK7fpc%2FZsneAiSsuD%2B21IPjc8rHrzKoIL1F%2FpzSmTl1DCsT7Kx%2FMYC6y28Ebg%2BT71Md%2BG2L&X-Amz-Signature=29d394edc82f54b7e5bb8ec34d0806d0e6092e2c4a6055368c0d63266412e689&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


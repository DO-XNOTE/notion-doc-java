---
title: mac安装sd-目标是视屏换脸
---

# mac安装sd-目标是视屏换脸

0.安装必备

```shell
0.1:mov2mov
0.2:roop
0.3:ControlNet
0.4:ADetailter
参考 https://www.youtube.com/watch?v=StkW_R3ezSY
```

1.基础环境

```shell
1.1: 安装 ffmpeg 6.0以上  安装python3.10.6 
1.2：下载运用  git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui.git
```

2.运行环境

```shell
查看：webui-mac-env.sh中需要的
把  torch==2.2.0
参考： https://pytorch.org/get-started/previous-versions/
```

3.安装插件 roop 可能显示不出来

```shell
地址： https://github.com/s0md3v/sd-webui-roop

导致 roop 安装不成功显示不出来需要安装以下版本的包

Checking roop requirements
1:pip install insightface==0.7.3
Installing sd-webui-roop requirement: insightface==0.7.3
2:pip nstall onnx==1.14.0
Installing sd-webui-roop requirement: onnx==1.14.0
3:pip install onnxruntime==1.15.0
Installing sd-webui-roop requirement: onnxruntime==1.15.0
4:pip install opencv-python==4.7.0.72
Installing sd-webui-roop requirement: opencv-python==4.7.0.72
5:Install ifnude
如果下载不下来 detector.onnx
这里下载 https://huggingface.co/s0md3v/nudity-checker/resolve/main/detector.onnx 
并将其放入 .ifnude/
6：install install inswapper_128.onnx
下载下来放入到 stable-diffusion-webui/models/roop中

参考： https://github.com/s0md3v/sd-webui-roop/issues/222

```

4.要安装的插件

```shell
	https://github.com/ZHKKKe/MODNet.git
	https://github.com/DominikDoom/a1111-sd-webui-tagcomplete.git
	https://github.com/Bing-su/adetailer.git
	https://github.com/cloneofsimo/lora.git
	https://github.com/kohya-ss/sd-webui-additional-networks.git
	https://github.com/Mikubill/sd-webui-controlnet.git
	https://github.com/Scholar01/sd-webui-mov2mov.git
	https://github.com/VinsonLaro/stable-diffusion-webui-chinese.git
	https://github.com/toriato/stable-diffusion-webui-wd14-tagger.git
	https://github.com/AlUlkesh/stable-diffusion-webui-images-browser.git
	https://github.com/s0md3v/sd-webui-roop.git
```

[image](https://prod-files-secure.s3.us-west-2.amazonaws.com/28cd6f37-bc4c-49e6-8d26-8dc351a825af/622ca584-ab4a-4a29-9977-de4fce992b56/Untitled.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666U7A6WTZ%2F20260721%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260721T234342Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEP3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFapYQQ5IW7yQoiGCoI9EjSngn8N60rFmhxbTS3o0wo1AiAilw8P2FiUvWghWBYodM8tlGo3uJv3ylyAt2m5XwBhyiqIBAjG%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMHhVD7ZtFwGr6ynCDKtwDmMhUaM3TIJF8%2B8RKra6LPQTyUn2g2yY%2B7hy0mDHlm2M0FGL4Ps7i70Gy3GIEqz605bZs0OR6qflEO%2Fjb1AX0MlzQqlqBZAQ0nO9ixQC3kwbdUIqN34DfBqQg245M%2B9EUOgP47aAUs7bwjkaeyKvCNC3J8ZDub%2BHKzfiBdnB7LfMujlYmP9eySnYk6lxSh8r1HDrHg8hT7oeZKWiYyX1ifGvmKDLdT%2Bwnn8cEJl9NFv%2Bvnh0sWoy4vH%2FVT%2BtvW3l%2Bb1HnQQq4MWFW84qwHMGDWzYBZM5HEH3dwXl6My9tsKxw3SkvAa5LLTCWkbsOErQ4fdEUwfHHGgh85AF8L2zT4HxOgKsuwfB%2FWFW4vL%2B5GPOhA76LBNYhUU9XaefKd4khFLQaWGrcXpFpiNnsCEzaJUcGHq6%2FWcgtz1k2AltZEGhMREPPAWKlTXBfGw0z%2BfabW5z8GHspVHfZ9rhhb9cADRlfA3cJLx8a1y8v49E7987vd48qyrZJbobiHTrrVWUTZxU7IZGqekykjCELAnTHJ2SR0XhWL21boK7b4BEMAXixkRk3qHiskfk6sDNRNagOdP79ha9w7OF4GEBMDWyUlEDs8cmlhPgNC5ApKTmDk9FJTEvucl0CMF93wA4wlrj%2F0gY6pgHbMI1DmixtYiGnBNCzXJ%2FP4%2BaGm3Z1Ph5yO9qp6mVZO8tS64ACu3KUQUJN6UNmQz6NKNpoQOxH0JoDGi%2B2KbkWPAxp0Z%2BKsk04D8CZzWU3Wbnj%2B5woZnBO%2FDOG9Kw%2FXHEapqwEfLfkg0wovLKNH41MJ%2FOUaRsd3HNEu96AvCTKk87IYS2xV0ur62uMWss%2FmmlW8XuZ9PiM8d%2BA%2BBrs%2FzRoz1D86pBC&X-Amz-Signature=91e3830572eb551a91dee3a8d492749350017580ecbffb79ed7041c8e2d28001&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)


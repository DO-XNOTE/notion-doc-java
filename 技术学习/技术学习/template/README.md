---
title: template
---

# template

```shell
huggingface model 转 coreml模型

python -m python_coreml_stable_diffusion.torch2coreml --convert-unet --convert-text-encoder --convert-vae-decoder --convert-safety-checker --model-version runwayml/stable-diffusion-v1-5 --convert-controlnet lllyasviel/sd-controlnet-mlsd lllyasviel/sd-controlnet-depth lllyasviel/sd-controlnet-canny --unet-support-controlnet -o coreml-v1.5

python -m python_coreml_stable_diffusion.torch2coreml --convert-unet  --model-version runwayml/stable-diffusion-v1-5  -o coreml-v1.5

需要的依赖指定版本

pip uninstall scikit-learn==1.1.2

pip3 install torch==2.1.0

transformers-4.30.0

验证生成图片

python -m python_coreml_stable_diffusion.pipeline --prompt "magic book on the table" -i coreml-v1.5  -o coreml-v1.5 compute-unit ALL --seed 93

python -m python_coreml_stable_diffusion.pipeline --prompt "a photo of an astronaut riding a horse on mars" -i coreml-v1.5 -o images   --model-version runwayml/stable-diffusion-v1-5 --compute-unit ALL --seed 93
```



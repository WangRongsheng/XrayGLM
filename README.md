# XrayGLM

 <p align="center">
      <a href='https://github.com/WangRongsheng/XrayGLM'>
            <img src='https://img.shields.io/badge/Project-Page-Green'>
      </a>
      <a href='https://github.com/WangRongsheng/XrayGLM'>
            <img src='https://img.shields.io/badge/Paper-Arxiv-red'>
      </a>
      <a href='https://github.com/WangRongsheng/XrayGLM'>
            <img src='https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue'>
      </a>
      <a href="https://github.com/WangRongsheng/XrayGLM">
        <img alt="GitHub Contributors" src="https://colab.research.google.com/assets/colab-badge.svg" />
      </a>
      <a href="https://github.com/WangRongsheng/XrayGLM/blob/main/LICENSE">
        <img alt="GitHub Contributors" src="https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-lightgrey.svg" />
      </a>
      </br>
      <a href="https://github.com/WangRongsheng/XrayGLM/graphs/contributors">
        <img alt="GitHub Contributors" src="https://img.shields.io/github/contributors/WangRongsheng/XrayGLM" />
      </a>
      <a href="https://github.com/WangRongsheng/XrayGLM/issues">
        <img alt="Issues" src="https://img.shields.io/github/issues/WangRongsheng/XrayGLM?color=0088ff" />
      </a>
      <a href="https://github.com/WangRongsheng/XrayGLM/pulls">
        <img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/WangRongsheng/XrayGLM?color=0088ff" />
      </a>
      <a href=href="https://github.com/kaixindelele/XrayGLM/stargazers">
        <img src="https://img.shields.io/github/stars/WangRongsheng/XrayGLM?color=ccf">
      </a>
  </p>
  
# 本文贡献

![](./assets/images/xrayglm.png)
  
# 数据集

- [MIMIC-CXR](https://physionet.org/content/mimic-cxr-jpg/2.0.0/)是一个公开可用的胸部X光片数据集，包括377,110张图像和227,827个相关报告。
- [OpenI](https://openi.nlm.nih.gov/faq#collection)是一个来自印第安纳大学医院的胸部X光片数据集，包括6,459张图像和3,955个报告。

在上述工作中，报告信息都为非结构化的，不利于科学研究。为了生成合理的医学报告，我们对两个数据集进行了预处理，并最终得到了可以用于训练的**英文报告**。除此之外，为了更好的支持中文社区发展，借助ChatGPT的能力，我们将英文报告进行了中文翻译，并最终形成了可用于训练的数据集。

|数据集|数量|下载链接|
|:-|:-|:-|
|MIMIC-CXR-zh|-|-|
|OpenI-zh|6,423|[诊疗报告](./data/Xray/openi-zh.json) 、[X光影像](https://pan.baidu.com/s/13GBsDMKf6xBZBSHpoWH_EA?pwd=k9sh)|

# 项目致谢

1. [VisualGLM-6B](https://github.com/THUDM/VisualGLM-6B)为我们提供了基础的代码参考和实现；
2. [MiniGPT-4](https://github.com/Vision-CAIR/MiniGPT-4)为我们这个项目提供了研发思路；
3. ChatGPT生成了高质量的中文版X光检查报告以支持XrayGLM训练；
4. [gpt_academic](https://github.com/binary-husky/gpt_academic)为文档翻译提供了多线程加速；
5. [MedCLIP](https://github.com/RyanWangZf/MedCLIP) 、[BLIP2](https://huggingface.co/docs/transformers/main/model_doc/blip-2) 、[XrayGPT](https://github.com/mbzuai-oryx/XrayGPT) 等工作也重大的参考意义；

![](./assets/images/mpu.png)

这项工作由[澳门理工大学应用科学学院](https://www.mpu.edu.mo/esca/zh/index.php)硕士生[王荣胜](https://github.com/WangRongsheng) 、[段耀菲](https://github.com/IsBaSO4) 、[李俊蓉](https://github.com/lijunrong0815)完成，同时这项工作受到[檀韬](https://scholar.google.com/citations?hl=zh-CN&user=lLg3WRkAAAAJ)副教授、[彭祥佑](http://www.patrickpang.net/)老师的帮助支持。

*特别鸣谢：[USTC-PhD Yongle Luo](https://github.com/kaixindelele) 提供了有3000美金的OpenAI账号，帮助我们完成大量的X光报告翻译工作

# 免责声明

本项目相关资源仅供学术研究之用，严禁用于商业用途。使用涉及第三方代码的部分时，请严格遵循相应的开源协议。模型生成的内容受模型计算、随机性和量化精度损失等因素影响，本项目无法对其准确性作出保证。即使本项目模型输出符合医学事实，也不能被用作实际医学诊断的依据。对于模型输出的任何内容，本项目不承担任何法律责任，亦不对因使用相关资源和输出结果而可能产生的任何损失承担责任。

# 项目引用

如果你使用了本项目的模型，数据或者代码，请声明引用：

```bash
@misc{wang2023XrayGLM,
      title={XrayGLM: The first Chinese Medical Multimodal Model that Chest Radiographs Summarization}, 
      author={Rongsheng Wang, Yaofei Duan, Junrong Li, Patrick Pang and Tao Tan},
      year={2023},
      publisher = {GitHub},
      journal = {GitHub repository},
      howpublished = {\url{https://github.com/WangRongsheng/XrayGLM}},
}
```

# 使用许可

此存储库遵循[CC BY-NC-SA](https://creativecommons.org/licenses/by-nc-sa/4.0/) ，请参阅许可条款。


## My attempt at [comma.ai speed challenge](https://github.com/commaai/speedchallenge)
This repository is made for my personal purpose of attempting the [comma.ai speed challenge](https://github.com/commaai/speedchallenge). I am hoping to update this repository regularly in a form of a log.

## Links to notebook
- [Preprocess + Train Notebook](https://colab.research.google.com/drive/16wj_3dMqNw1uozfQm41J7DylUjE-jezN?usp=sharing)

## Resources
- [Nvidia: End to End Learning for Self-Driving cars](https://arxiv.org/pdf/1604.07316v1.pdf)
- [CVF: Dense Optical Flow Prediction From a static Image](https://www.cv-foundation.org/openaccess/content_iccv_2015/html/Walker_Dense_Optical_Flow_ICCV_2015_paper.html)
- [OpenCV Docs: Optical Flow](https://docs.opencv.org/3.4/d4/dee/tutorial_optical_flow.html)

## Logs
- [The beginning](#2021/01/10---Initial-commit)

#### 2021/01/10 - Initial commit
Created an initial Google Colab notebook for this project and preprocessed the videos into individual frames.

#### 2021/01/12 - Creating extra training images
Flipped the training images to double the amount of training data; still not sure if I am going to use all of them. Found a paper by Nvidia describing convolution neural network for self-driving cars. I am gonna read more about optical flow, which is used to find the movement pattern based on contiguous frame. 
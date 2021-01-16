## My attempt at [comma.ai speed challenge](https://github.com/commaai/speedchallenge)
This repository is made for my personal purpose of attempting the [comma.ai speed challenge](https://github.com/commaai/speedchallenge). I am hoping to update this repository regularly in a form of a log.

## Links to notebook
- [Preprocess Notebook](https://colab.research.google.com/drive/16wj_3dMqNw1uozfQm41J7DylUjE-jezN?usp=sharing)
- [Model and Training Notebook](https://colab.research.google.com/drive/1uzaoiTZWCm2XaAtQCR4R0mIcGXrZ8oQE?usp=sharing)

## Resources
- [Nvidia: End to End Learning for Self-Driving cars](https://arxiv.org/pdf/1604.07316v1.pdf)
- [CVF: Dense Optical Flow Prediction From a static Image](https://www.cv-foundation.org/openaccess/content_iccv_2015/html/Walker_Dense_Optical_Flow_ICCV_2015_paper.html)
- [OpenCV Docs: Optical Flow](https://docs.opencv.org/3.4/d4/dee/tutorial_optical_flow.html)
- [millingab: deeps - Inspiration Repo](https://github.com/millingab/deeps)
- [Shervine Amidi: Generate Data in Parallel with PyTorch](https://stanford.edu/~shervine/blog/pytorch-how-to-generate-data-parallel)

## Logs
- [The beginning](#2021/01/10---Initial-commit)
- [Last stretch of first attempt](#2021/01/16---Created-Nvidia-model-on-PyTorch)

#### 2021/01/10 - Initial commit
Created an initial Google Colab notebook for this project and preprocessed the videos into individual frames.

#### 2021/01/12 - Created extra training images
Flipped the training images to double the amount of training data; still not sure if I am going to use all of them. Found a paper by Nvidia describing convolution neural network for self-driving cars. I am going to read more about optical flow, which is used to find the movement pattern based on contiguous frame.

#### 2021/01/13 - Experimented with optical flow
Found a GitHub repo that tried to solve the comma.ai problem. Based on that repo, I think I am going in the right direction. I might try implementing the same approach with my own twist as the end result. Tried to implement Lucas-Kanade and Farneback optical flow with opencv. Turned out that the latter produced more features in the image. Also implemented function to crop the dashboard to reduce the size of the image. The next step is to figure out how to feed the image and speed to the model. The GitHub repo I mentioned use generator so the model do not take up much memory when processing the images; might do the same thing, but will try to find other thing that fit. After that would be implementing some models to try. It looks like comma.ai use PyTorch, so I guess will be using it for this project.

#### 2021/01/16 - Created Nvidia model on PyTorch
Finally got the time to create the model in PyTorch. Top priority would be putting it all together to feed the model. The preprocess part is not particularly clean, need to put that into mental list of technical debt. Might end up using data loader, since I found a helpful page to take care of that from Stanford.
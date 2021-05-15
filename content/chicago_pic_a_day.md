Title: Pic-a-day Registration
Date: 2017-11-27
Category: Computer Vision
Tags: computer vision, registration
Slug: chicago_pic_a_day
Author: Brian Keating
Summary: Registration of pic-a-day time series of downtown Chicago using OpenCV.

My wife, Lynn, <s>works</s> worked on the 34th floor in the Chicago loop and has a great view from her office. When she started at her job, she starting taking pictures once a day from her window. She was remarkably consistent about remembering to take the pictures at about the same time of day every weekday. [The end result](https://drive.google.com/open?id=1YcygCgwlZiqAN92JWHnMMVColle5b5Wz) is a series of about 340 images covering a year and a half. While she was taking the pictures, a 40 story building was erected across the street, which kind of wrecked her view. I stitched the images together with ffmpeg 

```
ffmpeg -framerate 7 -f image2 -i in_frames/%*.jpg -c:v h264 -crf 1 original.mov
``` 

to produce this video:

#
<iframe width="560" height="315" src="https://www.youtube.com/embed/YJgCCjt5hog?rel=0" frameborder="0" gesture="media" allowfullscreen></iframe>
#

Pretty awesome, but I wanted to register/align the images so that it looks like the camera (my wife's phone) was on a stationary tripod the whole year. This amounts to estimating projection transformations that connect the images to each other.

I initially [tried matching keypoints](https://docs.opencv.org/3.0-beta/doc/py_tutorials/py_feature2d/py_feature_homography/py_feature_homography.html#py-feature-homography), which I think is a pretty standard approach. I spent a while tweaking parameters and got it working perfectly... about 2/3 of the time. The fact that this didn't work perfectly is a little surprising to me, since the images contain lots of prominent corners that seem ripe for matching.

What finally did get it working was opencv's [findTransformECC](https://docs.opencv.org/3.0-beta/modules/video/doc/motion_analysis_and_object_tracking.html#findtransformecc) function. This function is much simpler than the keypoints-descriptor-RANSAC approach -- it directly searches for tranform parameters that maximize the correlation between two images. My wife's photos were taken in widely varying lighting conditions, so in order to make them comparable, I preprocess them by median filtering and computing the gradient magnitude. I found that taking the square root of the gradient magnitude helped `findTransformECC` converge faster and more robustly.

Even after all this, there were still some images where the registration failed for no apparent reason. There are a number of ways to make the algorithm more robust -- use a multiscale approach, or combine ECC-based registration with keypoint-based registration. I took the easy way out and just deleted the offending photos :). There were about a dozen "problem images" that were removed from the dataset.

The end result of the registrations:

#
<iframe width="560" height="315" src="https://www.youtube.com/embed/O9Pr8s3eLWg?rel=0" frameborder="0" gesture="media" allowfullscreen></iframe>
#

One complication with registering these images is the presence of the new building that goes up halfway through the series. If you try to match the last image to the first one with `findTransformECC` it won't work because the new building takes up so much of the frame. Thus, selecting one reference image and matching everything to it won't work in this case.

What I did instead was to treat each image as the node of a directed graph. A perspective transform registering 2 images can be associated with a graph edge, and the inverse transform is associated with an edge pointing in the opposite direction.  This is a pretty flexible framework for multi-image registration, since rather than matching each image to a single reference image, we can match each image to *any other* image in the set. We register images until the graph contains a single connected component. At that point, we can connect any two image nodes in the graph with a path, and that path corresponds to a chain of transformations. Thus, any image can be selected as the reference image, and all other images warped to it. One could also enforce that circular chains of transforms be consistent (I believe is related to "closing the loop" in [SLAM](http://robots.stanford.edu/papers/thrun.graphslam.pdf)), although I did not pursue this (yet).

The notebook used to produce these results can be viewed [here]({static}/notebooks/RegisterImages.html) or downloaded [here]({static}/notebooks/RegisterImages.ipynb).

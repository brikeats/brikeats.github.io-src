Title: Eclipse
Date: 2017-09-23 12:50
Modified: 2017-09-23 12:50
Category: Demos
Tags: demo, video
Slug: eclipse
Author: Brian Keating
Summary: Eclipse

![eclipse totality]({filename}/images/totality.jpg)

My wife and I were fortunate enough to be able to see the eclipse in August just outside of Salem, Oregon. Our friend, Heidi, drove us down from Seattle where we were vacationing. I was concerned about the weather -- it's a bit of a drive and coastal Oregon isn't known for being sunny -- but it turned out to be a beautiful cloudless day and totality was just spectacular. I didn't get any pics of totality, but Heidi had brought her non-phone camera and got some good pics of totality (including the one above) and a video of the "diamond ring". She didn't have a tripod, so the sun wanders about in the frame:

[![Alt text](https://img.youtube.com/vi/q3EKl2VAPe0/0.jpg)](https://www.youtube.com/watch?v=q3EKl2VAPe0)

Looks pretty good, but I wanted to correct for this motion. This is a fairly easy problem, since the sun is infinitely far away and it doesn't change shape (so we only need to find 2 translations to register the frames), and the background is featureless black sky. I initially tried creating an eclipse-looking template, and using that to search each frame for the sun's position. This mostly worked well, but it was not robust -- it failed badly for some frames. I believe that some of the lens flares and other artifacts hurt the performance.

Finally, I just used [skimage's register_translation](http://scikit-image.org/docs/dev/auto_examples/transform/plot_register_translation.html) function to register consecutive frames. With the correct translations in hand, I zero pad the images such that the sun is in the center of every frame, write the images to file, and make them into a movie with ffmpeg. I also grabbed this image of the diamond ring:

![eclipse diamond ring]({filename}/images/diamond_ring.jpg)

The final result:

[![Alt text](https://img.youtube.com/vi/uao88kE0ukA/0.jpg)](https://www.youtube.com/watch?v=uao88kE0ukA)

The notebook used to produce these videos can be viewed [here]({filename}/notebooks/eclipse.html) or downloaded [here]({filename}/notebooks/eclipse.ipynb).
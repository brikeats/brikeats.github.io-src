Title: Eclipse
Date: 2017-09-23 12:50
Modified: 2017-09-23 12:50
Category: Demos
Tags: demo, video
Slug: eclipse
Author: Brian Keating
Summary: Correcting motion in a video sequence of the 2017 eclipse.

![eclipse totality]({filename}/images/totality.jpg)

My wife and I were fortunate enough to be able to see the eclipse in August just outside of Salem, Oregon. Our friend, Heidi, drove us down from Seattle where we were vacationing. I was concerned about the weather -- it's a bit of a drive and coastal Oregon isn't known for being sunny -- but it turned out to be a beautiful cloudless day and totality was just spectacular. I didn't get any pics of totality, but Heidi had brought her non-phone camera and got some good pics of totality (including the one above) and a video of the "diamond ring". She didn't have a tripod, so the sun wanders about in the frame:

#
<iframe width="560" height="315" src="https://www.youtube.com/embed/q3EKl2VAPe0" frameborder="0" allowfullscreen></iframe>
#


Looks pretty awesome, but I wanted to correct for this motion. This is a fairly easy problem, since the sun is infinitely far away and it doesn't change shape (so we only need to find 2 translations to register the frames), and the background is featureless black sky. I initially tried creating an eclipse-looking template, and used that to search each frame for the sun's position. This mostly worked well, but it was not robust -- it failed badly for some frames. I believe that some of the lens flares and other artifacts hurt the performance.

Finally, I just used [skimage's register_translation](http://scikit-image.org/docs/dev/auto_examples/transform/plot_register_translation.html) function to register consecutive frames. With the correct translations in hand, I zero pad the images such that the sun is in the center of every frame, write the images to file, and make them into a movie with ffmpeg. I also grabbed this image of the diamond ring:

![eclipse diamond ring]({filename}/images/diamond_ring.jpg)

The final result:

#
<iframe width="560" height="315" src="https://www.youtube.com/embed/uao88kE0ukA" frameborder="0" allowfullscreen></iframe>
#

The notebook used to produce these videos can be viewed [here]({filename}/notebooks/eclipse.html) or downloaded [here]({filename}/notebooks/eclipse.ipynb).
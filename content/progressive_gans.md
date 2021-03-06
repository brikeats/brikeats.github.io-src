Title: Progressive GANs
Date: 2017-12-23
Tags: computer vision, deep learning, generative
Slug: progressive_gans
Author: Brian Keating
Summary: Confabulating creepy celebrity headshots with Nvidia's progressive GANs.

Generative models, [GANs](https://en.wikipedia.org/wiki/Generative_adversarial_network) in particular, have been all the rage in the computer vision and deep learning communities for a few years now. These models are notoriously difficult to train, and it has been challenging to scale them up to larger (i.e., higher-res) images.

Nvidia has a [recent paper](https://arxiv.org/pdf/1710.10196.pdf) which effectively scales GANs up to 1024x1024 images. The basic idea is quite simple: start by training a generator and discriminator on very low resolution (2x2) images, and, as training progresses, add layers and increase the spatial resolution. Thus, the generator and the descriminator learn large-scale image structures first, then medium-scale, then fine-scale. This approach, dubbed "Progressive GANs", has a stabilizing influence on training, since the model doesn't need to learn all scales at once. They have super-cool visualizations of generated celebrity headshots:
#
<iframe width="560" height="315" src="https://www.youtube.com/embed/XOxxPcy5Gr4?rel=0" frameborder="0" gesture="media" allow="encrypted-media" allowfullscreen></iframe>
#

To play around with this, I cloned [the repo](https://github.com/tkarras/progressive_growing_of_gans) and downloaded the trained model binary `100-celeb-hq-1024x1024-ours` [from google drive](https://drive.google.com/open?id=0B4qLcYyJmiz0WUI5b3dBTWkxQU0). The models are implemented in Theano, which I haven't used before (and which is [no longer being developed](https://groups.google.com/forum/#!msg/theano-users/7Poq8BZutbY/rNCIfvAEAwAJ)). I wrote a notebook to use the generative model sample random celebrity faces -- input a random 512-D feature vector and it produces a celebrity face. The notebook can be viewed [here]({static}/notebooks/generate-celeb-samples.html) or downloaded [here]({static}/notebooks/generate-celeb-samples.ipynb). The model is pretty resource hungry -- running single-threaded on my laptop, it takes 40 seconds and ~3GB of RAM to produce a single image.

About half of the samples looked realistic...

![realistic head shot of handsome man]({static}/images/very_good.png)

![realistic head shot that looks vaguely like fat elvis]({static}/images/good.png)

...or almost right:

![realistic head shot with half a pair of glasses]({static}/images/disappearing_glasses.png)

![lady with horrifying mole on head]({static}/images/moley-mole-mole.png)

However, about 1/3 of the images were unnerving...

![woman who is too happy]({static}/images/happy-insane.png)

![goat-woman hybrid with steve buscemi teeth]({static}/images/bearded_woman.png)

...and some are downright disturbing:

![nightmarish image of middle-aged man with messed up mouth]({static}/images/nightmare.png)

![disturbing pic of young man with half-bald head that has a seam with green boogers coming out]({static}/images/nightmare2.png)

![otherworldly, arty-looking picture of a ghost]({static}/images/nightmare3.png)

The main purpose of this paper is to demonstrate that, with a clever multiscale training schedule, standard GANs can produce realistic images at high resolution. The most impressive results are achieved on a carefully curated dataset with a limited domain -- the celebrity dataset is carefully preprocessed using "classical" image processing so that the faces are aligned and the background is just-so. 

I think it's interesting to consider the failure modes of this model, in particular the image with disappearing glasses (3rd from the top). Many of the weird artifacts in these images are due to the fact that the model has no notion of the *objectness* of the pixel patterns that it sees. Mapping a real-valued feature vector to a texture, a color, lines, makes sense. Continuously changing the pose of the head, the hair/skin color, or the quality of the lighting is sensible; likewise one can imagine morphing the color and texture of the background. However, continuously changing model output from "no-glasses-in-image" to "has-glasses-in-image" makes less sense. In theory the model can learn discrete decision boundaries, but the architecture is not set up to explicitly capture the fact that pixel patterns are generated by discrete objects with properties. There are analogous problems with generative language models: individual phrases and clauses are okay, but the model has trouble combining them into a sensible whole.

The stabilizing influence of the multiscale training procedure is an important contribution to the GAN literature. However, it seems like confabulating more complex scenes requires a more sophisticated representation of the latent space than is afforded by a 512-dimensional vector. A better approach might be as simple as encouraging a more interpretable latent representation ([as in infoGANs](https://arxiv.org/abs/1606.03657)), or may require a more explicit "inverse rendering approach" (as in [Geoff Hinton's capsules](https://www.youtube.com/watch?v=rTawFwUvnLE)).
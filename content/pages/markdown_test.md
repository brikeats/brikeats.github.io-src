Title: Brian Keating
Slug: markdown-test
URL: 
Author: Brian Keating
Summary: Test for plugins and markdown display

Check, check. Lorem ipsum dolor sit amet, some math: $\chi^2$ consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. 
$$\alpha_0^\xi$$
  
#
<iframe width="560" height="315" src="https://www.youtube.com/embed/bLqJHjXihK8" frameborder="0" allowfullscreen></iframe>

Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 

https://www.youtube.com/watch?v=uPN-GcFqN1o

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut some latex: $\chi^2$ labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris `code_stuff_here` nisi ut aliquip ex ea commodo consequat.

![Alt Text]({filename}/images/lenet.jpg)

Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.


    import cv2

    def deskew(img):
        m = cv2.moments(img)
        if abs(m['mu02']) < 1e-2:
            return img.copy()
        skew = m['mu11']/m['mu02']
        M = np.float32([[1, skew, -0.5*SZ*skew], [0, 1, 0]])
        img = cv2.warpAffine(img, M, (SZ, SZ), flags=cv2.WARP_INVERSE_MAP | cv2.INTER_LINEAR)
        return img


* list item
* list item2

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
Section 1.10.32 of "de Finibus Bonorum et Malorum", written by Cicero in 45 BC
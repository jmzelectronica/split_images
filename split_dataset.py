
#split image

import cv2
img = cv2.imread('DJI_0018.JPG')
for r in range(0,img.shape[0],360):
    for c in range(0,img.shape[1],480):
        cv2.imwrite(f"img{r}_{c}.png",img[r:r+360, c:c+480,:])


#import cv2
#img = cv2.imread('image.png')
#for r in range(0,img.shape[0],30):
#    for c in range(0,img.shape[1],30):
#        cv2.imwrite(f"img{r}_{c}.png",img[r:r+30, c:c+30,:])

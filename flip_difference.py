# produce the difference of the grumpycat image and its horizontal reflection

import Image
import ImageChops
import numpy as np

img1 = Image.open("example.png")
img2 = img1.transpose(Image.FLIP_LEFT_RIGHT)
diff = ImageChops.difference(img1, img2)
identicals = 

img2.save("example_flip.png")
diff.save("example_diff.png")
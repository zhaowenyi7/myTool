from PIL import Image
from pylab import *

im = array(Image.open('E:\\data\\kjp.jpg'))
imshow(im)
print('click 3 points')
x = ginput(3)
print('you clicked:', x)
show()

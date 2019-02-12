from  PIL import Image
from  pylab import *
#from numpy import *
im = array(Image.open(r"C:\Users\AURORA\Desktop\work\image_python\image\1.jpg"))
imshow(im)
x=[100,100,500,500,250,250,30,100]
y=[50,270,100,150,210,100,50,60]
plot(x,y,"r*")
plot(x[:2],y[:2])
plot(x[2:4],y[2:4],'m')
plot(x[1:5],y[2:6],'bx:')
title('plotting:"1_new,jpg"')
show()

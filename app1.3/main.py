import numpy as np 
from PIL import Image

class Canvas:
    """Objects where all shapes are going to be drawn"""

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color

        #Create a 3d numpy of zeros
        self.data = np.zeros((self.height,self.width, 3), dtype=np.uint8)
        self.data[:] = self.color

    def make(self,imagepath='app1.3\\canvas.png'):
        img = Image.fromarray(self.data, 'RGB')
        img.save(imagepath)


class Rectangle:

    def __init__(self,x,y,width,height,color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, canvas):
        paint = self.x
        return paint

class Square:

    def __init__(self,x,y,side,color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

    def draw(self, canvas):
        paint = self.x
        return paint



    
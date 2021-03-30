import numpy as np 
from PIL import Image

# Create a 3d numpy array of zeros, then replace zeros (black pixels) with yellow pixels.
data = np.zeros((5,4,3), dtype=np.uint8)
data[:]= [255, 255, 0]
print(data)

# Make a red patch (on the rows; so rows from 0 to 5; columns 0 to 4)
data[0:3, 0:2]= [255, 200, 0]
data[3:4, 1:4]= [245, 3, 233]





img = Image.fromarray(data, 'RGB')
img.save('app1.3\\example\\canvas.png')
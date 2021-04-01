from shapes import Rectangle, Square
from canvas import Canvas

# Get canvas width and height from the user
canvas_width = input("Enter the width of canvas: ")
canvas_height = input("Enter the height of canvas: ")

# Make a dictionary of color codes and prompt for color
colors = {"white": (255,255,255), "black": (0,0,0)}
canvas_color = input("Enter the color of canvas: (white or black)")

# Create a canvas witht he user data
canvas = Canvas(width=canvas_width, height=canvas_height, color=colors[canvas_color])

while True:
    shape_type = input("What do you like to draw? Enter quit to quit. ")
    #Ask for rectangle data and create a rectangle if user entered 'rectangle'
    if shape_type.lower() == "rectangle":
        rec_x = int(input("Enter x of the rectangle: "))
        rec_y = int(input("Enter y of the rectangle: "))
        rec_width = int(input("Enter the width of the rectangle: "))
        rec_height = int(input("Enter the height of the rectangle: "))
        red = int(input("How much RED should the rectangle have? "))
        green = int(input("How much GREEN should the rectangle have? "))
        blue = int(input("How much BLUE should the rectangle have? "))

        # Create the rectangle
        r1 = Rectangle(x=rec_x, y=rec_y, height=rec_height, width=rec_width, color=(red,green,blue))
        r1.draw(canvas)

    if shape_type.lower() == "square":
        rq_x = int(input("Enter x of the square "))
        sq_y = int(input("Enter y of the square: "))
        sq_side = int(input("Enter the side of the square: "))
        red = int(input("How much RED should the square have? "))
        green = int(input("How much GREEN should the square have? "))
        blue = int(input("How much BLUE should the square have? "))

        # Create the square
        s1 = Square(x=rec_x, y=rec_y, side=sq_side, color=(red,green,blue))
        s1.draw(canvas)    


# canvas = Canvas(width=10, height=10, color=(255,255,255))
# r1 = Rectangle(x=1,y=6,width=5,height=2,color=(100,124,0))
# r1.draw(canvas)
# s1 = Square(x=6,y=6,side=3,color=(10,24,240))
# s1.draw(canvas)


canvas.make(imagepath='app1.3\\canvas.png')



    
import turtle
import cv2

# def racecar(lightning):
#     lightning.fillcolor('red')
#     lightning.begin_fill()
#     lightning.circle(20)
#     lightning.end_fill()

# turtle.title('Kachow')
# i_am_speed = turtle.Screen()
# # i_am_speed.bgpic("map_google.gif")
# i_am_speed.setup(750,850)
# i_am_speed.addshape('LMQ.gif')
# lightning = turtle.Turtle()
# lightning.shape('LMQ.gif')
# # lightning.color('red')
# # lightning.width(0.1)
# lightning.penup()
# lightning.goto(90,-280)
# lightning.pendown()


# input()

# Get xml files for creation of cascades
cascPath = "cascade_right.xml"
cascPath2 = "cascade_left.xml"

# Create the haar cascade
arrowCascade = cv2.CascadeClassifier(cascPath)
arrowCascade2 = cv2.CascadeClassifier(cascPath2)

slowpoke = cv2.VideoCapture('test.avi')

width = int(slowpoke.get(3))
height = int(slowpoke.get(4))
   
size = (width, height)

result = cv2.VideoWriter('result.avi', 
                         cv2.VideoWriter_fourcc(*'MJPG'),
                         10, size)

while(slowpoke.isOpened()):
    ret, image = slowpoke.read()
    # if ret == True:
    #     cv2.imshow('Vid', image)
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect arrows in the image
    arrows = arrowCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
    )
    arrows2 = arrowCascade2.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
    )
    
    for (x, y, w, h) in arrows:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    for (x, y, w, h) in arrows2:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('video',image) 
    result.write(image)



# https://www.geeksforgeeks.org/draw-moving-object-using-turtle-in-python/
# https://realpython.com/beginners-guide-python-turtle/
# https://pythonguides.com/attach-image-to-turtle-python/
# https://www.pixarpost.com/2017/05/ultimate-lightning-mcqueen-hands-on-review.html
# https://pythonprogramming.net/haar-cascade-face-eye-detection-python-opencv-tutorial/
import turtle
import cv2
import time

# Get xml files for creation of cascades
cascPath_r = "cascade_right.xml"
cascPath_l = "cascade_left.xml"

# Create the haar cascade
arrowCascade_r = cv2.CascadeClassifier(cascPath_r)
arrowCascade_l = cv2.CascadeClassifier(cascPath_l)

# select video file to load
slowpoke = cv2.VideoCapture('main_video.avi')
# slowpoke = cv2.VideoCapture('test_arrows.avi')

# create results video file
width = int(slowpoke.get(3))
height = int(slowpoke.get(4))
   
size = (width, height)

result = cv2.VideoWriter('main_results.avi', 
                         cv2.VideoWriter_fourcc(*'MJPG'),
                         10, size)

# result = cv2.VideoWriter('test_results.avi', 
#                          cv2.VideoWriter_fourcc(*'MJPG'),
#                          10, size)

# turtle initiation
turtle.title('Virtual Car')
i_am_speed = turtle.Screen()
i_am_speed.setup(850,850)
lightning = turtle.Turtle()
lightning.color('red')
lightning.shape('circle')
lightning.penup()
lightning.goto(0,0)
lightning.pendown()

# track changes in arrows
last_arrow = ''

# timing
start = time.time()

while(slowpoke.isOpened()):
    ret, frame = slowpoke.read()

    # convert to gray for easier identification
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect right arrows in the image
    arrow_r = arrowCascade_r.detectMultiScale(
        gray,
        scaleFactor=1.05,
        minNeighbors=3,
        minSize=(300, 300),
    )

    # Detect left arrows in the image
    arrow_l = arrowCascade_l.detectMultiScale(
        gray,
        scaleFactor=1.05,
        minNeighbors=3,
        minSize=(300, 300),
    )
    
    # draw a rectangle around them
    for (x, y, w, h) in arrow_r:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 8)
    for (x, y, w, h) in arrow_l:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 8)

    # control the turtle
    if len(arrow_r) > 0 and last_arrow!='right':
        last_arrow = 'right'
        lightning.right(90)
    elif len(arrow_l) > 0 and last_arrow!='left':
        last_arrow = 'left'
        lightning.left(90)
    else:
        lightning.forward(0.5)

    # save the video
    result.write(frame)

    elapsed_time = start - time.time()
    start = time.time()

    # print(elapsed_time)

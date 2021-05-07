# Run the program with "$python project.py"
# Code was added to Github in files so git clone should allow the file paths 
# to remain consistent
import cv2
import sys

# Get xml files for creation of cascades
cascPath = "cascade_right.xml"
cascPath2 = "cascade_left.xml"

# Create the haar cascade
arrowCascade = cv2.CascadeClassifier(cascPath)
arrowCascade2 = cv2.CascadeClassifier(cascPath2)

# Count beginning for the number of intersections the code needs to evaluate
i = 0

# Open an output file and set it as the standard output
with open('.\\output\\output.txt', 'w') as f:
    sys.stdout = f

    # Read the image
    imagePath = (f".\\input\\12 arrow_pics\\{i}.JPEG")
    image = cv2.imread(imagePath)
    # Convert the image to greyscale for faster, easier arrow detection
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

    # Calculates total number of arrows in the image for control purposes
    numarrows = len(arrows2) + len(arrows)

    print(f'Intersection {i+1}, image {i}.JPG')
    print(f"Found {numarrows} arrows")

    # Determines arrow direction for selection of proceeding file name
    if arrows is not None:
        direction = "right"
    elif arrows2 is not None:
        direction = "left"
    else:
        print(f'ERROR: No arrows detected in {imagePath}')
        exit()

    print(f'Arrow direction: {direction}')

    # Draw a rectangle around the arrows in the color image
    for (x, y, w, h) in arrows:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    for (x, y, w, h) in arrows2:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Uses rectangle size as determinant for program delay
    if w< 200 and h<200: 
        # Output the edited image to the screen so the delay between images can be 
            # utilized as vehicle "speed"
        cv2.imshow(f"arrows found in {i}.JPEG", image) 
        # Save the image with a box around the arrows in the output folder
        cv2.imwrite(f".\\output\\{i}.JPG", image) 
        # Pauses the program for the designated time for vehicle "speed" purposes
        cv2.waitKey(2000) 
        print('Time to reach next intersection: 2 seconds \n')
    else: 
        cv2.imshow(f"arrows found in {i}.JPEG", image) 
        cv2.imwrite(f".\\output\\{i}.JPG", image) 
        cv2.waitKey(6000) 
        print('Time to reach next intersection: 6 seconds \n')  

    # Resets arrow matrices
    arrows = 0
    arrows2 = 0

    # Loop through the remaining intersections
    # Code is a repeat of above with few changes
        # File name is now directional
        # Exit statement for when final desitnation has been reached was added
    while i < 6:
        # Read the image
        imagePath = (f".\\input\\12 arrow_pics\\{i}-{direction}.JPEG")
        image = cv2.imread(imagePath)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        print(imagePath)

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

        numarrows = len(arrows2) + len(arrows)

        print(f'Intersection {i+2}, image {i}-{direction}.JPG')

        # 2 arrows on an image are utilized to indicate the final destination has been reached
        if numarrows == 2:
            for (x, y, w, h) in arrows:
                cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
            for (x, y, w, h) in arrows2:
                cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
            
            print(f"Found {numarrows} arrows")
            cv2.imshow(f"arrows found in {i}-{direction}.JPEG", image) 
            cv2.imwrite(f".\\output\\{i}-{direction}.JPG", image)
            cv2.waitKey(6000) 
            print("Final Destination!")
            exit()

        print(f"Found {numarrows} arrows")

        if len(arrows):
            direction = "right"
        elif len(arrows2):
            direction = "left"
        else:
            print(f'ERROR: No arrows detected in {imagePath}')
            exit()

        print(f'Arrow direction: {direction}')

        # Street intersection enumeration
        i += 1

        # Draw a rectangle around the arrows
        for (x, y, w, h) in arrows:
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        for (x, y, w, h) in arrows2:
            cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

        if w< 200 and h<200: 
            cv2.imshow(f"arrows found in {i}-{direction}.JPEG", image) 
            cv2.imwrite(f".\\output\\{i}-{direction}.JPG", image) 
            cv2.waitKey(2000) 
            print('Time to reach next intersection: 2 seconds \n')
        else: 
            cv2.imshow(f"arrows found in {i}-{direction}.JPEG", image) 
            cv2.imwrite(f".\\output\\{i}-{direction}.JPG", image) 
            cv2.waitKey(6000)   
            print('Time to reach next intersection: 6 seconds \n')    

        arrows = 0
        arrows2 = 0
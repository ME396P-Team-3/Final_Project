# Final_Project

Our project objective is to make an autonomous car virtually navigate Austin from right outside the Capital to the EER building on campus, using computer vision based on arrow identification. 

You can find a map of our robot’s path in “itinerary.png”. Our main script is “project.py”. 

The virtual experience will be a series of intersection snapshots taken from Google Maps. 
For each picture, there will be either a right or left arrow at the intersection. The car will identify the type and make the associated turn. This will repeat iteratively until the car reaches the EER. 

In addition to this, we have simulated speed of vehicle by displaying the images with varying time delay. This would allow for scalability of our program. The delay between images will be determined by  arrow size: if the arrow is smaller than the threshold dimensions we set (w,h), then we programmed the car to go “faster”; if it is bigger, it will go "slower". 

We have used openCV here as our primary package for computer vision. You can access the 2 cascade classifiers we used to identify both the left and right arrows, “cascade_left.xml” and “cascade_right.xml”. The original source of these cascade classifiers can be found here: https://github.com/ryangmolina/rpi-car-arrow-detection-using-cascade-classifier.

We’ve also included all the input pictures of the intersections in the “input/12_arrow_pics” file and the correct output in the “output” file, for reference.

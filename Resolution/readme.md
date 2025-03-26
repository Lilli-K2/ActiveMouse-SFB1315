### Resolution of the video feed

If you know or suspect that your resolution does not match any of the conversion factors we already provide in the ActiveMouse code, we encourage acquainting yourself with this [opencv_tutorial](https://github.com/learncodebygaming/opencv_tutorials).
We specifically used the code provided in the [intro](https://github.com/learncodebygaming/opencv_tutorials/blob/master/001_intro/main.py) and modified it for our specific purposes.
In [detect object](https://github.com/Lilli-K2/ActiveMouse/blob/main/Resolution/DetectObject.py) you can find this modified code. It now identifies two objects from a screenshot and using the [calculation](https://github.com/Lilli-K2/ActiveMouse/blob/main/Resolution/Calculation.py) code gives you the distance between these objects in pixels plus the necessary factor to convert it to centimeters.

<strong>Before you start</strong> please note the following steps.
- Take a video of your setup using the camera and exact conditions your experimental recordings will be made under.
      In this video position two easily recognizable objects a known distance from eachother.
      We recorded three distances (5, 10, 15cm) to minimize human error a bit by averaging the results later.
- Take screenshots of the different positions and name them Haystack1-3. Make sure that the resolution is not changed when saving          the pngs!
- Manually select your objects and save them as different pngs (unchanged quality) under Needle and Tweedle. You can make                  rectangular selections even if the objects themselves are not rectangular.

Now load your images into the DetectObject script. Be mindful of using the correct images for the haystack (complete screenshot with specific distance between the objects) and needle and tweedle (the two objects).

<strong>You will also need</strong> to change the <strong>h_cm</strong> value in the <strong>calculation</strong> script for each respective real-life distance before running the <strong>DetectObject</strong> script.
As the code contains waitKey commands you need to press any key on your keyboard after each image is generated to keep it running. 
You can now find your specific conversion factor in a .txt file named the same. The code also gives you different pngs to ensure correct identification of the objects.    

</p>
<kbd>
<strong>Attention!</strong>
This tutorial only works if at no point the original resolution of the video is tampered with.
</kbd>
</p>

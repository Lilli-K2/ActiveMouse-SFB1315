# ActiveMouse

With ActiveMouse you can check at a glance if dlc-live tracking is satisfactory via a neat pop-up. It also generates graphic reprensentations of your animal's movements immediately after stopping the tracking thus giving you an overview of your animal's activity.
This code is designed to be used with deeplabcut-live and a deeplabcut model specifically trained to meet your tracking needs.
As you choose how to train the model the tracking itself and thus this code are highly adaptable to all kinds of projects and animals.

---

### Installation Instructions

<p align="left">
  <span style="display: inline-block; width: 60%;">
    <strong>ActiveMouse</strong>  
    <br>  
   This is the installation guide to setup deeplabcutlive gui with ActiveMouse
  </span>
</p>


### Setting up Deep Lab Cut live and ActiveMouse

We recommend using a conda environment:
- [Anaconda ](https://anaconda.org/anaconda)

### Install Dependencies

For a more detailed guide on installing [deeplabcut-live](https://github.com/DeepLabCut/DeepLabCut-live) and training models with [deeplabcut](https://github.com/DeepLabCut/DeepLabCut) please see their respective documentations.


Dlc live gui with gpu:
```bash
conda create -n dlc-live python=3.7 tensorflow-gpu==1.13.1
```
Dlc live gui without gpu:
```bash
conda create -n dlc-live python=3.7 tensorflow==1.13.1 
```
activate the environment
```bash
conda activate dlc-live 
```
install dlc live gui
```bash
pip install deeplabcut-live-gui
```
<kbd>
<strong>Attention</strong>
Please note that you need to manually install seaborn and matplotlib into your environment. This is easily done with a pip install and potentially a pip upgrade of these packages.
</kbd>

start dlclivegui
```bash
dlclivegui
```


<kbd>
<strong>Additional information:</strong>
Please keep in mind that this guide is for NVIDIA graphic cards. For other graphic cards please follow the instruction of the manufacturer
</kbd>


---
 
### Setting up the camera

To be able to use your camera in dlclive you need to know the correlating index.
In the folder [Camera-Test](https://github.com/Nasr-SFB1315/MouseCare/tree/main/Camera-Test) is a tutorial on how to find it.


<img align="right" src="https://github.com/Nasr-SFB1315/images/blob/main/dlclivecamera.png?raw=true" />
<p align="left">
First you need to set up camera by clicking on <strong>Init Cam</strong> make sure that it is set to <strong>OpenCVCam</strong> and give it a name. 
Click on <strong>Edit Camera Settings</strong> set the <strong>device</strong> to the corresponding index of the camera you use. You can set the values according to your needs. 
</p>
<p align="left">
 <kbd>
<strong>Addition information:</strong>
In regard to resolution and frame rate: Both can be adjusted according to your needs, but if you change frame rate in dlclive you also need to adjust it in MouseCare. We had success with a frame rate of 30fps, which is what we recommend to start with.
Changing the resolution as well as frame rate will change the load on the GPU/CPU. This dependents on the graphics card. For example, a 4090 can handle higher resolution than a 3060. We recommend testing with different resolution and fps to gauge the capability of your setup.
</kbd>
</p>


---

### Adding MouseCare

Make sure you have downloaded [ActiveMouse](https://github.com/Lilli-K2/ActiveMouse) from the repository.

<img align="right" src="https://github.com/Nasr-SFB1315/images/blob/main/dlclivecamera.png?raw=true" />
<p align="left">

Now we need to add ActiveMouse as the processor. Select the folder you saved ActiveMouse to under <strong>Processor Dir</strong>. Confirm that you want to add the folder to your dropdown list for a quicker set-up process the next time you open the deeplabcut-live gui.
Under <strong>Processor</strong> select <strong>MouseLickImageProcessor</strong>. Make sure to update the processor under <strong>Edit Proc Settings</strong> so everything is loaded correctly.
</p>
<kbd>
<strong>Additional information:</strong>
The pictures used in the ActiveMouse pop-up can be adjusted to your liking, although we suggest sizing them to 800x600 as this size works best with the tkinter gui in our experience. Make sure to change the <strong>lick_image</strong> and <strong>no_lick_image</strong> paths to the actual images you are using.
You can also change the accuracy threshold for displaying an image indicating satisfactory tracking under <strong>lik_thresh</strong>. It is set to 0.9 by default which has worked well for our past experiments but can obviously be adjusted according to your needs e.g. 0.99 for only considering very accurately tracked points or 0.7 to also consider more inaccurately tracked points.
Please note that you should update the Processor under <strong>Edit Proc Settings</strong> every time you make changes to the processor file.
Any changes to the processor that disrupt regular dlc-live flow will inevitably crash the dlc-live gui. Should you find yourself unable to open the gui consider reverting back to ActiveMouse as it is provided in this guide. 
</kbd>
</p>

---



### Adding the network

Make sure you have downloaded the [trained network](https://github.com/Lilli-K2/ActiveMouse/tree/main/trained-network) from the repository.
<br>
For first time use, we recommend using our [Accuracy-Test](https://github.com/Nasr-SFB1315/MouseCare/tree/main/Accuracy-Test) first, to see if the network recognizes the mouse in the setup accurately. 



<img align="right" src="https://github.com/Nasr-SFB1315/images/blob/main/dlclivecamera.png?raw=true" />
<p align="left">

Under <strong>DeepLabCut:</strong> select <strong>add DLC</strong>. Choose an easily recognizable name for the network e.g. ActiveMouse for quicker setup the next time you need it. Now navigate to the folder that contains your exported deeplabcut network under <strong>model path</strong>.
</p>
<kbd>
<strong>Additional information:</strong>
Should deeplabcut-live not recognize the exported deeplabcut model it is very likely that the selected folder is not what dlc-live expexted. For the network provided in this repository select the folder named <strong>DLC_LastMouse4Point_resnet_50_iteration-1_shuffle-1</strong>.
</kbd>
</p>

Press <strong>Update</strong> to ensure all changes have been saved correctly. 
You can now either start the tracking immediately by hitting <strong>Init</strong> or choose to use the <strong>Display DLC Keypoints</strong> feature provided by dlc-livebefore initiating the tracking.

</p>
<kbd>
<strong>Additional information:</strong>
Displaying the Keypoints is a great visual aid in making sure that the network is loaded correctly and in fact tracking the animal. However, it should be noted that especially with higher resolution videos your CPU/GPU is already pretty full and insufficient or lagging display of the keypoints is to be expected. Lagging display or lack thereof is not necessarily an indicator of unsatisfactory tracking, but rather an overloaded CPU/GPU.
You will also probably find that your videofeed is interrupted while loading the network. As soon as the network is loaded correctly the feed should resume. Should you notice an unusually slow or otherwise faulty video feed consider for example updating from CPU to GPU or using a lower resolution video feed.
</kbd>
</p>

---

### Setting up the session

Now we can finally set up the session.


<img align="right" src="https://github.com/Nasr-SFB1315/images/blob/main/dlclivecamera.png?raw=true" />
<p align="left">
Choose a folder under <strong>Directory</strong> you want the data to be saved to.
Now <strong>Set Up Session</strong>. Once again you may need to wait for the video feed to resume after a short while.
You will notice that you are now able to press the <strong>On-Button</strong> under <strong>Record</strong>.

</p>
<kbd>
<strong>Additional information:</strong>
Should you run into problems while setting up the Recording session or immediately after starting the recoring it is advised to check the terminal. Oftentimes an incorrect path to one of the images or a missing python package can lead to ActiveMouse not working as expected. Most issues are easily fixed by changing a path or pip installing a necessary python package.
</kbd>
</p>
  
As soon as you start your recording a <strong>pop-up window</strong> will appear, indicating the accuracy with which your animal is being tracked live.
With the code provided in ActiveMouse a positive image suggests the tracking of the mouse's neck tracking-point with 90% accuracy.
  
This allows the user to quickly realise at any point that the tracking has been unsatisfactory for a significant amount of time and interfere while the experiment is still being run. Thereby hopefully allowing uncomplicated changes to be made to the setup and ensuring swift resumption of the experiment.

</p>
<kbd>
<strong>Additional information:</strong>
Common problems we have encountered with inadequate tracking are bad lighting conditions, poor camera angles or camera quality as well as unsuitable deeplabcut networks. For the ladder we suggest retraining an already existing network with further video  footage or considering training a model from scratch to fit your specific conditions. For a detailed guide on training your model see the deeplabcut documentation.
</kbd>
</p>





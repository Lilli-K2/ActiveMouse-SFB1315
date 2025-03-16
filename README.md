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
start dlclivegui
```bash
dlclivegui
```


<kbd>
<strong>Addition information:</strong>
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

Make sure you have downloaded [MouseCare](https://github.com/Nasr-SFB1315/MouseCare/tree/main/MouseCare) from the resository.

<img align="right" src="https://github.com/Nasr-SFB1315/images/blob/main/dlclivecamera.png?raw=true" />
<p align="left">
To add MouseCare you need go to <strong>Processor Dir</strong> and navigate to the <strong>folder</strong> where you have downloaded MouseCare. 
From the drop down menu <strong>Processor</strong> and select <strong>MouseCare</strong>. Then press <strong>Edit Proc Settings</strong> to make sure that everthing is in order. Finish it by <strong>Set Proc</strong>
</p>
<kbd>
<strong>Addition information:</strong>
Please keep in mind once you have added MouseCare to dlclive it will be part of the loading process of dlvlive. This means if you make faulty changes to MouseCare, it will not only crash MouseCare but dlclive as well.
</kbd>
</p>


---



### Adding the network

Make sure you have downloaded the [trained network](https://github.com/Nasr-SFB1315/MouseCare/tree/main/Network) from the repository.
<br>
For first time use, we recommend using our [Accuracy-Test](https://github.com/Nasr-SFB1315/MouseCare/tree/main/Accuracy-Test) first, to see if the network recognizes the mouse in the setup accurately. 



<img align="right" src="https://github.com/Nasr-SFB1315/images/blob/main/dlclivecamera.png?raw=true" />
<p align="left">
Text here on how to proceed

</p>
<kbd>
<strong>Addition information:</strong>
The network is trained to recognize the facial features of head fixed mice. Given the scope of the project, it is not feasable to train a network to work in every setup imaginable, but it is possible to either train the provided network with new video data from your setup or generate a new network using deeplabcut. The tutorial on how to generate a new network is in the folder network.

</kbd>
</p>


---

### Setting up the session

Now that all the different softwares haven been loaded into dlc live, we can set up the session



<img align="right" src="https://github.com/Nasr-SFB1315/images/blob/main/dlclivecamera.png?raw=true" />
<p align="left">
Text here on how to proceed

</p>
<kbd>
<strong>Addition information:</strong>
It is recommended to check the terminal for information in case it does not work as expected. A common error is that not all the required python packages are installed on your system. Which can be fixed with the proper pip installs.

</kbd>
</p>




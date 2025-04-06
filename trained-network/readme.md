This is the [network](https://github.com/Lilli-K2/ActiveMouse-SFB1315/tree/main/trained-network/exported-models-V2-Copy/DLC_LastMouse4Point_resnet_50_iteration-1_shuffle-1) we have been using as we conduct our experiments. It is trained to track a <strong>single mouse</strong> based on <strong>four tracking points</strong> from a top-view in the dark under red light.
These points include the nose, neck, butt and tail of the animal. <br>

Make sure to download the entire ["DLC_LastMouse4Point_resnet_50_iteration-1_shuffle-1"](https://github.com/Lilli-K2/ActiveMouse-SFB1315/tree/main/trained-network/exported-models-V2-Copy/DLC_LastMouse4Point_resnet_50_iteration-1_shuffle-1) folder. Please be aware that the folder is quite large (195MB) before choosing a location for it to be saved to. <br>
After downloading the network find the <strong>pose_cfg.yaml</strong> file and change the <strong>project_path</strong> to the correct path. 
Should you encounter problems opening the trained network later in the dlc-live gui you might have given the wrong path or may need to manually change the other paths in the .yaml file. Usually choosing the correct <strong>project_path</strong> will suffice.

</p>
<kbd>
<strong>Attention!</strong>
This network will obviously not work for your experiments if you are using multiple mice under different camera or lighting conditions or other animal species altogether. In this case refer to DeepLabCut to train your own network and adjust the ActiveMouse code according to the points you consider in your tracking.
</kbd>
</p>

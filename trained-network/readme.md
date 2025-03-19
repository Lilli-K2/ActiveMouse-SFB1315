This is the [network]() we have been using as we conduct our experiments. It is trained to track a <strong>single mouse</strong> based on <strong>four tracking points</strong> from a top-view in the dark under red light.
These points include the nose, neck, butt and tail of the animal.

After downloading the network find the <strong>pose_cfg.yaml</strong> file and change the <strong>project_path</strong> to the correct path. 
Should you encounter problems opening the trained network later in the dlc-live gui you might have given the wrong path or may need to manually change the other paths in the .yaml file. Usually choosing the correct <strong>project_path</strong> will suffice.

</p>
<kbd>
<strong>Attention!</strong>
This network will obviously not work for your experiments if you are using multiple mice under different camera or lighting conditions or other animal species altogether. In this case refer to DeepLabCut to train your own network and adjust the ActiveMouse code according to the points you consider in your tracking.
</kbd>
</p>

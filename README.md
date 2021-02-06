[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donate_LG.gif)](https://www.paypal.com/donate?hosted_button_id=TV9HL7YRHZR7U)  
![GitHub](https://img.shields.io/github/license/BlenderDefender/MoCapkiteFA?color=green&style=for-the-badge)
![GitHub issues](https://img.shields.io/github/issues/BlenderDefender/MoCapkiteFA?style=for-the-badge)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/BlenderDefender/MoCapkiteFA?style=for-the-badge)
# MoCapkiteFA
MoCapkiteFA is an addon for blender, that allows you to quickly set up facial motion capture with just 3 easy steps.



After shooting your footage and creating a head-model, do this following steps:


# 1. Open Your model and track your footage

If your head-model is already a Blender file, then just go and open it like in this image:

![Open Headfile](/Screenshots/Face_Mocap_Screenshot1.png?raw=true)

Otherwise go to File >> Append >> "Your head-model-file" >> Models >> "Your head model" and import your model.


Now it's time to track the footage.
It's very important that we do this in the layout Tab and just switch the workspace as you can see in the image, because the Addon won't work if we do this in another way.


![Switch Workspace](/Screenshots/Face_Mocap_Screenshot2.png?raw=true)


In the Motion Tracking Workspace, open your footage and set scene frames. Pay attention to the aspect ratio and set the scene ratio to the ratio of your Footage: 


![Open Footage](/Screenshots/Face_Mocap_Screenshot3.png?raw=true)


Now its time to set up your trackers. Track every tracking point of your face. Make sure you didn't leave the Layout Tab:

![Track](/Screenshots/Face_Mocap_Screenshot4.png?raw=true)


# 2. Align your model to view

Back in 3D View, select your head object. Press Shift + A and Navigate to Add >> Motion Capture >> Pre Align:

![Pre Align](/Screenshots/Face_Mocap_Screenshot5.png?raw=true)

Then you'll have to do the exact aligning manually. Open up a background image and switch to wireframe mode. Take your time, it's important that the mesh almost fits perfectly:

![Align](/Screenshots/Face_Mocap_Screenshot6.png?raw=true)

# 3. Set up Motion Capture

Switch Back to Solid mode, select the face Object and Press Shift + A Add >> Motion Capture >> Setup Facial Motion Capture. This may take a while:

![Setup MoCap](/Screenshots/Face_Mocap_Screenshot7.png?raw=true)

After the programm finished successfully, it should look like this:

![Finished](/Screenshots/Face_Mocap_Screenshot8.png?raw=true)

And yes, that's all you have to do. You might adjust the weight paint a bit so that it looks more natural.
**[Watch this video from CG Matter](https://www.youtube.com/watch?v=uNK8S19OSmA) if you want a detailed explanaition on how to do the MoCap.**

## System requirements:
| **OS** | **Blender** |
| ------------- | ------------- |
| OSX | Testing, please give feedback if it works for you. |
| Windows | Blender 2.80+ |
| Linux | Testing, please give feedback if it works for you. |

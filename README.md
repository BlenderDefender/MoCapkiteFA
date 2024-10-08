[![Donate](https://img.shields.io/endpoint?url=https%3A%2F%2Fraw.githubusercontent.com%2FBlenderDefender%2FBlenderDefender%2Fshields_endpoint%2FMOCAPKITEFA.json)](https://bd-links.netlify.app/mocapkite-fa)
![GitHub](https://img.shields.io/github/license/BlenderDefender/MoCapkiteFA?color=green&style=for-the-badge)
[![GitHub issues](https://img.shields.io/github/issues/BlenderDefender/MoCapkiteFA?style=for-the-badge)](https://github.com/BlenderDefender/MoCapkiteFA/issues)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/BlenderDefender/MoCapkiteFA?style=for-the-badge)

# MoCapkiteFA

MoCapkiteFA is an addon for Blender, that allows you to quickly set up facial motion capture with just 3 easy steps.

After shooting your footage and creating a head-model, here's what you'll have to do:

# 1. Open Your model and track your footage

If your head-model is already a Blender file, then just go and open it like in this image:

![Open head model](https://github.com/BlenderDefender/MoCapkiteFA/raw/main/Screenshots/screenshot_1_open_model.png)

Otherwise go to File >> Append >> "Your head-model-file" >> Models >> "Your head model" and import your model.

Now it's time to track the footage!
It's very important that we do this in the 'Layout' tab and just switch the workspace as you can see in the image, because the Addon won't work if we do this in another way.

![Switch Workspace](https://github.com/BlenderDefender/MoCapkiteFA/raw/main/Screenshots/screenshot_2_switch_workspace.png)

In the Motion Tracking Workspace, open your footage and set scene frames. Pay attention to the aspect ratio and set the scene ratio to the ratio of your footage:

![Open Footage](https://github.com/BlenderDefender/MoCapkiteFA/raw/main/Screenshots/screenshot_3_open_footage.png)

Now its time to set up your trackers. Track every tracking point of your face. Make sure you don't leave the Layout Tab:

![Track](https://github.com/BlenderDefender/MoCapkiteFA/raw/main/Screenshots/screenshot_4_track.png)

# 2. Align your model to view

Back in 3D View, select your head object. Press Shift + A and Navigate to Add >> Motion Capture >> Pre Align:

![Pre Align](https://github.com/BlenderDefender/MoCapkiteFA/raw/main/Screenshots/screenshot_5_pre_align.png)

Then you'll have to do the exact aligning manually. Open up a background image and switch to wireframe mode. Take your time, it's important that the mesh almost fits perfectly:

![Align](https://github.com/BlenderDefender/MoCapkiteFA/raw/main/Screenshots/screenshot_6_align.png)

# 3. Set up Motion Capture

Switch back to Solid mode, select the face object and Press Shift + A Add >> Motion Capture >> Setup Facial Motion Capture. This may take a while:

![Setup MoCap](https://github.com/BlenderDefender/MoCapkiteFA/raw/main/Screenshots/screenshot_7_set_up_mocap.png)

After the programm finished successfully, it should look like this:

![Finished](https://github.com/BlenderDefender/MoCapkiteFA/raw/main/Screenshots/screenshot_8_finished.png)

And yes, that's all you have to do. You might adjust the weight paint a bit so that it looks more natural.
**[Watch this video from CG Matter](https://www.youtube.com/watch?v=uNK8S19OSmA) if you want a detailed explanation on how to do the MoCap.**

## System requirements:

| **OS**  | **Blender**                                        |
| ------- | -------------------------------------------------- |
| OSX     | Testing, please give feedback if it works for you. |
| Windows | Blender 2.80+                                      |
| Linux   | Testing, please give feedback if it works for you. |

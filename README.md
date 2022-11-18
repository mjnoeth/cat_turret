# cat_turret
Cat-Targeting Automated Turret (C.A.T.)

The Cat-Targeting Automated Turret (C.A.T.) consists of a raspberry pi, a webcam and a nerf turret.
The code to operate the turret will be contained in this repo. It will consist of:

- Vision: a python class used to track a target and determine if that target is a cat. It will be
          capable of displaying a live video feed with targets. It will also allow a callback to
          be provided that will provide coordinates of the target relative to the center and a
          boolean fire to indicate if the tracked target is a cat.

- Turret: a python class used to directly control motors that will aim the nerf gun. It will allow
          a callback to be provided if the turret is pointing at the target.

- FireRelay: a python class to control the firing mechanism.

This repo also contains the prototypes I used to learn how to use each device. They include:

- video_simple_webcam: a very simple program to just display the webcams video feed.
- video_tracking: a program that attempts to track motion and draw a box around a target.
- video_cat_detection: a program that attempts to detect cats and draw a box around a target.
- video_tracking_and_motion: a program that first detects motion; upon detecting motion the
  target will be cropped and searched to determine if a cat is present. If a cat is detected,
  a "free fire" mode will be activated for 5 seconds. Anytime a cat is detected, the free fire
  mode's timeout will be refreshed.
- relay_control: a program to control a relay that will ultimately replace the nerf gun's trigger
  mechanism

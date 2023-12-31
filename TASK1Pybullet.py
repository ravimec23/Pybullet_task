import gym
import os
import cv2
import pybullet_workshop_23
import pybullet as p
import time as t
import keyboard

CAR_LOCATION = [2, 3, 1.5]
VISUAL_CAM_SETTINGS = dict({
    'cam_dist': 13,
    'cam_yaw': 0,
    'cam_pitch': -110,
    'cam_target_pos': [0, 4, 0]
})

os.chdir(os.path.dirname(os.getcwd()))


env = gym.make('pybullet_workshop_23',
               arena="default",
               car_location=CAR_LOCATION,
               visual_cam_settings=VISUAL_CAM_SETTINGS
               )


while True:
    img = env.get_image(cam_height=0, dims=[512, 512])


    if keyboard.is_pressed(" "): 
        env.move(vels=[[0, 0], [0, 0]])
    elif keyboard.is_pressed("up"):  
        env.move(vels=[[5, 5], [5, 5]]) 
    elif keyboard.is_pressed("down"):  
        env.move(vels=[[-5, -5], [-5, -5]]) 
    elif keyboard.is_pressed("left"):  
        env.move(vels=[[-5, 5], [-5, 5]]) 
    elif keyboard.is_pressed("right"):
        env.move(vels=[[5, -5], [5, -5]]) 

    t.sleep(0.05)  
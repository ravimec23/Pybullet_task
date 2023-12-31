import gym
import os
import time as t
import cv2 as cv
import pybullet as p
import pybullet_workshop_23


VISUAL_CAM_SETTINGS = dict({
    'cam_dist': 13,
    'cam_yaw': 0,
    'cam_pitch': -110,
    'cam_target_pos': [0, 4, 0]
})

def create_environment(arena="arena2", car_location=[2, 0, 1.5], ball_location=None,
                       humanoid_location=None):
    return gym.make('pybullet_workshop_23', arena=arena, car_location=car_location,
                    ball_location=ball_location, humanoid_location=humanoid_location,
                    visual_cam_settings=VISUAL_CAM_SETTINGS)

def example_1():
    env = create_environment(ball_location=[4, 5, 1.5], humanoid_location=[-3, -4, 1.3])
    while True:
        img = env.get_image(cam_height=0, dims=[512, 512])
        cv.imshow("img", img)
        k = cv.waitKey(1)
        if k == ord('q'):
            break

def example_2():
    env = create_environment(ball_location=[4, 5, 1.5], humanoid_location=[-3, -4, 1.3])
    env.move(vels=[[2, 2], [2, 2]])
    t.sleep(2)
    env.move(vels=[[-2, 2], [-2, 2]])
    t.sleep(2)
    env.move(vels=[[-2, -2], [-2, -2]])
    t.sleep(2)
    env.close()

def example_3():
    env = create_environment(arena="default", car_location=[3, 0, 1.5],
                             ball_location=[4, 5, 1.5], humanoid_location=[-3, -4, 1.3])
    env.open_grip()
    env.move(vels=[[6, 6], [6, 6]])
    t.sleep(3.5)
    env.move(vels=[[0, 0], [0, 0]])
    env.close_grip()
    t.sleep(1)
    env.move(vels=[[-2, -2], [-2, -2]])
    t.sleep(2)
    env.move(vels=[[0, 0], [0, 0]])
    env.open_grip()
    t.sleep(2)
    env.close()

def example_4():
    env = create_environment(arena="default", car_location=[2, 0, 1.5],
                             ball_location=[-2, 0, 1.5], humanoid_location=[-6, 0, 1.2])
    env.open_grip()
    env.move(vels=[[2, 2], [2, 2]])
    t.sleep(3.5)
    env.move(vels=[[0, 0], [0, 0]])
    env.close_grip()
    t.sleep(1)
    env.open_grip()
    t.sleep(1)
    env.shoot()
    t.sleep(3)
    env.close()


example_1()
example_2()
example_3()
example_4()
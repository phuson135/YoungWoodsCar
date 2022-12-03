# """ 
# My CAR CONFIG 

# This file is read by your car application's manage.py script to change the car
# performance

# If desired, all config overrides can be specified here. 
# The update operation will not touch this file.
# """

# import os
# 
# #PATHS
# CAR_PATH = PACKAGE_PATH = os.path.dirname(os.path.realpath(__file__))
# DATA_PATH = os.path.join(CAR_PATH, 'data')
# MODELS_PATH = os.path.join(CAR_PATH, 'models')
# 
# #VEHICLE
# DRIVE_LOOP_HZ = 20      # the vehicle loop will pause if faster than this speed.
# MAX_LOOPS = None        # the vehicle loop can abort after this many iterations, when given a positive integer.
# 
# #CAMERA
CAMERA_TYPE = "CVCAM"   # (PICAM|WEBCAM|CVCAM|CSIC|V4L|D435|MOCK|IMAGE_LIST)
# IMAGE_W = 160
# IMAGE_H = 120
# IMAGE_DEPTH = 3         # default RGB=3, make 1 for mono
# CAMERA_FRAMERATE = DRIVE_LOOP_HZ
# CAMERA_VFLIP = False
# CAMERA_HFLIP = False
# CAMERA_INDEX = 0  # used for 'WEBCAM' and 'CVCAM' when there is more than one camera connected 
# # For CSIC camera - If the camera is mounted in a rotated position, changing the below parameter will correct the output frame orientation
# CSIC_CAM_GSTREAMER_FLIP_PARM = 0 # (0 => none , 4 => Flip horizontally, 6 => Flip vertically)
# 
# # For IMAGE_LIST camera
# # PATH_MASK = "~/mycar/data/tub_1_20-03-12/*.jpg"
# 
# #9865, over rides only if needed, ie. TX2..
# PCA9685_I2C_ADDR = 0x40     #I2C address, use i2cdetect to validate this number
# PCA9685_I2C_BUSNUM = None   #None will auto detect, which is fine on the pi. But other platforms should specify the bus num.
# 
# #SSD1306_128_32
# USE_SSD1306_128_32 = False    # Enable the SSD_1306 OLED Display
# SSD1306_128_32_I2C_ROTATION = 0 # 0 = text is right-side up, 1 = rotated 90 degrees clockwise, 2 = 180 degrees (flipped), 3 = 270 degrees
# SSD1306_RESOLUTION = 1 # 1 = 128x32; 2 = 128x64
# 
# #
# # DRIVE_TRAIN_TYPE
# # These options specify which chasis and motor setup you are using.
# # See Actuators documentation https://docs.donkeycar.com/parts/actuators/
# # for a detailed explanation of each drive train type and it's configuration.
# # Choose one of the following and then update the related configuration section:
# #
# # "PWM_STEERING_THROTTLE" uses two PWM output pins to control a steering servo and an ESC, as in a standard RC car.
# # "MM1" Robo HAT MM1 board
# # "SERVO_HBRIDGE_2PIN" Servo for steering and HBridge motor driver in 2pin mode for motor
# # "SERVO_HBRIDGE_3PIN" Servo for steering and HBridge motor driver in 3pin mode for motor
# # "DC_STEER_THROTTLE" uses HBridge pwm to control one steering dc motor, and one drive wheel motor
# # "DC_TWO_WHEEL" uses HBridge in 2-pin mode to control two drive motors, one on the left, and one on the right.
# # "DC_TWO_WHEEL_L298N" using HBridge in 3-pin mode to control two drive motors, one of the left and one on the right.
# # "MOCK" no drive train.  This can be used to test other features in a test rig.
# # "ETHERNET_API" no drive train.  This can be used to test other features in a test rig.
# # (deprecated) "SERVO_HBRIDGE_PWM" use ServoBlaster to output pwm control from the PiZero directly to control steering,
# #                                  and HBridge for a drive motor.
# # (deprecated) "PIGPIO_PWM" uses Raspberrys internal PWM
# # (deprecated) "I2C_SERVO" uses PCA9685 servo controller to control a steering servo and an ESC, as in a standard RC car
# #
DRIVE_TRAIN_TYPE = "ETHERNET_API"

ETHERNET_API = {
    "STEERING_LEFT":11,
    "STEERING_RIGHT":4,
    "THROTTLE_FORWARD":5,
    "THROTTLE_STOPPED":0,
}

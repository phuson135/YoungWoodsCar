
from donkeycar.parts.controller import Joystick, JoystickController
import subprocess
import logging
import time
from sh import tail
import os

logger = logging.getLogger(__name__)
class MyJoystick(Joystick):
    #An interface to a physical joystick available at /dev/input/js0
    def __init__(self, *args, **kwargs):
        super(MyJoystick, self).__init__(*args, **kwargs)

            
        self.button_names = {
            0x130 : 'a_button',
            0x131 : 'b_button',
            0x134 : 'y_button',
            0x133 : 'x_button',
            0x13b : 'M_button',
            0x13a : 'V_button',
            0x137 : 'right_shoulder',
            0x136 : 'left_shoulder',
            0x13c : 'Xbox_button',
            0x13e : 'Rstick_button',
            0x13d : 'Lstick_button',
        }


        self.axis_names = {
            0x00 : 'left_stick_horz',
            0x01 : 'left_stick_vert',
            0x04 : 'right_stick_vert',
            0x03 : 'right_stick_horz',
            0x10 : 'dpad_horiz',
            0x11 : 'dpad_vert',
            0x02 : 'left_trigger',
            0x05 : 'right_trigger',
        }



class MyJoystickController(JoystickController):
    #A Controller object that maps inputs to actions
    def __init__(self, *args, **kwargs):
        self.bbb_launched = None
        super(MyJoystickController, self).__init__(*args, **kwargs)


    def init_js(self):
        #attempt to init joystick
        try:
            self.js = MyJoystick(self.dev_fn)
            self.js.init()
        except FileNotFoundError:
            print(self.dev_fn, "not found.")
            self.js = None
        return self.js is not None

    def magnitude(self, reversed = False):
        def set_magnitude(axis_val):
            '''
            Maps raw axis values to magnitude.
            '''
            # Axis values range from -1. to 1.
            minimum = -1.
            maximum = 1.
            # Magnitude is now normalized in the range of 0 - 1.
            magnitude = (axis_val - minimum) / (maximum - minimum)
            if reversed:
                magnitude *= -1
            # print(magnitude)
            self.set_throttle(magnitude)
        return set_magnitude
    
    def launch_bbb_drive(self):
        if not (self.bbb_launched is None):
            self.close_bbb_drive()
            
        try:
            logger.info("Try Launching A New ./BBB drive")
            cmd = "nohup ./BBB  drive > output.txt 2>&1 &"
            self.bbb_launched = subprocess.Popen(cmd, shell=True)
            logger.info("Sucessfully launched a new ./BBB drive. "+str(self.bbb_launched.pid))
        except:
            logger.warning("Fail to launch a new ./BBB drive.")
            pass
        
    def close_bbb_drive(self):
        try:
            logger.info("Try killing the running ./BBB drive")
            cmd = "nohup ./BBB  kill > output.txt 2>&1 &"
            proc = subprocess.Popen(cmd, shell=True)
            logger.info("Sucessfully kill it. ")
            proc.kill()
            os.remove("output.txt")
            with open("output.txt", "w") as f:
                f.write("")
            self.bbb_launched = None
            
        except:
            logger.warning("Fail to kill ./BBB.")
            pass
    
    def custom_emergency_stop(self):
        self.set_steering(0)
        self.set_throttle(1)
        time.sleep(1)
        self.close_bbb_drive()
        
    def read_output_file(self):
        output = tail("-n", "10", "output.txt")
        logger.info('\nThe Last 10 Lines from BBB output file is: ')
        logger.info(output)
        
    def init_trigger_maps(self):
        #init set of mapping from buttons to function calls
            
        self.button_down_trigger_map = {
            'a_button' : self.toggle_mode,
            'b_button' : self.toggle_manual_recording,
            'x_button' : self.erase_last_N_records,
            'y_button' : self.custom_emergency_stop,
            'right_shoulder' : self.increase_max_throttle,
            'left_shoulder' : self.decrease_max_throttle,
            'M_button' : self.toggle_constant_throttle,
            'Xbox_button' : self.launch_bbb_drive,
            'V_button': self.read_output_file,
        }


        self.axis_trigger_map = {
            'left_stick_horz' : self.set_steering,
            'right_stick_vert': self.set_throttle,
            'right_trigger': self.magnitude(reversed = True),
            'left_trigger': self.magnitude(),
        }



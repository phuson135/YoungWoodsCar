from EthernetAPI.client import Client
from EthernetAPI.message_types import RC_ORDER
import donkeycar as dk
class Ethernet(object):
    """
    Motor controlled with an 'mini' L298N hbridge using 2 PwmPins,
    one for forward pwm and for reverse pwm.
    Chosen with configuration DRIVETRAIN_TYPE=DC_TWO_WHEEL
    See pins.py for pin provider implementations.

    See https://www.instructables.com/Tutorial-for-Dual-Channel-DC-Motor-Driver-Board-PW/
    for how an L298N mini-hbridge modules is wired.
    This driver can also be used for an L9110S/HG7881 motor driver.  See
    https://electropeak.com/learn/interfacing-l9110s-dual-channel-h-bridge-motor-driver-module-with-arduino/
    for how an L9110S motor driver module is wired.
    """

    def __init__(self, left_max, right_max, throttle_max, throttle_stop):
        self.client = Client()
        self.client.connect("192.168.137.1", 60006)
        self.left_max = left_max
        self.right_max = right_max
        self.throttle_max = throttle_max
        self.throttle_stop = throttle_stop
        self.client.send_message(RC_ORDER, "0|7.5")

    def run(self, throttle, steering) -> None:
        """
        Update the speed of the motor
        :param throttle:float throttle value in range -1 to 1,
                        where 1 is full forward and -1 is full backwards.
        """
        if (throttle >=0):
            throttle = self.map_range_float(throttle, 0, 1, self.throttle_stop, self.throttle_max)
        else:
            throttle = 0
            
        steering = self.map_range_float(steering, -1, 1, self.left_max, self.right_max)
        
        message = f"{throttle}|{steering}"
        self.client.send_message(RC_ORDER, message)

    def shutdown(self):
        self.client.send_message(RC_ORDER, "0|7.5")
        self.client.disconnect()
    
    def map_range_float(x, X_min, X_max, Y_min, Y_max):
        '''
        Same as map_range but supports floats return, rounded to 2 decimal places
        '''
        X_range = X_max - X_min
        Y_range = Y_max - Y_min
        XY_ratio = X_range/Y_range

        y = ((x-X_min) / XY_ratio + Y_min)

        # print("y= {}".format(y))
        return round(y,2)
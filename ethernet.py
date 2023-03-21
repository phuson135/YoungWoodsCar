from EthernetAPI.client import Client
from EthernetAPI.message_types import RC_ORDER
import donkeycar as dk
import logging
logger = logging.getLogger(__name__)
COUNTER = 3
class Ethernet(object):


    def __init__(self, left_max, right_max, throttle_max, throttle_stop):
        self.client = Client()
        self.connected = self.client.connect("192.168.137.1", 60006)
        self.left_max = left_max
        self.right_max = right_max
        self.throttle_max = throttle_max
        self.throttle_stop = throttle_stop
        self.throttle_old = None
        self.steering_old = None
        self.counter = 0
   #     self.client.send_message(RC_ORDER, "0|128")

    def run(self, throttle, steering) -> None:
        """
        Update the speed of the motor
        :param throttle:float throttle value in range -1 to 1,
                        where 1 is full forward and -1 is full backwards.
        """
        
        throttle = self.map_range_float(throttle, -.5, .5, self.throttle_stop, self.throttle_max)
        steering = self.map_range_float(steering, -1, 1, self.left_max, self.right_max)
        message = f"{throttle}|{steering}"
        # print(f"{steering}|{throttle}")
        if self.connected:
            try:
                self.client.send_message(RC_ORDER, message)
            except:
                logger.info('ERROR: FAIL TO SEND MESSAGE.')
                self.client.disconnect()
                self.client = Client()
                self.connected = self.client.connect("192.168.137.1", 60006)
        else:
            global COUNTER
            if self.counter == COUNTER:
                self.connected = self.client.connect("192.168.137.1", 60006)
                self.counter = 0
            else:
                self.counter +=1
            


    def shutdown(self):
        self.client.send_message(RC_ORDER, "0|128")
        self.client.disconnect()
    
    def map_range_float(self, x, X_min, X_max, Y_min, Y_max):
        '''
        Same as map_range but supports floats return, rounded to 2 decimal places
        '''
        X_range = X_max - X_min
        Y_range = Y_max - Y_min
        XY_ratio = X_range/Y_range

        y = ((x-X_min) / XY_ratio + Y_min)

        # print("y= {}".format(y))
        return round(y,2)
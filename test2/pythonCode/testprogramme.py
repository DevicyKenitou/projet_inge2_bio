import RPi.GPIO as GPIO
from RpiMotorLib import RpiMotorLib
import time

################################
# RPi and Motor Pre-allocations
################################
#
#define GPIO pins
direction= 20 # Direction (DIR) GPIO Pin
step = 21# Step GPIO Pin
EN_pin = 24 # enable pin (LOW to enable)


# Declare a instance of class pass GPIO pins numbers and the motor type
moteur1 = RpiMotorLib.A4988Nema(direction, step, (21,21,21), "DRV8825")
GPIO.setup(EN_pin,GPIO.OUT) # set enable pin as output




###########################
# Actual motor control
###########################
#
GPIO.output(EN_pin,GPIO.LOW) # pull enable to low to enable motor
moteur1.motor_go(True, # True=Clockwise, False=Counter-Clockwise
                     "Full" , # Step type (Full,Half,1/4,1/8,1/16,1/32)
                     5000, # number of steps
                     .010, # step delay [sec]                                        
                     False, # True = print verbose output 
                     .05) # initial delay [sec]

GPIO.cleanup() # clear GPIO allocations after run                                              ''''''''''''''''''''''''''''''''''''''fg
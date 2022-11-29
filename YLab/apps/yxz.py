import time
import board
import busio
from sensory import *

yxz = Yxz_3D(sample_interval = 0.001)
sen = Sensor_analog()

sensory = yxz #Sensory([yxz, sen])
sensory.connect()

while True:
    if sensory.sample():
        sensory.print()
    

import time
from pynput import keyboard
import sys


class TrafficLight:
    color = 'Черный'

    def running(self):
        while True:
            print("Trafficlight is red")
            time.sleep(10)
            print("Trafficlight is yellow")
            time.sleep(2)
            print("Trafficlight is green")
            time.sleep(10)
            print("Trafficlight is yellow")
            time.sleep(2)


trafficlight = TrafficLight()
trafficlight.running()

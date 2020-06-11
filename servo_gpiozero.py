from gpiozero import Servo
from time import sleep

servo = Servo(16)

while True:
    servo.min()
    print ("0 derajat")
    sleep(2)
    servo.mid()
    print ("90 derajat")
    sleep(2)
    servo.max()
    print ("180 derajat")
    sleep(2)

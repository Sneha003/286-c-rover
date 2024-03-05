from controller import Robot
from controller import Keyboard

robot = Robot()
keyboard = Keyboard()


wheel1_left=robot.getDevice("wheel1_left")
wheel1_left.setPosition(float('inf'))
wheel1_left.setVelocity(0.0)

wheel1_right=robot.getDevice("wheel1_right")
wheel1_right.setPosition(float('inf'))
wheel1_right.setVelocity(0.0)

wheel2_left=robot.getDevice("wheel2_left")
wheel2_left.setPosition(float('inf'))
wheel2_left.setVelocity(0.0)

wheel2_right=robot.getDevice("wheel2_right")
wheel2_right.setPosition(float('inf'))
wheel2_right.setVelocity(0.0)


timestep=64

speed=4
 
keyboard.enable(timestep)

while (robot.step(timestep) !=-1):
   
    key_pressed= keyboard.getKey()
    print(key_pressed)
    
    if(key_pressed== 83):
        wheel1_left.setVelocity(speed)
        wheel1_right.setVelocity(speed)
        wheel2_left.setVelocity(speed)
        wheel2_right.setVelocity(speed)
        
    if(key_pressed== 87):
        wheel1_left.setVelocity(-speed)
        wheel1_right.setVelocity(-speed)
        wheel2_left.setVelocity(-speed)
        wheel2_right.setVelocity(-speed)
          
    if(key_pressed== 65):
        wheel1_left.setVelocity(-speed)
        wheel1_right.setVelocity(speed)
        wheel2_left.setVelocity(-speed)
        wheel2_right.setVelocity(speed)
        
    if(key_pressed== 68):
        wheel1_left.setVelocity(speed)
        wheel1_right.setVelocity(-speed)
        wheel2_left.setVelocity(speed)
        wheel2_right.setVelocity(-speed)
        
    if(key_pressed== -1):
        wheel1_left.setVelocity(0)
        wheel1_right.setVelocity(0)
        wheel2_left.setVelocity(0)
        wheel2_right.setVelocity(0)
    

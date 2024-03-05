"""my_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot
from controller import Keyboard
from controller import DistanceSensor
from controller import Camera

speed=4

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = 64

keyboard=Keyboard()
keyboard.enable(timestep)

wheel1_left=robot.getDevice("wheel1_left")
wheel1_left.setPosition(float("inf"))
wheel1_left.setVelocity(0.0)

wheel2_left=robot.getDevice("wheel2_left")
wheel2_left.setPosition(float("inf"))
wheel2_left.setVelocity(0.0)

wheel1_right=robot.getDevice("wheel1_right")
wheel1_right.setPosition(float("inf"))
wheel1_right.setVelocity(0.0)

wheel2_right=robot.getDevice("wheel2_right")
wheel2_right.setPosition(float("inf"))
wheel2_right.setVelocity(0.0)

ds1=robot.getDevice("ds1")
ds2=robot.getDevice("ds2")
ds1.enable(timestep)
ds2.enable(timestep)

cam_slider=robot.getDevice("cam_slider")
cam=robot.getDevice("camera")
cam.enable(timestep)

speed=4
prev_key=0
key_pressed=-1
autoMode=False

num_of_turns=0

position=0
cam_slider_position=0
img_num=1


# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    prev_key=key_pressed
    key_pressed=keyboard.getKey()
    # print("which key is clicked:",key_pressed)
    
    if(prev_key==-1 and key_pressed==79):
           autoMode=not autoMode
    print(autoMode)
    
    if(key_pressed == 315):
        cam_slider_position=cam_slider_position+0.01
        cam_slider.setPosition(cam_slider_position)
        
    if(key_pressed==317):
        cam_slider_position=cam_slider_position-0.01
        cam_slider.setPosition(cam_slider_position)
        
    if(prev_key==-1 and key_pressed==80):
        cam.getImage()
        image_name="image"+str(img_num)+".png"
        cam.saveImage(image_name,50)
        img_num=img_num+1
        
    
    if(autoMode==True):
        ds1_value=ds1.getValue()
        ds2_value=ds2.getValue()
            
        if(ds1_value<1000 or ds2_value<1000):
             num_of_turns=5
    
    
        if(num_of_turns>0):
            num_of_turns=num_of_turns-1
            wheel1_left.setVelocity(-speed)
            wheel1_right.setVelocity(speed)
            wheel2_left.setVelocity(-speed)
            wheel2_right.setVelocity(-speed)
        else:
            wheel1_left.setVelocity(speed)
            wheel1_right.setVelocity(speed)
            wheel2_right.setVelocity(speed)
            wheel2_right.setVelocity(speed)
            
        
        
    if(autoMode==False):
        
    
    #a
        if(key_pressed==65):
            wheel1_left.setVelocity(-speed)
            wheel1_right.setVelocity(speed)
            wheel2_left.setVelocity(-speed)
            wheel2_right.setVelocity(speed)
            #d
        if(key_pressed==68):
            wheel1_left.setVelocity(speed)
            wheel1_right.setVelocity(-speed)
            wheel2_left.setVelocity(speed)
            wheel2_right.setVelocity(-speed)
            
            #w
        if(key_pressed==87):
            wheel1_left.setVelocity(speed)
            wheel1_right.setVelocity(speed)
            wheel2_left.setVelocity(speed)
            wheel2_right.setVelocity(speed)
            
            #s
        if(key_pressed==83):
            wheel1_left.setVelocity(-speed)
            wheel1_right.setVelocity(-speed)
            wheel2_left.setVelocity(-speed)
            wheel2_right.setVelocity(-speed)
            
            #w
        if(key_pressed==-1):
            wheel1_left.setVelocity(0.0)
            wheel1_right.setVelocity(0.0)
            wheel2_left.setVelocity(0.0)
            wheel2_right.setVelocity(0.0)

    

# Enter here exit cleanup code.a




import utils
import math
import struct
from typing import Tuple
from controller import Robot


def run_robot(robot):

    time_step = 32
    max_speed = 12.4
    
    #motors
    left_motor = robot.getDevice('right_motor')
    right_motor = robot.getDevice('left_motor')
    left_motor.setPosition(float('inf'))
    right_motor.setPosition(float('inf'))
    left_motor.setVelocity(0.0)
    right_motor.setVelocity(0.0)
    
    #enable ir sensor
    left_ir = robot.getDevice('ir0')
    left_ir.enable(time_step)
    
    #cam = robot.getDevice('camera')
    #cam.enable(time_step)
    
    right_ir = robot.getDevice('ir1')
    right_ir.enable(time_step)
    
    ro_ir = robot.getDevice('ir2')
    ro_ir.enable(time_step)
    
    ro_ir3 = robot.getDevice('ir3')
    ro_ir3.enable(time_step)
    
    ro_ir4 = robot.getDevice('ir4')
    ro_ir4.enable(time_step)
    
    #ro_ir5 = robot.getDevice('distance sensor')
    #ro_ir5.enable(time_step)
    
    # Step simulation
    while robot.step(time_step) != -1 :
        
        #read ir sensors
        left_ir_value = left_ir.getValue()
        right_ir_value = right_ir.getValue()
        ro_ir_value = ro_ir.getValue()
        ro_ir3_value = ro_ir3.getValue()
        ro_ir4_value = ro_ir4.getValue()
        #ro_ir5_value = ro_ir5.getValue()
        #cam_value = cam.getValue()
        print("one {} two {} three {} four {} five {}".format(ro_ir3_value,left_ir_value, ro_ir_value,right_ir_value,ro_ir4_value  ))
        #print(cam_value )
        left_speed = max_speed * 0.75
        right_speed = max_speed *0.75
        if (200< ro_ir_value < 300):
            left_speed = max_speed 
            right_speed = max_speed 
        if (left_ir_value > right_ir_value) and (200 < left_ir_value < 300):
            #print("Go left")
            left_speed = max_speed *0.75
            right_speed =- max_speed *0.75
            #print("right speed: {} left speed: {}".format(right_speed, left_speed))
        if (right_ir_value > left_ir_value) and (200 < right_ir_value < 300):
            #print("Go right MAN")
            right_speed = max_speed *0.75
            left_speed =  -max_speed *0.75
            #print("right speed: {} left speed: {}".format(right_speed, left_speed))
        if (200 < ro_ir3_value < 300):
            #print("Go right MAN")
            right_speed = max_speed *0.95
            left_speed =  max_speed *0.75
        if (200 < ro_ir4_value < 300):
            #print("Go right MAN")
            right_speed = max_speed *0.75
            left_speed =  max_speed *0.95

       
        
        left_motor.setVelocity(1 ) 
        right_motor.setVelocity(1)    
       
    
if __name__ == "__main__":
    my_robot = Robot()
    run_robot(my_robot)
    

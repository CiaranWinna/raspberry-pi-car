import RPi.GPIO as g
import time as t

g.setwarnings(False)

# trig is the pin on the sensor which will emit a very fast pulse
trig = 7
# echo is the pin which will recieve the pulse from the trig 
echo_right = 11
echo_left = 13

right_forward = 16
right_backward = 18

left_forward = 22
left_backward = 36

def init():
    g.setmode(g.BOARD)
    
    #sensors
    g.setup(trig, g.OUT)
    g.setup(echo_right, g.IN)
    g.setup(echo_left, g.IN)
    
    #motors
    g.setup(right_forward, g.OUT)
    g.setup(right_backward, g.OUT)
    g.setup(left_forward, g.OUT)
    g.setup(left_backward, g.OUT)

def distance(trig, echo):
    dis = 0
    start = 0
    end = 0
    g.output(trig, False)
    t.sleep(0.0001)
    g.output(trig, True)
    t.sleep(0.00001)
    g.output(trig, False)
    
    while g.input(echo) == 0:
        start = t.time()
        
    while g.input(echo) == 1:
        end = t.time()
        
    duration = end - start
    dis = duration * 17150
    dis = round(dis,2)
    return dis

def forward(slp):
    g.output(right_forward, True)
    g.output(left_forward, True)
    t.sleep(slp)
    g.output(right_forward, False)
    g.output(left_forward, False)
    g.cleanup()

def backward(slp):
    g.output(right_backward, True)
    g.output(left_backward, True)
    t.sleep(slp)
    g.output(right_backward, False)
    g.output(left_backward, False)
    g.cleanup()
    
    
def turn_left(slp):
    g.output(right_forward, True)
    g.output(left_forward, True)
    t.sleep(slp)
    g.output(left_forward, False)
    t.sleep(slp*3)
    g.output(right_forward, False)
    g.cleanup()
    
def turn_right(slp):
    g.output(right_forward, True)
    g.output(left_forward, True)
    t.sleep(slp)
    g.output(right_forward, False)
    t.sleep(slp*3)
    g.output(left_forward, False)
    g.cleanup()

if __name__=="__main__":
    # so the function is being called, and the time between outputs is 0.01 seconds so it is very 
    # fast and quickly showing on the screen. If the distance is less than 5, then the program 
    # will print out "Hi" to show that. s
    sleep_time = 0.1
    sleep_time2 = 0.01
    
    running = True
    
    while running:
        init()
        
        distance_right = distance(trig, echo_right)
        distance_left = distance(trig, echo_left)
        
        if (distance_right < 50 and distance_left > 50):
            turn_left(0.01)
        
        elif (distance_left < 50 and distance_right > 50):
            turn_right(0.01)
            
        elif (distance_right < 20 and distance_left < 20):
            t.sleep(0.5)
        else:
            forward(sleep_time)
            
        
        '''
        turn_left(0.01)
        if (distance_right < 10):
            running = False
        '''
        '''
        if (distance_right >= 50):
            forward(sleep_time)
            print("RIGHT OVER 50")
        elif (distance_right >= 20 and distance_right < 50):
            forward(sleep_time2)
            print("RIGHT %s" % distance_right)
        elif (distance_right >= 10 and distance_right < 20):
            backward(0.005)
            print("RIGHT %s" % distance_right)
        else:
            t.sleep(0.5)
            '''
        '''
        t.sleep(0.2)

        
        
        if (distance_left > 50):
            print("LEFT OVER 50")
        else:
            print("LEFT %s" % distance_left)
            
            
        #t.sleep(0.2)
'''

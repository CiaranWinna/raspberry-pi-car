import RPi.GPIO as g
import time as t
g.setmode(g.BOARD)
g.setwarnings(False)

# trig is the pin on the sensor which will emit a very fast pulse
trig = 7
# echo is the pin which will recieve the pulse from the trig 

echo_right = 11
echo_left = 13

g.setup(trig, g.OUT)
g.setup(echo_right, g.IN)
g.setup(echo_left, g.IN)

def distance(trig, echo):
    dis = 0
    start = 0
    end = 0
    g.output(trig, False)
    t.sleep(0.01)
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


if __name__=="__main__":
    # so the function is being called, and the time between outputs is 0.01 seconds so it is very 
    # fast and quickly showing on the screen. If the distance is less than 5, then the program 
    # will print out "Hi" to show that. s
    
    while True:
        distance_right = distance(trig, echo_right)
        
        if (distance_right > 50):
            print("RIGHT OVER 50")
        else:
            print("RIGHT %s" % distance_right)
        
        t.sleep(0.2)

        distance_left = distance(trig, echo_left)
        
        if (distance_left > 50):
            print("LEFT OVER 50")
        else:
            print("LEFT %s" % distance_left)
            
            
        t.sleep(0.5)

from hcsr04 import HCSR04
from time import sleep,ticks_ms

#Initiate Sensor Objects
sensor = HCSR04(trigger_pin=5, echo_pin=18, echo_timeout_us=10000)
sensor2 = HCSR04(trigger_pin=15, echo_pin=19, echo_timeout_us=10000)

from supportlibs import ref_distance

sample_rate=5

distance=ref_distance(sample_rate,sensor,sensor2)
sensor1_entrance_distance=distance[0]
sensor2_entrance_distance=distance[1]
print('Sensor 1 Average Distance: ',sensor1_entrance_distance)
print('Sensor 2 Average Distance: ',sensor2_entrance_distance)
#Number of people in a room at a given instance
occupants=0        
        
while True:
    sensors={}
    
    
    while True:
        distance=sensor.distance_cm()
        
        distance2=sensor2.distance_cm()
        #By measuring the time, we can calculate which sensor was triggered first
        #If the difference between sensor 1 and 2 is negative, then the movement is inwards
        #The opposite is true
        if distance<0.5*sensor1_entrance_distance:
            sensors['sensor1']=ticks_ms()
        if distance2<0.5*sensor2_entrance_distance:
            sensors['sensor2']=ticks_ms()
            
        else:
            continue
        #condition to check whether a person has crossed over
        #Validates whether 2 sesnsors have been activated to make an inward or outward transition.
        #Criteria is testing whether 2 keys have been populated in the sensors dictionary,
        #If not, the inner loop continues, else, Break out of the loop.
        
        if 'sensor1' in sensors and 'sensor2' in sensors:
            break
        else: continue
    
    #Calculating if a person has entered or left
    direction_detect= sensors['sensor1']-sensors['sensor2']
    print('Which Direction: ',direction_detect)
    if direction_detect < 0:
        occupants+=1
    elif direction_detect > 0:
        occupants-=1
    else: pass
    
    print('Occupants: ',occupants)
    continue
        
    
    


        
        
print('Sensor 1 to REF point: ',sensor1_entrance_distance)
print('Sensor 2 to REF point: ',sensor2_entrance_distance)


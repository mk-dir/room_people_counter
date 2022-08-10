def ref_distance(sample_size,sensor,sensor2):
    #Function that returns the average width of the door
    #by measuring the number taking n number of readings.
    #where n = sample_size
    counter=0
    sensor1_entrance_distance=0
    sensor2_entrance_distance=0

    while sample_size>counter:
        distance=sensor.distance_cm()
        distance2=sensor2.distance_cm()
        
        sensor1_entrance_distance+=distance
        sensor2_entrance_distance+=distance2
        counter+=1
        
    sensor1_entrance_distance= sensor1_entrance_distance/sample_size
    sensor2_entrance_distance= sensor2_entrance_distance/sample_size
    
    return sensor1_entrance_distance,sensor2_entrance_distance


        
        
        
        
        
        
        

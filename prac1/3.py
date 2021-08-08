import math

distance = float(input()) #6
speed = float(input()) #50
time_after_2km = (distance-2)/speed #0.12 = 2/50 + (6-2)/50 
                      #       0.04 + 0.08  
if distance <= 2:
    print(12000)
else:
    print(round(12000 + 3500*math.ceil(distance-2) + \
        350*time_after_2km))
    # 12000 + 3500*4
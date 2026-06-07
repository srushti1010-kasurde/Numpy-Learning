import numpy as np
taxi = np.genfromtxt("nyc_taxis.csv" , delimiter = ",", skip_header = True)
#print(taxi)
#To find mean speed of all rides
speed = taxi[:,7] / (taxi[:,8]/3600)#speed = distance(miles)/time(seconds)
mean_speed = speed.mean()
print(mean_speed)
# To find number of rides taken in february = 2
feb_rides = taxi [taxi[:,1]==2, 1]
#print(feb_rides.shape)
print(feb_rides.shape[0])
#To find number of rides where tip is more than $50
high_tip = taxi[taxi[:,-3]>50,-3]
print(high_tip.shape[0])
#To find number of rides where drop off was JFK airport =4 
JFK = taxi[taxi[:,6]==4,6]
print(JFK.shape[0])

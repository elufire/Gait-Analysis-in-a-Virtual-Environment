import matplotlib.pyplot as tplot
import math

#This version uses by frame or refresh of the update loop in unity as it's time stamp and is arguably much more reliable
filename = raw_input("Please enter filename: ")
divergence = []
distance = []
start_pos = [] 
#filename = E1.get()
data = open(filename, "r")
data = data.read()
data = data.split("\n")


for index in range(0, len(data)):
        if len(data[index]) == 0:
            del(data[index])
            continue
        data[index]=data[index].split(",")
        data[index][1]=float(data[index][1])
        data[index][2]=float(data[index][2])
        data[index][3]=float(data[index][3])
        data[index][4]=float(data[index][4])
        data[index][5]=float(data[index][5])
        data[index][6]=float(data[index][6])

frame = range(1, len(data)) 
frame2 = range(0, len(data))
#start_pos = data[0]
#start_pos = [float(i) for i in start_pos]
time_stamp, ex, ya, zed, rot, pit, yaw = zip(*data)

time_stamp=list(time_stamp)
for i in range(0, len(time_stamp)):
    #re.split(' |: ', time_stamp[i])
    time_stamp[i]=time_stamp[i].split()

a, tim, c = zip(*time_stamp)
del a, c
tim = list(tim)
for i in range(0, len(tim)):
    tim[i]=tim[i].split(':')
    tim[i][2]=float(tim[i][2])

n, m, seconds = zip(*tim)
del n, m
#seconds=set(seconds)
seconds=list(seconds)
#a,b,c,retime,d = zip(*time_stamp)
#del a, b, c, d
#print(seconds)
'''
ex = [float(i) for i in ex]
ya = [float(i) for i in ya]
zed = [float(i) for i in zed]
'''
start_pos = [ex[6], ya[6], zed[6]]
print(start_pos)

#the following block analyzes and generates possible gait intervals and further information on gait.
#I found it to be unreliable but it can be used
cont_var = 1
count =5
gait_inter = []
gait_dist =[]
for i in range(1, len(data)):
    if ya[i] > ya[i-1] and cont_var == -1 and count >=5:
        gait_inter.append(i)
        cont_var = 1
        count = 0
        
    elif ya[i] < ya[i-1] and cont_var == 1 and count >=5:
        #gait_inter.append(i)
        cont_var = -1
    count=count+1
        
num_gaits = range(1,(len(gait_inter)))
print("Gait intervals ", gait_inter)
        
for i in range(1, len(gait_inter)):
        gait_dist.append(math.sqrt(math.pow(ex[gait_inter[i]]-ex[gait_inter[i-1]],2)+math.pow(ya[gait_inter[i]]-ya[gait_inter[i-1]],2)+math.pow(zed[gait_inter[i]]-zed[gait_inter[i-1]],2)))


for i in range(1, len(data)): 
    if math.sqrt(math.pow(ex[i]-ex[i-1],2)+math.pow(ya[i]-ya[i-1],2)+math.pow(zed[i]-zed[i-1],2)) != 0:
        divergence.append(math.log(math.sqrt(math.pow(ex[i]-ex[i-1],2)+math.pow(ya[i]-ya[i-1],2)+math.pow(zed[i]-zed[i-1],2))))
    else:
        divergence.append(0)
        
for i in range(1, len(data)):
    distance.append(math.sqrt(math.pow(start_pos[0]-ex[i],2)+math.pow(start_pos[1]-ya[i],2)+math.pow(start_pos[2]-zed[i],2)))
    #distance.append(ex[i])
'''
max_Val=max(distance)
print(max_Val)
num_steps=int(max_Val/1.31)
print(num_steps)
steps=range(0,num_steps+1)
step_dist=[]
interval=int(len(frame)/num_steps)
index=0
p=0
while(index<=num_steps+1):
    step_dist.append(distance[p])
    p+=interval
    index=index+1
'''
'''
for i in range(1, len(data)): 
    if math.sqrt(math.pow(ex[i]-ex[i-1],2)+math.pow(ya[i]-ya[i-1],2)+math.pow(zed[i]-zed[i-1],2)) != 0:
        divergence.append(math.log(math.sqrt(math.pow(ex[i]-ex[i-1],2)+math.pow(ya[i]-ya[i-1],2)+math.pow(zed[i]-zed[i-1],2))))
    else:
        divergence.append(0)    
    '''
col=raw_input("What color would you like the graphs to be? ")
tplot.figure(1)
tplot.title("Distance")
tplot.xlabel("time")
tplot.ylabel("distance")
#tplot.plot(frame, distance, color='blue')
tplot.plot(frame, distance, color=col)
#this commented block would display a distance with steps and distance with a gait charts' that turned out to be
#unreliable in my inspection.
'''
tplot.figure(3)
tplot.title("Distance with steps")
tplot.xlabel("Steps")
tplot.ylabel("distance")
#tplot.plot(frame, distance, color='blue')
tplot.plot(steps, step_dist, color=col)

'''
'''
#del seconds[0]
tplot.figure(4)
tplot.title("Distance between Gaits")
tplot.xlabel("Gaits")
tplot.ylabel("Distance")
col=raw_input("What color would you like the distance graph to be? ")
tplot.scatter(num_gaits, gait_dist, color=col)
#tplot.scatter(num_gaits, gait_dist, color='orange')
'''
tplot.figure(2)
tplot.title("Divergence")
tplot.xlabel("time")
tplot.ylabel("Mean Divergence")
#col=raw_input("What color would you like the divergence graph to be? ")
tplot.scatter(frame, divergence, color=col)
#tplot.scatter(frame, divergence, color='orange')

#tplot.scatter(ex, ya, color='blue')
tplot.show()
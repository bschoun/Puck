import csv
import matplotlib.pyplot as plt 

xsum = 0
ysum = 0
zsum = 0
x = [] 
y = []
z = []
  
with open('data_analysis/accel.csv') as csvfile: 
    plots = csv.reader(csvfile, delimiter = ',') 
      
    for row in plots: 
        #x.append(float(row[0])) 
        #y.append(float(row[1]))
        #z.append(float(row[2])) 
        xsum += float(row[0])
        ysum += float(row[1])
        zsum += float(row[2])
        #x.append(float(row[0])) 
        #y.append(float(row[1]))
        #z.append(float(row[2]))
        x.append(xsum)
        y.append(ysum)
        z.append(zsum)
  
plt.plot(x, color='#0000ff')#, y, color = 'g', width = 0.72, label = "Age") 
plt.plot(y, color='#ff0000')
plt.plot(z, color='#00ff00')
#plt.plot(y)
#plt.xlabel('Names') 
#plt.ylabel('Ages') 
#plt.title('Ages of different persons') 
plt.legend() 
plt.show() 
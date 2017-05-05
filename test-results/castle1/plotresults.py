import numpy as np
import matplotlib.pyplot as plt
import csv
import re

#http://www.scipy-lectures.org/intro/matplotlib/auto_examples/plot_quiver_ex.html

loc_file = open("logs-vectors.csv", "rU") 
reader = csv.reader(loc_file)
list_1=[]
x = []
y = []
b = []
for i,row in enumerate(reader):
    #print row
    #print i
    if i%1 == 0:
        if len(row) > 0:
            that = row[2]
            print that
           # if len(row[2]) >= 33: #this is really bodged together, warning will not work with bearing between 0 and 9
           #     here = that[:-5]
           # else:
           #     here = that[:-4]
           # t = re.sub("[^0123456789\.]","",here)
            
           # print 'len', len(t)
           # n = t[6:]
           # m = n[:3]
           # print 'm',m
            x.append(float(row[0]))
            y.append(float(row[1]))
            b.append(int(that))

loc_file.close()


y_b = np.cos(np.radians(b))
x_b = np.sin(np.radians(b))


plt.quiver(y, x, x_b, y_b,width=0.001,scale=1 / 0.035) #http://matplotlib.org/examples/pylab_examples/quiver_demo.html


ways_t=[52.413830]
ways_l=[-4.090857]






plt.plot(ways_l,ways_t)
plt.scatter(ways_l,ways_t)

#loc_file2 = open('castle-simplescan1/water.csv', "r") 
#reader2 = csv.reader(loc_file2)
water_t=[52.4140165,52.4138921,52.4132672,52.4139052]
water_l=[-4.0911520,-4.0899235,-4.0906477,-4.0913129]
#for row in reader2:
#    water_t.append(float(row[0]))
#    water_l.append(float(row[1]))
#loc_file2.close()

plt.plot(water_l,water_t)
plt.scatter(water_l,water_t)
  

plt.plot(y,x,'r-')
plt.show()

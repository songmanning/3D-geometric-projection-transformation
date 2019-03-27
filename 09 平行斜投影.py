import numpy as np
import mpl_toolkits.mplot3d
import matplotlib.pyplot as plt
import math
x=[0,0,0,0,1,1,1,1]
y=[0,0,1,1,0,0,1,1]
z=[0,1,0,1,0,1,0,1]

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

ax=plt.subplot(111,projection='3d')
for i in range(len(x)):
        for j in range(len(x)):
            sum=i^j
            if (sum==1 or sum==2 or sum==4):
                ax.plot((x[i],x[j]),(y[i],y[j]),(z[i],z[j]),'red');

for i in range(len(x)):
    ax.text(x[i],y[i],z[i],i,color='blue')
ax.text(x[3],y[3],z[3],' 原始图形',color='black')
a=19.47
b=20.7
sina=math.sin(math.radians(a))
cosa=math.cos(math.radians(a))
sinb=math.sin(math.radians(b))
cosb=math.cos(math.radians(b))

x1=[0,0,0,0,0,0,0,0];
y1=[0,0,0,0,0,0,0,0];
z1=[0,0,0,0,0,0,0,0];
for i in range(len(x)):
    x1[i] = float(x[i])* cosb - float(y[i])*sinb ;
    y1[i] = 0;
    z1[i] = -float(x[i])*sinb*sina - float(y[i])*cosb*sina + float(z[i])*cosa;
for i in range(len(x)):
    for j in range(len(x)):
        sum=i^j
        if (sum==1 or sum==2 or sum==4):
            ax.plot((x1[i],x1[j]),(y1[i],y1[j]),(z1[i],z1[j]),color='green');

for i in range(len(x)):
    ax.text(x1[i],y1[i],z1[i],i,color='black')
ax.text(x1[3],y1[3],z1[3],' 变换图形',color='black')
plt.title('图9-2 正二测变换',fontsize='xx-large')



ax.set_zlabel('z')
ax.set_ylabel('y')
ax.set_xlabel('x')

plt.show()

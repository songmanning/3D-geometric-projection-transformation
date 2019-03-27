import numpy as np
import mpl_toolkits.mplot3d
import matplotlib.pyplot as plt
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
                ax.plot((x[i],x[j]),(y[i],y[j]),(z[i],z[j]),color='red');

for i in range(len(x)):
    ax.text(x[i],y[i],z[i],i,color='blue')
ax.text(x[3],y[3],z[3],' 原始图形',color='black')

x1=[0,0,0,0,0,0,0,0];
y1=[0,0,0,0,0,0,0,0];
z1=[0,0,0,0,0,0,0,0];
for i in range(len(x)):
    x1[i] = x[i];
    y1[i] = -1;
    z1[i] = z[i];
for i in range(len(x)):
    for j in range(len(x)):
        sum=i^j
        if (sum==1 or sum==2 or sum==4):
            ax.plot((x1[i],x1[j]),(y1[i],y1[j]),(z1[i],z1[j]),color='green');
ax.text(x1[0],y1[0],z1[0],'主视图',color='black')

x2=[0,0,0,0,0,0,0,0];
y2=[0,0,0,0,0,0,0,0];
z2=[0,0,0,0,0,0,0,0];
for i in range(len(x)):
    x2[i] = x[i];
    y2[i] = y[i];
    z2[i] = -1;
for i in range(len(x)):
    for j in range(len(x)):
        sum=i^j
        if (sum==1 or sum==2 or sum==4):
            ax.plot((x2[i],x2[j]),(y2[i],y2[j]),(z2[i],z2[j]),color='green');
ax.text(x2[0],y2[0],z2[0],'俯视图',color='black')


x3=[0,0,0,0,0,0,0,0];
y3=[0,0,0,0,0,0,0,0];
z3=[0,0,0,0,0,0,0,0];
for i in range(len(x)):
    x3[i] = -1;
    y3[i] = y[i];
    z3[i] = z[i];
for i in range(len(x)):
    for j in range(len(x)):
        sum=i^j
        if (sum==1 or sum==2 or sum==4):
            ax.plot((x3[i],x3[j]),(y3[i],y3[j]),(z3[i],z3[j]),color='green');
ax.text(x3[0],y3[0],z3[0],'侧视图',color='black')
plt.title('图8 平行投影-正投影变换',fontsize='xx-large')

ax.set_zlabel('z')
ax.set_ylabel('y')
ax.set_xlabel('x')

plt.show()

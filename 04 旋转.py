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
                ax.plot((x[i],x[j]),(y[i],y[j]),(z[i],z[j]),color='red');

for i in range(len(x)):
    ax.text(x[i],y[i],z[i],i,color='blue')
ax.text(x[3],y[3],z[3],' 原始图形',color='black')
s = int(input("绕z轴旋转度数："));

sina=math.sin(math.radians(s))
cosa=math.cos(math.radians(s))

for i in range(len(x)):
    x[i] = float(x[i]) * cosa - float(y[i]) * sina;
    y[i] = float(x[i]) * sina + float(y[i]) * cosa;

for i in range(len(x)):
    for j in range(len(x)):
        sum=i^j
        if (sum==1 or sum==2 or sum==4):
            ax.plot((x[i],x[j]),(y[i],y[j]),(z[i],z[j]),color='green');

for i in range(len(x)):
    ax.text(x[i],y[i],z[i],i,color='black')
ax.text(x[3],y[3],z[3],' 变换图形',color='black')
plt.title('图4 绕z轴旋转变换',fontsize='xx-large')


ax.set_zlabel('z')
ax.set_ylabel('y')
ax.set_xlabel('x')

plt.style.use('ggplot')
plt.show()

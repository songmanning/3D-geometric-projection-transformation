import matplotlib.pyplot as plt
import math
x=[0,0,0,0,1,1,1,1]
y=[0,0,1,1,0,0,1,1]
z=[0,1,0,1,0,1,0,1]

plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

ax=plt.subplot(111,projection='3d')
'''
for i in range(len(x)):
        for j in range(len(x)):
            sum=i^j
            if (sum==1 or sum==2 or sum==4):
                ax.plot((x[i],x[j]),(y[i],y[j]),(z[i],z[j]),color='red');

for i in range(len(x)):
    ax.text(x[i],y[i],z[i],i,color='blue')
ax.text(x[3],y[3],z[3],' 原始图形',color='black')
'''
l=-0.8;
m=-1.6;
n=-2;
d=-2.5;

for i in range(len(x)):
    x[i] = (x[i]+l) / ( (n+z[i])/d +1 ) ;
    y[i] = (y[i]+m) / ( (n+z[i])/d +1 );
    z[i] = 0;

for i in range(len(x)):
    ax.plot((x[i], 0), (y[i], 0), (z[i], 0), 'g:');
    for j in range(len(x)):
        sum=i^j
        if (sum==1 or sum==2 or sum==4):
            ax.plot((x[i],x[j]),(y[i],y[j]),(z[i],z[j]),'g-');
ax.text(0,0,0,'  一点透视',color='black')

for i in range(len(x)):
    ax.text(x[i],y[i],z[i],i,color='black')

plt.title('图10 一点透视投影变换',fontsize='xx-large')



ax.set_zlabel('z')
ax.set_ylabel('y')
ax.set_xlabel('x')

plt.show()

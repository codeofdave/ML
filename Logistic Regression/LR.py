import matplotlib.pyplot as plt
import numpy as np
import xlrd

def readdata():
    with xlrd.open_workbook('data.xlsx') as workbook :
        table = workbook.sheet_by_name('Sheet1')
        x1 = table.col_values(0)[1:]
        x2 = table.col_values(1)[1:]
        label = table.col_values(2)[1:]
        return x1,x2,label
x1,x2,label = readdata()

# X:(14,3) W:(3,1) Y,LABEL:(14,1),d(COST)/d(W):(3,1)

# Z = X*W
# Y = 1 / (e^(-Z) + 1)
# COST =  (LABEL-1)*log(1-Y) - LABEL*log(Y)
# d(COST) / d(W) = X.T * (Y - LABEL)
X = np.array([[1]*len(x1),x1,x2]).T
W = np.random.rand(3,1)
LABEL = np.array([label]).T

tmp= []
for epoch in range(10000):
    Z = np.dot(X,W)
    Y = 1 / (np.exp(-1*Z)+1)
    W -= 0.001*np.dot(X.T,(Y-LABEL))
    if (epoch+1) % 100 == 0:
        tmp.append([W.copy(),epoch])
print(W)

#w0 + w1*x1 + w2*x2 = 0  >>> x2 = -w1/w2 * x1 - w0/w2
for Wi in tmp:
    plt.clf()
    w0 = Wi[0][0,0]
    w1 = Wi[0][1,0]
    w2 = Wi[0][2,0]
    print(w0,w1,w2)
    x1 = np.arange(0,7,1)
    x2 = -1*x1*w1/w2 - w0/w2
    plt.plot(x1,x2,c='r',label='decision boundary')

    plt.scatter(np.mat(X)[:,1][np.mat(LABEL)==0].A,np.mat(X)[:,2][np.mat(LABEL)==0].A,s=50,label='label 0')
    plt.scatter(np.mat(X)[:,1][np.mat(LABEL)==1].A,np.mat(X)[:,2][np.mat(LABEL)==1].A,s=50,label='label 1',marker='^')
    plt.xlabel('x1',size=20)
    plt.ylabel('x2',size=20)
    plt.legend()
    plt.grid()
    plt.title('iter:%s' % str(Wi[1]))
    plt.pause(0.01)

plt.show()





#coding:utf-8
# K-means

import numpy as np
import sys
import matplotlib.pyplot as plt

argvs = sys.argv

if __name__ == "__main__":
    data = np.genfromtxt(argvs[1])
    print(data)

    #plt.subplot(2, 1, 1)
    plt.plot(data)

    #plt.subplot(2, 1, 2)
    #plt.plot(data[:,1])

    plt.show()  
        
    filename = argvs[1] + ".png"
    plt.savefig(filename)


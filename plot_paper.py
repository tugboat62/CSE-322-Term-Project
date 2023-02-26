import numpy as np
from scipy.interpolate import make_interp_spline
import matplotlib.pyplot as plt
import sys

file_name = 'paper_data.txt'
file_name2 = 'paper_data_prev.txt'

file = open(file_name, 'r')
file2 = open(file_name2, 'r')
packets_per_sec = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

rate_fairness = []
rate_prev_fairness = []
rate_throughput = []
rate_prev_throughput = []


while True:
    line = file.readline()
    line2 = file2.readline()
    if not line and not line2 :
        break
    tokens = line.split()
    tokens2 = line2.split()
    mesType = tokens[0]
    mesType2 = tokens2[0]
    size = int(tokens[1])
    size2 = int(tokens2[1])
    fairness = float(tokens[8])
    fairness2 = float(tokens2[8])
    throughput = float(tokens[2])
    throughput2 = float(tokens2[2])

    rate_fairness.append(fairness)
    rate_prev_fairness.append(fairness2)
    rate_throughput.append(throughput)
    rate_prev_throughput.append(throughput2)
    
   
file.close()

rateList = [rate_throughput, rate_fairness]
rate_prevList = [rate_prev_throughput, rate_prev_fairness]

for i in range(len(rateList)):
    x = np.array(packets_per_sec)
    y = np.array(rateList[i])
    z = np.array(rate_prevList[i])
    
    plt.plot(x, y, color='r', label='new', linestyle='dashed')
    plt.plot(x, z, color='g', label='old', linestyle='dashed')
    plt.xlabel('packets per second')
    if i == 0:
        plt.ylabel('Throughput')
        plt.title("packets per second vs Throughput")
    else:
        plt.ylabel('Fairness Index')
        plt.title("packets per second vs Fairness Index")
    
    plt.legend(loc='best')
    plt.show()
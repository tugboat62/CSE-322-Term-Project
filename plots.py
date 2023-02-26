import numpy as np
from scipy.interpolate import make_interp_spline
import matplotlib.pyplot as plt
import sys

file_name = 'data.txt'
file_name2 = 'data_prev.txt'
file_name3 = 'data_reno.txt'
if len(sys.argv) == 4 :
    file_name = sys.argv[1]
    file_name2 = sys.argv[2]
    file_name3 = sys.argv[3]

file = open(file_name, 'r')
file2 = open(file_name2, 'r')
file3 = open(file_name3, 'r')
nodes = [20, 40, 60, 80, 100]
flows = [10, 20, 30, 40, 50]
packets_per_sec = [100, 200, 300, 400, 500]
node_speed = [5, 10, 15, 20, 25]
tx_range = [1, 2, 3, 4, 5]

nodesTp = []
nodesAd = []
nodesDr = []
nodesDrat = []
nodesEnergy = []
nodesTp_per_node = []
nodes_fairness = []

flowsTp = []
flowsAd = []
flowsDr = []
flowsDrat = []
flowsEnergy = []
flowsTp_per_node = []
flows_fairness = []

rateTp = []
rateAd = []
rateDr = []
rateDrat = []
rateEnergy = []
rateTp_per_node = []
rate_fairness = []

speedTp = []
speedAd = []
speedDr = []
speedDrat = []
speedEnergy = []
speedTp_per_node = []
speed_fairness = []

txTp = []
txAd = []
txDr = []
txDrat = []
txEnergy = []
txTp_per_node = []
tx_fairness = []

nodes_prevTp = []
nodes_prevAd = []
nodes_prevDr = []
nodes_prevDrat = []
nodes_prevEnergy = []
nodes_prevTp_per_node = []
nodes_prev_fairness = []

flows_prevTp = []
flows_prevAd = []
flows_prevDr = []
flows_prevDrat = []
flows_prevEnergy = []
flows_prevTp_per_node = []
flows_prev_fairness = []

rate_prevTp = []
rate_prevAd = []
rate_prevDr = []
rate_prevDrat = []
rate_prevEnergy = []
rate_prevTp_per_node = []
rate_prev_fairness = []

speed_prevTp = []
speed_prevAd = []
speed_prevDr = []
speed_prevDrat = []
speed_prevEnergy = []
speed_prevTp_per_node = []
speed_prev_fairness = []

tx_prevTp = []
tx_prevAd = []
tx_prevDr = []
tx_prevDrat = []
tx_prevEnergy = []
tx_prevTp_per_node = []
tx_prev_fairness = []

nodes_renoTp = []
nodes_renoAd = []
nodes_renoDr = []
nodes_renoDrat = []
nodes_renoEnergy = []
nodes_renoTp_per_node = []
nodes_reno_fairness = []

flows_renoTp = []
flows_renoAd = []
flows_renoDr = []
flows_renoDrat = []
flows_renoEnergy = []
flows_renoTp_per_node = []
flows_reno_fairness = []

rate_renoTp = []
rate_renoAd = []
rate_renoDr = []
rate_renoDrat = []
rate_renoEnergy = []
rate_renoTp_per_node = []
rate_reno_fairness = []

speed_renoTp = []
speed_renoAd = []
speed_renoDr = []
speed_renoDrat = []
speed_renoEnergy = []
speed_renoTp_per_node = []
speed_reno_fairness = []

tx_renoTp = []
tx_renoAd = []
tx_renoDr = []
tx_renoDrat = []
tx_renoEnergy = []
tx_renoTp_per_node = []
tx_reno_fairness = []

while True:
    line = file.readline()
    line2 = file2.readline()
    line3 = file3.readline()
    if not line and not line2 and not line3:
        break
    tokens = line.split()
    tokens2 = line2.split()
    tokens3 = line3.split()
    mesType = tokens[0]
    mesType2 = tokens2[0]
    mesType3 = tokens3[0]
    size = int(tokens[1])
    size2 = int(tokens2[1])
    size3 = int(tokens3[1])
    throughput = float(tokens[2])
    throughput2 = float(tokens2[2])
    throughput3 = float(tokens3[2])
    avgDelay = float(tokens[3])
    avgDelay2 = float(tokens2[3])
    avgDelay3 = float(tokens3[3])
    delRate = float(tokens[4])
    delRate2 = float(tokens2[4])
    delRate3 = float(tokens3[4])
    dropRatio = float(tokens[5])
    dropRatio2 = float(tokens2[5])
    dropRatio3 = float(tokens3[5])
    total_energy = float(tokens[6])
    total_energy2 = float(tokens2[6])
    total_energy3 = float(tokens3[6])
    tp_per_node = float(tokens[7])
    tp_per_node2 = float(tokens2[7])
    tp_per_node3 = float(tokens3[7])
    fairness = float(tokens[8])
    fairness2 = float(tokens2[8])
    fairness3 = float(tokens3[8])

    if mesType == 'nodes':
        nodesTp.append(throughput)
        nodesAd.append(avgDelay)
        nodesDr.append(delRate)
        nodesDrat.append(dropRatio)
        nodes_prevTp.append(throughput2)
        nodes_prevAd.append(avgDelay2)
        nodes_prevDr.append(delRate2)
        nodes_prevDrat.append(dropRatio2)
        nodes_renoTp.append(throughput3)
        nodes_renoAd.append(avgDelay3)
        nodes_renoDr.append(delRate3)
        nodes_renoDrat.append(dropRatio3)
        nodesEnergy.append(total_energy)
        nodes_prevEnergy.append(total_energy2)
        nodes_renoEnergy.append(total_energy3)
        nodesTp_per_node.append(tp_per_node)
        nodes_prevTp_per_node.append(tp_per_node2)
        nodes_renoTp_per_node.append(tp_per_node3)
        nodes_fairness.append(fairness)
        nodes_prev_fairness.append(fairness2)
        nodes_reno_fairness.append(fairness3)

    elif mesType == 'flows':
        flowsTp.append(throughput)
        flowsAd.append(avgDelay)
        flowsDr.append(delRate)
        flowsDrat.append(dropRatio)
        flows_prevTp.append(throughput2)
        flows_prevAd.append(avgDelay2)
        flows_prevDr.append(delRate2)
        flows_prevDrat.append(dropRatio2)
        flows_renoTp.append(throughput3)
        flows_renoAd.append(avgDelay3)
        flows_renoDr.append(delRate3)
        flows_renoDrat.append(dropRatio3)
        flowsEnergy.append(total_energy)
        flows_prevEnergy.append(total_energy2)
        flows_renoEnergy.append(total_energy3)
        flowsTp_per_node.append(tp_per_node)
        flows_prevTp_per_node.append(tp_per_node2)
        flows_renoTp_per_node.append(tp_per_node3)
        flows_fairness.append(fairness)
        flows_prev_fairness.append(fairness2)
        flows_reno_fairness.append(fairness3)

    elif mesType == 'rate':
        rateTp.append(throughput)
        rateAd.append(avgDelay)
        rateDr.append(delRate)
        rateDrat.append(dropRatio)
        rate_prevTp.append(throughput2)
        rate_prevAd.append(avgDelay2)
        rate_prevDr.append(delRate2)
        rate_prevDrat.append(dropRatio2)
        rate_renoTp.append(throughput3)
        rate_renoAd.append(avgDelay3)
        rate_renoDr.append(delRate3)
        rate_renoDrat.append(dropRatio3)
        rateEnergy.append(total_energy)
        rate_prevEnergy.append(total_energy2)
        rate_renoEnergy.append(total_energy3)
        rateTp_per_node.append(tp_per_node)
        rate_prevTp_per_node.append(tp_per_node2)
        rate_renoTp_per_node.append(tp_per_node3)
        rate_fairness.append(fairness)
        rate_prev_fairness.append(fairness2)
        rate_reno_fairness.append(fairness3)

    elif mesType == 'speed' and file_name == 'data.txt' and file_name2 == 'data_prev.txt':
        speedTp.append(throughput)
        speedAd.append(avgDelay)
        speedDr.append(delRate)
        speedDrat.append(dropRatio)
        speed_prevTp.append(throughput2)
        speed_prevAd.append(avgDelay2)
        speed_prevDr.append(delRate2)
        speed_prevDrat.append(dropRatio2)
        speed_renoTp.append(throughput3)
        speed_renoAd.append(avgDelay3)
        speed_renoDr.append(delRate3)
        speed_renoDrat.append(dropRatio3)
        speedEnergy.append(total_energy)
        speed_prevEnergy.append(total_energy2)
        speed_renoEnergy.append(total_energy3)
        speedTp_per_node.append(tp_per_node)
        speed_prevTp_per_node.append(tp_per_node2)
        speed_renoTp_per_node.append(tp_per_node3)
        speed_fairness.append(fairness)
        speed_prev_fairness.append(fairness2)
        speed_reno_fairness.append(fairness3)

    elif mesType == 'tx' and file_name == 'data2.txt' and file_name2 == 'data_prev2.txt':
        txTp.append(throughput)
        txAd.append(avgDelay)
        txDr.append(delRate)
        txDrat.append(dropRatio)
        tx_prevTp.append(throughput2)
        tx_prevAd.append(avgDelay2)
        tx_prevDr.append(delRate2)
        tx_prevDrat.append(dropRatio2)
        tx_renoTp.append(throughput3)
        tx_renoAd.append(avgDelay3)
        tx_renoDr.append(delRate3)
        tx_renoDrat.append(dropRatio3)
        txEnergy.append(total_energy)
        tx_prevEnergy.append(total_energy2)
        tx_renoEnergy.append(total_energy3)
        txTp_per_node.append(tp_per_node)
        tx_prevTp_per_node.append(tp_per_node2)
        tx_renoTp_per_node.append(tp_per_node3)
        tx_fairness.append(fairness)
        tx_prev_fairness.append(fairness2)
        tx_reno_fairness.append(fairness3)

file.close()

nodesList = [nodesTp, nodesAd, nodesDr, nodesDrat, nodesEnergy, nodesTp_per_node, nodes_fairness]
nodes_prevList = [nodes_prevTp, nodes_prevAd, nodes_prevDr, nodes_prevDrat, nodes_prevEnergy, nodes_prevTp_per_node, nodes_prev_fairness]
nodes_renoList = [nodes_renoTp, nodes_renoAd, nodes_renoDr, nodes_renoDrat, nodes_renoEnergy, nodes_renoTp_per_node, nodes_reno_fairness]
flowsList = [flowsTp, flowsAd, flowsDr, flowsDrat, flowsEnergy, flowsTp_per_node, flows_fairness]
flows_prevList = [flows_prevTp, flows_prevAd, flows_prevDr, flows_prevDrat, flows_prevEnergy, flows_prevTp_per_node, flows_prev_fairness]
flows_renoList = [flows_renoTp, flows_renoAd, flows_renoDr, flows_renoDrat, flows_renoEnergy, flows_renoTp_per_node, flows_reno_fairness]
rateList = [rateTp, rateAd, rateDr, rateDrat, rateEnergy, rateTp_per_node, rate_fairness]
rate_prevList = [rate_prevTp, rate_prevAd, rate_prevDr, rate_prevDrat, rate_prevEnergy, rate_prevTp_per_node, rate_prev_fairness]
rate_renoList = [rate_renoTp, rate_renoAd, rate_renoDr, rate_renoDrat, rate_renoEnergy, rate_renoTp_per_node, rate_reno_fairness]
speedList = [speedTp, speedAd, speedDr, speedDrat, speedEnergy, speedTp_per_node, speed_fairness]
speed_prevList = [speed_prevTp, speed_prevAd, speed_prevDr, speed_prevDrat, speed_prevEnergy, speed_prevTp_per_node, speed_prev_fairness]
speed_renoList = [speed_renoTp, speed_renoAd, speed_renoDr, speed_renoDrat, speed_renoEnergy, speed_renoTp_per_node, speed_reno_fairness]
txList = [txTp, txAd, txDr, txDrat, txEnergy, txTp_per_node, tx_fairness]
tx_prevList = [tx_prevTp, tx_prevAd, tx_prevDr, tx_prevDrat, tx_prevEnergy, tx_prevTp_per_node, tx_prev_fairness]
tx_renoList = [tx_renoTp, tx_renoAd, tx_renoDr, tx_renoDrat, tx_renoEnergy, tx_renoTp_per_node, tx_reno_fairness]


for i in range(len(nodesList)):
    x = np.array(nodes)
    y = np.array(nodesList[i])
    z = np.array(nodes_prevList[i])
    w = np.array(nodes_renoList[i])
    # X_Y_Spline = make_interp_spline(x, y)
    # X_ = np.linspace(x.min(), x.max(), 500)
    # Y_ = X_Y_Spline(X_)
    plt.plot(x, y, color='r', label='new', linestyle='dashed')
    plt.plot(x, z, color='g', label='old', linestyle='dashed')
    # plt.plot(x, w, color='b', label='reno', linestyle='dashed')
    plt.xlabel('nodes')
    if i == 0:
        plt.ylabel('Throughput')
    elif i == 1:
        plt.ylabel('Average Delay')
    elif i == 2:
        plt.ylabel('Delivery Ratio')
    elif i == 3:
        plt.ylabel('Drop Ratio')
    elif i == 4:
        plt.ylabel('Energy')
    elif i == 5:
        plt.ylabel('Throughput per node')
    elif i == 6:
        plt.plot(x, w, color='b', label='reno', linestyle='dashed')
        plt.ylabel('Fairness Index')
    plt.title("nodes vs metrics")
    plt.legend(loc='best')
    plt.show()

for i in range(len(flowsList)):
    x = np.array(flows)
    y = np.array(flowsList[i])
    z = np.array(flows_prevList[i])
    w = np.array(flows_renoList[i])
    # X_Y_Spline = make_interp_spline(x, y)
    # X_ = np.linspace(x.min(), x.max(), 500)
    # Y_ = X_Y_Spline(X_)
    plt.plot(x, y, color='r', label='new', linestyle='dashed')
    plt.plot(x, z, color='g', label='old', linestyle='dashed')
    # plt.plot(x, w, color='b', label='reno', linestyle='dashed')
    plt.xlabel('flows')
    if i == 0:
        plt.ylabel('Throughput')
    elif i == 1:
        plt.ylabel('Average Delay')
    elif i == 2:
        plt.ylabel('Delivery Ratio')
    elif i == 3:
        plt.ylabel('Drop Ratio')
    elif i == 4:
        plt.ylabel('Energy')
    elif i == 5:
        plt.ylabel('Throughput per node')
    elif i == 6:
        plt.plot(x, w, color='b', label='reno', linestyle='dashed')
        plt.ylabel('Fairness Index')
    plt.title("flows vs metrics")
    plt.legend(loc='best')
    plt.show()

for i in range(len(rateList)):
    x = np.array(packets_per_sec)
    y = np.array(rateList[i])
    z = np.array(rate_prevList[i])
    w = np.array(rate_renoList[i])
    # X_Y_Spline = make_interp_spline(x, y)
    # X_ = np.linspace(x.min(), x.max(), 500)
    # Y_ = X_Y_Spline(X_)
    plt.plot(x, y, color='r', label='new', linestyle='dashed')
    plt.plot(x, z, color='g', label='old', linestyle='dashed')
    # plt.plot(x, w, color='b', label='reno', linestyle='dashed')
    plt.xlabel('packets per second')
    if i == 0:
        plt.ylabel('Throughput')
    elif i == 1:
        plt.ylabel('Average Delay')
    elif i == 2:
        plt.ylabel('Delivery Ratio')
    elif i == 3:
        plt.ylabel('Drop Ratio')
    elif i == 4:
        plt.ylabel('Energy')
    elif i == 5:
        plt.ylabel('Throughput per node')
    elif i == 6:
        plt.plot(x, w, color='b', label='reno', linestyle='dashed')
        plt.ylabel('Fairness Index')
    plt.title("packets per second vs metrics")
    plt.legend(loc='best')
    plt.show()

if file_name == 'data.txt' and file_name2 == 'data_prev.txt':
    for i in range(len(speedList)):
        x = np.array(node_speed)
        y = np.array(speedList[i])
        z = np.array(speed_prevList[i])
        w = np.array(speed_renoList[i])
        # X_Y_Spline = make_interp_spline(x, y)
        # X_ = np.linspace(x.min(), x.max(), 500)
        # Y_ = X_Y_Spline(X_)
        plt.plot(x, y, color='r', label='new', linestyle='dashed')
        plt.plot(x, z, color='g', label='old', linestyle='dashed')
        # plt.plot(x, w, color='b', label='reno', linestyle='dashed')
        plt.xlabel('node speed')
        if i == 0:
            plt.ylabel('Throughput')
        elif i == 1:
            plt.ylabel('Average Delay')
        elif i == 2:
            plt.ylabel('Delivery Ratio')
        elif i == 3:
            plt.ylabel('Drop Ratio')
        elif i == 4:
            plt.ylabel('Energy')
        elif i == 5:
            plt.ylabel('Throughput per node')
        elif i == 6:
            plt.plot(x, w, color='b', label='reno', linestyle='dashed')
            plt.ylabel('Fairness Index')
        plt.title("node speed vs metrics")
        plt.legend(loc='best')
        plt.show()

if file_name == 'data2.txt' and file_name2 == 'data_prev2.txt':
    for i in range(len(txList)):
        x = np.array(tx_range)
        y = np.array(txList[i])
        z = np.array(tx_prevList[i])
        w = np.array(tx_renoList[i])
        # X_Y_Spline = make_interp_spline(x, y)
        # X_ = np.linspace(x.min(), x.max(), 500)
        # Y_ = X_Y_Spline(X_)
        plt.plot(x, y, color='r', label='new', linestyle='dashed')
        plt.plot(x, z, color='g', label='old', linestyle='dashed')
        # plt.plot(x, w, color='b', label='reno', linestyle='dashed')
        plt.xlabel('transmission range')
        if i == 0:
            plt.ylabel('Throughput')
        elif i == 1:
            plt.ylabel('Average Delay')
        elif i == 2:
            plt.ylabel('Delivery Ratio')
        elif i == 3:
            plt.ylabel('Drop Ratio')
        elif i == 4:
            plt.ylabel('Energy')
        elif i == 5:
            plt.ylabel('Throughput per node')
        elif i == 6:
            plt.plot(x, w, color='b', label='reno', linestyle='dashed')
            plt.ylabel('Fairness Index')
        plt.title("transmission range vs metrics")
        plt.legend(loc='best')
        plt.show()
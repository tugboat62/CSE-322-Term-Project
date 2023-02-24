# need to add throughput for individual links varying 
import sys

size = 50
nodes = 40
mesType = 'flows'
file_name = 'data.txt'
file_name2 = 'trace.tr'
initial_energy = 20

if len(sys.argv) == 8 :
    mesType = sys.argv[1]
    size = int(sys.argv[2])
    file_name = sys.argv[3]
    file_name2 = sys.argv[4]
    initial_energy = float(sys.argv[5])
    nodes = int(sys.argv[6])
    # initial_energy = float(sys.argv[7])


received_packets = 0
sent_packets = 0
dropped_packets = 0
total_delay = 0
received_bytes = 0
total_energy = 0
sum_xi = 0
sum_xi2 = 0
totalFlows = 0

start_time = 1000000
end_time = 0

# constants
header_bytes = 20

# Using readline()
file1 = open(file_name2, 'r')
file2 = open(file_name, 'a+')
count = 0
sent_time = {}
flow_bytes = {}
flow_times = {}

while True:
    count += 1
    line = file1.readline()
    if not line:
        break
    params = line.split()
    event = params[0]
    if event == "N" or event == "M": # ignore node creation
        continue
    time_sec = float(params[params.index("-t")+1])
    node = params[(params.index("-Ni")+1)]
    layer = params[(params.index("-Nl")+1)]
    if line.find("-Ne") != -1:
        index = params.index("-Ne")
        energy = initial_energy - float(params[index + 1])
        total_energy += energy

    if start_time > time_sec:
        start_time = time_sec
    end_time = time_sec

    if layer == "AGT":
        flow_id = params[(params.index("-If")+1)]
        packet_type = params[(params.index("-It")+1)]
        if packet_type == "tcp" :
            packet_id = params[(params.index("-Ii")+1)]
            if event == "s" :
                sent_time[packet_id] = time_sec
                sent_packets += 1

            elif event == "r" :
                packet_bytes = float(params[int(params.index("-Il")+1)])
                delay = time_sec - sent_time[packet_id]
                if flow_id not in flow_times:
                    flow_times[flow_id] = 0
                    flow_bytes[flow_id] = 0
                flow_times[flow_id] += delay
                flow_bytes[flow_id] += packet_bytes
                total_delay += delay
                # if file_name2 == 'trace2.tr':
                #     bytesNo = packet_bytes - header_bytes
                # else:
                #     bytesNo = packet_bytes
                bytesNo = packet_bytes
                received_bytes += bytesNo
                received_packets += 1

    if params.count("tcp") > 0 and event == "d" :
        dropped_packets += 1


for key in flow_times:
    totalFlows += 1
    tp = (flow_bytes[key]*8)/flow_times[key]
    sum_xi += tp
    sum_xi2 += tp ** 2

file1.close()
print("received_packets", received_packets)
sent_time = time_sec
simulation_time = end_time - start_time
throughput = (received_bytes * 8) / simulation_time
avgDelay = (total_delay / received_packets)
delRate = (received_packets / sent_packets)
dropRatio = (dropped_packets / sent_packets)
tp_per_node = throughput / nodes
fairness_index = (sum_xi ** 2) / (sum_xi2 * totalFlows)
line = f"{mesType} {size} {throughput} {avgDelay} {delRate} {dropRatio} {total_energy} {tp_per_node} {fairness_index}\n"
file2.write(line)

file2.close()
# need to add throughput for individual links varying 
import sys

size = 50
mesType = 'flows'
file_name = 'data.txt'

if len(sys.argv) == 4 :
    mesType = sys.argv[1]
    size = int(sys.argv[2])
    file_name = sys.argv[3]

file1 = open(file_name, 'a+')
temp = open('temp.txt', 'r')
sums = [0] * 7
count = 0

while True:
    line = temp.readline()
    if not line:
        break
    count += 1
    params = line.split()
    for i in range(7):
        sums[i] += float(params[2+i])

for i in range(7):
    print(sums[i])
    print(count)
    sums[i] /= count
line = mesType + ' ' + str(size) + ' '
for i in range(7):
    if i == 6:
        line += str(sums[i])
    else:
        line += str(sums[i]) + ' '

print(line)

file1.write(line)
file1.close()
temp.close()
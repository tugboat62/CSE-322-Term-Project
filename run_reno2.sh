# > data_reno2.txt
> temp.txt
# Varying number of nodes
# n=0
# for i in {1..5}
# do
#     n=$((n+20))
#     for i in {1..20}
#     do
#         ns 1805051_part2.tcl $n 20 300 1 Reno
#         python3 parser.py nodes $n temp.txt trace2.tr 20 $n 20
#     done
#     python3 average.py nodes $n data_reno2.txt
#     > temp.txt
# done

# > temp.txt

# # Varying number of flows
# f=0
# for i in {1..5}
# do
#     f=$((f+10))
#     for i in {1..20}
#     do
#         ns 1805051_part2.tcl 40 $f 300 1 Reno
#         python3 parser.py flows $f temp.txt trace2.tr 20 40 20
#     done
#     python3 average.py flows $f data_reno2.txt
#     > temp.txt
# done

# > temp.txt

# Varying transmission range
tx=0
for i in {1..5}
do
    tx=$((tx+1))
    for i in {1..20}
    do
        ns 1805051_part2.tcl 40 20 300 $tx Reno
        python3 parser.py tx $tx temp.txt trace2.tr 20 40 300
    done
    python3 average.py tx $tx data_reno2.txt
    > temp.txt
done

> temp.txt

# Varying rate
r=0
for i in {1..5}
do
    r=$((r+100))
    for i in {1..20}
    do
        ns 1805051_part2.tcl 40 20 $r 1 Reno
        python3 parser.py rate $r temp.txt trace2.tr 20 40 20
    done
    python3 average.py rate $r data_reno2.txt
    > temp.txt
done

rm temp.txt


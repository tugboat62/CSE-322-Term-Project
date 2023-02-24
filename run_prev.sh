> data_prev.txt
> temp.txt
# Varying number of nodes
n=0
for i in {1..5}
do
    n=$((n+20))
    for i in {1..20}
    do
        ns 1805051.tcl $n 20 15 300
        python3 parser.py nodes $n temp.txt trace.tr 20 $n 20
    done
    python3 average.py nodes $n data_prev.txt
done

> temp.txt

# Varying number of flows
f=0
for i in {1..5}
do
    f=$((f+10))
    for i in {1..20}
    do
        ns 1805051.tcl 40 $f 15 300
        python3 parser.py flows $f temp.txt trace.tr 20 40 20
    done
    python3 average.py flows $f data_prev.txt
done

> temp.txt

# Varying speed
s=0
for i in {1..5}
do
    s=$((s+5))
    for i in {1..20}
    do
        ns 1805051.tcl 40 20 $s 300
        python3 parser.py speed $s temp.txt trace.tr 20 40 20
    done
    python3 average.py speed $s data_prev.txt
done

> temp.txt

# Varying rate
r=0
for i in {1..5}
do
    r=$((r+100))
    for i in {1..20}
    do
        ns 1805051.tcl 40 20 15 $r
        python3 parser.py rate $r temp.txt trace.tr 20 40 20
    done
    python3 average.py rate $r data_prev.txt
done

rm temp.txt
> paper_data.txt
> temp.txt

# Varying rate
r=0
for i in {1..10}
do
    r=$((r+100))
    for i in {1..20}
    do
        ns 1805051_paper.tcl 40 40 15 $r
        python3 parser.py rate $r temp.txt trace3.tr 20 40 20
    done
    python3 average.py rate $r paper_data.txt
    > temp.txt
done

rm temp.txt
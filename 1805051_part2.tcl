# simulator
set ns [new Simulator]


# ======================================================================
# Define options

set val(chan)                    Channel/WirelessChannel  ;# channel type
set val(prop)                    Propagation/TwoRayGround ;# radio-propagation model
set val(ant)                     Antenna/OmniAntenna      ;# Antenna type
set val(ll)                         LL                    ;# Link layer type
set val(ifq)                     Queue/DropTail/PriQueue  ;# Interface queue type
set val(ifqlen)                     50                    ;# max packet in ifq
set val(netif)                   Phy/WirelessPhy          ;# network interface type
set val(mac)                        Mac/802_11            ;# MAC type
set val(rp)                         AODV                  ;# ad-hoc routing protocol 
set val(nn)                         40                    ;# number of mobilenodes
set val(nf)                         20                    ;# number of flows
set val(grid)                       500                   ;# grid size 
set val(rate)                       250                   ;# packets per second 
set val(packet_size)                1000                  ;# packet size in bytes
set val(energymodel)                EnergyModel           ;# Energy set up
set val(initialenergy)              20.0                  ;# Initial energy
set val(congestion_control)         Vegas                 ;# congestion control
set val(coefficientOfTX)            1.0                   ;# coefficient of TX      
# set val(energymodel_15)             EnergyModel           ;# Energy set up
# set val(initialenergy_15)           300.0                  ;# Initial energy
# set val(idlepower_15)               40                    ;# LEAP (802.11g)
# set val(rxpower_15)                 75                    ;# LEAP (802.11g)
# set val(txpower_15)                 75                    ;# LEAP (802.11g)
# set val(sleeppower_15)              40                    ;# LEAP (802.11g)
# =======================================================================
# take arguments from command line
if { $argc == 4 } {
    puts "inside arguments"
    set val(nn)   [lindex $argv 0]
    set val(nf)   [lindex $argv 1]
    set val(rate)  [lindex $argv 2]
    set val(coefficientOfTX)  [lindex $argv 3]
}

if { $argc == 5 } {
    puts "inside arguments"
    set val(nn)   [lindex $argv 0]
    set val(nf)   [lindex $argv 1]
    set val(rate)  [lindex $argv 2]
    set val(coefficientOfTX)  [lindex $argv 3]
    set val(congestion_control)  [lindex $argv 4]
}

# set nowValue  [Phy/WirelessPhy set Pt_]            
# set newValue_Pt  [expr $val(coefficientOfTX) * $val(coefficientOfTX) * $nowValue]
# Phy/WirelessPhy set Pt_  $newValue_Pt;

Phy/WirelessPhy set CPThresh_ 100.0
Phy/WirelessPhy set CSThresh_ 4.21756e-11 ;#transmission range
Phy/WirelessPhy set RXThresh_ 4.4613e-10 ;#transmission range
Phy/WirelessPhy set bandwidth_ 512kb
Phy/WirelessPhy set Pt_ [expr { 0.2818 * $val(coefficientOfTX) }]
Phy/WirelessPhy set freq_ 2.4e+9
Phy/WirelessPhy set L_ 1.0 

# trace file
set trace_file [open trace2.tr w]
$ns use-newtrace
$ns trace-all $trace_file


# nam file
set nam_file [open animation2.nam w]


$ns namtrace-all-wireless $nam_file $val(grid) $val(grid)

# topology: to keep track of node movements
set topo [new Topography]
$topo load_flatgrid $val(grid) $val(grid) ;# 500m x 500m area


# general operation director for mobilenodes
create-god $val(nn)


# node configs
# ======================================================================

# $ns node-config -addressingType flat or hierarchical or expanded
#                  -adhocRouting   DSDV or DSR or TORA
#                  -llType	   LL
#                  -macType	   Mac/802_11
#                  -propType	   "Propagation/TwoRayGround"
#                  -ifqType	   "Queue/DropTail/PriQueue"
#                  -ifqLen	   50
#                  -phyType	   "Phy/WirelessPhy"
#                  -antType	   "Antenna/OmniAntenna"
#                  -channelType    "Channel/WirelessChannel"
#                  -topoInstance   $topo
#                  -energyModel    "EnergyModel"
#                  -initialEnergy  (in Joules)
#                  -rxPower        (in W)
#                  -txPower        (in W)
#                  -agentTrace     ON or OFF
#                  -routerTrace    ON or OFF
#                  -macTrace       ON or OFF
#                  -movementTrace  ON or OFF

# ======================================================================

$ns node-config -adhocRouting $val(rp) \
                -llType $val(ll) \
                -macType $val(mac) \
                -ifqType $val(ifq) \
                -ifqLen $val(ifqlen) \
                -antType $val(ant) \
                -propType $val(prop) \
                -phyType $val(netif) \
                -topoInstance $topo \
                -channelType $val(chan) \
                -energyModel $val(energymodel) \
                -initialEnergy $val(initialenergy)
                # -energyModel $val(energymodel_15) \
                # -idlePower $val(idlepower_15) \
                # -rxPower $val(rxpower_15) \
                # -txPower $val(txpower_15) \
                # -sleepPower $val(sleeppower_15) \
                # -initialEnergy $val(initialenergy_15) \
                -agentTrace ON \
                -routerTrace OFF \
                -macTrace OFF \
                -movementTrace OFF
                # -rx_sens_ -90 


array set nodes {}

# create nodes
for {set i 0} {$i < $val(nn) } {incr i} {
    set node($i) [$ns node]
    # set speed [expr 1.0 + rand()*4.0] 
    $node($i) random-motion 0                  ;# disable random motion
    
    set xx [expr rand()*$val(grid)]
    set yy [expr rand()*$val(grid)]
    
    while {[info exists nodes(xx,yy)]} {
        set xx [expr rand()*$val(grid)]
        set yy [expr rand()*$val(grid)]
    } 

    $node($i) set X_ $xx
    $node($i) set Y_ $yy
    $node($i) set Z_ 0.0
    # $node($i) set tx_range_ $val(tx_range)
    set nodes($xx,$yy) 1

    $ns initial_node_pos $node($i) 20
    # set dest_x [expr rand()*$val(grid)]
    # set dest_y [expr rand()*$val(grid)]
    # puts "node $i"
    # set start_time [expr 1.0 + rand()*10.0]
    # $ns at $start_time "$node($i) setdest $dest_x $dest_y $speed"
} 

unset nodes

# create flows
for {set i 0} {$i < $val(nf)} {incr i} {
    set src [expr {int(rand()*$val(nn))}]
    set dest [expr {int(rand()*$val(nn))}]
    while {$src == $dest} {
        set dest [expr {int(rand()*$val(nn))}]
    }
    
    # Traffic config
    # create agent
    # set udp [new Agent/UDP]
    # $udp set class_ 2
    # # attach to nodes
    # $ns attach-agent $node($src) $udp
    # set null [new Agent/Null]
    # $ns attach-agent $node($dest) $null
    # # connect agents
    # $ns connect $udp $null
    # $udp set fid_ $i

    # # Traffic generator
    # set cbr [new Application/Traffic/CBR]
    # # attach to agent
    # $cbr attach-agent $udp
    # $cbr set type_ CBR
    # $cbr set packetSize_ 512
    # $cbr set rate_ 64kb
    # $cbr set random_ false

    # # puts "Flow $i"
    
    # # start traffic generation
    # $ns at 1.0 "$cbr start"

    # Traffic config
    # create agent
    set tcp [new Agent/TCP/$val(congestion_control)]
    set tcp_sink [new Agent/TCPSink]
    # attach to nodes
    $ns attach-agent $node($src) $tcp
    $ns attach-agent $node($dest) $tcp_sink
    # connect agents
    $ns connect $tcp $tcp_sink
    $tcp set fid_ $i
    # $tcp set maxseq_ $val(rate)

    # Traffic generator
    set ftp [new Application/FTP]
    # attach to agent
    $ftp attach-agent $tcp
    $ftp set type_ FTP
    $ftp set maxpkts_ $val(rate)
    
    # $ftp set rate_ $val(rate)*$val(packet_size)
    
    # start traffic generation
    $ns at 1.0 "$ftp start"

}



# End Simulation

# Stop nodes
for {set i 0} {$i < $val(nn)} {incr i} {
    $ns at 20.0 "$node($i) reset"
}

# call final function
proc finish {} {
    global ns trace_file nam_file
    $ns flush-trace
    close $trace_file
    close $nam_file
}

proc halt_simulation {} {
    global ns
    puts "Simulation ending"
    $ns halt
}

$ns at 20.0001 "finish"
$ns at 20.0002 "halt_simulation"


# Run simulation
puts "Simulation starting"
$ns run


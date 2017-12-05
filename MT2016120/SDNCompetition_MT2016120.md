# Base Problem
## Approach
-   Lab_1.py was just the topology
-   Lab_2.py is a more beautified version of it + external controller
-   Lab_3.py = Lab_2.py + VLAN

# Sub problem 1
## Statement
Two hosts of same VLAN should not ping each other
## Approach
Pushed a flow into Switch 1 to stop sending packets destined to H1-S2-V1 (MAC - :03) which are incoming via port (openflow:1:1) that is connected to H1-S1-V1.

    - sh ovs-ofctl add-flow s1 in_port=1,dl_dst=00:00:00:00:00:03,actions=drop
    


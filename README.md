# Collection of statistics to understand the instantaneous behaviour of the underlying network 

## Problem Definition
The state of the art congestion control algorithms are based on End to End packet statistics. Leveraging the network feedback for congestion control is another promising dimension, but the catch is the availability of network statistics at one place. Software Defined Networking can mitigate
this limitation and hence be a pillar for network suggested TCP Congestion control.

##  Version 1 - StatCollection from all switch interfaces using Python script.
### Modules
#### 1. Topology Generation [source code](https://gitlab.com/IIITB_SDN_2017/MT2016119_MT2016120_StatCollection/blob/master/src/MT2016120_Sabari_Nathan/Generator.py)
* A generic topology generator. 
* Input is a CSV file whose 1st column specifies all nodes
    * Hosts' name should start with _'h'_
    * Switches' name should start with _'s'_
    * Controllers' name should start with _'c'_
* Since the internet can have different controllers controlling different part of network, we have support for different controllers. With a many to one mapping between Switch and controllers.
* Which controller controller controls which switch can also be specified.
* Run the script using `sudo python Generator.py`
* Make sure you are in the corresponding directory + followed all [set-up instructions](https://gitlab.com/IIITB_SDN_2017/MT2016119_MT2016120_StatCollection/blob/master/src/MT2016120_Sabari_Nathan/Setup%20instructions.md)
* 

## Issues to be addressed
1. Communicating the node statistics from each intermediate network device to SDN controller.
2. A web-based platform at the controller which shall respond to queries raised by the systems who wish to perform network suggested congestion control.
3. The intelligent decisions that the client would make, such as changing the routing metric (Layer 3), changing the token replenishment rate of the token buckets (Layer 2), setting the congestion window of TCP (Layer 4).

## Project delegation
1. Statistics collection and SDN-Node communication – Sabari Nathan A. (MT2016120).
2. Creating web interface between client and SDN controller for information retrieval – Maneesha S. (MT2016119)
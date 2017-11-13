##Problem Definition

The state of the art congestion control algorithms are based on End to End packet statistics. Leveraging the network feedback for congestion control is another promising dimension, but the catch is the availability of network statistics at one place. Software Defined Networking can mitigate
this limitation and hence be a pillar for network suggested TCP Congestion control.

## Issues to be addressed
1. Communicating the node statistics from each intermediate network device to SDN controller.
2. A web-based platform at the controller which shall respond to queries raised by the systems who wish to perform network suggested congestion control.
3. The intelligent decisions that the client would make, such as changing the routing metric (Layer 3), changing the token replenishment rate of the token buckets (Layer 2), setting the congestion window of TCP (Layer 4).

## Project delegation
1. Statistics collection and SDN-Node communication – Sabari Nathan A. (MT2016120).
2. Creating web interface between client and SDN controller for information retrieval – Maneesha S. (MT2016119)
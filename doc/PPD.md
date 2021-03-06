# Update for week 7-14/11/2017

## Sabari Nathan: 
1. Created a packet sniffing code for reading the IP header and the TCP header (Python - scapy).
2. Identified the list of statistics present at the SDN controller that will be useful for the TCP congestion window manipulation.
3. Read about PCE - Path Computation Element (RFC 4655) and possible help it would bring in to the project. Found that PCE had to be run at another level. It was
found that PCE would be an overkill for classification of flows.

## Maneesha S:
1. Environment setup inside Mininet OS and to create a web application.
   Issues faced:
        - Port number clash - resolved.
2. Working on an XML parser to send the statistics identified above.
3. Working on a web Interface so that hosts can query the MYSQL server and get the statistics.


# Agenda for week 15-21/11/2017:

## Sabari Nathan:
1. Creating an Internet like topology in consensus with Prof. Samar
2. Push the Flow descriptions (Source IP and Source port number) through sockets.
3. Parse the flow description and insert into MySQL server.


## Maneesha S:
1. Testing the web interface.
2. Write a Tomcat servlet to accept the queries from Mininet hosts.
3. Enable look-up in MySQL and respond to queries.

# Update for weeks 15-28/11/2017

## Sabari Nathan
1. Discussed with Prof. Samar for the topology.
2. Wrote a custom-built sniffer with the following features,
    - Sniff at each switch.
    - Sniff at mentioned interface.
    - Will report every time a new quadruple is encountered (Source IP,Port and Destination IP, Port).
    - Filters out all traffic but TCP flows.
    
## Maneesha S:
1. Created 3 web services,
    - GetRoutingInfo -> finds the path taken by the flow.
    - GetQueueInfo -> finds the corresponding queue statistics.
    - GetPortInfo -> finds the corresponding port statistics.
2. Decided and created the database schema to serve as the backend.


# Agenda for week 28/11/2017 - 3/12/2017

## Sabari Nathan:
1. Unit testing & scaling up.
2. Push flow descriptions to MySQL server created by Maneesha S.

## Maneesha:
1. Unit testing and scaling up

## Sabari Nathan and Maneesha
1. Integration testing.

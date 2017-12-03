from mininet.net import Mininet
from mininet.node import Controller, RemoteController
from mininet.topo import Topo
from mininet.link import TCLink  # So we can rate limit links
from mininet.cli import CLI  # So we can bring up the Mininet CLI

net = Mininet(topo=None, link=TCLink, build=False)
print "**** Adding hosts and switches ****"
h1 = net.addHost("h1",mac="00:00:00:00:00:10")
h2 = net.addHost("h2",mac="00:00:00:00:00:11")
h3 = net.addHost("h3",mac="00:00:00:00:00:12")
s1 = net.addSwitch("s1",listenPort=6634,mac="00:00:00:00:10:10")
s2 = net.addSwitch("s2",listenPort=6634,mac="00:00:00:00:10:11")
s3 = net.addSwitch("s3",listenPort=6634,mac="00:00:00:00:10:12")
s4 = net.addSwitch("s4",listenPort=6634,mac="00:00:00:00:10:13")
print "**** Adding Traffic conditioned links ****"

# Add links
net.addLink( h1, s1, bw=5, delay='5ms',use_htb=True)
net.addLink( h2, s2, bw=5, delay='5ms',use_htb=True)
net.addLink( h3, s3, bw=5, delay='5ms',use_htb=True)
net.addLink( s1, s4, bw=100, delay='7.5ms',use_htb=True)
net.addLink( s1, s2, bw=100, delay='7.5ms',use_htb=True)
net.addLink( s2, s3, bw=100, delay='7.5ms',use_htb=True)
net.addLink( s2, s4, bw=100, delay='7.5ms',use_htb=True)
print "**** Adding Remote controller from 192.168.56.1:6653****"

# Add controller
odl_c = net.addController('c0',controller=RemoteController,ip='192.168.56.1', port=6653)
net.build()

s1.start([odl_c])
s4.start([odl_c])
s3.start([odl_c])
s2.start([odl_c])
# Bring up the mininet CLI
CLI(net) 
net.stop()

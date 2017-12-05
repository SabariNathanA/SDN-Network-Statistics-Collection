__author__ = 'Maneesha'
from mininet.node import CPULimitedHost
from mininet.topo import Topo
from mininet.net import Mininet
from mininet.log import setLogLevel, info
from mininet.node import RemoteController
from mininet.cli import CLI
"""
Instructions to run the topo:
    1. Go to directory where this fil is.
    2. run: sudo -E python Simple_Pkt_Topo.py.py

The topo has 2 switches and 4 hosts. They are connected in a star shape.
"""


class SimplePktSwitch(Topo):
    """Simple topology example."""

    def __init__(self, **opts):
        """Create custom topo."""

        # Initialize topology
        # It uses the constructor for the Topo cloass
        super(SimplePktSwitch, self).__init__(**opts)

        # Add hosts and switches
	net = Mininet(link=TCLink)
        h1 = self.addHost('h1')
	h2 = self.addHost('h2')
	h3 = self.addHost('h3')
	h4 = self.addHost('h4')
	h5 = self.addHost('h5')
	h6 = self.addHost('h6')
	h7 = self.addHost('h7')
	h8 = self.addHost('h8')
	net.build()
	h1.cmd("ifconfig h1-eth0 0")
	h2.cmd("ifconfig h2-eth0 0")
	h3.cmd("ifconfig h3-eth0 0")
	h4.cmd("ifconfig h4-eth0 0")
	h5.cmd("ifconfig h5-eth0 0")
	h6.cmd("ifconfig h6-eth0 0")
	h7.cmd("ifconfig h7-eth0 0")
	h8.cmd("ifconfig h8-eth0 0")
	
	
       	
	
	
        # Adding switches
        s1 = self.addSwitch('s1', dpid="0000000000000001")
        s2 = self.addSwitch('s2', dpid="0000000000000002")
        

        # Add links
        self.addLink(h1, s1)
	self.addLink(h2, s1)
	self.addLink(h3, s1)
        self.addLink(h4, s1)
	self.addLink(h5, s2)
	self.addLink(h6, s2)
	self.addLink(h7, s2)
        self.addLink(h8, s2)
	self.addLink(s1, s2)
	
	s1.cmd("vconfig add s1-eth0 100")
	s1.cmd("vconfig add s1-eth1 200")
	
	s2.cmd("vconfig add s2-eth0 100")
	s2.cmd("vconfig add s2-eth1 200")
	
	s1.cmd("brctl addif brvlan100 s1-eth0")
	s1.cmd("brctl addif brvlan200 s1-eth1")
	s2.cmd("brctl addif brvlan100 s2-eth0")
	s2.cmd("brctl addif brvlan200 s2-eth1")
	s1.cmd("ifconfig brvlan100 up")
	s1.cmd("ifconfig brvlan200 up")
	s2.cmd("ifconfig brvlan100 up")
	s2.cmd("ifconfig brvlan200 up")
	h1.cmd("ifconfig h1-eth0 10.0.10.1 netmask 255.255.255.0")

 	h2.cmd("ifconfig h2-eth0 10.0.10.2 netmask 255.255.255.0")

 	h3.cmd("ifconfig h3-eth0 10.0.20.3 netmask 255.255.255.0")

  	h4.cmd("ifconfig h4-eth0 10.0.20.4 netmask 255.255.255.0")
	h5.cmd("ifconfig h5-eth0 10.0.10.5 netmask 255.255.255.0")

 	h6.cmd("ifconfig h6-eth0 10.0.10.6 netmask 255.255.255.0")

 	h7.cmd("ifconfig h7-eth0 10.0.20.7 netmask 255.255.255.0")

  	h8.cmd("ifconfig h8-eth0 10.0.20.8 netmask 255.255.255.0")



def run():
    c = RemoteController('c', '192.168.56.1', 6633)
    net = Mininet(topo=SimplePktSwitch(), host=CPULimitedHost, controller=None)
    net.addController(c)
    net.start()

    CLI(net)
    net.stop()

# if the script is run dire																																																																																																																																																																	ctly (sudo custom/optical.py):
if __name__ == '__main__':
    setLogLevel('info')
    run()
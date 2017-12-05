from mininet.node import Host,Controller,RemoteController
from mininet.topo import Topo
from mininet.util import quietRun
from mininet.log import error
from mininet.net import Mininet


class VLANHost( Host ):
    "Host connected to VLAN interface"

    def config( self, vlan=100, **params ):
        r = super( VLANHost, self ).config( **params )

        intf = self.defaultIntf()
        # remove IP from default, "physical" interface
        self.cmd( 'ifconfig %s inet 0' % intf )

        # create VLAN interface
        self.cmd( 'vconfig add %s %d' % ( intf, vlan ) )

        # assign the host's IP to the VLAN interface
        self.cmd( 'ifconfig %s.%d inet %s' % ( intf, vlan, params['ip'] ) )

        # update the intf name and host's intf map
        newName = '%s.%d' % ( intf, vlan )

        # update the (Mininet) interface to refer to VLAN interface name
        intf.name = newName

        # add VLAN interface to host's name to intf map
        self.nameToIntf[ newName ] = intf

        return r

hosts = { 'vlan': VLANHost }

def runTopo():

    net = Mininet( topo=None,build=False )
    c0=net.addController(name='c0',
                      controller=RemoteController,
                      ip='192.168.56.1',
                      port=6633)

    print "******* Adding switches **********"
    s1 = net.addSwitch( 's1' )
    s2 = net.addSwitch( 's2' )
    print "******* Adding Hosts of first vlan **********"
    h1s1v1 = net.addHost( 'h1s1v1', cls=VLANHost,mac='00:00:00:00:00:01', vlan=100 )
    h2s1v1 = net.addHost( 'h2s1v1', cls=VLANHost,mac='00:00:00:00:00:02' ,vlan=100 )
    h1s2v1 = net.addHost( 'h1s2v1', cls=VLANHost, mac='00:00:00:00:00:03',vlan=100 )
    h2s2v1 = net.addHost( 'h2s2v1', cls=VLANHost, mac='00:00:00:00:00:04',vlan=100 )

    print "******* Adding hosts of first vlan  **********"
    h3s2v2 = net.addHost( 'h3s2v2', cls=VLANHost, mac='00:00:00:00:00:05',vlan=200 )
    h4s2v2 = net.addHost( 'h4s2v2', cls=VLANHost, mac='00:00:00:00:00:06',vlan=200 )
    h3s1v2 = net.addHost( 'h3s1v2', cls=VLANHost, mac='00:00:00:00:00:07',vlan=200 )
    h4s1v2 = net.addHost( 'h4s1v2', cls=VLANHost, mac='00:00:00:00:00:08',vlan=200 )

    print "******* Adding links **********"
    net.addLink( h1s1v1, s1 )
    net.addLink( h2s1v1, s1 )
    net.addLink( h3s1v2, s1 )
    net.addLink( h4s1v2, s1 )
    net.addLink( h1s2v1, s2 )
    net.addLink( h2s2v1, s2 )
    net.addLink( h3s2v2, s2 )
    net.addLink( h4s2v2, s2 )
    net.addLink(s1,s2)
    net.start()
    CLI( net )
    net.stop()


if __name__ == '__main__':
    import sys
    from functools import partial

    from mininet.net import Mininet
    from mininet.cli import CLI
    from mininet.topo import SingleSwitchTopo
    from mininet.log import setLogLevel,info
    runTopo()

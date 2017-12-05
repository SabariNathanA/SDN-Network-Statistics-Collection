from mininet.node import Host,Controller,RemoteController
from mininet.topo import Topo
from mininet.net import Mininet

def runTopo():

    net = Mininet( topo=None,build=False )
    s1 = net.addSwitch( 's1' )
    s2 = net.addSwitch( 's2' )
    h1s1v1 = net.addHost( 'h1s1v1', mac='00:00:00:00:00:01',)
    h2s1v1 = net.addHost( 'h2s1v1', mac='00:00:00:00:00:02'  )
    h1s2v1 = net.addHost( 'h1s2v1', mac='00:00:00:00:00:03' )
    h2s2v1 = net.addHost( 'h2s2v1', mac='00:00:00:00:00:04' )
    h3s2v2 = net.addHost( 'h3s2v2', mac='00:00:00:00:00:05' )
    h4s2v2 = net.addHost( 'h4s2v2', mac='00:00:00:00:00:06' )
    h3s1v2 = net.addHost( 'h3s1v2',  mac='00:00:00:00:00:07')
    h4s1v2 = net.addHost( 'h4s1v2', mac='00:00:00:00:00:08' )
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
    from mininet.net import Mininet
    from mininet.cli import CLI
    from mininet.topo import SingleSwitchTopo
    from mininet.log import setLogLevel,info
    runTopo()

from mininet.topo import Topo

from mininet.link import TCLink

class MyTopo( Topo ):
	"Simple topology example."

	def __init__( self ):
		"Create custom topo."

		# Initialize topology
		Topo.__init__( self )

		# Add hosts and switches
		h1 = self.addHost( 'h1' )
		h2 = self.addHost( 'h2' )
		h3 = self.addHost( 'h3' )
		s1 = self.addSwitch( 's1' )
		s2 = self.addSwitch( 's2' )
		s3 = self.addSwitch( 's3' )
		s4 = self.addSwitch( 's4' )

		# Add links
		self.addLink( h1, s1, bw=10, delay='5ms', loss=10, max_queue_size = 10000 )
		self.addLink( h2, s2, bw=10, delay='5ms', loss=10, max_queue_size = 10000 )
		self.addLink( h3, s3, bw=10, delay='5ms', loss=10, max_queue_size = 10000 )
		self.addLink( s1, s4, bw=10, delay='5ms', loss=10, max_queue_size = 10000 )
		self.addLink( s1, s2, bw=10, delay='5ms', loss=10, max_queue_size = 10000 )
		self.addLink( s2, s3, bw=10, delay='5ms', loss=10, max_queue_size = 10000 )
		self.addLink( s2, s4, bw=10, delay='5ms', loss=10, max_queue_size = 10000 )
topos = { 'h3s4': ( lambda: MyTopo() ) }
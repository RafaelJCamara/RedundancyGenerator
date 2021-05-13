#!/usr/bin/env python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call

def myNetwork():

    net = Mininet( topo=None,
                   build=False,
                   ipBase='192.168.0.0/16')

    info( '*** Adding controller\n' )
    info( '*** Add switches\n')
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch, failMode='standalone')
    s2 = net.addSwitch('s2', cls=OVSKernelSwitch, failMode='standalone')
    s3 = net.addSwitch('s3', cls=OVSKernelSwitch, failMode='standalone')
    s4 = net.addSwitch('s4', cls=OVSKernelSwitch, failMode='standalone')
    s5 = net.addSwitch('s5', cls=OVSKernelSwitch, failMode='standalone')
    s6 = net.addSwitch('s6', cls=OVSKernelSwitch, failMode='standalone')
    s7 = net.addSwitch('s7', cls=OVSKernelSwitch, failMode='standalone')
    s8 = net.addSwitch('s8', cls=OVSKernelSwitch, failMode='standalone')
    s9 = net.addSwitch('s9', cls=OVSKernelSwitch, failMode='standalone')
    s10 = net.addSwitch('s10', cls=OVSKernelSwitch, failMode='standalone')

    info( '*** Add hosts\n')
    h1 = net.addHost('h1', cls=Host)
    h2 = net.addHost('h2', cls=Host)
    h3 = net.addHost('h3', cls=Host)
    h4 = net.addHost('h4', cls=Host)
    h5 = net.addHost('h5', cls=Host)
    h6 = net.addHost('h6', cls=Host)

    info( '*** Add links\n')
    net.addLink(h1, s1)
    net.addLink(h2, s2)
    net.addLink(h3, s3)
    net.addLink(h4, s4)
    net.addLink(h5, s5)
    net.addLink(h6, s6)
    net.addLink(s2, s1)
    net.addLink(s3, s1)
    net.addLink(s3, s2)
    net.addLink(s4, s1)
    net.addLink(s4, s2)
    net.addLink(s4, s3)
    net.addLink(s5, s1)
    net.addLink(s5, s2)
    net.addLink(s5, s3)
    net.addLink(s5, s4)
    net.addLink(s6, s1)
    net.addLink(s6, s2)
    net.addLink(s6, s3)
    net.addLink(s6, s4)
    net.addLink(s6, s5)

    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    net.get('s1').start([])
    net.get('s2').start([])
    net.get('s3').start([])
    net.get('s4').start([])
    net.get('s5').start([])
    net.get('s6').start([])
    net.get('s7').start([])
    net.get('s8').start([])
    net.get('s9').start([])
    net.get('s10').start([])


    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()


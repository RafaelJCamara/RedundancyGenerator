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
    c0 = net.addController(name='c0',
                           controller=Controller,
                           protocol='tcp',
                           port=6633)

    info( '*** Add switches\n')
    l1 = net.addSwitch('l1', cls=OVSKernelSwitch, failMode='standalone')
    l2 = net.addSwitch('l2', cls=OVSKernelSwitch, failMode='standalone')
    l3 = net.addSwitch('l3', cls=OVSKernelSwitch, failMode='standalone')
    l4 = net.addSwitch('l4', cls=OVSKernelSwitch, failMode='standalone')
    l5 = net.addSwitch('l5', cls=OVSKernelSwitch, failMode='standalone')
    l6 = net.addSwitch('l6', cls=OVSKernelSwitch, failMode='standalone')
    c1 = net.addSwitch('c1', cls=OVSKernelSwitch, failMode='standalone')
    c2 = net.addSwitch('c2', cls=OVSKernelSwitch, failMode='standalone')
    c3 = net.addSwitch('c3', cls=OVSKernelSwitch, failMode='standalone')
    c4 = net.addSwitch('c4', cls=OVSKernelSwitch, failMode='standalone')

    info( '*** Add hosts\n')
    h1 = net.addHost('h1', cls=Host)
    h2 = net.addHost('h2', cls=Host)
    h3 = net.addHost('h3', cls=Host)
    h4 = net.addHost('h4', cls=Host)
    h5 = net.addHost('h5', cls=Host)
    h6 = net.addHost('h6', cls=Host)

    info( '*** Add links\n')
    net.addLink(h1, l1)
    net.addLink(h2, l2)
    net.addLink(h3, l3)
    net.addLink(h4, l4)
    net.addLink(h5, l5)
    net.addLink(h6, l6)
    net.addLink(l1, c1)
    net.addLink(l1, c2)
    net.addLink(l1, c3)
    net.addLink(l1, c4)
    net.addLink(l2, c1)
    net.addLink(l2, c2)
    net.addLink(l2, c3)
    net.addLink(l2, c4)
    net.addLink(l3, c1)
    net.addLink(l3, c2)
    net.addLink(l3, c3)
    net.addLink(l3, c4)
    net.addLink(l4, c1)
    net.addLink(l4, c2)
    net.addLink(l4, c3)
    net.addLink(l4, c4)
    net.addLink(l5, c1)
    net.addLink(l5, c2)
    net.addLink(l5, c3)
    net.addLink(l5, c4)
    net.addLink(l6, c1)
    net.addLink(l6, c2)
    net.addLink(l6, c3)
    net.addLink(l6, c4)

    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    net.get('l1').start([c0])
    net.get('l2').start([c0])
    net.get('l3').start([c0])
    net.get('l4').start([c0])
    net.get('l5').start([c0])
    net.get('l6').start([c0])
    net.get('c1').start([c0])
    net.get('c2').start([c0])
    net.get('c3').start([c0])
    net.get('c4').start([c0])


    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()


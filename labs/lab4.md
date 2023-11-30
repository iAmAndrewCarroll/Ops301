### Lab 4

Marco provided the following in lecture

Wiring
- Marco used a crossover connection between routers
 - 0/1 to 0/1 on the routers
- Marco used a straight through connection between the router and the switch and the switch and the client and the other switch and the "google" server
- PC-A
  - IP Address: 192.168.100.10
  - Subnet: 255.255.255.0
  - Default Gateway: 192.168.100.1
- Server
  - IP Address: 192.168.200.10
  - Subnet:
  - Default Gateway:  
- Router 1
  - `no`
  - Router>`enable`
  - Router#`configure terminal`
  - Router(config)#`hostname INTERNAL`
  - Router(config)#`interface fa0/0`
  - Router(config-if)#`no shutdown`
  - Router(config-if)#`ip address 192.168.100.1 255.255.255.0`
  - Router(config-if)#`interface fa0/1`
  - Router(config-if)#`no shutdown`
  - Router(config-if)#`ip address 156.12.1.6 255.255.255.252`
  - Router(config-if)#`exit`
  - Router(config)#`router bgp 65000`
    - 65000 is the AS number
  - Router(config-router)#`bgp log-neighbor-changes`
  - Router(config-router)#`neighbor 156.12.1.5 remote-as 10000`
    - 10000 is the AS number of the other router
    - BGP 5 ADJChange - neighbor is up confirmation message
  - Router(config-router)#`network 192.168.100.0 mask 255.255.255.0`
    - this is the network that we are advertising to the other router
    - after this step exit all the way out and enter
      - Router#`show ip bgp`
        - this will show the routes that are being advertised
    - **router bgp 65000** will take you back into the proper config after exiting for the `show ip bgp` command

- Router 2
  - `no`
  - Router>`enable`
  - Router#`configure terminal`
  - Router(config)#`hostname CLOUD`
  - CLOUD(config)#`interface f0/0`
  - CLOUD(config-if)#`no shutdown`
  - CLOUD(config-if)#`ip address 192.168.200.1 255.255.255.0`
  - CLOUD(config-if)#`interface f0/1`
  - CLOUD(config-if)#`no shutdown`
  - CLOUD(config-if)#`ip address 156.12.1.5 255.255.255.252`
  - CLOUD(config-if)#`exit`
  - CLOUD(config)#`router bgp 10000`
    - 10000 is the AS number
  - CLOUD(config-router)#`bgp log-neighbor-changes`
  - CLOUD(config-router)#`neighbor 156.12.1.6 remote-as 65000`
    - 65000 is the AS number of the other router
    - BGP 5 ADJChange - neighbor is up confirmation message
  - CLOUD(config-router)#`network 192.168.200.0 mask 255.255.255.0`
    - this is the network that we are advertising to the other router
    - after this step exit all the way out and enter
      - CLOUD#`show ip bgp`
        - this will show the routes that are being advertised
    - **router bgp 10000** will take you back into the proper config after exiting for the `show ip bgp` command


# Reading 6

[Resources: Network Address Translation](https://www.geeksforgeeks.org/network-address-translation-nat/)

**1. What is the main purpose for implementing NAT on a network?**
- The main purpose of implementing NAT (Network Address Translation) on a network is to allow multiple devices within a private network to share a single public IP address when accessing the Internet. It helps conserve public IP addresses and provides a layer of security by hiding the internal network structure.

**2. At what layer of the OSI model does NAT happen?**
- NAT primarily operates at the Network Layer (Layer 3) of the OSI model. It involves translating IP addresses (both source and destination) in the packet headers, which is a function of the Network Layer.

**3. What happens to packets when NAT runs out of addresses in the pool of available IPs?**
- When NAT runs out of addresses in the pool of available IPs, it will drop incoming packets. If there are no more available addresses in the pool, the NAT device cannot assign a public IP to a new internal device trying to access the Internet. This situation can lead to connectivity issues for that device.

**4. What disadvantage does using NAT pose for routers?**
- The disadvantage of using NAT for routers is that it introduces delays in the switching path. NAT involves rewriting IP addresses and port numbers in packets, which adds processing overhead. Additionally, certain applications and protocols may not work correctly with NAT enabled, and it can complicate the implementation of tunneling protocols like IPsec, as routers are primarily designed to work at the network layer and not tamper with transport layer (port) information.

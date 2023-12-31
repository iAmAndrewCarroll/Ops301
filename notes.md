### Day 1

### Layers of the OSI Model:

1. **Physical Layer (Layer 1)**: Responsible for physical connections, synchronization of bits, transmission rate, physical topologies, and transmission modes.
2. **Data Link Layer (Layer 2)**: Ensures error-free data transfer between nodes, framing, physical addressing (MAC addresses), error control, flow control, and access control.
3. **Network Layer (Layer 3)**: Handles data transmission between hosts in different networks, routing, logical addressing (IP addresses), and selecting the best path for data transmission.
4. **Transport Layer (Layer 4)**: Provides end-to-end delivery of data segments, acknowledgment, error handling, segmentation, reassembly, and uses port numbers for communication.
5. **Session Layer (Layer 5)**: Establishes, maintains, and terminates connections, synchronizes data, and controls dialog between systems.
6. **Presentation Layer (Layer 6)**: Translates and manipulates data formats for transmission, including encryption, decryption, and compression.
7. **Application Layer (Layer 7)**: Where network applications operate, producing data for transfer, offering access to the network, and displaying received information.


| # | Layer | Address Type | Data Type | Devices/Protocols | Mnemonic |
| - | ----- | ------------ | --------- | -------- | -------- |
| 7 | Application | | | HTTP, FTP, DNS, DHCP, Computer | Away |
| 6 | Presentation | | | ASCII, JPEG/GIF/PNG, Computer (Format) | Pizza |
| 5 | Session | | | SMB, SIP, Computer | Sausage |
| 4 | Transport | Logical Port Number | Segments | TCP, UDP, Gateway, Load Balancer | Throw |
| 3 | Network | IP Address (197.168.1.1) | Packets | Router, L3 Switch (VLAN) | Not |
| 2 | Data Link | MAC Address (00:0a:95:9d:68:16) | Frame (group of bits) | L2 Switch, Bridge | Do |
| 1 | Pysical | Physical Port ID (P1, P7, etc) | Bits (0s and 1s) | Cables, Hubs, Repeaters, NICs, etc | Please |

**Full Mnemonic: Please Do Not Throw Sausage Pizza Away**
**4-1 Data Type Mnemonic: Some People Fear Birthdays (Segments, Packets, Frames, Bits)**
**4-1 Address Type Acronym: LIMP (Logical, IP, MAC, Physical)**
<br>
**Layer 1-3 are hardware/physical layers**
<br>
**Layer 4-7 are software/protocol layers**
<br>
**Layer 5-7 do not have specific Address or Data Types associated with them**
<br>
![Layer 1](note-media/layer1.png)
![Layer 2](note-media/layer2.png)
![Layer 3](note-media/layer3.png)
![Layer 4](note-media/layer4.png)
![Layer 5](note-media/layer5.png)
![Layer 6](note-media/layer6.png)
![Layer 7](note-media/layer7.png)


**Some Port Stuff**
Port 22: Logical port for SSH
Port 80: Logical port for HTTP
Port 443: Logical port for HTTPS

**1. List and describe the ports used for the following:**

| Service                   | Description                                                    | Protocol | Port(s) | Additional Info                                    |
|---------------------------|----------------------------------------------------------------|----------|---------|----------------------------------------------------|
| DHCP                      | Dynamic Host Configuration Protocol, assigns IP addresses     | UDP      | 67, 68  |                                                    |
| DNS                       | Domain Name System, translates domain names to IP addresses   | UDP      | 53      |                                                    |
| FTP                       | File Transfer Protocol, used for file transfers               | TCP      | 20, 21  | Data and control channels                         |
| HTTPS                     | HyperText Transfer Protocol Secure, sends/receives web pages  | TCP      | 443     | Encrypted                                          |
| HTTP                      | HyperText Transfer Protocol, sends/receives web pages         | TCP      | 80      | Unencrypted                                        |
| ICMP (Ping)               | ICMP, test connectivity to remote computer                   | ICMP     | Type 8  | Typically on port 0; blocked by firewalls          |
| NTP                       | Network Time Protocol, synchronizes system clocks            | UDP      | 123     |                                                    |
| RDP                       | Remote Desktop Protocol, view/control remote computer        | TCP      | 3389    | Encrypted                                          |
| SMB                       | Server Message Block, file and printer sharing                | TCP      | 445     | Commonly used in Windows file sharing              |
| SMTP                      | Simple Mail Transfer Protocol, sends email messages           | TCP      | 25      | Typically plaintext; SMTPS uses TLS on 587/465   |
| SFTP                      | SSH File Transfer Protocol, secure file transfers             | TCP      | 22      | Encrypted                                          |
| SSH                       | Secure Shell, secure remote access                             | TCP      | 22      | All traffic is encrypted, more secure than Telnet |
| Telnet                    | Telecommunication Network Protocol, allows remote access      | TCP      | 23      | Has security issues                               |



**TCP Handshake**
![TCP Handshake](note-media/tcphandshake.png)
Step 1: SYN (synchronize) - Client sends a SYN packet to the server to initiate a connection.
Step 2: SYN-ACK (synchronize-acknowledge) - Server responds with a SYN-ACK packet to acknowledge the request.
Step 3: ACK (acknowledge) - Client sends an ACK packet to acknowledge the server's response.

### Day 2

**Date Scripting**

**Don't forget your shebang!**
`#!/bin/bash`

**Date and Time Format Codes:**

| Format | Description                                       | Example     |
|--------|---------------------------------------------------|-------------|
| %Y     | Year (4-digit)                                    | 2023        |
| %m     | Month (01-12)                                     | 03          |
| %d     | Day of the month (01-31)                          | 15          |
| %H     | Hour (00-23)                                      | 14          |
| %M     | Minute (00-59)                                    | 45          |
| %S     | Second (00-59)                                    | 22          |
| %A     | Full weekday name (e.g., Sunday)                   | Monday      |
| %B     | Full month name (e.g., January)                   | September   |

**Shell Commands and Variables:**

| Command/Variable                     | Description                                     | Example                      |
|--------------------------------------|-------------------------------------------------|------------------------------|
| `echo $date`                          | Prints the date                                 | (Output varies)              |
| `year=$(date +%Y)`                    | Assigns the year to a variable                 | `$year` contains the year    |
| `month=$(date +%m)`                   | Assigns the month to a variable                | `$month` contains the month  |
| `day=$(date +%d)`                     | Assigns the day to a variable                  | `$day` contains the day      |
| `echo "Today is $month/$day/$year"`    | Prints the date in the format of MM/DD/YYYY    | Today is 03/15/2023          |
| `echo "Current Date: $(date +%m/%d/%Y)"` | Prints the date in the format of MM/DD/YYYY  | Current Date: 03/15/2023     |


**Append to a file**
`echo "Today is $month/$day/$year" >> test-date.txt` - appends the date to the test-date.txt file
`mv test-date.txt test-date-$(date +%m-%d-%Y).txt` - renames the file to include the date

**Types of Protocols and Ports I need to know to pass CompTia Network+**

**2. List of Protocols with Descriptions and Port Information:**

| Protocol               | Description                                     | Connection Type    | Associated Ports (if any)                   |
|------------------------|-------------------------------------------------|--------------------|--------------------------------------------|
| ICMP (Internet Control Message Protocol) | Used for network diagnostics and error reporting. | Connectionless    | N/A                                        |
| UDP (User Datagram Protocol)            | Provides a connectionless and lightweight communication mechanism. | Connectionless    | Various, e.g., DNS (53), NTP (123)         |
| TCP (Transmission Control Protocol)    | Provides reliable, connection-oriented communication. | Connection-oriented | Various, e.g., SSH (22), HTTP (80)        |
| IP (Internet Protocol)                 | A fundamental protocol for routing packets across networks. | N/A                | N/A                                        |
| Connection-oriented vs Connectionless   | Indicates whether a protocol establishes a connection before data transfer (connection-oriented) or sends data without establishing a connection (connectionless). | N/A | N/A                                      |

**Network Enumeration**

Port Scanning: The process of sending packets to specific ports on a host and analyzing the responses to learn more about the host and its services.  Can tell us what ports are open, what services are running, and what operating system is running, and IP addresses of other hosts on the network.

Network Enumeration uses further techniques to gather information about a network, such as:

- DNS zone transfers: A DNS zone transfer is the process of copying DNS data from a master DNS server to a slave DNS server.  This allows the slave server to have an exact copy of the DNS records from the master server.  This is useful for load balancing and redundancy.
- SNMP queries: Simple Network Management Protocol (SNMP) is a protocol for monitoring and managing network devices.  SNMP queries can be used to gather information about network devices, such as routers, switches, and printers.
- NetBIOS queries: NetBIOS is a protocol that allows applications on different computers to communicate within a local area network (LAN).  NetBIOS queries can be used to gather information about Windows computers on a network.
- LDAP queries: Lightweight Directory Access Protocol (LDAP) is a protocol for accessing and maintaining directory services over an IP network.  LDAP queries can be used to gather information about users, groups, and computers on a network.
- NTP queries: Network Time Protocol (NTP) is a protocol for synchronizing the clocks of computers over a network.  NTP queries can be used to gather information about the time and date of computers on a network.
- SMTP queries: Simple Mail Transfer Protocol (SMTP) is a protocol for sending email messages.  SMTP queries can be used to gather information about email servers on a network.

**Nmap Security Scanner:** A free and open-source network scanner used to discover hosts and services on a computer network by sending packets and analyzing the responses.  It can be used for network inventory, managing service upgrade schedules, and monitoring host or service uptime.
- Enumerate hosts on a network
- Enumerate ports open on a host
- Operate more discreetly or aggressively
- Perform service fingerprinting to determine waht software (OS or apps) might be running on the target host

**Nmap Syntax**

`nmap [options] {target specification}`
![Nmap Syntax](note-media/Nmap-Cheat-Sheet.png)

### Day 3

**chmod options (permissions)**

| Command           | Value | Numeric Value | Effect                 |
|-------------------|-------|---------------|------------------------|
| `chmod +r file`   | r     | 4             | Add read permission    |
| `chmod +w file`   | w     | 2             | Add write permission   |
| `chmod +x file`   | x     | 1             | Add execute permission |
| `chmod -r file`   | r     | 4             | Remove read permission |
| `chmod -w file`   | w     | 2             | Remove write permission|
| `chmod -x file`   | x     | 1             | Remove execute permission|
| `chmod 755 file`  | rwx   | 7             | Owner: rwx, Group: r-x, Others: r-x |
| `chmod 644 file`  | rw-   | 6             | Owner: rw-, Group: r--, Others: r-- |
| `chmod 600 file`  | rw-   | 6             | Owner: rw-, Group: ---, Others: --- |

permissions: rwxrwxrwx (owner, group, others)

you can set folder/dir level permissions and then also set permissions for specific files within the folder/dir.  A folder might have full rwx permissions but a sensitive file may only have rw permissions or even no permissions for the group or others.

**Subnetting**

Network: is a logical collection of contiguous IP addresses that share the same network ID.  A network is also known as a subnet.

Subnet: is literally a "sub-network", a netwrok inside a larger network

IP Address: includeds two parts
- Network ID: identifies the network. The network ID is the same for all hosts within the network.
- Host ID: identifies the host. The host ID is unique within the network.

Subnetting involves "borrowing" bits from the Host ID and adding them to the Network ID.

Subnetting: logically breakin an addressable block of IP addresses into mulitple, smaller addressable blocks

![subnetting](note-media/subnetting.jpeg)
![subnetting](note-media/subnet.jpeg)

Subnet Mask: is a 32-bit number that identifies the network ID and host ID of an IP address.  It is used to determine whether a host is on the local network or a remote network.
- Also known as a netmask, indicates which bits are "masked" to find the Host ID.
- Example: 255.255.255.0 in Decimal or 11111111.11111111.11111111.00000000 in Binary

CIDR Notation: is a shorthand notation for representing a subnet mask.  It is used to indicate the number of bits in the subnet mask.
- represents the number of binary bits (counted from left to right) which belong to the Network ID

Example:
- IP Address: 185.210.25.69/24
- Subnet Mask: 255.255.255/0
- Network ID: 185.210.25
- Host ID: 69
- Network (Subnet ID): 185.210.25.0
- First Host IP Address: 185.210.25.1
- Last Host IP Address:: 185.210.25.254
- Broadcast Address: 185.210.25.255
- Next Network (Subnet ID): 185.210.26.0
- Valid Host IP Addresses: 254

Example Subnet Mask Math:
![subnet mask math](note-media/subnetmath.jpeg)

Another Example of Subnet Mask Math:
- IP: 20.196.214.18/22
- Subnet Mask: 255.255.252.0
- 11111111.11111111.11111100.00000000
- ......8..........16.......22        
- Size of Subnet: 256 - 252 = 4
- Subnet: 20.196.212.0
- First Host: 20.196.212.1
- Last Host: 20.196.215.254
- Broadcast: 20.196.215.255
- Next Subnet: 20.196.216.0
- Number of Subnets: 64
- Hosts per Subnet: 1022 
![subnet mask math](note-media/subnetmath2.jpeg)

**Network Segmentation**

Reasons to implement network segmentation:
- Performance
- Security
- Regulatory Compliance
  - NIST SP 800-53
  - NIST SP 800-171
  - and more...

Network Segmentation: the process of dividing a network into smaller networks, called subnets.  Each subnet is a separate network segment.

Interfaces can be the physical ethernet ports on a router, but can also be represented virtually.
- commonly the lowest number is WAN, the rest tend to be LAN. Configurable.
- x0 is WAN, x1 is LAN, x2 is LAN, etc.
- ens0, ens1, ens2, etc.
- We can use these interfaces to divide the netwrok using different subnets and DHCP scopes.

![segmentation](note-media/segment.jpeg)

Microsegmentation: the process of dividing a network into even smaller networks, called microsegments.  Each microsegment is a separate network segment.
- microsegmentation uses much more information in segmentation policies like application-layer information. It enables policies that are more granular and flexible to meet the highly-specific needs of an organization or business application. ~Cisco

![microsegmentation](note-media/switch.jpeg)

Segmentation Methods:
- Logical Semgentation relies on sofware or packet header info to separate netwrok traffic.
- examples: VLANs, VPNs, and tunnels
- VLAN: a virtual LAN that logically separates a physical LAN into multiple virtual LANs.  VLANs are commonly used to separate traffic from different departments or different security zones.

### Day 4

**Cisco Packet Tracer**

Switch CLI Commands to enable trunk
- `enable`
- `configure terminal`
- `interface gigabitethernet 0/1` or `interface FastEthernet 0/1`
  - 0/1 is the port number
- `switchport mode trunk`
- `end`
- `write memory`

Router Setup - (We need to setup the switch to router connection as a trunk)
- `enable`
- `configure terminal`
- `interface fastethernet 0/0`
- `no shutdown`
- `exit` 
  - moves up one level out of the interface and back to router config
- `interface fastethernet 0/0.10`
  - 0/0.10 is the subinterface
  - you will see fastethernet 0/0.10 state changed to up
- `encapsulation dot1q 10`
  - 10 is the VLAN ID
  - encapsulation dot1q makes sure that other networks don't receive the traffic specific for VLAN 10
- `ip address 192.168.10.1 255.255.255.0`
  - this is the IP address and subnet mask for the VLAN 10 interface
- `interface fa0/0.20`
  - 0/0.20 is the subinterface
  - you will see fastethernet 0/0.20 state changed to up
- `encapsulation dot1q 20`
  - 20 is the VLAN ID
- `ip address 192.168.20.1 255.255.255.0`
  - this is the IP address and subnet mask for the VLAN 20 interface
- `exit`

**Important:**  I forgot to setup the ports for the computers and the router on the switches.  I went back in and corrected the access ports so they were on the proper VLANs.  Now I can ping each computer even on different VLANs.

**Subnetting**

Given the ip address 37.104.171.223/13, find the network id/subnet, first IP, last IP, broadcast IP, next subnet, number of subnets, and number of hosts per subnet.

- Network ID/Subnet: 255.255.248.0.0
  - think of the 13 as 13 1s. Each 255 is 8 1s.  So it would be like 11111111.11111000.00000000.00000000.  
  - The 1s are valued as 128 64 32 16 8 4 2 1.  Here we have 5 1s in the second set.  128 + 64 + 32 + 16 + 8 = 248.  So the subnet mask is 255.248.0.0
  - You can also decide to subtract the smaller number from 255.  In this case the 0s are valued at 4 2 and 1.  4 + 2 + 1 = 7.  255 - 7 = 248.  So the subnet mask is 255.248.0.0
- How to find the subnet that fits the IP address 37.104.171.223/13
  - count subnets by 8s. .0 .8 .16 ... .96 .104 .112 ... .224 .232 .240 .248
  - Our IP fits in the .104-.112 subnet subset
  - This helps us find our first IP 37.104.0.1
  - Our next subnet is 37.112.0.0
- First IP: 37.104.0.1
- Last IP: 37.112.255.254 (subtract 1 from the Broadcast IP)
- Broadcast IP: 37.111.255.255 (will be the very last IP address in the "neighborhood")
- Next Subnet: 37.112.0.0
- Number of Subnets Fit: 32
  - 11111111.11111000.00000000.00000000
  - we only look at the octet where the change happens.  
  - we will use 2^5 power because there are 5 1s in the octet where the change happens
  - 2^5 = 32
- Number of Hosts per Subnet: 524,286
  - 2^19 = 524,288
    - 19 is the number of 0s in the last octet
    - 2^19 - 2 = 524,286
      - 2 is subtracted because the first and last IP addresses are reserved for the network and broadcast addresses
    - 524,286 is the number of hosts per subnet

IP Address: 219.41.245.178/28
Subnet Mask: 255.255.255.240
- the /28 tells us there are 28 1s in the subnet mask and 4 0s
  - the 0s are worth 8 4 2 1 = 15
  - 255 - 15 = 240
  - Subnet is 255.255.255.240
Subnet ID: 219.41.245.176
- 256 - 240 = 16
- IP address is 219.41.245.178
  - 178 / 16 = 11.125
  - round down to 11; 11 * 16 = 176
  - 176 is the subnet ID
  - 176 to 192 is the range of the subnet
First IP: 219.41.245.177
Last IP: 219.41.245.190
Broadcast IP: 219.41.245.191
Next Subnet: 219.41.245.192
- last subnet in the range found in the subnet ID range 
- here the subnet range was 176 to 192
Number of Subnets: 16
- 2^4 = 16
Hosts per Subnet: 14
- number of subnets minus 2
  - 16 - 2 = 14

![subnetting](note-media/subnet-math.jpeg)

**Network Topologies**
- Logical Topology: how devices appear connected to the user
  - Broadcast
  - Point to point

- Physical Topology: how devices are physically connected

| Physical Topology | Description | Pros | Cons | Common Usage |
|-------------------|-------------|------|------|--------------|
| Bus               | All devices are connected to a single cable. | - Affordable. <br> - Simple to set up. | - Single point of failure (if the cable fails, the entire network goes down). <br> - Only half-duplex communication (one-way traffic at a time). | Extremely rare in modern networks. |
| Star              | All devices are connected to a central hub or switch mimicing a client-server architecture. | - Easy to set up and manage. <br> - Highly scalable <br> - Centralized control. <br> - Fault isolation (if one cable or device fails, it doesn't affect others). | - Dependency on the central hub/switch (if it fails, the entire network goes down). | Common in home and small office networks. |
| Ring              | Devices are connected in a circular fashion. | - Equal access to the network for all devices. <br> - No collisions in data transmission. | - Hard to scale. <br> - Single ring is half-duplex <br> - Single point of failure (if one device or cable fails, it can disrupt the entire ring). | Less common in modern networks due to its susceptibility to disruption. |
| Mesh              | Each device is connected to every other device. | - High redundancy (multiple paths for data to travel). <br> - Fault tolerance (if one link fails, data can still find an alternate route). | - High cabling and configuration complexity. <br> - Costly to implement in large networks. | Common in critical infrastructure networks (e.g., data centers, telecommunications). |
| Hybrid            | Combines two or more different physical topologies. | - Combines the strengths of multiple topologies. <br> - Provides flexibility. | - Increased complexity in design and management. | Common in larger enterprise networks that require different topologies for different segments. |

Wireless Topologies:
- Mesh
  - All devices are connected to every other device.
- Ad Hoc
  - Direct wireless connection between two devices.  Many printers can do this.
- Infrastructure
  - Devices are connected to a central access point (AP).  This is the most common wireless topology.  Access points broadcasts an SSID and you connect to it.

**Routing Protocols**

Static Routing: having predefined single path to the destination saved to your router that takes precedence over dynamic routs

Default Routing: Usually used in small networks, defauls is a manually defined path to take when not specific route can be determined

Dynamic Routing: Most common method of routing that calculates what route to take
- Convergence
- Accuracy

Routing Mechanism
- Autonomous System (AS)
  - private AS used for internal networks
  - public AS used for external networks like internet backbone
- Interior Gateway Protocol (IGP)
  - These protocols are what allow routers to communicate with each other within an AS
  - RIPv1, RIPv2 (Routing Information Protocol)
  -IGRP (Interior Gateway Routing Protocol)
  - OSPF (Open Shortest Path First)
- Exterior Gateway Protocols
  - BGP (Border Gateway Protocol)

Protocol Types
- Distance vector: uses distance as a metric value
  - RIP
    - Uses number of hops to make a decision (number of routers it has to go through to get to the server)
  - IGRP
- Link state: uses bandwidth as a metric value.  Works in a linked format and uses a complex metric table
  - OSPF (Open Shortest Path First) where shortest means fastest/shortest amount of time
  - IS-IS
- Hybrid: uses both distance and bandwidth as metric values
  - EIGRP (Enhanced Interior Gateway Routing Protocol)

**Day 6**

![Network Address Translation](note-media/nat.png)

pfSense VM
- Operating System: FreeBSD (64-bit)
- Base Mem: 1024
- 8 GB RAM

**Setting Up a New pfSense**
- Option 2 sets up the LAN/WAN interface
- 2 for LAN
  - Config IPv4 address LAN interface via DHCP? N
  - Enter the new LAN IPv4 address (this is a gateway address): 192.168.1.1
  - Enter the new LAN IPv4 subnet bit count (1 to 30): 24
  - For a LAN, press <ENTER> for none: <ENTER>
- Config IPv6 address for LAN interface via DHCP6? N
  - <ENTER> for none
- Do you want to enable the DHCP server on LAN? (y/n) `this sets the ip address range for the LAN`: Y
  - Enter the start address of the IPv4 client address range: 192.168.1.100
  - Enter the end address of the IPv4 client address range: 192.168.1.200
- Option 7 to ping google to verify internet connection: 8.8.8.8
**never be afraid to use option 4 to reset to factory defaults**

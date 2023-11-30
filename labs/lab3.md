### Lab 3

**Network Segmentation**

**Scenario**

Modern switches use virtual local-area networks (VLANs) to improve network performance by separating large Layer 2 broadcast domains into smaller ones. VLANs can also be used as a security measure by controlling which hosts can communicate. In general, VLANs make it easier to design a network to support the goals of an organization.

VLAN trunks are used to span VLANs across multiple devices. Trunks allow the traffic from multiple VLANS to travel over a single link, while keeping the VLAN identification and segmentation intact.

In this lab, you will create VLANs on both switches in the topology, assign VLANs to switch access ports, verify that VLANs are working as expected, and then create a VLAN trunk between the two switches to allow hosts in the same VLAN to communicate through the trunk, regardless of which switch the host is actually attached to.

[Download Cisco Packet tracer for your OS](https://skillsforall.com/resources/lab-downloads)

**Task 1: Build the Network and Configure Basic Device Settings**
![network topology](media/lab3-2-topology.png)

**Task 2: Configure VLANS and assign switch ports**
![vlan 10](media/lab3-3-vlan.png)
![vlan 20](media/lab3-6-vlan.png)

**Task 3: Configure Trunking**
![trunkS0](media/lab3-4-trunk.png)
![trunkS1](media/lab3-7-trunk.png)

**Other Visuals**
![pings](media/lab3-1-pings.png)
![access 0](media/lab3-5-access.png)
![access 1](media/lab3-8-access1.png)
![access 2](media/lab3-9-access2.png)

**Added Router With Screenshot of VLAN to VLAN Ping**

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
![router](media/lab3-10-router.png)

# Reading 4

**[Resource: VirtualBox Network Settings: Complete Guide](https://www.nakivo.com/blog/virtualbox-network-setting-guide/)**

**1. Which network mode in VirtualBox can be used to emulate unplugging the Ethernet cable from the network?**
- The network mode in VirtualBox that can emulate unplugging the Ethernet cable from the network is "Disconnected." When a VM is set to the Disconnected mode, it is effectively isolated from the network, similar to physically unplugging the Ethernet cable.

**2. Which network mode would be best if you wanted to run a server on a VM that could be fully accessible from your physical local area network?**
- If you want to run a server on a VM that should be fully accessible from your physical local area network (LAN), the best network mode to use in VirtualBox is "Bridged Adapter." Bridged Adapter mode connects the VM directly to your physical network, giving it its own unique IP address on the LAN. This allows other devices on your network to communicate with the VM as if it were a separate physical machine.

**3. What are the three options of promiscuous mode and what does each do?**
- In VirtualBox, there are three options for promiscuous mode, which control how a virtual network adapter handles network traffic:
   - **Deny**: In this mode, the virtual network adapter only receives packets specifically addressed to it. It does not see traffic intended for other VMs on the same network.
   - **Allow All**: In this mode, the virtual network adapter receives all network traffic on the physical network segment to which it is attached. This includes traffic intended for other VMs on the same network.
   - **Allow VMs**: This mode allows the virtual network adapter to receive network traffic for its own VM and any other VMs on the same network. It isolates VM traffic from the host's physical network traffic.

**4. What is Port Forwarding?**
- Port Forwarding is a networking technique used to redirect or forward network traffic from one port on a network device to another port on a different device. It is commonly used in VirtualBox and other virtualization environments to make services running on virtual machines accessible from the host system or the external network.
   - For example, if you have a web server running on a virtual machine within VirtualBox, you can set up port forwarding to allow external access to that web server. When a request is made to a specific port on the host system (e.g., port 80 for HTTP), the host system forwards that traffic to the corresponding port on the virtual machine where the web server is running. Port forwarding enables you to provide services hosted on VMs to the external network while maintaining network security and isolation.

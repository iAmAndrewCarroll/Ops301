# Reading 3

### [Resource: CIDR Block Notation Explained in 2 Minutes](https://medium.com/@acropoiesis/cidr-block-notation-explained-in-2-minutes-1010ec0dbc15)

**1. What is CIDR notation? What is a CIDR block?**
- CIDR notation is a way of representing IP address ranges efficiently. A CIDR block is simply a range of IP addresses.

**2. How many octets are found in an IPv4 address?**
- An IPv4 address consists of four octets.

**3. Setting binary aside and using the decimal system, what is the range of numbers found in an octet?**
- Using the decimal system, the range of numbers in an octet is from 0 to 255.

**4. What does the final digit after the “/” represent in an IPv4 address?**
- The final digit after the "/" in an IPv4 address represents how many bits make up the mask.

**5. How many IP addresses are in the CIDR block 10.0.0.0/24?**
- In the CIDR block 10.0.0.0/24, there are 256 IP addresses.


### [Resource: What is Network Segmentatino and Why It Matters](https://www.comptia.org/blog/security-awareness-training-network-segmentation)

**1. In your own words, describe network segmentation.**
- Network segmentation is a cybersecurity practice where different parts of a computer network are separated or segmented using devices like firewalls, switches, and routers. This separation helps improve security by isolating various network zones, making it more challenging for potential threats to move freely within the network.

**2. Network segmentation isn’t important as long as the network is using a well-configured firewall. Do you agree? Why or why not?**
- I don't agree that network segmentation isn't important as long as the network is using a well-configured firewall. While firewalls are essential for network security, they have their limitations. Firewalls primarily protect the perimeter of the network, but once a threat actor breaches this perimeter, they could move freely within the network. Network segmentation adds an extra layer of security by dividing the network into zones, limiting lateral movement, and preventing minor breaches from becoming major incidents. So, both firewalls and network segmentation are crucial for comprehensive network security.

**3. What is a screened subnet?**
- A screened subnet, also known as a DMZ (Demilitarized Zone) subnet, is a network zone that includes subnetworks exposing externally facing systems. These systems are often accessible via the internet and serve as a "handshake" area where external users interact with the network. The DMZ subnet separates these public-facing systems from the internal LAN (Local Area Network) and internal data that requires protection, helping to enhance network security.

**4. Cameras, ID card scanners, locked doors, and biometrics are just a few examples of what type of security?**
- Cameras, ID card scanners, locked doors, and biometrics are examples of physical security measures. Physical security focuses on protecting physical assets, facilities, and resources from unauthorized access, theft, vandalism, or damage. In the context of the article, it's highlighted that these physical security measures should be placed in their network zones to ensure their protection and segregation from other parts of the network.

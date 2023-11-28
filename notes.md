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

| Service   | Description                                                    | Protocol | Port    | Additional Info                                    |
|-----------|----------------------------------------------------------------|----------|---------|----------------------------------------------------|
| Telnet    | Telecommunication Network Protocol, allows remote access      | TCP      | 23      | Has security issues                               |
| SSH       | Secure Shell, secure remote access                             | TCP      | 22      | All traffic is encrypted, more secure than Telnet |
| DNS       | Domain Name System, translates domain names to IP addresses  | UDP      | 53      |                                                    |
| SMTP      | Simple Mail Transfer Protocol, sends email messages           | TCP      | 25      | Typically plaintext; SMTPS uses TLS on 587/465   |
| HTTP      | HyperText Transfer Protocol, sends/receives web pages         | TCP      | 80      | Unencrypted                                        |
| HTTPS     | HyperText Transfer Protocol Secure, sends/receives web pages  | TCP      | 443     | Encrypted                                          |
| RDP       | Remote Desktop Protocol, view/control remote computer        | TCP      | 3389    | Encrypted                                          |
| Ping      | ICMP, test connectivity to remote computer                   | ICMP     | Type 8  | Typically on port 0; blocked by firewalls          |


**TCP Handshake**
![TCP Handshake](note-media/tcphandshake.png)
Step 1: SYN (synchronize) - Client sends a SYN packet to the server to initiate a connection.
Step 2: SYN-ACK (synchronize-acknowledge) - Server responds with a SYN-ACK packet to acknowledge the request.
Step 3: ACK (acknowledge) - Client sends an ACK packet to acknowledge the server's response.

### Day 2

**Date Scripting**

**Don't forget your shebang!**
`#!/bin/bash`

`echo $date` - prints the date
`year=$(date +%Y)` - assigns the year to a variable
`month=$(date +%m)` - assigns the month to a variable
`day=$(date +%d)` - assigns the day to a variable

echo "Today is $month/$day/$year" - prints the date in the format of MM/DD/YYYY
echo "Current Date: $(date +%m/%d/%Y)" - prints the date in the format of MM/DD/YYYY

**Append to a file**
`echo "Today is $month/$day/$year" >> test-date.txt` - appends the date to the test-date.txt file
`mv test-date.txt test-date-$(date +%m-%d-%Y).txt` - renames the file to include the date


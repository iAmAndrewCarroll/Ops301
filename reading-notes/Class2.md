# Reading 2

### [Resource: What is a Port Scanner and How Does it Work?](https://www.varonis.com/blog/port-scanning-techniques)

**1. What is a port? Describe it with an analogy that would help a family member understand.**
   - A port in networking is like the gates at an airport. Imagine your computer is the airport, and it has many gates (ports). Each gate serves a specific purpose, just as ports allow different types of communication between devices. For example, port 80 might be the arrival gate to Rome where web traffic (HTTP) comes in, and port 22 could be a TSA checkpoint (SSH) for authorized access.

**2. What does a port scanner send to a port to check the current status?**
   - A port scanner sends a network request, similar to knocking on a door, to the specific TCP or UDP port it wants to check. It's like tapping on each door to see if someone responds on the other side.

**3. When a port scanner sends a request to connect, what are the three possible responses? Describe them.**
   - There are three possible responses when a port scanner sends a request:
     - Open, Accepted: It's like someone answering the door saying, "Hello, how can I help you?" The port is open and actively accepting connections.
     - Closed, Not Listening: This is similar to someone inside the house saying, "I'm sorry, but I'm not available right now." The port is closed and not actively accepting connections.
     - Filtered, Dropped, Blocked: It's like knocking on the door, but there's no response at all. The port doesn't even acknowledge the request, indicating it might be blocked by a firewall or some security measure.

**4. What is the difference between TCP and UDP?**
   - TCP (Transmission Control Protocol) and UDP (User Datagram Protocol) are two common communication protocols:
     - TCP is like sending a certified letter through the postal service. It ensures that your message arrives intact, in order, and you receive a confirmation when it's delivered. It's reliable but can be slower due to these checks.
     - UDP is like sending a postcard. It's faster because there's no guarantee of delivery, no confirmation, and no specific order. It's used for applications where speed is more important than guaranteed delivery, like live streaming or online gaming.

### [Resource: Common Ports](https://www.professormesser.com/network-plus/n10-008/n10-008-video/common-ports-n10-008/)

**1. List and describe the ports used for the following:**
- Telnet: Telecommunication Network Protocol, TCP port 23, allows you to view information on a remote computer. Has security issues.
- SSH: Secure Shell, TCP port 22, allows you to view information on a remote computer. More secure than Telnet as all traffic is encrypted.
- DNS: Domain Name System, UDP port 53, translates domain names to IP addresses.
- SMTP: Simple Mail Transfer Protocol, TCP port 25, sends email messages. Typically only for plaintext.  Most people are using a form of encrypted SMTP that uses TLS and that is commonly referred to as SMTPS and uses TCP port 587 or 465.
- HTTP: HyperText Transfer Protocol, TCP port 80, sends and receives web pages.  Unencrypted.
- HTTPS: HyperText Transfer Protocol Secure, TCP port 443, sends and receives web pages.  Encrypted.
- RDP: Remote Desktop Protocol, TCP port 3389, allows you to view and control a remote computer.  Encrypted.
- Ping: ICMP, ICMP type 8, allows you to test connectivity to a remote computer.  Unencrypted. Typically on port 0 and blocked by firewalls.

# Lab 1

### Part 1 - Deploy Kali Linux VM

Verify Internet Access
![Verify Internet Access](media/lab1-1.png)

### Part 2 - Traffic Capture

What is the difference between the various colors of packets that you see?
- The colors indicate the type of traffic. For example, green indicates TCP traffic, blue indicates UDP traffic, and black indicates other types of traffic.

The below image shows the packets captured when I visited [The CERN Website](http://info.cern.ch/) in order to run the HTTP Get process in Wireshark.
![Traffic Capture](media/lab1-5.png)

### Part 3 - TCP Analysis

How many segments are used here?
- TCP Segment Len: 422
![TCP Analysis](media/lab1-4.png)

What is the length in bytes of each segment?
- There are 422 bytes per segment.

Can You identify all three packets involved in the TCP three-way handshake? Include a screenshot of them.
- Lines 3, 4, and 5 are the three packets involved in the TCP three-way handshake as noted by the SYN, SYN/ACK, and ACK flags.
![TCP Handshake](media/lab1-5.png)

How much data is typically acknowledged per ACK?
- 54 or 60 bytes

### Part 4 - HTTP Analysis

HTTP Get method on the scan from [CERN](http://info.cern.ch/)
![HTTP Analysis](media/lab1-6.png)

Common HTTP headers: Host, User-Agent, Accept, Accept-Encoding, Accept-Language,
![Common HTTP Headers](media/lab1-7.png)

### Part 5 - Wrapup
Search [Indeed](https://www.indeed.com/) for Wireshark
- 1,763 jobs, varying titles and duties, wide range of compensation

Why is network traffic analysis a relevant skill to have?
- Network traffic analysis is a relevant skill to have because it allows you to see what is happening on your network. It can help you identify malicious activity, such as a hacker trying to gain access to your network. It can also help you identify network issues, such as a misconfigured router or switch.

Do I see myself working in this type of job in the future?
- Yes.  I am going to do start a SoHo focused MSP that will harden and update networks for small businesses and large homes.



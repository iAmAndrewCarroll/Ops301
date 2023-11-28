## Lab 2

**Part 1: Preparing a Network Environment and Staging Kali Linux**

| VM Setups | Network 1 Configuration             | Network 2 Configuration                | Purpose             |
|-----------|-------------------------------------|---------------------------------------|---------------------|
| pfSense   | - Bridged Adapter, eno1, intent     | - Internal Network, intent            | Firewall and routing |
| kali      | - Internal Network, intent           |                                       | Penetration testing  |
| win10     | - Internal Network, intent           |                                       | General Windows VM  |

**Part 2: Port Scanning with nmap**
**Scan for all hosts**

`nmap -sn pfsense > /home/kali/lab2/scan1.txt`
![pfsense scan](media/lab2-1.png)

- In technical terms this seems to be a ping scan with additional information including latency, DNS records, and a status report.
- The scan did not find the Windows 10 VM at 192.168.2.103.
- Why?  I only told it to scan pfsense and not the IP Address Range.
- Why would I perform this particular scan? To see all hosts that are up and running.

`nmap -sn 192.168.2.1/24 > /home/kali/lab2/scan2.txt`
![fast scan](media/lab2-2.png)

- This scan found all hosts on the network
- Why?  I told it to scan the entire network this time.

**Fast, Aggressive Scan**

`nmap -F -A 192.168.2.1/24 > /home/kali/lab2/fastscan.txt`
![aggressive scan](media/lab2-3.png)

- In technical terms this seems to perform a fast scan of the target hosts which includes version detection, OS detection, script scanning while remaining focused on common ports.
- This scan seems to have been successful in finding all hosts on the network.
- Why?  I told it to scan the entire network this time.
- Why perform this scan?  To check all ports on all hosts across the network. This is a good scan to perform when you are not sure what you are looking for.

**Scan the 1000 most common ports on each host**

`nmap -p- --top-ports 1000 192.168.2.1/24 > /home/kali/lab2/1000ports.txt`
![1000 scan](media/lab2-4.png)

- In technical terms this scan is performed on the top 1000 ports on each host in the specified network.
- This scan succeeded in scanning ports taht were not in ignored states.
- Why? At this stage I feel it did its job to the level of knowledge I have
- Why perform this scan?  This seems like a good way to catch low hanging vulnerabilities on the network.

**Scan with Intensity, or Instense Scan**

`nmap -T4 -A -v 192.168.2.1/24 > /home/kali/lab2/intense.txt`
![intense scan](media/lab2-5.png)

- In technical terms this performs an intense scan on all hosts, including version detection, OS detection, and script scanning wiht faster timing and more detailed output than the 1000 port or fast scan.
- This scan seems to have been successful.
- Why? The report is more detailed, the scan took almost 3x as long as before.
- If this picked up a port with a script running that was not authorized by the sysadmin team then you could have a potential vulnerability.  Interesting to consider the applications of such a scan.

**Slow, Comprehensive Scan**

`nmap -p- -T4 -A 192.168.2.1/24 > /home/kali/lab2/slow.txt`
![slow scan](media/lab2-6.png)

- In technical terms this performs a slow, comprehensive scan on all hosts, including version detection, OS detection, and script scanning with slower timing and more detailed output than the 1000 port or fast scan.
- This scan seems to have been successful.
- The report shows that al 65k+ ports were scanned on the windows vm and the pfsense vm.
- This is a comprehensive scan that could provide a boatload of information to an attacker or to a defender.

**Part 3: Reporting Nmap Findings**

Scans Performed:
| Scan Type                    | Scan Results                                  | Actual           |
|------------------------------|-----------------------------------------------|------------------|
| Scan 1 - Discover Hosts      | 2 hosts up (pfSense.lab12, 192.168.2.104)   | 2 hosts up       |
| Scan 2 - Fast, Aggressive    | 2 hosts up (pfSense.lab12, 192.168.2.104)   | 2 hosts up       |
| Scan 3 - Common Ports        | 2 hosts up (pfSense.lab12, 192.168.2.104)   | 2 hosts up       |
| Scan 4 - Intense Scan        | 2 hosts up (pfSense.lab12, 192.168.2.104)   | 2 hosts up       |
| Scan 5 - Comprehensive Scan  | 2 hosts up (pfSense.lab12, 192.168.2.104)   | 2 hosts up       |

Service Enumeration:

| Server IP Address      | Ports Open        | Service/Banner  |
|------------------------|--------------------|-----------------|
| 192.168.2.1 (pfSense.lab12) | 53/tcp, 80/tcp    | domain (Unbound), http (nginx) |
| 192.168.2.104          | Ignored            | N/A (No response) |

**Part 4: Protocol Hierarchy Statistics with Wireshark**

![hierarchy](media/lab2-7.png)
![endpoints](media/lab2-8.png)
![conversations](media/lab2-9.png)

**Part 5: Netstat**

`netstat -a`
Displays all active connections and the TCP and UDP ports on which the computer is listening.
![netstat](media/lab2-10.png)

`netstat -r`
Displays the kernel routing table.
![netstat](media/lab2-11.png)

`netstat -n -t` 
Displays all TCP connections and their respective IP addresses and port numbers.
![netstat](media/lab2-12.png)


pfSense A
- Adapter 1
  - NAT Network
- Adapter 2
  - Host only Network
    - Vbox Net 0
      - File > Tools > Network Manager > Host Only Adapter > Create

pfSense B
  - NAT Network
  - Vbox Net 1
    - File > Tools > Network Manager > NAT Network > Create

VM 1 (Kali)
- Vbox Net 0

VM 2 (Ubuntu or Win10)
- Vbox Net 1

VM > Tools >  Network > on the bottom disable DHCP

pfSense B
- Option 2: Set Interface IP ADdresses
  - 2 for LAN
    - Confi IPv4 address LAN DHCP? No
    - Enter IP address
    - Bit count > 24
    - For LAN press enter
    - Config IPv6 > No
    - Press enter
    - Enable DHCP server on LAN? y
      - enter start address: 192.168.200.2
      - enter end address: 192.168.200.100
    - Revert to HTTP as webConfigurator protocol? y
    - Press enter
pfSense A
- Same steps as above but use 192.168.100.2 and 192.168.100.100


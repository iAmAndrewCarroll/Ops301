### Lab: Web Server Deployment

**Overview**
Infrastructure deployment is an important role for the systems administrator. Public-facing infrastructure such as web servers present unique security and operational challenges compared to endpoints. Configuring a web server requires an understanding of firewall, networking design, network protocols, and security practices.

**Scenario**
GlobeX HR division wants to launch a new employee information website. This website will be public-facing, as it does not contain sensitive information, but rather helpful information about the various services available to employees. You’ve joined the project team and are tasked with standing up some prototype infrastructure for the web developer to work with. “All I know is Wordpress!” the web developer exclaims. “If you can get me a web server and remote access to it, I’ll be all set to begin front-end development.”

**Prerequisites**
- A pfSense VM in VirtualBox, free from configuration settings from previous labs
- A user endpoint VM in VirtualBox (any existing Windows 10 or Linux VM)

**Objectives**
- Deploy an NGINX web server on Linux Server behind pfSense
- On pfSense, setup port forwarding to route traffic on ports 8000 to the web server
- Create firewall rule exceptions for port 8000 and 22
- Add SSH and open up port 22 for administration purposes
- Deploy UFW firewall and activate it
- Allow correct traffic through pfSense
- Test and validate access using a computer on the other side of the pfSense firewall
- Submit an updated network topology

**Resources**
- [Ubuntu Server Download](https://ubuntu.com/download/server)
- [Ubuntu Official Documentation - Install NGINX](https://ubuntu.com/tutorials/install-and-configure-nginx#1-overview)
- [pfSense Port Forwarding](https://docs.netgate.com/pfsense/en/latest/nat/port-forwards.html)

### Tasks

**Part 1: Topology 1/2**

**1. Create Topology**
   - Read through the entire lab and use Draw.io to create an appropriate topology of the network you expect to construct.
   - Include as many details as you can such as computer names, OS types, IP addresses, etc.
   - Include a screenshot of this initial topology.

**Screenshot of Topology**
![Screenshot of Topology](media/lab7-14.png)

**Part 2: Staging**

**Configuration Steps**

**1. Prepare pfSense VM**
   - Ensure you have a fresh pfSense VM, free from configuration settings from previous labs.
   - You can reset an existing instance to factory settings (Diagnostics / Factory Defaults), revert to a baseline snapshot, import a fresh instance from a baseline OVA backup, or install pfSense on a new VM.
   - Regardless of the method used, start from a clean baseline to avoid complications.
   - Configure the WAN network adapter to NAT Network and the LAN adapter to Internal Network.

**pfSense VM Successful**
![pfSense VM Successful](media/lab7-1.png)

**2. Create Ubuntu Server VM**
   - Download the Ubuntu Server ISO.
   - Create a new VM in VirtualBox.
   - Install the latest version of Ubuntu Server.
   - Install OpenSSH during the OS installation process.
   - Reboot when installation is complete.
   - On the Ubuntu Server VM, configure the network adapter to match the LAN adapter of pfSense (should be set to the same Internal Network).

**Ubuntu Server VM Successful**
![Ubuntu Server VM Successful](media/lab7-2.png)

**3. User Endpoint VM Setup**
   - Set up a user endpoint VM with a GUI (Windows 10 or Kali) for configuring pfSense and testing the webserver.
   - Configure the network adapter to match the LAN adapter of pfSense and the Ubuntu Server (should be set to the same Internal Network).

**User Endpoint VM (Kali) Successful**
![User Endpoint VM (Kali) Successful](media/lab7-2.png)

**Part 3: NGINX Web Server Setup**

**In this step, you’ll deploy an NGINX web server on Linux Server behind pfSense.**

**SSH from Kali to Ubuntu Server**
![SSH from Kali to Ubuntu Server](media/lab7-3.png)

**Configuration Steps**

**Complete the following steps for NGINX Setup:**

1. Install NGINX
   - `sudo apt update`
    - `sudo apt install nginx`

2. Creating our own website
   - `cd /var/www`
   - `sudo mkdir globex`
   - `cd globex`
   - `sudo touch index.html`

3. Code the new web page:
   - open the html file for editing using nano `sudo nano index.html` and copy the following to the `index.html` file:
   - <!doctype html>
     <html>
     <head>
      <meta charset="utf-8">
      <title>Hello via Nginx!</title>
     </head>
     <body>
      <h1>Hello via Nginx!</h1>
      <p>We have just configured our Nginx web server to serve HTML on Ubuntu Server!</p>
     </body>
     </html>

**Screenshot of index.html**
![Screenshot of index.html](media/lab7-4.png)

4. Set up virtual host
   - `cd /etc/nginx/sites-enabled`
   - `sudo touch globex`
   - `sudo nano globex`

   Open the `globex` file, copy the following:
   -  server {
         listen 8000;
         listen [::]:8000;

         server_name employees.globex.com;

         root /var/www/globex;
         index index.html;

         location / {
            try_files $uri $uri/ =404;
         }
      }

**Screenshot of globex**
![Screenshot of globex](media/lab7-5.png)

5. Activate virtual host and test results:
   - check to see that nginx is running `sudo systemctl status nginx`

**Screenshot of nginx status**
![Screenshot of nginx status](media/lab7-6.png)

   - if it is not running, start it with `sudo systemctl start nginx`
   - if it is running, you may need to restart with `sudo systemctl restart nginx`

   - open ports 22, 8000 on UFW 
     - `sudo ufw status` > Status: inactive 
     - activate the Ubuntu Server's UFS
     - > `sudo ufw enable` > `sudo ufw status` > Status: active
     - Include a screenshot of UFW settings while you're shelled into Ubuntu Server

**Screenshot of UFW settings**
![Screenshot of UFW settings](media/lab7-7.png)

**Screenshot of Open Ports**
![Screenshot of Open Ports](media/lab7-8.png)

   - Test that your webpage is available by navigating to http://<ip of NGINXserver>:8000 on a VM on the same subnet as the webserver
     - http://192.168.1.100:8000
       - Did not immediately connect to the server
       - Shutdown the Kali and Ubunu Server VMs
       - Restarted the Kali and Ubuntu Server VMs
     - It should show "Hello via Nginx!"

**Screenshot of Hello via Nginx**
![Screenshot of Hello via Nginx](media/lab7-9.png)


6. Load the Globex website files:
   - Clone the class repo to the home directory of your Ubuntu Server
   - Recursively copy the assets from class-07/lab/starter-code folder to `/var/www/globex`
     - This will overwrite the `index.html` file you created earlier
   - Access the web page using a browser (remember we used port 8000) and include a 
   
**Screenshot of GlobeX**
![Screenshot of GlobeX](media/lab7-10.png)


**Part 4: Configuring pfSense**

Now that the web server is deployed, you’ll need to configure the pfSense perimeter to redirect inbound HTTP requests to the new VM’s IP address.

- Set your pfSense’s WAN interface to NAT Network on VirtualBox.
- Login to pfSense web UI and navigate to Interfaces > WAN. Scroll to the bottom and set *Block private networks and loopback addresses* and *Block bogon networks* to disabled. These default firewall rules clash with our VirtualBox NAT Network configuration.
- Determine the web server’s MAC address and add a static DHCP mapping to pfSense for the NGINX web server.
  - `Services > DHCP Server > LAN > DHCP Static Mapping`
  - MAC Address: `08:00:27:6d:2c:2c`
  - Client ID: `Ubuntu Server` 
  - IP Address: `192.168.1.100`
    - NOTE:  You have to change the IP Address pool range because the DHCP server cannot be within the range
      - Services > DHCP Server > LAN > Primary Address Pool: Address Pool Range
- In Firewall > NAT, configure pfSense to route incoming HTTP requests on WAN port 80 to the NGINX web server port 8000.
- Now that the web server has been deployed, we can access the web server from outside the network on a device that’s also set to NAT Network.

**Screenshot of pfSense Firewall/NAT/Port Forward**
![Screenshot of pfSense Firewall/NAT/Port Forward](media/lab7-11.png)

**Part 5: Testing**

- Identify your pfSense’s WAN address on its main dashboard screen towards the bottom right. You’ll need it for the upcoming step.
- Move Kali Linux outside the LAN by setting its network adapter to NAT Network.
- Test and validate that your web page is accessible from outside the LAN by querying pfSense’s WAN interface using a browser.
- You can explicitly specify the port using `http://<WAN ip of pfSense>:80` or, because http traffic uses port 80 by default, you can use `http://<WAN ip of pfSense>` and your browser should automatically connect to port 80.
- Include a **screenshot** of the successful browser test.

**Screensho of GlobeX from WAN on Kali and Ubuntu**
![Screenshot of GlobeX from WAN on Kali and Ubuntu](media/lab7-12.png)
![Screenshot of GlobeX from WAN on Kali and Ubuntu](media/lab7-13.png)
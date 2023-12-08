# Reading 10

[Resource: What is a virtual private cloud (VPC)?](https://www.cloudflare.com/learning/cloud/what-is-a-virtual-private-cloud/)

**1. How can one host within a VPC any services that need to be public?**
- To host services within a VPC that need to be public, you can utilize Network Address Translation (NAT). NAT matches private IP addresses to a public IP address for connections with the public Internet. This allows services to be publicly accessible while still residing within the VPC.

**2. What are examples of services that would live in the publicly-accessible part of the VPC? The privately-accessible part?**
- Publicly-accessible services in a VPC might include web servers, APIs, or any services that need to be accessed by users on the Internet. These services are typically placed in a dedicated subnet with NAT to make them reachable.
- Privately-accessible services are usually placed in subnets that are not directly accessible from the public Internet. These could include databases, internal applications, or sensitive data storage, which should not be exposed publicly.

**3. What are the trade-offs of using a VPC vs traditional infrastructure?**
- Advantages of using a VPC:
  - Scalability: VPCs hosted by public cloud providers allow for easy scalability, enabling you to add more computing resources as needed.
  - Hybrid Cloud Deployment: VPCs can be easily connected to public clouds or on-premises infrastructure via VPN, facilitating hybrid cloud setups.
  - Better Performance: Cloud-hosted services often offer better performance compared to on-premises servers.
  - Enhanced Security: Public cloud providers offering VPCs typically have robust security measures, making it advantageous for small and mid-market businesses.

- Trade-offs:
  - Cost: Depending on usage, cloud-based VPCs can be more expensive than traditional on-premises infrastructure.
  - Data Security: For large enterprises with stringent data security regulations, using a VPC may have fewer advantages due to concerns about data control.

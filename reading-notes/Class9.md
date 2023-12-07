# Reading 9

[Resource: How to capture network traffic? SPAN vs TAP](https://accedian.com/blog/capture-network-traffic-span-vs-tap/)

**1. What are the differences between SPAN and TAP?**
- SPAN (Port Mirroring) copies packets from selected ports to another port for analysis. It's cost-effective and flexible but may consume CPU resources and drop packets in congestion. TAP (Network TAP) is a hardware device that passively captures traffic between two points in a network, providing full visibility but can be costly and is not suitable for narrow traffic ranges or intra-switch traffic.

**2. What types of network devices can support network traffic mirroring?**
- Network switches commonly support network traffic mirroring using SPAN (Port Mirroring). Network TAPs are dedicated hardware devices designed for this purpose.

**3. How can network traffic mirroring be used for network security?**
- Network traffic mirroring can enhance network security by:
  - Monitoring for unusual or malicious traffic patterns.
  - Detecting and analyzing potential security breaches and unauthorized access.
  - Identifying and mitigating distributed denial-of-service (DDoS) attacks.
  - Capturing and analyzing network traffic for evidence in forensic investigations.
  - Monitoring for vulnerabilities and misconfigurations in real-time.

**4. Are there any legal or ethical considerations when using network traffic mirroring?**
- Legal considerations: Comply with privacy and data protection laws, especially when monitoring sensitive data. Consult legal counsel for compliance.
- Ethical considerations: Be transparent with users about monitoring, respect privacy, and only capture necessary data.
- Data retention: Establish clear data retention policies aligned with legal and ethical standards.
- Consent: In some cases, obtain user consent or authorization for monitoring, especially in corporate or educational settings.

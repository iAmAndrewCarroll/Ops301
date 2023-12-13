# Reading 13

[Resource: What is Active Directory?](https://www.cyberark.com/what-is/active-directory/)

**1. What exactly is "Active Directory" and what are the key services it provides?**
- Active Directory (AD) is a Microsoft service designed for managing identity and resources within Windows domain networks. It encompasses several key services:
  - **Active Directory Domain Services (AD DS):** This is the core service used for managing users and resources within the network.
  - **Active Directory Lightweight Directory Services (AD LDS):** It's a streamlined version of AD DS designed for directory-enabled applications.
  - **Active Directory Certificate Services (AD CS):** This service handles the issuance and management of digital security certificates.
  - **Active Directory Federation Services (AD FS):** AD FS facilitates the sharing of identity and access management information across organizations.
  - **Active Directory Rights Management Services (AD RMS):** AD RMS controls access permissions to documents, presentations, and other digital content.

**2. What are the differences between a domain, forest, and tree in Active Directory?**
- **Domain:** A domain is a fundamental unit within Active Directory. It consists of objects like users and devices that share the same AD database. Domains are identified by DNS names, like company.com.
- **Tree:** A tree is a collection of one or more domains with a contiguous namespace. They share a common DNS root name but have different subdomains. For example, marketing.company.com and engineering.company.com might be part of the same tree.
- **Forest:** A forest is a collection of one or more trees that share a common schema, global catalog, and directory configuration but do not have a contiguous namespace. The forest typically serves as the security boundary for an enterprise network.

**3. How can objects (e.g. users, devices) within a domain be grouped?**
- Within a domain, objects like users and devices can be grouped into organizational units (OUs). OUs are created to simplify administration and policy management. Administrators can structure OUs to mirror functional, geographical, or business structures. Group policies can then be applied to these OUs, making it easier to delegate control over resources to various administrators.

**4. Explain the benefits of Active Directory, as you would to a family member.**
- Active Directory is like a digital organizer for a computer network. It helps keep everything in order and secure. Here are some benefits in simple terms:
  - **Security:** It keeps the bad guys out and controls who can access what on the network.
  - **Organization:** It neatly arranges all the people, computers, and files so they're easy to find and manage.
  - **Simplicity:** Makes it easier for the computer experts to run things and reduces problems.
  - **Safety Net:** Even if something goes wrong, it helps the network stay up and running.
  - **Connecting to the Cloud:** It also helps connect our computer stuff to the internet cloud, where we can use online tools and apps.

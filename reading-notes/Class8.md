# Reading 8

[Resource: Computer Networking | AAA(Authntication, Authorization and Accounting)](https://www.geeksforgeeks.org/computer-network-aaa-authentication-authorization-and-accounting/)

**1. Explain each of the three A’s as you would to a non-technical family member. Use an analogy or a story.**
- Authentication is like showing your digital ID card to prove who you are online, just like showing your ID to get into a party.
- Authorization is like having different access levels in a library. Your library card allows you into certain sections based on your card type.
- Accounting is like keeping a record of your actions, similar to a library tracking which books you borrow.

**2. What should the administrator do if the ACS server fails to authenticate a user during AAA implementation?**
- If the ACS server fails, the administrator should set up a backup plan. They can use a local database on the device itself for authentication, like having a spare key when the main one doesn't work.

**3. What is the role of the NAS in the AAA implementation using an ACS server? Use a diagram.**

User Device <--> NAS <--> ACS Server

- The User Device is your computer trying to access the network.
- The NAS (Network Access Server) is like the gatekeeper at the entrance. It controls access and communicates with the ACS Server.
- The ACS Server (Access Control Server) checks your digital ID (authentication) and decides if you're allowed in. The NAS helps manage this process, like a bouncer checking your ID before entering a club.

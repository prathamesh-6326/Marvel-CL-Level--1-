# Marvel-CL-Level--1-
## Task 1 - Git Practice
Learning Git basics for Marvel UVCE ClCY Level 1

# Cloud Computing (CL)

## Task 1: Git and GitHub Basics

### What I Did
- Configured Git with my identity using `git config`
- Created a repository on GitHub called `Marvel-CL-Level--1-`
- Cloned the repository to my local Ubuntu machine
- Created a new branch called `feature/git-practice` to work safely without affecting the main code
- Edited the README.md file using the `nano` text editor
- Staged and committed the changes with a meaningful message
- Pushed the branch to GitHub and opened a Pull Request
- Merged the Pull Request into the main branch
- Practiced `git revert` to safely undo a commit without deleting history
- Practiced `git cherry-pick` to pick one specific commit from history

### Commands Used

| Command | What it does |
|---|---|
| `git config --global user.name` | Set my name so every commit is tagged with my identity |
| `git clone [link]` | Download the repository from GitHub to my laptop |
| `git checkout -b branchname` | Create a new branch to work safely |
| `git status` | Check what files were changed |
| `git add .` | Select all changed files to be saved |
| `git commit -m "message"` | Save a snapshot of the changes with a label |
| `git push origin branchname` | Upload the branch to GitHub |
| `git log --oneline` | See all commits in short form |
| `git revert HEAD` | Safely undo the last commit without deleting history |
| `git cherry-pick [id]` | Pick one specific commit from history and apply it |

### Key Concepts Learned
- **Branch:** A parallel copy of the project to experiment without breaking the original
- **Commit:** A saved snapshot of your work at a point in time
- **Pull Request (PR):** A request to merge your branch changes into the main branch
- **Revert:** Undoes a commit by creating a new commit — history stays intact
- **Cherry-pick:** Takes one specific commit from history without taking everything else

### Screenshot
](<img width="2311" height="1657" alt="Image" src="https://github.com/user-attachments/assets/810f5de1-21a3-4257-bb2f-713749f5c275" />)
](<img width="2953" height="1422" alt="Image" src="https://github.com/user-attachments/assets/f92de00f-1eb6-4524-94ae-3222d0e00221" />)

### Final Outcome
Successfully practiced the complete Git workflow — from cloning a repository to branching, committing, pushing, opening a pull request, merging, reverting, and cherry-picking. Understood the purpose of each command and when to use it.


## Task 2: Docker Fundamentals

### What is Docker?
Docker is a tool that lets you run applications inside isolated boxes called **containers**. The application and everything it needs to run is packaged together inside the container — so it works the same on any machine.

### Containers vs Virtual Machines
| Feature | Virtual Machine (VM) | Container |
|---|---|---|
| What it is | A full computer rented inside your computer | Just a room inside a shared house |
| Has its own OS? | Yes | No — shares the host OS |
| Speed | Slower to start | Starts in seconds |
| Size | Heavy (GBs) | Lightweight (MBs) |

Think of it this way:
- **VM** = Renting an entire house (own kitchen, bedroom, everything)
- **Container** = Renting just one room in a shared house

### What I Did
- Installed Docker on Ubuntu using `sudo apt install docker.io`
- Started and enabled the Docker service
- Ran `docker run hello-world` to verify Docker was working
- Pulled the Nginx image from Docker Hub
- Ran Nginx as a container and mapped port 8080 on my laptop to port 80 inside the container
- Accessed the running website at `http://localhost:8080` from the browser
- Inspected running containers, viewed logs, stopped and removed the container

### Commands Used

| Command | What it does |
|---|---|
| `sudo apt install docker.io` | Install Docker on Ubuntu |
| `sudo systemctl start docker` | Start the Docker service |
| `docker run hello-world` | Test if Docker is working |
| `docker pull nginx` | Download the Nginx image from Docker Hub |
| `docker run -d -p 8080:80 --name my-nginx nginx` | Run Nginx container in background, map ports |
| `docker ps` | See all running containers |
| `docker logs my-nginx` | View the container's activity logs |
| `docker stop my-nginx` | Stop the running container |
| `docker rm my-nginx` | Remove the container |

### Key Concepts Learned
- **Image:** A recipe or blueprint for a container (like a cake recipe)
- **Container:** The actual running instance created from an image (the actual cake)
- **Docker Hub:** An online library of images — like an app store for containers
- **Port Mapping (-p 8080:80):** Connects laptop's port 8080 to container's port 80 so the browser can reach it

### Screenshot
]( <img width="1578" height="745" alt="Image" src="https://github.com/user-attachments/assets/992aa72a-941a-4663-8cc6-ab547935a017" />)

](<img width="2936" height="1573" alt="Image" src="https://github.com/user-attachments/assets/dd04e466-b835-49f9-a4b6-1d411d882fd2" />)
](<img width="2936" height="1573" alt="Image" src="https://github.com/user-attachments/assets/3bfd2cdf-3923-4235-bc96-7ce6ddcb8f46" />)

### Final Outcome
Successfully installed Docker, pulled the Nginx image, ran it as a container, accessed it from the browser, and managed the full container lifecycle — start, inspect, logs, stop.

## Task 4: Launch and Manage an AWS EC2 Instance

### What is AWS EC2?
EC2 (Elastic Compute Cloud) is Amazon's service that lets you rent a computer that lives in their data center. You can access it from anywhere using SSH — like remotely logging into another machine through the terminal.

### What I Did
- Created an AWS Free Tier account
- Launched a **t3.micro Ubuntu** instance on EC2
- Created a key pair (`Marvel_CL_L1_T4.pem`) for secure SSH access
- Configured the security group to allow **SSH (port 22)** and **HTTP (port 80)**
- Protected the key file using `chmod 400`
- Connected to the EC2 instance remotely from my Ubuntu laptop using SSH
- Installed and started **Nginx** web server on the EC2 instance
- Accessed the Nginx welcome page from the browser using the EC2 public IP

### Commands Used

| Command | What it does |
|---|---|
| `chmod 400 Marvel_CL_L1_T4.pem` | Make the key file read-only (required by AWS for security) |
| `ssh -i [key.pem] ubuntu@[public-ip]` | Remotely log into the EC2 instance |
| `sudo apt update` | Update the package list |
| `sudo apt install nginx -y` | Install Nginx web server |
| `sudo systemctl start nginx` | Start the Nginx service |

### Key Concepts Learned
- **EC2:** Renting a computer from Amazon's data center
- **SSH:** Secure way to remotely access another computer through terminal
- **Security Group:** Firewall rules that control what traffic can enter/leave the instance
- **Key Pair (.pem):** A secure key file used to authenticate SSH access — like a physical key to a door
- **Public IP:** The address used to access the EC2 instance from the internet

### EC2 Instance 
- **Instance Type:** t3.micro (Free Tier)
- **OS:** Ubuntu 22.04 LTS
- **Public IP:** 16.171.39.66
- **Web Server:** Nginx

### Screenshot
](<img width="2943" height="1558" alt="Image" src="https://github.com/user-attachments/assets/d54561a8-7b79-40c3-99d6-3a912c1b468d" />)
](<img width="2943" height="1558" alt="Image" src="https://github.com/user-attachments/assets/0d6e4df5-af0c-4f7e-bca9-cadc96a39cd1" />)
](<img width="1578" height="745" alt="Image" src="https://github.com/user-attachments/assets/081ed54d-6720-4052-90d0-0ecd33c0bfa6" />)

### Final Outcome
Successfully launched an EC2 instance, connected to it remotely via SSH, installed Nginx, and accessed the web server from the browser using the instance's public IP address.

# Cyber Security (CY)

## Task 1: Fundamentals of Computer Networking — Introduction

### What I Learned
A network is simply things being connected together. It is not limited to computers — we see networks everywhere in daily life. A city's bus and train system, the electricity grid, the postal system, and even social groups of people are all examples of networks.

In computing, a network means devices connected together to share data and resources. A computer network can be as small as two devices (a laptop and phone sharing files) or as massive as the entire Internet with billions of devices. These devices can include phones, laptops, security cameras, traffic lights, and even modern farming machines.

Networks run almost everything in our daily lives — weather data collection, electricity delivery, traffic control, and social media. Understanding networks is essential in cybersecurity because if you understand how devices connect, you understand how attackers exploit those connections.

### Key Concepts
- A network = devices connected to communicate and share resources
- Networks can be small (2 devices) or massive (the entire Internet)
- Networks are everywhere — not just in computing

### Screenshot
](<img width="2943" height="1582" alt="Image" src="https://github.com/user-attachments/assets/64feaafb-1793-4636-b205-9cee7f39ab8e" />)

### Final Outcome
Understood what a network is, why it matters, and how it applies to cybersecurity.

## Task 2: Fundamentals of Computer Networking — Internet

### What I Learned
The Internet did not appear overnight. In the late 1960s, the U.S. Defence Department funded **ARPANET** — the first working network and the Internet's prototype. In 1989, **Tim Berners-Lee** created the **World Wide Web (WWW)**, which turned the Internet into the global information library we use today.

The Internet is essentially a **network of networks**. Small private networks (like your home WiFi) connect together to form the massive public network called the Internet.

- **Private Network:** A small closed group — like you and your friends sharing notes
- **Public Network (Internet):** When all these small private groups connect together globally

Devices identify each other using **IP addresses** — unique labels assigned to each device so data reaches the right destination.

### Key Concepts
- ARPANET → WWW → Internet (history of the Internet)
- Private Network vs Public Network
- Devices use IP addresses to identify each other on a network

### Screenshot
](<img width="2943" height="1582" alt="Image" src="https://github.com/user-attachments/assets/d6439b89-36ea-4075-8775-af11c55a51ca" />)

### Final Outcome
Understood how the Internet evolved, the difference between private and public networks, and how devices identify each other.

## Task 3: Fundamentals of Computer Networking — IP Address

### What I Learned
For devices to communicate on a network, they must be identifiable — just like people have names and fingerprints.

- **IP Address** = Like a name (can change)
- **MAC Address** = Like a fingerprint (unique to the device, built into hardware)

### IP Address
An IP address identifies a device on a network and is made up of four sets of numbers (e.g., `192.168.1.10`). It can change and cannot be shared by two devices at the same time on the same network.

There are two types:
- **Private IP:** Used inside a local network (home, office). Example: `192.168.1.10`
- **Public IP:** Used on the Internet, given by the ISP. All devices in a home share one public IP when accessing the Internet.

### IPv4 vs IPv6
- **IPv4** supports ~4.3 billion addresses (2³²) — we ran out
- **IPv6** was created to solve this — supports 2¹²⁸ addresses (practically unlimited)

### MAC Address
A MAC address is a unique 12-character hexadecimal code (e.g., `a4:c3:f0:85:ac:2d`) built into the device's network card at the factory. The first half identifies the manufacturer, the second half identifies the specific device.

### MAC Spoofing
Even though MAC addresses are meant to be permanent, they can be faked — this is called **MAC Spoofing**. If a firewall only allows a specific MAC address, an attacker can fake that address and bypass security. This is why relying only on MAC addresses for security is risky.

### Key Concepts Summary
| Feature | IP Address | MAC Address |
|---|---|---|
| Can it change? | Yes | No (but can be spoofed) |
| Purpose | Identifies device on network | Identifies physical network card |
| Public/Private? | Yes | No |
| Example | 192.168.1.10 | a4:c3:f0:85:ac:2d |

### Screenshot
](<img width="2943" height="1582" alt="Image" src="https://github.com/user-attachments/assets/fa1ec57c-3ebd-47d7-9db8-98dd10348024" />)

### Final Outcome
Understood IP addresses, MAC addresses, the difference between IPv4 and IPv6, and the security risk of MAC spoofing.

## Task 4: Fundamentals of Computer Networking — Ports

### What I Learned
Ports are points where data enters and leaves a device. Think of a harbour — ships can only dock at ports designed for their size and purpose. Similarly, in networking, ports control what kind of data can enter or leave a device.

Ports are numbered from **0 to 65535**. Standards were created so applications always know which port to use. For example, web traffic always uses Port 80 — that is why Chrome and Firefox can interpret web data consistently across all websites.

### Common Ports (Well-Known Ports: 0–1024)

| Protocol | Port | Purpose |
|---|---|---|
| FTP | 21 | File transfer between client and server |
| SSH | 22 | Secure remote login via terminal |
| HTTP | 80 | Regular web browsing |
| HTTPS | 443 | Secure (encrypted) web browsing |
| SMB | 445 | File and printer sharing |
| RDP | 3389 | Remote desktop access |
| LDAP | 389 | Directory services (unencrypted) |
| Memcached | 11211 | Used in DDoS attacks |

### Important Note
Port numbers are standards, not strict rules. A web server can run on Port 8080 instead of 80 — but then the port must be explicitly mentioned in the address (e.g., `website.com:8080`).

### Screenshot
](<img width="2943" height="1582" alt="Image" src="https://github.com/user-attachments/assets/74d93b4c-b4eb-4a96-bcc9-f273443915bd" />)

### Final Outcome
Understood what ports are, why standards exist, common port numbers and their purposes, and how non-standard ports must be explicitly specified.

## Task 5: Fundamentals of Computer Networking — Packets & Frames

### What I Learned
When data is sent across a network, it is not sent as one large file. Instead, it is broken into smaller units called **packets** and **frames**.

- **Packet** → Exists at **Layer 3 (Network Layer)** of the OSI model. Contains the IP header and the actual data (payload).
- **Frame** → Exists at **Layer 2 (Data Link Layer)**. Wraps the packet and adds MAC addresses to deliver data within a local network.

Think of it like sending a letter:
- The **letter** = packet (the actual content)
- The **envelope** = frame (the outer layer that helps deliver it)

This wrapping process is called **encapsulation**.

### Why Break Data into Packets?
Sending data in smaller packets reduces network congestion and improves reliability. For example, when you load an image on a website, the image is not sent as one large file — it is split into multiple packets that travel separately and are reassembled at your device.

### Important Packet Header Fields

| Header | Description |
|---|---|
| Time To Live (TTL) | Limits how long a packet exists on the network. Prevents packets from circulating endlessly. |
| Checksum | Verifies data integrity. If data changes during transmission, checksum won't match → packet discarded. |
| Source Address | IP address of the sending device |
| Destination Address | IP address of the receiving device |

### Key Concepts
- **Packet** = Layer 3 (Network Layer) — contains IP header + data
- **Frame** = Layer 2 (Data Link Layer) — wraps packet, contains MAC addresses
- **Encapsulation** = Wrapping data with additional information as it moves through OSI layers
- **TTL** = Prevents packets from looping forever on the network

### Screenshot
](<img width="2943" height="1582" alt="Image" src="https://github.com/user-attachments/assets/47c442e4-e947-4d65-85fe-ca691280ca56" />)
](<img width="2943" height="1582" alt="Image" src="https://github.com/user-attachments/assets/8438bc26-f676-45b3-a6bf-fbc5d87a06e2" />)

### Final Outcome
Understood the difference between packets and frames, why data is broken into packets, how encapsulation works across OSI layers, and the purpose of key packet header fields like TTL and Checksum.

<img width="1600" height="850" alt="image" src="https://github.com/user-attachments/assets/282fd987-e5a9-475f-b685-61dbd6b91e9d" /># Marvel-CL-Level--1-
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

## Task 3: Dockerize a Simple Application

### What is this task?
A Dockerfile describes how to package an application into an image. This task containerizes a static website from the starter code, runs it locally, and opens it in the browser through a mapped port.

Flow: `Dockerfile → docker build → image → docker run -p 8080:80 → Browser (localhost:8080)`

### What I Did
- Wrote a Dockerfile on top of `nginx:alpine` that copies the starter website into Nginx's web root
- Built the image as `my-app`
- Ran it as a container named `my-app-container` and mapped host port 8080 to container port 80
- Opened `http://localhost:8080` in the browser and saw the page
- Checked the image layers with `docker history`

### Source Code
| File | Purpose | Link |
|---|---|---|
| `Dockerfile` | Builds the image from `nginx:alpine` and copies the website into it | [Dockerfile](https://github.com/prathamesh-6326/Marvel-CL-Level--1-/blob/main/task3/Dockerfile) |

### Commands Used

| Command | What it does |
|---|---|
| `docker build -t my-app .` | Build an image named `my-app` from the Dockerfile in this folder |
| `docker run -d -p 8080:80 --name my-app-container my-app` | Run the image in the background and map port 8080 to port 80 |
| `docker ps` | Check the container is running and see the port mapping |
| `docker history my-app` | List the layers of the image and their sizes |
| `docker images my-app` | Show the image and its total size |
| `docker stop my-app-container` / `docker rm my-app-container` | Stop and remove the container |

### Image Layers
| Instruction | Layer | Size |
|---|---|---|
| `FROM nginx:alpine` | Base image layers (8 pulled) | about 26 MB |
| `COPY . /usr/share/nginx/html` | Website files | 28.7 kB |
| `EXPOSE 80` | Metadata only | 0 B |

### Key Concepts Learned
- **Dockerfile:** A text file of instructions that Docker follows to build an image
- **Layer:** Each instruction that changes files creates a read-only layer, and unchanged layers are cached on rebuild
- **Base image:** `FROM` sets the starting image, and `nginx:alpine` is a small Nginx image
- **COPY:** Puts the application files inside the image
- **EXPOSE:** Documents the container's port but does not publish it
- **Port mapping (-p 8080:80):** Publishes the container's port 80 on the host's port 8080

### Screenshot

Container running and layer history:

<img alt="Task 3 docker run, ps and history"
  src="<<img width="1600" height="850" alt="Image" src="https://github.com/user-attachments/assets/59c94dbf-620c-4417-a927-6c0f3cf88d38" />>" />

App in the browser:

<img alt="Task 3 browser localhost:8080" 
  src="<https://github.com/prathamesh-6326/Report-images/issues/3#issuecomment-5968517173>" />

### Final Outcome
Successfully wrote a Dockerfile for the starter website, built the image, ran it as a container with port 8080 mapped to port 80, opened it in the browser, and inspected the image layers.


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




## Task 5: Kubernetes Basics and Writing Pod Specs

### What is this task?
Kubernetes runs and manages containers across machines. A Pod is the smallest unit it deploys, and it is described in a YAML manifest. This task writes a Pod spec for Nginx, applies it, and inspects it with `kubectl`.

Flow: `pod.yaml → kubectl apply → Pod (nginx) → get / describe / logs`

### Core Concepts
| Concept | Meaning |
|---|---|
| **Node** | A machine (physical or virtual) that runs Pods |
| **Pod** | The smallest deployable unit: one or more containers sharing a network and storage |
| **Cluster** | A set of nodes managed together by Kubernetes |
| **Control Plane** | The components that manage the cluster: API server, scheduler, controller manager and etcd |

### What I Did
* Used a Killercoda single-node Kubernetes playground (node `controlplane`, v1.36.1) in place of Minikube
* Checked the cluster with `kubectl get nodes` and `kubectl cluster-info`
* Wrote `pod.yaml` for an Nginx container
* Applied it with `kubectl apply -f pod.yaml` and confirmed the Pod was `1/1 Running`
* Inspected the Pod with `kubectl describe pod nginx-pod`
* Viewed the container output with `kubectl logs nginx-pod`

### Source Code
| File | Purpose | Link |
|---|---|---|
| `pod.yaml` | Pod manifest running `nginx:latest` on port 80 | [pod.yaml](https://github.com/prathamesh-6326/Marvel-CL-Level--1-/blob/main/task5/pod.yaml) |

### Commands Used

| Command | What it does |
|---|---|
| `kubectl get nodes` | Show the cluster's nodes and whether they are Ready |
| `kubectl cluster-info` | Show the control plane and CoreDNS addresses |
| `kubectl apply -f pod.yaml` | Create the Pod from the manifest |
| `kubectl get pods` | Show Pod status, restarts and age |
| `kubectl get pods -o wide` | Show the Pod's IP and node |
| `kubectl describe pod nginx-pod` | Show full details: image, IP, conditions, events |
| `kubectl logs nginx-pod` | Show the container's logs |

### Key Concepts Learned
* **Manifest structure:** `apiVersion`, `kind`, `metadata` and `spec` are the four top-level fields
* **Labels:** Key-value tags (`app: nginx`) that other objects use to find the Pod
* **Declarative apply:** Re-running `kubectl apply` on an unchanged file reports `unchanged`
* **Pod conditions:** `Initialized`, `Ready`, `ContainersReady` and `PodScheduled` show how far startup got
* **Restart Count:** `0` means the container has not crashed

### Screenshot
![](<img width="1600" height="806" alt="Image" src="https://github.com/user-attachments/assets/4b16ea8d-a873-4904-a751-b12438cefa58" />)
![](<img width="1600" height="803" alt="Image" src="https://github.com/user-attachments/assets/6405cd9f-f692-441c-ae63-53409d552abb" />)
### Final Outcome
Successfully wrote a Pod manifest for Nginx, applied it to a Kubernetes cluster, confirmed it was Running, and inspected it with `get`, `describe` and `logs`.

---

## Task 6: Manage AWS S3 and IAM with CLI

### What is this task?
IAM controls who can do what in AWS (users, groups, roles and policies), and the AWS CLI lets you work with S3 from the terminal. This task creates an IAM user with S3 access, configures the CLI, and manages a bucket and its files.

### What I Did
_To be added after the Task 6 screenshots are checked._

### Commands Used
_To be added._

### Screenshot
![](<img width="1600" height="665" alt="Image" src="https://github.com/user-attachments/assets/5579ccc4-8cc6-42da-b76d-3fb6ab98bb73" />)
![](<img width="1600" height="900" alt="Image" src="https://github.com/user-attachments/assets/35989fac-f72a-4284-bd3a-6ad921a86985" />)
### Final Outcome
_To be added._

---

## Task 7: Deploy a Containerized Application on Kubernetes

### What is this task?
A Dockerized app is deployed on Kubernetes with YAML manifests, exposed through ClusterIP and NodePort Services, then scaled and updated with `kubectl`.

Flow: `Docker Hub image → Deployment (3 replicas) → ClusterIP / NodePort Service → scale → rolling update`

### What I Did
* Built a Docker image from `nginx:alpine` with a custom `index.html` and pushed it to Docker Hub as `prathamesh08/myapp:v1` and `prathamesh08/myapp:v2`
* Used a Killercoda Kubernetes playground (one node, v1.36.1)
* Wrote `deployment.yaml` (3 replicas of `prathamesh08/myapp:v1`), `service-clusterip.yaml` and `service-nodeport.yaml` (nodePort 30007), then ran `kubectl apply -f`
* Verified 3/3 Pods Running and opened the app through NodePort 30007, which returned "Hello from App v1"
* Scaled the Deployment 3 → 5 → 2 with `kubectl scale`
* Updated the image to `prathamesh08/myapp:v2` and watched the rolling update with `kubectl rollout status` and `kubectl get rs`. The app then returned "Hello from App v2"

### Commands Used

| Command | What it does |
|---|---|
| `kubectl apply -f deployment.yaml` | Create the Deployment |
| `kubectl apply -f service-clusterip.yaml` | Create the internal Service |
| `kubectl apply -f service-nodeport.yaml` | Create the external Service on port 30007 |
| `kubectl get pods` | Check that all replicas are Running |
| `kubectl scale deployment <name> --replicas=5` | Scale up (later `--replicas=2` to scale down) |
| `kubectl set image` (or edit the YAML and re-apply) | Update the image to `myapp:v2` and trigger the rolling update |
| `kubectl rollout status deployment/<name>` | Watch the rolling update finish |
| `kubectl get rs` | Show the new and old ReplicaSets |

### Key Concepts Learned
* **Dockerfile and image:** Packages the app into an image that the Deployment pulls from a registry
* **Deployment:** Declares the desired state and creates a ReplicaSet that keeps N Pods running
* **ClusterIP:** A stable internal IP and DNS name, reachable only inside the cluster
* **NodePort:** Opens a port (30000-32767) on every node for external access
* **Rolling update:** Changing the Pod template creates a new ReplicaSet and gradually replaces old Pods. The old ReplicaSet stays at 0 replicas for rollback
* **Selectors and labels:** Services find Pods through matching labels (`app: myapp`)

### Screenshot 
![](<img width="1600" height="384" alt="Image" src="https://github.com/user-attachments/assets/71cd30d2-cbc0-4778-bc9f-dcdb0065b086" />)
![](<img width="1600" height="773" alt="Image" src="https://github.com/user-attachments/assets/9dd17a43-164f-4470-ac7c-83396ecd6214" />)
### Final Outcome
The application was deployed with multiple replicas, exposed internally (ClusterIP) and externally (NodePort), then scaled and updated with no downtime using `kubectl`.

---

## Task 8: Use Kubernetes Secrets and Environment Variables

### What is this task?
Configuration and sensitive data are kept out of images and Deployment YAML. A **ConfigMap** holds non-sensitive settings, a **Secret** holds the AWS credentials, and the app uses them to list an S3 bucket.

Flow: `ConfigMap + Secret → Deployment (env vars + mounted file) → Pod → AWS S3`

### What I Did
* Used a running cluster with `kubectl` configured, plus an IAM user with read-only S3 access (`AmazonS3ReadOnlyAccess`) and an S3 bucket
* Created a ConfigMap `app-config` with `APP_MODE`, `S3_BUCKET_NAME`, `AWS_DEFAULT_REGION` and an `app.properties` file
* Created a Secret `aws-credentials` with `kubectl create secret`, so the keys never sit in a file that could be committed to Git
* Updated the Deployment to load the ConfigMap with `envFrom`, inject each credential with `secretKeyRef`, and mount `app.properties` at `/config`
* Deployed it, checked the Pod environment wiring, and read the logs to confirm S3 access

### Source Code
| File | Purpose | Link |
|---|---|---|
| `configmap.yaml` | ConfigMap with `APP_MODE`, bucket name, region and `app.properties` | [configmap.yaml](https://github.com/prathamesh-6326/Marvel-CL-Level--1-/blob/main/task8/configmap.yaml) |
| `deployment.yaml` | Deployment using `envFrom`, `secretKeyRef` and a mounted config file | [deployment.yaml](https://github.com/prathamesh-6326/Marvel-CL-Level--1-/blob/main/task8/deployment.yaml) |

The Secret is created only with the command below and is not stored in any file.

### Commands Used

| Command | What it does |
|---|---|
| `kubectl apply -f configmap.yaml` | Create the ConfigMap |
| `kubectl create secret generic aws-credentials --from-literal=AWS_ACCESS_KEY_ID=<REDACTED> --from-literal=AWS_SECRET_ACCESS_KEY=<REDACTED>` | Store the AWS keys in a Secret |
| `kubectl describe secret aws-credentials` | Show key names and sizes only, not values |
| `kubectl apply -f deployment.yaml` | Deploy the app |
| `kubectl rollout status deployment/s3-demo` | Wait for the rollout to finish |
| `kubectl get configmap,secret` | Confirm both objects exist |
| `kubectl describe pod -l app=s3-demo` | Show env vars as `<set to the key ... in secret ...>` |
| `kubectl logs deployment/s3-demo` | Show the config values and the S3 listing |
| `kubectl get deployment s3-demo -o yaml \| grep -n -i -A3 secretKeyRef` | Prove the Deployment holds only a reference, not the key values |

### Secrets vs ConfigMaps

| Aspect | ConfigMap | Secret |
|---|---|---|
| Purpose | Non-confidential configuration | Passwords, tokens, keys |
| Storage encoding | Plain text | base64-encoded (not encrypted by default) |
| Extra protection | None | tmpfs on nodes, only sent to nodes that need it, RBAC-restrictable, can be encrypted at rest |
| Size limit | 1 MiB | 1 MiB |
| Example in this task | `APP_MODE`, `S3_BUCKET_NAME`, `app.properties` | `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY` |

### Key Concepts Learned
* **envFrom / configMapRef:** Turns every ConfigMap key into an environment variable
* **secretKeyRef:** Injects one Secret key as an environment variable without writing its value in the YAML
* **Volume mount:** Mounts `app.properties` as a read-only file at `/config`
* **Refresh behaviour:** Env vars are not refreshed on change, so the Pod must restart. Volume-mounted ConfigMaps and Secrets update eventually, except with `subPath` mounts

### Security Notes
* Real credentials were never written into YAML files or committed to version control
* Secrets are only base64-encoded, not encrypted. Anyone with `get secret` permission can decode them, so use RBAC and encryption at rest
* The IAM user has read-only S3 permissions (least privilege)
* On EKS, prefer IAM Roles for Service Accounts (IRSA) over long-lived keys
* The access keys should be rotated or deleted after the lab

### Cleanup
```bash
kubectl delete deployment s3-demo
kubectl delete configmap app-config
kubectl delete secret aws-credentials
```

### Screenshot
![](<img width="1600" height="769" alt="Image" src="https://github.com/user-attachments/assets/4e7f373a-050f-40a0-b0a6-ef5d3e19e598" />)
![](<img width="1600" height="800" alt="Image" src="https://github.com/user-attachments/assets/b7331616-ca79-45d8-b947-29db11c2ff54" />)
### Final Outcome
A ConfigMap supplied non-sensitive settings as environment variables and a mounted file. A Secret supplied the AWS credentials through `secretKeyRef`, so they never appear in the Deployment manifest or the container image. The Pod logs confirmed that the app read its configuration and listed the S3 bucket using the injected credentials.

---

## Task 9: Deploy an App to Push Files from Kubernetes to S3

### What is this task?
A Flask app runs inside a Kubernetes Pod on Minikube and uploads files to an AWS S3 bucket. The AWS credentials are stored in a Kubernetes Secret and injected into the Pod as environment variables, so they never appear in the code or the image.

Flow: `curl / browser → Flask Pod (Minikube) → boto3 → S3 bucket`
Credentials: `IAM user access key → Kubernetes Secret → Pod env vars`

### What I Did
* Created an S3 bucket `prathamesh-s3-upload-demo` in `ap-south-1`
* Created an IAM policy `uploader-policy` allowing only `s3:PutObject` and `s3:ListBucket` on that bucket
* Created an IAM user `uploader-t-9`, attached the policy and generated an access key
* Used GitHub Codespaces for the terminal because the lab PC had no kubectl
* Started Minikube with the Docker driver
* Wrote a Flask app (`app.py`) with an upload form and an `/upload` endpoint using boto3
* Containerized it with a `Dockerfile` and loaded the image into Minikube
* Stored the AWS keys in a Kubernetes Secret `aws-creds`
* Deployed the app with a Deployment and Service (`deploy.yaml`), injecting the Secret with `envFrom.secretRef`
* Uploaded `task9-test.txt` through the app and verified it in the S3 console

### Source Code
Commit: https://github.com/prathamesh-6326/Marvel-CL-Level--1-/commit/1596935fedcc9206b8a384f91ec7c550439033da

| File | Purpose |
|---|---|
| `app/Dockerfile` | Builds the image (python:3.12-slim, flask, boto3) |
| `app/app.py` | Upload form and `/upload` endpoint using `s3.upload_fileobj` |
| `app/deploy.yaml` | Deployment (Secret via `envFrom.secretRef`) and Service |
| `task9-test.txt` | Test file uploaded to S3 |

### Commands Used

| Command | What it does |
|---|---|
| `minikube start --driver=docker --container-runtime=docker --network=bridge` | Start a local Kubernetes cluster |
| `kubectl get nodes` | Check that the node is Ready |
| `docker build -t s3-uploader:1 .` | Build the app image |
| `minikube image load s3-uploader:1` | Copy the image into Minikube |
| `kubectl create secret generic aws-creds --from-literal=AWS_ACCESS_KEY_ID=<REDACTED> --from-literal=AWS_SECRET_ACCESS_KEY=<REDACTED>` | Store the AWS keys in a Secret |
| `kubectl apply -f deploy.yaml` | Create the Deployment and Service |
| `kubectl get pods,svc,secret` | Check the Pod is Running and the Secret exists |
| `kubectl port-forward svc/s3-uploader 8080:80 &` | Expose the app on localhost:8080 |
| `curl -F "file=@task9-test.txt" localhost:8080/upload` | Upload the file through the app |
| `kubectl logs deploy/s3-uploader` | Read the app logs when debugging |
| `kubectl rollout restart deploy/s3-uploader` | Restart the Pod so it reads an updated Secret |

### Key Concepts Learned
* **Kubernetes Secret:** Stores sensitive data like passwords and keys, separate from the image and code
* **envFrom / secretRef:** Turns every key in a Secret into an environment variable inside the Pod
* **IAM least privilege:** The app's user can only upload to one bucket, nothing else
* **Minikube:** A single-node Kubernetes cluster for local practice
* **Port-forward:** Temporarily exposes a service inside the cluster on a local port
* **boto3:** The AWS SDK for Python. It reads `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` from the environment automatically

### Security Notes
* A dedicated IAM user was used, not root credentials
* Kubernetes Secrets are base64-encoded, not encrypted. Production should use encryption at rest or an external secrets manager
* The access key was deleted after verification

### Issues Faced
* The first Minikube setup had no outbound internet in Codespaces, so image pulls and the S3 call failed. Fixed by recreating it with the Docker runtime and loading the image with `minikube image load`
* A wrong access key caused `InvalidAccessKeyId`. Fixed by creating a new key, recreating the Secret and restarting the Pod

### Screenshot
Pod running, Secret present, upload successful:

![Pod, Secret and upload output]
(<img width="1600" height="776" alt="Image" src="https://github.com/user-attachments/assets/5b018014-a14a-46a2-aa5c-1a3cf04b9be3" />)

File visible in the S3 bucket:

![S3 Objects tab]
(<img width="1600" height="765" alt="Image" src="https://github.com/user-attachments/assets/625eca3a-d327-4da9-a8c9-474276372cc3" />)

### Final Outcome
Successfully built a containerized Flask app, deployed it on Minikube with AWS credentials injected from a Kubernetes Secret, uploaded a file through it, and verified the file in the S3 bucket. Docker, Kubernetes, IAM, S3 and Secrets worked together as one pipeline.

# Cyber Security (CY)

# Level 1 — UVCE MARVEL (TryHackMe) — Task Report

## Task 1: Fundamentals of Computer Networking — Introduction

### What I Learned
A network is simply things being connected together. It is not limited to computers — we see networks everywhere in daily life. A city's bus and train system, the electricity grid, the postal system, and even social groups of people are all examples of networks.

In computing, a network means devices connected together to share data and resources. A computer network can be as small as two devices (a laptop and phone sharing files) or as massive as the entire Internet with billions of devices. These devices can include phones, laptops, security cameras, traffic lights, and even modern farming machines.

Networks run almost everything in our daily lives — weather data collection, electricity delivery, traffic control, and social media. Understanding networks is essential in cybersecurity because if you understand how devices connect, you understand how attackers exploit those connections.

### Key Concepts
- A network = devices connected to communicate and share resources
- Networks can be small (2 devices) or massive (the entire Internet)
- Networks are everywhere — not just in computing

### Final Outcome
Understood what a network is, why it matters, and how it applies to cybersecurity.

---

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

### Final Outcome
Understood how the Internet evolved, the difference between private and public networks, and how devices identify each other.

---

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

### Final Outcome
Understood IP addresses, MAC addresses, the difference between IPv4 and IPv6, and the security risk of MAC spoofing.

---

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

### Final Outcome
Understood what ports are, why standards exist, common port numbers and their purposes, and how non-standard ports must be explicitly specified.

---

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

### Final Outcome
Understood the difference between packets and frames, why data is broken into packets, how encapsulation works across OSI layers, and the purpose of key packet header fields.

---

## Task 6: Fundamentals of Computer Networking — Networking Devices

### What I Learned
Network devices are the hardware that lets data move within and between networks. They work at different layers of the OSI model, control traffic flow, connect networks together, and enforce security. A device's "intelligence" comes from two parts: a **physical component** (memory) and a **logical component** (operating system).

Each device has a specific job:
- **Hub (Layer 1):** Broadcasts incoming data to every connected device without checking the destination. This causes collisions and wastes bandwidth. It works in half-duplex mode and is called a multiport repeater because it only retransmits electrical signals.
- **Switch (Layer 2):** Uses MAC address tables to send frames only to the intended device inside a LAN, improving speed, efficiency and security.
- **Access Point (Layer 1/2):** Extends a wired network by giving wireless (Wi-Fi) access to laptops, phones and IoT devices. Modern APs support Wi-Fi 6, MU-MIMO, beamforming and interference detection.
- **Router (Layer 3):** Connects different networks and forwards packets by destination IP address using a routing table. It also handles path selection, NAT, DHCP, firewalling, VPN support and QoS.
- **Firewall:** Monitors and controls traffic based on security rules. Next-Generation Firewalls use Deep Packet Inspection (DPI) to analyse full packet contents and enforce application-level controls.
- **IDPS:** An **IDS** passively monitors traffic and raises alerts (a security alarm). An **IPS** sits inline and automatically blocks threats by dropping malicious packets or resetting connections.
- **VPN:** Creates an encrypted tunnel over the public internet for secure remote access. Types: Site-to-Site, Remote Access, and Hybrid.
- **Multilayer Switch (Layer 2 + 3):** Switches by MAC and routes by IP at wire-speed using ASIC hardware. It enables inter-VLAN routing without a separate router.

### Key Concepts
| Device | Layer | Key Behaviour |
|---|---|---|
| Hub | 1 | Broadcasts to all ports, causes collisions |
| Switch | 2 | Forwards using MAC address table |
| Router | 3 | Forwards using IP address, connects networks |
| Multilayer Switch | 2 + 3 | Switching + routing in hardware (ASIC) |
| Firewall | — | Filters traffic by rules, DPI in NGFW |
| IDS / IPS | — | IDS alerts only; IPS blocks inline |
| VPN | — | Encrypted tunnel over public internet |

### Final Outcome
Understood the role and OSI layer of each major networking device, and how to tell similar devices apart (hub vs switch, IDS vs IPS, router vs multilayer switch).

---

## Task 7: Protocols — DNS

### What I Learned
**DNS (Domain Name System)** is the phonebook of the Internet. It converts human-friendly domain names into IP addresses, for example `google.com` → `142.250.195.78`. Without DNS we would have to remember long numbers instead of names.

Analogy: you do not remember everyone's phone number — you save their name. DNS works the same way for websites.

When a browser needs a website, it asks a DNS resolver to look up the IP address. The resolver finds the answer and returns it, and the browser then connects to that IP.

### Key Concepts
- DNS translates domain names → IP addresses
- Works like a phonebook for the Internet
- Makes the Internet usable without memorising IP addresses
- Completed the downloadable DNS task document for this task

### Final Outcome
Understood the purpose of DNS and how it lets users reach websites by name instead of IP address.

---

## Task 8: Protocols — DHCP

### What I Learned
Every device joining a network needs an **IP address + subnet mask**, a **default gateway (router)** and a **DNS server**. These can be set manually (mostly done for servers, which need fixed IPs and do not move between networks) or automatically using **DHCP (Dynamic Host Configuration Protocol)**.

Automatic configuration means no manual setup, no IP conflicts (two devices with the same IP), and seamless use on mobile devices.

DHCP is an **application-layer protocol** that uses **UDP**. The server listens on **port 67** and the client sends from **port 68**.

### The DORA Process
| Step | What Happens |
|---|---|
| **D**iscover | Client broadcasts: "Is there any DHCP server out there?" |
| **O**ffer | Server replies with an available IP address |
| **R**equest | Client asks to use that IP address |
| **A**cknowledge | Server confirms — the IP is now leased to the client |

During this exchange the client has no IP yet, so it uses source `0.0.0.0` → destination `255.255.255.255` (broadcast). At the data-link layer it sends to the broadcast MAC `ff:ff:ff:ff:ff:ff`.

### Commands Used
| Purpose | Windows | Linux/Mac |
|---|---|---|
| View full network configuration | `ipconfig /all` | `ifconfig` or `ip a` |
| Release current IP | `ipconfig /release` | `sudo dhclient -r` |
| Request a new IP | `ipconfig /renew` | `sudo dhclient` |

If no DHCP server is available, the system assigns itself an **APIPA** address (169.254.x.x).

### Final Outcome
Understood how DHCP automatically configures devices, the four DORA steps, the ports it uses, and how to view and renew an IP lease from the command line.

---

## Task 9: Protocols — ICMP

### What I Learned
**ICMP (Internet Control Message Protocol)** is used for network diagnostics and error reporting. It helps devices report problems and test connectivity. The two main tools built on it are **ping** and **traceroute/tracert**.

### Ping
Ping works like ping-pong between two computers:
- Sender sends an **ICMP Echo Request (Type 8)**
- Target replies with an **ICMP Echo Reply (Type 0)**

It tells you whether the target is alive, measures Round-Trip Time (RTT), and shows packet loss. No packet loss means a stable connection; high RTT suggests delay. If there is no reply, the target may be offline or a firewall may be blocking ICMP.

### Traceroute
Traceroute maps the path (hops) packets take, using the **TTL (Time-To-Live)** field:
- Each packet starts with a TTL value
- Every router reduces TTL by 1
- When TTL reaches 0, the router drops the packet and sends back **ICMP Time Exceeded (Type 11)**

This makes each router along the path reveal itself, showing its IP and the delay at each hop. A line of `* * *` means a router did not respond or ICMP is blocked.

### Key Concepts
| Item | Detail |
|---|---|
| Echo Request | ICMP Type 8 |
| Echo Reply | ICMP Type 0 |
| Time Exceeded | ICMP Type 11 |
| Field used by traceroute | TTL |
| `* * *` in traceroute | Router not responding / ICMP blocked |

### Final Outcome
Understood how ICMP supports ping and traceroute, the ICMP message types involved, and how firewalls can affect the results.

---

## Task 10: Protocols — HTTP(S)

### What I Learned
**HTTP (HyperText Transfer Protocol)** is the protocol used whenever you access a website. It was created by **Tim Berners-Lee** and his team between 1989 and 1991. It defines the rules a web browser (client) uses to communicate with a web server to request and receive HTML pages, images, videos and other resources.

**HTTPS (HyperText Transfer Protocol Secure)** is the secure version. It uses **SSL/TLS encryption** so that:
- Data cannot be easily intercepted or read by attackers
- The website is authentic and not a fake or impersonated server

### Hands-on Observations
- Visited `http://example.com` and `https://example.com` in two tabs and compared them
- HTTP shows a "Not secure" warning; HTTPS shows a padlock (secure connection indicator)
- In Developer Tools → Network tab, the page request uses the **GET** method and returns status code **200 (OK)**
- Checked the certificate of `https://gmail.com` and `https://meta.com` to see the **Certificate Authority (CA)** that issued it and the **Common Name (CN)** it was issued to

### Key Concepts
| Item | Detail |
|---|---|
| Secure web protocol | HTTPS |
| Created by | Tim Berners-Lee |
| Encryption technology | SSL/TLS |
| Request method seen | GET |
| Status code seen | 200 |
| Certificate info | CA = who issued it, CN = domain it was issued to |

### Final Outcome
Understood the difference between HTTP and HTTPS, how encryption and certificates build trust, and how to inspect requests and certificates in the browser.

---

## Task 11: Protocols — Other Important Models (OSI)

### What I Learned
The **OSI (Open Systems Interconnection) model** is a theoretical framework that splits network communication between two devices into seven abstraction layers. Its main purpose is educational, but vendors and cloud providers still use it as shorthand.

- **Layer 1 – Physical:** Transmits raw bits over a physical connection
- **Layer 2 – Data Link:** Organises bits into frames and delivers them to the correct destination (Ethernet lives here)
- **Layer 3 – Network:** Routes data across networks (the IP part of TCP/IP)
- **Layer 4 – Transport:** End-to-end communication between nodes (TCP and UDP)
- **Layers 5–7 – Session, Presentation, Application:** Too fine-grained in practice, so usually collapsed into one application layer (e.g. HTTP)

### TCP vs UDP
- **TCP:** Reliable. Splits data into segments with sequence numbers so the receiver can reassemble them in order, and provides error checking.
- **UDP:** Simpler and faster. No reliability guarantees — packets are sent and the receiver discards any that are bad.

### Encapsulation Example (HTTP request)
1. Application layer adds the HTTP header
2. Transport layer adds a TCP header (source port, destination port, sequence number)
3. Network layer adds an IP header (source and destination IP)
4. Data link layer adds a MAC header (usually the MAC of the next-hop router, not the final server)
5. Physical layer sends raw bits — the server removes headers layer by layer in reverse

Cloud load balancers use this shorthand: **L4** operates at TCP level, **L7** operates at the application protocol level (HTTP/HTTPS).

### Final Outcome
Understood the seven OSI layers, how TCP and UDP differ, and how data is encapsulated and decapsulated as it travels across a network.

---

## Task 12: Windows — Introduction

### What I Learned
Windows is the most widely used desktop operating system, which also makes it one of the most common targets for attackers. Understanding how it is structured is a basic skill for both defence and offence in cybersecurity.

Key parts of Windows covered:
- **Desktop & File Explorer:** the graphical interface for navigating files and folders
- **File system (NTFS):** organises files and supports permissions, encryption and journaling
- **Settings & Control Panel:** where system configuration is managed
- **Task Manager:** shows running processes, CPU/memory usage and startup programs

### Key Concepts
- Windows is widely used, so it is widely targeted
- NTFS is the default file system and supports file permissions
- Task Manager helps spot suspicious processes

### Final Outcome
Gained a basic understanding of the Windows environment and why knowing it matters for cybersecurity.

---

## Task 13: Windows — PowerShell

### What I Learned
**PowerShell** is a command-line shell and scripting language built on .NET. Unlike older shells that deal in plain text, PowerShell works with **objects**, which makes it powerful for automation and system administration. Commands are called **cmdlets** and follow a **Verb-Noun** pattern.

### Commands Used
| Command | Purpose |
|---|---|
| `Get-Help <cmdlet>` | Show help for a cmdlet |
| `Get-Command` | List available commands |
| `Get-Process` | List running processes |
| `Get-Service` | List services |
| `Get-ChildItem` | List files and folders (like `dir`/`ls`) |
| `Set-Location` | Change directory |
| `Get-Content <file>` | Read a file |

### Key Concepts
- Cmdlets use a Verb-Noun naming style
- PowerShell passes objects through the pipeline (`|`), not just text
- Attackers also use PowerShell, so it is important to monitor it

### Final Outcome
Understood what PowerShell is, how cmdlets are structured, and how to run basic system commands.

---

## Task 14: Windows — PowerShell vs CMD

### What I Learned
Both are command-line tools in Windows, but they differ a lot in power.

| Feature | CMD | PowerShell |
|---|---|---|
| Introduced | MS-DOS era | 2006 |
| Output type | Plain text | .NET objects |
| Scripting | Basic batch files (`.bat`) | Full scripting language (`.ps1`) |
| Command style | `dir`, `copy` | `Get-ChildItem`, `Copy-Item` |
| Automation | Limited | Strong, can manage the whole system |
| Remote management | Very limited | Built-in remoting |

CMD is simple and good for quick tasks. PowerShell is better for automation, administration and security work, but its power also makes it attractive to attackers.

### Key Concepts
- CMD = text-based, simple, older
- PowerShell = object-based, powerful, modern
- PowerShell can do everything CMD can do, and more

### Final Outcome
Understood the differences between CMD and PowerShell and when each one is appropriate.

---

## Task 15: Windows — System32

### What I Learned
`C:\Windows\System32` is one of the most important folders in Windows. It stores core system files, executables, DLLs and drivers that the operating system needs to run. Tools like `cmd.exe`, `powershell.exe` and `notepad.exe` live here.

Because the folder is so critical, it is protected and requires administrator rights to modify. Deleting or corrupting files in System32 can make Windows unstable or stop it from booting.

### Security Angle
Attackers often try to hide malware with names that look like System32 files, or replace legitimate files, so that they blend in. Knowing what normal looks like helps spot what does not belong.

### Key Concepts
- System32 holds core OS files and DLLs
- Protected by permissions — administrator rights required
- Never delete or edit files in it without knowing what they do

### Final Outcome
Understood what System32 is, why it is critical to Windows, and why it is a target for malware.

---

## Task 16: Windows — User Accounts & UAC

### What I Learned
Windows uses **user accounts** to control who can do what on a system.

- **Standard user:** can run apps and change personal settings, but cannot change system-wide settings
- **Administrator:** has full control over the system
- **Local vs Microsoft/domain accounts:** local accounts exist only on one machine; domain accounts are managed centrally

**UAC (User Account Control)** is a security feature that prompts for confirmation (or credentials) whenever a program tries to make changes that need administrator rights. This stops malware from silently changing the system.

### Key Concepts
- Principle of least privilege — use a standard account for daily work
- UAC prompts reduce the risk of unauthorised changes
- Administrator accounts are high-value targets for attackers

### Final Outcome
Understood Windows account types and how UAC protects the system from unauthorised changes.

---

## Task 17: Windows — Security

### What I Learned
Windows includes several built-in security tools:

- **Windows Defender / Microsoft Defender Antivirus:** real-time protection against malware
- **Windows Firewall:** filters inbound and outbound traffic using rules
- **Windows Update:** delivers security patches that fix known vulnerabilities
- **BitLocker:** full-disk encryption to protect data if a device is lost or stolen
- **Event Viewer:** logs system, security and application events for investigation

### Key Concepts
- Keep the system patched — most attacks use known vulnerabilities
- Layered security: antivirus + firewall + encryption + updates
- Logs (Event Viewer) are essential for detecting and investigating incidents

### Final Outcome
Understood the main built-in Windows security features and why a layered approach matters.

---

## Task 18: Linux — Introduction

### What I Learned
**Linux** is a free, open-source operating system kernel used in servers, cloud platforms, Android, embedded devices and most security tools. It is available in many **distributions** such as Ubuntu, Debian, Kali and Fedora. Kali Linux in particular is built for penetration testing.

Most work on Linux is done through the **terminal** using a shell such as Bash.

### Commands Used
| Command | Purpose |
|---|---|
| `pwd` | Show current directory |
| `ls` | List files and folders |
| `cd <dir>` | Change directory |
| `cat <file>` | Display file contents |
| `whoami` | Show current user |
| `man <cmd>` | Show the manual for a command |

### Key Concepts
- Linux is open source and widely used on servers and in security
- A distribution = kernel + tools + package manager
- The terminal is the main way to work with Linux

### Final Outcome
Understood what Linux is, why it is important in cybersecurity, and how to run basic terminal commands.

---

## Task 19: Linux — File Systems

### What I Learned
Linux organises everything in a single tree that starts at the root directory `/`. Everything — including devices — is treated as a file.

### Important Directories
| Directory | Purpose |
|---|---|
| `/` | Root of the whole file system |
| `/home` | Personal files of regular users |
| `/root` | Home directory of the root (admin) user |
| `/etc` | System configuration files |
| `/var` | Variable data such as logs |
| `/bin`, `/usr/bin` | Common executable programs |
| `/tmp` | Temporary files |
| `/dev` | Device files |

### File Permissions
Permissions are split into **read (r), write (w), execute (x)** for the **owner, group and others**. Example: `rwxr-xr--`. They can be changed with `chmod` and ownership with `chown`.

### Key Concepts
- Everything is a file in Linux
- `/etc` for configs, `/var/log` for logs
- Correct permissions are a core part of Linux security

### Final Outcome
Understood the Linux directory structure and how file permissions control access.

---

## Task 20: Others — Cryptography, Part 1

### What I Learned
**Cryptography** is the practice of protecting information by converting it into an unreadable form so that only the intended person can read it.

Key terms:
- **Plaintext:** the original readable message
- **Ciphertext:** the encrypted, unreadable message
- **Encryption / Decryption:** converting plaintext to ciphertext and back
- **Key:** the secret value used to encrypt and decrypt

### Types of Cryptography
| Type | Keys | Example |
|---|---|---|
| Symmetric | Same key to encrypt and decrypt | AES |
| Asymmetric | Public key encrypts, private key decrypts | RSA |
| Hashing | One-way, no key, produces a fixed-size digest | SHA-256 |

### Key Concepts
- Symmetric is fast but the key must be shared safely
- Asymmetric solves key sharing but is slower
- Hashing cannot be reversed and is used to verify integrity

### Final Outcome
Understood the basic terms and the three main types of cryptography.

---

## Task 21: Others — Cryptography, Part 2

### What I Learned
This part built on the basics and looked at how cryptography is used in the real world.

- **Hashing for passwords:** systems store the hash of a password, not the password itself. Salting adds random data so identical passwords do not produce the same hash.
- **Digital signatures:** created with a private key and verified with a public key, proving who sent a message and that it was not altered.
- **Digital certificates & PKI:** certificates bind a public key to an identity, and a trusted Certificate Authority (CA) vouches for it. This is what powers HTTPS.
- **Encoding vs encryption:** encoding (such as Base64) only changes format and is not secure; encryption needs a key.

### Key Concepts
- Salted hashes protect stored passwords
- Digital signatures give authenticity and integrity
- Base64 is encoding, not encryption

### Final Outcome
Understood how hashing, signatures and certificates are used to secure real systems.

---

## Task 22: Others — Cipher Breaker Challenge

### What I Learned
This challenge applied cryptography ideas by decoding messages hidden with classical ciphers and encodings.

### Common Techniques Used
| Technique | Idea |
|---|---|
| Caesar cipher | Each letter is shifted by a fixed number; broken by trying all 25 shifts |
| ROT13 | A Caesar shift of 13 — applying it twice returns the original |
| Base64 | Encoding of binary data into text characters, easily reversed |
| Hex / Binary | Different representations of the same data |
| Frequency analysis | Using how often letters appear to crack substitution ciphers |

### Key Concepts
- Classical ciphers are weak because the key space is small
- Recognising the pattern of the text (e.g. `==` at the end for Base64) is the first step
- Online decoders can help, but understanding the method matters more

### Final Outcome
Practised identifying and breaking simple ciphers and encodings and understood why they are not secure.

---

## Task 23: Principles of Cybersecurity — CIA

### What I Learned
The **CIA Triad** is the foundation of information security. It has three goals:

- **Confidentiality:** only authorised people can access the information
- **Integrity:** information stays accurate and is not changed without permission
- **Availability:** systems and data are accessible when needed

### Key Concepts
| Principle | Protects Against | Example Control |
|---|---|---|
| Confidentiality | Data leaks, eavesdropping | Encryption, access control |
| Integrity | Tampering, corruption | Hashing, digital signatures |
| Availability | Downtime, DDoS | Backups, redundancy |

### Final Outcome
Understood the three goals of the CIA Triad and how they guide security decisions.

---

## Task 24: Principles of Cybersecurity — CIA Explanation

### What I Learned
This task explained each part of the CIA Triad through real-life examples.

- **Confidentiality:** a hospital must keep patient records private. Breach example: stolen customer data.
- **Integrity:** a bank transfer must not be altered in transit. Breach example: someone changing the amount in a transaction.
- **Availability:** a website must stay online for users. Breach example: a DDoS attack or ransomware locking files.

Security often involves trade-offs — making a system extremely confidential (very strict access) can reduce its availability, so a balance is needed based on what is being protected.

### Key Concepts
- Every attack can be mapped to a failure of C, I or A
- Controls must balance all three goals
- Ransomware and DDoS mainly attack availability

### Final Outcome
Understood how confidentiality, integrity and availability apply in real scenarios and how attacks relate to each one.

---

## Task 25: Path 1 — Red Teaming

### What I Learned
**Red teaming** is an authorised, simulated attack on an organisation to test how well its people, processes and technology can detect and respond to a real adversary. The **red team** plays the attacker, while the **blue team** defends.

Unlike a basic vulnerability scan, a red team engagement is goal-based and mimics real attacker behaviour across the whole attack chain.

### Typical Stages
1. **Reconnaissance:** gathering information about the target
2. **Initial access:** finding a way in
3. **Privilege escalation:** gaining higher-level access
4. **Lateral movement:** moving to other systems
5. **Objective / reporting:** reaching the agreed goal and documenting findings for the defenders

### Key Concepts
- Red teaming is always **authorised** and within an agreed scope
- Red = attackers, Blue = defenders, Purple = both working together
- The outcome is a report that helps the organisation improve its defences

### Final Outcome
Understood what red teaming is, how it differs from vulnerability scanning, and the stages of a typical engagement.

---

## Task 26: Red Teaming Continuation

### What I Learned
This task continued the red teaming path and strengthened the idea that attackers follow a structured process, and that defenders can map to it.

- **Frameworks:** the Cyber Kill Chain and MITRE ATT&CK describe attacker tactics and techniques in a common language
- **Rules of engagement:** define scope, timing, and what is off-limits so testing stays legal and safe
- **Reporting:** findings must be clear, prioritised and include recommendations so the organisation can fix them
- **Ethics:** a red teamer must have written permission, protect any data found, and never go beyond scope

### Key Concepts
- MITRE ATT&CK maps real attacker techniques
- Written authorisation is mandatory before any testing
- Good reports turn findings into improvements

### Final Outcome
Understood how red teams use frameworks, rules of engagement and reporting, and why ethics and authorisation are essential.


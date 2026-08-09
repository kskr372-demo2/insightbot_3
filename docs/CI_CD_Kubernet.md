GKE (Google Kubernetes Engine)

Developer
   ↓
git push
   ↓
GitHub Actions
   ├── Tests
   ├── Docker Build
   └── Push Image
          ↓
   Container Registry
          ↓
   ┌─────────────────────────────┐
   │ Choose ONE deployment target│
   └─────────────────────────────┘
          ↓
   ┌──────────┬──────────┬─────────────┐
   │          │          │             │
  ECS       Kubernetes   Cloud Run    Azure
  (AWS)     (EKS/GKE)    (GCP)        etc.

##############################################################################

  Developer
   ↓
git push
   ↓
GitHub
   ↓
GitHub Actions
   │
   ├── CI
   │    ├── Run tests
   │    └── Build Docker image
   │
   └── CD
        ├── Push image to Artifact Registry
        └── Deploy image to Cloud Run
                    ↓
              InsightBot FastAPI

#################################################
GitHub Actions
      │
      │ CI
      ├── pytest
      └── docker build
             │
             ▼
     Artifact Registry
     (stores image)
             │
             │ CD
             ▼
        Cloud Run
     (runs/deploys image)

###########################################################################

| Platform               | Common container registry                        |
| ---------------------- | ------------------------------------------------ |
| **Google Cloud (GCP)** | **Google Artifact Registry**                     |
| **AWS**                | **Amazon ECR (Elastic Container Registry)**      |
| **Azure**              | **Azure Container Registry (ACR)**               |
| **GitHub**             | **GitHub Container Registry (GHCR)**             |
| **Kubernetes**         | ❗ Kubernetes itself has **no built-in registry** |
######################

Important: Kubernetes

Kubernetes runs containers; it doesn't normally store your Docker images.
******************
GitHub Actions
      ↓
Google Artifact Registry
      ↓
GKE (Kubernetes)
      ↓
Pod
      ↓
Your FastAPI container
*********************

Or with AWS:

GitHub Actions
      ↓
Amazon ECR
      ↓
EKS (Kubernetes)
      ↓
Pod
      ↓
Your FastAPI container

****************************

Cloud Run

Your chosen GCP architecture is:

GitHub Actions
      ↓
Google Artifact Registry
      ↓
Cloud Run
      ↓
InsightBot

############################################################
So the general production pattern is:

                 Container Registry
                       ↓
              ┌────────┴────────┐
              ↓                 ↓
          Cloud Run          Kubernetes
          ECS                 EKS/GKE
          Azure              etc.

Registry = stores your Docker image.
Runtime/orchestrator = pulls the image and runs it.


##############################
Then the repository address will be:

asia-south1-docker.pkg.dev/my-insightbot-project/insightbot

Google uses this general naming structure:

LOCATION-docker.pkg.dev/PROJECT-ID/REPOSITORY



#####################################################
What we'll create

We'll create four things:

1. Service Account
       ↓
2. Artifact Registry permission
       ↓
3. Workload Identity Pool
       ↓
4. GitHub OIDC Provider

Step 5 — Connect GitHub to the Service Account

Step 6 — Update ci.yml

GitHub Push
    ↓
Checkout
    ↓
Python setup
    ↓
Install dependencies
    ↓
Tests
    ↓
Authenticate to GCP ← NEW
    ↓
Configure Docker ← NEW
    ↓
Build Docker image
    ↓
Push Docker image ← NEW
    ↓
Artifact Registry


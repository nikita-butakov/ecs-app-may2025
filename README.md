# 🚀 ECS Demo App — My DevOps Project with AWS ECS & GitHub Actions

Hi! I’m **Nikita**, a DevOps Engineer, and this is my personal project where I built and deployed a Python web app to **AWS ECS Fargate** using **Docker** and **GitHub Actions** — fully automated from code to production.

> 🎯 The goal was to practice and demonstrate real DevOps skills using cloud-native services and CI/CD automation.

---

## 🧰 Technologies Used

- 🐍 **Python + Flask** — simple REST-style web application  
- 🐳 **Docker** — for containerization  
- 📦 **Amazon ECR** — to store Docker images  
- ☁️ **Amazon ECS Fargate** — for serverless container deployment  
- 🤖 **GitHub Actions** — for continuous integration & delivery

---

## 🌍 What the App Does

When deployed, the app renders a simple HTML page showing project info.

- The logic is in `app.py`, which uses **Flask** to serve HTML  
- Styling is included inline for simplicity

---

## 🛠️ Steps I Followed

1. ✅ Created a basic Python web application (`app.py`)  
2. 📝 Wrote a `Dockerfile` to containerize the app  
3. 🗂️ Created an Amazon **ECR** repository to host the image  
4. ⚙️ Set up **GitHub Actions** workflow (`.github/workflows/deploy.yml`)  
5. 🔐 Configured GitHub Secrets (AWS credentials, region, ECR repo info)  
6. 📤 Pushed the Docker image to ECR automatically via CI/CD  
7. ☁️ Created an **ECS Fargate** cluster and task definition  
8. 📦 Launched a **Service** in ECS using the task  
9. 🌐 Attached an **Application Load Balancer (ALB)**  
10. 🔎 Accessed the app via public ALB URL

---

## 🔐 GitHub Secrets Used

For secure CI/CD automation, the following **GitHub Secrets** were configured:

| Secret Name             | Description                                  |
|-------------------------|----------------------------------------------|
| `AWS_ACCESS_KEY_ID`     | IAM user's access key for AWS CLI            |
| `AWS_SECRET_ACCESS_KEY` | IAM user's secret access key                 |
| `AWS_REGION`            | AWS region where services are deployed       |
| `ECR_REGISTRY`          | Amazon ECR registry URI                      |
| `ECR_REPOSITORY`        | Name of the ECR repository                   |
| `ECS_CLUSTER_NAME`      | Name of the ECS cluster                      |
| `ECS_SERVICE_NAME`      | Name of the ECS service to update            |

> These secrets are referenced in the GitHub Actions workflow for authentication, image push, and ECS deployment.

---

## 📸 Demo Screenshots

### ✅ Initial Deployment

After the first successful CI/CD run in GitHub Actions, the new container was deployed. I opened the **ALB URL** in the browser and saw my project page:

<img src="https://github.com/nikita-butakov/ecs-app-may2025/blob/main/demo_screenshots/main_page.JPG?raw=true" alt="Main Page" width="800"/>

---

### 🧪 Testing CI/CD Update

I updated the `app.py` file and pushed the changes to GitHub. CI/CD was triggered:

- ✅ A **new container** was deployed automatically  
- ❌ The **old container** was stopped — with zero downtime

<img src="https://github.com/nikita-butakov/ecs-app-may2025/blob/main/demo_screenshots/new_container_task.JPG?raw=true" alt="New ECS Task" width="800"/>

---

### 📄 Verified the Update

I checked the ALB URL again — the updated content was live!

<img src="https://github.com/nikita-butakov/ecs-app-may2025/blob/main/demo_screenshots/main_page_updated.JPG?raw=true" alt="Updated Main Page" width="800"/>

---

### 🖥️ AWS Views

**Application Load Balancer:**

<img src="https://github.com/nikita-butakov/ecs-app-may2025/blob/main/demo_screenshots/alb.JPG?raw=true" alt="ALB Screenshot" width="800"/>

**ECS Cluster & Fargate Service:**

<img src="https://github.com/nikita-butakov/ecs-app-may2025/blob/main/demo_screenshots/ecs_cluster.JPG?raw=true" alt="ECS Cluster" width="800"/>

---

## 👤 Author

**Nikita Butakov**  
DevOps • Cloud • Automation  

- 🔗 [LinkedIn](https://linkedin.com/in/nikitabutakov)  
- 🐙 [GitHub](https://github.com/nikitabutakov)

---

## 📅 Project Date

**19 May 2025**

---

Thanks for reading! 🙌

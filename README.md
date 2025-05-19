# 🚀 ECS Demo App — My DevOps Project with AWS ECS & GitHub Actions

Hi! I’m **Nikita**, a DevOps Engineer, and this is my personal project where I built and deployed a Python web app to **AWS ECS Fargate** using **Docker** and **GitHub Actions** — fully automated from code to production.

> 🎯 The goal was to practice and demonstrate real DevOps skills using cloud-native services and CI/CD automation.

---

## 🧰 Technologies Used

- 🐍 **Python + Flask** — for a simple REST-style web application  
- 🐳 **Docker** — to containerize the app  
- 📦 **Amazon ECR** — to store Docker images  
- ☁️ **Amazon ECS Fargate** — for serverless container deployment  
- 🤖 **GitHub Actions** — for continuous integration and deployment (CI/CD)

---

## 🌍 What the App Does

When deployed, the app renders a simple HTML page showing project info.

- The logic is in `app.py`, which uses **Flask** to serve HTML
- The styling is included directly in the response (for simplicity)

---

## 🛠️ Steps I Followed

1. ✅ Created a basic Python web application (`app.py`)
2. 📝 Wrote a `Dockerfile` to containerize the app
3. 🗂️ Created an Amazon **ECR** repository for storing the image
4. ⚙️ Set up **GitHub Actions** workflow (`.github/workflows/deploy.yml`)
5. 🔐 Configured GitHub Secrets (AWS credentials, region, ECR repo info)
6. 📤 Pushed Docker image to ECR automatically from GitHub Actions
7. ☁️ Created an **ECS Fargate** cluster and task definition
8. 📦 Deployed a **Service** in ECS using the task
9. 🌐 Attached an **Application Load Balancer (ALB)**
10. 🔎 Accessed the app via public ALB URL

---

## 📸 Demo Screenshots

### ✅ Initial Deployment

After a successful CI/CD run in GitHub Actions, the new container was deployed. I opened the **ALB URL** in the browser and saw my project page.

🖼️ _Screenshot 1_

---

### 🧪 Testing Update via CI/CD

I changed the `app.py` file and committed the update. GitHub Actions ran the pipeline again:

- A **new container** was launched in ECS  
- The **old one was stopped automatically** — zero downtime!

🖼️ _Screenshot 2_

---

### 📄 Verified Update

I checked the ALB URL again, and the **new content** was visible. Everything worked as expected.

🖼️ _Screenshot 3_

---

### 🔄 AWS Components

- **Application Load Balancer view in AWS:**

🖼️ _Screenshot 4_

- **ECS Cluster & Fargate service view:**

🖼️ _Screenshot 5_

---

## 👤 Author

**Nikita Butakov**  
DevOps | Cloud | Automation  
🔗 [LinkedIn](https://linkedin.com/in/nikitabutakov)  
🐙 [GitHub](https://github.com/nikitabutakov)

---

## 📅 Project Date

**19 May 2025**

---

Thanks for reading! 🙌  



from flask import Flask

app = Flask(__name__)

@app.route("/")
def project_page():
    return """
    <html>
        <head>
            <title>DevOps Project – ECS CI/CD</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background-color: #f4f4f4;
                    text-align: center;
                    padding-top: 50px;
                }
                .container {
                    background-color: white;
                    padding: 40px;
                    border-radius: 10px;
                    box-shadow: 0 0 10px rgba(0,0,0,0.1);
                    display: inline-block;
                }
                h1 {
                    color: #2c3e50;
                }
                p {
                    font-size: 18px;
                }
                a {
                    color: #2980b9;
                    text-decoration: none;
                    font-weight: bold;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🚀 DevOps Project – AWS ECS CI/CD</h1>
                <p>🛠️ Stack: Python, Docker, GitHub Actions, ECS Fargate, ALB</p>
                <p>🌐 <a href="http://app-may2025-alb-1887390314.ca-central-1.elb.amazonaws.com/" target="_blank">Live Demo</a></p>
                <p>👤 Author: Nikita Butakov</p>
                <p>📅 Date: 19 May 2025</p>
            </div>
        </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)


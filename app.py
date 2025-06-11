from flask import Flask
app = Flask(__name__)

@app.route('/')
def portfolio():
    return '''
    <html>
        <head>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                    color: #333;
                }
                .header {
                    background-color: #4CAF50;
                    color: white;
                    padding: 20px;
                    text-align: center;
                }
                .container {
                    padding: 20px;
                }
                .about, .projects, .contact {
                    margin-bottom: 20px;
                }
                .project-item {
                    margin-bottom: 10px;
                    padding: 10px;
                    border: 1px solid #ddd;
                }
                .project-title {
                    font-weight: bold;
                    color: #4CAF50;
                }
                .footer {
                    background-color: #4CAF50;
                    color: white;
                    text-align: center;
                    padding: 10px;
                    position: fixed;
                    width: 100%;
                    bottom: 0;
                }
            </style>
        </head>
        <body>
            <div class="header">
                <h1>Shreyasri Balla</h1>
                <p>DevOps Engineer | Web Developer</p>
            </div>
            
            <div class="container">
                <div class="about">
                    <h2>About Me</h2>
                    <p>Dynamic and detail-oriented DevOps Engineer with 2 years of experience specializing in CI/CD pipelines, infrastructure automation, and monitoring solutions.<br>
                       Hands-on expertise with tools like Docker, Kubernetes, Ansible, Terraform, and cloud services such as AWS EC2, EKS, and RDS. Proficient in designing scalable infrastructure,<br> 
                       streamlining deployments, and implementing monitoring solutions to ensure high availability and reliability of applications.</p>
                </div>
                
                <div class="projects">
                    <h2>Projects</h2>
                    <div class="project-item">
                        <p class="project-title">Project 1: End-to-End Deployment of a Three-Tier Application on AWS EKS Cluster using GitOps</p>
                        <p>Objective: Led the deployment of a three-tier application on AWS EKS, utilizing GitOps with ArgoCD to automate and streamline the delivery process.</p>
                        <p><b>Key Achievements:</b></p>
                        <ul>
                            <li>Infrastructure Automation: Reduced setup time by 30% using Terraform for AWS provisioning.</li>
                            <li>CI/CD Pipeline: Achieved a 95% deployment success rate with zero downtime by implementing a Jenkins-driven CI/CD pipeline.</li>
                            <li>GitOps Integration: Cut manual intervention by 80% through ArgoCD integration, ensuring seamless synchronization between GitHub and EKS.</li>
                            <li>Monitoring Setup: Improved issue detection time by 40% with Prometheus and Grafana, enabling faster response to critical alerts.</li>
                        </ul>
                        <p><b>Impact:</b> Delivered a 99.9% deployment success rate, improved scalability, and reduced manual efforts by 90%, significantly enhancing operational efficiency and system reliability.</p>
                    </div>
                </div>
                
                <div class="contact">
                    <h2>Contact</h2>
                    <p>Email: shreyasrib03@gmail.com</p>
                    <p>LinkedIn: www.linkedin.com/in/shreyasriballa</p>
                </div>
            </div>
            
            <div class="footer">
                <p>&copy; 2024 Anjali Kota</p>
            </div>
        </body>
    </html>
    '''

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

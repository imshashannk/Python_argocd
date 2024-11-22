Modern software development is driven by automation, security, and scalability. In this project, I designed a complete CI/CD pipeline to deploy a Python application on a Kubernetes cluster using ArgoCD. The pipeline integrates essential tools for security, code quality, and monitoring, such as Trivy, Snyk, SonarQube, and Slack, to provide a seamless deployment experience with real-time feedback.

Key Features:
Python Web Application: A simple Flask application (app.py) with multiple routes.
Kubernetes Deployment: Manifests for deployment, service, and ingress configurations.
GitHub Actions CI/CD: Automated workflows for building and deploying the application.
Image Scanning: Security checks using Trivy and Snyk.
Code Scanning: Integrated SonarQube for static code analysis.
Real-Time Notifications: Alerts and updates sent to Slack.
Ingress Path-Based Routing: Configured routing for specific paths to handle traffic efficiently.

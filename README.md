# Project-1 : Automated-CI-CD-Pipeline-for-Microservices-on-AWS
Automate the build, test, containerization, and deployment of a microservices application using AWS-native DevOps tools.

🧱 1. **Architecture Overview**
 
- **Developer:** Pushes code changes to GitHub.  
- **CodePipeline:** Detects changes via webhook → orchestrates the flow.  
- **CodeBuild:** Builds Docker image, runs tests, and pushes image to ECR.  
- **ECR:** Stores built Docker images.  
- **CodeDeploy:** Deploys the new version to ECS (Fargate).  
- **ECS (Fargate):** Runs the containerized microservice behind a Load Balancer.

-------------------------------------------------------------------------------------------------------

⚙️ 2. **AWS Services Used**
| Service                 | Purpose                                   |
| ----------------------- | ----------------------------------------- |
| **CodeCommit / GitHub** | Source repository for your microservices  |
| **CodePipeline**        | Orchestrates CI/CD workflow               |
| **CodeBuild**           | Builds & tests code, creates Docker image |
| **ECR**                 | Stores Docker images                      |
| **ECS (Fargate)**       | Runs containerized app                    |
| **CodeDeploy**          | Handles blue/green or rolling deployments |
| **CloudWatch**          | Monitors build & deployment logs          |
| **SNS (optional)**      | Sends pipeline notifications              |

                                      

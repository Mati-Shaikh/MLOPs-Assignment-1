pipeline {
    agent any

    environment {
        DOCKER_HUB_CREDENTIALS = credentials('docker-hub-credentials') // Use your credential ID
        DOCKER_IMAGE_NAME = 'matishaikh77/mlops-assignment-1'
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image
                    sh "docker build -t ${DOCKER_IMAGE_NAME}:${env.BUILD_ID} ."
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    // Log in to Docker Hub
                    sh "echo ${DOCKER_HUB_CREDENTIALS_PSW} | docker login -u ${DOCKER_HUB_CREDENTIALS_USR} --password-stdin"

                    // Push the Docker image
                    sh "docker push ${DOCKER_IMAGE_NAME}:${env.BUILD_ID}"
                }
            }
        }
    }

    post {
        success {
            // Send email notification on successful deployment
            emailext body: 'The deployment was successful!', subject: 'Deployment Notification', to: 'matishaikh7@gmail.com'
        }
        failure {
            // Send email notification on failure
            emailext body: 'The deployment failed!', subject: 'Deployment Failure Notification', to: 'matishaikh7@gmail.com'
        }
    }
}
pipeline {
    agent any

    environment {
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
                withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', usernameVariable: 'DOCKER_HUB_USR', passwordVariable: 'DOCKER_HUB_PSW')]) {
                    script {
                        // Log in to Docker Hub
                        sh "echo ${DOCKER_HUB_PSW} | docker login -u ${DOCKER_HUB_USR} --password-stdin"

                        // Push the Docker image
                        sh "docker push ${DOCKER_IMAGE_NAME}:${env.BUILD_ID}"
                    }
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
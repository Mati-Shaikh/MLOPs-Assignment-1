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
                    docker.build("${DOCKER_IMAGE_NAME}:${env.BUILD_ID}")
                }
            }
        }

        stage('Push to Docker Hub') {
    steps {
        script {
            docker.withRegistry('https://index.docker.io/v1/', 'docker-hub-credentials') {
                docker.image("${DOCKER_IMAGE_NAME}:${env.BUILD_ID}").push('latest')
                docker.image("${DOCKER_IMAGE_NAME}:${env.BUILD_ID}").push("${env.BUILD_ID}")
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
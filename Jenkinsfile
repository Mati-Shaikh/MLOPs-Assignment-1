pipeline {
    agent any

    triggers {
        githubPush() // Trigger the pipeline on GitHub push events
    }

    environment {
        DOCKER_HUB_CREDENTIALS = credentials('docker-hub-credentials') // Use your Docker Hub credential ID
        DOCKER_IMAGE_NAME = 'matishaikh77/mlops-assignment-1'
    }

    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm // Check out the source code from GitHub
            }
        }

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
                        docker.image("${DOCKER_IMAGE_NAME}:${env.BUILD_ID}").push('latest') // Push as 'latest'
                        docker.image("${DOCKER_IMAGE_NAME}:${env.BUILD_ID}").push("${env.BUILD_ID}") // Push with build ID
                    }
                }
            }
        }
    }

    post {
        success {
            // Send email notification on successful deployment
            emailext body: 'The deployment was successful!', subject: 'Deployment Notification', to: 'fypstructify@gmail.com'
        }
        failure {
            // Send email notification on failure
            emailext body: 'The deployment failed!', subject: 'Deployment Failure Notification', to: 'fypstructify@gmail.com'
        }
    }
}

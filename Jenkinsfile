pipeline {
    agent any
    environment {
      COMPOSE_PROJECT_NAME = "${env.JOB_NAME}-${env.BUILD_ID)"}
    }
    stages {
        stage ('Build') {
            steps{
              sh '/usr/local/bin/docker-compose build'
              sh '/usr/local/bin/docker-compose up'
            }
        }
    post {
        sh "/usr/local/bin/docker-compose down -v"
      }
    }
}

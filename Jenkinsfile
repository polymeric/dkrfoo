pipeline {
    agent none
    stages {
        stage ('Build') {
            agent { 
                none 
            }
            steps{
              sh '/usr/local/bin/docker-compose up'
              sh '/usr/local/bin/docker-compose up'
            }
        }
    }
}

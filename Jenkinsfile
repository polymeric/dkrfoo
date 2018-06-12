pipeline {
    agent none
    stages {
        stage ('Build') {
            agent { 
                dockerfile {
                }
            }
            steps{
              sh '/usr/local/bin/docker-compose up'
            }
        }
    }
}

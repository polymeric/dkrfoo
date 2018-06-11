pipeline {
    agent none
    stages {
        stage ('Build') {
            agent { 
                dockerfile {
                }
            }
            steps{
              sh 'docker-compose up'
            }
        }
    }
}

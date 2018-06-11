pipeline {
    agent none
    stages {
        stage ('Build') {
            agent { 
                dockerfile {
                }
            }
            steps{
              docker-compose up
            }
        }
    }
}

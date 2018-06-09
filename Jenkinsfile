pipeline {
    agent { none }
    stages {
        stage ('Build') {
            agent { dockerfile true }
            steps{
                sh 'scm --version'
            }
        }
    }
}

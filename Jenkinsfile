pipeline {
    agent none
    stages {
        stage ('Build') {
            /* agent { dockerfile true } */
            agent { dockerfile true }
            steps{
                sh 'env'               
                sh 'docker-compose up'
            }
        }
        stage('Test') {
            agent {
                docker {
                    image 'qnib/pytest'
                    args '-p 5000:5000'
                }
            }
            steps {
                sh 'py.test --verbose --junit-xml test-reports/results.xml tests/test_rest_api.py'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }
    }
}

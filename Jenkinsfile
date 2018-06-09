pipeline {
    agent none
    stages {
        stage ('Build') {
            agent { dockerfile true }
            steps{
                sh 'env'               
            }
        }
        stage('Test') {
            agent {
                docker {
                    image 'qnib/pytest'
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

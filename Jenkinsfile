pipeline {
    agent none
    stages {
        stage ('Build') {
            agent { 
                dockerfile {
                    additionalBuildArgs '--network host --tag=dkrsrv'
                }
            }
            steps{
                sh 'env'               
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

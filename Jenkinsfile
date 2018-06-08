pipeline {
    agent none
    stages {
        stage (build) {
            agent {
                docker {
                    image 'python:2-alpine'
                }
            }
            steps {
                sh 'python -m py_compile src/app.py'
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
            stage('Deliver') {
                agent {
                    docker {
                        image 'cdrx/pyinstaller-linux:python2'
                    }
                }
                steps {
                    sh 'pyinstaller --onefile sources/app.py'
                }
                post {
                    success {
                        archiveArtifacts 'dist/flask-app'
                    }
                }
            }
    }
}



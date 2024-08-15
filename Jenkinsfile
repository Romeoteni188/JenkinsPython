
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', 
                branches: [[name: '*/main']], 
                userRemoteConfigs: [[url: 'https://github.com/Romeoteni188/JenkinsPython.git']]])
            }
        }

        stage('Setup') {
            steps {
                script {
                    // Crear un entorno virtual y instalar las dependencias
                    sh '''
                    python -m venv venv
                    python3 -m venv venv3
                    venv/bin/pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Linting') {
            steps {
                script {
                    sh '''
                    venv/bin/pylint **/*.py
                    venv3/bin/pylint **/*.py
                    '''
                }
            }
        }

        stage('Unit Testing') {
            steps {
                script {
                    sh '''
                    venv/bin/python -m unittest discover -s tests/unit
                    venv3/bin/python -m unittest discover -s tests/unit
                    '''
                }
            }
        }

        stage('Integration Testing') {
            steps {
                script {
                    sh '''
                    venv/bin/python -m unittest discover -s tests/integration
                    ven3v/bin/python -m unittest discover -s tests/integration
                    '''
                }
            }
        }

        stage('Build') {
            steps {
                ansiColor('xterm') {
                    sh 'echo "Compilación exitosa..!"'
                }
            }
        }
    }

    post {
        failure {
            script {
                def msg = "Build error for ${env.JOB_NAME} ${env.BUILD_NUMBER} (${env.BUILD_URL})"
                slackSend message: msg, channel: env.SLACK_CHANNEL
            }
        }
    }
}


pipeline {
    agent any
    stages {
        stage('Check Git') {
            steps {
                script {
                    sh '''
                        if ! which git > /dev/null 2>&1; then
                            echo "Error: Git no está instalado."
                            exit 1
                        else
                            echo "Git está instalado."
                        fi
                    '''
                }
            }
        }

        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', 
                    branches: [[name: 'main']], 
                    userRemoteConfigs: [[url: 'https://github.com/Romeoteni188/JenkinsPython.git']]])
            }
        }

        stage('Setup') {
            steps {
                script {
                    // Suponiendo que python3-venv ya está instalado
                    sh '''
                        python3 -m venv venv
                        venv/bin/pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Linting') {
            steps {
                script {
                    sh 'venv/bin/pylint **/*.py'
                }
            }
        }

        stage('Testing') {
            steps {
                script {
                    sh 'venv/bin/python -m unittest test_unita.py'
                }
            }
        }

        stage('Build') {
            steps {
                ansiColor('xterm') {
                    sh 'echo "Compilación exitosa..!!"'
                }
            }
        }
    }
}

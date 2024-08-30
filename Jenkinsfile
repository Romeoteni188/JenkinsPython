pipeline {
    agent any
    stages {
        stage('Check and Install Git') {
            steps {
                script {
                    sh '''
                        if ! which git > /dev/null 2>&1; then
                            echo "Git no está instalado. Instalando..."
                            apt update -y
                            apt install git -y
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
                    sh '''
                        if ! dpkg -l | grep -q python3-venv; then
                            echo "python3-venv no está instalado. Instalando..."
                            apt update -y
                            apt install python3-venv -y
                        else
                            echo "python3-venv está instalado."
                        fi
                    '''
                    // Crear y activar el entorno virtual
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

        stage('Testing') { // Cambiado de 'Unit Testing' a 'Testing'
            steps {
                script {
                    // Ejecutar pruebas desde el archivo test_unita.py
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

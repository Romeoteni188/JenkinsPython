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
                    // Instalar python3-venv si no está instalado
                    sh '''
                    if ! dpkg -l | grep -q python3-venv; then
                        echo "python3-venv no está instalado. Instalando..."
                        sudo apt-get update
                        sudo apt-get install -y python3-venv
                    fi
                    '''
                    
                    // Crear un entorno virtual y instalar las dependencias
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
                    sh '''
                    venv/bin/pylint **/*.py
                    '''
                }
            }
        }

        stage('Unit Testing') {
            steps {
                script {
                    sh '''
                    venv/bin/python -m unittest discover -s tests/unit
                    '''
                }
            }
        }

        stage('Integration Testing') {
            steps {
                script {
                    sh '''
                    venv/bin/python -m unittest discover -s tests/integration
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
}

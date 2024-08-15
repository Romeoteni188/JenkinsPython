pipeline {
    
    stages {
        stage('Checkout') {
            steps {
                 checkout([$class: 'GitSCM', 
                 branches: [[name: '*/main']], userRemoteConfigs: [[url: 'https://github.com/Romeoteni188/JenkinsPython.git']]])
                 }
        }
        stage('Setup') {
            steps {
                script {
                    sh 
                    python -m venv venv
                    source venv/bin/activate
                    pip install -r requirements.txt
                    
                }
            }
        }
        stage('Linting') {
            steps {
                script {
                    sh """
                    pylint **/*.py
                    """
                }
            }
        }
        stage('Unit Testing') {
            steps {
                script {
                    sh """
                    python -m unittest discover -s tests/unit
                    """
                }
            }
        }
        stage('Integration Testing') {
            steps {
                script {
                    sh 
                    python -m unittest discover -s tests/integration
                    
                }
            }
        }
    }
    post {
        failure {
            script {
                msg = "Build error for ${env.JOB_NAME} ${env.BUILD_NUMBER} (${env.BUILD_URL})"
                slackSend message: msg, channel: env.SLACK_CHANNEL
            }
        }
    }
    stages {
        stage('Build') {
            steps {
                ansiColor('xterm') {
                    sh 'echo "Compilacion exitosa..!"'
                }
            }
        }
    }

}

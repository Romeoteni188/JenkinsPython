pipeline {
    agent any

    parameters {
        string(name: 'BRANCH_NAME', defaultValue: 'main', description: 'Branch de Git a usar')
        booleanParam(name: 'RUN_TESTS', defaultValue: true, description: '¿Ejecutar pruebas unitarias?')
    }

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/Romeoteni188/JenkinsPython.git', branch: "${params.BRANCH_NAME}"
            }
        }

        stage('Setup') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Linting') {
            steps {
                echo 'Linting'
            }
        }

        stage('Testing') {
            when {
                expression {
                    return params.RUN_TESTS
                }
            }
            steps {
                sh '''
                . venv/bin/activate
                python3 -m unittest test_unita
                '''
            }
        }

        stage('Build') {
            steps {
                echo 'Build successful'
            }
        }

        stage('Run Dependency Track') {
            steps {
                script {
                    load 'Jenkinsfile2'
                }
            }
        }

        stage('Wait for 4 Minutes') {
            steps {
                sleep(time: 4, unit: 'MINUTES')
            }
        }

        stage('Run Pandoc') {
            steps {
                script {
                    load 'Jenkinsfile3'
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
        success {
            echo 'Pipeline 1 completado exitosamente.'
        }
        failure {
            echo 'El pipeline 1 falló.'
        }
    }
}

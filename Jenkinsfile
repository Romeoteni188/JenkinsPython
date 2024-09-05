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

        stage('Start Dependency Track') {
            steps {
                sh 'docker-compose up -d'
            }
        }

        stage('Run Dependency Track') {
            steps {
                script {
                    // Esperar 60 segundos para que Dependency Track esté listo
                    sleep(time: 60, unit: 'SECONDS')
                }
                sh '''
                    docker exec dependencytrack/apiserver /bin/sh -c "dependency-track-command-to-run"
                    docker exec dependencytrack/apiserver /bin/sh -c "dependency-track-command-to-generate-xml"
                    docker cp dependencytrack/apiserver:/path/to/generated.xml ./workspace/generated.xml
                '''
            }
        }

        stage('Wait for 4 Minutes') {
            steps {
                sleep(time: 4, unit: 'MINUTES')
            }
        }

        // stage('Run Pandoc') {
        //     steps {
        //         build job: 'JobForJenkinsfile3', wait: true
        //     }
        // }

        stage('Convert XML to PDF') {
            steps {
                sh '''
                    docker run --rm -v $(pwd)/workspace:/workspace pandoc/core pandoc /workspace/generated.xml -o /workspace/output.pdf
                    cp /workspace/output.pdf ./output.pdf
                '''
            }
        }

        stage('Stop Services') {
            steps {
                sleep(time: 10, unit: 'MINUTES')
                // Si es necesario detener contenedores, puedes agregar los comandos aquí
                // sh 'docker-compose down' (si necesitas detener los servicios)
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

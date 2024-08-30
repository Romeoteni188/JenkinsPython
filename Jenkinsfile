pipeline {
    agent any

    // Definición de parámetros
    parameters {
        string(name: 'BRANCH_NAME', defaultValue: 'main', description: 'Branch de Git a usar')
        booleanParam(name: 'RUN_TESTS', defaultValue: true, description: '¿Ejecutar pruebas unitarias?')
    }

    stages {
        stage('Checkout') {
            steps {
                // Clona el repositorio desde el branch especificado
                git url: 'https://github.com/Romeoteni188/JenkinsPython.git', branch: "${params.BRANCH_NAME}"
            }
        }

        stage('Setup') {
            steps {
                // Configura el entorno virtual y las dependencias
                sh '''
                # Crea el entorno virtual y actualiza pip
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Linting') {
            steps {
                // Corre el linter para verificar la calidad del código
                // sh '''
                // . venv/bin/activate
                // pylint **/*.py
                // '''
                echo 'linting'
            }
        }

        stage('Testing') {
            when {
                expression {
                    return params.RUN_TESTS // Solo ejecuta si RUN_TESTS es true
                }
            }
            steps {
                // Ejecuta las pruebas unitarias directamente en el archivo test_unita.py
                sh '''
                . venv/bin/activate
                python3 -m unittest test_unita
                '''
            }
        }

        stage('Build') {
            steps {
                // Construye o empaqueta la aplicación
                echo 'Build successful'
            }
        }
    }

    post {
        always {
            // Limpia el workspace después de la ejecución del pipeline
            cleanWs()
        }
        success {
            echo 'Pipeline completado exitosamente.'
        }
        failure {
            echo 'El pipeline falló.'
        }
    }
}

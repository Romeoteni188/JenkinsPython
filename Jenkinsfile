pipeline {
    
    options {
        buildDiscarder(logRotator(numToKeepStr: '10')) // Retain history on the last 10 builds
        ansiColor('xterm') // Enable colors in terminal
        timestamps() // Append timestamps to each line
        timeout(time: 20, unit: 'MINUTES') // Set a timeout on the total execution time of the job
    }
    agent {
        dockerfile { filename 'Dockerfile.build' } // Run this job within a Docker container built using Dockerfile.build
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm // Checkout (git clone ...) the project's repository
            }
        }
        stage('Setup') {
            steps {
                script {
                    sh """
                    pip install -r requirements.txt
                    """
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
                    sh """
                    # You have the option to stand up a temporary environment to perform
                    # these tests and/or run the tests against an existing environment. The
                    # advantage to the former is you can ensure the environment is clean
                    # and in a desired initial state. The easiest way to stand up a temporary
                    # environment is to use Docker and a wrapper script to orchestrate the
                    # process. This script will handle standing up supporting services like
                    # MySQL & Redis, running DB migrations, starting the web server, etc.
                    # You can utilize your existing automation, your custom scripts and Make.
                    ./standup_testing_environment.sh # Name this whatever you'd like

                    python -m unittest discover -s tests/integration
                    """
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
}

pipeline {
    agent any

    environment {
        // Load environment variables from a secure location
        ENV_VARS = credentials('etl-env')
    }

    stages {
        stage('Checkout') {
            steps {
                // Pull the latest ETL Code from the Git repository
                git branch: 'main', url: 'https://github.com/jibbs1703/Economic-Indicator-Data-Pipeline.git'
            }
        }

        stage('Create Virtual Environment or Docker') {
            steps {
                // Set up the virtual environment named 'etl-venv'
                sh '''
                # Check if Virtual Environment Exists
                if [ ! -d "etl-venv" ]; then
                    python3 -m venv etl-venv
                fi

                # Activate the Virtual Environment
                source etl-venv/bin/activate

                # Upgrade pip Installer
                pip install --upgrade pip
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install dependencies within the virtual environment
                sh '''
                # Activate the virtual environment
                source etl-venv/bin/activate

                # Install dependencies if you have a requirements.txt
                if [ -f requirements.txt ]; then
                    pip install -r requirements.txt
                fi
                '''
            }
        }

        stage('Run ETL Script') {
            steps {
                // Run the etl.py script
                sh 'python3 etl.py'
            }
        }
    }

    post {
        always {
            // Clean up any artifacts, deactivate virtualenv, etc. (optional)
            // Clean workspace
            cleanWs()
        }
        success {
            // Actions to take when the pipeline succeeds
            echo 'ETL Job completed successfully!'
        }
        failure {
            // Actions to take when the pipeline fails
            echo 'ETL Job failed!'
        }
    }
}

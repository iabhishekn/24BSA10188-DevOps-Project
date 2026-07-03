pipeline {
    agent any

    environment {
        IMAGE_NAME = "${env.DOCKERHUB_REPO ?: 'abc-technologies/corporate-website'}"
        IMAGE_TAG = "${env.BUILD_NUMBER ?: 'local'}"
        CONTAINER_NAME = "abc-technologies-site"
        APP_PORT = "8080"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Static File Validation') {
            steps {
                sh '''
                    test -f index.html
                    test -f about.html
                    test -f services.html
                    test -f careers.html
                    test -f contact.html
                    test -f gallery.html
                    test -f assets/css/styles.css
                    test -f assets/js/main.js
                '''
            }
        }

        stage('Maven Package') {
            steps {
                sh 'mvn -q -DskipTests package'
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t $IMAGE_NAME:$IMAGE_TAG -t $IMAGE_NAME:latest .'
            }
        }

        stage('Container Smoke Test') {
            steps {
                sh '''
                    docker rm -f $CONTAINER_NAME || true
                    docker run -d --name $CONTAINER_NAME -p $APP_PORT:80 $IMAGE_NAME:$IMAGE_TAG
                    sleep 5
                    curl -fsS http://localhost:$APP_PORT/
                    curl -fsS http://localhost:$APP_PORT/services.html
                '''
            }
            post {
                always {
                    sh 'docker ps --filter name=$CONTAINER_NAME'
                }
            }
        }

        stage('Docker Push') {
            when {
                expression { return env.PUSH_IMAGE == 'true' }
            }
            steps {
                sh '''
                    docker push $IMAGE_NAME:$IMAGE_TAG
                    docker push $IMAGE_NAME:latest
                '''
            }
        }

        stage('Kubernetes Deploy') {
            when {
                expression { return env.DEPLOY_K8S == 'true' }
            }
            steps {
                sh '''
                    kubectl apply -f k8s/deployment.yaml
                    kubectl apply -f k8s/service.yaml
                    kubectl rollout status deployment/abc-technologies-website
                    kubectl get pods,svc -l app=abc-technologies-website
                '''
            }
        }
    }

    post {
        success {
            echo 'ABC Technologies website pipeline completed successfully.'
        }
        always {
            archiveArtifacts artifacts: 'target/*.jar, k8s/*.yaml, monitoring/**/*.yml, monitoring/**/*.json, monitoring/**/*.cfg', allowEmptyArchive: true
        }
    }
}

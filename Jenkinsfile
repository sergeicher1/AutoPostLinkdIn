pipeline{
    agent any
    stages{
    stage('version'){
    steps{
    sh 'python3 --version'
    }
    }
        stage('run cv'){
          steps{
            sh 'python3 AutomationPostsLinkedIn/job_karov_cv_runner.py'
          }
        }
    }
}
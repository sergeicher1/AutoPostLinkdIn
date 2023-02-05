pipeline{
    agent any
    stages{
    stage('version'){
    steps{
    sh 'pyhon --version'
    }
    }
        stage('run cv'){
          steps{
            sh 'python job_karov_cv_runner.py'
          }
        }
    }
}
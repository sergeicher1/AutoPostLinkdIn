pipeline{
    agent any
    stages{
    stage('version'){
    steps{
    sh 'pyhon3 --version'
    }
    }
        stage('run cv'){
          steps{
            sh 'python3 job_karov_cv_runner.py'
          }
        }
    }
}
pipeline {
  agent {
    dockerfile {
      filename 'Dockerfile'
    }

  }
  stages {
    stage('') {
      steps {
        echo 'my first step'
      }
    }
    stage('stage') {
      parallel {
        stage('stage') {
          steps {
            sh '''echo "saidatta"
'''
          }
        }
        stage('') {
          steps {
            timestamps() {
              echo 'this is my second foot print'
            }

          }
        }
      }
    }
  }
}
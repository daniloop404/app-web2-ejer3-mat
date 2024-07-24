node {
    stage('Revisión'){
        checkout scm
    }

    stage ('Instalación de dependencias'){
        bat 'npm install'
    }

    stage('Construir'){
        bat 'npm run ng build'
    }

}
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

    stage('Mover al servidor'){
        bat 'xcopy  C:\\ProgramData\\Jenkins\\.jenkins\\workspace\\angular-pipeline\\dist\\app-03\\browser  C:\\servidor\\fire /E'
    }

}
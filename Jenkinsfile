@Library('sfdi-devops-tools-infra') _

pipeline {
    agent any
    
    stages{
        stage ("Deploy to Unix"){
          steps{
             //wrap([$class: 'BuildUser']) {
                //GET_BUILD_USER = sh ( script: 'echo "${BUILD_USER}"', returnStdout: true).trim()
                echo "build user : ${env.BUILD_USER}"
                echo "get build user id : ${env.BUILD_USER_ID}"
                echo "get user id : ${env.USER}"
              
            //}
                }
        }
        }
        

}				
        
    

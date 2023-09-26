@Library('sfdi-devops-tools-infra') _

pipeline {
    agent any
    
    stages{
        stage ("Deploy to Unix"){
          steps{
             //wrap([$class: 'BuildUser']) {
                //GET_BUILD_USER = sh ( script: 'echo "${BUILD_USER}"', returnStdout: true).trim()
                echo "current build : ${currentBuild.buildUser}"
                def buildUser = currentBuild.rawBuild.getCause(hudson.model.Cause$UserIdCause).getUserName()                     
                echo "Build triggered by user: ${buildUser}"
                //echo "get build user id : ${env.BUILD_USER_ID}"
                //echo "get user id : ${env.USER}"
              
            //}
                }
        }
        }
        

}				
        
    

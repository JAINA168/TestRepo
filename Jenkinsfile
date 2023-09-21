@Library('sfdi-devops-tools-infra') _

pipeline {
    agent any
    
    stages{
        stage ("Deploy to Unix"){
             wrap([$class: 'BuildUser']) {
                GET_BUILD_USER = sh ( script: 'echo "${BUILD_USER}"', returnStdout: true).trim()
            }
                }
        }
        
    post {
        failure {
            notification_email(Email_Alert: Email_Alert, Notify_to: Notify_to) 
        }
        success {
            notification_email(Email_Alert: Email_Alert, Notify_to: Notify_to)
        }
    }
}				
        
    

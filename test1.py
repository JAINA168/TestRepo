#!/usr/bin/env groovy
import java.text.SimpleDateFormat
import java.util.Date
import java.util.UUID

def call(Map config){
    if ((env.BRANCH_NAME != 'dev') || (config.Email_Alert == 'Yes')){
        sub = " $currentBuild.result - $currentBuild.fullProjectName Jenkins Job"
        //recp = config.Notify_to
        def requestId = generateRequestID()
        recp = 'cc:$DEFAULT_RECIPIENTS,' + config.Notify_to
        msg = """

            The Jenkins Deployment Job $env.JOB_NAME is $currentBuild.result
            
            **************************************
            For Build Output, Please visit below link
            Build URL: $env.BUILD_URL
            Build Result: $currentBuild.result
            Github URL: $env.GIT_URL
            Github Branch: $env.BRANCH_NAME
            Deployment Request Id: $requestId
            ***************************************

            For further queries - Please reach out to DL-SFADevOps@pfizer.com

            Thanks,
            SFA DevOps Team

        """
        emailext attachLog: true, body: "$msg", 
                recipientProviders: [requestor()], 
                replyTo: 'DL-SFADevOps@pfizer.com', 
                subject: "$sub",
                to: "$recp"
        println """
            Build Number: $env.BUILD_NUMBER
            Branch Name: $env.BRANCH_NAME
            JOB URL: $env.JOB_DISPLAY_URL
            BUILD_NUMBER: $env.BUILD_NUMBER
            Build ID: $env.BUILD_ID
            JOB_NAME: $env.JOB_NAME
            Build_Status: $currentBuild.result
            Project Name: $currentBuild.fullProjectName
            """

    }
}

// Generate unique request ID with prefix "DR"
def generateRequestID() {
    def prefix = "DR"
    def timestamp = new Date().time
    def uniqueID = UUID.randomUUID().toString().replaceAll("-", "").substring(0, 2) // Truncate to 2 characters
    def requestID = "${prefix}${formatTimestamp(timestamp)}${uniqueID}"
    return requestID
}

// Format timestamp as yyyyMMddHHmmss
def formatTimestamp(timestamp) {
    def format = new SimpleDateFormat("yyyyMMddHHmm")
    return format.format(new Date(timestamp))
}

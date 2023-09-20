#!/usr/bin/env groovy
import java.text.SimpleDateFormat
import java.util.Date
import java.util.UUID

def call(Map config){
    if ((env.BRANCH_NAME != 'dev') || (config.Email_Alert == 'Yes')){
        
        //recp = config.Notify_to
        def requestId = generateRequestID()
        def projectNameSegments = currentBuild.fullProjectName.split('/')
        def environment = projectNameSegments[-1]
        def project = projectNameSegments[-3:-2]
        def pod_name = projectNameSegments[-2]
        def initiator = env.BUILD_TRIGGER_BY
        sub = " '$pod_name' in environment '$environment'- $currentBuild.result "
        recp = 'cc:$DEFAULT_RECIPIENTS,' + config.Notify_to
        msg = """
            <html>
            <body style="font-family: Arial, sans-serif; background-color: #f4f4f4; padding: 20px;">
              <div style="background-color: #fff; padding: 20px; border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.1);">
                <h3 style="color: #007bff;">The Jenkins Deployment Job $env.JOB_NAME is $currentBuild.result</h3>
                <h3>Pod Name: $pod_name</h3>
                <h3>Job Parameters:</h3>
                <table border="1">
                    <tr>
                        <th>Parameter Name</th>
                        <th>Value</th>
                    </tr>
                    ${getParametersTable()}
                </table>
                <hr/>
                
                <h3>Build Information:</h3>
                <table border="1">
                    <tr>
                        <th>Information</th>
                        <th>Value</th>
                    </tr>
                    <tr>
                        <td>Build URL</td>
                        <td><a href="$env.BUILD_URL">$env.BUILD_URL</a></td>
                    </tr>
                    <tr>
                        <td>Build Result</td>
                        <td>$currentBuild.result</td>
                    </tr>
                    <tr>
                        <td>Github URL</td>
                        <td><a href="$env.GIT_URL">$env.GIT_URL</a></td>
                    </tr>
                    <tr>
                        <td>Github Branch</td>
                        <td>$env.BRANCH_NAME</td>
                    </tr>
                    <tr>
                        <td>Deployment Requested By</td>
                        <td>$initiator</td>
                    </tr>
                    <tr>
                        <td>Deployment Request Id</td>
                        <td>$requestId</td>
                    </tr>
                </table>
                
                <hr/>
                
                <hr/>
                
                <hr/>
                <p>
                    For further queries, please reach out to <a href='mailto:DL-SFADevOps@pfizer.com'>DL-SFADevOps@pfizer.com</a>.
                </p>
                
                <p>
                    Thanks,<br/>
                    SFA DevOps Team
                </p>
              </div>  
            </body>
            </html>
        """
        
        emailext attachLog: true, body: "$msg", 
                recipientProviders: [requestor()], 
                replyTo: 'DL-SFADevOps@pfizer.com', 
                subject: "$sub",
                to: "$recp",
                contentType: 'text/HTML'
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
def getParametersTable() {
    def parameterTable = ""
    params.keySet().each { paramName ->
        parameterTable += """
            <tr>
                <td>$paramName</td>
                <td>${params[paramName]}</td>
            </tr>
        """
    }
    return parameterTable
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

#!/usr/bin/env groovy
import java.text.SimpleDateFormat
import java.util.Date
import java.util.UUID

def call(Map config){
    if ((env.BRANCH_NAME != 'dev') || (config.Email_Alert == 'Yes')){
        sub = " $currentBuild.result - $currentBuild.fullProjectName Jenkins Job"
        //recp = config.Notify_to
        def requestId = generateRequestID()
        def projectNameSegments = currentBuild.fullProjectName.split('/')
        def pod_name = projectNameSegments[-2]
        def initiator = env.USER 
        recp = 'cc:$DEFAULT_RECIPIENTS,' + config.Notify_to
        msg = """
            <html>
            <body style="font-family: Arial, sans-serif; background-color: #f4f4f4; padding: 20px;">
              <div style="background-color: #fff; padding: 20px; border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.1);">
                <h2 style="color: #007bff;">The Jenkins Deployment Job $env.JOB_NAME is $currentBuild.result</h2>
                
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

                <h3>Pod Name: $pod_name</h3>
                <h3>Job Parameters:</h3>
                <table border="1">
                    <tr>
                        <th>Parameter Name</th>
                        <th>Value</th>
                    </tr>
                    <tr>
                        <td>Deploy_to_PostgreSQL</td>
                        <td>${params.Deploy_to_PostgreSQL}</td>
                    </tr>
                    <tr>
                        <td>Deploy_to_Unix</td>
                        <td>${params.Deploy_to_Unix}</td>
                    </tr>
                    <tr>
                        <td>Deploy_to_Autosys</td>
                        <td>${params.Deploy_to_Autosys}</td>
                    </tr>
                    <tr>
                        <td>dry_run</td>
                        <td>${params.dry_run}</td>
                    </tr>
                    <tr>
                        <td>Email_Alert</td>
                        <td>${params.Email_Alert}</td>
                    </tr>
                    <tr>
                        <td>Notify_to</td>
                        <td>${params.Notify_to}</td>
                    </tr>
                </table>
                
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

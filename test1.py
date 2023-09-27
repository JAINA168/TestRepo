 <html>
            <body style="font-family: Arial, sans-serif; background-color: #fff; padding: 20px;">
              <div style="background-color: #fff; padding: 20px; border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.1);">
                <h3 style="color: #007bff;">The Jenkins Deployment Job $env.JOB_NAME is $currentBuild.result</h3>
                <h3>Pod Name: $pod_name</h3>
                <h3>Job Parameters:</h3>
                <table border="1" cellpadding="5" cellspacing="0" style="background-color: #e6f3fa; border-collapse: collapse; max-width: 600px; width: 50%;">
                    <tr>
                        <th style="width: 150px;">Parameter Name</th>
                        <th>Value</th>
                    </tr>
                    ${getParametersTable()}
                </table>
                <hr/>
                
                <h3>Build Information:</h3>
                <table border="1" cellpadding="5" cellspacing="0" style="background-color: #e6f3fa; border-collapse: collapse; max-width: 600px; width: 100%;">
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
                        <td>Deployment Request Id</td>
                        <td>$requestId</td>
                    </tr>
                </table>
                
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

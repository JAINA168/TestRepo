        msg = """
            <html>
            <body>
                <h2>The Jenkins Deployment Job $env.JOB_NAME is $currentBuild.result</h2>
                
                <hr/>
                
                <h3>Build Information:</h3>
                <ul>
                    <li>Build URL: <a href='$env.BUILD_URL'>$env.BUILD_URL</a></li>
                    <li>Build Result: $currentBuild.result</li>
                    <li>Github URL: <a href='$env.GIT_URL'>$env.GIT_URL</a></li>
                    <li>Github Branch: $env.BRANCH_NAME</li>
                    <li>Deployment Request Id: $requestId</li>
                </ul>
                
                <hr/>
                
                <h3>Job Parameters:</h3>
                <ul>
                    <li>Deploy_to_PostgreSQL: ${params.Deploy_to_PostgreSQL}</li>
                    <li>Deploy_to_Unix: ${params.Deploy_to_Unix}</li>
                    <li>Deploy_to_Autosys: ${params.Deploy_to_Autosys}</li>
                    <li>dry_run: ${params.dry_run}</li>
                    <li>Email_Alert: ${params.Email_Alert}</li>
                    <li>Notify_to: ${params.Notify_to}</li>
                </ul>
                
                <hr/>
                
                <h3>Technology: $technology</h3>
                <h3>Pod Name: ${params.PodName}</h3>
                
                <hr/>
                
                <p>
                    For further queries, please reach out to <a href='mailto:DL-SFADevOps@pfizer.com'>DL-SFADevOps@pfizer.com</a>.
                </p>
                
                <p>
                    Thanks,<br/>
                    SFA DevOps Team
                </p>
            </body>
            </html>
        """

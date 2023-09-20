            <html>
            <body style="font-family: Arial, sans-serif; background-color: #f4f4f4; padding: 20px;">
              <div style="background-color: #fff; padding: 20px; border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.1);">
                <h2 style="color: #007bff;">The Jenkins Deployment Job $env.JOB_NAME is $currentBuild.result</h2>
                
                <hr/>
                
                <h3>Build Information:</h3>
                <table border="1" style="background-color: #ffffff; border-collapse: collapse; width: 100%;">
                    <!-- ... (previous rows) ... -->
                </table>
                
                <hr/>

                <h3 style="background-color: #ffffff;">Pod Name: $pod_name</h3>
                <h3>Job Parameters:</h3>
                <table border="1" style="background-color: #ffffff; border-collapse: collapse; width: 100%;">
                    <!-- ... (previous rows) ... -->
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

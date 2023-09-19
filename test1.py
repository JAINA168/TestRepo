            <html>
            <body>
                <h2>The Jenkins Deployment Job $env.JOB_NAME is $currentBuild.result</h2>
                
                <hr/>
                
                <h3>Build Information:</h3>
                <ul>
                    <!-- Build Information List -->
                </ul>
                
                <hr/>
                
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
                    <!-- Add more parameters as needed -->
                </table>
                
                <hr/>
                
                <!-- Add the rest of your content here -->
                
            </body>
            </html>
        """
        

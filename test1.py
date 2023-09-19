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
                        <td>Deployment Request Id</td>
                        <td>$requestId</td>
                    </tr>
                </table>
                
                <hr/>

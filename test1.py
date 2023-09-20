            <h3>Job Parameters:</h3>
            <table border="1">
                <tr>
                    <th>Parameter Name</th>
                    <th>Value</th>
                </tr>
                ${getParametersTable()}
            </table>

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

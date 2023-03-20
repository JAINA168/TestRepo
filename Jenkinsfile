@Library('sfdi-devops-tools-infra') _

pipeline {
    agent any
    environment {
        //unix server details
        unix_server = "${getProperty("${env.BRANCH_NAME}_repl_unix_server")}"
        unix_src_path1 = "unix/scripts"
        unix_dest_path1 = "/app/etl/repl/scripts"
        unix_src_path2 = "unix/parameter_files"
        unix_dest_path2 = "/app/etl/repl/parameter_files"
        unix_service_account = "srvamr-sfaops"
        //snowflake changelog file details
        snowflake_changeLogFile_COMETL_CONTROL_db = "snowflake/COMETL_CONTROL/changelog.sf.xml"
        snowflake_changeLogFile_COMM_APAC_VVA_db = "snowflake/COMM_APAC_VVA/changelog.sf.xml"
        snowflake_changeLogFile_COMM_EU_VVA_db = "snowflake/COMM_EU_VVA/changelog.sf.xml"
        snowflake_changeLogFile_COMM_US_VVA_db = "snowflake/COMM_US_VVA/changelog.sf.xml"
        //snowflake db connection details
        snowflake_COMETL_CONTROL_db_url = "${getProperty("${env.BRANCH_NAME}_repl_snowflake_COMETL_CONTROL_db_url")}"
        snowflake_COMM_APAC_VVA_db_url = "${getProperty("${env.BRANCH_NAME}_repl_snowflake_COMM_APAC_VVA_db_url")}"
        snowflake_COMM_EU_VVA_db_url = "${getProperty("${env.BRANCH_NAME}_repl_snowflake_COMM_EU_VVA_db_url")}"
        snowflake_COMM_US_VVA_db_url = "${getProperty("${env.BRANCH_NAME}_repl_snowflake_COMM_US_VVA_db_url")}"
        //snowflake credentials
        cometl_control_snowflake_credid = "${env.BRANCH_NAME}_repl_snowflake_credid_ctl"
        comm_apac_vva_snowflake_credid = "${env.BRANCH_NAME}_repl_snowflake_credid_apac"
        comm_eu_vva_snowflake_credid = "${env.BRANCH_NAME}_repl_snowflake_credid_eu"
        comm_us_vva_snowflake_credid = "${env.BRANCH_NAME}_repl_snowflake_credid_us"
    }
    parameters {
        choice choices: ['No', 'Yes'], description: 'Mention if You want to Deploy into Unix Environment', name: 'Deploy_to_Unix'
        choice choices: ['No', 'Yes'], description: 'Mention if You want to Deploy into Snowflake Environment', name: 'Deploy_to_Snowflake_COMETL_CONTROL'
        choice choices: ['No', 'Yes'], description: 'Mention if You want to Deploy into Snowflake Environment', name: 'Deploy_to_Snowflake_COMM_APAC_VVA'
        choice choices: ['No', 'Yes'], description: 'Mention if You want to Deploy into Snowflake Environment', name: 'Deploy_to_Snowflake_COMM_EU_VVA'
        choice choices: ['No', 'Yes'], description: 'Mention if You want to Deploy into Snowflake Environment', name: 'Deploy_to_Snowflake_COMM_US_VVA'
        choice choices: ['No', 'Yes'], description: 'Mention if You Alert via Email', name: 'Email_Alert'
        choice choices: ['Yes', 'No'], description: 'Mention if You want to execute a Dry Run', name: 'dry_run'
        string  defaultValue: 'None', description: 'Provide the comma separated Email addresses.', name: 'Notify_to'
    }
    stages{
        stage("Approval for Prod"){
            when {
                expression { "${env.BRANCH_NAME}" == "main" }
            }
            steps{
                script{
                    email_approval()
                }
            }
        }
        stage ("Deploy to Unix"){
            when {
                 expression { params.Deploy_to_Unix == "Yes" }
            }
                steps{
                    script{
                        def unix_permission = '775'
                        if (env.BRANCH_NAME == 'main'){
                            unix_permission = '755'
                        }
                        //scripts files deployment 
                        unix_deploy(src: unix_src_path1, dest: unix_dest_path1, server: unix_server, service_account: unix_service_account, permissions: unix_permission)
                        unix_deploy(src: unix_src_path2, dest: unix_dest_path2, server: unix_server, service_account: unix_service_account, permissions: unix_permission)
                        
                        //Adhoc commands for file permissions
                        // Add the code if needed.
                        }
                }
        }
        stage ("Deploy to Snowflake Datbase - COMETL_CONTROL"){
            when {
                 expression { params.Deploy_to_Snowflake_COMETL_CONTROL == "Yes" }
            }
                steps{
                    script{
                        println "Deploying into COMETL_CONTROL ${env.BRANCH_NAME} environment"
                        snowflake_deploy(url: snowflake_COMETL_CONTROL_db_url, cred: cometl_control_snowflake_credid, changelog: snowflake_changeLogFile_COMETL_CONTROL_db, dry_run: dry_run) 
                        }
                }
        }
        stage ("Deploy to Snowflake Datbase - COMM_APAC_VVA"){
            when {
                 expression { params.Deploy_to_Snowflake_COMM_APAC_VVA == "Yes" }
            }
                steps{
                    script{
                        println "Deploying into COMM_APAC_VVA ${env.BRANCH_NAME} environment"
                        snowflake_deploy(url: snowflake_COMM_APAC_VVA_db_url, cred: comm_apac_vva_snowflake_credid, changelog: snowflake_changeLogFile_COMM_APAC_VVA_db, dry_run: dry_run)
                        }
                }
        }
        stage ("Deploy to Snowflake Datbase - COMM_EU_VVA"){
            when {
                 expression { params.Deploy_to_Snowflake_COMM_EU_VVA == "Yes" }
            }
                steps{
                    script{
                        println "Deploying into COMM_EU_VVA ${env.BRANCH_NAME} environment"
                        snowflake_deploy(url: snowflake_COMM_EU_VVA_db_url, cred: comm_eu_vva_snowflake_credid, changelog: snowflake_changeLogFile_COMM_EU_VVA_db, dry_run: dry_run)
                        }
                }
        }
        stage ("Deploy to Snowflake Datbase - COMM_US_VVA"){
            when {
                 expression { params.Deploy_to_Snowflake_COMM_US_VVA == "Yes" }
            }
                steps{
                    script{
                        println "Deploying into COMM_US_VVA ${env.BRANCH_NAME} environment"
                        snowflake_deploy(url: snowflake_COMM_US_VVA_db_url, cred: comm_us_vva_snowflake_credid, changelog: snowflake_changeLogFile_COMM_US_VVA_db, dry_run: dry_run)
                        }
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

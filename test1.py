stage ("Deploy to Unix"){
            when {
                 expression { params.Deploy_to_Unix == "Yes" }
            }
                steps{
                    script{
                        unix_deploy(src: unix_src_path_scripts, dest: unix_deploy_path_scripts, server: unix_server, service_account: unix_service_account, permissions: unix_permission)
                        unix_deploy(src: unix_src_path_params, dest: unix_deploy_path_params, server: unix_server, service_account: unix_service_account, permissions: unix_permission)
                        unix_deploy(src: unix_src_path_scripts_ui, dest: unix_deploy_path_scripts_ui, server: unix_server, service_account: unix_service_account, permissions: unix_permission)
                        }
                }
        }


#!/usr/bin/env groovy

def call(Map config) {
    println "Deploying code into Unix environment"
    // withCredentials([usernamePassword(credentialsId: "${var1}", passwordVariable: 'PASS', usernameVariable: 'USER')]) {
    //     println USER
    //     println PASS
    // }
    println config.src
    println config.dest
    println config.server
    println config.service_account
    println config.permissions
    //println config.group
    //println config.owner
    sh "ls"
    if(config.service_account == 'srvamr-palign@amer'){
        priv_key_path = '/var/lib/jenkins/.ssh/palign_id_rsa'
    }else{
        priv_key_path = '/var/lib/jenkins/.ssh/id_rsa'
    }
    sh "scp -i ${priv_key_path} -r ${config.src}/* ${config.service_account}@${config.server}:${config.dest}"
    // Set Permissions of the destination files
    sh "ssh -i ${priv_key_path} ${config.service_account}@${config.server} 'sudo chmod ${config.permissions} ${config.dest}/*'"
    //Set the owner and file permissions inside a folder
    // sh "ssh ${config.service_account}@${config.server} 'chown ${config.owner}:${config.group} ${config.dest}/*'"
}

#!/usr/bin/env groovy

def deployToUnix(Map config) {
    println "Deploying code into Unix environment"
    println config.src
    println config.dest
    println config.server
    println config.service_account
    println config.permissions
    
    if (config.dry_run == 'Yes') {
        // Check if dry_run is 'Yes'
        sh "ls ${config.src}" // List files inside config.src
        return // Exit the script
    }
    
    // Continue with deployment operations if dry_run is 'No'
    sh "ls"    
    if (config.service_account == 'srvamr-palign@amer') {
        priv_key_path = '/var/lib/jenkins/.ssh/palign_id_rsa'
    } else {
        priv_key_path = '/var/lib/jenkins/.ssh/id_rsa'
    }
    
    sh "scp -i ${priv_key_path} -r ${config.src}/* ${config.service_account}@${config.server}:${config.dest}"
    
    // Set Permissions of the destination files
    sh "ssh -i ${priv_key_path} ${config.service_account}@${config.server} 'sudo chmod ${config.permissions} ${config.dest}/*'"
    
    // Set the owner and file permissions inside a folder (if needed)
    // sh "ssh ${config.service_account}@${config.server} 'chown ${config.owner}:${config.group} ${config.dest}/*'"
}
